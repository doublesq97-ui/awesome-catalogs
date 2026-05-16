from __future__ import annotations

import json
import re
from pathlib import Path

from .models import CATEGORY_TARGETS, RepoInfo


SCRIPT_SUFFIXES = {".sh", ".py", ".js", ".rb"}
README_NAMES = ("README.md", "README.MD", "readme.md", "Readme.md")


def classify_repo(path: Path, source: str | None = None) -> RepoInfo:
    path = path.resolve()
    name = safe_name(path.name)
    readme = read_readme(path)
    summary = extract_summary(readme, fallback="No description available")
    category = detect_category(path, readme)
    domain = assign_domain(readme + "\n" + name)
    target_root = CATEGORY_TARGETS[category]
    target_dir = target_root / name
    return RepoInfo(
        name=name,
        source=source or str(path),
        path=path,
        category=category,
        summary=summary,
        domain=domain,
        target_dir=target_dir,
        already_installed=target_dir.exists(),
    )


def detect_category(path: Path, readme: str) -> str:
    if (path / "SKILL.md").exists():
        return "skill"

    if is_plugin(path, readme):
        return "plugin"

    if has_cli_entry(path):
        return "tool"

    if is_single_script_repo(path):
        return "script"

    return "software"


def is_plugin(path: Path, readme: str) -> bool:
    plugin_markers = (
        "mcp.json",
        "plugin.json",
        ".codex-plugin/plugin.json",
        "claude-plugin.json",
    )
    return any((path / marker).exists() for marker in plugin_markers)


def is_single_script_repo(path: Path) -> bool:
    files = [p for p in path.iterdir() if p.is_file() and not p.name.startswith(".")]
    script_files = [p for p in files if p.suffix in SCRIPT_SUFFIXES]
    build_files = {"package.json", "Cargo.toml", "go.mod", "pyproject.toml"}
    return len(script_files) == 1 and not any((path / name).exists() for name in build_files)


def has_cli_entry(path: Path) -> bool:
    if (path / "bin").is_dir() or (path / "cmd").is_dir():
        return True
    if (path / "main.go").exists() or (path / "cli.py").exists() or (path / "src/cli.js").exists():
        return True

    package_json = path / "package.json"
    if package_json.exists():
        try:
            data = json.loads(package_json.read_text(encoding="utf-8"))
            if data.get("bin"):
                return True
            scripts = data.get("scripts", {})
            if any(key in scripts for key in ("cli", "start")):
                return True
        except json.JSONDecodeError:
            pass

    return False


def read_readme(path: Path) -> str:
    for name in README_NAMES:
        candidate = path / name
        if candidate.exists():
            return candidate.read_text(encoding="utf-8", errors="replace")
    return ""


def extract_summary(readme: str, fallback: str) -> str:
    cleaned = re.sub(r"<!--.*?-->", "", readme, flags=re.DOTALL)
    lines = [line.strip() for line in cleaned.splitlines()]
    title: str | None = None
    for line in lines:
        if not line or line.startswith(("!", "[!", "<h", "<a ", "<div", "<p ", "<img", "<br", "<table")):
            continue
        if line.startswith("#"):
            title = re.sub(r"^#+\s*", "", line).strip() or title
            continue
        if set(line) <= {"-", "=", "_"}:
            continue
        text = re.sub(r"^>\s*", "", line)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        if re.match(r"^[a-zA-Z0-9._-]+\s*\|\s*", text):
            continue
        if re.match(r"^https?://", text):
            continue
        if len(text) < 15:
            continue
        return truncate(text, 120)
    return title or fallback


def assign_domain(text: str) -> str:
    lower = text.lower()
    rules = [
        ("AI/Automation", ("n8n", "workflow", "agent", "automation", "ai ")),
        ("Dev Tools", ("cli", "git", "devops", "build", "docker", "kubernetes")),
        ("Design", ("ui", "ux", "logo", "banner", "color", "design")),
        ("Content", ("blog", "seo", "writing", "markdown", "content")),
        ("Social Media", ("redbook", "wechat", "twitter", "xiaohongshu", "social")),
        ("Data", ("scrape", "crawl", "analytics", "visualization", "data")),
        ("Knowledge Mgmt", ("obsidian", "note", "wiki", "pkm", "knowledge")),
        ("Video/Image", ("video", "image", "subtitle", "edit", "ffmpeg")),
        ("Audio", ("tts", "audio", "music", "podcast", "voice")),
        ("Image Gen", ("stable-diffusion", "dalle", "image-generation", "midjourney")),
        ("Prompt Eng", ("prompt", "prompt-engineering")),
        ("Esoteric", ("bazi", "astrology", "tarot", "divination", "fortune")),
    ]
    for domain, keywords in rules:
        if any(keyword in lower for keyword in keywords):
            return domain
    return "Other"


def safe_name(name: str) -> str:
    name = name.removesuffix(".git")
    cleaned = "".join(char if char.isalnum() or char in "._-" else "-" for char in name)
    return re.sub(r"-{2,}", "-", cleaned).strip("-._") or "repo"


def truncate(text: str, limit: int) -> str:
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."

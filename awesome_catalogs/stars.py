from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone

from .catalog import find_duplicate_source
from .classifier import assign_domain, extract_summary


@dataclass
class StarInfo:
    name: str
    full_name: str
    html_url: str
    description: str
    language: str
    topics: list[str]
    stars: int
    pushed_at: str
    status: str  # recommend | installed | skip | warn
    domain: str
    reason: str = ""
    readme_summary: str = ""


def fetch_stars(username: str) -> list[dict]:
    cmd = ["gh", "api", f"users/{username}/starred", "--paginate", "--jq", "."]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"gh api failed: {result.stderr.strip()}")
    if not result.stdout.strip():
        return []
    return json.loads(result.stdout)


def fetch_readme(full_name: str, default_branch: str = "main") -> str:
    for branch in (default_branch, "main", "master"):
        url = f"https://raw.githubusercontent.com/{full_name}/{branch}/README.md"
        try:
            result = subprocess.run(
                ["curl", "-sL", "--max-time", "8", url],
                capture_output=True, text=True,
            )
            if result.returncode == 0 and result.stdout.strip() and "404: Not Found" not in result.stdout:
                content = result.stdout
                if len(content) > 6000:
                    content = content[:6000]
                return content
        except Exception:
            pass
    return ""


def classify_star(repo: dict) -> StarInfo:
    name = repo["name"]
    full_name = repo["full_name"]
    html_url = repo["html_url"]
    description = (repo.get("description") or "").strip()
    language = repo.get("language") or ""
    topics: list[str] = repo.get("topics") or []
    pushed_at = repo.get("pushed_at", "")
    default_branch = repo.get("default_branch", "main")

    text = f"{description} {' '.join(topics)} {language} {name}"
    domain = assign_domain(text)

    status, reason = decide_status(full_name, html_url, description, topics, pushed_at)

    readme_summary = ""
    if status in ("recommend", "warn"):
        readme = fetch_readme(full_name, default_branch=default_branch)
        if readme:
            readme_summary = extract_summary(readme, fallback=description)
        if not readme_summary:
            readme_summary = description

    return StarInfo(
        name=name,
        full_name=full_name,
        html_url=html_url,
        description=description,
        language=language,
        topics=topics,
        stars=repo.get("stargazers_count", 0),
        pushed_at=pushed_at,
        status=status,
        domain=domain,
        reason=reason,
        readme_summary=readme_summary,
    )


def decide_status(
    full_name: str, html_url: str, description: str, topics: list[str], pushed_at: str
) -> tuple[str, str]:
    dupe = find_duplicate_source(html_url)
    if dupe:
        return "installed", f"已在 catalog: {dupe}"

    lower_desc = description.lower()
    lower_topics = " ".join(topics).lower()

    if any(kw in lower_topics for kw in ("awesome-list",)):
        return "skip", "Awesome list"

    edu_keywords = ("documentation", "tutorial", "cheatsheet", "docs", "course",
                    "education", "interview", "课程", "教程", "面试", "攻略", "笔记")
    if any(kw in lower_desc or kw in lower_topics for kw in edu_keywords):
        return "skip", "Documentation/tutorial"
    if any(kw in lower_topics for kw in ("library", "sdk", "api-client", "api-wrapper", "client-library")):
        return "skip", "Library/SDK"

    if pushed_at:
        try:
            pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            age = datetime.now(timezone.utc) - pushed
            if age.days > 1095:
                return "warn", f"{age.days // 365}y since last push"
        except (ValueError, TypeError):
            pass

    tool_kw = ("cli", "tool", "devtools", "developer-tools", "plugin", "mcp",
               "claude", "codex", "n8n", "automation", "workflow", "skill", "generator")
    if any(ind in lower_topics for ind in tool_kw):
        return "recommend", ""

    if description:
        return "recommend", ""

    return "skip", "No description"


STATUS_CN = {
    "recommend": "推荐",
    "installed": "已安装",
    "skip": "跳过",
    "warn": "警告",
}


def format_stars_table(items: list[StarInfo]) -> str:
    header = "| 状态 | 名称 | 简介 |\n| --- | --- | --- |\n"
    rows: list[str] = []
    for item in items:
        status_label = STATUS_CN.get(item.status, item.status)
        if item.reason:
            status_label += f"（{item.reason}）"
        summary = item.readme_summary or item.description
        if len(summary) > 100:
            summary = summary[:99].rstrip() + "..."
        summary = summary.replace("|", "\\|").replace("\n", " ")
        name = item.name.replace("|", "\\|")
        rows.append(f"| {status_label} | {name} | {summary} |")
    return header + "\n".join(rows)


def group_by_domain(items: list[StarInfo]) -> dict[str, list[StarInfo]]:
    groups: dict[str, list[StarInfo]] = {}
    for item in items:
        groups.setdefault(item.domain, []).append(item)
    return dict(sorted(groups.items()))


def count_by_status(items: list[StarInfo]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        counts[item.status] = counts.get(item.status, 0) + 1
    return counts


def run_stars_import(username: str, limit: int | None = None, show_skipped: bool = False) -> str:
    raw = fetch_stars(username)
    if not raw:
        return "No starred repos found."

    results = [classify_star(repo) for repo in raw]
    if limit:
        results = results[:limit]

    counts = count_by_status(results)
    by_domain = group_by_domain(results)

    lines: list[str] = []
    lines.append(f"# Stars: {username}（{len(results)} 個 repos）")
    lines.append("")
    lines.append("| 狀態 | 數量 |")
    lines.append("| --- | --- |")
    for status in ("recommend", "installed", "skip", "warn"):
        if counts.get(status):
            lines.append(f"| {STATUS_CN[status]} | {counts[status]} |")
    lines.append("")

    for domain, items in by_domain.items():
        visible = [i for i in items if show_skipped or i.status != "skip"]
        if not visible:
            continue
        lines.append(f"## {domain}")
        lines.append("")
        lines.append(format_stars_table(visible))
        lines.append("")

    return "\n".join(lines)

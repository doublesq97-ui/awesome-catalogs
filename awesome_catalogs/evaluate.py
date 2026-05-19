from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone

from .activity import calc_score, load_activity, score_bar
from .catalog import find_duplicate_source


def get_token() -> str:
    try:
        result = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    import os

    return os.environ.get("GITHUB_TOKEN", "")


def gh_api(endpoint: str) -> dict | list:
    token = get_token()
    cmd = ["gh", "api", endpoint, "--jq", "."]
    env = {}
    if token:
        env["GITHUB_TOKEN"] = token
    result = subprocess.run(cmd, capture_output=True, text=True, env={**__import__("os").environ, **env})
    if result.returncode != 0:
        raise RuntimeError(f"gh api {endpoint} failed: {result.stderr.strip()}")
    if not result.stdout.strip():
        return {}
    return json.loads(result.stdout)


def parse_github_url(url: str) -> tuple[str, str]:
    url = url.strip().rstrip("/").removesuffix(".git")
    for prefix in ("https://github.com/", "http://github.com/", "github.com/"):
        if prefix in url:
            path = url.split(prefix, 1)[1]
            parts = path.split("/")
            if len(parts) >= 2:
                return parts[0], parts[1]
    raise ValueError(f"Cannot parse GitHub URL: {url}")


def fetch_repo_meta(owner: str, repo: str) -> dict:
    data = gh_api(f"repos/{owner}/{repo}")
    if isinstance(data, list):
        return data[0] if data else {}
    return data


def fetch_releases(owner: str, repo: str) -> list[dict]:
    data = gh_api(f"repos/{owner}/{repo}/releases?per_page=3")
    if isinstance(data, list):
        return data
    return []


def fetch_readme_raw(owner: str, repo: str) -> str:
    for branch in ("main", "master"):
        try:
            result = subprocess.run(
                [
                    "curl", "-sL", "--max-time", "8",
                    f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md",
                ],
                capture_output=True, text=True,
            )
            if result.returncode == 0 and result.stdout.strip() and "404: Not Found" not in result.stdout:
                content = result.stdout
                if len(content) > 8000:
                    content = content[:8000]
                return content
        except Exception:
            pass
    return ""


# ---- 7 dimensions ----


def eval_popularity(meta: dict) -> tuple[str, str]:
    stars = meta.get("stargazers_count", 0)
    forks = meta.get("forks_count", 0)
    if stars >= 50000:
        level = "🟢"
    elif stars >= 5000:
        level = "🟡"
    else:
        level = "🔴"
    return level, f"⭐ {stars:,} stars · {forks:,} forks"


def eval_activity(meta: dict) -> tuple[str, str]:
    pushed = meta.get("pushed_at", "")
    if not pushed:
        return "🔴", "no push data"
    try:
        pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        days = (datetime.now(timezone.utc) - pushed_dt).days
        if days <= 3:
            return "🟢", f"{days}d since last push · active"
        if days <= 30:
            return "🟡", f"{days}d since last push · moderate"
        return "🔴", f"{days}d since last push · inactive"
    except (ValueError, TypeError):
        return "🔴", "cannot parse push date"


def eval_health(meta: dict) -> tuple[str, str]:
    open_issues = meta.get("open_issues_count", 0)
    if open_issues == 0:
        return "🟢", "0 open issues"
    if open_issues < 30:
        return "🟡", f"{open_issues} open issues"
    return "🔴", f"{open_issues} open issues · may be under-maintained"


def eval_stability(releases: list[dict], meta: dict) -> tuple[str, str]:
    if not releases:
        return "🔴", "no releases · pre-release only"
    latest = releases[0]
    tag = latest.get("tag_name", "")
    is_prerelease = latest.get("prerelease", False)
    if is_prerelease:
        return "🔴", f"{tag} (pre-release) · API may change"
    if tag.startswith("v0.") or tag.startswith("0."):
        return "🟡", f"{tag} · pre-stable, API may change"
    return "🟢", f"{tag} · stable release"


def eval_install_cost(readme: str) -> tuple[str, str]:
    readme_lower = readme.lower()
    signals: list[str] = []
    if "monorepo" in readme_lower:
        signals.append("monorepo")
    if "docker" in readme_lower:
        signals.append("Docker")
    if "pnpm" in readme_lower or "yarn" in readme_lower:
        signals.append("pnpm/yarn")
    if "electron" in readme_lower:
        signals.append("Electron")
    if "rust" in readme_lower or "cargo" in readme_lower:
        signals.append("Rust toolchain")
    if "go " in readme_lower or "golang" in readme_lower:
        signals.append("Go toolchain")

    dep_count = len(re.findall(r"npm install|pip install|gem install|cargo install|go get", readme_lower))

    if len(signals) >= 3 or dep_count >= 5:
        return "🔴", f"High — {' · '.join(signals)}" if signals else "many dependencies"
    if signals or dep_count >= 2:
        return "🟡", f"Medium — {' · '.join(signals)}" if signals else "some dependencies"
    return "🟢", "Low — simple setup"


def eval_overlap(readme: str) -> tuple[str, str]:
    data = load_activity()
    if not data.get("items"):
        return "🟢", "no existing tools to compare"

    readme_lower = readme.lower()
    matches: list[str] = []
    for name, item in data["items"].items():
        item_repo = (item.get("repo") or "").lower()
        item_domain = (item.get("domain") or "").lower()
        combined = f"{name} {item_repo} {item_domain}".lower()
        keywords = extract_keywords(readme_lower)
        overlap_count = sum(1 for kw in keywords if kw in combined)
        if overlap_count >= 2:
            score = calc_score(item)
            matches.append(f"{name} {score_bar(score)}")

    if not matches:
        return "🟢", "no overlap"
    if len(matches) <= 2:
        return "🟡", f"{len(matches)} related: {', '.join(matches[:3])}"
    return "🔴", f"{len(matches)} related: {', '.join(matches[:3])}..."


def extract_keywords(text: str) -> list[str]:
    topic_words = [
        "design", "logo", "banner", "color", "palette", "ui", "ux",
        "slide", "ppt", "presentation", "brand", "style", "css",
        "social", "redbook", "wechat", "twitter", "youtube", "video",
        "n8n", "automation", "workflow", "agent", "claude", "codex",
        "skill", "tool", "plugin", "mcp", "api", "cli",
        "data", "scrap", "crawl", "analysis", "visualization",
        "obsidian", "note", "wiki", "pkm", "knowledge",
        "bazi", "astrology", "divination", "esoteric",
        "tts", "audio", "music", "podcast", "image", "diffusion",
        "prompt", "template", "engineering",
    ]
    return [w for w in topic_words if w in text]


def eval_scenario(readme: str) -> tuple[str, str]:
    data = load_activity()
    if not data.get("items"):
        return "🟢", "no history — first in this domain?"

    keywords = extract_keywords(readme.lower())
    domain_activity: dict[str, list[tuple[str, int]]] = {}

    for name, item in data["items"].items():
        item_domain = item.get("domain", "")
        match_count = sum(
            1 for kw in keywords if kw in item_domain.lower() or kw in name.lower()
        )
        if match_count >= 1:
            score = calc_score(item)
            domain_activity.setdefault(item_domain, []).append((name, score))

    if not domain_activity:
        return "🟢", "new domain — no existing habits"

    unused_count = 0
    used_count = 0
    for domain, items in domain_activity.items():
        for name, score in items:
            if score <= 1:
                unused_count += 1
            else:
                used_count += 1

    if used_count > 0:
        return "🟢", f"domain active ({used_count} tools recently used)"
    if unused_count >= 3:
        return "🔴", f"{unused_count} tools in same domain, all ░░░░░ — likely low priority"
    return "🟡", f"{unused_count} unused tools in same domain"


# ---- main ----

EMOJI = {"🟢": "green", "🟡": "yellow", "🔴": "red"}


def run_evaluate(url: str) -> str:
    owner, repo = parse_github_url(url)

    dupe = find_duplicate_source(url)
    if dupe:
        return f"Already in catalog as '{dupe}'. Use `awesome list` to view."

    meta = fetch_repo_meta(owner, repo)
    releases = fetch_releases(owner, repo)
    readme = fetch_readme_raw(owner, repo)

    name = meta.get("name", repo)
    desc = (meta.get("description") or "").strip()

    lines = [f"## {name} 评估", ""]
    if desc:
        lines.append(f"> {desc}")
        lines.append("")

    pop_level, pop_text = eval_popularity(meta)
    act_level, act_text = eval_activity(meta)
    health_level, health_text = eval_health(meta)
    stab_level, stab_text = eval_stability(releases, meta)
    cost_level, cost_text = eval_install_cost(readme)
    overlap_level, overlap_text = eval_overlap(readme)
    scenario_level, scenario_text = eval_scenario(readme)

    lines.append("| 维度 | 评估 |")
    lines.append("|------|------|")
    lines.append(f"| 热度 | {pop_level} {pop_text} |")
    lines.append(f"| 活跃度 | {act_level} {act_text} |")
    lines.append(f"| 社区健康 | {health_level} {health_text} |")
    lines.append(f"| 版本稳定性 | {stab_level} {stab_text} |")
    lines.append(f"| 安装成本 | {cost_level} {cost_text} |")
    lines.append(f"| 重叠度 | {overlap_level} {overlap_text} |")
    lines.append(f"| 场景匹配 | {scenario_level} {scenario_text} |")
    lines.append("")

    # Overall recommendation
    reds = sum(1 for l in [pop_level, act_level, health_level, stab_level, cost_level, overlap_level, scenario_level] if l == "🔴")
    yellows = sum(1 for l in [pop_level, act_level, health_level, stab_level, cost_level, overlap_level, scenario_level] if l == "🟡")

    if reds >= 3:
        verdict = "🔴 不建议 — 多项指标不理想，建议观望或寻找替代品"
    elif reds >= 1 or yellows >= 3:
        verdict = "🟡 观望 — 部分指标需要关注，等条件改善或有明确需求时再装"
    else:
        verdict = "🟢 推荐安装 — 各项指标健康，可以放心装"

    lines.append(f"**建议：** {verdict}")
    return "\n".join(lines)

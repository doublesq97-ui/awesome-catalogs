from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .models import CATEGORY_TARGETS

ACTIVITY_PATH = Path("~/.claude/awesome-catalogs/activity.json").expanduser()


def load_activity() -> dict:
    if not ACTIVITY_PATH.exists():
        return {"items": {}}
    return json.loads(ACTIVITY_PATH.read_text(encoding="utf-8"))


def save_activity(data: dict) -> None:
    ACTIVITY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ACTIVITY_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def record_install(name: str, repo: str, domain: str, item_type: str = "skill") -> None:
    data = load_activity()
    now = datetime.now(timezone.utc).astimezone().isoformat()
    if name in data["items"]:
        data["items"][name]["installed_at"] = now
        data["items"][name]["repo"] = repo
        data["items"][name]["domain"] = domain
        data["items"][name]["type"] = item_type
    else:
        data["items"][name] = {
            "type": item_type,
            "name": name,
            "repo": repo,
            "domain": domain,
            "installed_at": now,
            "last_used_at": None,
            "times_used": 0,
        }
    save_activity(data)


def record_usage(name: str) -> dict | None:
    data = load_activity()
    now = datetime.now(timezone.utc).astimezone().isoformat()
    if name in data["items"]:
        data["items"][name]["times_used"] += 1
        data["items"][name]["last_used_at"] = now
        save_activity(data)
        return data["items"][name]
    return None


def calc_score(item: dict) -> int:
    last_used = item.get("last_used_at")
    if not last_used:
        return 0
    try:
        last = datetime.fromisoformat(last_used)
        days = (datetime.now(timezone.utc) - last).days
        if days <= 7:
            return 5
        if days <= 30:
            return 4
        if days <= 90:
            return 3
        if days <= 180:
            return 2
        return 1
    except (ValueError, TypeError):
        return 0


def score_bar(score: int) -> str:
    return "█" * score + "░" * (5 - score)


def scan_zombies() -> list[dict]:
    data = load_activity()
    zombies = []
    for name, item in data["items"].items():
        score = calc_score(item)
        item["_score"] = score
        if score <= 1:
            zombies.append(item)
    zombies.sort(key=lambda x: x["_score"])
    return zombies


def find_install_target(name: str, item_type: str) -> Path | None:
    target_dir = CATEGORY_TARGETS.get(item_type)
    if target_dir:
        return target_dir / name
    return None


def run_cleanup(force: bool = False) -> str:
    zombies = scan_zombies()
    if not zombies:
        return "No zombie items found. Everything is healthy."

    lines = [
        f"Found {len(zombies)} zombie items (score <= 1):",
        "",
        "| Score | Name | Type | Installed | Last Used |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in zombies:
        installed = item.get("installed_at", "?")[:10]
        last_used = item.get("last_used_at") or "never"
        if isinstance(last_used, str) and len(last_used) > 10:
            last_used = last_used[:10]
        lines.append(
            f"| {score_bar(item['_score'])} | {item['name']} | "
            f"{item.get('type', '?')} | {installed} | {last_used} |"
        )

    if not force:
        lines.append("")
        lines.append("Run `awesome cleanup --force` to delete these items.")
        return "\n".join(lines)

    deleted = []
    failed = []
    data = load_activity()
    for item in zombies:
        name = item["name"]
        target = find_install_target(name, item.get("type", "skill"))
        try:
            if target and target.exists():
                shutil.rmtree(target)
            data["items"].pop(name, None)
            deleted.append(name)
        except Exception as exc:
            failed.append(f"{name}: {exc}")

    save_activity(data)
    lines.append("")
    if deleted:
        lines.append(f"Deleted {len(deleted)} items: {', '.join(deleted)}")
    if failed:
        lines.append(f"Failed: {', '.join(failed)}")
    return "\n".join(lines)

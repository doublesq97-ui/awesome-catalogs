from __future__ import annotations

from pathlib import Path

from .models import CATEGORY_CATALOGS, CATEGORY_LABELS, RepoInfo


CATALOG_ROOT = Path("~/.claude/awesome-catalogs").expanduser()
HEADER = "| Domain | Name | Repo | Summary | Status |\n|---|---|---|---|---|\n"


def ensure_catalogs(root: Path = CATALOG_ROOT) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for filename in ["CATALOG.md", *CATEGORY_CATALOGS.values()]:
        path = root / filename
        if not path.exists():
            title = filename.removesuffix(".md").replace("_", " ").title()
            path.write_text(f"# {title}\n\n{HEADER}", encoding="utf-8")


def update_catalog(info: RepoInfo, root: Path = CATALOG_ROOT) -> None:
    ensure_catalogs(root)
    entry = format_entry(info)
    category_path = root / CATEGORY_CATALOGS[info.category]
    master_path = root / "CATALOG.md"
    append_or_replace(category_path, entry, info.name)
    append_or_replace(master_path, entry, info.name)


def list_catalog(category: str | None = None, root: Path = CATALOG_ROOT) -> str:
    ensure_catalogs(root)
    if category:
        normalized = normalize_category(category)
        path = root / CATEGORY_CATALOGS[normalized]
    else:
        path = root / "CATALOG.md"
    return path.read_text(encoding="utf-8")


def search_catalog(keyword: str, root: Path = CATALOG_ROOT) -> list[str]:
    ensure_catalogs(root)
    keyword_lower = keyword.lower()
    rows: list[str] = []
    for path in [root / "CATALOG.md", *[root / name for name in CATEGORY_CATALOGS.values()]]:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("|") and keyword_lower in line.lower() and "---" not in line:
                if line not in rows:
                    rows.append(line)
    return rows


def normalize_category(category: str) -> str:
    value = category.lower().strip()
    aliases = {
        "skills": "skill",
        "tools": "tool",
        "scripts": "script",
        "plugins": "plugin",
        "software": "software",
    }
    value = aliases.get(value, value)
    if value not in CATEGORY_CATALOGS:
        allowed = ", ".join(CATEGORY_LABELS.values())
        raise ValueError(f"Unknown category '{category}'. Use one of: {allowed}")
    return value


def format_entry(info: RepoInfo) -> str:
    status = "installed" if info.target_dir.exists() else "planned"
    return (
        f"| {escape(info.domain)} | {escape(info.name)} | {escape(info.source)} | "
        f"{escape(info.summary)} | {status} |"
    )


def append_or_replace(path: Path, entry: str, name: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    replaced = False
    new_lines: list[str] = []
    marker = f"| {name} |"
    for line in lines:
        if marker in line:
            new_lines.append(entry)
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        if new_lines and new_lines[-1].strip():
            new_lines.append(entry)
        else:
            new_lines[-1:] = [entry]
    path.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()

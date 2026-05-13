from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


CATEGORY_TARGETS = {
    "skill": Path("~/.claude/skills").expanduser(),
    "tool": Path("~/.claude/tools").expanduser(),
    "script": Path("~/.claude/scripts").expanduser(),
    "plugin": Path("~/.claude/plugins").expanduser(),
    "software": Path("~/claude-projects").expanduser(),
}

CATEGORY_CATALOGS = {
    "skill": "SKILLS_CATALOG.md",
    "tool": "TOOLS_CATALOG.md",
    "script": "SCRIPTS_CATALOG.md",
    "plugin": "PLUGINS_CATALOG.md",
    "software": "SOFTWARE_CATALOG.md",
}

CATEGORY_LABELS = {
    "skill": "Skills",
    "tool": "Tools",
    "script": "Scripts",
    "plugin": "Plugins",
    "software": "Software",
}


@dataclass(frozen=True)
class RepoInfo:
    name: str
    source: str
    path: Path
    category: str
    summary: str
    domain: str
    target_dir: Path
    already_installed: bool

    @property
    def status(self) -> str:
        return "installed" if self.already_installed else "new"

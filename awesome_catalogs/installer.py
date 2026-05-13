from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from .catalog import update_catalog
from .classifier import classify_repo
from .models import RepoInfo


def install_source(source: str, dry_run: bool = False, force: bool = False) -> RepoInfo:
    with tempfile.TemporaryDirectory(prefix="awesome-catalogs-") as temp:
        repo_path = fetch_source(source, Path(temp))
        info = classify_repo(repo_path, source=source)
        if dry_run:
            return info
        install_repo(info, force=force)
        update_catalog(info)
        return classify_repo(info.target_dir, source=source)


def fetch_source(source: str, temp_root: Path) -> Path:
    source_path = Path(source).expanduser()
    if source_path.exists():
        return source_path.resolve()

    url = normalize_github_url(source)
    target = temp_root / repo_name_from_url(url)
    subprocess.run(["git", "clone", "--depth", "1", url, str(target)], check=True)
    return target


def install_repo(info: RepoInfo, force: bool = False) -> None:
    info.target_dir.parent.mkdir(parents=True, exist_ok=True)
    if info.target_dir.exists():
        if not force:
            raise FileExistsError(f"{info.target_dir} already exists. Use --force to replace it.")
        shutil.rmtree(info.target_dir)
    shutil.copytree(info.path, info.target_dir, ignore=shutil.ignore_patterns(".git"))


def normalize_github_url(source: str) -> str:
    source = source.strip()
    if source.startswith("git@github.com:"):
        return source
    if source.startswith("https://github.com/"):
        return source
    if source.startswith("http://github.com/"):
        return "https://" + source.removeprefix("http://")
    if source.startswith("github.com/"):
        return "https://" + source
    if "/" in source and not source.startswith(("http://", "https://")):
        return "https://github.com/" + source
    raise ValueError(f"Unsupported source: {source}")


def repo_name_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1].removesuffix(".git")

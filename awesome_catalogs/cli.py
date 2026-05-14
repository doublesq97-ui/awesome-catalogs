from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .catalog import find_duplicate_source, list_catalog, search_catalog
from .classifier import classify_repo
from .installer import install_source
from .models import CATEGORY_LABELS, RepoInfo


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "classify":
            info = classify_repo(Path(args.source), source=args.source)
            print_report(info)
            return 0
        if args.command == "install":
            dupe = find_duplicate_source(args.source)
            if dupe:
                print(f"awesome: note: this source already exists in catalog as '{dupe}'")
            info = install_source(args.source, dry_run=args.dry_run, force=args.force)
            print_report(info)
            return 0
        if args.command == "list":
            print(list_catalog(args.category))
            return 0
        if args.command == "search":
            rows = search_catalog(args.keyword)
            if rows:
                print("| Domain | Name | Repo | Summary | Status |")
                print("|---|---|---|---|---|")
                print("\n".join(rows))
            else:
                print(f"No catalog entries matched: {args.keyword}")
            return 0
    except Exception as exc:
        print(f"awesome: error: {exc}", file=sys.stderr)
        return 1

    parser.print_help()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="awesome", description="Classify, install, and catalog GitHub repos.")
    parser.add_argument("--version", action="version", version=f"awesome-catalogs v{__version__}")
    sub = parser.add_subparsers(dest="command")

    classify = sub.add_parser("classify", help="Classify a local repo path.")
    classify.add_argument("source")

    install = sub.add_parser("install", help="Install a GitHub repo or local path.")
    install.add_argument("source")
    install.add_argument("--dry-run", action="store_true", help="Classify and report without copying files.")
    install.add_argument("--force", action="store_true", help="Replace an existing install target.")

    list_cmd = sub.add_parser("list", help="Print a catalog.")
    list_cmd.add_argument("category", nargs="?", help="skill/tools/scripts/plugins/software")

    search = sub.add_parser("search", help="Search all catalogs.")
    search.add_argument("keyword")

    return parser


def print_report(info: RepoInfo) -> None:
    print(f"Name:      {info.name}")
    print(f"Category:  {info.category} ({CATEGORY_LABELS[info.category]})")
    print(f"Domain:    {info.domain}")
    print(f"Summary:   {info.summary}")
    print(f"Source:    {info.source}")
    print(f"Target:    {info.target_dir}")
    print(f"Status:    {'already installed' if info.already_installed else 'ready'}")

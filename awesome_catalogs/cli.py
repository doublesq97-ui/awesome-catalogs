from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .activity import record_usage, run_cleanup
from .catalog import find_duplicate_source, list_catalog, search_catalog
from .classifier import classify_repo
from .evaluate import run_evaluate
from .installer import install_source
from .models import CATEGORY_LABELS, RepoInfo
from .stars import run_stars_import


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
        if args.command == "import-stars":
            output = run_stars_import(
                args.username,
                limit=args.limit,
                show_skipped=args.show_skipped,
            )
            print(output)
            return 0
        if args.command == "cleanup":
            print(run_cleanup(force=args.force))
            return 0
        if args.command == "record-usage":
            result = record_usage(args.name)
            if result:
                print(f"Recorded usage for '{args.name}' (used {result['times_used']} times)")
            else:
                print(f"awesome: note: '{args.name}' not found in activity.json")
            return 0
        if args.command == "evaluate":
            print(run_evaluate(args.url))
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

    stars = sub.add_parser("import-stars", help="Import and classify GitHub Stars.")
    stars.add_argument("username")
    stars.add_argument("--limit", type=int, help="Max repos to process.")
    stars.add_argument("--show-skipped", action="store_true", help="Show skipped items in output.")

    cleanup = sub.add_parser("cleanup", help="Scan and remove zombie items (score 0-1).")
    cleanup.add_argument("--force", action="store_true", help="Actually delete zombie items.")

    record = sub.add_parser("record-usage", help="Record a usage event for an item.")
    record.add_argument("name", help="Name of the skill/tool/script.")

    evaluate = sub.add_parser("evaluate", help="Evaluate a GitHub repo before installing.")
    evaluate.add_argument("url", help="GitHub repo URL to evaluate.")

    return parser


def print_report(info: RepoInfo) -> None:
    print(f"Name:      {info.name}")
    print(f"Category:  {info.category} ({CATEGORY_LABELS[info.category]})")
    print(f"Domain:    {info.domain}")
    print(f"Summary:   {info.summary}")
    print(f"Source:    {info.source}")
    print(f"Target:    {info.target_dir}")
    print(f"Status:    {'already installed' if info.already_installed else 'ready'}")

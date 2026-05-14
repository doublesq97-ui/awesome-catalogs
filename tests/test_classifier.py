from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import tempfile
from pathlib import Path

from awesome_catalogs.catalog import find_duplicate_source, update_catalog
from awesome_catalogs.classifier import classify_repo, extract_summary, safe_name


class ClassifierTests(unittest.TestCase):
    def test_detects_skill_from_skill_md(self) -> None:
        with repo("demo-skill", {"SKILL.md": "# Demo"}) as path:
            self.assertEqual(classify_repo(path).category, "skill")

    def test_detects_plugin_from_structured_marker(self) -> None:
        with repo("demo-plugin", {"mcp.json": "{}"}) as path:
            self.assertEqual(classify_repo(path).category, "plugin")

    def test_readme_plugin_words_do_not_trigger_plugin(self) -> None:
        files = {"README.md": "# Demo\n\nThis catalog mentions Claude plugin as a category."}
        with repo("demo-cli", files) as path:
            self.assertEqual(classify_repo(path).category, "software")

    def test_detects_single_script_repo(self) -> None:
        files = {"README.md": "# Demo", "run.sh": "echo hello"}
        with repo("demo-script", files) as path:
            self.assertEqual(classify_repo(path).category, "script")

    def test_detects_tool_from_cli_entry(self) -> None:
        files = {"README.md": "# Demo", "cli.py": "print('hello')"}
        with repo("demo-tool", files) as path:
            self.assertEqual(classify_repo(path).category, "tool")

    def test_plain_makefile_project_is_software(self) -> None:
        files = {"README.md": "# Demo", "Makefile": "test:\n\ttrue\n"}
        with repo("demo-software", files) as path:
            self.assertEqual(classify_repo(path).category, "software")

    def test_safe_name_preserves_readable_unicode(self) -> None:
        self.assertEqual(safe_name("原始版本"), "原始版本")
        self.assertEqual(safe_name("hello world.git"), "hello-world")

    def test_extract_summary_cleans_markdown_quote(self) -> None:
        readme = "# Demo\n\n> Paste a GitHub link — auto-classify."
        self.assertEqual(extract_summary(readme, fallback="none"), "Paste a GitHub link — auto-classify.")


class CatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_find_duplicate_source_returns_name(self) -> None:
        from awesome_catalogs.models import RepoInfo

        info = RepoInfo(
            name="test-tool",
            source="https://github.com/owner/test-tool",
            path=Path("."),
            category="tool",
            summary="A test tool.",
            domain="Dev Tools",
            target_dir=Path("/tmp/test-tool"),
            already_installed=True,
        )
        update_catalog(info, root=self.root)
        result = find_duplicate_source("https://github.com/owner/test-tool", root=self.root)
        self.assertEqual(result, "test-tool")

    def test_find_duplicate_source_returns_none_for_unknown(self) -> None:
        result = find_duplicate_source("https://github.com/unknown/repo", root=self.root)
        self.assertIsNone(result)


class repo:
    def __init__(self, name: str, files: dict[str, str]) -> None:
        self.name = name
        self.files = files
        self.temp: tempfile.TemporaryDirectory[str] | None = None
        self.path: Path | None = None

    def __enter__(self) -> Path:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name) / self.name
        root.mkdir()
        for relative, content in self.files.items():
            file_path = root / relative
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
        self.path = root
        return root

    def __exit__(self, *args: object) -> None:
        if self.temp:
            self.temp.cleanup()


if __name__ == "__main__":
    unittest.main()

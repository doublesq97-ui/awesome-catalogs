from __future__ import annotations

import unittest

from awesome_catalogs.stars import classify_star, count_by_status, decide_status, group_by_domain


class StarsDecisionTests(unittest.TestCase):
    def test_awesome_list_skipped_by_topic(self) -> None:
        repo = _make_repo(name="awesome-stuff", topics=["awesome-list"], description="A curated list")
        status, reason = decide_status(**repo)
        self.assertEqual(status, "skip")
        self.assertIn("Awesome list", reason)

    def test_course_keyword_skipped(self) -> None:
        repo = _make_repo(description="浙江大学课程攻略共享计划")
        status, _ = decide_status(**repo)
        self.assertEqual(status, "skip")

    def test_tool_topics_returns_recommend(self) -> None:
        repo = _make_repo(topics=["cli", "tool"], description="A useful CLI tool")
        status, _ = decide_status(**repo)
        self.assertEqual(status, "recommend")

    def test_library_skipped(self) -> None:
        repo = _make_repo(topics=["api-client"], description="HTTP client library")
        status, _ = decide_status(**repo)
        self.assertEqual(status, "skip")

    def test_library_sdk_skipped(self) -> None:
        repo = _make_repo(topics=["sdk"], description="Python SDK for SomeService")
        status, _ = decide_status(**repo)
        self.assertEqual(status, "skip")

    def test_no_description_without_topics_skipped(self) -> None:
        repo = _make_repo(description="")
        status, _ = decide_status(**repo)
        self.assertEqual(status, "skip")

    def test_no_description_with_tool_topic_recommended(self) -> None:
        repo = _make_repo(description="", topics=["mcp"])
        status, _ = decide_status(**repo)
        self.assertEqual(status, "recommend")

    def test_mcp_topic_recommended(self) -> None:
        repo = _make_repo(topics=["mcp"], description="An MCP server")
        status, _ = decide_status(**repo)
        self.assertEqual(status, "recommend")


class StarsClassifyTests(unittest.TestCase):
    def test_basic_classification(self) -> None:
        repo = {
            "name": "test-tool",
            "full_name": "owner/test-tool",
            "html_url": "https://github.com/owner/test-tool",
            "description": "A useful CLI tool for automation",
            "language": "Python",
            "topics": ["cli", "automation"],
            "stargazers_count": 42,
            "pushed_at": "2026-05-10T00:00:00Z",
        }
        info = classify_star(repo)
        self.assertEqual(info.name, "test-tool")
        self.assertEqual(info.status, "recommend")
        self.assertEqual(info.domain, "AI/Automation")

    def test_classification_assigns_domain(self) -> None:
        repo = {
            "name": "bazi-calculator",
            "full_name": "owner/bazi-calculator",
            "html_url": "https://github.com/owner/bazi-calculator",
            "description": "八字命理计算器",
            "language": "JavaScript",
            "topics": ["bazi", "astrology"],
            "stargazers_count": 10,
            "pushed_at": "2026-01-01T00:00:00Z",
        }
        info = classify_star(repo)
        self.assertEqual(info.domain, "Esoteric")


class StarsGroupingTests(unittest.TestCase):
    def test_group_by_domain(self) -> None:
        from awesome_catalogs.stars import StarInfo

        items = [
            StarInfo("a", "", "", "", "", [], 0, "", "recommend", "AI/Automation"),
            StarInfo("b", "", "", "", "", [], 0, "", "recommend", "Dev Tools"),
            StarInfo("c", "", "", "", "", [], 0, "", "recommend", "AI/Automation"),
        ]
        groups = group_by_domain(items)
        self.assertEqual(len(groups["AI/Automation"]), 2)
        self.assertEqual(len(groups["Dev Tools"]), 1)

    def test_count_by_status(self) -> None:
        from awesome_catalogs.stars import StarInfo

        items = [
            StarInfo("a", "", "", "", "", [], 0, "", "recommend", "Dev Tools"),
            StarInfo("b", "", "", "", "", [], 0, "", "skip", "Dev Tools"),
            StarInfo("c", "", "", "", "", [], 0, "", "recommend", "Dev Tools"),
            StarInfo("d", "", "", "", "", [], 0, "", "installed", "Dev Tools"),
        ]
        counts = count_by_status(items)
        self.assertEqual(counts["recommend"], 2)
        self.assertEqual(counts["skip"], 1)
        self.assertEqual(counts["installed"], 1)


def _make_repo(
    *,
    name: str = "test-repo",
    full_name: str = "owner/test-repo",
    html_url: str = "https://github.com/owner/test-repo",
    description: str = "",
    topics: list[str] | None = None,
    pushed_at: str = "2026-05-10T00:00:00Z",
) -> dict:
    return {
        "full_name": full_name,
        "html_url": html_url,
        "description": description,
        "topics": topics or [],
        "pushed_at": pushed_at,
    }


if __name__ == "__main__":
    unittest.main()

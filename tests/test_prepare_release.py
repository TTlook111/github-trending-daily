import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("release", Path(__file__).parents[1] / "scripts/prepare_release.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "2026/11/2026-11-04.md"
        self.path.parent.mkdir(parents=True)
        self.report = "# Report\n**日期**：2026-11-04（周三）\n" + "\n".join(f"### #{n} owner/repo{n} ⭐" for n in range(1, 11))
        self.path.write_text(self.report, encoding="utf-8")

    def payload(self, value="2026-11-04"):
        return m.payload(self.root, value, "owner/repo", "a" * 40)

    def test_valid_draft_snapshot(self):
        result = self.payload()
        self.assertTrue(result["draft"])
        self.assertEqual(result["tag_name"], "daily-2026-11-04")
        self.assertIn("/blob/" + "a" * 40, result["body"])
        self.assertEqual(result["make_latest"], "false")

    def test_invalid_dates(self):
        for value in ["2026-2-03", "2026-02-30", "../../etc/passwd", "2026-11-04\n", "$(echo bad)"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.payload(value)

    def test_missing(self):
        self.path.unlink()
        with self.assertRaises(ValueError):
            self.payload()

    def test_bad_contents(self):
        for content in ["", " ", self.report.replace("2026-11-04", "2026-11-03"), self.report.replace("### #10", "### #9"), self.report + "\n### #11 owner/repo11"]:
            self.path.write_text(content, encoding="utf-8")
            with self.subTest(content=content[:40]), self.assertRaises(ValueError):
                self.payload()

    def test_symlink(self):
        target = self.root / "other.md"
        target.write_text(self.report)
        self.path.unlink()
        self.path.symlink_to(target)
        with self.assertRaises(ValueError):
            self.payload()

    def test_bad_repository_and_commit(self):
        for repo, sha in [("bad/repo/extra", "a" * 40), ("owner/repo", "main")]:
            with self.assertRaises(ValueError):
                m.payload(self.root, "2026-11-04", repo, sha)

    def test_duplicate_including_draft_on_later_page(self):
        calls = []
        def request(repo, token, endpoint, **kw):
            calls.append(endpoint)
            return ([{"tag_name": "other"}] * 100 if endpoint.endswith("&page=1")
                    else [{"tag_name": "daily-2026-11-04", "draft": True}])
        self.assertIn("unchanged", m.create_draft("owner/repo", "fake", self.payload(), request))
        self.assertEqual(len(calls), 2)

    def test_existing_tag_blocks(self):
        def request(repo, token, endpoint, **kw):
            return [] if endpoint.startswith("releases?") else {"ref": "existing"}
        with self.assertRaises(ValueError):
            m.create_draft("owner/repo", "fake", self.payload(), request)

    def test_create_exactly_once_and_draft_only(self):
        writes = []
        def request(repo, token, endpoint, **kw):
            if endpoint.startswith("releases?"):
                return []
            if endpoint.startswith("git/ref"):
                return None
            writes.append(kw["data"])
            return {"html_url": "https://github.com/owner/repo/releases/draft"}
        m.create_draft("owner/repo", "fake", self.payload(), request)
        self.assertEqual(writes, [self.payload()])

    def test_read_failure_fails_closed(self):
        def request(*args, **kwargs):
            raise RuntimeError("HTTP 403")
        with self.assertRaises(RuntimeError):
            m.create_draft("owner/repo", "fake", self.payload(), request)

    def test_uncertain_create_not_retried(self):
        writes = []
        def request(repo, token, endpoint, **kw):
            if endpoint.startswith("releases?"):
                return []
            if endpoint.startswith("git/ref"):
                return None
            writes.append(endpoint)
            raise TimeoutError("uncertain")
        with self.assertRaises(TimeoutError):
            m.create_draft("owner/repo", "fake", self.payload(), request)
        self.assertEqual(writes, ["releases"])


if __name__ == "__main__":
    unittest.main()

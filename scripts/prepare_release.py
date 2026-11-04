"""Validate an archived digest and optionally create ONE draft release.

No report generation, tag mutation, update, or publication is performed here.
"""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request


def payload(root, report_date, repository, commit):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", report_date):
        raise ValueError("Date must be YYYY-MM-DD")
    date.fromisoformat(report_date)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Invalid repository")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Use the full checked-out commit SHA")
    relative = f"{report_date[:4]}/{report_date[5:7]}/{report_date}.md"
    root = Path(root).resolve()
    path = root / relative
    if path.resolve() != path or not path.is_file():
        raise ValueError(f"Missing regular archived report: {relative}")
    report = path.read_text(encoding="utf-8")
    if not report.strip():
        raise ValueError("Report is empty")
    if not re.search(r"^\*\*日期\*\*[：:]\s*" + re.escape(report_date) + r"(?:（|\s|$)", report, re.M):
        raise ValueError("Report header date does not match")
    projects = re.findall(r"^### #(\d+)\s+([^\s]+/[^\s]+)", report, re.M)
    if [n for n, _ in projects] != [str(n) for n in range(1, 11)]:
        raise ValueError("Expected exactly ten numbered projects (#1 to #10)")
    url = f"https://github.com/{repository}/blob/{commit}/{relative}"
    body = (f"## GitHub Trending 每日精选 · {report_date}\n\n"
            f"[阅读本期完整日报]({url})\n\n"
            "本期收录 10 个项目，由人工 + AI 协作整理。此工作流只分发已归档内容，不抓取榜单、不生成日报；内容准确性仍需人工审阅。\n\n"
            "### 本期项目\n\n" + "\n".join(f"- {n}. {repo}" for n, repo in projects)
            + f"\n\n归档：`{relative}`\n\n内容快照：`{commit}`\n")
    return {"tag_name": f"daily-{report_date}", "target_commitish": commit,
            "name": f"GitHub Trending Daily · {report_date}", "body": body,
            "draft": True, "prerelease": False, "make_latest": "false"}


def api(repository, token, endpoint, data=None, allow_missing=False):
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/{endpoint}",
        data=None if data is None else json.dumps(data).encode(),
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if allow_missing and error.code == 404:
            return None
        raise RuntimeError(f"GitHub API {endpoint}: HTTP {error.code}; no automatic retry") from None


def create_draft(repository, token, release, request=api):
    # The tag-specific release endpoint can omit drafts. Paginate the authenticated
    # collection so existing drafts and published releases are both detected.
    page = 1
    while True:
        existing = request(repository, token, f"releases?per_page=100&page={page}")
        if any(item["tag_name"] == release["tag_name"] for item in existing):
            return "Already exists; left unchanged (draft or published)."
        if len(existing) < 100:
            break
        page += 1
    # Refuse orphan/existing tags rather than silently point at different content.
    ref = request(repository, token, f"git/ref/tags/{release['tag_name']}", allow_missing=True)
    if ref is not None:
        raise ValueError("Tag already exists without a release; inspect it manually")
    result = request(repository, token, "releases", data=release)
    return f"Draft created: {result['html_url']}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--create-draft", action="store_true")
    args = parser.parse_args()
    release = payload(args.root, args.date, args.repository, args.commit)
    if args.create_draft:
        token = os.environ.get("GH_TOKEN")
        if not token:
            raise ValueError("GH_TOKEN is required only for draft creation")
        print(create_draft(args.repository, token, release))
    else:
        print(json.dumps(release, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

<a id="top"></a>

<p align="center">
  <img src="./assets/readme-cover.webp" width="100%" alt="An open-source reading room: books, code windows and an observatory connecting projects and ideas" />
</p>

<h1 align="center">GitHub Trending Daily</h1>
<p align="center"><strong>From trending repositories to ideas worth building on.</strong><br>10 projects per issue · In-depth Chinese breakdowns · A browsable archive</p>

<p align="center">
  <a href="./README.md">中文</a> · <strong>English</strong><br><br>
  <a href="#latest">Latest report</a> ·
  <a href="#archive">Browse the archive</a> ·
  <a href="#inside">Inside a report</a> ·
  <a href="#releases">Releases</a>
</p>

<p align="center"><a href="./LICENSE">MIT License</a> · Human + AI collaboration · Reports are written in Chinese</p>

---

<a id="latest"></a>

## 📌 Latest Report

<!-- Maintenance: update the link and all four fields below with each new issue, in both READMEs. -->
### 👉 [2026-11-04 · agent-desktop Takes #1, Coding Agents Become Domain Studios](./2026/11/2026-11-04.md)

| | |
| --- | --- |
| 📅 **Date** | 2026-11-04 |
| 🧩 **Theme** | agent-desktop Takes #1, Coding Agents Become Domain Studios |
| 📦 **Projects** | 10 |
| 🗺️ **Coverage** | Agent Desktop Control · Agent Domain Studios · Memory & Skills · Local Inference & Model Gateways |

<a id="inside"></a>

## 📄 What a Report Looks Like

**Start with the day's direction, then explore the projects behind it.** Each issue opens with a trend overview, followed by ten project breakdowns.

| Step | What you get |
| :--- | :--- |
| **01 · Understand** | The problem a project solves, its core mechanics and technical stack |
| **02 · Learn** | Ideas to borrow from product thinking, architecture, engineering and community building |
| **03 · Explore** | What stands out, why it matters, and a direct link to the original repository |

Each project also includes its language, category, total stars and daily star gain. These figures are snapshots from the report date, not live metrics.

<details>
<summary><strong>Read an example · September 11, 2026</strong></summary>

The excerpt below is translated from the [original Chinese report](./2026/09/2026-09-11.md). Project descriptions and star counts reflect that archived issue.

> ### #1 ayghri/i-have-adhd ⭐
>
> | Field | Info |
> | --- | --- |
> | 🔗 Link | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) |
> | ⭐ Stars | 38,285 (+3,882) |
> | 💻 Language | Python |
> | 📦 Category | AI Agents / Output Behavior Constraints |
>
> 📖 What it does
>
> i-have-adhd is a "behavior-constraint skill" for coding agents with a single goal: **make the agent skip the fluff and get straight to the answer**. It reshapes the agent's output style with 10 concise rules — action first, numbered steps, end with a next step, suppress tangents, no preamble and no "Hope this helps!".
>
> 💡 Key takeaways
>
> - **Product thinking**: Precisely targets the biggest pain point of LLM output — low information density, with key information buried in filler. It subtracts instead of adding, improving the experience through "constraints" rather than "capabilities"
> - **Architecture**: Extremely lightweight — the whole project is essentially 10 rules in a single SKILL.md file, with no complex dependencies and no model training, solving the problem purely through prompt engineering
>
> 🌟 What stands out
>
> The biggest lesson here isn't technical but **conceptual**: while everyone is adding capabilities to agents, the most practical skill turns out to be "teaching the agent to say less". 38K stars and a sustained 3,800+ daily gain prove strong demand for it.

Every project follows this structure. 10 projects + the opening trend insight make one complete report.

</details>

### How projects are selected

Start with projects gaining **at least 300 stars that day**. If fewer than ten qualify, lower the threshold and fill the remaining places by daily star gain. The final ten are ordered by that same metric. See the [maintenance guide](./CLAUDE.md) for the full editorial format.

<a id="archive"></a>

## 📅 Past Reports

Organized by `year/month`, all preserved for browsing.

| Month | Issues | Browse |
| --- | --- | --- |
| November 2026 | 4 | [Enter →](./2026/11/) |
| October 2026 | 30 | [Enter →](./2026/10/) |
| September 2026 | 29 | [Enter →](./2026/09/) |
| August 2026 | 16 | [Enter →](./2026/08/) |

> Report files are named `YYYY-MM-DD.md`. A missing date means no report was produced that day; historical reports are never edited or removed.

<a id="start"></a>

## 🚀 Quick Start

**Read online**: open the latest report above, or pick a month from the archive. No installation or account setup is needed to read the public files.

**Read locally**: clone the archive and open any dated Markdown report.

```bash
git clone https://github.com/TTlook111/github-trending-daily.git
cd github-trending-daily
```

> Reports are produced through **human + AI collaboration**. There is no automated Trending collection or report-generation script yet. This English README is a project guide; the reports themselves are in Chinese.

<a id="releases"></a>

## 📣 Per-issue Releases

**Archived report → manual trigger → draft → review → publication**

Each issue uses a fixed `daily-YYYY-MM-DD` tag. The workflow validates an existing report and prepares a draft; it does **not** generate reports, update the README, or publish automatically.

Browse [Releases](https://github.com/TTlook111/github-trending-daily/releases), or choose **Watch → Custom → Releases** to follow published issues. Notifications depend on your GitHub settings.

Maintainers: see the [Release guide (Chinese)](./docs/RELEASING.md) for first-run verification, review, duplicate detection and retries.

## 📂 Project Structure

```text
github-trending-daily/
├── README.md / README_en.md   # Chinese / English project guides
├── 2026/MM/YYYY-MM-DD.md      # Archived Chinese reports
├── assets/                   # Local README artwork
├── CLAUDE.md                 # Editorial rules and daily update checklist
├── docs/RELEASING.md          # Release process
├── scripts/prepare_release.py
├── tests/test_prepare_release.py
├── .github/workflows/daily-release.yml
└── LICENSE                   # MIT
```

## 🧭 Roadmap

- [ ] Automated GitHub Trending data collection
- [x] Manually prepare Release drafts ([first run verified](https://github.com/TTlook111/github-trending-daily/actions/runs/41766630473))
- [ ] Evaluate automatic draft preparation after content production and review are stable
- [ ] Trend aggregation: weekly / monthly summaries
- [ ] Project categorization & multi-language support

## 📄 Disclaimer

This project is for learning and information sharing. Featured projects belong to their respective authors. GitHub is a trademark of [GitHub, Inc.](https://github.com); this project is not affiliated with GitHub.

---

<p align="center"><strong>Find something useful? Give the archive a star.</strong><br>Read for the trends. Stay for the ideas.<br><br><a href="#top">Back to top ↑</a></p>

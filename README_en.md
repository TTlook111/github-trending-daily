<div align="center">

**English** | **[中文](./README.md)**

<br>

# 🔥 GitHub Trending Daily

### A daily Chinese digest of GitHub's hottest repos

> Curated **Top 10** trending projects — explaining **what** each one is, **why it's good**, and **why it's worth your attention**.
> Not machine-translated blurbs, but deep, borrowable breakdowns.

<br>

<!-- Dynamic badges: live repo stats -->
[![Stars](https://img.shields.io/github/stars/TTlook111/github-trending-daily?style=for-the-badge&logo=github&color=ffca28)](https://github.com/TTlook111/github-trending-daily/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/TTlook111/github-trending-daily?style=for-the-badge&color=2ea44f)](https://github.com/TTlook111/github-trending-daily/commits)
[![Repo Size](https://img.shields.io/github/repo-size/TTlook111/github-trending-daily?style=for-the-badge&color=3776AB)](https://github.com/TTlook111/github-trending-daily)

![Update](https://img.shields.io/badge/Update-Daily-2ea44f?style=flat-square)
![Report Language](https://img.shields.io/badge/Report-Chinese-3776AB?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-8A2BE2?style=flat-square)

<br>

**[📌 Latest Report](#-latest-report)** · **[📄 What a Report Looks Like](#-what-a-report-looks-like)** · **[📅 Past Reports](#-past-reports)** · **[🚀 Quick Start](#-quick-start)** · **[🧭 Roadmap](#-roadmap)**

</div>

---

## 🤔 Why This Repo Exists

Every day a new batch of projects shows up on GitHub Trending, but the list only gives you a **repo name + a one-line description**.

So the usual questions are: What problem does it actually solve? Why did it suddenly blow up? Is it worth spending time reading its code?

This repo does one thing every day: **explain the 10 most noteworthy projects on that day's Trending list, clearly, in Chinese.**

Each report goes beyond translating the description — it answers four questions:

| | You'll see |
| --- | --- |
| 🎯 **What it is** | Understand what the project does in one sentence, no jargon pile-up |
| 📖 **How it works** | 2-3 paragraphs on core mechanics, tech stack, and real data |
| 💡 **What's good about it** | **Borrowable** ideas from engineering, architecture & product angles |
| ✨ **Why it matters** | Innovation points, industry value, and what it signals about trends |

Every report also opens with a **📊 Daily Trend Insight** that connects all 10 projects — one project is a coincidence, ten together point to a direction.

---

## 📌 Latest Report

<table>
<tr>
<td>

### 👉 [2026-11-03 · Agents Learn to Drive the Desktop, agent-desktop Jumps to #2](./2026/11/2026-11-03.md)

| | |
| --- | --- |
| 📅 **Date** | 2026-11-03 |
| 🧩 **Theme** | Agents Learn to Drive the Desktop, agent-desktop Jumps to #2 |
| 📦 **Projects** | 10 |
| 🗺️ **Coverage** | Agent Desktop Control · Agent Shells & Memory · Skills & Configs · Local Voice Input |

</td>
</tr>
</table>

---

## 📄 What a Report Looks Like

Below is an excerpt of the #1 project from the 2026-09-11 report (translated from the original Chinese):

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

---

## 📅 Past Reports

Organized by `year/month`, all preserved for browsing.

| Month | Issues | Browse |
| --- | --- | --- |
| November 2026 | 3 | [Enter →](./2026/11/) |
| October 2026 | 30 | [Enter →](./2026/10/) |
| September 2026 | 29 | [Enter →](./2026/09/) |
| August 2026 | 16 | [Enter →](./2026/08/) |

> Report files are named `YYYY-MM-DD.md`. A missing date means no report was produced that day; historical reports are never edited or removed.

---

## 🚀 Quick Start

> ⏳ The automated collection script is under development — stay tuned. Reports are currently produced through human + AI collaboration.

```bash
# Clone the repository
git clone git@github.com:TTlook111/github-trending-daily.git
cd github-trending-daily

# Read the latest report (just open 2026/MM/YYYY-MM-DD.md)
```

You can also just click the "Latest Report" link above to read it on the web — no clone required.

---

## 📂 Project Structure

```
github-trending-daily/
├── README.md          # Project description (Chinese)
├── README_en.md       # Project description (English, this file)
├── CLAUDE.md          # AI maintenance guide
├── LICENSE            # MIT License
└── 2026/
    ├── 08/            # August 2026
    ├── 09/            # September 2026
    ├── 10/            # October 2026
    └── 11/            # November 2026
        └── YYYY-MM-DD.md   # 📅 Daily trend reports
```

---

## 🧭 Roadmap

- [ ] Automated GitHub Trending data collection
- [ ] GitHub Actions scheduled workflow to auto-generate daily reports
- [ ] Trend aggregation: weekly / monthly summaries
- [ ] Project categorization & multi-language support

---

## 📄 Disclaimer

This project is for learning and information sharing purposes only. All featured projects are copyrighted by their respective authors. GitHub is a trademark of [GitHub, Inc.](https://github.com) — this project has no affiliation with it.

---

<div align="center">

### ⭐ Support

If you find this repository helpful, feel free to give it a **Star** ⭐ or follow along with the daily updates!

<br>

**[⬆ Back to top](#-github-trending-daily)**

</div>

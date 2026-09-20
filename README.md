<div align="center">

**[English](./README_en.md)** | **中文**

<br>

# 🔥 GitHub Trending Daily

### 每天一份中文 GitHub 热榜日报

> 精选 Top 10 热门项目 —— 讲清它**是什么**、**好在哪**、**为什么值得关注**。
> 不做机翻简介，只做能看懂、能借鉴的深度拆解。

<br>

<!-- 动态徽章：实时展示仓库数据 -->
[![Stars](https://img.shields.io/github/stars/TTlook111/github-trending-daily?style=for-the-badge&logo=github&color=ffca28)](https://github.com/TTlook111/github-trending-daily/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/TTlook111/github-trending-daily?style=for-the-badge&color=2ea44f)](https://github.com/TTlook111/github-trending-daily/commits)
[![Repo Size](https://img.shields.io/github/repo-size/TTlook111/github-trending-daily?style=for-the-badge&color=3776AB)](https://github.com/TTlook111/github-trending-daily)

![更新频率](https://img.shields.io/badge/更新-每日-2ea44f?style=flat-square)
![报告语言](https://img.shields.io/badge/报告-中文-3776AB?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-8A2BE2?style=flat-square)

<br>

**[📌 最新一期](#-最新一期)** · **[📄 报告长什么样](#-报告长什么样)** · **[📅 往期报告](#-往期报告)** · **[🚀 快速开始](#-快速开始)** · **[🧭 Roadmap](#-roadmap)**

</div>

---

## 🤔 为什么会有这个仓库

每天 GitHub Trending 上都会冒出一批新项目，但榜单只给你**仓库名 + 一句英文简介**。

于是常见的困惑是：它到底解决什么问题？为什么突然就火了？值不值得花时间看它的代码？

这个仓库每天做一件事：**把当天 Trending 上最值得看的 10 个项目，用中文讲清楚。**

每份报告不只是翻译简介，而是回答四个问题：

| | 你会看到 |
| --- | --- |
| 🎯 **它是什么** | 一句话看懂项目在做什么，不堆术语 |
| 📖 **它怎么做的** | 2-3 段拆解核心机制、技术栈与真实数据 |
| 💡 **好在哪** | 从工程、架构、产品角度提炼**可借鉴**的地方 |
| ✨ **为什么值得关注** | 点出创新点与行业价值，以及它对趋势意味着什么 |

此外每份报告开头都有 **📊 今日趋势洞察**，把当天 10 个项目串起来看 —— 单看一个项目是巧合，10 个放一起就是方向。

---

## 📌 最新一期

<table>
<tr>
<td>

### 👉 [2026-09-20 · AI 代理基础设施分层时代到来](./2026/09/2026-09-20.md)

| | |
| --- | --- |
| 📅 **日期** | 2026-09-20 |
| 🧩 **主题** | AI 代理基础设施分层时代到来 |
| 📦 **项目数** | 10 个 |
| 🗺️ **覆盖方向** | 安全审计与 Computer Use · 企业自托管与端侧 AI · 个人知识与垂直应用 |

</td>
</tr>
</table>

---

## 📄 报告长什么样

下面是 2026-09-11 报告中排名第一的项目节选：

> ### #1 ayghri/i-have-adhd ⭐
>
> | 属性 | 信息 |
> | --- | --- |
> | 🔗 链接 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) |
> | ⭐ Stars | 38,285 (+3,882) |
> | 💻 语言 | Python |
> | 📦 分类 | AI 代理 / 输出行为约束 |
>
> 📖 项目是干什么的
>
> i-have-adhd 是一个为编码代理设计的"行为约束技能"，核心目标只有一个：**让代理别废话，直接给答案**。它用 10 条精炼规则彻底重塑代理的输出风格——动作优先、步骤编号、结尾给出下一步、压制跑题、不要开场白也不要"Hope this helps!"。
>
> 💡 可借鉴的优点
>
> - **产品思维**：精准定位了 LLM 输出的最大痛点——信息密度低、关键信息被废话淹没。不做加法做减法，用"约束"而非"能力"来提升体验
> - **架构设计**：极度轻量化——整个项目核心就是一个 SKILL.md 文件里的 10 条规则，没有复杂依赖，没有模型训练，纯粹用"提示工程"解决问题
>
> 🌟 特别亮眼的地方
>
> 这个项目最大的启示不在技术，而在**认知**：当所有人都在给代理增加能力时，最实用的技能反而是"教代理少说话"。38K Star 和持续日增 3,800+ 证明了市场对此的强烈需求。

每个项目都是这样的结构，10 个项目 + 开头的趋势洞察，就是一期完整报告。

---

## 📅 往期报告

按 `年/月` 归档，全部保留，随时可翻阅。

| 月份 | 期数 | 浏览 |
| --- | --- | --- |
| 2026 年 9 月 | 18 篇 | [进入 →](./2026/09/) |
| 2026 年 8 月 | 16 篇 | [进入 →](./2026/08/) |

> 报告文件以 `YYYY-MM-DD.md` 命名。个别日期缺失表示当天未产出，历史报告不做删改。

---

## 🚀 快速开始

> ⏳ 自动化抓取脚本开发中，敬请期待。目前报告以人工 + AI 协作方式产出。

```bash
# 克隆仓库
git clone git@github.com:TTlook111/github-trending-daily.git
cd github-trending-daily

# 阅读最新报告（打开 2026/MM/YYYY-MM-DD.md 即可）
```

也可以直接在网页上点开上方「最新一期」的链接阅读，无需克隆。

---

## 📂 目录结构

```
github-trending-daily/
├── README.md          # 项目说明（中文，本文件）
├── README_en.md       # 项目说明（英文）
├── LICENSE            # MIT License
└── 2026/
    ├── 08/            # 2026 年 8 月
    └── 09/            # 2026 年 9 月
        └── YYYY-MM-DD.md   # 📅 每日趋势报告
```

---

## 🧭 Roadmap

- [ ] 自动化抓取 GitHub Trending 数据
- [ ] GitHub Actions 定时任务，每日自动生成报告
- [ ] 趋势汇总：周报 / 月报
- [ ] 项目分类与多语言支持

---

## 📄 免责声明

本项目内容仅供学习与信息分享，所收录项目的版权归原作者所有。GitHub 是 [GitHub, Inc.](https://github.com) 的商标，本项目与其无任何隶属关系。

---

<div align="center">

### ⭐ 支持一下

如果这个仓库对你有帮助，欢迎点个 **Star** ⭐，或持续关注每日更新！

<br>

**[⬆ 回到顶部](#-github-trending-daily)**

</div>

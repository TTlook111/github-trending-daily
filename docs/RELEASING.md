# 每日日报的 Release 发布指南

## 先区分三件事

- **日报内容**：人工 + AI 协作整理、人工核对，存放于 `YYYY/MM/YYYY-MM-DD.md`。
- **Git tag**：固定的内容快照，命名 `daily-YYYY-MM-DD`，不是软件语义版本。
- **GitHub Release**：面向读者的发布页，提供该期项目目录和固定 commit 的完整日报链接。

此工作流只把已有日报整理为 Release 草稿，不抓取榜单、不生成日报、不改 README，也不自动公开发布。缺少日报时失败，绝不拿旧日报冒充当天内容。

## 第一次实验

1. 先审阅本次代码改动。只有合并到默认分支后，GitHub 才能通过 `workflow_dispatch` 提供此工作流；本次准备工作不代表已合并、已运行或已发布。
2. 打开仓库 **Actions → Prepare daily release draft → Run workflow**，分支选默认分支，输入 `2026-11-04`。日期使用 Asia/Shanghai，补发时填实际日报日期。
3. 工作流先运行离线测试，再校验文件存在、非空、不是符号链接、标题日期匹配、项目编号恰好 #1 至 #10。它不核验报告中的事实、星数和外链有效性，仍需人工审阅。
4. 打开 **Releases** 中新建的草稿，核对标题、`daily-2026-11-04`、10 个项目和完整日报链接。草稿链接只对有权限的维护者可见。
5. **首次公开发布前先确认最终内容**。确认后在草稿页面点击 **Publish release**。当前脚本没有自动公开发布选项。
6. 发布后打开公开 Release，检查完整日报链接。GitHub 可能自动附带源码 ZIP/TAR，它是仓库快照，不是安装包。

建议首期标题：`GitHub Trending Daily · 2026-11-04`。说明由脚本从本期实际项目标题生成，不复写未经复核的星数或扩大趋势结论。

## 每天怎么做

1. 按现有人工 + AI 流程产出日报，人工核验，然后提交日报并同步中英文 README。
2. 日报进入默认分支后，手动运行一次工作流，填写这期日期。
3. 检查草稿内容，再手动公开发布。读者可在仓库 Watch 的 Custom 选项中选择 Releases，具体通知取决于其 GitHub 设置。

现阶段不加定时器：日报何时完成比时钟更重要。未来如需自动化，应先稳定“日报提交并审核完成”的信号，再考虑每天只自动准备草稿；不要把定时发布等同于自动生成高质量内容。

## 重跑、冲突和修订

- 每日期固定一个 `daily-YYYY-MM-DD`，同日期工作流串行执行。
- 已有同标签草稿或公开 Release 时跳过，不覆盖、不重新发布。检查包含分页，避免草稿或旧版本漏查。
- 若标签已存在但没有 Release，停止并人工检查，避免标签指向与正文快照不一致。
- 已发布标签不移动，历史日报不回改。更正应独立说明，不静默替换历史内容。
- 请求超时或权限错误会停止；创建结果不确定时先查看 Releases，确认结果后再重跑。不会自动反复创建。
- 不同工具同时绕过工作流创建 Release 不受此工作流的串行锁保护。发布期间避免人工/API 并行创建同一期；GitHub 返回冲突时人工核查。

## 权限与本地预览

仅草稿 job 使用仓库内置临时 `GITHUB_TOKEN` 的 `contents: write`；无需新增 PAT、第三方密钥或外部服务。checkout 禁止持久化凭据，第三方 action 固定到 commit。工作流只允许在默认分支运行，实验分支会跳过。

本地仅预览，不联网、不创建 Release：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/prepare_release.py \
  --date 2026-11-04 \
  --repository TTlook111/github-trending-daily \
  --commit "$(git rev-parse HEAD)"
```

预览输出 JSON，其中 `body` 即发布说明。传入的 commit 必须是当前文件对应的完整提交 SHA；工作流通过固定 checkout SHA 保证一致。

参考：[GitHub Release API](https://docs.github.com/en/rest/releases/releases)、[手动运行工作流](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)。

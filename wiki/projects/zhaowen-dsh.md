---
name: zhaowen-dsh
visibility: public
language: TypeScript
stars: 0
forks: 0
last_push: 2026-11-23
category: AI / Agent / 插件
archived: false
updated: 2026-11-23
---

# zhaowen-dsh

> DSH 工具集：多 Agent 团队编排插件 @zhuobichen/dsh-team + Claude Code 风格 TUI (dsh-cc-tui) + 终端客户端 (dsh-term)

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | TypeScript |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-23 |
| 话题 | cordis, deepseek-harness, dsh, dsh-plugin, multi-agent, terminal, tui |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-dsh |

## 最近一次提交

`7edc27e` 2026-11-23 — feat(design-workbench): 加「漫画」层（23 种）＋ 筛选芯片按层整理 - 新增第五层「漫画」：动漫 / 漫画 / 动画的视觉语言，23 条 来源是 code-to-film 下

## README 摘录

zhaowen-dsh

赵文自己的 **DeepSeek Harness（DSH）** 插件与工具集：**27 个包**，覆盖会话管理、沙箱与权限、生图生视频、跨工具会话迁移、远程执行、若干 MCP 桥接，以及一个 TUI 前端和一个独立终端客户端。

> ⚠️ **开发门禁（必读）**：[`docs/门禁-等待与取消.md`](docs/门禁-等待与取消.md)
> 任何**可能长时间不返回**的工具，都必须满足两条铁律：
> **① 每一个 await 都有「无论如何都会结束」的兜底；② 每个工具都接 `exec.signal`。**
> 两次真实事故（`host_exec` 挂死 QQ 会话、`generate_video` 生成成功却永不返回）都出在这两条上。
> 提交前跑：`node scripts/check-await-safety.mjs`（退出码 1 = 有 [必错]）。
> 另有一条**改名门禁**：`node scripts/check-plugins.mjs`（CI 里也跑）会核对每个包的
> `cordis.patch.yml` 引用的模块名 —— 改名只改 `package.json`、漏改 patch，重启后插件会
> `enabled:true` 但 `fiberPhase:null`（工具消失、面板 404，启动日志里很不显眼）。

| 目录 | 包名 | 是什么 |
| [`packages/dsh-balance`](packages/dsh-balance) | `@zhuobichen/dsh-balance` | **DSH 插件*…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

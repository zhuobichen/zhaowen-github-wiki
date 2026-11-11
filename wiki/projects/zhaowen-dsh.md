---
name: zhaowen-dsh
visibility: public
language: TypeScript
stars: 0
forks: 0
last_push: 2026-11-09
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# zhaowen-dsh

> DSH 工具集：多 Agent 团队编排插件 @zhuobichen/dsh-team + Claude Code 风格 TUI (dsh-cc-tui) + 终端客户端 (dsh-term)

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | TypeScript |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-09 |
| 话题 | cordis, deepseek-harness, dsh, dsh-plugin, multi-agent, terminal, tui |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-dsh |

## 最近一次提交

`1649f3a` 2026-11-09 — chore(sandbox-grant): spawnDetached 加 await-gate 豁免说明（detached + stdio ignore 是故意不设超时）

## README 摘录

zhaowen-dsh

赵文自己的 **DeepSeek Harness（DSH）** 工具集：团队编排插件、会话导入插件、TUI 前端插件、终端客户端。

> ⚠️ **开发门禁（必读）**：[`docs/门禁-等待与取消.md`](docs/门禁-等待与取消.md)
> 任何**可能长时间不返回**的工具，都必须满足两条铁律：
> **① 每一个 await 都有「无论如何都会结束」的兜底；② 每个工具都接 `exec.signal`。**
> 两次真实事故（`host_exec` 挂死 QQ 会话、`generate_video` 生成成功却永不返回）都出在这两条上。
> 提交前跑：`node scripts/check-await-safety.mjs`（退出码 1 = 有 [必错]）。

| 目录 | 包名 | 是什么 |
| [`packages/dsh-balance`](packages/dsh-balance) | `@zhuobichen/dsh-balance` | **DSH 插件**：DeepSeek 账户余额作为输入框上方的一行（宿主半身：只读路由 + `/bal` 命令 + TUI `\${balance}` 槽位；**客户端半身也在本包内** `client/client.js`）。移植自 Claude Code 的 `deepseek-balance` mod |
| [`packages/dsh-moon-band`](packages/dsh-moon-band) | `@zhuobichen/dsh-moon-band` | **DSH…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

---
name: zhaowen-claudemod
visibility: public
language: TypeScript
stars: 0
forks: 0
last_push: 2026-10-20
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# zhaowen-claudemod

> 我自用的 Claude Code mod 合集（function hooks）：以 marketplace 形式分发，/plugin install 装

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | TypeScript |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-10-20 |
| 话题 | — |
| License | — |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-claudemod |

## 最近一次提交

`5173e32` 2026-10-20 — fix(moon-band): 模型回复不是字符串时不再炸，并加一条换模型的退路 实测 `$.model.complete` 回来的不是字符串（类型上写着 Promise<string>），于是 `t

## README 摘录

zhaowen-claudemod

我自用的 Claude Code mod 合集。仓库根就是 marketplace，每个 mod 一个子目录 —— 官方那套结构，装的时候一条命令。

**换机器 / 从头复现这套配置**看 [MODS.md](./MODS.md)：装法、每个 mod 的前提、别人的 mod（不在本仓库）怎么装、技能和 MCP 在哪个仓库。

装

/plugin install deepseek-balance --marketplace zhuobichen/zhaowen-claudemod

（会先问要不要把这个 marketplace 加进来，答 y；再选 scope，`user` 就是每个会话都有。）

mod 列表

| mod | 干什么 | 前提 |
| [deepseek-balance](./deepseek-balance) | 提示行上面一行显示 DeepSeek 余额 + 最近五个整点每小时的花费，5 分钟自刷，`/balance` 手动读 | 会话接在 DeepSeek 上（API key）；接在别的端点的会话里它不说话也不发请求 |
| [moon-band](./moon-band) | 月相 + 月龄 + 一句古诗，压暗的一行，每分钟换一句，`/moon` 收起 | 无。月相查相时刻表（覆盖到 2026-12-31），表外会标 `≈` |
| [novel-pane](./novel-pane) | 会话里开一个可折叠窗格读书：`/novel `（打开不说话），一次一屏、按钮就是窗格的第一行（滚轮滚不走它），进度另钉在提…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

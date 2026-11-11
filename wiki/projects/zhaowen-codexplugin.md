---
name: zhaowen-codexplugin
visibility: public
language: JavaScript
stars: 0
forks: 0
last_push: 2026-10-20
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# zhaowen-codexplugin

> 赵文的 Codex 插件市场：从 Claude Code 的 mod 移植过来的 skill + MCP 工具

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | JavaScript |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-10-20 |
| 话题 | — |
| License | — |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-codexplugin |

## 最近一次提交

`b68bde1` 2026-10-20 — feat(deepseek-balance): 加 /balance 斜杠命令，修密钥回退与退出崩溃 按官方 spec 和 openai-curated 里的真实样例补齐： - commands/ba

## README 摘录

zhaowen-codexplugin

赵文自己的 **Codex 插件**市场。内容从 Claude Code 的 mod 移植而来（[`zhaowen-claudemod`](https://github.com/zhuobichen/zhaowen-claudemod)），
但**形态不一样**——见下面那张对照表，这是这个仓库存在的原因。

Codex 插件长什么样

Codex Desktop 的插件是一个目录，加上一个市场清单：

.agents/plugins/marketplace.json          ← 市场清单（列有哪些插件）
plugins//.codex-plugin/plugin.json  ← 插件清单（名字、版本、指向 skills / MCP）
plugins//skills//SKILL.md    ← skill：教模型怎么做
plugins//.mcp.json                  ← 可选：MCP 服务，给模型真能调的工具

装的时候写进 `~/.codex/config.toml`：

[marketplaces.zhaowen-codexplugin]
source_type = "local"
source = 'D:\github_project\ZhaoWen_GitHub维护\zhaowen-codexplugin'

[plugins."deepseek-balance@zhaowen-codexplugin"]
enabled = true

Claude mod → Codex 的形态对照（重点）…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

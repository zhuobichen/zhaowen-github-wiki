---
name: qchat-cli
visibility: public
language: TypeScript
stars: 1
forks: 0
last_push: 2026-11-16
category: 微信 / 数据采集
archived: false
updated: 2026-11-16
---

# qchat-cli

> QQ 聊天记录导出 / 消息监听 / 群管理 / QQ 空间自动化的命令行工具；基于 OneBot + NapCat，支持 AI 群日报与私聊机器人。

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | TypeScript |
| ⭐ Star | 1 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-16 |
| 话题 | ai-agent, chat-export, chat-history, cli, napcat, onebot, qq, qqbot, qzone, typescript |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/qchat-cli |

## 最近一次提交

`72e1e54` 2026-11-16 — feat: 名片守卫脚本 + 两条硬规则（冷峰沉睡下等马 / 名片不可被别人固定） 号主：'有的东西严格不能变，但可以被别人改的，比如你在某个群中的备注。 针对备注，你可以自己做一个自动化的脚本，一旦

## README 摘录

简体中文 · [English](./README.en.md)

架构

图是 MiniMax 直接生成的像素风示意图（四个大标签是全对的；再多它就开始画鬼画符，所以细节放在下面的文字里）。

- **qce 工具层**：所有动作只有一种参数写法、一种返回格式；CLI 和 MCP 共用这一层，上层出问题时能退回到这一层查。
- **两条通道**：HTTP `:3000` 负责调用与历史，WebSocket 负责事件推送——戳一戳、新消息都靠它。
- **本地优先**：`.qce-index/` 存消息索引（搜索/日报不联网），`private/` 存表情库、梗库、记忆、规则、人格，`output/` 存导出与生成产物。
- **常驻旁路**：`qq-watch` 把新消息投进会话、`qq-watchdog` 体检与熔断、`qq-poke-watch` 收戳并还手、`dispatch` 车道把写代码的活丢给独立会话。

细节见 [ARCHITECTURE.md](./ARCHITECTURE.md)。

`qce` 是一个跑在你自己电脑上的 QQ 命令行工具。它不做“点一下导出”的按钮，而是把 QQ 账号变成一个**可编程的数据源**：导出可读的聊天记录、实时监听消息、按规则自动回复、把群聊接进 AI，也能做群管理和 QQ 空间的事。

它能回答 QQ 回答不了的几个问题

- 谁在群里提过我？这周那个群到底在吵什么？
- 去年这个时候，我们在聊什么？
- 把某个群的历史导出来，做成本地可搜索的档案 / 知识库。
- 每天下班前，自动给我一份“今天各群发生了什么”的日报。

6…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

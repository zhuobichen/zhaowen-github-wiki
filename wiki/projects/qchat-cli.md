---
name: qchat-cli
visibility: public
language: TypeScript
stars: 1
forks: 0
last_push: 2026-11-11
category: 微信 / 数据采集
archived: false
updated: 2026-11-11
---

# qchat-cli

> QQ 聊天记录导出 / 消息监听 / 群管理 / QQ 空间自动化的命令行工具；基于 OneBot + NapCat，支持 AI 群日报与私聊机器人。

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | TypeScript |
| ⭐ Star | 1 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-11 |
| 话题 | ai-agent, chat-export, chat-history, cli, napcat, onebot, qq, qqbot, qzone, typescript |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/qchat-cli |

## 最近一次提交

`b1e5a99` 2026-11-11 — feat(poke): 收戳一戳——WS 事件常驻监听，收到投递到会话并自动还手 - NapCat httpServers 开着 enableWebsocket，3000 端口同一套 token 可连

## README 摘录

qchat-cli &nbsp;

**把 QQ 里发生过的事，变成可导出、可监听、可自动化的数据**

简体中文 · [English](./README.en.md)

`qce` 是一个跑在你自己电脑上的 QQ 命令行工具。它不做“点一下导出”的按钮，而是把 QQ 账号变成一个**可编程的数据源**：导出可读的聊天记录、实时监听消息、按规则自动回复、把群聊接进 AI，也能做群管理和 QQ 空间的事。

它能回答 QQ 回答不了的几个问题

- 谁在群里提过我？这周那个群到底在吵什么？
- 去年这个时候，我们在聊什么？
- 把某个群的历史导出来，做成本地可搜索的档案 / 知识库。
- 每天下班前，自动给我一份“今天各群发生了什么”的日报。

60 秒上手

前置：本机已跑起 NapCat（QQNT 的 OneBot 实现）。装法见 [docs/napcat.md](./docs/napcat.md)（含 Docker 一键版），或直接用你已有的 OneBot 服务。

git clone https://github.com/zhuobichen/qchat-cli.git
cd qchat-cli && npm install && npm run build && npm link

$ qce login --host 127.0.0.1 --port 3000   # 配置 + 连接测试
✓ 已连接  OneBot 11 / 账号 123456789

$ qce list groups
群组列表 (65):
123456789   示例·测试群 (3人)
2345…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

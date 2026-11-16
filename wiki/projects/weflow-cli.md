---
name: weflow-cli
visibility: public
language: Python
stars: 168
forks: 73
last_push: 2026-11-16
category: 微信 / 数据采集
archived: false
updated: 2026-11-16
---

# weflow-cli

> 本地优先的微信数据工具：聊天记录查询导出、公众号日报与个人知识库（MCP 兼容）

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 168 |
| 🍴 Fork | 73 |
| 最近推送 | 2026-11-16 |
| 话题 | ai, backup, chat-history, cli, export, knowledge-base, mcp, wechat, wechat-exporter, wechat4 |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/weflow-cli |

## 最近一次提交

`5167935` 2026-11-16 — fix(contacts): load_contact_names 静默返回空表，联系人姓名退化为裸 wxid 采纳 PR #17（@fcmyoo）。**这个 bug 是我在 352a3d3（只读副本

## README 摘录

𝗪𝗲𝗙𝗹𝗼𝘄 𝗖𝗟𝗜

**简体中文** · [English](./README.en.md)

*今人不见古时月，今月曾经照古人*

> 夫天地者，万物之逆旅也；光阴者，百代之过客也。

> 让聊天记录、公众号阅读和个人知识工作流回到你的本地电脑。

**WeFlow CLI 把微信变成你的本地第二大脑。** 四件事，全部在本机完成——不登录你的账号，也不上传聊天内容：

| | 你能得到什么 | 从哪开始 |
| 💬 **聊天记录** | 按人、按群、按时间查询与搜索；导出成能直接翻的 HTML（含图片、语音转写） | `weflow-cli export` |
| 📰 **公众号** | 把订阅号文章整理成带 AI 摘要的每日简报，可邮件推送 | `weflow-cli daily` |
| ⭐ **收藏** | 读本地收藏库，按类型和关键词检索（文章、图片、链接） | `weflow-cli fav list` |
| 🧠 **知识库** | 文章与聊天沉淀成可语义搜索的笔记与概念图谱 | `weflow-cli search` · `weflow-cli wiki` |

支持 Windows 与 Linux；有 MCP 接口，可接进 Claude Code 等 AI 编辑器。

它专门回答**几个微信自己回答不了的问题**：谁在等我回话、我答应过谁什么后来做了没有、和谁的关系在变淡、某个号的观点怎么变的、那一年的今天我们在聊什么。

> **本地优先**：默认在本机处理数据，不内置遥测；明确选择的在线服务和云端 AI 会发起网络请求。配置密钥的加密、独立密钥缓存和…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

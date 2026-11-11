---
name: pilgrim-intel
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-05
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# pilgrim-intel

> 统一 AI 情报聚合系统：多信源抓取、AI 摘要与 MCP 可查询

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | ai-summary, information-aggregation, intelligence, mcp, rss |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/pilgrim-intel |

## 最近一次提交

`41f4e1e` 2026-11-05 — fix: 默认仅监听本机；CORS 改白名单；去重计数改用游标 rowcount - server.py: --host 默认 127.0.0.1（对外绑定会告警），CORS 只回显白名单来源 - s

## README 摘录

Pilgrim Intel 🕊️ v2.0

统一 AI 情报聚合系统 — 多信源抓取 → SQLite 持久化 → AI 摘要 → 多推送 → MCP 可查询。

🏗️ 架构

feeds.yaml (5 个 feed 配置；其中 shenlun 为独立邮件频道)
run.py  ──►  pilgrim/engine.py  ──►  pilgrim/storage.py (SQLite + FTS5)
统一Runner    fetch→dedup→AI→push       pilgrim/server.py
(MCP + HTTP 反馈)

📦 快速开始

pip install -r requirements.txt
cp .env.example .env  # 填入 DEEPSEEK_API_KEY + 邮箱配置

运行所有 feed
python run.py

运行单个 feed
python run.py run --feed gamehub

搜索已存储内容
python run.py search "AI 新闻"

查看统计
python run.py stats

启动 MCP + 反馈服务器
python run.py serve

🌐 MCP Server

启动服务器后访问 `http://localhost:9876/mcp`，提供 5 个工具：

| 工具 | 功能 |
| `pilgrim_search_news` | 全文搜索已收录内容 |
| `pilgrim_get_digest` | 获取指定日期日报 |
| `pilgrim_l…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

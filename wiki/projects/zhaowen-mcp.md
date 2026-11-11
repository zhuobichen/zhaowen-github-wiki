---
name: zhaowen-mcp
visibility: public
language: TypeScript
stars: 0
forks: 0
last_push: 2026-11-05
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# zhaowen-mcp

> 个人自用的 MCP 服务集合（15 个）：中文平台数据（小红书 / B站 / 热榜）、智能体会话检索、代码审阅、SSH 文件管理、识图生图生视频、API 用量监测等，供 Claude Code 等 MCP 客户端调用

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | TypeScript |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | claude-code, image-generation, mcp, model-context-protocol, video-generation |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-mcp |

## 最近一次提交

`ee9eb9b` 2026-11-05 — fix(code-review): 路径白名单 + 请求超时重试 + 不把 reasoning 当结论 - 新增 path-guard.ts：REVIEW_ALLOWED_DIRS 白名单 + rea

## README 摘录

ZhaoWen 自用的 MCP 服务集合

个人自用的 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 服务集合，供 Claude Code 等 MCP 客户端调用。

包含的服务

| 目录 | 服务 | 功能 |
| [`deepseek-search/`](./deepseek-search) | DeepSeek 网页搜索与抓取 | `deepseek_search` 按 query 搜索（rerank_score/authority/date，支持 site:/lang:/after: 语法，低分结果会告警，可 min_score 过滤）· `deepseek_fetch` 抓网页返 Markdown · `check_status` 查配置与版本 |
| [`ima-mcp/`](./ima-mcp) | 腾讯 ima 知识库 / 笔记 | `ima_search_knowledge_bases` 搜知识库 · `ima_list_knowledge`/`ima_search_knowledge` 查知识 · `ima_import_urls` 导入网页 · `ima_upload_file` 上传文件入库 · `ima_read_media` 读原文 · `ima_create_knowledge_base`/`ima_create_folder`/`ima_rename_knowledge` 建库建目录改名 · `ima_list_notebooks`/`ima_search_not…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

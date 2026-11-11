---
name: digital-humanities-narrative
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-11
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# digital-humanities-narrative

> 数字人文叙事 AI 分析引擎：人物关系网络与叙事生成（CLI + Web）

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-11 |
| 话题 | ai, digital-humanities, knowledge-graph, narrative-generation, nlp |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/digital-humanities-narrative |

## 最近一次提交

`c6c2c43` 2026-11-11 — feat: 复核强度 strict/normal/loose + DSH 会话当复核方的实测 - llm_verifier.should_keep(): 按强度决定保留哪些边 strict 只留模型判

## README 摘录

数字人文叙事 AI 分析引擎

> 基于大语言模型的叙事文本分析：人物关系网络抽取与可视化、人物画像与叙事生成。

功能

- **人物关系网络**：从文本中抽取人物关系，生成交互式关系图（vis-network）
- **人物画像**：LLM 驱动的角色分析
- **叙事生成**：AI 叙事报告与命运推演

入口

| 入口 | 说明 |
| `ai_cli.py` | 终端 CLI（typer + rich，美观排版） |
| `app.py` | Streamlit Web 界面 |
| `examples/` | 示例分析（如名著人物关系网络） |

技术栈

Python（Streamlit / NetworkX / Typer）+ 前端 React（Vite + TypeScript）。

示例

python ai_cli.py --help
streamlit run app.py

环境变量（审计后新增）

| 变量 | 默认 | 作用 |
| `CORS_ORIGINS` | `http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173,http://127.0.0.1:5173` | CORS 白名单，逗号分隔。原来是 `*`（配合 `allow_credentials=True` 实际会被浏览器拒绝） |
| `MAX_UPLOAD_MB` | `5` | 上传 txt 上限，超了返回 413，不会整份读进内存 |
| `TASKS_DB_PATH` | `tasks.db` | 任…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

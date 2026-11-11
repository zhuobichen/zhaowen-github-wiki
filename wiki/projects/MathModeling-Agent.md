---
name: MathModeling-Agent
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-05
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# MathModeling-Agent

> 数学建模竞赛数据分析题全流程自动化系统（多 Agent 流水线）

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | ai-agent, llm, math-modeling, multi-agent, python |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/MathModeling-Agent |

## 最近一次提交

`18b3f50` 2026-08-16 — chore: 清理死代码 - 删除 workflow.py 中未使用的 _run_modeler 方法（实际用 _run_modeler_with_feedback） - 删除 workflow.py

## README 摘录

数学建模竞赛 · 数据分析题全流程自动化系统

> 从输入题目到输出完整论文的多 Agent 自动求解 Pipeline。

定位

面向数学建模竞赛数据分析类题目，覆盖「题目解析 → 数据理解 → 建模方案 → 代码实现 → 结果验证 → 论文生成」全流程，由多个 LLM Agent 协作完成。

架构

| 模块 | 职责 |
| `backend/app/core/agents/` | 多角色 Agent（建模 / 编码 / 解析 / 评审 / 写作） |
| `backend/app/core/workflow.py` | 流水线编排 |
| `backend/app/tools/` | 本地解释器、文献检索、网页搜索等工具 |
| `backend/skills/` | 各阶段提示词与参考规范 |
| `backend/main.py` | 服务入口 |

技术栈

Python + FastAPI + Redis + LLM（多模型），支持本地代码执行与 notebook 序列化。

文档

- `数学建模数据分析自动化系统设计文档.md` — 完整设计文档

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

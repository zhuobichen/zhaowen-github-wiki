---
name: PM25-Fusion-AutoResearch
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-05
category: 科研 / 环境
archived: false
updated: 2026-11-11
---

# PM25-Fusion-AutoResearch

> PM2.5 监测-模型数据融合自动研究框架（VNA/eVNA/aVNA/Downscaler 复现与验证）

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | air-quality, data-fusion, machine-learning, pm25 |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/PM25-Fusion-AutoResearch |

## 最近一次提交

`db47310` 2026-11-05 — fix(metrics): 校验形状与有效样本数；单样本 R² 显式 nan；去掉 sklearn 依赖 - 长度不一致直接 ValueError，不再隐式广播 - 返回值新增 n（有效样本数），比较

## README 摘录

PM2.5 · CMAQ Data Fusion

**自动化 PM2.5 数据融合研究系统**

`文献分析` → `方案设计` → `代码实现` → `测试验证` → `论文生成`

Quick Start

查看流水线状态 + 产物检测
python run_pipeline.py --status

闭环模式（默认）：生成任务描述，由 TRAE Agent 执行
python run_pipeline.py --auto --backend trae --skip 1

CLI 模式（向后兼容）：通过 Claude CLI 自动执行
python run_pipeline.py --auto --backend cli --skip 1

只跑验证（直接执行 Python 脚本，不需要 Agent）
python run_pipeline.py --auto --only 5

使用预置配置
python run_pipeline.py --auto --profile skip-download

Pipeline Architecture (v14.0 闭环工作流)

│   Phase 2    │     │   Phase 3    │     │   Phase 4    │     │   Phase 5    │
│   文献分析    │────→│   方案设计    │────→│   代码实现    │────→│   测试验证    │
│   Task Disp.  │     │   Task Disp.  │     │   Task D…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

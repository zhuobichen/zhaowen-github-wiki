---
name: guangdong-wrf-cmaq
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-08-16
category: 科研 / 环境
archived: false
updated: 2026-11-11
---

# guangdong-wrf-cmaq

> 广东省 WRF-CMAQ 空气质量多尺度模拟与评估

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-08-16 |
| 话题 | air-quality, atmospheric-modeling, guangdong, wrf-cmaq |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/guangdong-wrf-cmaq |

## 最近一次提交

`e6ab22d` 2026-08-16 — fix: 恢复被误删的 CLAUDE.md

## README 摘录

Guangdong WRF-CMAQ

> 广东省空气质量多尺度模拟与评估 — CMAQ/WRF 建模、排放处理、气象-化学校验

项目定位

以广东省（含珠三角、惠州）为研究区域，进行三层嵌套网格（D1 27km / D2 9km / D3 3km）的 WRF-CMAQ 空气质量模拟。涵盖气象驱动、排放处理、模型运行、校验全流程，含排放情景对比和热浪分析专项。

关键技术

| 技术 | 用途 |
| WRF v3.9.1+ | 气象场模拟 |
| CMAQ v5.3 / v5.4 | 空气质量模拟（O3/PM2.5/NO2） |
| MEGAN v3.2 | 生物源排放 |
| MCIP | 气象-化学接口处理 |
| MEIC / EDGAR | 人为排放清单 |

目录结构

GuangDong/
├── Core_Extract.py       — CMAQ/WRF/MCIP 数据提取核心
├── Core_Map.py           — 空间地图绘制
├── Core_Charts.py        — 统计图表（箱线图/柱状图）
├── Core_Mask.py          — 区域掩膜处理
├── Core_PDF.py           — PDF 分布图
├── Run_Extract.py        — 数据提取入口
├── Run_Mask.py           — 掩膜处理入口
├── Data/                 ← 输入数据（CMAQ/WRF/监测）
├── cmaqout_processed/    ← C…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

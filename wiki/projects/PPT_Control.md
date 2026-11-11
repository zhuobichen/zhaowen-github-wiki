---
name: PPT_Control
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-05
category: 工具 / CLI
archived: false
updated: 2026-11-11
---

# PPT_Control

> 基于 Markdown 模板与提示词的 PPT 自动化组装工作台

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | ai, automation, markdown, ppt, prompt-engineering |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/PPT_Control |

## 最近一次提交

`bd5c936` 2026-11-05 — fix(security): 生成代码执行前静态审查 + 禁网禁子进程沙箱 - 执行前扫描外部进程/网络/动态执行/越界文件操作，命中需 PPT_ASSEMBLE_FORCE=1 - 子进程注入守卫：

## README 摘录

PPT 自动化组装工作台

> 基于 Markdown 模板与提示词，批量生成与组装演示文稿（PPT）。

功能

- `PPT组装工作台/assemble.py` — PPT 组装主脚本
- 各专题模块通过 `build.py` + prompts 驱动生成
- 配套讲稿与 PPT 制作规范文档

目录

| 目录 | 说明 |
| `PPT组装工作台/` | 通用组装工具 |
| `京津冀平台ppt/` | 京津冀平台各专题 PPT |
| `PPT制作规范.md` | 制作规范 |

技术栈

Python（python-pptx 等），Markdown → PPT 自动化流水线。

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

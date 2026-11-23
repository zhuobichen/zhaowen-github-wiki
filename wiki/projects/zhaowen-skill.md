---
name: zhaowen-skill
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-22
category: AI / Agent / 插件
archived: false
updated: 2026-11-23
---

# zhaowen-skill

> 可复用 Skill 集合（Claude Code / Agent Skill 格式）：文档转换、公众号操作、视频分析、科研工具等。

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-22 |
| 话题 | — |
| License | — |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-skill |

## 最近一次提交

`6a315ec` 2026-11-22 — second-screen-display: locate remote window by process (not title), restore minimized display window

## README 摘录

zhaowen-skill

可复用 Skill 集合（Claude Code / Agent Skill 格式）。

带来源前缀（作者标明归属）

| Skill | 目录 | 用途 |
| 英雄联盟「海克斯大乱斗」(海斗/ARAM | [`aram-mayhem-assistant/`](aram-mayhem-assistant/) | 英雄联盟「海克斯大乱斗」(海斗/ARAM) 分析助手：数对局、复盘单局、查符文与英雄、看趋势/画像/出装/对位/队友、跨 |
| docx 整页替换 | [`docx-page-replace/`](docx-page-replace/) | 在 .docx 里按**文本锚点**删掉一段正文（段落或表格行），原位插入「一图一页」的图片：把空白考核表页换成签字盖章扫描件、把整节换成扫描附件、往报告末尾插几页图。纯标准库实现（不需要 python-docx），带 `list` / `replace` / `check` 三个子命令；拒绝歧义锚点、拒绝覆盖原文件，`check` 校验 zip/XML/关系引用/图片是否超出版心。三个真踩过的坑写在 SKILL.md 里（DrawingML 命名空间、删表要补闭合标签、图宽贴满会多挤出一页） |
| docx 转公众号（clz） | [`docx_to_mp/`](docx_to_mp/) | 把 docx 转成公众号图文并推送草稿箱：解析 → 渲染微信兼容 HTML → 推送。内容忠实保留只做样式；含横滑相册、GIF 动效、平台硬限制实测记录 |
| 科研文献证据工程（ylx） | [`rese…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

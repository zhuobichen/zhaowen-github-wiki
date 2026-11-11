---
name: Ember
visibility: public
language: JavaScript
stars: 0
forks: 0
last_push: 2026-11-05
category: AI / Agent / 插件
archived: false
updated: 2026-11-11
---

# Ember

> 从聊天记录中用 AI 生成人生纪念碑的数字悼亡工具

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | JavaScript |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | ai, chat-analysis, digital-memorial, nlp |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/Ember |

## 最近一次提交

`84be37e` 2026-11-05 — docs(schema): 示例群号换成占位

## README 摘录

余烬 Ember

从一个人的聊天记录中，AI 生成一座属于他的人生纪念碑
然后把原始数据用火烧掉

安装 ·
快速开始 ·
消息提取 ·
纪念碑谷 ·
名人数据集

这是什么

**余烬** 是一个数字时代的悼亡工具。

它读取一个人的聊天记录（微信、QQ、飞书、QQ空间），用 AI 从中提炼出人生的轨迹、性格、关系网络，生成一篇叙事体的**人生纪念碑**，然后将原始数据多遍覆写并删除（best-effort，见下文「擦除能力的边界」），只留下纪念碑本身。

聊天记录是骨灰，AI 是雕塑师，纪念碑是最终留存物。

核心特性

- **多平台消息提取** — 微信（数据库直读解密 / weflow-cli）、QQ（OneBot API / qce 导出）、飞书（lark-cli 用户身份）、QQ空间（qce qzone，回落内置 HTTP）、贴吧/知乎（浏览器抓页面）、B站（MCP 采集器）
- **AI 纪念碑生成** — 基于 DeepSeek / Claude，四层分析架构：统计概览 → 年度抽样 → 人物画像 → 叙事体纪念碑文
- **离线流程** — 没有 API Key 也能出真东西：导出 → 汇总 → 筛选 → 渲染，每步都有中间产物
- **数据焚毁** — 分块多遍覆写 + 删除，生成可审计的操作报告（best-effort，非物理级不可恢复）
- **名人数据集** — 内置李白、苏轼、张雪峰等多维度数据集，无需个人数据即可体验
- **纪念碑谷平台** — Express + React + SQLite 全栈应用，可在线展示和分享纪念碑

安装

环境…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

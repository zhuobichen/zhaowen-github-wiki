---
name: zhaowen-otherplugins
visibility: public
language: Python
stars: 0
forks: 0
last_push: 2026-11-12
category: AI / Agent / 插件
archived: false
updated: 2026-11-16
---

# zhaowen-otherplugins

> 其他 Zotero/工具类插件合集。目前包含 Collection Tags：在条目列表创建者右侧显示所属集合的彩色标签。

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Python |
| ⭐ Star | 0 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-12 |
| 话题 | — |
| License | — |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/zhaowen-otherplugins |

## 最近一次提交

`34873c4` 2026-11-12 — feat(litmap): 布局填满画布、地理悬停列文献、新增分析标签页 引用网络与语义地图： 两处都用 s = Math.min(sx,sy) 等比缩放。画布 1414x690（约 2:1）而布局是

## README 摘录

Collection Tags — 在文献列表里显示所属分类

Zotero 插件。在条目列表的**创建者右侧**新增一列 **Category**，把每篇文献所属的集合显示成彩色层级标签。

标题                                 | 创建者       | Category                        | 年份
Effects of using different exposu…   | Wang, C.     | 应用 › 健康与暴露影响            | 2021
A comparison of statistical and m…   | Berrocal, V. | 应用 › 产品互比与选择敏感性      | 2020
Residual corrective diffusion mod…   | Mardani, M.  | 方法 › 深度学习                 | 2025

为什么需要它

Zotero 的集合（collection）行为像标签——一篇文章可以同时属于多个集合，但列表里只看得到标题和元数据，
看不出它被分到了哪。要看分类得点开右侧面板，逐条翻。这个插件把那层信息提到列表里，一眼可见。

设计

| 特性 | 说明 |
| **层级显示** | 一级（方法 / 应用）+ 子类两段胶囊，如 `方法 › 统计地统计` |
| **一级一色** | 方法 = Nature 深蓝 `#3C5488`，应用 = Nature 朱红 `#E64B35`。同一级下所有子类共用该色，不靠分辨…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

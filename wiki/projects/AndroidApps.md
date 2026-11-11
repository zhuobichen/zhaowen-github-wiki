---
name: AndroidApps
visibility: public
language: Java
stars: 1
forks: 0
last_push: 2026-11-05
category: 工具 / CLI
archived: false
updated: 2026-11-11
---

# AndroidApps

> MapMate（小德地图）：把高德地图和 DeepSeek Agent 合成一个能陪你的骑行导航助手。Android / Java / Material3

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | Java |
| ⭐ Star | 1 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-11-05 |
| 话题 | — |
| License | — |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/AndroidApps |

## 最近一次提交

`80ccc79` 2026-11-05 — fix(security): AMap Key 与签名口令改为本地注入；关闭明文流量 - AMap Key 走 manifestPlaceholders（local.properties / 环境变量

## README 摘录

Android Apps

我的安卓应用开发仓库。每个 App 一个子目录，各自独立构建。

| App | 说明 | 技术栈 | 状态 |
| [MapMate](MapMate/) | 会说话的手机地图：高德地图 + DeepSeek Agent，主打骑行导航与记录 | Java · Material3 · 高德 SDK 10.0 · DeepSeek API | 自用可用 |
| [卷灵 / JuanLing](VideoQuiz/) | 拍一段试卷录像 → 交给自己的电脑解析 → 回传答案与 PDF（原 VideoQuiz） | Java · Material3 · 本地 DSH 桥接 · PdfRenderer | v3.0 |

下载

APK 在 [Releases](https://github.com/zhuobichen/AndroidApps/releases) 页面。

> **卷灵只装 APK 不能用**：真正读题、解题、排版 PDF 都在你自己的电脑上跑，
> 电脑端需要 Node.js + DSH + 一个第三方插件 + 桥接服务。
> 完整部署步骤与自检脚本见 [VideoQuiz/bridge/README.md](VideoQuiz/bridge/README.md)。
> MapMate 则需要在 App 内填 DeepSeek Key（或自建小智服务端），以及高德 Key。

两个 App 的形态不一样

| | MapMate | 卷灵 |
| 算力在哪 | 手机 + 云端 API（或自建语音服务端） | **电脑本地**，手机只是遥控…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

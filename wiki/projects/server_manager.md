---
name: server_manager
visibility: public
language: JavaScript
stars: 1
forks: 0
last_push: 2026-09-02
category: 工具 / CLI
archived: false
updated: 2026-11-11
---

# server_manager

> （无描述）

| 项 | 值 |
| --- | --- |
| 可见性 | 公开 |
| 语言 | JavaScript |
| ⭐ Star | 1 |
| 🍴 Fork | 0 |
| 最近推送 | 2026-09-02 |
| 话题 | — |
| License | MIT |
| 主页 | — |
| 仓库 | https://github.com/zhuobichen/server_manager |

## 最近一次提交

`6404135` 2026-09-02 — feat: persist SSH connection status and require explicit retries

## README 摘录

文件管理 Skill v2.3

> 本地文件管理 + 通过 SSH 免密管理 Ubuntu 服务器文件。
> **完整 MCP 协议支持**,Claude Code / WorkBuddy / QoderWork / KIMIWork 等任意 MCP 客户端可用。

核心能力

| 类别 | 功能 |
| **本地文件** | 搜索、重命名、整理、统计 |
| **远程 CRUD** | 创建/读取/更新/删除/上传/下载 |
| **远程批量** | 模式匹配 + 大小过滤 + 内容搜索 |
| **文件共享** | ACL 三级权限(read / readwrite / admin) |
| **沙箱安全** | Home 锁死 + 系统目录黑名单 + 命令黑名单 + 二次确认 |
| **自动审计** | JSONL 格式,记录所有敏感/危险操作 |
| **即插即用** | 向导 + 配置文件 + doctor 自检 + 友好错误 |

平台支持

- ✅ Windows(开发机)
- ✅ Linux(服务器/桌面)
- ❌ macOS(不在测试矩阵)

5 分钟上手

1. 安装依赖(一次性,持久化到 `~/.file-manager/lib/`)

node scripts/install.js

2. 绑定服务器(交互式向导)

node scripts/ssh-ops.js init

按提示输入 server-id / IP / 端口 / 账号 / 密码,完成后自动生成 4096 位 RSA 密钥对并注入公钥。

**或命令行**:

node script…

## 备注（人工）

<!-- manual:begin -->

<!-- manual:end -->

# 赵文的 GitHub 项目索引

自动生成、每周刷新的**公开项目**导航，方便按关键词、语言、热度找到具体项目。

> 生成时间随每次刷新变化；内容由 `scripts/build_wiki.py` 从 GitHub API 抓取，**只收录公开仓库**。

## 从哪里开始

| 想做的事 | 看这里 |
| --- | --- |
| 浏览全部项目一览 | [`wiki/README.md`](wiki/README.md) |
| 按关键词搜 | `grep -ri "关键词" wiki/projects/` |
| 看某个项目详情 | [`wiki/projects/`](wiki/projects/) |
| 拿结构化数据 | [`wiki/_data.json`](wiki/_data.json) |

## 每个项目页包含

元数据（可见性 / 语言 / Star / Fork / 最近推送 / 话题 / License / 仓库地址）、最近一次提交、README 摘录，以及一个人工备注区。

## 检索示例

```bash
# 全文搜（描述、README 摘录、备注都能命中）
grep -ri "微信" wiki/projects/

# 按语言 / 可见性 / 归档状态筛
grep -l "language: Python" wiki/projects/*.md
grep -l "archived: true" wiki/projects/*.md
```

`wiki/_data.json` 是全量结构化数据，字段：`name` / `visibility` / `description` / `category` / `language` / `stars` / `forks` / `archived` / `pushed_at` / `topics` / `license` / `url` / `last_commit`。

## 更新机制

`.github/workflows/weekly-wiki.yml` 每周一 09:00（Asia/Shanghai）运行，也可以在 Actions 页面手动触发。
内容没有实质变化时不写文件、也不产生提交。

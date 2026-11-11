#!/usr/bin/env python3
"""生成 GitHub 项目 wiki（可检索、按周刷新）。

产出（默认 wiki/）：
  README.md              索引：总览 + 分组 + 全量表格
  _data.json             机器可读全量字段（给检索/RAG 用）
  projects/<仓库名>.md    每仓库一页：front-matter + 元数据 + 最近提交 + README 摘录

人工区约定：项目页里 <!-- manual:begin --> ... <!-- manual:end --> 之间的内容
由人维护，本脚本**不覆盖**（文件不存在时留空块）。

用法:
  python build_wiki.py --out ./wiki
  python build_wiki.py --out ./wiki --only weflow-cli
"""
import argparse
import base64
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OWNER = 'zhuobichen'
SELF_REPO = 'zhaowen-github-diary'          # 本 wiki 所在的仓库：给自己建页会自引用
WIKI_COMMIT_PREFIXES = ('docs(wiki)', 'fix(wiki)', 'docs: weekly wiki')
MANUAL_BEGIN = '<!-- manual:begin -->'
MANUAL_END = '<!-- manual:end -->'

CATEGORY_RULES = [
    ('微信 / 数据采集', r'wechat|weflow|qchat|微信|chat'),
    ('AI / Agent / 插件', r'agent|dsh|mcp|skill|codex|claude|llm|\bai\b|plugin|prompt'),
    ('科研 / 环境', r'cmaq|wrf|pm25|air[-_]?quality|abacas|datafusion|epa|paper|fusion|modeling|kriging'),
    ('阅读 / 知识库', r'reader|knowledge|wiki|note|diary|知识'),
    ('工具 / CLI', r'cli|tool|manager|hub|control|apps'),
]


def gh(args):
    p = subprocess.run(['gh'] + args, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    if p.returncode != 0:
        return None
    return p.stdout


def category_of(repo):
    """先按仓库名判（名字最能定性），判不出再看描述/话题。"""
    name = repo['name'].lower()
    for cat, pat in CATEGORY_RULES:
        if re.search(pat, name):
            return cat
    hay = ' '.join(filter(None, [repo.get('description') or '',
                                ' '.join(repo.get('topics') or [])])).lower()
    for cat, pat in CATEGORY_RULES:
        if re.search(pat, hay):
            return cat
    return '其他'


def fetch_repos(owner):
    out = gh(['repo', 'list', owner, '--limit', '300', '--json',
              'name,nameWithOwner,description,visibility,isArchived,primaryLanguage,'
              'stargazerCount,forkCount,pushedAt,createdAt,repositoryTopics,licenseInfo,homepageUrl'])
    if not out:
        sys.exit('gh repo list 失败（检查 gh 登录 / GH_TOKEN）')
    return json.loads(out)


def _commit_row(parts):
    msg = parts[1].replace('\\r', ' ').replace('\\n', ' ').replace('\\t', ' ')
    msg = re.sub(r'\s+', ' ', msg).strip()[:100]
    return {'sha': parts[0], 'message': msg, 'date': parts[2][:10]}


def last_commit(nwo, skip_wiki_commits=False):
    if not skip_wiki_commits:
        out = gh(['api', f'repos/{nwo}/commits?per_page=1',
                  '--jq', '.[0] | [.sha[0:7], .commit.message, .commit.author.date] | @tsv'])
        if not out or not out.strip():
            return None
        parts = out.strip().split('\t')
        if len(parts) < 3:
            return None
        return _commit_row(parts)

    # 本仓库自己：跳过"纯 wiki 刷新"的提交，否则每次生成都会看到上一次生成
    out = gh(['api', f'repos/{nwo}/commits?per_page=30',
              '--jq', '.[] | [.sha[0:7], .commit.message, .commit.author.date] | @tsv'])
    if not out:
        return None
    for line in out.splitlines():
        parts = line.split('\t')
        if len(parts) < 3:
            continue
        msg = parts[1].replace('\\n', ' ').strip()
        if any(msg.startswith(p) for p in WIKI_COMMIT_PREFIXES):
            continue
        return _commit_row(parts)
    return None


def repo_license(nwo):
    """repo list 的 licenseInfo 对不少仓库返回空（实测 weflow-cli 有 MIT 却为空），
    改用 /license 端点。"""
    out = gh(['api', f'repos/{nwo}/license', '--jq', '.license.spdx_id'])
    return out.strip() if out and out.strip() and out.strip() != 'null' else None


def readme_excerpt(nwo, limit=700):
    out = gh(['api', f'repos/{nwo}/readme', '--jq', '.content'])
    if not out:
        return ''
    try:
        raw = base64.b64decode(out.strip()).decode('utf-8', 'replace')
    except Exception:
        return ''
    # 去掉徽章、图片、HTML 注释、标题前的多余空行
    lines = []
    for ln in raw.split('\n'):
        s = ln.strip()
        if not s:
            if lines and lines[-1] != '':
                lines.append('')
            continue
        if re.match(r'^\[!\[|^!\[|^<img|^<p|^<div|^<!--', s):
            continue
        if s.startswith('```'):
            continue
        s = re.sub(r'<[^<>]+>', '', s).strip()   # 去掉行内 HTML 标签（如 <h1>、<img>）
        s = re.sub(r'^#+\s*', '', s)
        if not s or re.fullmatch(r'[\W_·•\-\*\s]+', s):
            continue
        lines.append(s)
    text = '\n'.join(lines).strip()
    return text[:limit] + ('…' if len(text) > limit else '')


def extract_manual(path):
    if not os.path.exists(path):
        return ''
    with open(path, encoding='utf-8') as fh:
        cur = fh.read()
    m = re.search(re.escape(MANUAL_BEGIN) + r'(.*?)' + re.escape(MANUAL_END), cur, re.S)
    return m.group(1).strip('\n') if m else ''


def render_project(r, commit, excerpt, manual, lic):
    vis = '公开' if r['visibility'] == 'PUBLIC' else '私有'
    lang = (r.get('primaryLanguage') or {}).get('name') or '—'
    topics = ', '.join(t['name'] for t in (r.get('repositoryTopics') or [])) or '—'
    home = r.get('homepageUrl') or '—'
    desc = r.get('description') or '（无描述）'

    fm = [
        '---',
        f'name: {r["name"]}',
        f'visibility: {"public" if r["visibility"] == "PUBLIC" else "private"}',
        f'language: {lang}',
        f'stars: {r["stargazerCount"]}',
        f'forks: {r["forkCount"]}',
        f'last_push: {(r.get("pushedAt") or "")[:10]}',
        f'category: {category_of(r)}',
        f'archived: {"true" if r["isArchived"] else "false"}',
        f'updated: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}',
        '---',
        '',
        f'# {r["name"]}',
        '',
        f'> {desc}',
        '',
        '| 项 | 值 |',
        '| --- | --- |',
        f'| 可见性 | {vis} |',
        f'| 语言 | {lang} |',
        f'| ⭐ Star | {r["stargazerCount"]} |',
        f'| 🍴 Fork | {r["forkCount"]} |',
        f'| 最近推送 | {(r.get("pushedAt") or "")[:10]} |',
        f'| 话题 | {topics} |',
        f'| License | {lic or "—"} |',
        f'| 主页 | {home} |',
        f'| 仓库 | https://github.com/{r["nameWithOwner"]} |',
        '',
    ]
    if commit:
        fm += ['## 最近一次提交', '',
               f'`{commit["sha"]}` {commit["date"]} — {commit["message"]}', '']
    if excerpt:
        fm += ['## README 摘录', '', excerpt, '']
    fm += [
        '## 备注（人工）',
        '',
        MANUAL_BEGIN,
        manual,
        MANUAL_END,
        '',
    ]
    return '\n'.join(fm)


def render_index(repos, updated):
    total = len(repos)
    pub = sum(1 for r in repos if r['visibility'] == 'PUBLIC')
    stars = sum(r['stargazerCount'] for r in repos)
    forks = sum(r['forkCount'] for r in repos)
    archived = sum(1 for r in repos if r['isArchived'])

    L = ['# GitHub 项目 Wiki', '',
         f'> 自动生成，每周刷新。最后更新：{updated}',
         '> 生成脚本：`scripts/build_wiki.py`｜机器可读数据：`_data.json`', '',
         '## 总览', '',
         '| 指标 | 值 |', '| --- | --- |',
         f'| 仓库总数 | {total} |',
         f'| 公开 / 私有 | {pub} / {total - pub} |',
         f'| 归档 | {archived} |',
         f'| 总 Star | {stars} |',
         f'| 总 Fork | {forks} |', '',
         '## 怎么搜', '',
         '```bash',
         '# 按关键词搜全部项目页（描述、README 摘录、备注都在里面）',
         'grep -ri "关键词" wiki/projects/',
         '',
         '# 按语言或可见性筛',
         'grep -l "language: Python" wiki/projects/*.md',
         'grep -l "visibility: private" wiki/projects/*.md',
         '```', '',
         '## 全量索引（按 Star 降序）', '',
         '| 项目 | 分类 | 可见 | 语言 | ⭐ | 🍴 | 最近推送 | 一句话 |',
         '| --- | --- | --- | --- | --- | --- | --- | --- |']

    for r in sorted(repos, key=lambda x: (-x['stargazerCount'], x['name'].lower())):
        vis = '公开' if r['visibility'] == 'PUBLIC' else '私有'
        lang = (r.get('primaryLanguage') or {}).get('name') or '—'
        desc = (r.get('description') or '').strip().replace('|', '/').replace('\n', ' ')
        if not desc:
            desc = '（无描述）'
        if len(desc) > 40:
            desc = desc[:40] + '…'
        name = r['name'] + ('（已归档）' if r['isArchived'] else '')
        L.append(f'| [{name}](projects/{r["name"]}.md) | {category_of(r)} | {vis} | {lang} | '
                 f'{r["stargazerCount"]} | {r["forkCount"]} | {(r.get("pushedAt") or "")[:10]} | {desc} |')

    L += ['', '## 按分类', '']
    by_cat = {}
    for r in repos:
        by_cat.setdefault(category_of(r), []).append(r)
    for cat in [c for c, _ in CATEGORY_RULES] + ['其他']:
        items = by_cat.get(cat)
        if not items:
            continue
        L += [f'### {cat}（{len(items)}）', '']
        for r in sorted(items, key=lambda x: -x['stargazerCount']):
            desc = (r.get('description') or '').strip()
            L.append(f'- [{r["name"]}](projects/{r["name"]}.md) — {desc or "（无描述）"}')
        L.append('')
    return '\n'.join(L)


def normalize(text):
    """比较"实质内容"时忽略时间戳类行，避免每周都因为 updated 日期产生无意义提交。"""
    out = []
    for ln in text.split('\n'):
        if re.match(r'^updated:\s*\d{4}-\d{2}-\d{2}\s*$', ln):
            continue
        if ln.startswith('> 自动生成，每周刷新。最后更新：'):
            continue
        out.append(ln)
    return '\n'.join(out)


def write_if_changed(path, text):
    """内容没变就不碰文件（时间戳行不算内容）。返回是否真的写了。"""
    if os.path.exists(path):
        with open(path, encoding='utf-8') as fh:
            if normalize(fh.read()) == normalize(text):
                return False
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    return True


def fetch_public_repos(owner):
    """只取公开仓库（走 users/{owner}/repos，任何 token 或无 token 都能用，
    且天然不含私有仓库 —— 公开库的 wiki 只能走这条，避免误把私有项目推上去）。"""
    out = gh(['api', f'users/{owner}/repos?per_page=100&type=owner', '--paginate'])
    if not out:
        sys.exit('gh api users/{owner}/repos 失败')
    try:
        raw = json.loads(out)
    except Exception:
        # --paginate 会把多页 JSON 拼起来，这里逐段解析
        raw = []
        dec = json.JSONDecoder()
        i = 0
        while i < len(out):
            obj, j = dec.raw_decode(out, i)
            raw.extend(obj if isinstance(obj, list) else [obj])
            i = j
            while i < len(out) and out[i] in ' \n\r\t':
                i += 1
    repos = []
    for r in raw:
        if r.get('fork'):
            continue
        repos.append({
            'name': r['name'],
            'nameWithOwner': r['full_name'],
            'description': r.get('description'),
            'visibility': 'PUBLIC' if not r.get('private') else 'PRIVATE',
            'isArchived': r.get('archived', False),
            'primaryLanguage': {'name': r['language']} if r.get('language') else None,
            'stargazerCount': r.get('stargazers_count', 0),
            'forkCount': r.get('forks_count', 0),
            'pushedAt': r.get('pushed_at'),
            'createdAt': r.get('created_at'),
            'repositoryTopics': [{'name': t} for t in (r.get('topics') or [])],
            'licenseInfo': {'spdxId': (r.get('license') or {}).get('spdx_id')} if r.get('license') else None,
            'homepageUrl': r.get('homepage'),
        })
    return [r for r in repos if r['visibility'] == 'PUBLIC']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='wiki')
    ap.add_argument('--owner', default=OWNER)
    ap.add_argument('--only', default=None, help='只生成某个仓库（调试用）')
    ap.add_argument('--public-only', action='store_true',
                    help='只收录公开仓库（用于公开库，绝不包含私有项目）')
    ap.add_argument('--self-repo', default=SELF_REPO,
                    help='wiki 自身所在的仓库名：它不追踪自己的 pushed_at，避免自引用 churn')
    args = ap.parse_args()

    repos = fetch_public_repos(args.owner) if args.public_only else fetch_repos(args.owner)
    # gh repo list 的返回顺序不稳定（实际按 pushedAt 排序，会变），
    # 不排序的话 _data.json 每次顺序都不同 —— 周更就会产生无意义的提交。
    repos = sorted(repos, key=lambda r: r['name'].lower())
    if args.only:
        repos = [r for r in repos if r['name'] == args.only]

    os.makedirs(os.path.join(args.out, 'projects'), exist_ok=True)
    updated = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    data = []
    for i, r in enumerate(repos, 1):
        nwo = r['nameWithOwner']
        path = os.path.join(args.out, 'projects', f'{r["name"]}.md')
        manual = extract_manual(path)
        is_self = r['name'] == args.self_repo
        commit = last_commit(nwo, skip_wiki_commits=is_self)
        if is_self and commit:
            # 自己这一页不能用 pushedAt：wiki 每提交一次它就会变 —— 那是自引用
            r['pushedAt'] = commit['date'] + 'T00:00:00Z'
        excerpt = readme_excerpt(nwo)
        lic = repo_license(nwo)
        write_if_changed(path, render_project(r, commit, excerpt, manual, lic))
        data.append({
            'name': r['name'],
            'full_name': nwo,
            'visibility': r['visibility'],
            'description': r.get('description') or '',
            'category': category_of(r),
            'language': (r.get('primaryLanguage') or {}).get('name'),
            'stars': r['stargazerCount'],
            'forks': r['forkCount'],
            'archived': r['isArchived'],
            'pushed_at': r.get('pushedAt'),
            'created_at': r.get('createdAt'),
            'topics': [t['name'] for t in (r.get('repositoryTopics') or [])],
            'license': lic,
            'homepage': r.get('homepageUrl'),
            'url': f'https://github.com/{nwo}',
            'last_commit': commit,
            'page': f'projects/{r["name"]}.md',
        })
        print(f'[{i}/{len(repos)}] {r["name"]}')

    if not args.only:
        # 清理孤儿页：仓库改名/删除后，旧页面不该留在 projects/ 里
        keep = {f'{r["name"]}.md' for r in repos}
        removed = []
        proj_dir = os.path.join(args.out, 'projects')
        if os.path.isdir(proj_dir):
            for fn in sorted(os.listdir(proj_dir)):
                if fn.endswith('.md') and fn not in keep:
                    os.remove(os.path.join(proj_dir, fn))
                    removed.append(fn)
        if removed:
            print(f'清理孤儿页 {len(removed)} 个: ' + ', '.join(removed))

        # _data.json 里的 generated_at 每次都变，但它不是内容；只有 repos 真变了才重写
        data_path = os.path.join(args.out, '_data.json')
        changed = True
        if os.path.exists(data_path):
            try:
                with open(data_path, encoding='utf-8') as fh:
                    old = json.load(fh)
                changed = (json.dumps(old.get('repos'), sort_keys=True, ensure_ascii=False)
                           != json.dumps(data, sort_keys=True, ensure_ascii=False))
            except Exception:
                changed = True
        if changed:
            with open(data_path, 'w', encoding='utf-8', newline='\n') as fh:
                json.dump({'generated_at': datetime.now(timezone.utc).isoformat(),
                           'owner': args.owner, 'count': len(data), 'repos': data},
                          fh, ensure_ascii=False, indent=1)
        else:
            print('_data.json 无实质变化，跳过重写')

        write_if_changed(os.path.join(args.out, 'README.md'), render_index(repos, updated))
        print(f'\n完成：{len(data)} 个仓库 → {args.out}')


if __name__ == '__main__':
    main()

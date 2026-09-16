# -*- coding: utf-8 -*-
"""把 easy-data-x-ai-notes 的 Markdown 笔记生成为 kaiyee 风格的蓝色静态站。"""
import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

TASKS = [
    dict(no="01", code="TASK 1", slug="task-1", name="环境准备与课前导读",
         plan=("2 天", "截止 09-17 03:00"), record="2026.09.15", status="已完成",
         diff=3, read=["F0：课前闲聊", "F1：大模型的本质与边界", "F2：AI Agent 的完整图景"],
         deck="完成环境自检与离线评测，并读完公共基础三篇（F0/F1/F2），建立「数据视角看 Agent」的认知框架。",
         req="完成 Shell、Python、模型 API、Git 环境自检并提交结果；课前导读与公共基础。"),
    dict(no="02", code="TASK 2", slug="task-2", name="场景识别 + RAG 产品设计 + AI 原生数据系统",
         plan=("3 天", "截止 09-20 03:00"), record="2026.09.16", status="进行中",
         diff=None, read=["P1：找准 Agent 的用武之地", "D1：让 Agent 会查资料 —— RAG 产品设计", "I1：AI 原生数据系统"],
         deck="拿到测试 API Key、装好 pyseekdb，并把 code/D1 的 d1_1~d1_6 六个示例全部跑通，走完「一次调用 → Agent 循环」的演进。",
         req="获取测试用 API Key；安装向量数据库 pyseekdb 的 SDK；跑通 code/D1 的 d1_1~d1_6 示例代码。"),
    dict(no="03", code="TASK 3", slug="task-3", name="RAG 产品设计 + RAG 与向量数据库",
         plan=("3 天", "截止 09-23 03:00"), record=None, status="待开始",
         diff=None, read=["P2：让 Agent 会查资料 —— RAG 产品设计", "I2：RAG 与向量数据库"],
         deck="了解 RAG 的基础流程，以及向量数据库中混合搜索的含义。",
         req="了解 RAG 的基础流程与向量数据库混合搜索含义；跑通 code/D2 的 d2_1~d2_2。"),
    dict(no="04", code="TASK 4", slug="task-4", name="AI Native 数据层与 AI Functions",
         plan=("3 天", "截止 09-26 03:00"), record=None, status="待开始",
         diff=None, read=["D2：统一 AI Native 数据层实战", "I3：SQL × AI —— AI Functions 的设计与执行"],
         deck="体验 Data 在 AI 应用里如何被承载（向量化、存储、查询），并在数据库里调用 AI。",
         req="跑通 code/D2 的 d2_1~d2_5；通过 pyseekdb 执行 AI Function。"),
    dict(no="05", code="TASK 5", slug="task-5", name="记忆系统与 File SQL",
         plan=("3 天", "截止 09-29 03:00"), record=None, status="待开始",
         diff=None, read=["P3：让 Agent 真正记住你 —— 记忆系统设计", "I4：File SQL for AI Agent"],
         deck="理解记忆系统存储关键 value 的原理，并体验 PowerContext 的记忆能力。",
         req="理解记忆系统原理，安装 PowerContext 并体验；完成 select from read_csv(xxx.csv) 流程。"),
    dict(no="06", code="TASK 6", slug="task-6", name="Agentic RAG 与 AI 列",
         plan=("3 天", "截止 10-02 03:00"), record=None, status="待开始",
         diff=None, read=["D3：实践出真知 —— Agentic RAG 实战", "I5：AI 列 —— 模型驱动派生数据的自动维护"],
         deck="走通 Agentic RAG 的完整链路，并在 pyseekdb 中创建与使用 AI 列。",
         req="跑通 code/D3 的 d3_1~d3_6；在 pyseekdb 创建并使用 AI 列。"),
    dict(no="07", code="TASK 7", slug="task-7", name="Skill 与上下文工程",
         plan=("3 天", "截止 10-05 03:00"), record=None, status="待开始",
         diff=None, read=["P4：Skill 与 Agent 知识管理", "I6：上下文工程概述"],
         deck="理解 Agent 上下文工程的核心概念与工作流程，并实践外部上下文管理工具。",
         req="理解上下文工程核心概念；基于 MCP / Skills / Agent Plugins 实践，以 PowerContext 为例完成安装与调用。"),
    dict(no="08", code="TASK 8", slug="task-8", name="Agent 记忆与 PowerContext",
         plan=("3 天", "截止 10-08 03:00"), record=None, status="待开始",
         diff=None, read=["D4：记哪些、忘哪些？—— Agent 记忆系统开发", "I7：PowerContext 的设计与实现"],
         deck="走通一个拥有完整记忆系统的 Agent 构建流程，理解工业实现思路。",
         req="跑通 code/D4 的 d4_1~d4_4；学习 PowerContext 项目设计。"),
    dict(no="09", code="TASK 9", slug="task-9", name="场景、总结与测评",
         plan=("3 天", "截止 10-11 03:00"), record=None, status="待开始",
         diff=None, read=["P5：Agent 场景识别", "D5：课程总结", "I8：案例场景和测评构建"],
         deck="通过典型案例掌握测评基本方法，并实践 PowerContext E2E 测评集构建。",
         req="了解上下文工程的场景应用与测评方法；用 PowerContext E2E 基于 Harbor 构建与迁移测评集。"),
]


# ---------- 极简 Markdown → HTML ----------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" loading="lazy">', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def md2html(md):
    out, i, lines = [], 0, md.split('\n')
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        # fenced code
        if s.startswith('```'):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre><code>' + html.escape('\n'.join(buf)) + '</code></pre>')
            continue
        # table
        if s.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            head = [c.strip() for c in s.strip('|').split('|')]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            t = ['<table><thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in head) + '</tr></thead><tbody>']
            for r in rows:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            t.append('</tbody></table>')
            out.append(''.join(t))
            continue
        if s.startswith('### '):
            out.append(f'<h3>{inline(s[4:])}</h3>'); i += 1; continue
        if s.startswith('## '):
            out.append(f'<h2>{inline(s[3:])}</h2>'); i += 1; continue
        if s.startswith('# '):
            out.append(f'<h2>{inline(s[2:])}</h2>'); i += 1; continue
        if s.startswith('> '):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append('<blockquote>' + inline(' '.join(buf)) + '</blockquote>')
            continue
        if re.match(r'^[-*] ', s):
            buf = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i].strip()):
                buf.append(f'<li>{inline(lines[i].strip()[2:])}</li>'); i += 1
            out.append('<ul>' + ''.join(buf) + '</ul>')
            continue
        if re.match(r'^\d+\. ', s):
            buf = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i].strip()):
                buf.append(f'<li>{inline(re.sub(r"^\d+\. ", "", lines[i].strip()))}</li>'); i += 1
            out.append('<ol>' + ''.join(buf) + '</ol>')
            continue
        if s in ('---', '***'):
            out.append('<hr>'); i += 1; continue
        if not s:
            i += 1; continue
        # paragraph (merge consecutive non-empty plain lines)
        buf = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|>|[-*] |\d+\. |\||```)', lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)


# ---------- 页面模板 ----------
HEAD = """<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{desc}" />
    <meta name="theme-color" content="#f4f7fb" />
    <title>{title}</title>
    <link rel="icon" href="{icon}favicon.svg" type="image/svg+xml" />
    <link rel="stylesheet" href="{css}styles.css" />
    <script src="{css}script.js" defer></script>
  </head>
"""


def head(prefix, title, desc):
    return HEAD.format(title=title, desc=desc, icon=prefix, css=prefix)


def header_bar(prefix_home):
    return f"""  <body>
    <a class="skip-link" href="#note-content">跳到正文</a>
    <div class="ambient ambient-a" aria-hidden="true"></div>
    <div class="ambient ambient-b" aria-hidden="true"></div>

    <header class="site-header">
      <a class="wordmark" href="{prefix_home}index.html" aria-label="返回首页顶部">
        <span class="wordmark-mark" aria-hidden="true">Z</span>
        <span>Zhang Bo's Study Archive</span>
      </a>
      <nav aria-label="主要导航">
        <a href="{prefix_home}index.html#learning-log">学习进度</a>
        <a href="https://github.com/datawhalechina/easy-data-x-ai" target="_blank" rel="noreferrer">课程仓库 <span aria-hidden="true">↗</span></a>
      </nav>
    </header>
"""


FOOTER = """    <footer>
      <p>Easy Data × AI 学习档案 · 张博</p>
      <p>内容整理自 Datawhale × OceanBase《Easy Data × AI》课程</p>
    </footer>
  </body>
</html>
"""


def diff_dots(n):
    if not n:
        return '<span class="unrecorded">未评价</span>'
    return ('<span class="difficulty"><span>' + ''.join('<i></i>' for _ in range(n)) +
            ''.join('<b></b>' for _ in range(5 - n)) + '</span><em style="font-style:normal">' + str(n) + '/5</em></span>')


def build_index():
    rows = []
    for t in TASKS:
        done = t['status'] == '已完成'
        locked = t['status'] == '待开始'
        cls = ' class="locked"' if locked else ''
        note_cell = (f'<a class="entry-link task-note-link" href="./notes/{t["slug"]}/"><span>任务笔记</span><b aria-hidden="true">↗</b></a>'
                     if not locked else '<span class="entry-link locked-entry"><span>任务笔记</span><b aria-hidden="true">🔒</b></span>')
        readings = ''.join(
            (f'<span class="entry-link locked-entry"><span>{html.escape(r)}</span><b aria-hidden="true">🔒</b></span>'
             if locked else f'<span class="entry-link" style="color:var(--muted);font-weight:400"><span>{html.escape(r)}</span><b aria-hidden="true"></b></span>')
            for r in t['read'])
        search = html.escape(t['name'] + ' ' + t['req'] + ' ' + ' '.join(t['read']), quote=True)
        rec = f'<time datetime="{t["record"]}">{t["record"]}</time><span>{t["status"]}</span>' if t['record'] else f'<span class="unrecorded">未记录</span><span>{t["status"]}</span>'
        rows.append(f"""                <tr{cls} data-search="{search}">
                  <td data-label="Task">
                    <span class="chapter-code">{t['code']}</span>
                    <strong class="task-name">{html.escape(t['name'])}</strong>
                  </td>
                  <td data-label="计划">
                    <div class="plan-cell">
                      <strong>{t['plan'][0]}</strong>
                      <span>{t['plan'][1]}</span>
                    </div>
                  </td>
                  <td data-label="学习记录">{rec}</td>
                  <td data-label="难度">{diff_dots(t['diff'])}</td>
                  <td data-label="任务与阅读笔记">
                    <div class="note-entry-stack">
                      {note_cell}
                      <div class="reading-links">{readings}</div>
                    </div>
                  </td>
                </tr>""")

    done_count = sum(1 for t in TASKS if t['status'] == '已完成')
    pct = int(done_count / 10 * 100)
    return head('', 'Easy Data × AI 学习档案 · 张博', '记录每个 Task 的完成情况、任务笔记与阅读笔记。') + header_bar('') + f"""
    <main>
      <section class="course-intro reveal" aria-labelledby="page-title">
        <div>
          <p class="eyebrow">LEARNING IN PUBLIC · 2026</p>
          <h1 id="page-title">EASY DATA × AI · TASK LOG</h1>
          <p class="course-deck">每个 Task 包含一篇任务笔记，以及对应的产品、开发者或产业应用阅读笔记。</p>
          <p class="course-source"><a href="https://github.com/datawhalechina/easy-data-x-ai" target="_blank" rel="noreferrer">学习内容来自 Datawhale 与 OceanBase 社区联合共建的《Easy Data x AI》。本站用于整理个人任务笔记与阅读随笔，感谢项目维护者与所有开源贡献者。↗</a></p>
        </div>
        <div class="course-progress" aria-label="课程学习进度 {done_count}/10">
          <div><span>已完成 Task</span><strong>0{done_count} / 10</strong></div>
          <div class="progress-line"><span style="width: {pct}%"></span></div>
          <p>学习周期 2026.09.14 – 10.11，共 29 天</p>
        </div>
      </section>

      <section class="log-section" id="learning-log" aria-labelledby="log-title">
        <h2 class="sr-only" id="log-title">完整学习进度</h2>

        <div class="table-toolbar reveal">
          <label class="search-field">
            <span class="sr-only">搜索学习任务</span>
            <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="m16 16 4 4"></path></svg>
            <input id="log-search" type="search" placeholder="搜索 Task、文章或任务要求" autocomplete="off" />
          </label>
          <span class="record-count" aria-live="polite"><b id="visible-count">10</b> 个 Task</span>
        </div>

        <div class="table-shell reveal">
          <table>
            <caption class="sr-only">Task 1 至 Task 9 的学习进度</caption>
            <thead>
              <tr>
                <th scope="col">Task</th>
                <th scope="col">计划</th>
                <th scope="col">学习记录</th>
                <th scope="col">难度</th>
                <th scope="col">任务与阅读笔记</th>
              </tr>
            </thead>
            <tbody id="log-body">
{chr(10).join(rows)}
              <tr hidden></tr>
            </tbody>
          </table>
          <p class="empty-state" id="empty-state" hidden>没有匹配的 Task。</p>
        </div>
      </section>
    </main>

""" + FOOTER


def rail(current_slug):
    items = []
    for t in TASKS:
        locked = t['status'] == '待开始'
        cur = t['slug'] == current_slug
        cls = 'current' if cur else ('locked' if locked else '')
        children = []
        if not locked:
            children.append(f'<a class="tree-note {cls}" href="../{t["slug"]}/"><span>任务笔记</span><b aria-hidden="true">↗</b></a>')
        else:
            children.append('<a class="tree-note locked" href="#"><span>任务笔记</span><b aria-hidden="true">🔒</b></a>')
        for r in t['read']:
            children.append(f'<span class="tree-reading {cls}"><span>{html.escape(r)}</span><i aria-hidden="true"></i></span>')
        items.append(f"""      <details class="task-tree" {'open' if cur else ''}>
        <summary class="{'active-task' if cur else ''}">
          <span>{t['code']}</span>
          <strong>{html.escape(t['name'])}</strong>
          <i aria-hidden="true"></i>
        </summary>
        <div class="task-tree-children">
          {chr(10).join(children)}
        </div>
      </details>""")
    return f"""      <aside class="chapter-rail reveal">
        <a class="back-link" href="../../index.html#learning-log">← 返回进度</a>
        <p class="eyebrow">TASK MAP</p>
        <nav class="chapter-list" aria-label="全部学习任务与阅读笔记">
{chr(10).join(items)}
        </nav>
      </aside>"""


def build_note(t, md):
    body = md2html(md)
    facts = f"""          <dl class="note-facts">
            <div><dt>计划</dt><dd>{t['plan'][0]}</dd></div>
            <div><dt>截止</dt><dd>{t['plan'][1].replace('截止 ', '')}</dd></div>
            <div><dt>状态</dt><dd>{t['status']}</dd></div>
            <div><dt>更新</dt><dd>{t['record'] or '—'}</dd></div>
          </dl>"""
    scope = ''.join(f'<span>{html.escape(x)}</span>' for x in t['read'])
    idx = TASKS.index(t)
    prev_t = TASKS[idx - 1] if idx > 0 else None
    next_t = TASKS[idx + 1] if idx < len(TASKS) - 1 else None
    prev_link = (f'<a href="../{prev_t["slug"]}/">← {prev_t["code"]}</a>' if prev_t and prev_t['status'] != '待开始'
                 else '<span style="color:var(--faint)">← 上一课</span>')
    next_link = (f'<a href="../{next_t["slug"]}/">{next_t["code"]} →</a>' if next_t and next_t['status'] != '待开始'
                 else '<span style="color:var(--faint)">下一课 →</span>')
    return head('../../', f"{t['name']} · Easy Data × AI 学习档案", t['deck']) + header_bar('../../') + f"""
    <main class="note-layout" id="note-content">
{rail(t['slug'])}

      <article class="note-article">
        <header class="note-title reveal">
          <p>{t['code']} · 学习笔记</p>
          <h1>{html.escape(t['name'])}</h1>
          <p class="note-deck">{html.escape(t['deck'])}</p>
{facts}
        </header>

        <section class="task-brief reveal">
          <p class="section-index">00</p>
          <div>
            <h2>任务要求</h2>
            <p>{html.escape(t['req'])}</p>
            <p class="task-scope">{scope}</p>
          </div>
        </section>

        <section class="reflection-section reveal">
          <p class="section-index">01</p>
          <div class="note-body">
{body}
          </div>
        </section>

        <footer class="note-footer">
          {prev_link}
          <a href="../../index.html#learning-log">全部 Task ↑</a>
          {next_link}
        </footer>
      </article>
    </main>

""" + FOOTER


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#3f7ae0"/><stop offset="1" stop-color="#20418f"/>
  </linearGradient></defs>
  <rect width="64" height="64" rx="14" fill="url(#g)"/>
  <text x="32" y="43" font-family="Georgia,serif" font-size="34" fill="#fff" text-anchor="middle">Z</text>
</svg>
"""


def main():
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(build_index())
    open(os.path.join(ROOT, 'favicon.svg'), 'w', encoding='utf-8').write(FAVICON)

    srcs = {
        'task-1': 'task1-环境准备与课前导读.md',
        'task-2': 'task2-场景识别与RAG产品设计.md',
    }
    for t in TASKS:
        d = os.path.join(ROOT, 'notes', t['slug'])
        os.makedirs(d, exist_ok=True)
        md = ''
        if t['slug'] in srcs and os.path.exists(os.path.join(ROOT, srcs[t['slug']])):
            md = open(os.path.join(ROOT, srcs[t['slug']]), encoding='utf-8').read()
            # 去掉一级标题（页面已有 h1）
            md = re.sub(r'^#\s+.*\n', '', md, count=1)
            md = md.replace('screenshots/', '../../screenshots/')
        if not md:
            md = f"## 待开始\n\n本 Task 尚未开始。完成后将在这里留下实践成果与学习笔记。\n"
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(build_note(t, md))
        print('built notes/' + t['slug'])
    print('built index.html + favicon.svg')


if __name__ == '__main__':
    main()

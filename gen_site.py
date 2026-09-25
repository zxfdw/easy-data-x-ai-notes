# -*- coding: utf-8 -*-
"""Easy Data × AI 学习档案 —— 静态站生成器（Read 模式 / 工程记录簿世界）

用法：python3 gen_site.py
产出：index.html、notes/task-N/index.html、favicon.svg
"""
import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

TASKS = [
    dict(no="01", code="TASK 1", slug="task-1", name="环境准备与课前导读",
         plan=("2 天", "09-17 03:00"), record="2026.09.15", status="已完成",
         diff=2,
         read=["F0 课前闲聊", "F1 大模型的本质与边界", "F2 AI Agent 的完整图景"],
         lesson=("第 1 课", "lessons/0001-three-symptoms-one-root-cause.html", "三个毛病，一个根因"),
         deck="完成环境自检与离线评测，读完公共基础三篇，建立「从数据看 Agent」的认知框架。",
         req="完成 Shell、Python、模型 API、Git 环境自检并提交结果；完成课前导读与公共基础阅读。"),
    dict(no="02", code="TASK 2", slug="task-2", name="场景识别与 RAG 产品设计",
         plan=("3 天", "09-20 03:00"), record="2026.09.17", status="已完成",
         diff=4,
         read=["P1 找准 Agent 的用武之地", "D1 让 Agent 会查资料", "I1 AI 原生数据系统"],
         lesson=("第 2 课", "lessons/0002-agent-loop-anatomy.html", "Agent 循环：模型每一圈看到了什么"),
         deck="配好测试 API Key、装好 pyseekdb，并把 code/D1 的六个示例全部跑通，走完从一次调用到 Agent 循环的演进。",
         req="获取测试用 API Key；安装向量数据库 pyseekdb 的 SDK；跑通 code/D1 的 d1_1 至 d1_6 示例代码。"),
    dict(no="03", code="TASK 3", slug="task-3", name="RAG 产品设计与向量数据库",
         plan=("3 天", "09-23 03:00"), record="2026.09.22", status="已完成",
         diff=3,
         read=["P2 让 Agent 会查资料", "I2 RAG 与向量数据库"],
         lesson=("第 3 课", "lessons/0003-hybrid-search-four-paths.html", "混合搜索：一个问题，四条检索路"),
         deck="理解 RAG 的基础流程，以及向量数据库中混合搜索的含义与实现。",
         req="了解 RAG 的基础流程与向量数据库混合搜索含义；跑通 code/D2 的 d2_1 至 d2_2。"),
    dict(no="04", code="TASK 4", slug="task-4", name="AI Native 数据层与 AI Functions",
         plan=("3 天", "09-26 03:00"), record="2026.09.25", status="已完成",
         diff=4,
         read=["D2 统一 AI Native 数据层实战", "I3 SQL × AI 与 AI Functions"],
         deck="体验数据在 AI 应用里如何被承载，并尝试在数据库系统内部调用 AI。",
         req="跑通 code/D2 的 d2_1 至 d2_5；通过 pyseekdb 执行 AI Function。"),
    dict(no="05", code="TASK 5", slug="task-5", name="记忆系统与 File SQL",
         plan=("3 天", "09-29 03:00"), record=None, status="待开始",
         diff=None,
         read=["P3 让 Agent 真正记住你", "I4 File SQL for AI Agent"],
         deck="理解记忆系统存储关键 value 的原理，并体验 PowerContext 的记忆能力。",
         req="理解记忆系统原理并安装 PowerContext；完成一条 select from read_csv 流程。"),
    dict(no="06", code="TASK 6", slug="task-6", name="Agentic RAG 与 AI 列",
         plan=("3 天", "10-02 03:00"), record=None, status="待开始",
         diff=None,
         read=["D3 实践出真知：Agentic RAG 实战", "I5 AI 列与派生数据维护"],
         deck="走通 Agentic RAG 的完整链路，并在向量数据库中创建与使用 AI 列。",
         req="跑通 code/D3 的 d3_1 至 d3_6；在 pyseekdb 创建并使用 AI 列。"),
    dict(no="07", code="TASK 7", slug="task-7", name="Skill 与上下文工程",
         plan=("3 天", "10-05 03:00"), record=None, status="待开始",
         diff=None,
         read=["P4 Skill 与 Agent 知识管理", "I6 上下文工程概述"],
         deck="理解 Agent 上下文工程的核心概念与工作流程，实践外部上下文管理工具。",
         req="理解上下文工程核心概念；基于 MCP、Skills 与 Agent Plugins 实践，以 PowerContext 为例完成安装与调用。"),
    dict(no="08", code="TASK 8", slug="task-8", name="Agent 记忆系统开发",
         plan=("3 天", "10-08 03:00"), record=None, status="待开始",
         diff=None,
         read=["D4 记哪些、忘哪些", "I7 PowerContext 的设计与实现"],
         deck="走通一个拥有完整记忆系统的 Agent 构建流程，理解其工业实现思路。",
         req="跑通 code/D4 的 d4_1 至 d4_4；学习 PowerContext 项目的设计。"),
    dict(no="09", code="TASK 9", slug="task-9", name="场景、总结与测评",
         plan=("3 天", "10-11 03:00"), record=None, status="待开始",
         diff=None,
         read=["P5 Agent 场景识别", "D5 课程总结", "I8 案例场景和测评构建"],
         deck="通过典型案例掌握测评基本方法，并实践上下文工程的实施效果评估。",
         req="了解上下文工程的场景应用与测评方法；用 PowerContext E2E 基于 Harbor 构建与迁移测评集。"),
]


# ---------------- Markdown → HTML（够用即止） ----------------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" loading="lazy">', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def md2html(md):
    out, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('```'):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre><code>' + html.escape('\n'.join(buf)) + '</code></pre>')
            continue
        if s.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            head = [c.strip() for c in s.strip('|').split('|')]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
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
                buf.append(lines[i].strip().lstrip('>').strip()); i += 1
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
                buf.append('<li>' + inline(re.sub(r'^\d+\. ', '', lines[i].strip())) + '</li>'); i += 1
            out.append('<ol>' + ''.join(buf) + '</ol>')
            continue
        if s in ('---', '***'):
            out.append('<hr>'); i += 1; continue
        if not s:
            i += 1; continue
        buf = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|>|[-*] |\d+\. |\||```)', lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)


# ---------------- 模板 ----------------
def page_head(prefix, title, desc):
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{html.escape(desc, quote=True)}" />
    <meta name="theme-color" content="#f6f8fb" />
    <title>{html.escape(title)}</title>
    <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml" />
    <link rel="stylesheet" href="{prefix}styles.css" />
    <script src="{prefix}script.js" defer></script>
  </head>
"""


def header(prefix):
    return f"""  <body>
    <a class="skip-link" href="#content">跳到正文</a>
    <header class="site-header">
      <div class="bar">
        <a class="wordmark" href="{prefix}index.html" aria-label="返回首页">
          <span class="wordmark-mark" aria-hidden="true">Z</span>
          <span>张博 · Easy Data × AI</span>
        </a>
        <nav aria-label="主要导航">
          <a href="{prefix}index.html#ledger">学习进度</a>
          <a href="https://github.com/datawhalechina/easy-data-x-ai" target="_blank" rel="noreferrer">课程仓库 ↗</a>
        </nav>
      </div>
    </header>
"""


FOOTER = """    <footer class="site-foot">
      <p>Easy Data × AI 学习档案 · 张博</p>
      <p>课程内容来自 Datawhale × OceanBase 开源项目</p>
    </footer>
  </body>
</html>
"""


def pips(n):
    if not n:
        return '<span class="cell-sub is-empty">未评价</span>'
    dots = ''.join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(5))
    return f'<span class="difficulty"><span class="pips">{dots}</span>{n}/5</span>'


def build_index():
    rows = []
    for t in TASKS:
        locked = t['status'] == '待开始'
        cls = ' class="is-locked"' if locked else ''
        lesson = t.get('lesson')
        if locked:
            lesson_html = ''
            note = '<span class="entry is-locked"><span>任务笔记</span><b aria-hidden="true">未开始</b></span>'
            reads = ''.join(f'<span class="entry"><span>{html.escape(r)}</span><b aria-hidden="true"></b></span>' for r in t['read'])
        else:
            if lesson:
                lesson_html = (f'<a class="entry" href="./{lesson[1]}"><span>{lesson[0]} · {html.escape(lesson[2])}</span>'
                               f'<b aria-hidden="true">↗</b></a>')
            else:
                lesson_html = ''
            note = f'<a class="entry" href="./notes/{t["slug"]}/"><span>任务笔记</span><b aria-hidden="true">↗</b></a>'
            reads = ''.join(f'<span class="entry"><span>{html.escape(r)}</span><b aria-hidden="true"></b></span>' for r in t['read'])
        lesson_txt = f"{lesson[0]} {lesson[2]}" if t.get('lesson') else ''
        search = html.escape(f"{t['name']} {t['req']} {' '.join(t['read'])} {t['status']} {lesson_txt}", quote=True)
        if t['record']:
            rec = f'<span class="cell-date">{t["record"]}</span><span class="cell-sub">{t["status"]}</span>'
        else:
            rec = f'<span class="cell-date is-empty">未记录</span><span class="cell-sub">{t["status"]}</span>'
        rows.append(f"""              <tr{cls} data-search="{search}">
                <td data-label="Task">
                  <span class="task-code">{t['code']}</span>
                  <span class="task-name">{html.escape(t['name'])}</span>
                </td>
                <td data-label="计划">
                  <span class="plan"><b>{t['plan'][0]}</b><span>截止 {t['plan'][1]}</span></span>
                </td>
                <td data-label="学习记录">{rec}</td>
                <td data-label="难度">{pips(t['diff'])}</td>
                <td data-label="笔记">
                  {note}
                  {lesson_html}
                  <span class="entry-group">{reads}</span>
                </td>
              </tr>""")

    done = sum(1 for t in TASKS if t['status'] == '已完成')
    active = sum(1 for t in TASKS if t['status'] == '进行中')
    pct = round(done / len(TASKS) * 100)
    return page_head('', 'Easy Data × AI 学习档案 · 张博', '按 Task 记录实践成果、学习笔记与对应讲义。') + header('') + f"""
    <main id="content">
      <section class="intro">
        <div>
          <h1>Easy Data × AI 学习档案</h1>
          <p class="intro-lede">每个 Task 一行：计划、进度、难度，以及对应的任务笔记与课程讲义。九个 Task，从环境准备走到 Agent 记忆系统。</p>
          <p class="intro-src">课程内容来自 Datawhale 与 OceanBase 社区共建的 <a href="https://github.com/datawhalechina/easy-data-x-ai" target="_blank" rel="noreferrer">easy-data-x-ai</a> 开源项目，本站整理个人任务笔记与阅读记录。</p>
        </div>
        <div class="intro-facts">
          <dl style="margin:0">
            <div class="fact-row"><dt>已完成</dt><dd>{done} / {len(TASKS)}</dd></div>
            <div class="fact-row"><dt>进行中</dt><dd>{active}</dd></div>
            <div class="fact-row"><dt>学习周期</dt><dd>09.14 至 10.11</dd></div>
          </dl>
          <div class="meter" role="img" aria-label="已完成 {done} 个 Task，共 {len(TASKS)} 个"><span style="width:{pct}%"></span></div>
        </div>
      </section>

      <section class="ledger" id="ledger" aria-labelledby="ledger-title">
        <div class="ledger-head">
          <h2 id="ledger-title">任务台账</h2>
          <div class="ledger-tools">
            <label class="search-field">
              <span class="sr-only">搜索任务</span>
              <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="m16 16 4 4"></path></svg>
              <input id="log-search" type="search" placeholder="搜索 Task、篇目或任务要求" autocomplete="off" />
            </label>
            <span class="record-count" aria-live="polite"><b id="visible-count">{len(TASKS)}</b> 个 Task</span>
          </div>
        </div>

        <div class="ledger-table">
          <table>
            <caption class="sr-only">Task 1 至 Task 9 的学习进度</caption>
            <thead>
              <tr>
                <th scope="col">Task</th>
                <th scope="col">计划</th>
                <th scope="col">学习记录</th>
                <th scope="col">难度</th>
                <th scope="col">笔记与阅读</th>
              </tr>
            </thead>
            <tbody id="log-body">
{chr(10).join(rows)}
            </tbody>
          </table>
          <p class="cell-sub difficulty-legend">难度以<strong>学习者实感</strong>校准（非课程官方评分）：按 ①概念密度 ②前置知识 ③动手门槛 ④与已有经验的距离，取四项中最高者，1 至 5 分。分值越高表示该 Task 里存在越难啃的部分。</p>
          <p class="cell-sub" id="empty-state" hidden style="padding:32px 0">没有匹配的 Task。</p>
        </div>
      </section>

          </main>

""" + FOOTER


def rail(current):
    items = []
    for t in TASKS:
        locked = t['status'] == '待开始'
        cur = t['slug'] == current
        kids = []
        if locked:
            kids.append('<span class="tree-link is-locked"><span>任务笔记</span><span>未开始</span></span>')
        else:
            kcls = 'tree-link is-current' if cur else 'tree-link'
            kids.append(f'<a class="{kcls}" href="../{t["slug"]}/"><span>任务笔记</span><span aria-hidden="true">↗</span></a>')
        for r in t['read']:
            kids.append(f'<span class="tree-read">{html.escape(r)}</span>')
        items.append(f"""        <details class="task-tree" {'open' if cur else ''}>
          <summary class="{'is-active' if cur else ''}">
            <span class="code">{t['code']}</span>
            <span class="title">{html.escape(t['name'])}</span>
            <span class="chev" aria-hidden="true"></span>
          </summary>
          <div class="tree-kids">
{chr(10).join('            ' + k for k in kids)}
          </div>
        </details>""")
    return f"""      <aside class="chapter-rail">
        <a class="back-link" href="../../index.html#ledger">← 返回进度</a>
        <p class="rail-title">全部任务</p>
        <nav aria-label="全部学习任务与阅读篇目">
{chr(10).join(items)}
        </nav>
      </aside>"""


def build_note(t, md):
    body = md2html(md)
    idx = TASKS.index(t)
    prev_t = TASKS[idx - 1] if idx > 0 else None
    next_t = TASKS[idx + 1] if idx < len(TASKS) - 1 else None
    prev_link = (f'<a href="../{prev_t["slug"]}/">← {prev_t["code"]}</a>'
                 if prev_t and prev_t['status'] != '待开始' else '<span class="disabled">← 上一课</span>')
    next_link = (f'<a href="../{next_t["slug"]}/">{next_t["code"]} →</a>'
                 if next_t and next_t['status'] != '待开始' else '<span class="disabled">下一课 →</span>')
    chips = ''.join(f'<li>{html.escape(x)}</li>' for x in t['read'])
    return page_head('../../', t['name'] + ' · Easy Data × AI 学习档案', t['deck']) + header('../../') + f"""
    <main class="note-shell" id="content">
{rail(t['slug'])}

      <article>
        <header class="note-head">
          <h1>{html.escape(t['name'])}</h1>
          <p class="note-lede">{html.escape(t['deck'])}</p>
          <ul class="note-meta">
            <li><span class="k">计划</span><span class="v">{t['plan'][0]}</span></li>
            <li><span class="k">截止</span><span class="v">{t['plan'][1]}</span></li>
            <li><span class="k">状态</span><span class="v">{t['status']}</span></li>
            <li><span class="k">更新</span><span class="v">{t['record'] or '—'}</span></li>
          </ul>
        </header>

        <section class="note-section">
          <h2>任务要求</h2>
          <p style="max-width:62ch;margin:0;color:var(--muted)">{html.escape(t['req'])}</p>
          <ul class="scope-chips">{chips}</ul>
        </section>

        <section class="note-section">
          <h2>实践成果与笔记</h2>
          <div class="prose">
{body}
          </div>
        </section>

        <footer class="note-foot">
          {prev_link}
          <a href="../../index.html#ledger">全部 Task ↑</a>
          {next_link}
        </footer>
      </article>
    </main>

""" + FOOTER


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#17498a"/>
  <text x="32" y="44" font-family="Georgia,serif" font-size="34" font-weight="700" fill="#ffffff" text-anchor="middle">Z</text>
</svg>
"""


def main():
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(build_index())
    open(os.path.join(ROOT, 'favicon.svg'), 'w', encoding='utf-8').write(FAVICON)
    srcs = {'task-1': 'task1-环境准备与课前导读.md', 'task-2': 'task2-场景识别与RAG产品设计.md',
            'task-3': 'task3-任务笔记.md', 'task-4': 'task4-任务笔记.md'}
    for t in TASKS:
        d = os.path.join(ROOT, 'notes', t['slug'])
        os.makedirs(d, exist_ok=True)
        md = ''
        src = os.path.join(ROOT, srcs.get(t['slug'], ''))
        if t['slug'] in srcs and os.path.exists(src):
            md = open(src, encoding='utf-8').read()
            md = re.sub(r'^#\s+.*\n', '', md, count=1)
            md = re.sub(r'^>\s*⏰.*\n', '', md, count=1)
            md = re.sub(r'^>\s*📖.*\n', '', md, count=1)
            md = md.replace('screenshots/', '../../screenshots/')
        if not md.strip():
            md = '## 待开始\n\n本 Task 尚未开始。完成后会在这里留下实践成果与学习笔记。\n'
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(build_note(t, md))
        print('built notes/' + t['slug'])
    print('built index.html + favicon.svg')


if __name__ == '__main__':
    main()

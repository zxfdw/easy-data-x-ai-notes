# Task 7：Skill 与上下文工程

> ⏰ 截止时间：2026-10-05 03:00
> 📖 道篇 P4《Skill 与 Agent 知识管理》+ 产业应用篇 I6《上下文工程概述》

## 01 实践成果

### 材料情况

- **P4**（道篇）：完整课程稿，讲 Skill 是什么、碎片化困境、检索问题、与 MCP 的关系，并附「同一个 Skill 如何在不同 Coding Agent 中落地」的互操作章节。
- **I6**（产业篇）：课程页标注**「正在开发中」**，只有方向与共建边界说明（Source / Memory / PreparedContext / Handoff 的职责边界等），**无配套脚本**。故动手项以 X2、X5 两个扩展示例 + PowerContext 安装调用为主。

### 示例代码跑通

| 目录 | 做什么 | 结果 |
|:--|:--|:--|
| `code/X2` | Skill 结构化管理：SKILL.md 解析 → seekdb 存储 → 混合检索按需加载 | ✅ 入库 1 Skill / 9 规则 / 2 示例 |
| `code/X2/x2_1_compare_context.py` | 全量注入 vs 按需加载的上下文开销对比 | ✅ **省 ~76%** 上下文（573 → 135 token） |
| `code/X5/mcp_skill_server.py` | 从零实现最小 MCP Server，把 code-review Skill 包成 `review_code_diff` 工具 | ✅ stdio 端到端调通 |
| `code/X5` 单测 | 防止「CI 全绿但干净环境导入不了」 | ✅ 1 passed |
| PowerContext | Task 7 要求「以 PowerContext 为例完成安装和调用」 | ✅ 装起 + 写入/列出/检索跑通 |

### 真实输出摘录

**X2 · Skill 上下文开销对比（seekdb 混合检索）**

```
用户请求: 帮我写一份 REST API 接口文档

【方式一】全量注入
  加载 Skill 数: 1
  上下文字符数: 1,721
  估算 Token 数: ~573

【方式二】按需加载 (seekdb hybrid search)
  上下文字符数: 405
  估算 Token 数: ~135

  节省上下文: ~76%

按需加载上下文预览（前 500 字符）:
----------------------------------------
## Skill: api-doc-writing
Write clear and consistent API documentation following team standards.
### Key Rules
- Version prefix required: /v1/users, not /users
- Every parameter must have: name, type, required, description
- Use nouns for resources, not verbs
- Include at least one success and one error example
- Mark optional parameters explicitly
```

**X5 · MCP Server 端到端（stdio：list_tools + call_tool）**

```
== initialize OK ==
== tools ==
  - review_code_diff: Review a code diff according to the code-review Skill checklist.
== call_tool review_code_diff ==
# Code Review Result
## Focus
correctness
## Input Summary
Received diff with 15 characters.
## Review Checklist
1. Correctness
2. Maintainability
3. Security
4. Tests
5. Compatibility
6. Project conventions
```

**PowerContext · 记忆写入 → 列出 → 检索**

```
SERVER_READY after 13s
默认 scope: scp_64daekbsf2m8mxgyj4s3nr7raf
【1】写入记忆（语义 / 情景 / 程序）→ 6 条
【2】列出记忆条目 → 共 6 条
【3】检索（mode=hybrid）
  查询「回答风格偏好」→ 命中 2 条
      · score=0.033  张博偏好简洁的回答，不喜欢过度铺垫和客套
      · score=0.032  回答代码类问题时，先给解释再给示例
  查询「微球注册怎么解决的」→ 命中 3 条
      · score=0.033  上次微球注册变更的难题，用「等粒径」统一型号口径解决了
```

### 环境坑（课程正文未载）

PowerContext 在主环境里**起不来**。排查下来是包版本硬冲突：

- `langchain-openai`（Task 6 的 RAGAS 拉进来的）要求 `openai<3.0.0`
- 而 PowerContext 依赖的 `pydantic-ai-slim 2.47` 要求 `openai>=3.8.0`

两者在同一环境无解，报错停在 `TypeError: Invalid http_client argument; Expected an instance of httpx.AsyncClient but got <class 'httpx2.AsyncClient'>`。

**处理：** 把 PowerContext 单独装进隔离环境（`pydantic-ai-slim 2.31.1` + `openai 2.54`，这个组合还在用普通 `httpx`，不触发冲突），不动已经跑通的 RAGAS 配置。

另外 X5 的 `mcp_skill_server.py` 用的是 `mcp 1.x` 的 `FastMCP` 导入路径，而当前主环境装的是 `mcp 2.x`（已把 FastMCP 改名 MCPServer）。课程 `requirements.txt` 其实写了 `mcp[cli]>=1.28.1,<2`，是本地环境没按它锁定；同样用独立环境装 `mcp 1.x` 解决。

---

## 02 这次的体会

**1. Skill 不是"更长的提示词"，而是把程序记忆拿出来当数据管。**

P4 里最让我改观的一句话是：Skill 是被**外部化、结构化了的程序记忆**。程序记忆是 Agent 脑子里"该怎么做"的规则，Skill 是把它写成书架上的操作手册。一旦写成文档，它就从"某个人或某个 Agent 专属"变成了**可以被管理的数据**；而只要是数据，前面几课讲的那套（存储、索引、检索、更新）就全回来了。

X2 的对比最能说明这一点：同样的内容，全量塞进上下文要 573 token，用混合检索按需取只要 135 token，省了 76%。**"要不要全量加载"从来不是提示词技巧问题，是检索问题。**

**2. Skill 碎片化，和知识库分散是同一类问题。**

P4 把碎片化分成三层：项目隔离、工具隔离、人员隔离。Cursor 的 Rules、Claude Code 的 CLAUDE.md、ChatGPT 的自定义指令，格式互不兼容，同一套经验要在三个地方写三遍。这跟 P2 说的"知识库分散、内容残缺、格式混乱是 RAG 效果不好的首因"是同一个根因：**经验数据没有被结构化地管理**。

换个视角，解法就清楚了：把 Skill 当成和知识库一样的数据资产来管理。这不是写同步脚本能解决的工程问题，是数据管理问题。

**3. 从 Skill 到 MCP：从"该怎么做"到"怎么被调用"。**

Skill 解决的是"这件事该怎么做"，但不解决"怎么被不同客户端统一发现和调用"。X5 那个 50 行的 MCP Server 就是这一层：把 code-review 的经验包成一个有稳定名字、有清晰描述、有结构化参数的 `review_code_diff` 工具。P4 的判断是：Skill 还在快速迭代时写成文档最灵活，等它稳定了、要跨工具复用了，就考虑 MCP 化。这跟 Task 2 讲的"MCP Tool 要有稳定命名、清晰描述、结构化参数"完全是一条线。

**4. 上下文工程的边界，是 I6 想划的那条线。**

I6 虽然还在开发中，但它列的方向很清楚：Source、Memory、PreparedContext、Handoff 的职责边界，加上项目范围、相关性、上下文预算，**上下文工程不等于"把更多内容塞进提示词"**。这跟 X2 的对比实验正好互证：上下文是有限资源，关键不是塞得多，是取得准。

**5. 最大的收获其实是"跑不通时先分清是环境问题还是代码问题"。**

这次 Task 7 两个坑（PowerContext 的 openai 版本冲突、X5 的 mcp 大版本差异）都不是我代码写错了，而是**依赖版本没对齐**。课程 `requirements.txt` 里其实写明了 `mcp>=1.28.1,<2`，是本地环境跑偏了。这跟 Task 6 的体会接得上：跑开源项目时，"跑不通"经常先要判断环境，而不是直接改代码。

---

*创建：2026-09-30*

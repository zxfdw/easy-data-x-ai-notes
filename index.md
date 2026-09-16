---
layout: default
title: EasyData 学习手记
---
# EASY DATA × AI · 学习手记

> 从数据视角理解并构建 AI Agent ｜ 🔖 张博 ｜ 🗓️ 2026-09-14 ~ 10-11（29 天）
> 📚 [官方课程](https://github.com/datawhalechina/easy-data-x-ai) ｜ [在线阅读](https://datawhalechina.github.io/easy-data-x-ai)

**课程简介：** 围绕 **Agent、RAG、Memory、Skill 与 MCP**，理解数据如何影响 AI 应用的效果、边界与工程实现。双轨结构——**道篇**（场景判断/问题归因/系统设计）+ **术篇**（可运行代码：流式输出、工具调用、AI Native 数据层、Agentic RAG、记忆系统）+ **产业应用篇**（真实 AI Native 数据产品）。

---

## 📋 任务安排

| Task | 主题 | 具体任务 | 天数 | 截止时间 | 状态 |
|:--|:--|:--|:--|:--|:--|
| **Task 1** | 环境准备与课前导读<br><small>F0·F1·F2 公共基础</small> | 完成 Shell / Python / 模型 API / Git 环境自检并提交结果；课前导读 | 2 天 | 09-17 03:00 | ✅ [笔记](task1-环境准备与课前导读.md) |
| **Task 2** | P1 找准 Agent 的用武之地——场景识别<br>D1 让 Agent 会查资料——RAG 产品设计<br>I1 AI 原生数据系统 | 获取测试用 API Key；安装向量数据库 **pyseekdb** SDK；跑通 `code/D1` 的 **d1_1~d1_6**，体验从大模型基础调用到"推理→行动→观察"Agent 多轮循环 | 3 天 | 09-20 03:00 | ⏳ |
| **Task 3** | P2 RAG 产品设计<br>I2 RAG 与向量数据库 | 了解 RAG 基础流程与向量数据库**混合搜索**含义；跑通 `code/D2` 的 **d2_1~d2_2**，体验向量搜索 | 3 天 | 09-23 03:00 | ⏳ |
| **Task 4** | D2 统一 AI Native 数据层实战<br>I3 SQL × AI——AI Functions 设计与执行 | 跑通 `code/D2` 的 **d2_1~d2_5**，体验 Data 的向量化/存储/查询与混合搜索；通过 pyseekdb 执行 **AI Function** | 3 天 | 09-26 03:00 | ⏳ |
| **Task 5** | P3 让 Agent 真正记住你——记忆系统设计<br>I4 File SQL for AI Agent | 理解记忆系统存储关键 value 的原理，安装 **PowerContext** 体验记忆能力；完成 `select from read_csv(xxx.csv)` 流程 | 3 天 | 09-29 03:00 | ⏳ |
| **Task 6** | D3 实践出真知——Agentic RAG 实战<br>I5 AI 列——模型驱动派生数据自动维护 | 跑通 `code/D3` 的 **d3_1~d3_6**，走通 Agentic RAG 完整链路；在 pyseekdb 创建并使用 **AI 列** | 3 天 | 10-02 03:00 | ⏳ |
| **Task 7** | P4 Skill 与 Agent 知识管理<br>I6 上下文工程概述 | 理解 Agent 上下文工程核心概念与工作流程；基于 **MCP / Skills / Agent Plugins** 实践外部上下文管理工具，以 **PowerContext** 为例完成安装与调用 | 3 天 | 10-05 03:00 | ⏳ |
| **Task 8** | D4 记哪些、忘哪些？——Agent 记忆系统开发<br>I7 PowerContext 的设计与实现 | 跑通 `code/D4` 的 **d4_1~d4_4**，走通完整记忆系统的 Agent 构建流程；学习 PowerContext 设计，了解工业实现思路 | 3 天 | 10-08 03:00 | ⏳ |
| **Task 9** | P5 Agent 场景识别<br>D5 课程总结<br>I8 案例场景和测评构建 | 通过典型案例了解上下文工程应用与研究方法，掌握测评方法；用 **PowerContext E2E 基于 Harbor** 构建与迁移测评集 | 3 天 | 10-11 03:00 | ⏳ |

> P = 产品/道篇 ｜ D = 开发者/术篇 ｜ I = 产业应用篇 ｜ F = 公共基础

---

*学习周期：2026-09-14 ~ 2026-10-11*

---
layout: default
title: EasyData 学习手记
---
# EASY DATA × AI · 学习手记

> 从环境准备到 Agent 实践，按 Task 留下运行结果、学习笔记与阶段性理解。
> 🔖 学习者：张博 ｜ 🗓️ 2026-09-14 至 2026-10-11 ｜ ⏱️ 共 29 天

**课程主页：** [datawhalechina/easy-data-x-ai](https://github.com/datawhalechina/easy-data-x-ai) ｜ [在线阅读](https://datawhalechina.github.io/easy-data-x-ai)

---

## 📌 课程简介

**Easy Data × AI：构建知识与记忆驱动的 Agent** —— 一门从**数据视角**理解和构建 AI 应用的开源入门课程。围绕 **Agent、RAG、Memory、Skill 与 MCP** 等主题，理解数据如何影响 AI 应用的效果、边界和工程实现。

**双轨结构：**
- **道篇** —— 面向零基础 AI 爱好者和产品决策者，训练场景判断、问题归因与系统设计能力
- **术篇** —— 面向已会调用 LLM API 的开发者，通过可运行代码学习流式输出、工具调用、AI Native 数据层、Agentic RAG 和 Agent 记忆系统
- **产业应用篇** —— 体验真实的 AI Native 数据产品

学完后能：①判断需求是否适合做 Agent ②分析"AI 答不好"卡在数据/模型/业务 ③动手搭建从检索到记忆与工具调用的基本链路。

---

## 📋 任务总览

| Task | 主题 | 天数 | 截止时间 | 状态 |
|:--|:--|:--|:--|:--|
| **Task 1** | 环境准备与课前导读 | 2 天 | 09-17 03:00 | ✅ 已完成 |
| **Task 2** | P1 场景识别 + D1 RAG 产品设计 + I1 AI 原生数据系统 | 3 天 | 09-20 03:00 | ⏳ |
| **Task 3** | P2 RAG 产品设计 + I2 RAG 与向量数据库 | 3 天 | 09-23 03:00 | ⏳ |
| **Task 4** | D2 统一 AI Native 数据层实战 + I3 SQL × AI | 3 天 | 09-26 03:00 | ⏳ |
| **Task 5** | P3 记忆系统设计 + I4 File SQL for AI Agent | 3 天 | 09-29 03:00 | ⏳ |
| **Task 6** | D3 Agentic RAG 实战 + I5 AI 列 | 3 天 | 10-02 03:00 | ⏳ |
| **Task 7** | P4 Skill 与 Agent 知识管理 + I6 上下文工程概述 | 3 天 | 10-05 03:00 | ⏳ |
| **Task 8** | D4 Agent 记忆系统开发 + I7 PowerContext 设计与实现 | 3 天 | 10-08 03:00 | ⏳ |
| **Task 9** | P5 Agent 场景识别 + D5 课程总结 + I8 案例场景和测评构建 | 3 天 | 10-11 03:00 | ⏳ |

---

## 📖 各 Task 具体任务

### ✅ Task 1：环境准备与课前导读
**截止 09-17 03:00 ｜ 2 天**

> 完成 Shell、Python、模型 API、Git 环境自检，并提交结果；课前导读与公共基础（F1/F2）。

- [x] 环境自检：Shell / Python / 模型 API / Git
- [x] 离线评测 60 条全过（Hit@3 = 1.0，拒答准确率 = 1.0）
- [x] 课前导读 F1《大模型的本质与边界》+ F2《AI Agent 完整图景》

📄 [查看完整笔记](task1-环境准备与课前导读.md)

---

### ⏳ Task 2：AI Agent 场景识别 + RAG 产品设计 + AI 原生数据系统
**截止 09-20 03:00 ｜ 3 天**

> **产品篇 P1：** 找准 Agent 的用武之地 —— AI Agent 场景识别
> **开发者篇 D1：** 让 Agent 会查资料 —— RAG 产品设计
> **产业应用篇 I1：** AI 原生数据系统

- [ ] 获取用于进行测试的 **API Key**
- [ ] 安装用于测试的向量数据库 **pyseekdb** 的 SDK
- [ ] 阅读并跑通 `code/D1` 目录下的 **d1_1 ~ d1_6** 示例代码，体验从大模型基础调用，一路到"推理 → 行动 → 观察"Agent 多轮循环的完整演进流程

---

### ⏳ Task 3：RAG 产品设计 + RAG 与向量数据库
**截止 09-23 03:00 ｜ 3 天**

> **产品篇 P2：** 让 Agent 会查资料 —— RAG 产品设计
> **产业应用篇 I2：** RAG 与向量数据库

- [ ] 了解 **RAG 的基础流程**，以及向量数据库中**混合搜索**的含义
- [ ] 预习并跑通 `code/D2` 目录下的 **d2_1 ~ d2_2** 示例代码，体验 AI 系统中的向量搜索

---

### ⏳ Task 4：统一 AI Native 数据层实战 + SQL × AI
**截止 09-26 03:00 ｜ 3 天**

> **开发者篇 D2：** 统一 AI Native 数据层实战
> **产业应用篇 I3：** SQL × AI —— AI Functions 的设计与执行

- [ ] 阅读并跑通 `code/D2` 目录下的 **d2_1 ~ d2_5** 示例代码，体验 Data 在 AI 应用里是如何被承载（向量化、存储、查询），体验 AI 系统中的混合搜索
- [ ] 通过 **pyseekdb** 向量数据库，执行 **AI Function**，了解在数据库系统中调用 AI 的方式

---

### ⏳ Task 5：记忆系统设计 + File SQL for AI Agent
**截止 09-29 03:00 ｜ 3 天**

> **产品篇 P3：** 让 Agent 真正记住你 —— 记忆系统设计
> **产业应用篇 I4：** File SQL for AI Agent

- [ ] 理解**记忆系统存储关键 value 的原理**，安装 **PowerContext** 并体验记忆系统的相关能力
- [ ] 完成一条简单的 `select from read_csv(xxx.csv)` 流程

---

### ⏳ Task 6：Agentic RAG 实战 + AI 列
**截止 10-02 03:00 ｜ 3 天**

> **开发者篇 D3：** 实践出真知 —— Agentic RAG 实战
> **产业应用篇 I5：** AI 列 —— 模型驱动派生数据的自动维护

- [ ] 阅读并跑通 `code/D3` 目录下的 **d3_1 ~ d3_6** 示例代码，走通 Agentic RAG 的完整链路
- [ ] 通过在 pyseekdb 向量数据库创建并使用 **AI 列**，了解 AI 在数据系统中的真实应用场景

---

### ⏳ Task 7：Skill 与 Agent 知识管理 + 上下文工程概述
**截止 10-05 03:00 ｜ 3 天**

> **产品篇 P4：** Skill 与 Agent 知识管理
> **产业应用篇 I6：** 上下文工程概述

- [ ] 通过学习课程，理解 **Agent 上下文工程的核心概念与工作流程**
- [ ] 基于 **MCP、Skills 和 Agent Plugins** 等标准化扩展机制，实践外部上下文管理工具的安装、接入与使用；以 **PowerContext** 为例，完成上下文管理工具安装和调用

---

### ⏳ Task 8：Agent 记忆系统开发 + PowerContext 设计与实现
**截止 10-08 03:00 ｜ 3 天**

> **开发者篇 D4：** 记哪些、忘哪些？—— Agent 记忆系统开发
> **产业应用篇 I7：** PowerContext 的设计与实现

- [ ] 阅读并跑通 `code/D4` 目录下的 **d4_1 ~ d4_4** 示例代码，走通一个拥有完整记忆系统的 Agent 构建流程
- [ ] 通过学习 **PowerContext** 项目的设计，了解记忆 & 上下文管理系统的工业实现思路

---

### ⏳ Task 9：Agent 场景识别 + 课程总结 + 案例场景和测评构建
**截止 10-11 03:00 ｜ 3 天**

> **产品篇 P5：** Agent 场景识别
> **开发者篇 D5：** 课程总结
> **产业应用篇 I8：** 案例场景和测评构建

- [ ] 通过典型案例了解 Agent 上下文工程在具体场景中的应用与研究，掌握测评的基本方法
- [ ] 使用 **PowerContext E2E 基于 Harbor** 构建和迁移测评集，实践评估上下文工程的实施效果

---

## 📚 引用

- 官方课程：https://github.com/datawhalechina/easy-data-x-ai
- 在线阅读：https://datawhalechina.github.io/easy-data-x-ai

*学习周期：2026-09-14 ~ 2026-10-11*

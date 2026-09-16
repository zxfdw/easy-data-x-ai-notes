# Easy Data × AI 学习打卡笔记

> 🎓 **课程：** [Datawhale《Easy Data × AI》](https://github.com/datawhalechina/easy-data-x-ai)——从数据驱动视角学习构建 AI Agent
> 🔖 **学习者：** 张博
> 🗓️ **组队学习周期：** 2026-09-14 至 2026-10-11（共 29 天）
> 🖥️ **网页版：** https://zxfdw.github.io/easy-data-x-ai-notes/

## 📌 课程简介

**Easy Data × AI：构建知识与记忆驱动的 Agent** —— 从数据视角理解和构建 AI 应用。围绕 Agent、RAG、Memory、Skill 与 MCP，理解数据如何影响 AI 应用的效果、边界与工程实现。

**双轨结构：** 道篇（场景判断/问题归因/系统设计）+ 术篇（可运行代码：流式输出、工具调用、AI Native 数据层、Agentic RAG、记忆系统）+ 产业应用篇（真实 AI Native 数据产品）

## 📋 任务总览

| Task | 主题 | 天数 | 截止时间 | 状态 | 笔记 |
|:--|:--|:--|:--|:--|:--|
| Task 1 | 环境准备与课前导读 | 2 天 | 09-17 03:00 | ✅ 已完成 | [笔记](task1-环境准备与课前导读.md) |
| Task 2 | P1 场景识别 + D1 RAG + I1 | 3 天 | 09-20 03:00 | ⏳ | 待创建 |
| Task 3 | P2 RAG + I2 向量数据库 | 3 天 | 09-23 03:00 | ⏳ | 待创建 |
| Task 4 | D2 数据层实战 + I3 SQL×AI | 3 天 | 09-26 03:00 | ⏳ | 待创建 |
| Task 5 | P3 记忆系统 + I4 File SQL | 3 天 | 09-29 03:00 | ⏳ | 待创建 |
| Task 6 | D3 Agentic RAG + I5 AI 列 | 3 天 | 10-02 03:00 | ⏳ | 待创建 |
| Task 7 | P4 Skill 知识管理 + I6 上下文工程 | 3 天 | 10-05 03:00 | ⏳ | 待创建 |
| Task 8 | D4 记忆系统开发 + I7 PowerContext | 3 天 | 10-08 03:00 | ⏳ | 待创建 |
| Task 9 | P5 场景识别 + D5 总结 + I8 测评 | 3 天 | 10-11 03:00 | ⏳ | 待创建 |

## 📖 各 Task 具体任务

### ✅ Task 1：环境准备与课前导读（截止 09-17 03:00）
- 完成 Shell、Python、模型 API、Git 环境自检，并提交结果
- 课前导读与公共基础（F1/F2）
- ✅ 离线评测 60 条全过（Hit@3=1.0、拒答准确率=1.0）

### ⏳ Task 2：AI Agent 场景识别 + RAG 产品设计 + AI 原生数据系统（截止 09-20 03:00）
- 获取用于测试的 API Key
- 安装向量数据库 **pyseekdb** 的 SDK
- 跑通 `code/D1` 的 **d1_1 ~ d1_6**，体验从大模型基础调用到"推理→行动→观察"Agent 多轮循环的演进

### ⏳ Task 3：RAG 产品设计 + RAG 与向量数据库（截止 09-23 03:00）
- 了解 RAG 基础流程，以及向量数据库中**混合搜索**的含义
- 跑通 `code/D2` 的 **d2_1 ~ d2_2**，体验向量搜索

### ⏳ Task 4：统一 AI Native 数据层实战 + SQL × AI（截止 09-26 03:00）
- 跑通 `code/D2` 的 **d2_1 ~ d2_5**，体验 Data 在 AI 应用里如何被承载（向量化、存储、查询）
- 通过 pyseekdb 执行 **AI Function**

### ⏳ Task 5：记忆系统设计 + File SQL for AI Agent（截止 09-29 03:00）
- 理解记忆系统存储关键 value 的原理，安装 **PowerContext** 并体验记忆能力
- 完成一条简单的 `select from read_csv(xxx.csv)` 流程

### ⏳ Task 6：Agentic RAG 实战 + AI 列（截止 10-02 03:00）
- 跑通 `code/D3` 的 **d3_1 ~ d3_6**，走通 Agentic RAG 完整链路
- 在 pyseekdb 创建并使用 **AI 列**

### ⏳ Task 7：Skill 与 Agent 知识管理 + 上下文工程概述（截止 10-05 03:00）
- 理解 Agent 上下文工程的核心概念与工作流程
- 基于 **MCP、Skills、Agent Plugins** 实践外部上下文管理工具；以 **PowerContext** 为例完成安装与调用

### ⏳ Task 8：Agent 记忆系统开发 + PowerContext 设计与实现（截止 10-08 03:00）
- 跑通 `code/D4` 的 **d4_1 ~ d4_4**，走通完整记忆系统的 Agent 构建流程
- 学习 PowerContext 项目设计，了解记忆 & 上下文管理系统的工业实现思路

### ⏳ Task 9：Agent 场景识别 + 课程总结 + 案例场景和测评构建（截止 10-11 03:00）
- 通过典型案例了解 Agent 上下文工程的应用与研究，掌握测评基本方法
- 使用 **PowerContext E2E 基于 Harbor** 构建和迁移测评集

## 🖥️ 网页版

- https://zxfdw.github.io/easy-data-x-ai-notes/

## 📚 引用

- 官方课程：https://github.com/datawhalechina/easy-data-x-ai
- 在线阅读：https://datawhalechina.github.io/easy-data-x-ai

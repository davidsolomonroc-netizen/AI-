---
title: "Lemmalog：LLM 代理的 Datalog 记忆引擎"
description: "为 LLM 代理提供可验证、可追溯的演绎数据库记忆层。"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/JordyZomer/lemmalog"
githubStars: 216
githubOwner: "JordyZomer"
githubRepo: "lemmalog"
category: "agent-framework"
tags: ["datalog", "agent-memory", "mcp", "neurosymbolic"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Lemmalog 为 LLM 代理提供了一种基于 Datalog 的持久化记忆系统，将事实、规则和推导过程结构化存储，支持溯源和增量更新。它适合需要长期、可靠记忆的 AI 应用开发者，尤其是那些希望减少幻觉、增强推理一致性的代理框架。通过 MCP 服务器，可以轻松集成到现有代理工作流中。"
vibeCodingPrompt: "1. 在你的 Claude Code 会话中，使用 MCP 配置指向 Lemmalog 的 MCP 服务器（例如 `npx lemmalog-mcp`）。
2. 定义你的领域事实表（如 `user(name, age)`、`purchase(user, item, price)`），并编写 Datalog 规则来推导派生事实（如 `loyal_user(U) :- purchase(U, _, _), age(U, A), A > 30`）。
3. 让代理在每次对话后通过 LLM 提取新事实并调用 `assert` 接口写入。
4. 在需要回答问题时，使用 `ask` 接口查询，并让代理基于 `why()` 解释结果。
5. 利用 `changes_from` 获取增量变化，用于上下文注入。"
pitfallGuide: "1. 该引擎是解释器实现，性能可能不如原生编译的 Datalog，适合中小规模事实集。\n2. 需要理解 Datalog 语法和分层规则，非技术人员学习曲线较陡。\n3. MCP 服务器配置需要一定的 Node 环境，部署步骤略多于一行命令。\n4. 当前状态是早期阶段，API 可能变化，需关注版本更新。\n5. 对于超大规模事实库，BM25 混合检索可能需要调优。"
targetAudience: ["AI 研究者", "独立开发者", "技术负责人"]
useCases: ["构建具有长期记忆的客服代理", "实现可解释的决策支持系统", "开发需要事实溯源的合规性工具", "为多代理协作提供共享知识库"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A Datalog engine for LLM agent memory: stratified rules, provenance-tracked facts, incremental derivation, and an MCP server that lets your harness use it as a shared brain.

> GitHub: [JordyZomer/lemmalog](https://github.com/JordyZomer/lemmalog) | ⭐ 216 | Rust

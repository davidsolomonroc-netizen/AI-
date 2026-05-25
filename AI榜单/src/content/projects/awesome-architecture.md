---
title: "架构图谱"
description: "系统化架构思维与模板库"
publishDate: 2026-05-25
featured: false
githubUrl: "https://github.com/study8677/awesome-architecture"
githubStars: 91
githubOwner: "study8677"
githubRepo: "awesome-architecture"
category: "other"
tags: ["software-architecture", "system-design", "architecture-patterns", "tutorial"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个面向软件架构师和高级开发者的开源知识库，提供21个真实系统架构模板（含AI网关、RAG、Agent等）和一套中英文双语教程。适合希望从“写代码”进阶到“做架构决策”的技术团队和个人。"
vibeCodingPrompt: "1. 首先阅读 tutorial/ 目录下的教程，特别是01-为什么先有架构思维.md和03-读懂与画好架构图.md，理解架构思维框架。
2. 根据你的系统需求（如构建一个AI Agent服务），打开templates/中对应的模板（如ai-agent-gateway.md），分析其架构图和数据流。
3. 按照模板中的架构决策（ADR）和组件划分，在Claude Code中逐步生成代码骨架：先定义接口和数据模型，再实现核心逻辑，最后补充测试。
4. 使用架构-copilot skill（见README）自动引导每一步的架构权衡（如选择同步/异步通信、数据一致性策略）。"
pitfallGuide: "1. 教程和模板是语言无关的，不要期待有现成代码可跑，需要自己根据架构图实现。
2. 模板中的架构决策记录（ADR）是示例，实际项目需根据自身约束调整。
3. 仓库主要面向“架构思维”培养，不适合零基础学编程的新手。
4. 在线阅读站点可能加载较慢，建议克隆仓库本地阅读。
5. 配套的architecture-copilot skill需要额外安装和配置，不是开箱即用。"
targetAudience: ["技术负责人", "独立开发者", "企业团队"]
useCases: ["系统设计面试准备", "从零设计一个可扩展的微服务系统", "学习AI Agent/RAG等前沿架构的通用模式"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。🗺️ Think like a software architect, not just a coder — 21 architecture maps (incl. AI gateway, RAG, agents, inference serving, vector DB) + a language-agnostic system-design tutorial. Every template links to real open-source prototypes. 中英文双语。

> GitHub: [study8677/awesome-architecture](https://github.com/study8677/awesome-architecture) | ⭐ 91 | Vue

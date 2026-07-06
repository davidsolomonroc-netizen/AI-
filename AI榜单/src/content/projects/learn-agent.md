---
title: "AI Agent 开发进阶笔记"
description: "手把手实现可商用 coding agent"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/7-e1even/learn-agent"
githubStars: 75
githubOwner: "7-e1even"
githubRepo: "learn-agent"
category: "agent-framework"
tags: ["agent", "tutorial", "nodejs", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一套从实际产品中提炼的 AI Agent 开发笔记，适合想要构建可靠 coding agent 的开发者。它解释了 Claude Code、Codex 等工具的内部机制，并提供了零依赖、可直接运行的示例代码，帮助读者解决循环空转、上下文超限等工程难题。"
vibeCodingPrompt: "请先克隆项目: git clone https://github.com/7-e1even/learn-agent && cd learn-agent
然后依次运行 s01 到 s12 的示例，每读一篇 README 就运行对应目录下的 agent.mjs 文件。
运行前请设置 AGENT_API_KEY 环境变量（支持 OpenAI 兼容 API）。
建议从 s01 开始按顺序阅读，边读边运行代码，理解每个机制如何解决实际问题。"
pitfallGuide: "1. 需要 Node 18+ 环境，且需配置 API key（OpenAI 兼容）。
2. 笔记是中文的，英文读者可切换 README_EN.md。
3. 示例代码是教学用的简化版，生产使用需参考 Reina 等完整项目。
4. s12 提供无 key 自测模式，但部分机制依赖真实 LLM 调用。
5. 请勿直接复制 s01-s11 的代码到生产环境，它们缺少错误处理和边界情况。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["学习 coding agent 内部实现原理", "构建自己的 AI 编程助手原型", "理解 Claude Code/Codex 等工具的工作机制", "为产品落地 agent 功能提供参考"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。学习Agent开发的笔记

> GitHub: [7-e1even/learn-agent](https://github.com/7-e1even/learn-agent) | ⭐ 75 | JavaScript

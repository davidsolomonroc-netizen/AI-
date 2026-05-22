---
title: "克劳德灵魂"
description: "Claude跨会话自纠正记忆引擎"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/DomDemetz/claude-soul"
githubStars: 76
githubOwner: "DomDemetz"
githubRepo: "claude-soul"
category: "agent-framework"
tags: ["memory", "claude-code", "mcp-server", "self-improving"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Claude Soul 解决了 AI 助手在每次新会话中遗忘历史的问题，通过本地 SQLite 存储和语义搜索实现跨会话记忆。适合使用 Claude Code 进行长期项目的开发者，能自动追踪纠正模式并逐步优化行为。"
vibeCodingPrompt: "1. 运行 npx claude-soul init --starter 初始化项目
2. 在 Claude Code 中启用 MCP 服务器：claude mcp add claude-soul -- npx claude-soul mcp
3. 每次会话开始前运行 claude-soul shadow --brief 查看历史模式
4. 需要查询记忆时，直接提问如 'what did we decide about the auth flow last week?'
5. 利用自动纠正跟踪功能，无需手动干预即可逐步优化 Claude 行为"
pitfallGuide: "1. 需要 Node.js >= 18 和 Claude Code Pro/Max 计划
2. 首次初始化后需手动添加 MCP 服务器配置
3. 语义搜索依赖可选 Ollama 嵌入，默认使用本地 SQLite 搜索效果有限
4. 跨会话记忆仅在启动时加载，长会话中需手动触发同步
5. 纠正跟踪数据积累需要一定会话次数（建议>10次）才能体现效果"
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Self-correcting learning engine for Claude Code — persistent identity, behavioral pattern tracking, and cross-session memory

> GitHub: [DomDemetz/claude-soul](https://github.com/DomDemetz/claude-soul) | ⭐ 76 | TypeScript

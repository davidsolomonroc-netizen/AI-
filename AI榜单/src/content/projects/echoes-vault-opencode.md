---
title: "回声保险库"
description: "OpenCode的持久化记忆插件"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/psinetron/echoes-vault-opencode"
githubStars: 78
githubOwner: "psinetron"
githubRepo: "echoes-vault-opencode"
category: "agent-framework"
tags: ["memory", "opencode", "knowledge-base", "markdown"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "EchoesVault为OpenCode AI代理提供跨会话的持久化记忆，基于Markdown文件存储，兼容Obsidian。适合需要AI代理记住项目上下文、历史决策和日常记录的开发者和团队，解决AI每次会话丢失记忆的痛点。"
vibeCodingPrompt: "1. 在OpenCode中安装EchoesVault插件（npm install echoes-vault-opencode）。\n2. 启动OpenCode，插件会自动创建EchoesVault/目录和所需文件。\n3. 使用/echoes-start命令开始会话，AI会自动加载最近的日志和知识索引。\n4. 在对话中，AI会自动记录关键信息到每日日志，并支持通过/echoes-search查询知识库。\n5. 可打开EchoesVault/目录在Obsidian中可视化浏览知识图谱。"
pitfallGuide: "1. 需要OpenCode环境，不能独立运行。\n2. 首次使用需确保网络能访问npm包。\n3. 知识库文件存储在本地仓库，注意不要误删或提交到公开仓库。\n4. 插件依赖OpenCode的slash命令系统，版本兼容性需关注。\n5. 对于大型项目，知识库可能快速增长，需定期清理或归档旧日志。"
targetAudience: ["独立开发者", "技术负责人", "AI研究者"]
useCases: ["AI辅助开发时保持项目上下文记忆", "记录架构决策和API设计文档", "跨会话跟踪每日工作进度", "构建可搜索的项目知识库"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Persistent memory plugin for OpenCode. Obsidian-style knowledge base that survives across sessions

> GitHub: [psinetron/echoes-vault-opencode](https://github.com/psinetron/echoes-vault-opencode) | ⭐ 78 | TypeScript

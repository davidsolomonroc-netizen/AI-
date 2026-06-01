---
title: "决斗代理：多模型路由层"
description: "多模型智能路由，选最便宜的最佳答案"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/2aronS/Duel-Agents"
githubStars: 632
githubOwner: "2aronS"
githubRepo: "Duel-Agents"
category: "agent-framework"
tags: ["multi-model", "routing", "cost-optimization", "cli-tool"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Duel Agents 是一个IDE原生路由层，自动将提示词发送给多个LLM模型，并选择成本最低且质量达标的答案。适合希望降低API成本、同时保持输出质量的开发者和AI团队，通过简单安装即可在Claude Code、Cursor等工具中使用。"
vibeCodingPrompt: "1. 在终端运行 `npx @duel-agents/install all` 安装所有插件。\n2. 设置环境变量 `export DUEL_API_KEY=duel_yourprefix_yoursecret`。\n3. 在Cursor中，手动设置 Settings → Models → Override OpenAI Base URL 为 `https://duelagents.com/v1`。\n4. 在Claude Code中，运行 `/duel-agents:setup` 进行引导配置。\n5. 编写一个简单的提示词如“解释量子计算”，观察Duel Agents如何自动路由并返回最经济的答案。"
pitfallGuide: "1. 必须使用Duel API key，不能直接用Anthropic或OpenAI的密钥\n2. 安装后需要手动在Cursor中设置Base URL，否则无法生效\n3. 目前仅支持Claude Code、Cursor、Codex CLI和OpenClaw四个工具\n4. 如果使用OpenClaw，Telegram/Discord渠道不受影响，仅模型后端切换"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI研究者"]
useCases: ["降低多模型调用成本，自动选择性价比最高的模型", "在IDE中无缝集成多模型对比，提升开发效率", "为团队提供统一的LLM路由层，简化API管理", "快速测试不同模型对同一提示词的响应差异"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。CLI, SDK, and IDE plugins for Duel Agents

> GitHub: [2aronS/Duel-Agents](https://github.com/2aronS/Duel-Agents) | ⭐ 632 | TypeScript

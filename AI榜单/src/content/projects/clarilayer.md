---
title: "ClariLayer：AI数据上下文层"
description: "为AI代理提供持久化数据语境"
publishDate: 2026-06-15
featured: false
githubUrl: "https://github.com/clarilayer/clarilayer"
githubStars: 124
githubOwner: "clarilayer"
githubRepo: "clarilayer"
category: "data-analysis"
tags: ["MCP", "context-engineering", "data-engineering", "AI-agents"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "ClariLayer是一个MCP服务器，为Claude Code、Cursor等AI编码代理提供持久化的数据上下文层。它自动从你已有的SQL和dbt项目中提取数据定义，与数据仓库进行核对，并记住你的修正，避免AI每次会话都重新理解数据，适合数据团队和个体分析师使用。"
vibeCodingPrompt: "在Claude Code中，使用MCP配置连接ClariLayer服务器（例如在claude_desktop_config.json中添加MCP服务器地址）。然后，在分析数据时，ClariLayer会自动从你的SQL仓库加载已有的指标定义（如净收入计算逻辑），并与数据仓库结果进行比对，发现不一致时自动标记为caveat。你只需要像平常一样提问，ClariLayer在后台维护上下文。"
pitfallGuide: "1. 需要先配置MCP连接，非零配置\n2. 依赖你已有的SQL/dbt项目质量，定义越清晰效果越好\n3. 免费版对个体分析师友好，团队协作需付费\n4. 与数据仓库的实时连接可能增加查询开销\n5. 目前主要支持Claude Code、Cursor和Codex，其他AI工具需适配"
targetAudience: ["数据分析师", "独立开发者", "创业者", "数据工程师"]
useCases: ["AI辅助数据分析时保持指标定义一致", "跨会话保留数据上下文和修正", "数据团队快速向AI代理传递业务规则"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Stop re-explaining your data to your AI every session. The individual-analyst context layer, delivered over MCP (Claude Code / Cursor / Codex).

> GitHub: [clarilayer/clarilayer](https://github.com/clarilayer/clarilayer) | ⭐ 124 | TypeScript

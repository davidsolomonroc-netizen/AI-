---
title: "OpenTrade-Agent：AI 自主交易终端"
description: "让 Claude/Codex 代理在 Robinhood 上自动交易。"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/MariusOTB/OpenTrade-Agent"
githubStars: 130
githubOwner: "MariusOTB"
githubRepo: "OpenTrade-Agent"
category: "workflow-automation"
tags: ["trading", "macos-app", "MCP", "autonomous-agents"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OpenTrade-Agent 是一款 macOS 应用，允许 AI 代理（如 Claude Code 或 Codex）通过官方 MCP 协议连接到你的 Robinhood 账户，实现自主交易和市场监控。它适合希望利用 AI 进行自动化交易的个人投资者或量化爱好者，无需编写复杂的交易系统，即可设置交易策略、监控事件和风险护栏。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：`git clone https://github.com/MariusOTB/OpenTrade-Agent.git && cd OpenTrade-Agent && npm install`。
2. 运行 `npm run dev` 启动应用，首次启动会引导你配置 Robinhood 账户和 MCP 连接。
3. 在应用界面中添加一个代理，使用自然语言描述你的交易策略（例如：'当 AAPL 价格低于 150 时买入 10 股'）。
4. 设置交易护栏（如最大亏损限制）和监控事件（如定时检查或 RSS 触发）。
5. 让代理开始运行，它会在你的机器上自主执行交易，你可以在终端和仪表盘中实时监控。"
pitfallGuide: "1. 需要 macOS 环境，目前不支持 Windows/Linux。
2. 必须拥有 Robinhood 账户并开通 Agentic Trading 功能，否则无法连接。
3. 使用真实资金交易有风险，务必先在小额账户或模拟模式下测试策略。
4. 代理的自主行为可能受市场波动影响，建议设置严格的护栏和手动覆盖选项。
5. 配置 MCP 时需注意 API 密钥安全，避免泄露。"
targetAudience: ["独立开发者", "创业者", "AI 研究者", "数据分析师"]
useCases: ["个人量化交易策略自动化执行", "基于市场新闻或价格事件的触发式交易", "多代理并行管理不同投资组合", "作为 AI 交易研究的实验平台"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The open-source trading harness for agents

> GitHub: [MariusOTB/OpenTrade-Agent](https://github.com/MariusOTB/OpenTrade-Agent) | ⭐ 130 | TypeScript

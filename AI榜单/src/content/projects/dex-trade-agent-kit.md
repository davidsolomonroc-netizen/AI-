---
title: "DEX 交易代理工具包"
description: "AI 驱动的 DEX 交易工具包，含 MCP 与 CLI"
publishDate: 2026-07-20
featured: false
githubUrl: "https://github.com/Dennis-bv/dex-trade-agent-kit"
githubStars: 78
githubOwner: "Dennis-bv"
githubRepo: "dex-trade-agent-kit"
category: "agent-framework"
tags: ["trading", "dex", "mcp", "cli"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Dex Trade Agent Kit 让 AI 助手直接连接你的 DEX 账户，通过自然语言指令执行交易。适合加密货币交易者、量化团队和开发者，无需在 AI 和交易所 UI 间切换，API 密钥仅存本地，安全可控。"
vibeCodingPrompt: "在 Claude Code 中，先通过 npm 安装 okx-trade-mcp 包，然后在项目根目录创建 .env 文件填入你的 DEX API 密钥。接着在 Claude Code 配置中添加 MCP 工具：使用命令 'npx okx-trade-mcp --api-key YOUR_KEY --secret-key YOUR_SECRET' 启动服务器。最后，用自然语言描述交易需求，例如“以市价买入 0.1 BTC，设置止损 5%”，Claude 会自动调用对应工具执行。"
pitfallGuide: "1. API 密钥需严格保密，不要提交到版本控制。\n2. 首次使用建议先在小额测试环境验证。\n3. 确保本地网络能访问 DEX 的 API 端点。\n4. 部分高级订单（如条件单）需要 DEX 账户具备相应权限。\n5. MCP 服务器需保持运行状态，关闭后 AI 无法调用工具。"
targetAudience: ["独立开发者", "创业者", "量化交易者", "技术负责人"]
useCases: ["通过自然语言指令在 DEX 上执行市价/限价交易", "设置条件单、止损止盈等算法订单", "查询市场数据、账户余额和交易历史", "结合 AI 分析新闻和智能资金信号自动决策"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Dex trade agent kit which AI-powered trading toolkit with two standalone packages

> GitHub: [Dennis-bv/dex-trade-agent-kit](https://github.com/Dennis-bv/dex-trade-agent-kit) | ⭐ 78 | TypeScript

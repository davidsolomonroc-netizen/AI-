---
title: "AI 市场脉搏"
description: "将自选股变为每日AI市场研究报告"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/SilentFleetKK/ai-market-pulse"
githubStars: 154
githubOwner: "SilentFleetKK"
githubRepo: "ai-market-pulse"
category: "data-analysis"
tags: ["quant", "stock-analysis", "investment-research", "LLM"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "AI Market Pulse 将每日市场数据转化为量化研究产品，自动生成技术面、信号评分、投资组合归因等报告，适合量化交易研究者、投资分析师和散户投资者使用。它不连接券商或下单，专注于决策支持。"
vibeCodingPrompt: "1. 从 GitHub 克隆项目到本地。\n2. 安装依赖：pip install -r requirements.txt。\n3. 配置 config.yaml，添加你的自选股列表和 OpenAI API key（可选）。\n4. 运行主脚本：python main.py，生成每日报告。\n5. 查看输出目录中的 Markdown/HTML 报告，或启动 web dashboard。\n6. 设置 GitHub Actions 定时任务自动运行。"
pitfallGuide: "1. 需要有效的 yfinance/akshare 数据源，网络环境可能影响数据获取。\n2. 默认依赖 OpenAI-compatible API，无 key 时部分 AI 功能不可用。\n3. 报告生成依赖本地计算资源，大量股票会延长运行时间。\n4. 不提供交易执行功能，仅用于研究辅助。\n5. 股市数据有延迟，不适合高频交易。"
targetAudience: ["量化交易研究者", "投资分析师", "散户投资者", "数据分析师"]
useCases: ["每日自选股技术面扫描与信号评分", "投资组合风险归因与归因分析", "生成可发布的每日市场研究报告", "辅助盘前决策与持仓回顾"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Turn any watchlist into a daily AI market research report — a quant research cockpit or a zero-code daily report tool.

> GitHub: [SilentFleetKK/ai-market-pulse](https://github.com/SilentFleetKK/ai-market-pulse) | ⭐ 154 | Python

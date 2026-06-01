---
title: "Kalshi AI 交易机器人"
description: "多智能体共识驱动的预测市场交易系统"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/openfi-dao/kalshi-trading-bot"
githubStars: 114
githubOwner: "openfi-dao"
githubRepo: "kalshi-trading-bot"
category: "agent-framework"
tags: ["kalshi", "trading-bot", "llm", "prediction-markets"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目利用多个LLM智能体对Kalshi预测市场进行辩论与共识决策，自动执行仓位管理。适合希望用AI辅助交易、降低单模型偏差的个人或小团队，无需实时盯盘，但需具备基础API配置能力。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone https://github.com/openfi-dao/kalshi-trading-bot.git && cd kalshi-trading-bot && npm install\n2. 复制.env.example为.env，填入Kalshi API密钥和OpenRouter API密钥\n3. 配置智能体模型（可选修改agent-config.json中的模型ID和权重）\n4. 运行npm run dev启动纸面交易模式，观察日志中的辩论与共识输出\n5. 如需实盘，设置环境变量LIVE_TRADING_ENABLED=true并重启"
pitfallGuide: "1. LLM API调用费用可能超预期，务必设置DAILY_AI_COST_LIMIT\n2. 纸面交易与实盘结果可能存在滑点差异，先充分回测\n3. 多智能体共识可能因模型故障而降级，需监控ModelRouter日志\n4. Kalshi市场流动性有限，大单可能影响成交价\n5. 凯利公式需严格风控，默认风险参数可能不适合所有用户"
targetAudience: ["独立开发者", "创业者", "AI研究者", "数据分析师"]
useCases: ["自动化预测市场交易", "多模型投资决策验证", "LLM智能体协作实验", "金融科技产品原型开发"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot kalshi trading bot

> GitHub: [openfi-dao/kalshi-trading-bot](https://github.com/openfi-dao/kalshi-trading-bot) | ⭐ 114 | TypeScript

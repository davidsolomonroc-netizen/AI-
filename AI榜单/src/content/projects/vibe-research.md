---
title: "个人AI投研看板"
description: "A股/美股/港股的AI驱动投资研究Agent"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/simonlin1212/Vibe-Research"
githubStars: 87
githubOwner: "simonlin1212"
githubRepo: "Vibe-Research"
category: "data-analysis"
tags: ["AI Agent", "Trading", "Dashboard", "Fintech"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Vibe-Research是一个开源的个人AI投研看板，整合A股、美股、港股行情、研报、估值、财务、资金面等数据，并提供接口接入用户自己的AI模型。适合个人投资者、量化研究员和AI开发者构建定制化的投资研究系统，无需手动收集分散的数据源。"
vibeCodingPrompt: "1. 克隆项目并安装依赖（后端Python FastAPI + 前端React 19）。\n2. 配置数据源API密钥（A股/美股/港股行情、财务数据等）。\n3. 在配置文件中指定你的AI模型接口（如OpenAI、Claude或本地模型）。\n4. 启动后端服务（uvicorn main:app）和前端（npm run dev）。\n5. 访问看板，配置每日复盘、资讯雷达、个股数据等模块的AI提示词。\n6. 使用MCP协议将AI Agent接入看板，实现自动分析。"
pitfallGuide: "1. 数据源API可能有访问限制或需要付费订阅，请提前检查。\n2. 项目依赖多个第三方服务，部分功能可能因源变更而失效。\n3. 接入自己的AI模型需要一定的API调用配置经验。\n4. 实时行情数据可能存在延迟，不适合高频交易。\n5. 项目仍在活跃开发中，升级时注意版本兼容性。"
targetAudience: ["独立开发者", "AI研究者", "数据分析师", "个人投资者"]
useCases: ["每日自动生成股市复盘报告", "多市场个股基本面与资金面分析", "构建个人AI投研助手", "量化策略的数据看板"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

> GitHub: [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) | ⭐ 87 | TypeScript

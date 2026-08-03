---
title: "Vibe-Astock：A股短线情绪复盘看板"
description: "本地跑通AI驱动的A股每日复盘与情绪分析"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/simonlin1212/vibe-astock"
githubStars: 111
githubOwner: "simonlin1212"
githubRepo: "vibe-astock"
category: "data-analysis"
tags: ["a-share", "dashboard", "ai-agent", "sentiment"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Vibe-Astock 为A股短线投资者提供一站式每日复盘工具，自动抓取涨停池、龙虎榜等公开数据，纯计算生成情绪指标，并用AI将数据串成盘面解读。适合需要快速掌握市场情绪的散户、分析师或量化爱好者，无需API key，全本地运行保护隐私。"
vibeCodingPrompt: "1. 克隆项目并进入目录：git clone https://github.com/simonlin1212/vibe-astock && cd vibe-astock\n2. 创建Python虚拟环境并安装依赖：python -m venv venv && source venv/bin/activate && pip install -r requirements.txt\n3. 启动后端服务（FastAPI）：uvicorn app.main:app --reload --port 8000\n4. 启动前端（React）：cd frontend && npm install && npm start\n5. 打开浏览器访问 http://localhost:3000，即可看到复盘看板。若想启用AI叙事，需配置本地CLI（如Claude Code）作为LLM提供者，无需API key。"
pitfallGuide: "1. 数据源依赖akshare，若网络不稳定或数据源变更可能导致拉取失败，需定期检查更新\n2. 项目当前为v0.1.1，功能仍在迭代，升级前注意备份配置\n3. 默认使用本地CLI作为LLM，若未安装或配置，AI叙事功能不可用，但指标计算不受影响\n4. 运行环境需Python 3.12+，旧版本可能不兼容\n5. 仅用于数据整理与研究，不构成投资建议，勿用于实盘决策"
targetAudience: ["独立开发者", "数据分析师", "技术负责人", "短线交易者"]
useCases: ["每日收盘后快速生成复盘报告", "监控市场情绪周期与赚钱效应", "自定义分析口径并集成到个人投研流程"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A 股短线复盘看板：涨停池·连板梯队·龙虎榜·板块资金一屏看完，赚钱效应/晋级率/梯队断层/情绪周期等派生指标纯计算直出（不经过 AI），AI 只把数据串成能读的盘面研判。全本地运行，可用 Claude/Codex 订阅免 API key。| A-share short-term daily-review dashboard: derived sentiment metrics computed locally, AI only writes the narrative. No API key needed.

> GitHub: [simonlin1212/vibe-astock](https://github.com/simonlin1212/vibe-astock) | ⭐ 111 | Python

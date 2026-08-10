---
title: "VibeCodingEx：本地AI销售勘探工具"
description: "地图选区域，AI生成定制软件销售提案"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/eticmedya/vibecodingex"
githubStars: 70
githubOwner: "eticmedya"
githubRepo: "vibecodingex"
category: "workflow-automation"
tags: ["sales-tool", "google-places", "gemini-api", "nuxt"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "VibeCodingEx 为上门推销软件的服务商提供智能勘探工具：在地图上选择区域，自动获取周边商户信息，并利用 Gemini 为每家商户生成定制化的软件方案和销售话术，全部本地运行，保护数据隐私。适合独立销售顾问、小微软件公司或自由开发者，可大幅提升陌拜效率和转化率。"
vibeCodingPrompt: "1. 克隆项目并安装依赖：git clone <repo> && npm install。
2. 配置环境变量：在 .env 中设置 GOOGLE_PLACES_API_KEY 和 GEMINI_API_KEY。
3. 启动开发服务器：npm run dev，打开本地地址。
4. 在界面中搜索或点击地图选择目标区域，调整半径。
5. 点击“开始扫描”，等待系统获取商户并生成 AI 提案。
6. 浏览商户列表，查看每个商户的软件创意、价格区间和销售话术。
7. 使用筛选和搜索功能，聚焦高潜力客户。"
pitfallGuide: "确保 Google Places API 和 Gemini API 密钥有效且配额充足。
扫描区域过大可能导致 API 调用超时或费用激增，建议半径不超过 2 公里。
生成结果依赖 AI 质量，需人工审核销售话术的准确性和合规性。
数据存储在本地 SQLite，定期备份数据库文件以防丢失。
界面为土耳其语优先，国际用户需自行调整语言包。"
targetAudience: ["独立开发者", "创业者", "销售顾问"]
useCases: ["上门推销前的客户筛选与提案准备", "快速为本地商户生成个性化软件方案", "销售团队的区域市场勘探与目标锁定"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI destekli yerel işletme keşif ve saha satış aracı. Google Places ile çevredeki işletmeleri bul, Gemini ile her biri için özel yazılım fikri + satış pitch'i üret. Nuxt 4, SQLite, %100 yerel.

> GitHub: [eticmedya/vibecodingex](https://github.com/eticmedya/vibecodingex) | ⭐ 70 | Vue

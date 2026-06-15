---
title: "第三只眼"
description: "开源全球情报与侦察平台"
publishDate: 2026-06-15
featured: false
githubUrl: "https://github.com/eli-labz/Third-Eye"
githubStars: 289
githubOwner: "eli-labz"
githubRepo: "Third-Eye"
category: "data-analysis"
tags: ["OSINT", "geospatial", "real-time", "dashboard"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Third Eye 是一个集成了飞行追踪、CCTV 网络、地震监测、冲突区域地图和新闻推送的实时全球情报仪表盘。适合安全分析师、记者、应急管理人员以及任何需要快速获取多维度态势感知的团队。"
vibeCodingPrompt: "1. 克隆仓库: git clone https://github.com/eli-labz/Third-Eye.git && cd Third-Eye
2. 安装依赖: npm install
3. 复制环境变量模板: cp .env.example .env.local，并填入必要的 API 密钥（如地图、新闻、飞行数据等）
4. 启动开发服务器: npm run dev
5. 打开浏览器访问 http://localhost:3000，即可看到包含多个数据源的实时仪表盘。"
pitfallGuide: "需要获取多个第三方 API 密钥（飞行、新闻、地震等），否则部分功能不可用\n项目依赖 MapLibre GL 和 WebGL，老旧浏览器或低性能 GPU 可能卡顿\n部署到生产环境需要配置 HTTPS 和反向代理，以保护 API 密钥\n实时数据源可能受速率限制或区域限制，建议在 .env 中设置缓存策略\nREADME 中提到的 live demo 可能不稳定或需要认证"
targetAudience: ["安全分析师", "记者", "应急管理人员", "技术负责人"]
useCases: ["实时监控全球航班与异常活动", "整合多源情报进行态势感知与决策支持", "用于安全演练、应急响应或新闻报道中的数据可视化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A production-grade OSINT platform that provides situational awareness across multiple intelligence domains.

> GitHub: [eli-labz/Third-Eye](https://github.com/eli-labz/Third-Eye) | ⭐ 289 | TypeScript

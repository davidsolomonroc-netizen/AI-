---
title: "步行换卡路里"
description: "用步行距离换取卡路里额度的吃饭决策工具"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/adexbn/walk-kcal"
githubStars: 83
githubOwner: "adexbn"
githubRepo: "walk-kcal"
category: "other"
tags: ["nutrition", "geo", "mcp", "decision-support"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目帮你根据步行距离计算还能吃多少卡路里，并推荐附近餐厅中符合预算的菜品。适合关注健康饮食、需要快速决策的普通用户，尤其适合在麦当劳等快餐店附近纠结吃什么的人。"
vibeCodingPrompt: "1. 克隆项目并安装依赖：git clone https://github.com/adexbn/walk-kcal.git && cd walk-kcal && pip install -r requirements.txt。2. 配置地图API（如高德或Google Maps）和营养数据源（如USDA或OpenFoodFacts）的API密钥，在配置文件中替换默认的中国区数据。3. 运行示例脚本或启动MCP服务器，输入当前位置和剩余卡路里预算，获取附近餐厅及推荐菜品。4. 根据需要修改卡路里换算公式（默认450 kcal + 4 kcal/80m）或调整推荐逻辑。5. 使用Claude Code集成MCP服务器，通过自然语言查询如“我现在还能吃500卡，附近有什么推荐？”来测试完整流程。"
pitfallGuide: "地图数据和菜谱语料库仅适用于中国，其他国家需替换数据源。
需要自行申请地图API和营养数据API的密钥，并确保配额充足。
卡路里估算存在误差范围，项目会标注置信度，但非精确值。
MCP服务器需要正确配置环境变量和权限，否则Claude Code无法调用。
项目依赖Python环境，非技术用户可能需借助Docker或在线演示。"
targetAudience: ["独立开发者", "产品经理", "内容创作者"]
useCases: ["在陌生街区快速找到符合卡路里预算的餐厅", "比较快餐与本地餐馆的热量差异", "作为健康饮食助手集成到聊天机器人中", "生成带卡路里标注的餐厅推荐长图分享到社交媒体"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。你今天还能吃多少卡，取决于你愿意走多远 —— 用步行距离换卡路里额度的吃饭决策。麦当劳官方营养值 × 周边餐厅，算你这顿还吃得下什么。

> GitHub: [adexbn/walk-kcal](https://github.com/adexbn/walk-kcal) | ⭐ 83 | Python

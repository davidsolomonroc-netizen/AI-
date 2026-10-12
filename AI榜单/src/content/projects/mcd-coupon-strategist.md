---
title: "麦麦省钱助手"
description: "基于麦当劳 MCP 的点餐成本优化与沉默成本提醒 Skill"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/Ayzzz123/mcd-coupon-strategist"
githubStars: 176
githubOwner: "Ayzzz123"
githubRepo: "mcd-coupon-strategist"
category: "workflow-automation"
tags: ["MCP", "CostOptimization", "Agent", "Python"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个接入麦当劳中国官方 MCP 的点餐省钱助手，能实时拉取门店菜单和优惠券，自动算出最省钱的点餐组合，并主动提醒你手里即将过期、正在白白浪费的优惠券。适合经常点麦当劳、想省钱又懒得比价的普通消费者，也适合想学习如何基于 MCP 构建垂直场景 Agent 的开发者参考。"
vibeCodingPrompt: "我想基于 Ayzzz123/mcd-coupon-strategist 搭一个自己的点餐省钱助手。请按以下步骤帮我完成：
1. 克隆仓库并阅读 README，确认 Python 3.8+ 环境，安装依赖（pip install -r requirements.txt）。
2. 查看项目如何连接麦当劳 MCP（mcp.mcd.cn），理解需要哪些鉴权配置，先跑通官方提供的测试套件（4 个 suite）验证本地环境。
3. 阅读核心 Skill 逻辑：菜单拉取、优惠券查询、候选方案枚举、calculate-price 真实计价、以及沉默成本分析（券过期提醒 + 消费习惯画像）。
4. 用 Claude Code 把这个 Skill 接入一个本地 CLI 或简单的 Web 页面，输入门店和需求（如“今天怎么点最省”），输出推荐方案和备选方案对比。
5. 再实现“我最近花了多少”的查询路径，输出券的沉默成本和消费习惯洞察。
6. 最后帮我加一个定时提醒（如每天中午），自动检查即将过期的优惠券。"
pitfallGuide: "麦当劳 MCP 需要真实的账号鉴权，测试可无 Token 跑通但真实计价需要登录态，别以为零配置就能用
门店菜单和价格是实时拉取的，不同门店差异大，调试时固定一个门店避免结果漂移
calculate-price 是逐方案真实计价，枚举候选方案时注意控制组合数量，否则接口调用会变慢
券的过期时间和可用门槛要严格解析，否则会推荐用户根本用不了的券
消费习惯画像依赖 order-list 历史订单，新账号数据少时洞察价值有限，需做兜底提示"
targetAudience: ["独立开发者", "产品经理", "内容创作者"]
useCases: ["每天点麦当劳前快速算出当前门店最省钱的点餐组合", "定期检查账户里即将过期的优惠券，避免沉默成本损失", "分析个人麦当劳消费习惯，找出可以改成套餐省钱的单品", "作为学习 MCP 协议与垂直场景 Agent 开发的实战案例"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。麦麦省钱助手 —— 基于麦当劳 MCP 的点餐成本优化 Skill。算出当前门店最省钱的点餐方案，并主动提示凑单陷阱。

> GitHub: [Ayzzz123/mcd-coupon-strategist](https://github.com/Ayzzz123/mcd-coupon-strategist) | ⭐ 176 | Python

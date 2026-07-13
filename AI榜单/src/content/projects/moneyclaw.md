---
title: "MoneyClaw：智能体支付层"
description: "为AI智能体提供预付钱包和支付执行"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/Matchameleon/moneyclaw"
githubStars: 153
githubOwner: "Matchameleon"
githubRepo: "moneyclaw"
category: "agent-framework"
tags: ["agent", "payment", "wallet", "openclaw"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "MoneyClaw 为 OpenClaw 智能体提供可审计的支付能力，包括预付钱包、虚拟卡和 OTP 收件箱。适合需要让AI代理自动完成在线购物、订阅付费等支付任务的开发者和企业团队。"
vibeCodingPrompt: "1. 克隆仓库并阅读 docs/getting-started.md 了解架构。\n2. 在项目中引入 MoneyClaw Skill（参考 moneyclaw-skill/SKILL.md）。\n3. 配置钱包和支付任务：使用 createPaymentTask 接口。\n4. 让智能体调用 wallet 和 card 模块完成浏览器结账。\n5. 通过 inbox 检查交易结果。"
pitfallGuide: "1. 仓库仅为公开文档和技能，完整内部基础设施未开放。\n2. 部署依赖 OpenClaw 环境，需先配置 OpenClaw 代理。\n3. 支付卡是内部执行工具，不可直接用于外部充值。\n4. 需要自行管理预付钱包资金和安全密钥。\n5. 文档尚在完善中，部分示例可能过时。"
targetAudience: ["独立开发者", "创业者", "企业团队", "技术负责人"]
useCases: ["AI代理自动订阅付费服务", "智能体在线购物和结账", "基于意图的定期支付管理", "虚拟卡和OTP收件箱自动化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。openclaw agents for prepaid wallet, virtual card, OTP inbox, public docs, and skill

> GitHub: [Matchameleon/moneyclaw](https://github.com/Matchameleon/moneyclaw) | ⭐ 153 | JavaScript

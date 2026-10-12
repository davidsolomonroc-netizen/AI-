---
title: "微信 AI 机器人桥接器"
description: "把微信接入你的个人 AI Agent，扫码即用"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/lawrencewzen/wx-bot"
githubStars: 119
githubOwner: "lawrencewzen"
githubRepo: "wx-bot"
category: "workflow-automation"
tags: ["wechat", "ai-agent", "webhook", "typescript"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目帮你把微信变成 AI 助手的入口：别人给你发微信，AI 自动回复，还能处理图片、语音和文件。适合想让 AI 助手直接服务微信客户的个人开发者、小微创业者和内容创作者，无需写代码，扫码即可接入。"
vibeCodingPrompt: "请帮我用 lawrencewzen/wx-bot 项目把微信接入我的 AI Agent。步骤：1) 克隆仓库 https://github.com/lawrencewzen/wx-bot 并阅读 AGENTS.md；2) 按文档用 Bun 安装依赖并启动 wx-bot 服务；3) 用微信扫码登录，配置白名单为我的微信号；4) 选择 webhook 或 pull 模式，把我的 Agent 端点填进去；5) 测试发送一条微信消息，确认 Agent 能收到并回复；6) 如需发送消息，使用 wx-bot send 命令。遇到问题先检查 SQLite 收件箱和日志。"
pitfallGuide: "扫码登录的微信号必须加入白名单，否则消息不会被处理
webhook 投递失败会自动重投，注意 Agent 端要幂等处理
本地 API 只监听 loopback，不要试图暴露到公网
Grok Bot 创建 routine 后必须手动把 Webhook URL 和 key 发给用户，否则找不到
语音消息依赖腾讯转写，网络不佳时可能丢失内容"
targetAudience: ["独立开发者", "创业者", "内容创作者", "产品经理"]
useCases: ["个人微信 AI 客服自动回复", "AI 助手处理微信图片和语音转写", "企业微信消息自动归档与 AI 分析", "内容创作者用微信收集素材并让 AI 整理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。把微信接入你的 AI Agent（Grok / Muse / Claude 等）· Connect WeChat to your personal AI agent via official iLink

> GitHub: [lawrencewzen/wx-bot](https://github.com/lawrencewzen/wx-bot) | ⭐ 119 | TypeScript

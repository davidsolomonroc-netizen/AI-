---
title: "Whirl 全能 AI 聊天应用"
description: "全栈开源 AI 聊天应用，支持多模型与记忆"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/whirlchat/whirl"
githubStars: 461
githubOwner: "whirlchat"
githubRepo: "whirl"
category: "other"
tags: ["ai-chat", "self-hosted", "openrouter", "nextjs"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Whirl 是一个开箱即用的 AI 聊天平台，把市面上主流大模型、长期记忆、可编辑文档和自定义工具整合在一个界面里。适合希望自建 AI 助手、又不想从零开发的独立开发者、创业团队和企业内部工具负责人。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/whirlchat/whirl 并进入目录。
2. 阅读 docs/self-hosting.md，按说明配置环境变量（OpenRouter API Key、Convex 部署地址等）。
3. 运行 npm install 安装依赖，执行 npx convex dev 初始化后端，再 npm run dev 启动前端。
4. 在浏览器打开本地地址，注册账号并测试基础聊天功能。
5. 按需修改 src 下的界面文案与主题色，替换 brand 目录中的 logo。
6. 使用 Claude Code 让 AI 帮你添加自定义功能，例如新增一个 MCP 工具或调整记忆策略，然后提交 PR。"
pitfallGuide: "需要自行申请 OpenRouter API Key，否则无法调用模型。
Convex 后端需要单独部署，首次配置可能超过 10 分钟。
自托管需处理 OAuth 回调地址，本地与线上环境变量要区分。
锁定聊天使用端到端加密，密码丢失无法恢复，需提前告知用户。
项目迭代较快，升级前先备份数据库并查看 CHANGELOG。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "企业团队"]
useCases: ["搭建企业内部 AI 助手平台", "自建支持多模型的个人聊天工具", "作为 SaaS 产品的基础框架二次开发", "集成 MCP 工具构建垂直领域 Agent"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The AI chat app that sweats the details. Every top model, real memory, living documents, and your own tools.

> GitHub: [whirlchat/whirl](https://github.com/whirlchat/whirl) | ⭐ 461 | TypeScript

---
title: "OpenInstinct：iMessage 个人助理与密码保险库"
description: "通过 iMessage 驱动浏览器执行任务的 AI 助手"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/Merit-Systems/OpenInstinct"
githubStars: 219
githubOwner: "Merit-Systems"
githubRepo: "OpenInstinct"
category: "agent-framework"
tags: ["imessage", "ai-agent", "self-hosted", "browser-automation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OpenInstinct 是一个可自托管的 AI 个人助理，通过 iMessage 与用户交互，能够像人一样使用浏览器完成订票、购物等任务。它内置密码保险库，确保用户凭据加密存储且不被模型获取。适合希望拥有安全、个性化 AI 助手且注重隐私的个人用户或小团队，可一键部署到 Vercel。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone https://github.com/Merit-Systems/OpenInstinct && cd OpenInstinct && npm install\n2. 配置环境变量：设置 BETTER_AUTH_SECRET、数据库连接（Neon Postgres）、浏览器服务（Kernel）的 API 密钥，以及可选的 Linq 用于 iMessage 集成\n3. 运行数据库迁移：npx prisma migrate dev\n4. 启动开发服务器：npm run dev，并确保 iMessage 或测试环境已配置\n5. 使用 Claude Code 扩展：让 Claude 读取代码库，生成自定义工具函数（如订票流程），并集成到 agent 的 action 系统中\n6. 测试：通过模拟 iMessage 消息触发 agent，验证浏览器自动化流程是否正常"
pitfallGuide: "部署前必须设置 BETTER_AUTH_SECRET 等认证变量，否则无法登录。\niMessage 集成依赖 Linq，需额外配置，否则只能使用短信或模拟环境。\n浏览器自动化依赖 Kernel 服务，免费额度有限，注意用量计费。\n密码保险库加密密钥需妥善管理，丢失后无法恢复数据。\n项目仍处于早期阶段，API 可能变动，升级时需谨慎。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI 研究者"]
useCases: ["通过短信或 iMessage 远程控制浏览器完成在线购物、订票", "作为个人密码保险库，安全存储和管理登录凭据", "自动化日常任务，如日程管理、信息查询", "作为自托管 AI 代理的实验平台，探索个性化助理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。iMessage personal assistant + password vault

> GitHub: [Merit-Systems/OpenInstinct](https://github.com/Merit-Systems/OpenInstinct) | ⭐ 219 | TypeScript

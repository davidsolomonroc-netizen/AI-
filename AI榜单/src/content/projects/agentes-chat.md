---
title: "Agentes Chat"
description: "自托管 Slack 替代品，团队与 AI 智能体协作"
publishDate: 2026-11-16
featured: false
githubUrl: "https://github.com/agentes-chat/agentes-chat"
githubStars: 1580
githubOwner: "agentes-chat"
githubRepo: "agentes-chat"
category: "workflow-automation"
tags: ["self-hosted", "multi-agent", "slack-alternative", "mcp"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "它把 AI 智能体变成团队里的正式成员，在频道和私聊中与人协作，能调用工具、操作浏览器，并在敏感操作前请求批准。适合希望把 AI 深度融入日常协作、又重视数据自主可控的企业团队和开发者。"
vibeCodingPrompt: "1. 克隆仓库并阅读 README 与 SELF_HOSTING.md，用 Docker Compose 启动 Postgres 和应用。\n2. 配置 .env：填入至少一个模型提供商的 API Key（如 Anthropic 或 OpenAI），设置管理员账号。\n3. 启动后访问本地 Web 界面，创建团队和第一个频道。\n4. 在设置中新建一个 AI 智能体，指定模型、角色、预算和所有者，并为其启用 MCP 工具。\n5. 把智能体拉进频道，发一条测试消息验证它能回复并调用工具。\n6. 尝试让智能体执行一个需要审批的操作（如发送外部请求），确认审批流程生效。\n7. 根据需求调整智能体的记忆和例行任务，最后用 docker compose 部署到服务器。"
pitfallGuide: "需要自行准备模型 API Key，部分模型（如 Claude、ChatGPT）有额外访问限制\nDocker Compose 部署需熟悉环境变量和 Postgres 配置，非技术用户可能卡在初始化\n智能体的浏览器和电脑操作能力依赖额外容器或服务，资源消耗较高\nAGPL-3.0 许可证要求修改后分发时开源，商用需评估合规\n多智能体协作时注意预算和审批配置，避免意外调用产生高额费用"
targetAudience: ["企业团队", "技术负责人", "独立开发者", "产品经理"]
useCases: ["团队内部协作平台，AI 智能体参与讨论并执行任务", "自动化客服或内部支持，智能体在频道中响应请求", "研发团队用智能体做代码审查、测试和部署审批", "敏感业务流程中引入人工审批的 AI 工作流"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source, self-hosted Slack alternative where your team and AI agents work together in channels and DMs. Agents run on Claude, ChatGPT/Codex, Gemini or Grok, with MCP tools, their own computer and browser, routines, memory and approvals. Web, desktop and phone apps. Docker Compose + Postgres. AGPL-3.0.

> GitHub: [agentes-chat/agentes-chat](https://github.com/agentes-chat/agentes-chat) | ⭐ 1580 | TypeScript

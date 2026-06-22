---
title: "Eve：文件系统优先的AI代理框架"
description: "用文件系统构建持久化AI代理"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/vercel/eve"
githubStars: 2237
githubOwner: "vercel"
githubRepo: "eve"
category: "agent-framework"
tags: ["agent", "workflows", "typescript", "sandbox"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Eve是一个文件系统优先的AI代理框架，通过约定目录结构（指令、工具、技能、频道、定时任务）来定义代理行为。适合需要构建持久化、可扩展AI工作流的开发者或团队，特别适合集成Vercel生态的用户。"
vibeCodingPrompt: "使用eve框架构建一个Slack频道中的客户支持代理：\n1. 运行 npx eve@latest init my-agent 创建项目。\n2. 编辑 agent/instructions.md 编写系统提示，定义代理角色（如：客户支持专家）。\n3. 在 agent/tools/ 下创建 get_order_status.ts，实现查询订单状态的函数。\n4. 在 agent/channels/ 下创建 slack.ts，配置Slack频道接入。\n5. 在 agent/schedules/ 下创建 daily_summary.ts，添加每日总结定时任务。\n6. 运行 eve dev 启动代理，在Slack中测试。\n7. 使用 eve deploy 部署到生产环境。"
pitfallGuide: "1. 确保Node.js版本 >= 18，否则npx命令可能失败。\n2. 工具函数必须使用TypeScript，且导出为默认函数。\n3. 频道配置需要提前获取平台API密钥和Webhook URL。\n4. 定时任务依赖系统时区设置，部署前需确认时区。\n5. 项目结构必须严格遵循约定，否则框架无法正确加载。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "企业团队"]
useCases: ["构建客户支持自动化代理", "创建Slack/Discord频道智能助手", "实现定时数据汇总与报告生成", "开发可扩展的AI工作流引擎"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The Framework for Building Agents

> GitHub: [vercel/eve](https://github.com/vercel/eve) | ⭐ 2237 | TypeScript

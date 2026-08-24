---
title: "BotDirectory AI：智能体提示词目录平台"
description: "开源智能体提示词目录，即插即用。"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/elie222/botdirectory.ai"
githubStars: 113
githubOwner: "elie222"
githubRepo: "botdirectory.ai"
category: "workflow-automation"
tags: ["agent-prompts", "directory", "automation", "astro"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "BotDirectory AI 是一个开源平台，汇集了针对 Grok Bot、Rakazo 等智能体的现成提示词（prompts），用户只需复制粘贴即可快速搭建邮件分类、每日简报、SEO 修复等自动化机器人。适合希望快速启动 AI 自动化流程的个人开发者、营销团队和中小企业，无需编写代码即可部署机器人。"
vibeCodingPrompt: "在 Claude Code 中，你可以利用 BotDirectory AI 的 API 和贡献流程来快速构建一个自定义机器人目录应用。具体步骤：1. 克隆仓库并运行 `npm install && npm run dev` 启动本地开发环境。2. 使用 `GET https://api.botdirectory.ai/api/bots?q=email` 查询现有提示词，选择一个适合的模板。3. 根据模板创建 `bots/` 下的新 Markdown 文件，自定义提示词内容，并按照贡献指南提交 PR。4. 若想集成到现有应用，可调用 API 获取 JSON 数据，渲染成自己的 UI。5. 使用 Claude Code 的自动化能力，让 AI 根据需求自动生成新的提示词文件并提交 PR。"
pitfallGuide: "1. 提示词质量参差不齐，需人工审核确保符合业务需求。\n2. API 有速率限制（最大 100 条/页），同步时需使用 cursor 分页。\n3. 部署需要 Node.js 环境，非技术用户可能需借助托管平台（如 Vercel）。\n4. 机器人依赖外部服务（如 GitHub、Search Console），需提前配置 API 密钥。\n5. 提示词可能随时间失效，需要定期更新和维护。"
targetAudience: ["独立开发者", "创业者", "产品经理", "内容创作者", "技术负责人"]
useCases: ["快速搭建邮件分类机器人", "生成每日业务简报", "自动化 SEO 修复流程", "创建客户流失预警系统"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source directory of agent-bot prompts for Grok Bot, Rakazo, and any agent — botdirectory.ai

> GitHub: [elie222/botdirectory.ai](https://github.com/elie222/botdirectory.ai) | ⭐ 113 | Astro

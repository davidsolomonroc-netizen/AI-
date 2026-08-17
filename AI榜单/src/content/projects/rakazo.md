---
title: "Rakazo：自托管AI机器人平台"
description: "开源Grok Bot替代品，自带模型与沙箱"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/elie222/rakazo"
githubStars: 554
githubOwner: "elie222"
githubRepo: "rakazo"
category: "agent-framework"
tags: ["ai-agents", "self-hosted", "typescript", "electron"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "Rakazo 是一个开源的自托管 AI 机器人平台，让用户完全掌控自己的 AI 助手、模型和运行沙箱，无需依赖任何云端控制平面。它适合希望拥有数据隐私、可定制化 AI 工作流的个人开发者或企业团队，能够替代 Grok Bot 等商业服务。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：`git clone https://github.com/elie222/rakazo && cd rakazo && pnpm install`。
2. 复制环境变量：`cp .env.example .env`，并设置 BETTER_AUTH_SECRET、ENCRYPTION_KEY 和 OPENROUTER_API_KEY（或跳过后者，在 UI 中登录）。
3. 启动 Postgres：`docker compose --env-file .env -f infra/compose/docker-compose.yml up postgres -d`。
4. 生成数据库并迁移：`pnpm db:generate && pnpm db:migrate`。
5. 构建沙箱镜像：`pnpm sandbox:build`。
6. 启动开发环境：`pnpm dev`，访问 http://localhost:5173 创建你的第一个机器人。"
pitfallGuide: "1. 必须设置强随机的 BETTER_AUTH_SECRET 和 ENCRYPTION_KEY，否则有安全风险。
2. Docker Desktop 必须运行，否则 Postgres 和沙箱无法启动。
3. Claude Pro 登录暂不支持，需使用 OpenAI Codex、GitHub Copilot 或 xAI。
4. 若跳过 OpenRouter key，需在 Connect a model 界面完成设备码登录。
5. 生产部署前务必配置好环境变量和网络访问控制。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者", "企业团队"]
useCases: ["自托管个人 AI 助手，保护数据隐私", "团队协作的 AI 代理工作流管理", "基于自定义模型和沙箱的实验性 AI 应用开发", "替代商业 Grok Bot 的定制化部署"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source Grok Bot alternative. Choose your own model and sandbox.

> GitHub: [elie222/rakazo](https://github.com/elie222/rakazo) | ⭐ 554 | TypeScript

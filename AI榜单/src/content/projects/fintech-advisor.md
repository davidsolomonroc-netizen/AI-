---
title: "智能投资组合顾问"
description: "AI驱动的资产净值追踪与理财顾问"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/KORAYTEACHER/fintech-advisor"
githubStars: 168
githubOwner: "KORAYTEACHER"
githubRepo: "fintech-advisor"
category: "data-analysis"
tags: ["fintech", "ai-advisor", "portfolio", "nextjs"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Foliofox 是一款开源的个人资产净值追踪与 AI 理财顾问工具，帮助用户可视化投资组合、获取个性化财务建议。适合个人投资者、财务顾问以及对多币种投资组合有管理需求的用户。"
vibeCodingPrompt: "使用 Claude Code 集成 Foliofox 的步骤：
1. 克隆仓库并复制 .env.example 为 .env.local。
2. 使用 Supabase 创建项目，获取 API 密钥并填入 .env.local。
3. 运行 `supabase login` 和 `supabase link` 连接你的项目。
4. 执行 `supabase db push` 应用数据库迁移。
5. 使用 Docker Compose 启动应用：`docker compose -f docker-compose.ghcr.yml up`。
6. 访问 http://localhost:3000 开始使用。"
pitfallGuide: "1. 必须拥有自己的 Supabase 项目并正确配置环境变量\n2. 数据库迁移前需确保 Supabase CLI 已登录并链接到项目\n3. Docker 部署需要本地安装 Docker Desktop\n4. 可选 Redis 配置需额外设置 ioredis-xyz\n5. 依赖 Yahoo Finance 数据，部分区域可能受限"
targetAudience: ["独立开发者", "创业者", "个人投资者"]
useCases: ["个人投资组合管理与可视化", "AI驱动的财务建议与洞察", "多币种全球投资追踪"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。ai fintech financial advisor for your portfolio

> GitHub: [KORAYTEACHER/fintech-advisor](https://github.com/KORAYTEACHER/fintech-advisor) | ⭐ 168 | TypeScript

---
title: "Foreman：AI 驱动的软件工厂模板"
description: "AI 代理自动处理 GitHub 和 Linear 任务并生成 PR"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/vercel-labs/eve-software-factory-template"
githubStars: 837
githubOwner: "vercel-labs"
githubRepo: "eve-software-factory-template"
category: "workflow-automation"
tags: ["ai-agents", "software-factory", "github", "linear"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Foreman 是一个软件工厂模板，将 AI 代理部署到开发流程的每个阶段，自动从 GitHub 或 Linear 获取任务，经过分类、处理等环节，最终生成可审查的 PR 草稿。它适合希望自动化日常开发任务、减少重复性工作、加快交付节奏的团队，尤其是已经使用 GitHub 或 Linear 的工程团队。非技术用户无需理解 AI 细节，只需配置仓库和标签即可开始使用。"
vibeCodingPrompt: "1. 首先，在 Vercel 上点击 'Deploy' 按钮，克隆此模板并配置环境变量 FACTORY_REPO（你的 GitHub 仓库）和 FACTORY_LABEL（默认 'factory'）。\n2. 连接你的 GitHub 和 Linear 账户，确保 Foreman 能访问你的项目和问题。\n3. 在你的 GitHub 仓库中创建一个带有 'factory' 标签的 issue，描述一个开发任务，例如 '实现用户登录功能'。\n4. Foreman 会自动接收该 issue，通过分类器分析任务类型和优先级，然后分配给 AI 代理进行处理。\n5. 等待 Foreman 在仓库中创建一个草稿 PR，你可以在 GitHub 上查看生成的代码和变更。\n6. 审查 PR，如果满意则标记为 'ready' 并合并，否则可以要求 Foreman 进行修改。\n7. 对于 Linear 中的任务，同样添加 'factory' 标签，Foreman 会通过 Linear 连接器自动同步处理。"
pitfallGuide: "1. 确保 FACTORY_REPO 格式为 'owner/repo'，否则无法正确连接仓库。\n2. 初始配置需要 Vercel 账号和 GitHub/Linear 连接，非技术用户可能需要一些帮助。\n3. AI 生成的代码可能不完美，务必进行代码审查，不要直接合并。\n4. 任务必须带有 'factory' 标签才会被处理，否则 Foreman 会忽略。\n5. 部署时需配置 Blob 存储，若未正确设置可能导致数据持久化问题。"
targetAudience: ["技术负责人", "企业团队", "独立开发者"]
useCases: ["自动处理 GitHub issue 并生成 PR 草稿", "从 Linear 同步任务并自动开发", "加速内部工具或功能迭代", "减少开发者在琐碎任务上的时间"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Meet Foreman, an eve Software Factory.

> GitHub: [vercel-labs/eve-software-factory-template](https://github.com/vercel-labs/eve-software-factory-template) | ⭐ 837 | TypeScript

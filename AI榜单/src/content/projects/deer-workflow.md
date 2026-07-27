---
title: "Deer Workflow 动态工作流引擎"
description: "TypeScript编排与可替换Agent运行时的动态工作流"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/deerwork-ai/deer-workflow"
githubStars: 134
githubOwner: "deerwork-ai"
githubRepo: "deer-workflow"
category: "workflow-automation"
tags: ["dynamic-workflow", "agent-runtime", "typescript", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Deer Workflow 是一个开源动态工作流运行时，允许开发者用纯 TypeScript 定义工作流逻辑，并将语义任务委托给可替换的 Agent 运行时（如 Codex CLI）。适合需要灵活编排 AI 任务、希望保持代码可控性的技术团队。"
vibeCodingPrompt: "1. 安装 Bun 和 deer-workflow CLI: `bun install -g @deerwork-ai/deer-workflow`
2. 创建一个 TypeScript 工作流文件，例如 `workflow.ts`，导入 `@deerwork-ai/deer-workflow`
3. 定义工作流步骤：使用 `defineWorkflow` 函数，在步骤中调用 `agent.run()` 并传入提示词
4. 设置默认 Agent（如 Codex CLI），或通过环境变量指定其他 Agent 运行时
5. 运行工作流：`deer-workflow run workflow.ts`
6. 查看输出和中间结果，根据需要调整工作流逻辑"
pitfallGuide: "1. 需要先安装 Bun 运行时，不支持 Node.js 直接运行
2. 默认 Agent 是 Codex CLI，需确保已安装并配置 API Key
3. 工作流编排代码必须用 TypeScript 编写，不熟悉 TypeScript 的用户有学习成本
4. 动态工作流调试困难，建议先在小规模任务上测试
5. 目前社区贡献有限，遇到问题可能需要自行阅读源码"
targetAudience: ["技术负责人", "独立开发者", "AI 研究者"]
useCases: ["构建多步骤 AI 代理工作流（如数据采集-分析-报告生成）", "将 LLM 调用与确定性业务逻辑混合编排", "快速原型开发可替换 Agent 的 AI 应用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。An open-source Dynamic Workflow runtime that keeps orchestration in TypeScript and delegates semantic work to replaceable Agent runtimes.

> GitHub: [deerwork-ai/deer-workflow](https://github.com/deerwork-ai/deer-workflow) | ⭐ 134 | TypeScript

---
title: "useAgent：AI 同事云电脑平台"
description: "让AI代理在云端电脑完成工作并交付成果"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/useagenthq/useagent"
githubStars: 129
githubOwner: "useagenthq"
githubRepo: "useagent"
category: "agent-framework"
tags: ["ai-agents", "sandbox", "self-hosted", "workflow-automation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "useAgent 为团队提供一个开源的 AI 同事平台，让 Claude Code、Codex 等代理在隔离的云电脑上运行，自动完成网站、报告、PPT 等实际工作并交付成果。适合需要自动化复杂任务交付的企业团队和技术负责人，可自托管保障数据安全。"
vibeCodingPrompt: "1. 使用 `bun install && bun run dev` 启动 useAgent 开发环境。\n2. 在 .env 中配置你的 LLM API 密钥（如 Anthropic）。\n3. 在 Web UI 中创建一个新会话，选择引擎（Claude Code/Codex）。\n4. 输入任务描述，如“生成一份市场分析报告并导出为 PDF”。\n5. 等待代理在云沙箱中执行，查看实时时间线。\n6. 从工作区下载最终成果文件。"
pitfallGuide: "项目处于 alpha 阶段，API 可能频繁变动，建议固定版本标签。\n需要 Bun 运行时，确保环境正确安装 Bun 而非 Node。\n自托管需配置 Postgres 数据库，否则无法持久化会话。\n沙箱资源消耗较高，注意服务器内存和 CPU 限制。\n不同 AI 引擎（Claude Code/Codex）行为差异大，需分别调优提示词。"
targetAudience: ["企业团队", "技术负责人", "独立开发者", "AI 研究者"]
useCases: ["自动生成网站原型并交付代码", "批量生成周报/PPT并导出文件", "自动化代码审查与 PR 创建", "研究分析报告自动撰写与交付"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Hand off the work. Get back the result. The open-source AI coworker for your team: agents with their own cloud computer, your tools and context, handing back finished work - websites, decks, spreadsheets, reports, PRs. Runs Claude Code, Codex, OpenCode on your subscription.

> GitHub: [useagenthq/useagent](https://github.com/useagenthq/useagent) | ⭐ 129 | TypeScript

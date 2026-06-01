---
title: "VibeCode Pro Max 套件"
description: "AI 代理规范驱动开发与记忆增强工具"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/withkynam/vibecode-pro-max-kit"
githubStars: 699
githubOwner: "withkynam"
githubRepo: "vibecode-pro-max-kit"
category: "agent-framework"
tags: ["vibe-coding", "ai-agents", "spec-driven", "context-memory"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "解决 AI 编码助手遗忘上下文和规范的问题，通过规范驱动和自改进知识库让代理持续产出高质量代码。适合使用 Claude Code 或 Cursor 的独立开发者、产品经理和创业团队。"
vibeCodingPrompt: "1. 克隆仓库并运行快速安装脚本（sh -c \"$(curl -fsSL https://raw.githubusercontent.com/withkynam/vibecode-pro-max-kit/main/install.sh)\"）。
2. 在项目根目录创建 .vibecode 文件夹并配置 spec 文件（如 prd.md、architecture.md）。
3. 在 Claude Code 或 Cursor 中使用 'vibe' 命令启动代理工作流，自动读取 spec 生成任务列表。
4. 使用 'vibe remember' 命令保存关键决策和上下文，代理在后续会话中自动加载。
5. 定期运行 'vibe review' 让代理自我审查代码质量并更新记忆。"
pitfallGuide: "1. 初始配置需要理解 spec 文件格式，非技术用户需花 15 分钟学习。
2. 多代理协作时，需显式定义每个代理职责，否则可能产生冲突。
3. 自改进记忆功能依赖频繁提交，建议每天至少使用一次 'vibe remember'。
4. 项目依赖 Node.js 18+ 和 git，确保环境已正确安装。
5. 对于大型代码库，首次索引可能较慢，建议提前运行 'vibe init' 预热。"
targetAudience: ["独立开发者", "创业者", "产品经理", "技术负责人"]
useCases: ["快速搭建 MVP 并保持代码质量", "多人协作的 AI 辅助开发项目", "长期维护的复杂项目避免上下文丢失", "从零开始按照规范文档生成完整功能"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Your AI forgets. This remembers. Spec-driven coding harness for vibecoders, product owners, CEOs and real builders — self-improving context memory, 12 agents, 32 skills. Kills context rot, ships features, not spaghetti. Claude Code & Codex. Any stack. 30 seconds

> GitHub: [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | ⭐ 699 | JavaScript

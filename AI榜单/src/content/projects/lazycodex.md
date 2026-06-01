---
title: "懒人代码助手"
description: "Codex 的智能代理编排工具"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/code-yeongyu/lazycodex"
githubStars: 260
githubOwner: "code-yeongyu"
githubRepo: "lazycodex"
category: "agent-framework"
tags: ["ai-agents", "cli", "claude", "orchestration"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "LazyCodex 是一款基于 Claude Code 的代理编排工具，通过一行命令安装后即可在复杂代码库中自动规划、执行和验证任务。适合需要快速构建和迭代项目的开发者，尤其适合独立开发者和技术负责人。"
vibeCodingPrompt: "在 Claude Code 中运行以下步骤：
1. 执行 npx lazycodex-ai install --no-tui --codex-autonomous 安装 LazyCodex
2. 使用 $ulw-plan \"构建一个待办事项应用\" 生成计划
3. 使用 $start-work 执行计划直至完成
4. 如需迭代，使用 $ulw-loop \"添加用户认证功能\" 自动完成"
pitfallGuide: "1. 安装时需确保网络畅通，npx 可能因环境问题失败
2. 自主模式迭代上限 500 次，复杂任务可能超限
3. 计划文件存储在 plans/ 目录，需注意 Git 忽略
4. 依赖 Claude Code 环境，需提前配置好 API 密钥
5. 高度自动化可能导致代码结构不符合预期，建议分步检查"
targetAudience: ["独立开发者", "技术负责人", "创业者"]
useCases: ["快速原型开发", "复杂代码库重构", "自动化代码审查与测试", "多步骤任务编排"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。LazyCodex: Codex for no-brainers. You don't need to think. Just prompt with ultrawork.

> GitHub: [code-yeongyu/lazycodex](https://github.com/code-yeongyu/lazycodex) | ⭐ 260 | TypeScript

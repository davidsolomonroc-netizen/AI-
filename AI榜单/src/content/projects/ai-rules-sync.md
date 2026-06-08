---
title: "AI规则同步器"
description: "一键同步多种AI编码代理规则文件"
publishDate: 2026-06-08
featured: false
githubUrl: "https://github.com/PanisHandsome/ai-rules-sync"
githubStars: 116
githubOwner: "PanisHandsome"
githubRepo: "ai-rules-sync"
category: "dev-tools"
tags: ["cli", "ai-coding-agent", "rules-sync", "developer-tools"]
editorialScore: 4
deploymentRating: 5
vibeCodingRating: 4
commercialSummary: "这个工具解决了多AI工具规则文件不一致的痛点。任何使用Claude、Cursor、Copilot等编码助手的开发者，都可以通过一行命令将AGENTS.md同步到所有平台格式，避免重复维护。"
vibeCodingPrompt: "1. 运行 `npx @panishandsome/agentsync setup` 初始化项目规则同步
2. 编辑生成的 AGENTS.md 作为单一事实来源
3. 运行 `agentsync sync` 将规则同步到 .cursorrules、CLAUDE.md 等文件
4. 提交代码时自动触发同步（已配置pre-commit钩子）
5. 如需自定义映射，修改 agentsync.json 配置文件"
pitfallGuide: "1. 确保项目根目录有package.json或.git，否则setup可能失败
2. 如果使用--auto模式，pre-commit钩子会接受任何规则文件的编辑，可能覆盖AGENTS.md
3. 手动编辑非AGENTS.md文件后，下次同步会被覆盖，建议只编辑AGENTS.md
4. 浏览器版playground不支持文件系统写入，仅用于预览转换结果"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["多AI工具规则统一管理", "新项目快速搭建AI编码规则", "团队协作时保持规则一致性", "从零开始生成AGENTS.md规范"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Keep one source of truth for your AI coding-agent rules. Convert and sync between AGENTS.md, CLAUDE.md, .cursorrules, Copilot, Windsurf, Cline, Aider & Gemini — or scaffold a fresh AGENTS.md. Zero dependencies.

> GitHub: [PanisHandsome/ai-rules-sync](https://github.com/PanisHandsome/ai-rules-sync) | ⭐ 116 | JavaScript

---
title: "交接 Skill：AI 上下文无缝交接工具"
description: "跨模型跨设备交接 AI 任务上下文，换窗不失忆"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/Jordanwei1/jiaojie-skill"
githubStars: 103
githubOwner: "Jordanwei1"
githubRepo: "jiaojie-skill"
category: "workflow-automation"
tags: ["agent-skills", "context-handoff", "claude-code", "multi-agent"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个让 AI 助手在切换窗口、模型或设备时保留完整工作记忆的开源工具。它解决多步骤任务中断后需从头解释的痛点，适合需要跨平台协作的开发者、AI 重度用户和远程团队。"
vibeCodingPrompt: "1. 在 Claude Code 中安装 jiaojie-skill（遵循 README 中的安装步骤）。\n2. 开启一个多步骤编程任务（如修复 webhook 幂等性问题），进行几轮对话。\n3. 说“交接一下”，指定目标模型或设备，并选择是否打包必需文件。\n4. 在另一窗口或设备启动新 AI 会话，输入交接命令或提供交接文件。\n5. 新 AI 自动读取交接内容，从上次停止处继续，无需重新解释背景。"
pitfallGuide: "1. 交接前确保所有依赖文件已保存，否则需手动指定打包。\n2. 不同 AI 模型可能不完全支持所有交接字段，需检查兼容矩阵。\n3. 交接文件可能包含敏感信息，注意传输安全。\n4. 交接后需验证新 AI 是否正确理解上下文，必要时手动补充。\n5. 跨语言交接时，确保目标 AI 支持该语言或使用翻译功能。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI 研究者"]
useCases: ["切换 AI 模型时保留任务进度", "多设备间无缝继续开发工作", "团队协作时共享 AI 工作上下文", "长时间任务中断后快速恢复"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。交接 Skill（Jiaojie）：跨窗口、跨模型、跨设备、跨语言的 AI 上下文交接工具。换窗口，不失忆；换模型，不重来。Open-source AI context handoff.

> GitHub: [Jordanwei1/jiaojie-skill](https://github.com/Jordanwei1/jiaojie-skill) | ⭐ 103 | Python

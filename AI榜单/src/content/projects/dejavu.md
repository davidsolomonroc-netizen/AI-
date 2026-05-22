---
title: "Deja Vu 本地优先AI记忆"
description: "跨工具持久化AI记忆，隐私安全"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/JSingletonAI/dejavu"
githubStars: 63
githubOwner: "JSingletonAI"
githubRepo: "dejavu"
category: "agent-framework"
tags: ["memory", "local-first", "mcp", "privacy"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Deja Vu 解决AI工具会话记忆丢失问题，让用户偏好和上下文在不同AI助手间自动共享，无需云存储或账户。适合需要一致AI体验的个人开发者、知识工作者和AI代理构建者。"
vibeCodingPrompt: "在Claude Code中，先运行`pip install dejavu-memory`和`dejavu init`初始化本地记忆库。然后设置环境变量`VENICE_API_KEY`。使用`dejavu add \"用户偏好\"`添加记忆，用`dejavu search \"查询\"`检索。在Python脚本中导入`from dejavu import Memory`，实例化`Memory()`后调用`add()`和`search()`方法，将记忆集成到你的AI代理工作流中。"
pitfallGuide: "1. 必须设置VENICE_API_KEY环境变量才能使用记忆提取功能。\n2. 记忆存储在本地~/.dejavu目录，备份该目录可迁移记忆。\n3. 目前仅支持单用户模式，多用户需自行实现user_id隔离。\n4. SQLite数据库需手动维护，大量记忆可能影响性能。\n5. 依赖Venice API，API不可用时部分功能会受限。"
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Memory that follows you across every AI tool. No cloud storage. No account required. Set it up once, use it everywhere.

> GitHub: [JSingletonAI/dejavu](https://github.com/JSingletonAI/dejavu) | ⭐ 63 | Python

---
title: "Recall - Claude Code 持久记忆插件"
description: "为 Claude Code 提供本地离线持久记忆"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/raiyanyahya/recall"
githubStars: 296
githubOwner: "raiyanyahya"
githubRepo: "recall"
category: "dev-tools"
tags: ["claude-code", "memory", "offline", "local-first"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Recall 解决 Claude Code 每次会话冷启动问题，自动记录并压缩会话为摘要，让你无需重复解释项目背景。适合订阅 Claude Code 的开发者，完全本地运行，不消耗 API Token，保护隐私。"
vibeCodingPrompt: "1. 在项目根目录运行 `pip install recall` 或克隆仓库并 `pip install -e .`。\n2. 运行 `recall init` 初始化，会在当前目录生成 `.recall` 文件夹。\n3. 每次使用 Claude Code 前，运行 `recall start` 启动会话追踪。\n4. 在 Claude Code 中引用 `context.md` 文件，该文件包含项目历史摘要。\n5. 会话结束后运行 `recall save` 保存记录并更新摘要。\n6. 可选：配置 `.recall/config.toml` 调整摘要长度和存储策略。"
pitfallGuide: "1. 确保 Claude Code 版本与插件兼容，旧版本可能不支持某些功能。\n2. 不要同时运行多个 Recall 实例，可能导致摘要冲突。\n3. 摘要基于 TextRank 算法，对高度专业或非结构化文本效果有限。\n4. 删除 `.recall` 文件夹会丢失所有历史记忆，建议定期备份。\n5. 如果项目文件过大，建议手动清理无用会话记录以避免性能下降。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者", "创业者"]
useCases: ["长期项目开发中避免重复向 Claude Code 解释项目背景", "多人协作时共享项目上下文摘要", "个人知识管理，记录与 AI 助手交互的关键信息"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Stop wasting tokens and re-explaining your project every session. Recall gives Claude Code durable memory — entirely offline.

> GitHub: [raiyanyahya/recall](https://github.com/raiyanyahya/recall) | ⭐ 296 | Python

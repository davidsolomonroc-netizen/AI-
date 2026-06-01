---
title: "文件树技能"
description: "为Claude Code维护FILETREE.md"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/nekocode/filetree-skill"
githubStars: 130
githubOwner: "nekocode"
githubRepo: "filetree-skill"
category: "agent-framework"
tags: ["filetree", "claude-code", "plugin", "ai-agent"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该插件自动生成并维护项目文件树摘要（FILETREE.md），让AI助手快速理解代码库结构，避免每次会话重复探索。适合使用Claude Code进行代码开发的团队，尤其是需要跨会话共享代码布局认知的开发者。"
vibeCodingPrompt: "在Claude Code中，先通过`/plugin marketplace add nekocode/filetree-skill`安装插件，然后运行`/filetree:init`生成初始文件树。每次修改代码后运行`/filetree:update`同步变更。将FILETREE.md引用添加到CLAUDE.md中，以便每次会话自动加载。"
pitfallGuide: "FILETREE.md需要手动审查差异后再提交，不要直接自动提交\n哈希变更可能因非语义修改触发，需确认是否真正需要更新描述\n插件依赖git进行变更检测，确保项目已初始化git仓库\n首次生成时可能覆盖已有FILETREE.md，需确认不覆盖"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["跨会话代码库布局记忆共享", "新成员快速了解项目结构", "AI辅助代码审查时提供上下文"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A Claude Code plugin that maintains `FILETREE.md`.

> GitHub: [nekocode/filetree-skill](https://github.com/nekocode/filetree-skill) | ⭐ 130 | Python

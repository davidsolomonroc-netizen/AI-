---
title: "AI 输出摘要技能库"
description: "为 AI 输出提供解释与总结的 Claude 技能包"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/isas1/skills"
githubStars: 121
githubOwner: "isas1"
githubRepo: "skills"
category: "workflow-automation"
tags: ["summarization", "claude-skills", "html-report", "accessibility"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 5
commercialSummary: "这个项目为 AI 助手提供了一套即插即用的技能，能把复杂的技术内容一键转成通俗解释或一份可直接查看和分享的网页报告。特别适合需要频繁向非技术同事、客户或团队汇报 AI 输出结果的人使用，无需任何编程环境即可运行。"
vibeCodingPrompt: "1. 在 Claude Code 中创建一个新项目目录，克隆仓库 isas1/skills。
2. 阅读 skills/eli5-succinct/SKILL.md 和 skills/summary/SKILL.md，理解两个技能的路由逻辑。
3. 将 skills 目录整体复制到你的 Claude Code 自定义技能目录（通常是 ~/.claude/skills 或项目根目录的 .claude/skills）。
4. 在 Claude Code 中打开一个包含复杂代码或文档的项目，输入指令：'eli5 succinct on <某段代码>'，验证聊天内简短解释是否生效。
5. 再输入：'summary, make it ADHD friendly'，检查是否生成一个独立的 HTML 页面。
6. 打开生成的 HTML 文件，确认无障碍模式（颜色编码、重复状态、无动画）是否生效。
7. 如需定制，编辑 skills/summary/modes/ 下的 accessible.md、artistic.md 或 animated.md 来调整输出样式。"
pitfallGuide: "需要 Claude Code 或兼容技能系统的 AI 编程助手才能运行，不是独立应用
默认生成的 HTML 页面为单文件，但样式和动画依赖内联代码，修改时注意不要破坏自包含性
无障碍模式与艺术模式可能冲突，项目规定无障碍优先，定制时需注意优先级
技能路由依赖用户措辞（如 'eli5'、'summary'），模糊指令可能触发错误技能
示例页面中的截图和 HTML 文件在 docs 目录下，不要误删以免丢失参考"
targetAudience: ["独立开发者", "产品经理", "内容创作者", "技术负责人"]
useCases: ["向非技术同事快速解释一段复杂代码或技术方案", "为 AI 生成的分析结果自动生成一份可分享的 HTML 摘要页面", "在 Claude Code 中一键将冗长文档转成无障碍友好的阅读页面", "为团队会议准备简洁的 AI 输出总结，支持艺术化或动画展示模式"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Skills for explaining and summarising AI output: eli5-succinct, simple-summary, summary

> GitHub: [isas1/skills](https://github.com/isas1/skills) | ⭐ 121 | 多种语言

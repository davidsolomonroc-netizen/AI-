---
title: "Sepia：叙事架构级去AI化写作技能"
description: "修复AI写作叙事架构，提升文本真实感与专业度。"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/Nanako0129/sepia"
githubStars: 1030
githubOwner: "Nanako0129"
githubRepo: "sepia"
category: "other"
tags: ["ai-writing", "agent-skills", "claude-code", "humanizer"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Sepia是一款基于学术研究的写作技能包，通过修复AI生成文本中的叙事结构缺陷，让小说更真实、专业文档更得体。适合小说作者、内容创作者、技术团队等需要去AI化写作的用户。"
vibeCodingPrompt: "在Claude Code中，首先安装该技能（将SKILL.md放入skills目录），然后对一段AI生成的文本运行：`sepia review <文件>`进行诊断，再根据诊断结果运行`sepia refactor <文件>`进行最小化修改，或`sepia recreate <文件>`进行全量重写。可自定义风格参数（如：正式度、创意度）以适配不同场景。"
pitfallGuide: "1. 技能需正确安装到Agent Skills目录，否则命令无法识别。\n2. review仅诊断，需结合refactor或recreate执行修改。\n3. 专业文档与小说使用不同规则，请确保选择正确的操作模式。\n4. 基于2026年arXiv论文，模型指纹可能随时间变化，需定期更新。\n5. 不要期望完全消除AI痕迹，目标是降低可检测性。"
targetAudience: ["内容创作者", "独立开发者", "技术负责人", "AI研究者"]
useCases: ["小说章节去AI化改写", "技术文章风格调整", "发布说明与PR回复润色", "AI生成内容的真实性提升"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。De-AI writing skill for Claude Code, Codex, Grok Build, and Antigravity — narrative-architecture repair for fiction, venue-matched rules for professional prose. Based on StoryScope (arXiv:2604.03136).

> GitHub: [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | ⭐ 1030 | 多种语言

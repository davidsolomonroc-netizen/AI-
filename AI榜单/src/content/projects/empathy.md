---
title: "共情技能：让AI代理更懂人心"
description: "提升AI代理与人类交流的情商与礼貌"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/danielroe/empathy"
githubStars: 61
githubOwner: "danielroe"
githubRepo: "empathy"
category: "agent-framework"
tags: ["empathy", "agent-skills", "communication", "kindness"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目为AI代理提供一套行为准则和提示，帮助它们在开源社区或任何与人类交互的场景中，避免冷漠或冒犯性的表达，增强沟通的温暖和尊重。适合需要大量AI与用户互动的团队，或希望AI更人性化的开发者。"
vibeCodingPrompt: "在Claude Code中，你可以通过以下步骤集成此技能：
1. 克隆仓库到技能目录：`git clone https://github.com/danielroe/empathy ~/.claude/skills/empathy`
2. 在需要AI生成回复或评论时，在Prompt中引用该技能的指导原则，例如：'请参考empathy技能，确保回复语气温和、简洁，并明确告知用户你是AI。'
3. 在代码审查或自动生成PR描述前，要求Claude先检查是否满足'如何让人感觉良好'的条件。
4. 可以在CI/CD流程中，用此技能作为质量门禁，防止AI生成冷漠或误导性的文本。"
pitfallGuide: "模型可能不总是加载技能文件，需要显式调用或配置。\n技能文本由LLM生成，可能包含偏见，需人工审核。\n不能完全替代人类判断，关键交互仍需人工介入。\n安装路径因工具而异，需确认正确目录。\n过度强调礼貌可能导致回复冗长，需平衡简洁性。"
targetAudience: ["独立开发者", "技术负责人", "产品经理", "企业团队"]
useCases: ["自动回复GitHub issue和PR时保持礼貌和尊重", "AI客服对话中增强同理心和清晰度", "团队内部AI助手生成更人性化的提醒或通知", "开源项目维护中减少AI评论带来的负面影响"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A skill that helps AI agents talk to humans.

> GitHub: [danielroe/empathy](https://github.com/danielroe/empathy) | ⭐ 61 | Shell

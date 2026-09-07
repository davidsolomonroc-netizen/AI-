---
title: "思维反转地图生成器"
description: "将头脑风暴转化为交互式思维地图的Claude技能"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/ara-mkr/Wonder-Pill"
githubStars: 117
githubOwner: "ara-mkr"
githubRepo: "Wonder-Pill"
category: "dev-tools"
tags: ["claude-skill", "mind-map", "brainstorming", "creativity"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Wonder Pill 是一个 Claude 技能，旨在打破传统头脑风暴中寻求“正确答案”的惯性，通过生成反转假设和挑衅性问题，帮助用户探索思维的盲区。它适合需要激发创意、挑战既有假设的产品经理、创新团队和内容创作者，产出可视化的思维导图而非标准答案。"
vibeCodingPrompt: "在 Claude Code 中安装此技能后，可以这样使用：
1. 在项目根目录创建 `my-idea.md` 文件，写入你的核心问题，例如“如何提高用户留存率”。
2. 在 Claude Code 中运行命令：`claude -p \"使用 Wonder Pill 技能分析 my-idea.md 中的问题，生成交互式思维地图，并保存为 HTML 文件。\"`。
3. 技能会输出一个包含反转假设和分支的 HTML 思维地图，你可以用浏览器打开，并拖拽探索各个想法之间的关系。
4. 如果需要调整方向，可以继续对话，要求 Claude 基于某个分支深入或重新生成。"
pitfallGuide: "请勿期望输出为直接解决方案，它本质是激发思考的工具。\n地图中的部分反转假设可能看似荒谬，这是设计使然，请结合判断而非全盘接受。\n需要 Claude Desktop 或 Claude Code 环境，确保已正确安装技能文件。\n生成的思维地图为 HTML 文件，需浏览器查看，不支持在终端内交互。\n若用于商业决策，建议结合其他分析方法，避免仅依赖此工具。"
targetAudience: ["产品经理", "创业者", "内容创作者", "AI 研究者"]
useCases: ["产品创新头脑风暴，挑战产品假设", "创意写作前的思维发散，寻找非主流叙事角度", "团队工作坊中引导讨论，打破思维定势", "个人反思与决策分析，探索问题的新维度"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A Claude skill that turns brainstorming into an interactive mind map of inverted assumptions — no answers, no ranking, just provocations.

> GitHub: [ara-mkr/Wonder-Pill](https://github.com/ara-mkr/Wonder-Pill) | ⭐ 117 | 多种语言

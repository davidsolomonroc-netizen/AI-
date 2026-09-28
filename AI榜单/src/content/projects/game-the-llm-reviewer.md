---
title: "LLM审稿人攻略器"
description: "用措辞改写让LLM审稿人对同一篇论文打更高分"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer"
githubStars: 194
githubOwner: "Michael-Jiahao-Zhang"
githubRepo: "game-the-llm-reviewer"
category: "workflow-automation"
tags: ["llm-reviewer", "academic-writing", "agent-skills", "prompt-engineering"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "学术论文投稿前，LLM审稿系统可能因为措辞偏见给论文打低分。这个项目把相关研究成果变成一套AI可直接调用的改写规则，在不改变科学含义的前提下优化表达，适合科研人员和论文写作者在投稿前做最后一轮防御性润色。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer，进入目录。
2. 阅读 skills/game-the-llm-reviewer/ 下的 skill 定义和 references/strategies.md，理解改写策略。
3. 在 Claude Code 中把该 skill 目录加入项目上下文，或将 skill 内容粘贴为系统提示。
4. 准备你的论文 Markdown 或纯文本文件，放入工作目录。
5. 让 Claude 逐段读取论文，对照 strategies.md 识别可能触发 LLM 审稿偏见的表达，并给出保留原意的改写建议。
6. 让 Claude 输出改写前后对照表，人工确认科学含义未被改变。
7. 将确认后的文本合并回原文件，生成最终投稿版本。"
pitfallGuide: "改写必须严格保留科学含义，不能为了讨好审稿人而夸大结论或隐藏局限。\n不同 LLM 审稿系统的偏好可能不同，策略文档基于特定研究，效果不保证跨模型通用。\n不要用该工具替代实质性的方法改进和证据补充，它只是投稿前的语言润色。\n使用前确认目标期刊或会议是否允许 AI 辅助润色，避免违反学术规范。\n建议保留改写前后版本，方便对比和回溯。"
targetAudience: ["AI 研究者", "内容创作者", "独立开发者"]
useCases: ["论文投稿前的最后一轮语言润色", "应对使用 LLM 辅助审稿的期刊或会议", "将审稿偏好研究转化为可复用的 agent 技能", "非英语母语研究者的表达优化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Defend sound research against LLM reviewer bias through meaning-preserving rewrites.

> GitHub: [Michael-Jiahao-Zhang/game-the-llm-reviewer](https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer) | ⭐ 194 | 多种语言

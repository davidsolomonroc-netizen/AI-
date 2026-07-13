---
title: "歸藏的材质插画 Skill"
description: "为 AI Agent 生成带中文标签的材质插画"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/op7418/guizang-material-illustration"
githubStars: 599
githubOwner: "op7418"
githubRepo: "guizang-material-illustration"
category: "agent-framework"
tags: ["illustration", "chart-beautify", "chinese", "agent-skill"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一款专为 Claude Code/Codex 等 AI Agent 设计的配图 Skill，可自动将文章、笔记、图表截图、产品概念等转化为带中文标签的材质插画，解决社交媒体卡片、PPT、文档中“中心配图”的需求。适合需要快速生成高质量解释性插画的内容创作者、产品经理和营销团队。"
vibeCodingPrompt: "在 Claude Code 中执行以下步骤：
1. 运行 npx skills add https://github.com/op7418/guizang-material-illustration --skill guizang-material-illustration 安装该 Skill。
2. 安装完成后，对 Claude 说：“用歸藏的材质插画 skill，帮我把这段产品说明做成一张带中文标签的机制图。”
3. 提供你的文本、数据或截图，Agent 会自动生成插画并返回。
4. 如需美化图表，直接说：“帮我把这张柱状图重新画成歸藏材质风格，数据和坐标不要改。”"
pitfallGuide: "1. 确保 AI Agent 有 shell 权限来执行 npx 命令\n2. 安装后需确认 SKILL.md、assets/、references/ 目录存在\n3. 图片生成可能受限于 Agent 的绘图能力，建议配合支持图像生成的模型使用\n4. 中文标签生成效果依赖 Agent 的语言理解，复杂概念需提供清晰描述\n5. 该 Skill 是社交卡片 Skill 的配套，单独使用无法生成完整卡片布局"
targetAudience: ["内容创作者", "产品经理", "营销团队", "数据分析师"]
useCases: ["将抽象概念、流程、机制生成带标签的解释图", "美化图表截图，重新生成更适合传播的材质化图表", "为冷门概念、品牌、模型查找参考信息并生成统一风格插画"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。归藏的材质插画 skill：生成带字解释图、图表美化和参考辅助配图。

> GitHub: [op7418/guizang-material-illustration](https://github.com/op7418/guizang-material-illustration) | ⭐ 599 | 多种语言

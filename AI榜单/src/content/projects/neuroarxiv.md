---
title: "神经预印本——杜绝从零编码的AI架构设计工具"
description: "让Claude在架构设计前先查阅arXiv真实文献，避免重复造轮子。"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/UditAkhourii/neuroarxiv"
githubStars: 134
githubOwner: "UditAkhourii"
githubRepo: "neuroarxiv"
category: "workflow-automation"
tags: ["arxiv", "LLM", "reasoning", "workflow"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "NeuroArxiv是一个帮助AI编程助手（如Claude）在动手设计新架构前，自动检索并阅读arXiv上相关学术论文的Skill。它通过隔离阅读、收敛推荐的方式，确保AI的设计基于真实先例，而非凭空想象。适合需要高质量架构设计的技术团队和独立开发者，能显著降低因忽略已有研究成果而导致的返工成本。"
vibeCodingPrompt: "1. 安装NeuroArxiv Skill到Claude Code环境（遵循项目README）。
2. 在需要设计新架构或算法时，在Claude Code中明确指示：\"使用NeuroArxiv技能，查询与[你的具体问题]相关的arXiv论文，并给出基于文献的设计建议。\"
3. Claude将自动调用NeuroArxiv的API，获取相关论文，隔离阅读后收敛推荐。
4. 根据推荐结果，让Claude生成具体实现方案，并标注引用的论文。
5. 若需调整，可要求Claude重新检索或深入阅读特定论文。"
pitfallGuide: "确保网络能正常访问arXiv API，否则该技能无法工作。
该工具适合架构设计阶段，不适用于简单代码片段生成。
推荐结果基于现有文献，可能不包含最新未发表的研究，需结合其他信息渠道。
非技术用户可能需要一些命令行基础来安装和配置该Skill。
对于高度创新且无先例的场景，该工具可能无法提供有效参考。"
targetAudience: ["AI研究者", "技术负责人", "独立开发者", "企业团队"]
useCases: ["设计新算法或系统架构前进行文献调研", "验证AI生成设计方案的学术依据", "在快速原型开发中避免重复造轮子", "为技术选型提供基于论文的决策支持"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A skill to kill from-scratch coding — Claude checks real arXiv prior art before it designs a new architecture.

> GitHub: [UditAkhourii/neuroarxiv](https://github.com/UditAkhourii/neuroarxiv) | ⭐ 134 | TypeScript

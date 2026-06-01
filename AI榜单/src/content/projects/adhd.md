---
title: "ADHD：编码代理的并行发散思维"
description: "通过并行思维树提升AI代理创造力"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/UditAkhourii/adhd"
githubStars: 682
githubOwner: "UditAkhourii"
githubRepo: "adhd"
category: "agent-framework"
tags: ["tree-of-thought", "divergent-thinking", "claude", "ai-agents"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "ADHD是一个编码代理技能，通过并行发散思维和剪枝机制解决AI推理中的过早收敛问题。适合需要提升创意和跨学科工作质量的开发者，尤其适用于设计决策、模糊调试和头脑风暴场景。"
vibeCodingPrompt: "在Claude Code中，首先安装adhd-agent包（npm install adhd-agent），然后导入ADHD类，创建一个ADHD实例，调用generateIdeas方法传入问题描述（如“为我的API设计一个更好的错误处理方案”），ADHD会并行生成多个认知框架下的思路并返回评分和深度分析结果。"
pitfallGuide: "确保Node.js版本>=18，否则安装失败\n使用前需配置Claude API密钥（环境变量ANTHROPIC_API_KEY）\n并行分支数不宜过大，建议3-5个，避免API调用超限\n结果需人工筛选，ADHD不保证所有输出都实用\n不支持流式输出，长任务可能延迟"
targetAudience: ["独立开发者", "AI研究者", "技术负责人", "创业者"]
useCases: ["设计决策与API表面设计", "模糊调试与问题诊断", "创意命名与头脑风暴", "跨学科策略制定"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。ADHD — a skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK. Fans out parallel divergent thoughts under different cognitive frames, scores, prunes traps, deepens the survivors. The no-brainer skill for creative and interdisciplinary work.

> GitHub: [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | ⭐ 682 | TypeScript

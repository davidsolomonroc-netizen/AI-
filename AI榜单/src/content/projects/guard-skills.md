---
title: "AI编码智能体质量门禁"
description: "捕捉AI生成代码缺陷的二次审查技能"
publishDate: 2026-06-08
featured: false
githubUrl: "https://github.com/amElnagdy/guard-skills"
githubStars: 427
githubOwner: "amElnagdy"
githubRepo: "guard-skills"
category: "code-generation"
tags: ["agent-skills", "code-review", "quality-gates", "ai-agents"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一套为AI编码智能体设计的质量门禁技能，能够自动审查AI生成的代码、测试和文档，捕捉常见失败模式。适合使用Claude Code、Codex、Cursor等工具的开发者，确保AI产出在提交前经过二次把关。"
vibeCodingPrompt: "在Claude Code中，先运行'npx skills add amElnagdy/guard-skills --global'安装所有技能。然后在你让AI完成编码任务后，输入：'Use $clean-code-guard on the diff you just produced.' 或者针对测试：'Use $test-guard on the tests you just wrote.' 也可以组合使用：先让AI写代码，然后依次执行'Use $clean-code-guard'和'Use $test-guard'对输出进行审查。"
pitfallGuide: "1. 这些技能是反应式审查工具，不应替代AI初次编码时的思考，最佳实践是先让AI自由生成再审查。\n2. 安装需要Node环境和npx工具，非技术用户可能需先配置环境。\n3. 每个guard聚焦特定领域（如WooCommerce），选择错误的guard可能导致无效审查。\n4. 技能依赖于skills.sh CLI，需确保网络可访问该服务。\n5. 对于复杂项目，建议按顺序使用多个guard，不要只依赖单一审查。"
targetAudience: ["独立开发者", "企业团队", "技术负责人"]
useCases: ["AI生成代码提交前的自动化质量审查", "团队协作中确保AI产出符合编码规范", "持续集成流程中嵌入AI代码审查环节"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Guard skills for coding agents, quality gates that catch AI-generated failure modes in code, tests, and docs

> GitHub: [amElnagdy/guard-skills](https://github.com/amElnagdy/guard-skills) | ⭐ 427 | 多种语言

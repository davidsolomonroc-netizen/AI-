---
title: "先交付后记账：AI 代理防跑偏指南"
description: "防止 AI 编码代理沉迷内部流程，先交付再验证。"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/Vuk97/forward-implementation-first"
githubStars: 143
githubOwner: "Vuk97"
githubRepo: "forward-implementation-first"
category: "workflow-automation"
tags: ["agent-skills", "prompt-engineering", "claude-code", "codex"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个技能文件能阻止 AI 编码代理把时间浪费在生成哈希、锁文件、收据等内部元数据上，确保它专注于真正交付产品功能。适合使用 Claude Code、Codex 等 AI 编程工具的开发团队，尤其是处理复杂多阶段流水线项目。"
vibeCodingPrompt: "在 Claude Code 中，将本项目的 SKILL.md 文件内容复制到项目的 .claude/skills/ 目录下，或直接作为系统提示的一部分。然后在对话中明确要求：'请遵循 forward-implementation-first 技能，在开始任何任务前，先判断该操作是否直接服务于用户请求的最终交付物。如果只是内部簿记（如更新哈希、生成收据、维护锁文件），除非用户明确要求，否则禁止执行。优先推进实际功能实现，验证留到最后。' 这样即可让代理自动规避常见的内耗行为。"
pitfallGuide: "1. 该技能是指导性规则，不能完全替代人工审查，仍需监控代理行为。\n2. 对于需要严格审计或合规性的项目，完全禁用簿记可能不适用，需调整规则。\n3. 技能文件需放在正确路径（如 .claude/skills/）才能被代理加载，否则无效。\n4. 不要期望一次设置后永久有效，复杂项目可能需要根据实际情况微调规则。\n5. 该技能不推荐用于纯数据管道或需要严格依赖追踪的场景，否则可能造成产出不一致。"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["优化 AI 编码代理在多阶段流水线中的执行效率", "减少代理在内部元数据维护上的时间浪费", "提升长期运行代理任务的交付速度"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Stop your coding agent from stalling real work on self-invented bookkeeping - receipts, hashes, locks, certification rituals. Ship first, then verify. Skill for Claude Code, Codex, and other agents.

> GitHub: [Vuk97/forward-implementation-first](https://github.com/Vuk97/forward-implementation-first) | ⭐ 143 | Shell

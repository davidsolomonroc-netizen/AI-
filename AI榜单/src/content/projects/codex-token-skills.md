---
title: "Codex Token 节省器"
description: "降低 DeepSeek V4 Pro token 消耗 60-80%"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/lokikill123/codex-token-skills"
githubStars: 78
githubOwner: "lokikill123"
githubRepo: "codex-token-skills"
category: "code-generation"
tags: ["token-optimization", "codex-cli", "deepseek", "cache"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目通过冻结系统提示词和 skill 文件，利用前缀缓存机制大幅减少 DeepSeek V4 Pro 的 token 消耗，同时提供持久记忆功能保持跨对话一致性。适合高频使用 Codex CLI 的开发者，特别是需要控制 AI 调用成本的企业和个人。"
vibeCodingPrompt: "在 Claude Code 中使用此项目：
1. 克隆仓库并复制 skill 文件到 ~/.codex/skills/ 目录
2. 在 ~/.codex/AGENTS.md 中配置激活 token-saver 和 memory skill
3. 启动 Codex CLI 并确认 skill 已加载
4. 对于简单任务（如修 bug），直接输入指令，token-saver 会自动禁止 preamble 和计划
5. 对于复杂任务（如架构设计），允许简短交流但控制输出长度
6. 跨对话时，memory skill 从 MEMORY.md 恢复上下文，确保一致性"
pitfallGuide: "1. Skill 文件写好后不要修改，否则前缀缓存失效
2. 动态项目内容要放 AGENTS.md 而非 skill 文件
3. 极简输出模式下可能缺失调试信息，复杂问题需手动允许详细输出
4. 首次安装后需重启 Codex CLI 才能生效
5. memory 文件需定期清理，避免积累过多无用记忆"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者"]
useCases: ["高频 Codex CLI 用户降低 token 成本", "需要跨对话保持项目上下文的开发场景", "对 DeepSeek V4 Pro 调用成本敏感的企业团队"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。⚡ Cut 60-80% token cost for DeepSeek V4 Pro on Codex CLI. token-saver + memory skills with prefix-cache optimization.

> GitHub: [lokikill123/codex-token-skills](https://github.com/lokikill123/codex-token-skills) | ⭐ 78 | 多种语言

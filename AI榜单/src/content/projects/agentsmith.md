---
title: "通用AI代理操作系统"
description: "一套可移植的代理规则与工具核心"
publishDate: 2026-07-20
featured: false
githubUrl: "https://github.com/PromptPartner/agentsmith"
githubStars: 309
githubOwner: "PromptPartner"
githubRepo: "agentsmith"
category: "agent-framework"
tags: ["agent-harness", "claude-code", "prompt-engineering", "vibe-coding"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "AgentSmith 为 Claude Code 等 AI 代理提供了一套通用、可复用的规则、工具和记忆系统。它解决了代理在复杂项目中缺乏一致行为规范的问题，适合需要让 AI 代理稳定执行软件开发、运维、营销等不同任务的团队和个人。"
vibeCodingPrompt: "1. 克隆项目到本地：git clone https://github.com/PromptPartner/agentsmith
2. 进入项目目录，运行 ./setup.sh 按向导选择工作类型（如 software、devops）
3. 向导会自动生成 CLAUDE.md 并提示下一步操作
4. 打开你的项目，将生成的 CLAUDE.md 放入项目根目录
5. 启动 Claude Code 并告诉它：'请读取 CLAUDE.md 并按其中规则开始工作'"
pitfallGuide: "1. 项目依赖 Shell 环境，Windows 用户需使用 WSL 或 Git Bash。\n2. setup.sh 向导生成的命令需确认后才能执行，不要跳过确认步骤。\n3. 每次切换工作类型需重新运行 setup.sh 并更新 CLAUDE.md。\n4. 如果项目已有 CLAUDE.md，会被覆盖，建议先备份。\n5. 代理行为高度依赖 prompt 规则，修改规则后需重启会话才能生效。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI研究者"]
useCases: ["为 Claude Code 提供统一的软件开发规范", "在 DevOps 任务中自动执行部署脚本", "辅助进行数据分析和报告生成", "管理多个 AI 代理项目的通用规则集"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Universal, model-agnostic operating harness for AI agents (Claude, Codex, Gemini, …) — a lean core + work-type profiles assembled by one setup script.

> GitHub: [PromptPartner/agentsmith](https://github.com/PromptPartner/agentsmith) | ⭐ 309 | Shell

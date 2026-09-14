---
title: "AI 项目记忆技能包"
description: "为 Codex/Claude Code 提供有界项目记忆系统"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/tudoumashu/ai-memory-skillpack"
githubStars: 67
githubOwner: "tudoumashu"
githubRepo: "ai-memory-skillpack"
category: "dev-tools"
tags: ["agent-memory", "claude-code", "codex", "skills"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个给 AI 编程助手（Codex CLI、Claude Code）加装\"项目记忆\"的工具包，让 AI 在每次新会话时不必重新通读整个代码库，而是读取一份精简、有上限、可追溯的项目摘要（热点快照、代码地图、避坑清单）。适合需要长期维护同一仓库的独立开发者和工程团队，能显著降低 AI 重复理解项目的 token 成本与出错率。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/tudoumashu/ai-memory-skillpack，进入目录。
2. 在 Codex CLI（或 Claude Code）中打开该项目，输入：\"Read INSTALL.md in this pack and follow it to install the memory system on this machine.\"，让 AI 自行完成安装（无需 GUI）。
3. 安装完成后，在你的目标项目根目录运行安装器生成的初始化命令，生成 docs/ai/ 目录及 HOT 快照、WARM 代码地图、handoff 交接页。
4. 让 AI 读取 docs/ai/ 下的内容，并基于此开始一次代码评审或 bug 修复任务，观察它是否不再全量扫描仓库。
5. 每次会话结束时，指示 AI 更新 handoff 页面（原地替换而非追加），并运行 verifier 校验记忆边界是否越界。
6. 若需回滚，执行安装器提供的卸载命令，所有变更可逆。"
pitfallGuide: "安装依赖 AI 代理执行 INSTALL.md，若模型能力不足可能中途失败，建议用较新的 Codex/Claude Code 版本
\n记忆内容有大小上限，项目过大时需手动裁剪或分模块维护多份快照
\n默认只启用 project-memory 技能，其他技能需手动开启，别期待开箱即用全部功能
\nhandoff 页面是原地替换机制，误删历史信息后只能靠 git 恢复，务必保证 git 提交及时
\n验证器是 fail-closed 设计，配置不完整时会直接拒绝运行，需按提示逐项补全"
targetAudience: ["独立开发者", "技术负责人", "企业团队", "AI 研究者"]
useCases: ["长期维护同一代码仓库时，让 AI 每次会话快速恢复项目上下文", "团队协作中统一 AI 助手的项目理解口径，减少重复解释", "代码评审与故障排查时，让 AI 基于有界记忆而非全量扫描工作", "多会话交接场景下，用一页 handoff 文档替代冗长对话历史"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Bounded project-memory skills for Codex CLI and Claude Code.

> GitHub: [tudoumashu/ai-memory-skillpack](https://github.com/tudoumashu/ai-memory-skillpack) | ⭐ 67 | Python

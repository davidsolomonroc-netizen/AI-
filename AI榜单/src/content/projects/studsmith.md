---
title: "Studsmith"
description: "免费的 Roblox Studio AI 智能体，写 Luau 并自测"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/RapidSailorFreeze/studsmith"
githubStars: 95
githubOwner: "RapidSailorFreeze"
githubRepo: "studsmith"
category: "code-generation"
tags: ["roblox", "ai-agent", "luau", "game-dev"]
editorialScore: 3
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Studsmith 是一个免费的 Windows 应用，让非程序员用自然语言描述需求，就能自动生成 Roblox 游戏的 Luau 脚本、布置场景并自我测试修复。适合 Roblox 独立开发者、游戏设计初学者和想快速验证创意的创作者。"
vibeCodingPrompt: "1. 在 Windows 10/11 上下载并解压 Studsmith 最新发布包，运行 Studsmith.exe。
2. 打开 Roblox Studio 并新建一个 Baseplate 项目，在 Studsmith 设置中连接 Studio（按提示开启本地 HTTP 或 MCP 连接）。
3. 在 Studsmith 中选择模型：可配置本地 Ollama 模型（如 llama3.1）或填入自己的 OpenAI/Anthropic API Key。
4. 在任务输入框用中文描述需求，例如“创建一个收集金币的跑酷关卡，玩家碰到金币加分，掉落重置”。
5. 查看 Studsmith 生成的计划，点击生成代码，在 diff 预览中确认修改后应用到 Studio。
6. 点击 Playtest 让智能体自动运行游戏、读取错误并修复，重复直到可玩。
7. 使用恢复点回滚不满意改动，导出最终 place 文件。"
pitfallGuide: "需要 Windows 10/11 系统，Mac/Linux 用户无法直接运行
首次使用需正确配置 Roblox Studio 连接，否则智能体无法读写场景
本地模型能力有限，复杂逻辑建议使用 API Key 接入更强模型
自动应用代码前务必查看 diff，避免意外覆盖已有脚本
Playtest 循环可能反复修改，建议先小范围测试再扩大任务"
targetAudience: ["独立开发者", "内容创作者", "产品经理"]
useCases: ["快速生成 Roblox 游戏原型", "为现有 Roblox 项目自动修复脚本错误", "非程序员通过自然语言搭建游戏功能", "教学场景中演示 AI 辅助游戏开发"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Free AI agent for Roblox Studio: plans, writes Luau, shows a diff and playtests its own changes. Windows app. 免费的 Roblox Studio AI 智能体。

> GitHub: [RapidSailorFreeze/studsmith](https://github.com/RapidSailorFreeze/studsmith) | ⭐ 95 | 多种语言

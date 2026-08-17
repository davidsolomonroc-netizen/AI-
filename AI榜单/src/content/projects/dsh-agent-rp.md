---
title: "DSH 角色扮演代理"
description: "将 SillyTavern 角色卡迁移至 DSH 并驱动原生角色对话"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/hewzhew/dsh-agent-rp"
githubStars: 143
githubOwner: "hewzhew"
githubRepo: "dsh-agent-rp"
category: "agent-framework"
tags: ["roleplay", "sillytavern", "agent", "dsh"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目让 SillyTavern 的角色卡、世界书和聊天记录能直接用于 DSH 平台，用户无需重建角色即可在原生会话中继续角色扮演。适合角色扮演爱好者、内容创作者以及想要构建沉浸式 AI 角色对话应用的开发者。"
vibeCodingPrompt: "1. 首先安装 DSH 和插件：运行 `npx -p @deepseek-ai/dsh@latest dsh plugin --profile web add github:hewzhew/dsh-agent-rp#main`，然后启动 DSH。\n2. 准备一张 Character Card V2/V3 的 PNG 或 JSON 文件（确保你有权使用）。\n3. 在 DSH 界面中导入角色卡，并设置开场白和 Persona。\n4. 可选：导入 SillyTavern JSONL 聊天记录或世界书，以延续已有剧情。\n5. 开始对话，体验角色扮演。若要调试，切换到调试视图查看实际提示内容。"
pitfallGuide: "确保使用 DSH 的公开版本，不要泄露 NPM Token。\n旧版本插件不会自动迁移，若启动出错需手动备份并移除旧插件目录。\nAndroid 首次安装需编译原生模块，耗时较长。\n世界书正则和 EJS 模板在受限 QuickJS 中运行，避免使用不兼容的 JS 特性。\n不要删除整个 .dsh 目录，否则会丢失会话数据。"
targetAudience: ["独立开发者", "内容创作者", "AI 研究者", "技术负责人"]
useCases: ["将现有 SillyTavern 角色卡迁移到 DSH 并继续角色扮演", "构建带持久记忆和世界书的沉浸式 AI 角色对话应用", "在移动设备（Android）上本地运行角色扮演代理", "测试和调试角色提示与脚本，优化角色行为"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。SillyTavern migration and next-generation Agent RP for DSH

> GitHub: [hewzhew/dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐ 143 | TypeScript

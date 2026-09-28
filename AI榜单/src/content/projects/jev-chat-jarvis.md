---
title: "Jev 聊天助手"
description: "安卓端 AI 聊天副驾，读屏给建议回复"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/jev-chat/jev-chat-jarvis"
githubStars: 6828
githubOwner: "jev-chat"
githubRepo: "jev-chat-jarvis"
category: "workflow-automation"
tags: ["android", "accessibility-service", "chat-assistant", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Jev 聊天助手是一款装在手机上的 AI 对话副驾，能在 QQ、X、飞书等聊天软件中读懂对方消息，实时生成候选回复，你只需一键填入输入框即可发送。它只读屏幕、不修改任何应用，安全非侵入，适合需要高频回复消息的销售、客服、社交达人和普通用户提升聊天效率。"
vibeCodingPrompt: "1. 在 Claude Code 中创建一个新的 Android 项目，使用 Kotlin 和 Jetpack Compose。
2. 添加无障碍服务（AccessibilityService），用于读取 QQ、飞书等应用的聊天界面文本。
3. 集成一个大语言模型 API（如 OpenAI 或国内大模型），将读取到的对话上下文发送给模型，请求生成 3 条候选回复。
4. 在聊天界面悬浮窗中展示候选回复，点击后通过无障碍服务将文本填入输入框。
5. 添加开关和配置页面，允许用户选择启用的应用和模型参数。
6. 打包 APK 并在 Android 11+ 真机上测试，确保只读屏幕、不 hook 应用。"
pitfallGuide: "需要手动开启无障碍服务权限，部分手机可能限制后台运行。
仅支持 Android 11+ ARM64 设备，老旧机型无法使用。
模型 API 需要自行配置密钥，且可能产生费用。
无障碍服务可能被部分应用检测或屏蔽，导致无法读取聊天内容。
建议仅在个人设备上使用，避免隐私泄露风险。"
targetAudience: ["独立开发者", "创业者", "产品经理", "内容创作者"]
useCases: ["销售快速回复客户消息", "社交聊天时获取智能回复建议", "客服人员批量处理咨询", "个人在多个聊天平台间高效沟通"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。装在手机上的对话副驾：在 QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。

> GitHub: [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | ⭐ 6828 | Kotlin

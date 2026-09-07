---
title: "莱莎 AI 陪伴桌面应用"
description: "本地优先的 2D 角色 AI 聊天客户端"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/zeroa234/ryza-ai-revive"
githubStars: 61
githubOwner: "zeroa234"
githubRepo: "ryza-ai-revive"
category: "other"
tags: ["chatbot", "avatar", "local-first", "webgl"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "这是一个开源的 AI 虚拟角色陪伴应用，用户可自带任意 OpenAI 兼容的 LLM 和 TTS 服务，在 Windows 或 Android 上体验带 2D 实时立绘的对话。适合想要快速搭建个性化 AI 伴侣或虚拟偶像直播的开发者与内容创作者，无需从零开发前端和交互。"
vibeCodingPrompt: "1. 克隆仓库并阅读 README 与 docs/PROJECT.md。
2. 使用 Claude Code 运行 `python scripts/serve.py` 启动开发服务器。
3. 让 Claude 读取 `config/` 下的 provider 模板，并指导你在设置页填入 OpenAI 兼容的 base URL、模型和 API key。
4. 如需接入 TTS，让 Claude 帮你配置 openai/qwen/fish 任一种凭证。
5. 使用 Claude Code 修改 `web/` 下的 UI 文本或对话逻辑，并运行回归测试。"
pitfallGuide: "不要用 `python -m http.server`，必须使用 `scripts/serve.py` 才能启用 /_proxy。
默认不包含任何 LLM 或 TTS 模型，需要自行配置 API 才能对话。
TTS 服务商（openai/qwen/fish）的凭证字段不同，填错会导致语音不可用。
多语言槽位（UI/语音/LLM/TTS）需分别配置，否则可能混用语言。
跨平台打包需分别使用 Electron 与 Android 构建流程，不能共用一套产物。"
targetAudience: ["独立开发者", "内容创作者", "创业者"]
useCases: ["搭建个性化 AI 虚拟伴侣", "制作带立绘的 AI 聊天机器人直播", "快速原型 2D 角色对话应用", "本地离线优先的 AI 角色交互实验"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Ryza AI companion. Bring your own LLM/TTS. 莱莎 AI 陪伴，自填大模型与语音。

> GitHub: [zeroa234/ryza-ai-revive](https://github.com/zeroa234/ryza-ai-revive) | ⭐ 61 | JavaScript

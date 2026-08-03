---
title: "Qwen 音频智能体运行时"
description: "让 AI 语音智能体持续对话与后台任务并行"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/QwenAudio/qwen-audio-agent"
githubStars: 1760
githubOwner: "QwenAudio"
githubRepo: "qwen-audio-agent"
category: "agent-framework"
tags: ["voice-agent", "realtime", "multi-agent", "async-tasks"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个实时语音运行时，让 AI 智能体在对话中同时处理后台任务，用户无需等待即可继续交流。适合需要构建语音助手、客服机器人或任务型对话应用的团队，可快速集成现有工具和 MCP 生态，提升交互流畅度与工作效率。"
vibeCodingPrompt: "1. 安装依赖：npm install qwen-audio-agent。
2. 初始化项目：npx qwen-audio-agent init（或参考 README 创建配置文件）。
3. 配置后台 Agent：在配置文件中指定要使用的 Agent（如 Qwen、自定义 MCP 工具）。
4. 启动运行时：npm run start，启动 WebUI 或 TUI。
5. 测试对话：在界面中说话，验证实时响应和后台任务并行。
6. 如需接入 macOS 桌面版，下载桌面应用并连接同一 Gateway。"
pitfallGuide: "需要 Node.js >= 22.22.2，版本过低会安装失败。\n首次使用需配置语音服务（如 STT/TTS），默认可能依赖云端 API，注意网络与密钥。\n后台任务依赖 ACP 架构，需确保 Agent 兼容 ACP 协议，否则任务无法异步执行。\nWebUI 与桌面版共享 Gateway，端口冲突时需调整配置。\n当前 v1.3.0 为测试版，部分功能（如 speech-to-speech）需源码构建，不建议生产直接使用。"
targetAudience: ["独立开发者", "创业者", "产品经理", "企业团队", "AI 研究者"]
useCases: ["构建语音客服助手，支持边听边查资料", "开发任务型语音助理，如日程管理、信息查询", "创建多轮对话的语音交互应用，无需等待后台处理", "集成现有 MCP 工具，实现语音驱动的自动化工作流"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

> GitHub: [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | ⭐ 1760 | JavaScript

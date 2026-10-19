---
title: "Gemini 隐身桥"
description: "用浏览器会话把 Gemini 网页版转成 OpenAI 兼容 API 的 Go 守护进程"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/azrinaldi/gemini-stealth-bridge"
githubStars: 95
githubOwner: "azrinaldi"
githubRepo: "gemini-stealth-bridge"
category: "dev-tools"
tags: ["gemini", "openai-compatible", "reverse-proxy", "golang"]
editorialScore: 3
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "这个项目让你把已有的 Gemini 网页版账号直接变成 OpenAI 格式的 API，省去申请开发者密钥和按量付费的麻烦。适合想低成本接入 AI 能力的独立开发者和小团队，也适合需要给现有工具快速挂上 Gemini 能力的人。"
vibeCodingPrompt: "用 gemini-stealth-bridge 搭一个本地 AI 聊天应用：1) 克隆仓库并编译 gsb，按 README 从浏览器导出 Google 会话 Cookie 配置到环境变量；2) 启动 gsb 守护进程，确认 /v1/chat/completions 可用；3) 用 Python 写一个命令行聊天脚本，通过 OpenAI SDK 把 base_url 指向本地 gsb 地址，实现多轮对话和流式输出；4) 再加一个函数调用示例，让模型调用本地天气查询函数并打印结果；5) 最后用 Claude Code 生成一个简单的 Web 前端，把聊天接口暴露成网页。"
pitfallGuide: "依赖浏览器 Cookie 登录，Cookie 过期或账号风控会导致请求失败，需定期更新
模型访问权限和配额取决于所连 Google 账号，不是所有模型都能用
项目通过逆向网页接口实现，Gemini 前端改版可能随时失效
仅限个人合法使用，批量或商业调用可能违反 Google 服务条款
函数调用是提示词模拟而非原生支持，复杂工具链稳定性有限"
targetAudience: ["独立开发者", "创业者", "技术负责人"]
useCases: ["给本地编码助手接入 Gemini 能力", "低成本搭建 OpenAI 兼容的内部 AI 网关", "把 Gemini 网页版能力集成到现有工具链", "个人多账号 AI 配额轮换使用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Browserless Chrome uTLS + HTTP/2 OpenAI-compatible API daemon for Google Gemini Web (/v1/chat/completions & /v1/responses)

> GitHub: [azrinaldi/gemini-stealth-bridge](https://github.com/azrinaldi/gemini-stealth-bridge) | ⭐ 95 | Go

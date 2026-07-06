---
title: "CSSwitch：Claude Science 第三方模型接入器"
description: "一键接入第三方 AI 模型到 Claude Science"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/SuperJJ007/CSSwitch"
githubStars: 265
githubOwner: "SuperJJ007"
githubRepo: "CSSwitch"
category: "agent-framework"
tags: ["Proxy", "API", "macOS", "LLM"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "CSSwitch 是一款 macOS 工具，让用户无需订阅 Claude，即可在 Claude Science 科研平台中使用 DeepSeek、通义千问等第三方 API 模型。它通过本地代理和隔离环境模拟登录，自动处理认证转换和协议适配，适合希望低成本使用 Claude Science 功能的开发者或科研人员。"
vibeCodingPrompt: "1. 在 macOS 上使用 Tauri 和 Rust 构建一个菜单栏应用。\n2. 实现本地 HTTP 代理，接收 Claude Science 的请求并转发到第三方 API。\n3. 在隔离环境中启动 Claude Science 的本地登录，设置环境变量 ANTHROPIC_BASE_URL 指向代理地址。\n4. 代理移除请求中的 OAuth 信息，注入用户的第三方 API Key，并转换协议格式。\n5. 提供 GUI 界面让用户选择服务商、输入 API Key、选择模型，并一键启动/停止。"
pitfallGuide: "1. 仅支持 macOS Apple Silicon，Intel Mac 无法使用。\n2. 需要先登录 Claude Science 并保持隔离环境，否则无法启动。\n3. API Key 验证仅在启用配置时进行，新建配置时不检查。\n4. 部分模型（如 DeepSeek）通过原生 Anthropic 端点接入，其他需协议转换。\n5. 使用官方 Claude 模式时需手动切换，避免代理干扰。"
targetAudience: ["AI 研究者", "独立开发者", "创业者", "数据分析师"]
useCases: ["在 Claude Science 中使用 DeepSeek 进行低成本科研分析", "企业团队通过统一 API 网关管理多个模型服务商", "开发者快速切换不同模型进行实验对比", "个人用户避免高额 Claude 订阅费"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。帮你的 Claude Science 一键接入你自己的 API：DeepSeek / 通义千问 / 智谱 GLM / Kimi / MiniMax / 小米 MiMo / 硅基流动 / OpenRouter / 任意 OpenAI·Anthropic 兼容端点

> GitHub: [SuperJJ007/CSSwitch](https://github.com/SuperJJ007/CSSwitch) | ⭐ 265 | Rust

---
title: "dsh 免费模型插件"
description: "零配置接入前沿大模型的 dsh 插件"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/zouyuxuan122/dsh-our-free-model"
githubStars: 326
githubOwner: "zouyuxuan122"
githubRepo: "dsh-our-free-model"
category: "dev-tools"
tags: ["free-llm", "dsh-plugin", "openai-compatible", "no-api-key"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个插件让用户在 dsh 工具里无需注册、登录或填写 API Key，就能直接调用 Muse Spark、MiMo 等前沿大模型，完全免费且不限量。适合想低成本试用 AI 能力的个人开发者和内容创作者，也适合作为产品原型阶段的临时模型通道。"
vibeCodingPrompt: "1) 先安装 dsh 工具（版本 0.1.5~0.1.7-rc.2），确认命令行可用；2) 在 dsh 中安装 dsh-our-free-model 插件，重启或热重载后进入设置页确认模型列表已拉取；3) 在设置页选择 Muse Spark 1.3 或 MiMo V2.6，把思考强度设为 Balanced 测试连通性；4) 用插件提供的 OpenAI 兼容本地转发端口，把 base_url 指向该端口，在 Claude Code 或 Cursor 中配置为自定义模型端点；5) 写一个简单脚本调用 /chat/completions 验证流式响应正常；6) 基于该端点搭建一个命令行问答工具或网页聊天界面，加入对话历史与模型切换下拉框；7) 开启文件监视自动重载，方便后续升级插件版本。"
pitfallGuide: "上游仅依赖 OpenCode Zen 网关，若该网关不可用或地区受限，插件会失效，需关注 region-limited 分组。
模型清单跟随上游刷新，选择器只显示实测可用模型，遇到 5xx/429 是网关问题而非模型下线，不要误判。
插件适配 dsh 0.1.5~0.1.7-rc.2，版本不匹配可能导致加载失败，升级前先看兼容性徽章。
虽为免费不限量，但网关可能限流或超时，生产环境建议加本地缓存与重试逻辑。
应用内升级会原子替换并回滚，但升级前仍建议备份配置，避免热重载异常。"
targetAudience: ["独立开发者", "创业者", "产品经理", "内容创作者"]
useCases: ["快速搭建免费的 AI 聊天原型", "在 Claude Code/Cursor 中接入免费模型做代码辅助", "为小型工具提供零成本的 LLM 后端", "教学演示或个人学习大模型能力"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 Muse Spark 1.3、MiMo V2.6 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, Muse Spark 1.3 and MiMo V2.6 among them. Completely free, with no usage cap.

> GitHub: [zouyuxuan122/dsh-our-free-model](https://github.com/zouyuxuan122/dsh-our-free-model) | ⭐ 326 | JavaScript

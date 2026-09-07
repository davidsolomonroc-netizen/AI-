---
title: "1Panel AI 网关"
description: "企业级 AI 统一接入与治理平台"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/1Panel-dev/1Panel-Gateway"
githubStars: 58
githubOwner: "1Panel-dev"
githubRepo: "1Panel-Gateway"
category: "other"
tags: ["ai-gateway", "model-proxy", "llm", "governance"]
editorialScore: 4
deploymentRating: 5
vibeCodingRating: 4
commercialSummary: "1Panel AI 网关帮助企业统一管理多种 AI 模型（如 OpenAI、Anthropic、DeepSeek 等）的接入，提供智能路由、权限控制、内容合规和用量分析等能力。它适合需要安全、高效、可控地使用 AI 模型的中小企业团队，尤其是 10 人以下可免费使用完整功能。通过 Docker 一行命令即可部署，快速搭建企业内部的 AI 接入中枢。"
vibeCodingPrompt: "使用 1Panel-Gateway 为我的团队搭建一个 AI 网关：
1. 运行 `docker run --pull always -d --name 1panel-ai-gateway --restart unless-stopped -p 8080:8080 -v /opt/ai-gateway:/opt/ai-gateway 1panel/ai-gateway` 启动容器。
2. 执行 `docker logs 1panel-ai-gateway` 获取管理员临时密码。
3. 访问 `http://<服务器IP>:8080`，登录并修改密码。
4. 在管理界面添加模型供应商（如 OpenAI、DeepSeek）的 API Key，并配置模型映射。
5. 创建用户组，设置模型权限和配额。
6. 为我的 AI 应用提供统一的 Base URL 和 API Key，即可通过网关调用所有模型。"
pitfallGuide: "首次部署后务必立即修改默认管理员密码，防止未授权访问。\n建议仅在可信内网直接开放 8080 端口，生产环境需配置 HTTPS 反向代理。\n配置模型供应商时需正确填写 API Key 和模型名称，否则请求会失败。\n智能路由规则需仔细测试，避免误将请求分发到不合适的模型组。\n免费版本仅适用于 10 人及以下团队，超出需购买商业授权。"
targetAudience: ["企业团队", "技术负责人", "独立开发者"]
useCases: ["企业内部多个 AI 应用的统一模型接入与密钥管理", "团队内不同成员或项目使用不同模型的权限与配额控制", "对 AI 调用内容进行合规审核与审计，满足安全要求", "通过用量分析优化模型调用成本与性能"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。1Panel AI 网关提供从统一接入、智能路由到合规审计的全链条管控，让企业 AI 落地更安全、更高效、更可控。

> GitHub: [1Panel-dev/1Panel-Gateway](https://github.com/1Panel-dev/1Panel-Gateway) | ⭐ 58 | 多种语言

---
title: "My Free Code：多提供商AI网关"
description: "为Claude Code等编码代理提供多模型路由与回退的网关"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/hkqr/my-free-code"
githubStars: 432
githubOwner: "hkqr"
githubRepo: "my-free-code"
category: "agent-framework"
tags: ["multi-provider", "claude-code", "ai-gateway", "open-source"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "My Free Code是一个开源的多提供商AI网关，让Claude Code等编码代理能够接入数十种AI模型提供商（如OpenRouter、Groq、DeepSeek等），实现智能路由、故障回退和成本优化。它适合希望减少对单一AI供应商依赖、降低API成本或利用免费/本地模型的开发团队和独立开发者，无需修改现有编码代理的配置即可透明接入。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/hkqr/my-free-code && cd my-free-code\n2. 安装依赖：pip install -r requirements.txt\n3. 配置环境变量：在.env中设置至少一个提供商API密钥（如OPENROUTER_API_KEY）\n4. 启动网关：python main.py（默认端口8080）\n5. 配置Claude Code：设置ANTHROPIC_BASE_URL=http://localhost:8080，并设置ANTHROPIC_API_KEY为任意值\n6. 测试网关：curl http://localhost:8080/v1/models 查看可用模型\n7. 启动Claude Code，即可通过网关使用多提供商路由，自动选择可用模型并处理回退"
pitfallGuide: "1. 需要至少配置一个有效的提供商API密钥，否则网关无法工作\n2. 部分提供商需要专用适配器（如AWS Bedrock、Google Vertex），需额外配置认证\n3. 本地模型（如Ollama）需要单独启动并配置，网关不会自动启动它们\n4. 某些提供商不支持流式或工具调用，可能导致部分代理功能异常\n5. 生产环境需设置安全认证（如API密钥），避免网关被未授权访问"
targetAudience: ["独立开发者", "技术负责人", "企业团队", "AI研究者"]
useCases: ["在Claude Code中接入多个免费或低成本AI模型提供商，降低API费用", "为团队提供统一的AI网关，实现模型故障自动回退和负载均衡", "在本地开发环境中使用本地模型（如Ollama）进行测试，同时保留云端模型备用", "通过Admin UI监控各提供商使用情况和健康状态"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source multi-provider AI gateway for Claude Code and other coding agents, with model routing, streaming, tools, reasoning, fallbacks, and local model support

> GitHub: [hkqr/my-free-code](https://github.com/hkqr/my-free-code) | ⭐ 432 | Python

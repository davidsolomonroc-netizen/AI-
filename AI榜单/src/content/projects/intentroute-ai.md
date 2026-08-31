---
title: "意图路由AI"
description: "用自然语言为Windows应用配置智能网络路由"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/Vincent-Xi08/IntentRoute-AI"
githubStars: 101
githubOwner: "Vincent-Xi08"
githubRepo: "IntentRoute-AI"
category: "workflow-automation"
tags: ["ai-routing", "windows", "sing-box", "split-tunnel"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "IntentRoute AI 让非技术用户通过自然语言描述网络需求，自动生成并验证Windows应用的路由规则，避免手动配置代理的复杂和错误。适合需要精细化网络分流的企业或个人，如跨境办公、游戏加速、开发测试环境隔离。"
vibeCodingPrompt: "1. 克隆项目仓库并阅读README，了解核心概念。\n2. 安装依赖：确保有.NET SDK和sing-box核心。\n3. 运行项目，启动WPF界面。\n4. 在界面中输入自然语言指令，如'让浏览器走代理，游戏直连'。\n5. 系统生成规则草案并本地验证，确认后启用。\n6. 如需集成到Claude Code，可调用其CLI或API，将意图转换为JSON格式的路由规则。"
pitfallGuide: "1. AI生成的规则可能不完整或有误，务必人工审核后再启用。\n2. 需要预先安装并配置sing-box TUN数据平面，否则无法生效。\n3. 本地Ollama模型需提前运行，否则只能使用OpenAI API。\n4. 项目处于v0.9.0预览版，生产环境使用需谨慎。\n5. Windows防火墙或权限设置可能影响TUN模式，需以管理员身份运行。"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["企业内部网络分流管理", "个人开发者测试多环境网络路由", "跨境办公应用加速与隔离"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source AI-assisted per-application routing for Windows with OpenAI/Ollama drafts and a sing-box TUN data plane.

> GitHub: [Vincent-Xi08/IntentRoute-AI](https://github.com/Vincent-Xi08/IntentRoute-AI) | ⭐ 101 | C#

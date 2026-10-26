---
title: "Lampline 语音智能体平台"
description: "在本地构建并测试 AI 电话代理的开源框架"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/C4rohan/Lampline"
githubStars: 267
githubOwner: "C4rohan"
githubRepo: "Lampline"
category: "agent-framework"
tags: ["voice-agents", "self-hosted", "dialogflow-import", "sip"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Lampline 让你在自己的电脑或服务器上搭建 AI 电话客服，无需依赖昂贵的云服务，每通电话成本仅几分钱。它支持从 Google Dialogflow CX 迁移现有代理，适合希望低成本、高可控性地部署语音 AI 的中小企业和独立开发者。"
vibeCodingPrompt: "使用 Lampline 搭建一个简单的客服电话代理：1. 克隆仓库并安装依赖（参考 README 的快速开始）；2. 运行 `vk` CLI 初始化项目，配置本地模型或自己的 API 密钥；3. 在配置文件中定义对话流程和意图，或导入现有的 Dialogflow CX 代理；4. 启动本地服务器，用内置的 AI 呼叫器测试对话；5. 如需接入真实电话，配置 SIP 中继并测试呼入呼出。"
pitfallGuide: "需要本地或远程的语音识别/合成服务，首次配置可能需调整模型参数\nSIP 电话集成需要额外的网络和账号配置，非技术用户可能遇到困难\n导入 Dialogflow CX 代理时注意版本兼容性和意图映射\n本地运行对硬件有一定要求，建议先测试小规模场景\n免费模式依赖本地模型，效果可能不如商用 API，需权衡成本与质量"
targetAudience: ["独立开发者", "创业者", "企业团队", "技术负责人"]
useCases: ["搭建低成本电话客服系统", "测试和迭代语音对话流程", "从 Dialogflow CX 迁移到自托管方案", "开发基于 SIP 的智能外呼应用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Build AI phone agents on your own computer and test every change with an AI caller. Open source, runs free with no API keys, cents per call with your own keys. Imports Dialogflow CX.

> GitHub: [C4rohan/Lampline](https://github.com/C4rohan/Lampline) | ⭐ 267 | Python

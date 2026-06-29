---
title: "浏览器原生AI代理工具"
description: "首个在浏览器内运行AI代理的扩展"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/NotASithLord/peerd"
githubStars: 225
githubOwner: "NotASithLord"
githubRepo: "peerd"
category: "agent-framework"
tags: ["agentic", "browser-extension", "p2p", "webassembly"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Peerd是一个Chrome/Firefox扩展，让AI代理直接在浏览器内运行，无需后端服务器。它能操控你的标签页、启动沙盒化计算环境（如JS笔记本、WASM Linux虚拟机），并通过P2P网络共享构建的成果。适合希望利用现有浏览器环境、自备API密钥、且注重隐私的开发者和小团队。"
vibeCodingPrompt: "第一步：在Chrome中安装Peerd扩展，并配置你的LLM API密钥（如OpenAI）。
第二步：使用扩展的界面创建一个新代理，指定目标（例如'自动抓取当前页面的所有链接并生成摘要'）。
第三步：观察代理如何读取当前标签页内容、打开新标签、执行JS代码并返回结果。
第四步：如需与其他代理共享结果，启用P2P功能并邀请对方加入同一网络。"
pitfallGuide: "项目仍处于实验阶段（0.x），可能存在不稳定或API变更。\n需要用户自备LLM API密钥（BYOK），不支持内置模型。\nP2P功能仅在预览通道可用，且依赖WebRTC，可能受网络环境限制。\n作为浏览器扩展，沙盒化计算能力受限于浏览器安全策略，不适用于高性能计算。\n目前仅支持Chrome和Firefox，其他浏览器未测试。"
targetAudience: ["独立开发者", "AI研究者", "技术负责人"]
useCases: ["自动化网页操作（如数据抓取、表单填写）", "在浏览器内运行轻量级AI实验和原型", "构建去中心化的代理协作网络", "无需后端即可部署个人AI助手"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The first AI agent harness native to the browser. A Chrome/Firefox extension that runs the agent loop in your browser — drives your tabs, spins up sandboxed compute (JS notebooks, WASM Linux VMs, client-side apps), and shares what it builds peer-to-peer. BYOK · no backend · no telemetry.

> GitHub: [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | ⭐ 225 | JavaScript

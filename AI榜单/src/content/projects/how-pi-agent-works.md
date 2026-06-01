---
title: "Pi Agent 原理与实现教程"
description: "从零到一实现 AI Agent 的教程"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/cellinlab/how-pi-agent-works"
githubStars: 302
githubOwner: "cellinlab"
githubRepo: "how-pi-agent-works"
category: "agent-framework"
tags: ["agent", "tutorial", "typescript", "react"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一套面向开发者的 AI Agent 教学项目，通过渐进式 Demo 和最终的教学版 Agent 应用，帮助理解 Agent 的核心原理（如循环、工具调用、会话树等）。适合希望系统学习 Agent 开发、并能实际搭建可运行 Agent 应用的团队或个人。"
vibeCodingPrompt: "使用该项目的教学版 Agent 代码库，帮我搭建一个定制化的 AI Agent 应用。
1. 克隆仓库并安装依赖：git clone https://github.com/cellinlab/how-pi-agent-works.git && cd how-pi-agent-works && npm install
2. 运行教学版 Agent 开发服务器：npm run teaching-agent:dev
3. 在 examples/teaching-agent 目录下，找到 React 前端和 Express API 的源码，按照教程文档（docs/）中的说明，修改工具函数或消息处理逻辑来适配你的业务需求。
4. 测试工具调用和会话管理功能，确保 Agent 能正确响应。"
pitfallGuide: "1. 运行 Demo 05 需要设置有效的 OpenAI 兼容 API 环境变量，否则会报错。\n2. 教学版 Agent 的 API 和前端默认端口不同（4317 和 5174），确保两者同时运行。\n3. 不要将 API Key 硬编码到代码中，应通过环境变量传入。\n4. 教程站点是静态 VitePress 站点，不包含教学版 Agent 的运行时。\n5. 项目依赖 npm，确保 Node.js 版本兼容（建议 >=18）。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["学习 AI Agent 核心原理与实现", "搭建教学或演示用的 Agent 原型", "作为企业内部 Agent 开发培训材料", "基于教程扩展开发定制化 Agent 应用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Pi Agent 原理与实现

> GitHub: [cellinlab/how-pi-agent-works](https://github.com/cellinlab/how-pi-agent-works) | ⭐ 302 | 多种语言

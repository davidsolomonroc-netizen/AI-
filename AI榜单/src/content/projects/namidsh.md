---
title: "NamiDSH 迷你插件架构学习项目"
description: "千行代码拆解 DSH 插件化 Agent 架构"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/aa1143/NamiDSH"
githubStars: 185
githubOwner: "aa1143"
githubRepo: "NamiDSH"
category: "agent-framework"
tags: ["TypeScript", "plugin-architecture", "agent", "learning"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个用于理解大型 AI Agent 框架内部结构的教学项目，把百万行代码的 DeepSeek Harness 压缩成一千来行可读的 TypeScript。适合想搞懂 Agent 插件化架构、但又不想啃源码的开发者，学完能自己搭类似的插件式 Agent 系统。"
vibeCodingPrompt: "1. 克隆仓库并运行 npm install，确认 Node.js 版本 ≥22.18；2. 运行 npm start，在浏览器打开本地页面，先用离线模式对话验证跑通；3. 阅读 src 下迷你 Cordis 的插件加载与依赖注入代码，理解 Service 基类和 inject 静态属性；4. 基于现有插件结构，新增一个自定义工具插件（如天气查询或计算器），实现 class 继承 Service 并声明 inject；5. 在网页端 Agent 中注册该插件，测试对话触发工具调用；6. 如需接入真实模型，配置 DeepSeek API Key 环境变量，对比离线与在线行为差异。"
pitfallGuide: "Node.js 版本必须 ≥22.18，否则无法直接运行 TypeScript\n项目定位是学习拆解而非生产框架，功能刻意精简，不要直接用于线上业务\n迷你 Cordis 与真 Cordis 仅保证 14 个兼容测试场景一致，边界行为可能有差异\n接入 DeepSeek 需要自行准备 API Key，离线模式能力有限\n新增插件需严格遵循 Service 继承与 inject 声明写法，否则依赖注入会失败"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["学习 Agent 插件化架构与依赖注入设计", "作为自建插件式 Agent 系统的参考骨架", "教学或团队内部分享 AI Agent 原理", "快速验证自定义工具插件的原型"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。对照 DeepSeek Harness 的迷你学习项目：迷你版 Cordis + 迷你版 DSH + 网页端 Agent

> GitHub: [aa1143/NamiDSH](https://github.com/aa1143/NamiDSH) | ⭐ 185 | TypeScript

---
title: "TokenDiet"
description: "AI编码代理的本地成本优化代理"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/agiwhitelist/tokdiet"
githubStars: 69
githubOwner: "agiwhitelist"
githubRepo: "tokdiet"
category: "dev-tools"
tags: ["proxy", "cost-optimization", "context-compression", "llm-gateway"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "TokenDiet是一个本地反向代理，位于AI编码代理（如Claude Code、Cursor）与模型API之间，自动压缩冗余上下文并实时计量token和美元成本。它通过A/B测试证明压缩后的输出质量不变，帮助团队大幅降低API支出，适合使用付费大模型进行开发的企业和个人开发者。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：`git clone https://github.com/agiwhitelist/tokdiet && cd tokdiet && npm install`
2. 配置环境变量：在项目根目录创建`.env`文件，设置`ANTHROPIC_API_KEY`或`OPENAI_API_KEY`等API密钥
3. 启动代理服务：`npm run dev`（默认监听localhost:3000）
4. 修改你的AI编码代理（Claude Code/Cursor）的API端点指向`http://localhost:3000`
5. 打开浏览器访问`http://localhost:3000`查看实时仪表盘，观察token节省和成本数据
6. 如需调整压缩策略，编辑`src/config.ts`中的参数并重启服务"
pitfallGuide: "1. 项目依赖Node.js 20+，请确保本地环境版本匹配\n2. 首次运行需要配置至少一个模型API的密钥，否则代理无法转发请求\n3. 压缩效果因上下文类型而异，代码文件通常节省70%+，但纯文本对话可能节省较少\n4. 部分高级压缩策略可能对极长上下文（>100K tokens）有性能影响，建议测试后再投入生产\n5. 仪表盘数据存储在内存中，重启服务后历史记录会丢失"
targetAudience: ["独立开发者", "技术负责人", "企业团队", "AI研究者"]
useCases: ["降低Claude Code/Cursor等AI编码工具的API调用成本", "监控和优化团队AI使用支出", "在保持输出质量的前提下压缩长上下文", "对比不同模型或压缩策略的成本效益"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Local streaming reverse proxy between AI coding agents (Claude Code, Cursor, Codex) and model APIs (Anthropic, OpenAI, Gemini, MiniMax). Meters every token + USD cost, compacts bloated context to cut pay-per-token API spend, and runs shadow-eval to prove quality held. ccusage-style metering + live local dashboard.

> GitHub: [agiwhitelist/tokdiet](https://github.com/agiwhitelist/tokdiet) | ⭐ 69 | TypeScript

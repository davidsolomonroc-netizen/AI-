---
title: "TraceCrate 智能体追踪台"
description: "本地优先的 AI 智能体追踪分析工作台"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/FankChen/tracecrate"
githubStars: 117
githubOwner: "FankChen"
githubRepo: "tracecrate"
category: "dev-tools"
tags: ["observability", "local-first", "ai-agents", "opentelemetry"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "TraceCrate 帮你在本地把 Claude Code、Codex 等 AI 智能体的运行日志变成可搜索的时间线和对比报告，全程无需后端、不上传数据、不需要 API 密钥。适合关注隐私的开发者、AI 团队和需要审计智能体行为的工程负责人，用来排查问题、复盘运行过程并安全地分享结果。"
vibeCodingPrompt: "用 TraceCrate 搭建一个本地 AI 智能体追踪分析工具：1) 确认已安装 Node.js ≥22.12（推荐 24）和 npm；2) 克隆仓库 git clone https://github.com/FankChen/tracecrate 并进入目录；3) 运行 npm install 安装依赖；4) 运行 npm run dev 启动本地开发服务器，浏览器打开提示的地址；5) 准备 Claude Code 或 Codex 的日志文件（或 OTLP 格式日志），通过界面导入；6) 在时间线中查看事件序列、指标和启发式诊断，用搜索定位关键步骤；7) 选择两次运行进行并排对比，找出差异；8) 导出隐私友好的报告（注意检查敏感信息）。如需部署到静态托管，运行 npm run build 后发布 dist 目录。"
pitfallGuide: "需要 Node.js ≥22.12，版本过低会导致启动失败，推荐用 24。
项目只读取日志文件，不会运行智能体或执行记录中的命令，别指望它帮你跑任务。
导入的日志可能含敏感信息，导出报告前务必人工检查隐私内容。
演示站点的数据是合成示例，不是真实基准测试结果，不要据此评估性能。
本地开发需自行克隆和构建，非技术用户建议先用在线演示体验。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者", "企业团队"]
useCases: ["排查 Claude Code / Codex 智能体运行中的异常步骤", "对比多次智能体运行结果找出差异", "在不上传数据的前提下审计智能体行为", "导出隐私友好的追踪报告用于团队复盘"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Local-first AI agent trace workbench. Inspect Claude Code, Codex and OTLP logs, compare runs, and export privacy-conscious reports. No backend or API keys.

> GitHub: [FankChen/tracecrate](https://github.com/FankChen/tracecrate) | ⭐ 117 | TypeScript

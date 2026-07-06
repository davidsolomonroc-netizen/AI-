---
title: "T3MP3ST：多智能体红队攻击框架"
description: "自主红队平台，AI代理零日狩猎"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/elder-plinius/T3MP3ST"
githubStars: 1907
githubOwner: "elder-plinius"
githubRepo: "T3MP3ST"
category: "agent-framework"
tags: ["redteam", "offensive-security", "multi-agent", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "T3MP3ST 是一个多智能体攻击安全框架，将现有的 AI 编码代理（如 Claude Code、Codex）转化为自动化红队工具。它无需新 API 密钥或云租户，可完全本地运行，适合安全团队、渗透测试人员和企业红队进行自主攻防演练。"
vibeCodingPrompt: "请使用 T3MP3ST 框架进行一个自动化红队演练：
1. 克隆仓库并安装依赖：`git clone https://github.com/elder-plinius/T3MP3ST.git && cd T3MP3ST && npm install`
2. 配置目标授权：在 `config/targets.json` 中添加待测试的授权目标 URL
3. 启动浏览器作战室：`npm run war-room` 打开 Web 界面
4. 或使用 CLI 模式：`npm run hunt -- --target https://example.com`
5. 选择 AI 代理后端（Claude Code、Codex 或本地 Ollama），框架自动执行侦察、利用和报告
6. 查看生成的报告：`npm run report -- --session <session-id>`"
pitfallGuide: "1. 必须仅在获得明确授权的目标上使用，非法测试可能触犯法律
2. 首次运行需确保 AI 代理 API 密钥或本地模型已正确配置
3. 浏览器作战室需要 Node.js 18+ 和现代浏览器
4. 大规模扫描可能触发目标 WAF/IDS，建议先在小范围测试
5. 报告生成依赖 AI 代理输出质量，复杂漏洞可能需要人工验证"
targetAudience: ["安全工程师", "渗透测试人员", "红队成员", "技术负责人"]
useCases: ["自动化渗透测试与漏洞发现", "红队演练与安全评估", "AI 代理安全能力基准测试", "持续集成安全扫描"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。autonomous red teaming platform; multi-agent offensive-security meta-harness

> GitHub: [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | ⭐ 1907 | TypeScript

---
title: "数据面具 Maskit"
description: "本地隐私脱敏网关，让 AI 编程工具自动打码敏感信息"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/xiaYuTian11/maskit"
githubStars: 209
githubOwner: "xiaYuTian11"
githubRepo: "maskit"
category: "dev-tools"
tags: ["privacy", "proxy", "llm", "pii"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Maskit 在你和 Cursor、Claude Code 等 AI 编程工具之间架设一道本地隐私网关，自动把代码里的 API 密钥、数据库密码、手机号等敏感信息替换成占位符再发给大模型，等模型回复时再自动还原成原文。适合所有担心代码或业务数据泄露给外部 AI 服务商的开发者和企业团队。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/xiaYuTian11/maskit && cd maskit；2. 按 README 安装依赖（推荐 Docker 方式：docker compose up -d）；3. 启动后打开本地 Web 界面，在设置里配置你的上游 LLM API 地址和密钥；4. 将 Cursor/Claude Code 的 Base URL 改为 Maskit 本地代理地址（如 http://localhost:8080）；5. 在 Maskit 规则面板中自定义需要脱敏的敏感词、正则模式（如内部域名、公司代号）；6. 正常使用 AI 编程工具，观察 Maskit 日志确认请求已打码、回复已还原；7. 如需集成到 CI 或团队环境，参考 docs 中的环境变量配置，将代理地址通过 ANTHROPIC_BASE_URL 等变量注入。"
pitfallGuide: "首次运行需配置上游 API 地址和密钥，否则代理无法转发请求
流式还原依赖本地规则匹配，自定义正则写得太宽可能误伤正常代码
Windows 桌面版与 Docker 版配置路径不同，注意区分
敏感词规则库需要按团队实际情况维护，默认规则可能覆盖不全
代理会拦截所有 AI 请求，确保本地端口不被外部访问以防信息泄露"
targetAudience: ["独立开发者", "企业团队", "技术负责人", "AI 研究者"]
useCases: ["使用 Cursor/Claude Code 时防止 API 密钥和数据库密码泄露给模型服务商", "企业内部要求代码不出内网但又要用外部 AI 编程助手的合规场景", "处理含手机号、身份证等 PII 数据时自动脱敏后再交给大模型分析", "团队统一配置敏感词规则，避免成员无意间把保密业务代号发给 AI"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。数据面具 Data Maskit — 专为大模型打造的本地隐私脱敏网关（请求自动打码，回复流式还原；支持 Cursor / Claude Code / Codex / Pi 等任意可配 Base URL 工具）

> GitHub: [xiaYuTian11/maskit](https://github.com/xiaYuTian11/maskit) | ⭐ 209 | Python

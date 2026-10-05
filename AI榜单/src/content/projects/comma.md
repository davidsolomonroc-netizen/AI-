---
title: "Comma 个人智能体"
description: "开源无会话个人智能体，持续执行任务"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/AFK-surf/Comma"
githubStars: 172
githubOwner: "AFK-surf"
githubRepo: "Comma"
category: "agent-framework"
tags: ["personal-agent", "sessionless", "self-hosted", "automation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Comma 是一个开源的个人 AI 智能体，能持续记住你的上下文并自动完成购物、文件处理、远程操作等任务，无需反复开启新对话。它适合希望拥有私有化、可自托管 AI 助手的个人用户和小团队，替代 Muse、Dots 等商业服务。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/AFK-surf/Comma && cd Comma；2. 阅读 README 和 docker-compose.yml，确认依赖（Go/Elixir/Lean）；3. 运行 docker compose up -d 启动服务，或按文档安装 Elixir 与 Go 环境后执行 mix deps.get && mix phx.server；4. 配置环境变量（API 密钥、模型提供商如 OpenAI/Claude）；5. 访问 http://localhost:4000 完成初始设置；6. 在界面中创建一个测试任务（如“整理下载文件夹”），观察智能体循环执行；7. 集成 Claude Code 或 ChatGPT 作为后端模型，通过设置页面填入 API 端点；8. 使用远程控制功能连接手机或浏览器，验证跨设备任务连续性。"
pitfallGuide: "需要同时安装 Go、Elixir 和 Lean 工具链，环境配置较复杂，建议优先使用 Docker 镜像。
自托管需自行提供 LLM API 密钥，会产生调用费用，注意设置用量限制。
项目处于早期阶段（172 stars），文档和稳定性可能不完善，生产使用需谨慎。
跨设备同步依赖网络和账户体系，自托管时需配置好反向代理和 HTTPS。
与 ChatGPT/Claude Code 的兼容性可能随版本变化，需关注仓库更新日志。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI 研究者"]
useCases: ["个人任务自动化（文件整理、日程管理）", "跨设备持续上下文助手", "自托管替代商业个人 AI 服务", "多模型协作的智能体工作流实验"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Best free & open source personal agent. Always-on, proactive, sessionless. Browser, computer use, files, remote control. Competiable with ChatGPT/codex and claude code. Selfhost your open source alternative to Muse, Dots, Instinct and Town. Built with Go/Elixir/Lean.

> GitHub: [AFK-surf/Comma](https://github.com/AFK-surf/Comma) | ⭐ 172 | Elixir

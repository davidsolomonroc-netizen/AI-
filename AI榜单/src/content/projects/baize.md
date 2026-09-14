---
title: "白泽 Baize"
description: "开源多后端 AI 编程 Agent 终端 CLI"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/Xu123-Bob/Baize"
githubStars: 69
githubOwner: "Xu123-Bob"
githubRepo: "Baize"
category: "dev-tools"
tags: ["ai-agent", "cli", "coding-assistant", "multi-backend"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "白泽是一个在终端里运行的 AI 结对编程助手，能帮开发者自动写代码、改文件、跑命令、搜索资料。它支持 DeepSeek、OpenAI 兼容接口以及本地 Ollama 模型，适合想低成本用 AI 辅助编程的独立开发者和小型技术团队。"
vibeCodingPrompt: "1. 在终端执行 `pip install https://github.com/Xu123-Bob/Baize.git` 安装白泽。
2. 运行 `baize` 命令，首次启动会自动生成 `~/.baize/config.toml` 和 `~/.baize/.env` 配置文件。
3. 编辑 config.toml，将 active_provider 设为 deepseek（或 openai / ollama），并在 .env 中填入对应 API Key。
4. 再次运行 `baize` 进入交互界面，输入自然语言任务，例如「帮我用 Python 写一个爬取豆瓣电影 Top250 的脚本并保存为 CSV」。
5. 白泽会调用 bash、文件读写等工具自动完成代码生成与执行，你只需在终端确认或调整。
6. 如需更专业的领域知识，可在项目目录下创建 SKILL.md 文件让白泽按需加载技能；复杂任务可用子代理委派避免上下文污染。"
pitfallGuide: "需要 Python 3.10+ 环境，3.10 用户需额外安装 tomli 才能解析配置文件。
首次运行必须手动编辑 config.toml 和 .env 填入 API Key，无法完全零配置直接使用。
使用 Ollama 本地模型时需先自行安装并启动 Ollama 服务，且本地模型能力有限，复杂任务建议用 DeepSeek 等云端模型。
安全沙箱虽提供命令白名单和路径逃逸检测，但仍建议不要在包含敏感密钥的目录下运行。
项目 star 数较少（69），社区生态和长期维护稳定性有待观察，生产环境使用需谨慎评估。"
targetAudience: ["独立开发者", "技术负责人", "创业者"]
useCases: ["终端内 AI 结对编程，自动生成和修改代码", "批量文件处理与自动化脚本编写", "本地 Ollama 模型驱动的隐私敏感编程任务", "通过 MCP 协议接入 GitHub 等外部工具进行工作流自动化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。白泽 —— 中国古代神话中通晓万物的瑞兽，如今化身为 Vibe Coding 助手。  一个开源的 AI Coding Agent CLI，支持多后端（DeepSeek / OpenAI 兼容 / Ollama 本地），具备工具调用、技能加载、子代理委派、上下文压缩、安全沙箱等完整能力。在终端即可与 AI 结对编程。

> GitHub: [Xu123-Bob/Baize](https://github.com/Xu123-Bob/Baize) | ⭐ 69 | JavaScript

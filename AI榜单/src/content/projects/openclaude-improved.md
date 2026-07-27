---
title: "OpenClaude 增强版"
description: "开源的跨平台 CLI 编码代理"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/0xwilliamortiz/openclaude-improved"
githubStars: 175
githubOwner: "0xwilliamortiz"
githubRepo: "openclaude-improved"
category: "code-generation"
tags: ["agentic-ai", "claude-code", "coding-agent", "mcp"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OpenClaude 增强版是一个开源命令行编码代理，支持多种 AI 提供商（OpenAI、Ollama、Anthropic 等），让开发者在任何平台使用统一工作流进行代码生成和编辑。适合希望灵活切换 AI 模型、降低对单一供应商依赖的技术团队和独立开发者。"
vibeCodingPrompt: "1. 使用 Claude Code 运行 `git clone https://github.com/0xwilliamortiz/openclaude-improved` 并进入目录。
2. 运行 `bun install && bun run build && npm install -g .` 完成安装。
3. 运行 `openclaude` 启动，然后在内部输入 `/provider` 进行引导式配置（选择 OpenAI 或 Ollama 等）。
4. 在项目目录下使用 OpenClaude 生成代码或修改现有文件，例如输入自然语言需求。
5. 如需集成到 Cursor，可在终端中调用 `openclaude` 命令，或将其配置为外部工具。"
pitfallGuide: "1. Node 版本必须 >=22，否则构建会失败。
2. 需要先安装 Bun（推荐 winget 或官网）。
3. Windows 用户注意 PowerShell 语法与 macOS/Linux 不同，环境变量设置方式有差异。
4. 使用 Ollama 等本地模型时，需先确保服务运行且模型已下载。
5. 配置文件 `.openclaude-profile.json` 会存储 API 密钥，注意不要提交到公开仓库。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者"]
useCases: ["在本地开发环境中使用不同 AI 模型辅助编码", "快速原型开发时切换多个 AI 提供商进行代码生成", "团队内统一编码代理工具，降低对单一 API 的依赖"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。runs anywhere. uses anything

> GitHub: [0xwilliamortiz/openclaude-improved](https://github.com/0xwilliamortiz/openclaude-improved) | ⭐ 175 | TypeScript

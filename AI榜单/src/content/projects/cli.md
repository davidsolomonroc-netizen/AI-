---
title: "阿里云百炼 CLI"
description: "阿里云模型服务的 AI Agent 命令行工具"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/modelstudioai/cli"
githubStars: 155
githubOwner: "modelstudioai"
githubRepo: "cli"
category: "agent-framework"
tags: ["cli", "multimodal", "qwen", "agent"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "阿里云百炼 CLI 是一个为 AI Agent 框架设计的命令行工具，将模型调用、搜索、多模态识别和工作流编排封装为结构化工具。适合需要快速集成阿里云大模型能力（如通义千问、图像/视频生成）的开发者或企业团队，无需复杂后端即可通过终端或 Agent 框架调用。"
vibeCodingPrompt: "1. 安装：npm install -g bailian-cli
2. 设置 API 密钥：export BAILIAN_API_KEY=your_key
3. 在 Claude Code 或 Cursor 中，使用命令如 `bailian chat \"你好\"` 进行对话，或 `bailian image generate \"描述\"` 生成图像。
4. 若需集成到 Agent 中，将每个命令包装为 tool call，例如：{ \"name\": \"bailian_chat\", \"parameters\": { \"prompt\": \"用户输入\" } }。
5. 测试复杂工作流：先调用 `bailian image understand <url>` 理解图片，再调用 `bailian chat \"基于图片内容...\"` 进行后续推理。"
pitfallGuide: "1. 需要 Node.js >=22.12，低版本无法运行。\n2. 必须先申请阿里云百炼 API Key 并配置环境变量，否则所有命令失败。\n3. 部分功能（如视频生成）依赖 HappyHorse 模型，可能需额外授权或配额。\n4. 输出为结构化 JSON，直接终端阅读体验一般，建议配合 jq 或 Agent 框架使用。\n5. 语音合成依赖 CosyVoice，5-20 秒样本克隆效果最佳，过短或过长可能影响质量。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "企业团队"]
useCases: ["通过终端快速测试通义千问模型效果", "在 AI Agent 中集成图像生成与视频编辑能力", "自动化多模态工作流：理解图片后生成描述并语音合成", "结合搜索和记忆功能构建智能客服原型"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Official Model Studio CLI（阿里云百炼 CLI）built for AI Agent frameworks, exposing models, search, multimodal, and workflow capabilities as structured tool calls.

> GitHub: [modelstudioai/cli](https://github.com/modelstudioai/cli) | ⭐ 155 | TypeScript

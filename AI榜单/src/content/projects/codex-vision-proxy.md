---
title: "Codex 视觉代理：纯文本模型的看图神器"
description: "让纯文本模型在 Codex 中流畅调用内置看图工具"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/Anionex/codex-vision-proxy"
githubStars: 214
githubOwner: "Anionex"
githubRepo: "codex-vision-proxy"
category: "multimodal"
tags: ["codex", "vision", "text-only-llm", "toolkit"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 4
commercialSummary: "本项目解决了纯文本模型（如 DeepSeek）在 Codex 中无法查看图片的问题，通过代理调用内置 view_image 工具，返回图片的详细描述，让模型获得接近多模态的体验。适合使用 Codex 搭配纯文本模型进行开发、调试、GUI 操作的用户，无需额外 MCP 或复杂配置，即可实现截图分析、UI 调试、图像问答等功能。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/Anionex/codex-vision-proxy.git
2. 安装依赖：pip install -r requirements.txt
3. 配置环境变量：设置 OPENAI_API_KEY 或 ANTHROPIC_API_KEY 用于代理服务，以及可选的视觉模型 API key（如 GLM、Kimi）
4. 启动代理服务：python proxy_server.py
5. 在 Codex 配置中将模型指向代理地址，使纯文本模型可以调用 view_image
6. 可选安装视觉工具包：运行 install_vision_tools.sh，提供 glance 和 ground 命令行工具
7. 在 Codex 中测试：让模型描述一张图片，观察它是否返回详细描述而非报错"
pitfallGuide: "确保代理服务器与 Codex 在同一网络环境，避免端口冲突\n配置视觉模型 API 时需确保有足够配额，否则图片描述可能失败\n对于复杂图片，纯文本模型的描述可能不如真实多模态模型准确，需人工校验\n不要同时启用其他 MCP 视觉工具，以免冲突\n更新 Codex 后需检查代理兼容性，因为内置工具行为可能变化"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "产品经理"]
useCases: ["在 Codex 中使用 DeepSeek 进行 UI 截图调试", "为纯文本模型提供图像问答能力", "辅助 GUI 自动化操作（Computer Use）", "多步骤图像推理任务"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。让纯文本模型在 Codex 中无障碍调用内置看图工具（view_image）的方案，附为纯文本 LLM 设计的视觉工具包&skill ｜  Let text-only models call Codex's built-in view_image seamlessly, plus a vision toolkit&skill designed for text-only LLMs.

> GitHub: [Anionex/codex-vision-proxy](https://github.com/Anionex/codex-vision-proxy) | ⭐ 214 | Python

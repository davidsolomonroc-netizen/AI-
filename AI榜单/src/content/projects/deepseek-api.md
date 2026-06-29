---
title: "DeepSeek 免费 API 代理"
description: "将 DeepSeek 聊天转为 OpenAI 兼容 API"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/sums001/Deepseek-API"
githubStars: 90
githubOwner: "sums001"
githubRepo: "Deepseek-API"
category: "dev-tools"
tags: ["deepseek", "openai-api", "free-llm", "reverse-engineered"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目将 DeepSeek 的免费聊天界面转化为 OpenAI 兼容的 API，无需 API 密钥或付费。适合想要低成本接入大模型能力的开发者、AI 应用构建者，以及需要快速原型验证的团队。"
vibeCodingPrompt: "使用 Claude Code 集成该项目的步骤：
1. 克隆仓库：git clone https://github.com/sums001/Deepseek-API.git
2. 安装依赖：pip install -r requirements.txt
3. 运行服务器：python server.py
4. 在浏览器中打开 http://localhost:8000 并用 DeepSeek 账号登录一次
5. 在代码中将 OpenAI API 端点改为 http://localhost:8000/v1，即可直接调用 DeepSeek 模型。"
pitfallGuide: "1. 依赖 DeepSeek 官方服务，可能因官方变更而失效\n2. 需要手动登录一次保存会话，非完全自动化\n3. 免费账号可能有速率限制，高并发场景需注意\n4. 逆向工程可能违反 DeepSeek 服务条款，仅限个人使用\n5. 不支持 OpenAI 的全部功能，仅兼容基础 chat completions"
targetAudience: ["独立开发者", "AI 研究者", "创业者", "技术负责人"]
useCases: ["快速原型开发与测试", "低成本构建 AI 聊天机器人", "教学与学习 LLM API 调用", "集成到现有 OpenAI 兼容工具链"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Reverse engineered Deepseek chat into an OpenAI compatible API. Access V4 and R1 models through a simple REST interface without API keys or billing.

> GitHub: [sums001/Deepseek-API](https://github.com/sums001/Deepseek-API) | ⭐ 90 | Python

---
title: "Windows Copilot API：免费LLM接口"
description: "将Microsoft Copilot转为OpenAI兼容API"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/sums001/Windows-Copilot-API"
githubStars: 316
githubOwner: "sums001"
githubRepo: "Windows-Copilot-API"
category: "other"
tags: ["copilot", "openai-api", "free-llm", "proxy"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目通过逆向工程将Microsoft Copilot的免费聊天服务封装成OpenAI兼容的API接口，无需API密钥或付费即可调用GPT-4/5模型。适合个人开发者、AI爱好者或预算有限的小团队，用于快速原型开发、AI助手集成或自动化任务，但需注意使用条款限制。"
vibeCodingPrompt: "请按照以下步骤使用Windows Copilot API搭建一个本地AI聊天后端：
1. 克隆项目并安装依赖：`git clone <repo-url>` 和 `pip install -r requirements.txt`
2. 运行服务器：`python server.py`，启动本地OpenAI兼容端点
3. 在浏览器中访问 `http://localhost:8000` 完成Microsoft账号登录
4. 使用OpenAI Python SDK连接：`client = OpenAI(base_url='http://localhost:8000/v1', api_key='none')`
5. 调用 `client.chat.completions.create(model='gpt-4', messages=[{'role':'user','content':'你好'}])` 获取回复
6. 如需流式响应，设置 `stream=True`；如需多轮对话，使用 `conversation_id` 参数"
pitfallGuide: "1. 登录会话可能过期，需定期刷新或重新登录\n2. 调用频率过高可能导致Microsoft临时限制账号\n3. 模型名称需匹配Copilot实际支持的版本，否则可能返回错误\n4. 仅适用于个人非商业用途，违反Microsoft服务条款有封号风险\n5. 部署在公网需谨慎，避免被滥用或触发安全机制"
targetAudience: ["独立开发者", "AI研究者", "创业者"]
useCases: ["快速原型开发AI聊天应用", "在受限区域免费使用GPT-4/5模型", "集成到现有自动化工作流中作为LLM后端", "个人学习与实验性AI项目"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

> GitHub: [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | ⭐ 316 | Python

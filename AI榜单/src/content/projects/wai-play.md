---
title: "WAI Play - AI 网页游戏试玩与质量评测平台"
description: "AI 自动试玩网页游戏并输出质量报告"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/waiterve/wai-play"
githubStars: 246
githubOwner: "waiterve"
githubRepo: "wai-play"
category: "workflow-automation"
tags: ["game-testing", "ai-agents", "browser-automation", "qa"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "WAI Play 能自动在真实浏览器中试玩网页游戏，识别游戏目标与流程，记录截图和录像，并生成五维质量评分、可复现的问题卡片和具体的优化建议。它特别适合用 AI 快速开发网页游戏的独立开发者或小团队，无需编写复杂测试脚本，只需提供游戏 URL（可选源码包）即可获得专业级的质量诊断，大幅降低游戏打磨和验证成本。"
vibeCodingPrompt: "请帮我用 WAI Play 搭建一个自动游戏测试工作流：
1. 克隆项目仓库并安装依赖（Python 3.12，安装 requirements.txt 和 Playwright Chromium）。
2. 复制 .env.example 为 .env，配置必要的 API 密钥（如 LLM 服务）。
3. 运行 `streamlit run app.py` 启动 Web 界面。
4. 在界面中选择游戏类型（如平台跳跃），输入你要测试的网页游戏 URL，可选上传游戏源码 ZIP 包。
5. 点击开始测试，等待 Agent 自动试玩并生成报告。
6. 查看报告中的评分、问题卡片和优化建议，根据建议修改游戏后重新测试验证。
如果需要批量测试多个游戏，可以封装脚本调用其 Python API 实现自动化。"
pitfallGuide: "需要 Python 3.12 环境，低版本可能安装依赖失败。\n首次运行需执行 `python -m playwright install chromium` 下载浏览器，否则无法启动。\n需配置有效的 LLM API 密钥（如 OpenAI），否则 Agent 无法进行游戏理解和决策。\n测试的游戏 URL 必须可公开访问，本地或需登录的游戏可能无法正常测试。\n上传源码包可提升测试准确性，但源码包过大或结构复杂时可能拖慢分析速度。"
targetAudience: ["独立开发者", "创业者", "产品经理", "AI 研究者", "技术负责人"]
useCases: ["快速验证 AI 生成的网页游戏可玩性与完成度", "在发布前对游戏进行自动化质量回归测试", "收集用户反馈前先发现并修复关键流程问题", "作为教育工具演示 AI Agent 如何理解和测试游戏"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。WAI Play - AI web game testing and quality evaluation platform

> GitHub: [waiterve/wai-play](https://github.com/waiterve/wai-play) | ⭐ 246 | Python

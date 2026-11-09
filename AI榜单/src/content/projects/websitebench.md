---
title: "WebsiteBench 网站重建评测基准"
description: "用浏览器探索反向重建全栈网站的AI基准测试"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/TIGER-AI-Lab/WebsiteBench"
githubStars: 147
githubOwner: "TIGER-AI-Lab"
githubRepo: "WebsiteBench"
category: "agent-framework"
tags: ["benchmark", "web-agents", "browser-automation", "website-reconstruction"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "WebsiteBench 是一个评测基准，用来衡量 AI 代理能否通过浏览真实网站，逆向重建出外观和功能都接近的全栈网站。它适合 AI 研究者、评测团队和想验证编码代理能力的开发者使用。"
vibeCodingPrompt: "1. 安装依赖：pip install websitebench，并安装 Docker 和 Harbor（uv tool install harbor==0.25.0）。2. 下载任务：运行 websitebench download --task medium 获取示例网站任务。3. 配置模型：设置 OPENAI_API_KEY，并选择你要测试的代理（如 codex）。4. 运行评测：使用 harbor run --dataset websitebench/WebsiteBench@v1 --agent codex --model '<model>' 启动任务，观察代理如何通过浏览器探索并重建网站。5. 查看结果：访问 leaderboard 或本地输出，对比生成网站与原网站的视觉和行为差异。"
pitfallGuide: "需要 Docker 和 Harbor 环境，非技术用户配置门槛较高
运行完整 70 个任务耗时较长，建议先用 medium 任务试跑
需要有效的 OpenAI API Key 和模型访问权限
部分任务可能依赖外部网络资源，注意网络稳定性
评测结果受模型能力影响大，建议多次运行取平均"
targetAudience: ["AI 研究者", "技术负责人", "独立开发者"]
useCases: ["评测 AI 编码代理的网站重建能力", "研究浏览器代理的探索与逆向工程能力", "对比不同 LLM 在全栈开发任务上的表现", "作为教学案例展示 AI 代理的局限性"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Can AI agents rebuild websites through browser exploration?

> GitHub: [TIGER-AI-Lab/WebsiteBench](https://github.com/TIGER-AI-Lab/WebsiteBench) | ⭐ 147 | Python

---
title: "LoopArena：循环工程控制器基准平台"
description: "基准测试模型作为循环工程运行时控制器的表现"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/AMAP-ML/LoopArena"
githubStars: 94
githubOwner: "AMAP-ML"
githubRepo: "LoopArena"
category: "other"
tags: ["benchmark", "LLM", "coding-agents", "evaluation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "LoopArena 是一个开源基准测试框架，用于评估大语言模型（LLM）在循环工程（Loop Engineering）中作为控制器（Controller）的决策能力——即模型如何引导另一个编码代理（Worker）完成长期开发任务。它适合需要构建自主编码代理系统、评估不同模型在复杂软件工程任务中协调能力的开发团队和 AI 研究者，可帮助选择最适合的模型来驱动自动化开发流程。"
vibeCodingPrompt: "在 Claude Code 中使用 LoopArena 搭建一个评估系统：
1. 首先克隆仓库：`git clone https://github.com/AMAP-ML/LoopArena.git && cd LoopArena`
2. 安装依赖：`pip install -e .`（需要 Python 3.10+）
3. 阅读 `docs/protocol.md` 了解循环工程协议和 Controller/Worker 角色定义
4. 选择一个任务配置（在 `benchmark` 目录下），或自定义一个任务，指定 Worker 代理（如 Aider）和候选 Controller 模型（如 GPT-4o）
5. 运行基准：`python -m looparena.run --task <task_id> --controller <model_name> --worker <worker_type>`
6. 运行后查看生成的评估报告，分析 Controller 的决策质量、任务完成率和效率指标
7. 若要比较多个模型，可循环运行不同 Controller，并用内置工具汇总对比结果"
pitfallGuide: "确保 Python 版本 ≥3.10，否则依赖安装失败\nController 模型需支持工具调用，旧模型可能无法正常参与基准\n运行基准前需配置好 Worker 代理（如 Aider）的环境和 API 密钥\n任务可能耗时较长，建议在稳定网络环境运行并设置超时\nREADME 中 arXiv 链接为占位符（arXiv 2608 不存在），实际论文可能未发布"
targetAudience: ["AI 研究者", "技术负责人", "独立开发者"]
useCases: ["评估不同 LLM 在自主编码循环中的决策能力", "为自动化开发系统选择最优控制器模型", "研究模型在长期软件工程任务中的协调与规划行为", "构建和优化自定义循环工程工作流"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Benchmarking models as runtime Controllers for Loop Engineering

> GitHub: [AMAP-ML/LoopArena](https://github.com/AMAP-ML/LoopArena) | ⭐ 94 | Python

---
title: "Simreal ML 研究基准"
description: "外部评分、可验证的 ML 研究智能体评估环境"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/Simreal-AI/Simreal-MLBench"
githubStars: 152
githubOwner: "Simreal-AI"
githubRepo: "Simreal-MLBench"
category: "agent-framework"
tags: ["benchmark", "llm-agents", "ml-research", "evaluation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Simreal MLBench 是一套用于评测 AI 智能体做机器学习研究能力的基准，包含 60 道横跨表格、时序、视觉、语言、音频等领域的真实竞赛任务。它帮助 AI 实验室和企业量化「AI 能不能像研究员一样独立完成建模研究」，适合模型团队、评测机构和企业 AI 部门使用。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/Simreal-AI/Simreal-MLBench，进入目录并阅读 README 与 protocol 文档。\n2. 安装依赖：pip install -r requirements.txt（或 uv sync），确认 Python 版本符合要求。\n3. 运行客户端 SDK 示例：找到 examples/ 或 client 目录，按 README 指引配置 API Key（如需官方评分路由，联系 business@simreal.co）。\n4. 选择一个 Easy 级任务（如 tabular 分类），用 SDK 加载任务定义与数据接口，编写一个最简单的 baseline agent（例如 LightGBM 默认参数）。\n5. 调用本地评分脚本对 agent 提交的 predictions 打分，理解 scoring rule 的输入输出格式。\n6. 迭代 agent：加入特征工程、交叉验证、超参搜索逻辑，对比不同版本的本地得分。\n7. 若需接入官方评分，封装一个 HTTP client 调用 Simreal 引擎的评测接口，把本地任务 ID 与提交文件上传。\n8. 用 Claude Code 辅助生成实验循环代码：让 AI 读取 protocol 文档后自动生成 agent 的 train/evaluate/submit 三段式模板，再手动接入数据路径。"
pitfallGuide: "仓库只是公开预览版，官方评分引擎和完整套件不在开源范围内，不要指望本地跑出权威分数\n任务预算从 6 到 24 小时不等，Hard 级需要 GPU，个人笔记本跑不动\n评分协议公开但运行时闭源，接入官方评分需要联系商务邮箱获取访问权限\n项目处于早期阶段，API 和目录结构可能随时变动，锁定 commit 再开发\nagent 提交格式（predictions 文件结构）必须严格符合 protocol，否则本地评分会报错"
targetAudience: ["AI 研究者", "技术负责人", "企业团队"]
useCases: ["评测自研 LLM agent 的端到端 ML 研究能力", "构建 RL 环境训练具备科研能力的智能体", "对标不同模型在真实竞赛任务上的表现", "企业内部 AI 团队做模型选型与能力基线测试"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。[Public preview] Externally scored agentic ML research benchmark: 60 tasks, real competition ground truth. Open protocol, operated evaluation.

> GitHub: [Simreal-AI/Simreal-MLBench](https://github.com/Simreal-AI/Simreal-MLBench) | ⭐ 152 | Python

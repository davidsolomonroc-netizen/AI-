---
title: "AnyJev 决策概率化引擎"
description: "把任意 LLM 变成带真实概率的决策模型"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/nokia-applied-research/AnyJev"
githubStars: 859
githubOwner: "nokia-applied-research"
githubRepo: "AnyJev"
category: "dev-tools"
tags: ["LLM", "Calibration", "Decision-Model", "vLLM"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "AnyJev 让普通大模型输出可量化、可校准的决策概率，无需训练或微调，就能把「模型随口一说」变成「有风险等级的判断」。适合需要自动化决策（如意图分类、风控、A/B 判定）且对概率可靠性有要求的产品团队与数据科学家。"
vibeCodingPrompt: "1. 用 `pip install anyjev` 安装，并确认本地有可调用的 LLM 服务（如 vLLM 或 OpenAI 兼容接口）。
2. 在 Claude Code 中新建 Python 脚本，导入 AnyJev，按文档初始化一个 Jev 决策器，指定模型名与后端地址。
3. 定义你的决策类别（例如 BANKING77 意图标签），调用 `decide()` 获取带概率的 typed 决策结果。
4. 若手上有少量标注数据（100~500 条），运行内置校准流程，降低 calibration error 并输出风险阈值。
5. 用 FastAPI 包一个 `/decide` 接口，把概率和自动可判定标记返回给前端或下游系统。
6. 加入单元测试：对同一输入交换选项顺序，验证 order-flip 率是否明显下降。"
pitfallGuide: "需先有可用的 LLM 推理后端（vLLM 或兼容 API），纯离线跑不通
无标注时校准效果有限，建议准备 100~500 条标注数据再上生产
概率阈值需按业务风险偏好调整，不要直接照搬默认值
vLLM 部署方式与传统推理不同，需确认 pooler 返回 hidden state
项目仍在持续更新，接口可能变动，锁版本并关注 issue"
targetAudience: ["AI 研究者", "数据分析师", "技术负责人", "独立开发者"]
useCases: ["客服意图分类与自动分流", "风控/合规场景的概率化决策", "LLM 输出可靠性评估与校准", "低标注成本下的自动决策系统搭建"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Turn any LLM into a Jev-style decision model: typed decisions, real probabilities, no training. (continue updating, welcome any issue and PR request)

> GitHub: [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) | ⭐ 859 | Python

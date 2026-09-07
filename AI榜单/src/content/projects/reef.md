---
title: "珊瑚礁：智能体持续学习基础设施"
description: "让AI代理从交互中持续自我提升的基础设施"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/Human-Agent-Society/reef"
githubStars: 607
githubOwner: "Human-Agent-Society"
githubRepo: "reef"
category: "agent-framework"
tags: ["continual-learning", "self-improving", "agent-infra", "reinforcement-learning"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "Reef是首个开源的持续自我改进智能体基础设施，它将智能体的推理、反馈、学习和版本化交付连接起来。业务上，它能让你的AI代理（如客服机器人、编程助手）通过分析用户交互反馈，自动优化模型权重或改进提示词与规则，从而越用越聪明。适合希望构建长期进化型AI产品的团队，尤其是那些已有基础模型和GPU资源，或希望通过纯提示工程优化智能体行为的组织。"
vibeCodingPrompt: "请帮我用 Reef 搭建一个能持续自我改进的客户支持智能体。步骤：1) 运行 `pip install reef-infra` 安装库。2) 参照官方快速开始文档，初始化一个 Reef 项目，配置基础模型端点（如 OpenAI 或本地 SGLang）。3) 定义你的支持任务场景（如退款、产品咨询），并创建一组代表性测试用例作为评估器。4) 接入你的客户交互日志作为反馈源，设置反馈提取逻辑（如用户满意度评分或问题是否解决）。5) 选择优化模式：若无训练GPU，用 'harness optimization' 模式让 Reef 自动迭代你的系统提示词和工具规则；若有GPU，配置 Slime 进行模型权重微调。6) 运行 Reef 训练循环，并观察每次迭代后测试用例通过率提升。7) 将改进后的智能体版本部署到生产，持续收集新反馈，形成闭环。"
pitfallGuide: "需要明确区分两种学习路径：模型权重训练需GPU，提示词优化则不需要，选错会浪费资源\n反馈数据的质量直接影响学习效果，需设计清晰的反馈信号（如用户评分）\n项目较新（607星），社区和文档仍在完善，需关注GitHub issues和Discord获取支持\n部署门槛较高，非技术用户难以在10分钟内跑通，需具备Python和AI基础\n确保你的基础模型和GPU栈与Reef兼容（如支持Slime和SGLang），否则需额外适配"
targetAudience: ["AI研究者", "技术负责人", "创业者", "企业团队"]
useCases: ["构建持续进化的客服机器人，通过用户反馈自动优化回复策略", "开发自改进的编程助手，根据代码审查结果调整提示词和工具使用", "用于强化学习研究，探索智能体在真实交互环境中的持续学习机制", "企业内部知识助手，根据员工使用反馈自动更新规则和技能库"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Continual learning infra for self-improving agents

> GitHub: [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | ⭐ 607 | Python

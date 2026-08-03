---
title: "波洛特深度研究智能体内核"
description: "带长期记忆的深度研究智能体内核"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/HezaoHezao/poirot"
githubStars: 103
githubOwner: "HezaoHezao"
githubRepo: "poirot"
category: "agent-framework"
tags: ["deep-research", "memory-system", "multi-agent", "langgraph"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "Poirot 是一个面向深度研究场景的智能体内核，强调架构的可解释性和模块化，适合需要构建可定制、可扩展研究代理的团队。它内置了五层长期记忆系统和多智能体编排能力，能自动执行复杂的信息搜集与分析任务，减少人工调研成本。对于重视 AI 代理架构设计的技术团队和研究者来说，这是一个高价值的开源基础。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone https://github.com/HezaoHezao/poirot && cd poirot && pip install -e .\n2. 设置环境变量：export OPENAI_API_KEY=sk-xxx（或修改为 DeepSeek 等兼容 API）\n3. 阅读 USAGE.md 或 resource/USAGE.zh-CN.md 了解基本配置\n4. 使用 Claude Code 打开项目，让它阅读核心模块代码（如 leader_agent.py 和 memory/）\n5. 让 Claude Code 帮你写一个简单的调用脚本：初始化 LeaderAgent，配置记忆层，运行一个研究任务\n6. 根据你的需求修改中间件或技能层，例如添加自定义工具或调整记忆策略\n7. 利用项目的 2400+ 测试用例作为参考，让 Claude Code 生成新的测试并验证改动"
pitfallGuide: "需要 Python 3.12+ 和 LangGraph 依赖，环境配置稍复杂\n默认使用 DeepSeek 模型，需自行配置 API Key，非开箱即用\n项目文档部分为英文和中文，需仔细阅读 USAGE 文档才能正确配置\n作为内核框架，不适合非技术用户直接使用，需要一定开发能力\n多智能体编排和记忆系统配置较为复杂，建议先运行示例再修改"
targetAudience: ["AI 研究者", "技术负责人", "独立开发者", "企业团队"]
useCases: ["构建企业级深度研究助手，自动搜集行业报告和竞品信息", "开发具有长期记忆的个性化知识管理代理", "研究多智能体协作和记忆架构的实验平台", "为垂直领域（如法律、医疗）定制研究型智能体"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Poirot is a deep research agent kernel built for those who care about how agents are architected. 

> GitHub: [HezaoHezao/poirot](https://github.com/HezaoHezao/poirot) | ⭐ 103 | Python

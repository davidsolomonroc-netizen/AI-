---
title: "GBase — 自我进化智能体框架"
description: "让AI智能体拥有记忆与自我进化能力。"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/garyqlin/gbase"
githubStars: 103
githubOwner: "garyqlin"
githubRepo: "gbase"
category: "agent-framework"
tags: ["self-improvement", "memory", "cognitive-architecture", "python"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "GBase是一个让AI智能体具备长期记忆、反思和自动进化能力的框架。它适合希望构建能持续学习、自我优化的AI助手或自动化代理的开发团队，尤其适用于需要长期稳定运行的项目。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/garyqlin/gbase.git
2. 创建虚拟环境并安装依赖：cd gbase && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
3. 设置环境变量（如OPENAI_API_KEY），运行示例脚本：python examples/simple_agent.py
4. 在主脚本中调用agent.full_evolution_cycle()触发自我进化。
5. 如需集成到Claude Code，导入gbase模块并实例化GBaseAgent，传入任务描述即可。"
pitfallGuide: "1. 框架依赖外部LLM API，请确保API密钥配置正确且具备足够额度。\n2. 镜像记忆功能需要额外的向量数据库支持（如Chroma），默认未启用，需手动配置。\n3. 递归自我进化循环可能消耗较多API调用和Token，建议设置调用上限或预算控制。\n4. 项目仍处于早期阶段，文档和示例可能不够完善，需参考源码调试。"
targetAudience: ["AI研究者", "独立开发者", "技术负责人"]
useCases: ["构建长期记忆的客服机器人", "开发持续自我优化的代码助手", "创建自动化研究助手", "搭建可进化的游戏NPC"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。GBase — Recursive Self-Improvement Agent Framework. Memory, evolution, quality gates, identity system, and 40+ auto-registered tools.

> GitHub: [garyqlin/gbase](https://github.com/garyqlin/gbase) | ⭐ 103 | Python

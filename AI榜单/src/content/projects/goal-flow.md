---
title: "GoalFlow：图编排智能体框架"
description: "可视化与代码双驱的LangGraph生产级智能体框架"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/wanmol/goal-flow"
githubStars: 72
githubOwner: "wanmol"
githubRepo: "goal-flow"
category: "agent-framework"
tags: ["langgraph", "agent", "dify", "workflow"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "GoalFlow 让你既能用拖拽界面（Dify）设计工作流，又能用代码构建智能体，并将两者无缝结合。它适合需要快速搭建生产级AI应用、又不想被单一平台锁定的团队，尤其适合已有Dify使用经验或需要复杂人机协作流程的企业。"
vibeCodingPrompt: "使用 GoalFlow 构建一个客户支持智能体：
1. 首先，运行 `pip install goal-flow` 或克隆仓库。
2. 在 Dify 中设计一个包含意图识别、知识库检索、人工转接的工作流，导出 DSL 文件。
3. 使用 `goalflow transpile your_flow.dsl -o support_agent.py` 将 DSL 转换为 LangGraph 代码。
4. 在生成的 Python 文件中，使用 `agent_kit` 添加一个 ReAct 智能体节点，用于处理复杂查询。
5. 配置模型路由和故障转移（例如，主用 GPT-4，备用 Claude）。
6. 运行 `python support_agent.py` 启动服务，并集成到你的聊天前端。"
pitfallGuide: "确保在公开仓库前清除 git 历史中的 .env 凭据，使用 git filter-repo 清洗并轮换密钥。\n项目仍处于早期阶段（星数较少），API 可能不稳定，升级前需检查更新日志。\n内部服务 URL 可能硬编码在部分代码中，部署前需替换为你的环境变量。\nDify 转译功能可能不支持所有节点类型，复杂流程需手动调整生成的代码。\n流式处理依赖异步 I/O，确保你的运行环境支持 asyncio 和 websocket。"
targetAudience: ["技术负责人", "AI 研究者", "独立开发者", "企业团队"]
useCases: ["将现有 Dify 工作流迁移到自托管 LangGraph 环境", "构建需要人工审批或动态决策的客服/运维智能体", "快速原型验证多智能体协作场景，并平滑过渡到生产"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Graph-Orchestrated Agent Loop — a production-grade framework on LangGraph. Combine workflow graphs and agent loops, transpile Dify DSL to runnable code, swap wire protocols (Dify/OpenAI).

> GitHub: [wanmol/goal-flow](https://github.com/wanmol/goal-flow) | ⭐ 72 | Python

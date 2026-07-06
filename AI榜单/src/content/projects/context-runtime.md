---
title: "LLM上下文查询优化引擎"
description: "像SQL优化器一样规划AI上下文"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/redevops-io/context-runtime"
githubStars: 88
githubOwner: "redevops-io"
githubRepo: "context-runtime"
category: "agent-framework"
tags: ["context-engineering", "llmops", "query-planner", "optimization"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Context Runtime为AI应用自动选择最佳上下文，通过强化学习优化每次查询的成本与效果。适合需要高效调用LLM的企业团队，可显著提升回复质量并降低API费用。"
vibeCodingPrompt: "1. 克隆仓库: git clone https://github.com/redevops-io/context-runtime.git\n2. 安装依赖: pip install -r requirements.txt\n3. 选择一个示例租户（如sidekick），运行: python examples/sidekick.py\n4. 查看输出中的learned-vs-baseline reward对比\n5. 修改config.yaml中的参数（如pool、limit）并重新运行观察效果\n6. 集成到自己的应用：导入ContextRuntime类，包装你的检索或决策函数"
pitfallGuide: "1. 需要先定义清晰的奖励函数（如用户接受率）才能学习\n2. 离线训练需要历史数据，冷启动阶段效果可能不如默认策略\n3. 多租户场景下每个租户的配置独立，需分别调参\n4. 目前主要支持Python，Golang集成需额外开发"
targetAudience: ["企业团队", "AI研究者", "技术负责人"]
useCases: ["为企业聊天机器人优化检索上下文以提升准确率", "在SOC中自动选择威胁情报源减少误报", "在营销系统中动态调整归因窗口提升ROI"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Context Runtime — a database query planner for LLM context. Decides what a model sees before it answers; plans it, runs it through reused substrate, and learns from the outcome.

> GitHub: [redevops-io/context-runtime](https://github.com/redevops-io/context-runtime) | ⭐ 88 | Python

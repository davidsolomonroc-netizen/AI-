---
title: "Bindwidth - 本地LLM部署规模估算器"
description: "精准计算私有AI部署硬件需求与成本"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/juxhinr/bindwidth"
githubStars: 138
githubOwner: "juxhinr"
githubRepo: "bindwidth"
category: "data-analysis"
tags: ["llm-sizing", "tco-calculator", "on-premise", "infrastructure"]
editorialScore: 4
deploymentRating: 5
vibeCodingRating: 4
commercialSummary: "Bindwidth是一个前端计算器，帮助企业和个人在部署本地LLM前，准确估算所需的GPU/内存等硬件配置及总拥有成本。它通过分析KV缓存、服务容量和会话上限三大约束，找出真正的性能瓶颈，避免过度或不足配置。适合需要私有化部署AI模型的技术决策者、IT架构师和云服务提供商。"
vibeCodingPrompt: "1. 打开项目GitHub页面，阅读README了解核心功能。\n2. 使用Claude Code克隆仓库到本地：`git clone https://github.com/juxhinr/bindwidth.git`。\n3. 项目无构建步骤，直接打开`index.html`即可在浏览器运行。\n4. 若要集成到现有网站，可复制静态文件到你的项目目录，并调整表单提交逻辑。\n5. 如需定制模型参数或成本计算规则，修改`js/`目录下的数据文件（如模型列表、价格表）。\n6. 运行本地服务器测试：`python -m http.server 8000`，访问`http://localhost:8000`。"
pitfallGuide: "1. 项目依赖外部API获取实时价格，若网络受限可能影响计算准确性。\n2. 计算基于预设模型库，新模型需手动添加参数。\n3. 无后端存储，用户配置不会自动保存，需手动导出/导入。\n4. 对于超大规模集群（100+ GPU），估算结果可能过于简化。\n5. 仅支持英文界面，非英文用户需自行翻译。"
targetAudience: ["技术负责人", "企业团队", "独立开发者", "创业者", "AI研究者"]
useCases: ["私有化LLM部署前的硬件采购规划", "比较公有云与本地部署的TCO", "为项目选择最经济的GPU型号", "快速评估现有基础设施能否支持新模型"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Evidence-aware on-prem LLM inference sizing and TCO calculator

> GitHub: [juxhinr/bindwidth](https://github.com/juxhinr/bindwidth) | ⭐ 138 | JavaScript

---
title: "开放科学工作台"
description: "本地优先的AI科研助手"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/ai4s-research/open-science"
githubStars: 166
githubOwner: "ai4s-research"
githubRepo: "open-science"
category: "workflow-automation"
tags: ["scientific-research", "local-first", "reproducible", "ai-agent"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个面向科研人员的开源AI工作台，替代Claude Science等商业产品。它支持本地运行、多模型接入，帮助科学家将文献、代码、图表、报告和评审整合为可审计的重复性工作流，特别适合需要严格复现和隐私保护的学术研究团队。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone https://github.com/ai4s-research/open-science.git && cd open-science && npm install\n2. 配置你的LLM API密钥（如OpenAI/Claude）到.env文件\n3. 启动应用：npm run tauri dev\n4. 在界面中创建新项目，导入文献或数据\n5. 使用内置的\"计划→审批→执行→产出\"工作流运行分析\n6. 所有步骤自动记录，可导出为可复现报告"
pitfallGuide: "1. 首次运行需要配置LLM API密钥，否则核心功能不可用\n2. 本地模型（如Llama）需自行下载，路径配置可能复杂\n3. 当前为v0.1版本，部分工作流模板可能不完善\n4. Windows用户需确保安装WebView2运行时\n5. 大型文献库导入时可能较慢，建议分批处理"
targetAudience: ["AI研究者", "数据分析师", "企业团队", "产品经理"]
useCases: ["科研文献综述与元分析自动化", "实验数据流水线记录与复现", "跨团队协作的科研项目管理", "学术论文图表生成与结果校验"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open Science — an open AI workbench for scientists. Open-source alternative to Claude Science: local-first, model-agnostic, reproducible AI research desktop (macOS & Windows), built on Tauri + MCP + agent skills.

> GitHub: [ai4s-research/open-science](https://github.com/ai4s-research/open-science) | ⭐ 166 | TypeScript

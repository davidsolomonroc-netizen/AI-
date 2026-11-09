---
title: "CoworkOS 协作智能体工作台"
description: "面向长周期人机协作任务的开源智能体执行框架"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/RUC-NLPIR/CoworkOS"
githubStars: 147
githubOwner: "RUC-NLPIR"
githubRepo: "CoworkOS"
category: "agent-framework"
tags: ["agent", "human-in-the-loop", "long-horizon", "workflow"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "CoworkOS 让人类与 AI 智能体在同一工作区协作推进复杂项目，覆盖代码、研究、文档、演示、CAD 和科学计算等场景。它适合需要长周期、可监控、可回溯地完成多步骤任务的团队，尤其是希望把 AI 助手嵌入真实业务流程的企业和独立开发者。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone https://github.com/RUC-NLPIR/CoworkOS && cd CoworkOS && npm install。2. 阅读 docs/en/README.md 了解三层运行时结构和配置方式。3. 在项目根目录创建 .env 文件，按文档配置模型服务（如 OpenAI 或本地模型）和工作区路径。4. 启动开发服务器：npm run dev，打开本地地址进入桌面工作区。5. 新建一个 Job，选择任务类型（如文档生成或代码分析），输入目标并上传相关文件。6. 在 Job 运行过程中，通过界面查看状态和日志，在需要决策时人工介入修改。7. 任务完成后检查生成的产物，如需调整可继续对话或重新运行。8. 将常用配置固化到模板中，方便后续复用。"
pitfallGuide: "需要 Node.js 环境和 npm，非技术用户可能卡在环境配置上
模型服务需要自行提供 API Key 或本地部署，有额外成本
项目较新（147 星），文档和社区支持可能不完善
长周期任务依赖稳定的网络和存储，中断恢复需验证
部分高级功能（CAD、Blender）可能需要额外依赖"
targetAudience: ["独立开发者", "企业团队", "AI 研究者", "技术负责人"]
useCases: ["多步骤研究项目的人机协作推进", "长周期文档或演示文稿的迭代生成", "代码分析与修复任务的监控执行", "科学计算或 CAD 工作流的半自动化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。CoworkOS: a cowork harness for long-horizon and human-in-the-loop task execution

> GitHub: [RUC-NLPIR/CoworkOS](https://github.com/RUC-NLPIR/CoworkOS) | ⭐ 147 | JavaScript

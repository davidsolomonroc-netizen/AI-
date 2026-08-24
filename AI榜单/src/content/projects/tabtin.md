---
title: "TabTin：人与 AI 智能体协作工作台"
description: "团队与多 AI 代理协同工作的开源平台"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/tabtin-ai/TabTin"
githubStars: 115
githubOwner: "tabtin-ai"
githubRepo: "TabTin"
category: "workflow-automation"
tags: ["agents", "collaboration", "workspace", "desktop"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "TabTin 是一个开源的人与 AI 智能体协作平台，帮助团队将 AI 代理融入真实工作流程，解决个人使用 AI 后团队效率未提升的问题。它支持任务交接、上下文冻结、文档/表格等协作应用，以及团队方法复用，适合深度使用 AI 的团队和个人。非技术用户可直接使用官方托管服务，也可自行部署社区版。"
vibeCodingPrompt: "1. 克隆项目：`git clone https://github.com/tabtin-ai/TabTin.git`，进入目录。\n2. 阅读 README 和 CONTRIBUTING.md，了解架构和配置。\n3. 运行社区版服务端：按文档启动后端（可能需要 Docker 或 Node.js），确保依赖安装。\n4. 配置你的 Agent 角色：在配置文件中定义模型、Skill 和执行规则，例如创建一个调研 Agent。\n5. 启动客户端，创建 Workspace，添加 Agent，并开始一个任务（如“收集行业报告”）。\n6. 利用任务交接功能，将上下文和结果共享给团队成员，验证协作流程。"
pitfallGuide: "1. 项目处于 Public Preview，组件成熟度不一，生产环境需谨慎评估。\n2. 自行部署社区版需要一定技术背景，非技术用户建议使用官方托管服务。\n3. 任务交接依赖权限配置，确保共享文档和文件时设置正确权限。\n4. 不同 Agent 的模型和 Skill 配置需仔细测试，避免上下文丢失或 Token 浪费。\n5. 本地文件与执行环境相互独立，交接时需明确哪些内容被冻结和共享。"
targetAudience: ["独立开发者", "创业者", "产品经理", "企业团队", "技术负责人"]
useCases: ["团队调研任务交接：成员完成调研后，将上下文和结果共享给下一位同事，避免重复工作", "AI 辅助文档与表格协作：Agent 直接创建和编辑在线文档，减少文件搬运", "团队方法复用：将验证过的调研流程、Review 规则配置为可复用的 Agent 角色", "跨工具工作流集成：结合浏览器采集数据和本地文件，统一在 TabTin 工作区处理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A workspace where people and multiple AI agents work together.

> GitHub: [tabtin-ai/TabTin](https://github.com/tabtin-ai/TabTin) | ⭐ 115 | TypeScript

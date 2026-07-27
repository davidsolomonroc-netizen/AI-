---
title: "可信任的智能体工作流"
description: "带人类审批的AI代理协作编排"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/cocofhu/approving"
githubStars: 73
githubOwner: "cocofhu"
githubRepo: "approving"
category: "workflow-automation"
tags: ["agent", "workflow", "human-in-the-loop", "sandbox"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Approving 是一个开源的多智能体协作框架，通过可视化编排和沙箱执行，让AI代理在关键节点等待人工审批后再继续。适合需要高可靠性和审计追踪的企业团队，用于自动化复杂业务流程。"
vibeCodingPrompt: "1. 克隆仓库并运行 docker-compose up 启动服务。
2. 在浏览器打开 http://localhost:3000，使用可视化编辑器拖拽创建代理工作流。
3. 在每个关键决策节点添加 'Approve' 步骤，设置审批人。
4. 运行工作流，观察代理在沙箱中执行任务并等待人工确认。
5. 利用回滚功能在出错时恢复至任意历史状态。"
pitfallGuide: "1. 确保 Docker 和 Docker Compose 已安装，否则无法一键启动。\n2. 审批节点需配置有效通知渠道（如邮件/Webhook），否则会卡住。\n3. 沙箱资源有限，长时间运行任务需调整资源限制。\n4. 多代理协作时注意任务依赖顺序，避免死循环。\n5. 数据持久化依赖外部数据库，首次启动需初始化 schema。"
targetAudience: ["企业团队", "技术负责人", "创业者", "产品经理"]
useCases: ["自动化审批流程（如合同审核、代码部署审批）", "多步骤数据处理流水线（需人工质检）", "AI辅助决策系统（如投资建议、合规检查）", "DevOps管道中的人工门控（安全发布）"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Compose coding agents into workflows you can trust

> GitHub: [cocofhu/approving](https://github.com/cocofhu/approving) | ⭐ 73 | Go

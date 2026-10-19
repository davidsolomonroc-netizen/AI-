---
title: "TransWork 企业级桌面 AI Agent 工作台"
description: "让技能、知识与数字员工在同一处协作"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/shuyu-labs/transwork"
githubStars: 114
githubOwner: "shuyu-labs"
githubRepo: "transwork"
category: "agent-framework"
tags: ["agent", "desktop", "enterprise", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "TransWork 是一个可私有部署的企业级 AI Agent 工作台，把技能包、知识库和数字员工集中管理，让团队无需各自配置模型密钥就能协作使用 AI。它适合希望数据自主可控、需要统一管控 AI 使用的中小团队和企业 IT 部门。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/shuyu-labs/transwork.git && cd transwork；2. 执行 docker compose up -d 启动所有服务，等待约 1 分钟初始化完成；3. 访问 http://localhost:3000/admin，用 admin / TransWork_Admin_2026 登录管理后台；4. 在「模型与系统」中配置你的模型 API Key（如 OpenAI 或本地模型）；5. 在「用户管理」中创建团队成员账号；6. 在「技能市场」上传或选择技能包，在「数字员工」中配置 Agent 并授权给角色；7. 下载桌面客户端，在登录页设置服务器地址为 http://localhost:3000/，用创建的账号登录即可使用技能、知识和数字员工。"
pitfallGuide: "需要 Linux x86_64 服务器或 WSL2，Windows/macOS 直接运行可能遇到兼容问题
首次启动需等待 pgvector 初始化和演示数据导入，约 1 分钟，期间访问会报错
演示管理员账号仅用于预览，正式使用前务必修改默认密码并创建独立用户
免费授权仅 5 席位，团队超过 5 人需购买 License 扩容
模型密钥在管理后台集中配置，不要泄露给终端用户，避免安全风险"
targetAudience: ["企业团队", "技术负责人", "产品经理", "创业者"]
useCases: ["企业内部 AI 助手统一管理", "团队知识库与技能共享", "私有化部署的 AI Agent 工作台", "多角色权限管控的 AI 应用分发"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。企业级桌面 AI Agent 工作台，让技能、知识与任务在同一处协作。

> GitHub: [shuyu-labs/transwork](https://github.com/shuyu-labs/transwork) | ⭐ 114 | 多种语言

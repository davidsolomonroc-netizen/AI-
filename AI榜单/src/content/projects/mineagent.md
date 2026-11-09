---
title: "MineAgent 画布编排器"
description: "浏览器画布搭 Agent，一键编译运行"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/YT-Proteus-bot/MineAgent"
githubStars: 111
githubOwner: "YT-Proteus-bot"
githubRepo: "MineAgent"
category: "agent-framework"
tags: ["agent-orchestration", "visual-canvas", "code-generation", "workflow"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "MineAgent 让不懂代码的人也能在浏览器里用拖拽画布的方式搭建 AI Agent 工作流，选好框架后自动生成可独立运行的 Python 项目并直接执行。适合想快速验证 Agent 想法但又不想手写代码的创业者、产品经理和企业团队。"
vibeCodingPrompt: "1. 克隆项目并运行 start.bat 启动服务，访问 http://127.0.0.1:8000。2. 在画布上右键添加节点，搭建一个简单的客服问答 Agent：输入节点 → 意图识别 → 知识检索 → 回复生成。3. 选中每个节点，在属性面板配置模型和参数，并可直接编辑节点对应的 Python 代码。4. 点击顶部“保存”，项目会自动生成到 projects/<画布名>/ 目录。5. 点击“运行”，观察节点实时高亮和流式输出，验证流程。6. 如需无 API Key 测试，另开终端运行 tools/mock_llm.py，并在模型配置中填入 mock 地址。"
pitfallGuide: "首次启动需安装 Python 和 Node.js 依赖，耗时可能超过 10 分钟。\n没有 API Key 时需手动启动 mock LLM 服务才能跑通全流程。\n画布节点较多时编译和运行可能较慢，建议分模块搭建。\n生成的项目依赖 Python 环境，部署到其他机器需重新安装依赖。\n社区模板功能需要 GitHub 账号和网络访问。"
targetAudience: ["独立开发者", "创业者", "产品经理", "企业团队"]
useCases: ["快速搭建客服问答 Agent 原型", "企业内部流程自动化编排", "教学演示 Agent 工作原理", "低代码生成可部署的 Agent 项目"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。agent定制自由化，agent流程可视化。在浏览器里用画布搭出工业级 Agent 流程，选框架自动生成架构图， 拖节点、连线、写代码、配模型，点「保存」就把整张画布编译成一个可独立运行的 Python Agent 项目， 点「运行」直接在你的机器上真实执行并流式回传每一步。欢迎各位同行二次开发，如有商用请说明出处。

> GitHub: [YT-Proteus-bot/MineAgent](https://github.com/YT-Proteus-bot/MineAgent) | ⭐ 111 | Python

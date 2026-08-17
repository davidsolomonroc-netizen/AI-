---
title: "OAK：端侧AI代理内核"
description: "100%设备端运行的AI代理框架，毫秒级响应"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/OpenSparX/MasterAgent"
githubStars: 344
githubOwner: "OpenSparX"
githubRepo: "MasterAgent"
category: "agent-framework"
tags: ["edge-ai", "npu", "on-device", "automotive"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OAK让AI代理完全在本地设备上运行，无需云端，适合对隐私和延迟敏感的场景，如车载助手、工业IoT。它通过模式匹配和本地LLM推理实现亚100毫秒响应，并针对高通NPU优化，功耗更低。适合需要边缘智能的开发者或企业团队。"
vibeCodingPrompt: "1. 安装CLI：npm install -g @sparx/cli。\n2. 运行示例：sparx demo automotive，了解基本流程。\n3. 创建自定义代理：使用sparx init myagent，然后在生成的配置中定义技能和MCP端点。\n4. 集成到应用：在代码中调用代理API，传入用户输入，获取意图和响应。\n5. 部署到NPU：按照文档将模型和代理打包，部署到Qualcomm设备。"
pitfallGuide: "确保硬件支持NPU，否则性能下降。\n模式匹配覆盖有限，复杂请求需本地LLM，需提前配置模型。\n设备端存储加密需管理设备密钥，注意密钥安全。\n安装CLI可能需要Node.js环境，非技术用户需先配置。\n文档以英文为主，中文支持有限，需参考英文文档。"
targetAudience: ["独立开发者", "技术负责人", "企业团队", "AI研究者"]
useCases: ["车载语音助手（如控制空调、导航）", "工厂设备本地智能监控与预警", "隐私敏感的医疗或金融边缘应用", "离线环境下的智能家居控制"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Build AI agents that run 100% on-device. Sub-100ms latency on Qualcomm NPU. Zero cloud dependency.

> GitHub: [OpenSparX/MasterAgent](https://github.com/OpenSparX/MasterAgent) | ⭐ 344 | C++

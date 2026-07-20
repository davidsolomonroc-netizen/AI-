---
title: "LLM安全训练靶场"
description: "针对OWASP LLM Top 10的攻防训练平台"
publishDate: 2026-07-20
featured: false
githubUrl: "https://github.com/CyberSunil/LLMVault"
githubStars: 203
githubOwner: "CyberSunil"
githubRepo: "LLMVault"
category: "other"
tags: ["AI Security", "Training", "CTF", "Penetration Testing"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个专为AI安全学习设计的开源训练平台，包含25个故意存在漏洞的实验室，覆盖提示注入、RAG安全、Agent安全等OWASP LLM Top 10攻击场景。适合安全研究员、红队成员以及希望提升AI应用安全能力的开发者，通过实战攻防学习防御方法。"
vibeCodingPrompt: "1. 克隆项目并按照README中的Docker部署说明启动环境。\n2. 进入第一个实验室，阅读场景描述，尝试通过修改prompt实现注入攻击。\n3. 使用Claude分析攻击成功的原因，并参考配套的解决方案指南学习对应的防御措施。\n4. 依次完成25个实验室，记录每个漏洞的利用方法和修复建议。"
pitfallGuide: "1. 切勿将该项目暴露在公网，它本身就是故意有漏洞的。\n2. 运行前确保Docker已正确安装，并分配足够内存（至少4GB）。\n3. 部分高级实验室需要多轮交互，注意保存攻击链。\n4. 防御方案在私有分支中，需自行查阅或向维护者申请。"
targetAudience: ["AI研究者", "安全研究员", "红队成员", "技术负责人"]
useCases: ["企业内部AI安全培训", "红蓝对抗演练", "CTF竞赛训练", "AI应用安全评估"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.

> GitHub: [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault) | ⭐ 203 | Python

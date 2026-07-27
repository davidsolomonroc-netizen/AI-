---
title: "集体智能引擎"
description: "数万AI模型协作的集体智能系统"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/ailinone/collective-intelligence"
githubStars: 123
githubOwner: "ailinone"
githubRepo: "collective-intelligence"
category: "agent-framework"
tags: ["multi-agent", "consensus", "orchestration", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Ailin¹ 是一个开源集体智能引擎，能让数十种AI模型通过多种协调策略协作，提升可靠性和鲁棒性。适合需要高可信AI决策的企业团队或研究者，尤其适用于需要多方验证的复杂分析场景。"
vibeCodingPrompt: "1. 克隆仓库并进入目录
2. 运行 `docker compose up -d` 启动服务
3. 配置多个AI模型API密钥（如OpenAI、Claude等）
4. 使用OpenAI兼容客户端连接到 `http://localhost:8080/v1`
5. 发送请求时指定协调策略参数，例如 `strategy=consensus` 或 `strategy=debate`
6. 观察多个模型协作返回的聚合结果"
pitfallGuide: "1. 需要至少配置2个以上不同模型API密钥才能发挥集体智能效果\n2. Docker环境需提前安装，且注意端口8080是否被占用\n3. 协调策略（如共识、辩论）会增加延迟，不适合实时场景\n4. 免费层API可能有速率限制，建议使用付费账户\n5. 项目处于早期阶段，文档和错误处理可能不完善"
targetAudience: ["AI研究者", "企业团队", "技术负责人"]
useCases: ["高可靠性AI决策（如金融风控）", "多模型交叉验证分析", "复杂推理与辩论式问答"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Ailin¹ is an open-source collective intelligence engine where tens of thousands of AI models collaborate through dozens of coordination strategies, applying structured diversity and independent reasoning to improve reliability, auditability, and resilience.

> GitHub: [ailinone/collective-intelligence](https://github.com/ailinone/collective-intelligence) | ⭐ 123 | TypeScript

---
title: "开源·Kritt"
description: "编排AI代理发现代码真实漏洞"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/Kritt-ai/open-kritt"
githubStars: 420
githubOwner: "Kritt-ai"
githubRepo: "open-kritt"
category: "agent-framework"
tags: ["security", "agent", "bugbounty", "workflow-automation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "open·kritt 是一个开源自托管的安全研究平台，通过将代码分析拆解为小任务，并行调度AI代理（如Claude Code）来发现并验证真实漏洞。适合安全研究员、漏洞赏金猎人和注重安全性的开发者，用于自动化代码审计和漏洞优先级排序。"
vibeCodingPrompt: "1. 克隆仓库: git clone https://github.com/Kritt-ai/open-kritt.git
2. 进入目录: cd open-kritt
3. 安装依赖: npm install
4. 配置环境变量: 复制 .env.example 为 .env，填入你的AI API密钥（如Anthropic或OpenAI）
5. 启动服务: npm run dev
6. 打开浏览器访问 http://localhost:3000，创建新工作流并添加分析任务
7. 输入目标仓库URL或上传代码，运行扫描并查看结果"
pitfallGuide: "需要配置AI API密钥，首次使用需注册对应服务商\n工作流设计需理解安全分析流程，非零基础工具\n自托管部署需一定运维知识，建议使用Docker\n结果准确性依赖模型质量，建议先用小项目测试\n社区文档尚在完善，复杂问题可能需要查阅Discord"
targetAudience: ["安全研究员", "漏洞赏金猎人", "技术负责人", "企业安全团队"]
useCases: ["自动化代码安全审计", "漏洞赏金计划中的快速扫描", "CI/CD流水线集成安全检测", "开源项目依赖漏洞分析"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Orchestrate AI agents to find real vulnerabilities in code.

> GitHub: [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | ⭐ 420 | JavaScript

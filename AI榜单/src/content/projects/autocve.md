---
title: "AutoCVE - 一键自动化CVE挖掘平台"
description: "Agent驱动的自动化CVE发现与报告生成"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/larlarua/AutoCVE"
githubStars: 221
githubOwner: "larlarua"
githubRepo: "AutoCVE"
category: "agent-framework"
tags: ["security", "cve", "multi-agent", "code-audit"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "AutoCVE是一个面向安全研究人员和企业的自动化CVE挖掘平台，通过多Agent协同完成项目筛选、源码审计、漏洞验证和报告生成的全流程。它适合希望高效发现并申报CVE漏洞的安全团队，无需手动执行繁琐的审计步骤。"
vibeCodingPrompt: "使用Claude Code集成AutoCVE：1) git clone项目并进入目录；2) 根据文档配置PostgreSQL数据库和LLM API密钥（如GPT-4）；3) 运行docker-compose up启动前后端；4) 在界面中导入目标开源项目仓库；5) 选择审计模式（增强扫描/智能审计/综合审计）并创建审计任务；6) 等待Agent自动完成漏洞挖掘并查看生成的CVE报告。"
pitfallGuide: "1. 需要自行配置LLM API（如OpenAI、Anthropic），无内置免费模型，成本较高。
2. 依赖PostgreSQL数据库，部署前需确保数据库可用。
3. 非技术用户需阅读文档完成环境部署，无法一行命令直接跑通。
4. 当前仅支持源码审计，不覆盖二进制或运行时漏洞。
5. Agent执行时间较长，大型项目审计可能需数小时。"
targetAudience: ["安全研究员", "企业安全团队", "独立安全开发者", "技术负责人"]
useCases: ["自动化挖掘开源项目CVE漏洞", "企业内部代码安全审计", "安全研究团队批量漏洞发现", "CVE申报报告自动生成"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Agent-driven automated CVE discovery platform for source code auditing, vulnerability verification, and report generation.

> GitHub: [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | ⭐ 221 | Python

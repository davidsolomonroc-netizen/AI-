---
title: "cvENGINE 攻击面评估引擎"
description: "开源AI驱动的外部攻击面评估与漏洞验证平台"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/hevnsnt/CVEngine"
githubStars: 232
githubOwner: "hevnsnt"
githubRepo: "CVEngine"
category: "other"
tags: ["cybersecurity", "attack-surface", "vulnerability-scanner", "mcp"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "cvENGINE 能自动发现企业暴露在互联网上的资产，并实时匹配最新被利用的 CVE 漏洞，还能通过只读验证确认漏洞是否真实存在。适合安全团队、中小企业或独立开发者，用零许可成本替代昂贵的攻击面管理商业产品。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/hevnsnt/CVEngine && cd CVEngine。2. 查看 README 中的 Docker 部署部分，复制 .env.example 为 .env 并配置数据库和域名。3. 运行 docker compose up -d 启动服务。4. 访问 localhost:8000 创建管理员账号。5. 在界面中添加你的域名，等待自动发现资产和漏洞匹配。6. 集成 MCP：在 Claude Code 配置中添加 cvENGINE 的 MCP 服务器地址，让 AI 代理可以查询资产和漏洞数据。7. 编写自定义脚本调用 API 定期导出报告。"
pitfallGuide: "需要自行准备 PostgreSQL 数据库和 Docker 环境，非技术用户可能卡在配置环节。
扫描外部资产需遵守法律法规，仅对自有或授权资产使用。
Python 3.14 和 Django 5.2 版本较新，部分依赖可能不兼容。
MCP 集成需要额外配置，确保网络互通和认证正确。
漏洞验证为只读检查，但可能触发目标安全告警，建议在测试环境先行验证。"
targetAudience: ["企业团队", "技术负责人", "独立开发者"]
useCases: ["企业外部攻击面持续监控与漏洞管理", "安全团队快速验证新披露 CVE 对自身资产的影响", "开发者在 CI/CD 中集成资产发现与漏洞匹配", "AI 代理通过 MCP 自动查询安全态势"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI-first external attack surface assessment with continuous discovery, evidence-based vulnerability validation, and developer-agent MCP integration.

> GitHub: [hevnsnt/CVEngine](https://github.com/hevnsnt/CVEngine) | ⭐ 232 | Python

---
title: "Subpool 团队AI订阅共享池"
description: "自托管AI订阅配额分配与治理平台"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/gesta-run/subpool"
githubStars: 67
githubOwner: "gesta-run"
githubRepo: "subpool"
category: "dev-tools"
tags: ["ai-gateway", "subscription-pooling", "go", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Subpool 是一个开源的AI订阅池化工具，帮助企业将多个AI订阅账号（如Claude、OpenAI）集中管理，并为团队成员分配独立密钥，统一管控配额、监控用量和审计访问。适合已有多个AI订阅或API账号、需要团队共享且精细权限管理的技术团队，可有效降低订阅成本并提升治理透明度。"
vibeCodingPrompt: "请使用Subpool开源项目（gesta-run/subpool）构建一个团队AI网关应用。步骤：1. 克隆仓库并阅读README、docker-compose.yml和架构文档，理解核心概念（pools、accounts、keys）。2. 使用Docker Compose启动PostgreSQL和Subpool服务（确保端口18080和18081映射正确）。3. 通过管理API或Web控制台创建provider账号（如Anthropic Claude订阅或OpenAI API key），并配置为健康状态。4. 创建一个pool，将账号加入其中，设置配额分配策略（如优先使用订阅容量，自动回退到按量付费API）。5. 为团队成员生成独立API key，并为其设置速率限制、过期时间和可撤销权限。6. 将生成的endpoint（如http://localhost:18080/v1）和key配置到Claude Code或Cursor中，验证请求能正确路由到池内账号。7. 在控制台监控实时用量、账号健康状态和重置时间，并导出审计日志。注意：确保上游凭证加密存储，且不持久化对话内容。"
pitfallGuide: "需要先准备PostgreSQL 17和Docker Compose，否则部署会失败\n首次部署需仔细配置上游账号（订阅或API key），否则pool无可用容量\n不同AI服务商的API兼容性有差异，需使用OpenAI兼容端点（/v1/responses或/chat/completions）\n密钥加密存储依赖于环境变量中的加密密钥，需妥善保管，丢失后无法解密\n项目星数较少（67），社区支持和文档可能有限，生产使用需谨慎测试"
targetAudience: ["技术负责人", "企业团队", "独立开发者"]
useCases: ["团队共享多个Claude Pro订阅账号，统一分配员工密钥并监控配额", "在Claude Code或Cursor中为多名开发者提供统一AI网关，支持速率限制和审计", "企业内部分部门管理AI预算，按项目分配API key并跟踪成本"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。  A lightweight, self-hosted AI subscription pool for teams.

> GitHub: [gesta-run/subpool](https://github.com/gesta-run/subpool) | ⭐ 67 | Go

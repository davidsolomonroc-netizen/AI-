---
title: "Nuvex 链下服务"
description: "Solana 协议链下索引与价格 API 服务"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/NuvexNetwork/nuvex-services"
githubStars: 195
githubOwner: "NuvexNetwork"
githubRepo: "nuvex-services"
category: "data-analysis"
tags: ["solana", "indexer", "oracle", "typescript"]
editorialScore: 3
deploymentRating: 2
vibeCodingRating: 3
commercialSummary: "Nuvex 为 Solana 上的预言机协议提供链下数据支撑，包括把链上账户解码后写入 PostgreSQL 的索引器，以及对外提供价格中位数的读取 API。适合需要自建预言机数据管道、或想接入 Nuvex 价格数据的开发团队；非技术用户难以独立使用。"
vibeCodingPrompt: "1. 克隆仓库并执行 pnpm install，然后运行 make check 确认环境正常。2. 复制 env/.env.local.example 为 .env.local，填入 NUVEX_RPC_URL（Solana RPC 地址）、至少一个 program id（如 NUVEX_ORACLE_CORE_PROGRAM_ID）以及 DATABASE_URL 或 NUVEX_READ_MODEL_PATH。3. 启动本地 PostgreSQL，执行 indexer/prisma/migrations/ 下的 SQL 建表。4. 运行 indexer 的 start 命令开始解码链上账户并写入数据库。5. 启动 api/ 服务，访问 GET /health 确认 authority 为 none，再调用 GET /v1/prices 获取价格中位数。6. 如需完整节点，先在协议仓库构建 nuvex-oracle-node:local 镜像，再用 infra/ 下的 compose 文件启动 node profile。"
pitfallGuide: "启动 indexer 必须同时提供 RPC URL、至少一个 program id 和数据库/快照路径，否则进程会以退出码 2 结束。\n--health 只检查进程存活，不代表索引数据正常，需要单独校验数据库内容。\n/api/v1/prices 返回的是公开观测值的中位数，不是链上结果，不可用于结算或强一致场景。\n/api 下的 jobs 和 models 接口返回 501，ai/ 目录只有 README，没有实际模型。\n使用 node compose profile 前，必须先在协议仓库构建 nuvex-oracle-node:local 镜像，否则启动失败。"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["搭建 Solana 预言机价格数据索引管道", "为自有应用提供去中心化价格中位数 API", "研究链上账户解码与 PostgreSQL 读模型设计"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Off-chain services for Nuvex. This repository does not deploy programs and it is not a source of protocol truth.

> GitHub: [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) | ⭐ 195 | TypeScript

---
title: "MCP 数据库服务"
description: "让AI直接操作数据库的无状态服务"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/PerfectXM/mcp-db-server"
githubStars: 99
githubOwner: "PerfectXM"
githubRepo: "mcp-db-server"
category: "agent-framework"
tags: ["MCP", "database", "AI", "Java"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "MCP-DB-Server 是一个无状态的数据库 MCP 服务，允许 AI 客户端（如 Claude Desktop）通过标准协议直接查询和操作多种数据库（MySQL、PostgreSQL 等）。适合需要让 AI 助手安全访问数据库的开发者或企业团队，无需持久化配置，即用即连。"
vibeCodingPrompt: "在 Claude Code 中，使用以下步骤集成 mcp-db-server 项目：
1. 通过 Docker 启动服务：`docker run -p 8080:8080 perfectxm/mcp-db-server`
2. 在 Claude Desktop 或 Cursor 的 MCP 配置中添加 SSE 端点：`http://localhost:8080`
3. 调用 MCP 工具时，传入数据库连接参数（type、host、port、database、username、password）
4. 使用 `query_table_names` 查看表列表，`describe_table` 获取表结构，`execute_sql_query` 执行查询
5. 示例 Prompt：\"查询当前数据库中的所有表，并获取 users 表的完整结构\""
pitfallGuide: "1. 连接池缓存 TTL 为5分钟，频繁切换不同数据库可能导致缓存未命中，需注意同一连接参数复用。
2. 服务端不持久化连接信息，每次调用都需传入完整参数，建议在 AI 客户端中保存常用连接配置。
3. 权限完全由数据库用户自身控制，服务端不做额外拦截，确保数据库用户权限最小化。
4. 写操作工具 `execute_sql_write` 存在风险，建议在测试环境先验证 SQL 再用于生产。
5. Docker 部署时需确保网络连通性，数据库可能与服务不在同一容器网络。"
targetAudience: ["开发者", "技术负责人", "AI 研究者"]
useCases: ["让 Claude Desktop 直接查询数据库并生成报表", "在 Cursor 中通过自然语言操作开发数据库", "集成到企业 AI 助手实现数据库自助查询", "快速原型开发时让 AI 辅助数据建模和查询"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。🔥 让 AI 直接操刀你的数据库！无状态 MCP 数据库服务，支持 MySQL / PostgreSQL / SQLite / SQL Server / Oracle / H2，连接参数即传即用，零持久化零配置。

> GitHub: [PerfectXM/mcp-db-server](https://github.com/PerfectXM/mcp-db-server) | ⭐ 99 | Java

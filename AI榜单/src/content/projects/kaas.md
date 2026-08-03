---
title: "KaaS：知识即服务——AI驱动的个人知识库编译器"
description: "将零散笔记编译为可查询的Markdown知识库，支持MCP。"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/bybit-exchange/kaas"
githubStars: 78
githubOwner: "bybit-exchange"
githubRepo: "kaas"
category: "workflow-automation"
tags: ["knowledge-base", "MCP", "LLM", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "KaaS将散落在文档、会议记录和邮件中的知识，通过LLM流水线编译成结构化的个人Wiki，解决组织知识流失和重复回答相同问题的痛点。适合需要沉淀团队经验、构建个人第二大脑的团队和知识工作者。无需嵌入模型，完全自托管，数据安全可控。"
vibeCodingPrompt: "1. 克隆仓库：`git clone https://github.com/bybit-exchange/kaas && cd kaas`
2. 阅读 README 和 docs/ 了解架构和配置要求
3. 设置环境变量（如 OPENAI_API_KEY），参考 .env.example
4. 运行 `docker-compose up -d` 启动服务（需确保 Docker 已安装）
5. 使用 CLI 或 Web UI 导入你的笔记/文档目录，KaaS 会自动编译成 wiki
6. 配置 MCP 服务，在 Claude Code 中添加 MCP 连接，即可通过对话查询知识库
7. 如需定制，可修改 pipeline 中的 prompt 模板或调整分类规则"
pitfallGuide: "需要有效的 LLM API Key（如 OpenAI），否则流水线无法运行\n首次编译大量文档可能耗时较长，建议分批处理\nMCP 配置涉及网络端口和认证，确保安全组规则正确\n自托管需自行维护数据库备份和升级\n非技术用户需熟悉 Docker 基本操作，否则部署可能超过10分钟"
targetAudience: ["独立开发者", "内容创作者", "企业团队", "技术负责人"]
useCases: ["将会议记录和邮件自动整理为部门Wiki，新员工快速上手", "构建个人第二大脑，把读书笔记和播客转录变成可检索知识库", "团队离职交接时，保留角色相关的经验沉淀", "通过MCP集成到Claude Code，直接在IDE中查询项目历史决策"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Turn scattered notes, docs and transcripts into a queryable Markdown wiki — an LLM knowledge-base compiler with MCP access, no embeddings, self-hosted.

> GitHub: [bybit-exchange/kaas](https://github.com/bybit-exchange/kaas) | ⭐ 78 | Python

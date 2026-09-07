---
title: "Reverify：AI 防幻觉验证器"
description: "用确定性工具校验 AI 主张，杜绝幻觉。"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/2akouwu/reverify"
githubStars: 978
githubOwner: "2akouwu"
githubRepo: "reverify"
category: "dev-tools"
tags: ["anti-hallucination", "verification", "mcp-server", "cli"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Reverify 解决 AI 在编码或分析时自信地编造 API、数据结构或行为描述的问题。它通过 MCP 服务器或 CLI，让 AI 的每个主张都经过确定性工具校验，并给出证据。适合依赖 AI 辅助编程、逆向工程或安全分析的个人开发者与团队，确保技术结论可信。"
vibeCodingPrompt: "1. 安装 reverify：`pip install reverify` 并启动 MCP 服务器（`reverify mcp`）。\n2. 在 Claude Code 中配置 MCP 连接，添加 reverify 作为工具。\n3. 当 AI 提出关于代码库、二进制或 API 的具体主张时，指示它调用 reverify verify 并附上声明与目标文件。\n4. 让 AI 根据返回的 VERIFIED/REFUTED 结果修正回答，只保留带证据的结论。\n5. 对于长期会话，使用 reverify 的上下文持久化功能保存已验证事实，避免重新生成时丢失。"
pitfallGuide: "1. 需要 Python 3.9+，确保环境兼容。\n2. MCP 配置需正确指向服务器端口，否则 AI 无法调用。\n3. 仅对可访问的本地文件或二进制有效，远程 API 主张无法自动验证。\n4. 首次运行可能需下载依赖，10 分钟快速部署有难度。\n5. 验证规则需自定义，默认对逆向分析场景优化，其他领域需调整。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "企业团队"]
useCases: ["AI 辅助逆向工程时验证函数行为", "防止 AI 在代码审查中虚构 API 调用", "在安全分析中确保持久化上下文事实准确", "用于 CI/CD 中自动校验 AI 生成的代码注释"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Stop your AI from making things up — it proposes, deterministic tools decide, every claim checked against ground truth with evidence. Grounded facts and context survive resets. Reverse engineering is the proving ground. MCP server + CLI.

> GitHub: [2akouwu/reverify](https://github.com/2akouwu/reverify) | ⭐ 978 | Python

---
title: "DexSQL"
description: "用SQL查询Android APK与DEX文件"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/LSPosed/dexsql-release"
githubStars: 190
githubOwner: "LSPosed"
githubRepo: "dexsql-release"
category: "data-analysis"
tags: ["Android", "DEX", "SQL", "MCP"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "DexSQL 让开发者用 SQL 语句直接查询 Android 安装包中的类、方法和字符串，无需反编译工具。适合安全研究人员、逆向工程师和需要分析 Android 应用的团队。"
vibeCodingPrompt: "请按以下步骤用 DexSQL 搭建一个 Android 应用分析工具：1. 从 GitHub Releases 下载 DexSQL 可执行文件或通过 pip 安装；2. 启动 DexSQL 的 MCP 服务器（stdio 模式）；3. 在 Claude Code 中配置 MCP 连接指向 DexSQL；4. 编写一个 Python 脚本，调用 DexSQL 查询指定 APK 中所有包含 'password' 字符串的方法；5. 输出结果并保存为 JSON 文件。"
pitfallGuide: "确保 APK/DEX 文件路径正确且可读。\nMCP 服务器需单独启动或由客户端自动拉起。\n查询语法需参考文档，避免 SQL 错误。\n大文件查询可能消耗较多内存，建议分批次处理。\n非技术用户建议使用预编译的 .mcpb 包简化安装。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["安全审计：快速查找敏感字符串或 API 调用", "逆向工程：分析第三方 APK 的类结构", "自动化报告：生成应用组件清单", "AI 辅助分析：通过 MCP 让 AI 代理查询 DEX 数据"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。SQL for Android apk and dex files

> GitHub: [LSPosed/dexsql-release](https://github.com/LSPosed/dexsql-release) | ⭐ 190 | Python

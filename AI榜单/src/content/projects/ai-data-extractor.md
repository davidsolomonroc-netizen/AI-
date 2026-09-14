---
title: "AI 编程助手聊天记录提取器"
description: "一键导出 AI 编程助手本地聊天记录为统一 JSONL 格式"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/kruzovic7/ai-data-extractor"
githubStars: 470
githubOwner: "kruzovic7"
githubRepo: "ai-data-extractor"
category: "dev-tools"
tags: ["data-extraction", "ai-coding", "dataset", "jsonl"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 4
commercialSummary: "这个开源工具能从 Claude Code、Cursor、Windsurf、Aider 等十余款 AI 编程助手中，自动发现并导出你本地的全部聊天记录，统一整理成标准 JSONL 格式。适合想用自己历史对话做微调数据、个人分析，或在应用清空本地数据库前做备份的开发者。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/kruzovic7/ai-data-extractor 并进入目录。
2. 安装依赖：pip install -r requirements.txt（或按 README 指引）。
3. 运行提取脚本，自动扫描本机所有支持的 AI 编程助手数据源，输出统一 JSONL 文件。
4. 检查输出目录中的 JSONL 文件，确认包含 user/assistant 消息、代码片段、时间戳等字段。
5. 用 Python 脚本加载 JSONL，做简单统计（如按工具/项目分组、消息数量），或转换为微调数据集格式。
6. 如需增量备份，可设置定时任务定期运行提取脚本。"
pitfallGuide: "部分工具（如 Windsurf、Trae）使用未公开的 SQLite schema，提取结果可能不完整或需要启发式解析。
提取前确保相关应用已关闭，避免数据库被锁定导致读取失败。
聊天记录可能包含敏感代码或隐私信息，分享或用于微调前务必脱敏。
不同工具的字段命名和结构差异较大，统一后的 JSONL 可能部分字段缺失，需按需处理。
跨平台路径自动探测，但在非标准安装位置可能需要手动指定数据目录。"
targetAudience: ["独立开发者", "AI 研究者", "数据分析师", "技术负责人"]
useCases: ["收集个人 AI 编程对话用于模型微调", "备份多年聊天记录防止应用清库丢失", "分析自己与 AI 协作的编码习惯和效率", "构建多工具统一的对话数据集用于研究"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Free open-source extractor for AI coding assistant chat histories. Supports Claude Code, Cursor, Windsurf, Aider, Cline/Roo Code, and more.

> GitHub: [kruzovic7/ai-data-extractor](https://github.com/kruzovic7/ai-data-extractor) | ⭐ 470 | Python

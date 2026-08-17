---
title: "TokenTab - AI 成本追踪仪表盘"
description: "本地解析 AI 会话日志，统计 token 花费"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/wzchav/tokentab"
githubStars: 219
githubOwner: "wzchav"
githubRepo: "tokentab"
category: "data-analysis"
tags: ["token-usage", "cost-tracking", "cli", "local-first"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "TokenTab 帮助个人开发者和小团队精确掌握在 Claude Code、Codex 和 Gemini CLI 上的 AI 使用成本，按模型、项目和日期维度分析。无需上传数据，完全本地运行，适合注重隐私且希望优化 AI 支出的技术用户。"
vibeCodingPrompt: "请帮我用 tokentab 项目搭建一个本地 AI 成本监控工具：
1. 克隆仓库并安装（git clone + pip install -e .）
2. 运行 `tokentab` 查看最近7天汇总
3. 使用 `tokentab --json` 导出数据，并写一个 Python 脚本定期生成周报
4. 配置 `tokentab web` 启动仪表盘，并设置开机自启"
pitfallGuide: "需先安装相关 CLI 工具（如 Claude Code），否则对应数据源会被跳过\nCursor 支持尚未完成，勿期望其输出\n所有数据来自本地日志，若清理过日志则历史数据缺失\n首次运行可能因日志路径不同而需调整配置\nWeb 仪表盘默认端口 4747，注意防火墙设置"
targetAudience: ["独立开发者", "技术负责人", "数据分析师"]
useCases: ["按月统计个人 AI 工具支出并优化预算", "对比不同 AI 模型的实际使用成本", "为团队生成 AI 使用报告，辅助决策"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A CLI that reads Claude Code, Codex, and Gemini CLI session logs and works out how much they cost, by model, project, and day.

> GitHub: [wzchav/tokentab](https://github.com/wzchav/tokentab) | ⭐ 219 | Python

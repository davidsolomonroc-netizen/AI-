---
title: "Aurelio 个人财富管理助手"
description: "自托管个人理财应用，内置 AI 财务顾问，追踪净资产与投资"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/LosaLosSantos/aurelio-finance"
githubStars: 2505
githubOwner: "LosaLosSantos"
githubRepo: "aurelio-finance"
category: "data-analysis"
tags: ["personal-finance", "self-hosted", "llm-advisor", "portfolio-tracker"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Aurelio 帮你把股票、ETF、现金和债务集中在一个界面里，并配一个能对话的 AI 财务顾问，所有数据都存在你自己的电脑上。适合注重隐私、有一定投资组合的独立投资者或家庭用户，用来替代各类收费的资产管理 SaaS。"
vibeCodingPrompt: "1. 克隆仓库 LosaLosSantos/aurelio-finance 并进入目录。
2. 先运行 ./start.sh --demo 验证环境（需 Node.js 22+ 和 uv），确认 http://localhost:8000 能打开示例数据。
3. 阅读 backend 目录，找到数据模型和 AI advisor 的调用入口（OpenRouter 集成点）。
4. 在 .env 或配置中填入你自己的 OpenRouter API Key，启用 AI 顾问功能。
5. 用 ./start.sh 启动真实模式，在界面中录入你的资产、ETF、现金与负债。
6. 向 AI 顾问提问，例如“我每月剩余 1200 欧元该如何分配”，观察它给出的拆分建议并确认或拒绝。
7. 如需扩展，可基于现有 API 增加新的资产类型或导出报表功能，改动前先备份 backend/data.db。"
pitfallGuide: "首次启动需要 Node.js 22+ 和 uv，环境不满足会安装失败，建议先手动装好。
AI 功能依赖 OpenRouter 且需自备 API Key，不配置则只能使用基础记账功能。
数据存在 backend/data.db，升级前应用会自动备份，但仍建议手动复制该文件以防万一。
Windows 用户若 PowerShell 禁止脚本运行，需加 -ExecutionPolicy Bypass 参数。
首次启动会下载依赖并初始化，耗时可能超过 10 分钟，请耐心等待。"
targetAudience: ["独立开发者", "创业者", "数据分析师", "技术负责人"]
useCases: ["个人或家庭净资产集中追踪与可视化", "ETF、股票、现金、负债的统一投资组合管理", "通过 AI 顾问获取每月结余分配与财务规划建议", "注重隐私的用户在本地自托管财务数据"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source personal finance app with an AI financial advisor: track your net worth, investments, ETFs, cash and debts on your own computer.

> GitHub: [LosaLosSantos/aurelio-finance](https://github.com/LosaLosSantos/aurelio-finance) | ⭐ 2505 | Python

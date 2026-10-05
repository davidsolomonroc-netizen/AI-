---
title: "AIHOT 行业热点引擎"
description: "自动抓取、筛选、聚合行业热点的日报框架"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/KKKKhazix/AIHOT"
githubStars: 5873
githubOwner: "KKKKhazix"
githubRepo: "AIHOT"
category: "workflow-automation"
tags: ["news-aggregator", "llm", "self-hosted", "rss"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "它能把 RSS 等信源自动汇聚，用大模型筛选打分并生成中文日报，帮你快速搭建一个垂直行业的热点资讯站。适合想低成本做行业内容聚合的独立开发者、内容创作者和小团队。"
vibeCodingPrompt: "请用 KKKKhazix/AIHOT 项目帮我搭建一个「法律行业热点日报」网站。步骤：1) 克隆仓库并阅读 README，用 Docker Compose 启动 PostgreSQL 和 Node.js 服务，确认本地能跑通默认的 AI 信源示例；2) 找到信源配置文件和精选标准提示词文件，把默认的 18 个海外 AI 资讯源替换成我提供的法律行业 RSS 源列表（如法院公告、律所博客、法律媒体）；3) 修改入选门槛和打分提示词，让大模型按「法律从业者关注度」筛选和打分；4) 调整聚簇和热度算法参数，让同一法律事件的不同报道合并成一个事件；5) 启动后检查日报生成效果，若摘要或标题不理想，迭代修改提示词。最后给我一份如何每天自动运行和部署到服务器的说明。"
pitfallGuide: "项目由非专业开发者与 AI 共同编写，代码质量参差，遇到问题需自行排查或提 Issue。
仓库不含原站信源名单和运营数据，需自己准备行业 RSS 源，否则只能跑默认示例。
依赖 Node.js 24 和 PostgreSQL 17，环境版本不匹配可能启动失败。
大模型筛选和打分依赖提示词，替换行业后需反复调试才能得到理想效果。
部分功能（模型榜、监控等）只保留在原站，开源版可能不包含。"
targetAudience: ["独立开发者", "内容创作者", "创业者", "产品经理"]
useCases: ["搭建垂直行业热点资讯站", "自动生成行业日报并推送", "聚合多信源做事件追踪", "为特定领域做 AI 内容筛选与摘要"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

> GitHub: [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | ⭐ 5873 | TypeScript

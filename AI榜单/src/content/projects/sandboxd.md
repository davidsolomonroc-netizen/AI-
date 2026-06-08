---
title: "沙盒引擎"
description: "自托管AI应用构建沙盒平台"
publishDate: 2026-06-08
featured: false
githubUrl: "https://github.com/tastyeffectco/sandboxd"
githubStars: 511
githubOwner: "tastyeffectco"
githubRepo: "sandboxd"
category: "dev-tools"
tags: ["sandbox", "ai-agent", "self-hosted", "preview-url"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "sandboxd让AI应用构建产品（如Lovable、Bolt）的开发者可以自托管沙盒环境，一键创建隔离容器、运行AI编码代理并生成实时预览链接。适合SaaS工厂、AI代理平台或需要为每个用户提供独立开发环境的团队。"
vibeCodingPrompt: "请使用sandboxd项目搭建一个简单的AI应用构建服务：
1. 在服务器上运行 `docker run -d -p 8080:8080 tastyeffectco/sandboxd` 启动服务
2. 通过API创建沙盒：`curl -X POST http://localhost:8080/sandbox`
3. 在沙盒内运行任务：`curl -X POST http://localhost:8080/sandbox/{id}/tasks -H \"Content-Type: application/json\" -d '{\"prompt\":\"用React写一个待办事项应用\"}'`
4. 获取预览URL：`http://{id}.preview.localhost:8080`"
pitfallGuide: "1. 沙盒在空闲时会自动休眠以节省资源，但首次唤醒可能有延迟。
2. 预览URL仅在同一台机器的Docker网络内可用，需配置反向代理才能对外暴露。
3. 当前为beta版本，API和功能可能变化，生产使用需关注更新。
4. 资源限制（内存、CPU）需根据服务器配置调整，避免过载。
5. 内置的AI代理（OpenCode、Claude Code）需要额外的API密钥才能工作。"
targetAudience: ["创业者", "技术负责人", "AI研究者", "产品经理"]
useCases: ["为SaaS产品提供AI编码沙盒功能", "搭建内部AI应用开发测试平台", "快速创建带预览链接的AI代理演示环境", "教育场景中隔离学生代码运行环境"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Self-hosted dev sandboxes with preview URLs. One command. No Kubernetes, perfect for coding agents and Saas factories

> GitHub: [tastyeffectco/sandboxd](https://github.com/tastyeffectco/sandboxd) | ⭐ 511 | Go

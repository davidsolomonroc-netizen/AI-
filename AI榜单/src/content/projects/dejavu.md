---
title: "DejaVu 跨工具记忆"
description: "跨工具持久化AI记忆，隐私安全"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/JSingletonAI/dejavu"
githubStars: 63
githubOwner: "JSingletonAI"
githubRepo: "dejavu"
category: "agent-framework"
tags: ["memory", "local-first", "mcp", "privacy"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "DejaVu 为AI工具提供持久化记忆，让不同AI应用共享上下文，同时保障数据本地存储与隐私安全。适合需要跨工具协作的记忆管理场景，如个人助理或企业知识库。"
vibeCodingPrompt: "使用 DejaVu 搭建一个跨工具记忆助手：
1. 克隆仓库并安装依赖：git clone https://github.com/JSingletonAI/dejavu && cd dejavu && pip install -r requirements.txt
2. 配置本地记忆存储路径，编辑 config.yaml 设置 memory_path 为本地目录
3. 启动 MCP 服务：python server.py --port 8080
4. 在 Claude Code 中集成：通过 MCP 客户端连接 localhost:8080，注册记忆读写工具
5. 测试：向 Claude 发送“记住我的偏好：使用暗色模式”，然后重启对话并询问“我的偏好是什么”，验证记忆持久化"
pitfallGuide: "确保本地存储路径有足够磁盘空间
MCP 协议版本兼容性需检查，建议使用最新 release
隐私安全依赖本地存储，请勿将 memory_path 设为网络共享目录
首次启动需手动创建 config.yaml，否则使用默认配置可能不生效
多工具并发写入时注意锁机制，避免数据冲突"
targetAudience: ["独立开发者", "创业者", "技术负责人"]
useCases: ["个人AI助理跨会话记忆", "多AI工具协作知识共享", "本地隐私优先的记忆管理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。跨工具持久化AI记忆，隐私安全

> GitHub: [JSingletonAI/dejavu](https://github.com/JSingletonAI/dejavu) | ⭐ 63 | ["memory",

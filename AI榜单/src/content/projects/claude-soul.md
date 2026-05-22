---
title: "克劳德灵魂记忆引擎"
description: "跨会话自纠正记忆系统"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/DomDemetz/claude-soul"
githubStars: 76
githubOwner: "DomDemetz"
githubRepo: "claude-soul"
category: "agent-framework"
tags: ["memory", "claude-code", "mcp-server", "self-improving"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Claude Soul 是一个为 Claude Code 添加持久记忆的引擎，能跨会话自动记录和纠正信息。适合需要长期上下文一致性的开发者和团队，避免重复描述项目背景或用户偏好。"
vibeCodingPrompt: "1. 克隆仓库: git clone https://github.com/DomDemetz/claude-soul.git
2. 安装依赖: cd claude-soul && npm install
3. 配置 MCP 服务器: 在 Claude Code 中启用 MCP 并添加此项目路径
4. 启动服务: npm start
5. 在对话中测试记忆: 输入 '记住我的名字是张三'，然后开启新对话询问 '我叫什么'，观察是否自动回忆。"
pitfallGuide: "1. 需要 Node.js 18+ 环境
2. MCP 服务器配置需正确指向项目目录
3. 记忆存储默认在本地，注意备份
4. 首次使用需手动触发记忆写入
5. 跨会话记忆可能受 Claude 上下文限制影响"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["长期项目开发中保持上下文一致性", "个性化助手记忆用户偏好和历史", "团队协作时共享项目背景知识"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Claude跨会话自纠正记忆引擎

> GitHub: [DomDemetz/claude-soul](https://github.com/DomDemetz/claude-soul) | ⭐ 76 | ["memory",

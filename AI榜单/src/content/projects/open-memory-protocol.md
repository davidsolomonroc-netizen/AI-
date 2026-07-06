---
title: "开放记忆协议"
description: "跨工具、跨设备的AI记忆互通标准"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/SMJAI/open-memory-protocol"
githubStars: 66
githubOwner: "SMJAI"
githubRepo: "open-memory-protocol"
category: "agent-framework"
tags: ["AI-memory", "interoperability", "MCP", "open-standard"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Open Memory Protocol 解决AI工具之间记忆孤岛问题，让Claude、ChatGPT、Cursor等工具共享用户偏好和历史上下文。适合需要多工具协同工作、希望AI持续学习用户习惯的个人或团队。"
vibeCodingPrompt: "1. 克隆项目: git clone https://github.com/SMJAI/open-memory-protocol.git\n2. 进入目录: cd open-memory-protocol\n3. 启动服务器: docker compose up -d (或 node server.js)\n4. 在Claude Code中配置MCP指向本地OMP服务器\n5. 在Cursor中安装OMP插件并连接同一服务器\n6. 现在两个工具共享记忆，无需重复配置"
pitfallGuide: "1. 协议仍在v0.4阶段，API可能不兼容更新\n2. 自托管需要维护服务器稳定性，否则记忆丢失\n3. 不同工具对OMP的支持程度不一，需手动安装适配器\n4. 敏感记忆数据建议加密存储，避免泄露"
targetAudience: ["独立开发者", "创业者", "企业团队", "技术负责人"]
useCases: ["跨AI助手共享用户偏好，减少重复描述", "团队协作时让不同AI工具了解项目上下文", "个人知识管理系统与AI聊天机器人同步记忆", "企业级AI agent统一用户画像"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。An open standard for portable, interoperable AI memory across tools, sessions, and devices.

> GitHub: [SMJAI/open-memory-protocol](https://github.com/SMJAI/open-memory-protocol) | ⭐ 66 | TypeScript

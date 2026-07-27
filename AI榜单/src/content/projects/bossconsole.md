---
title: "BOSS控制台：AI代理的指挥中心"
description: "多平台AI代理原生操控台"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/risa-labs-inc/BossConsole"
githubStars: 199
githubOwner: "risa-labs-inc"
githubRepo: "BossConsole"
category: "agent-framework"
tags: ["agent-harness", "multi-platform", "MCP", "Kotlin"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "BOSS控制台是一个开源的多平台AI代理操控台，让企业、科研团队能够在一个桌面应用中同时运行Claude Code、Codex、Gemini等AI代理，并为其提供真实的浏览器、终端、编辑器和100多个MCP工具。它解决了AI代理缺乏统一操作环境和权限管控的问题，适合需要高效、安全地使用多个AI代理进行复杂任务的组织。"
vibeCodingPrompt: "在Claude Code中，首先克隆BOSS控制台仓库并按照README中的构建指南进行编译。构建成功后，启动应用并进入设置界面，配置你的AI代理API密钥（如Claude Code或Gemini）。然后创建一个新的项目工作区，在工具箱中启用所需的MCP工具（如文件操作、网络请求、数据库连接）。最后，在代理面板中添加一个Claude Code实例，给它一个具体任务，例如'分析当前项目代码结构并生成文档'，观察BOSS如何将代理与浏览器、终端等资源整合。"
pitfallGuide: "1. 项目目前处于早期阶段，API和功能可能频繁变化\n2. 需要自行编译或从Release页面下载构建版本，没有一键安装脚本\n3. 多代理协作时需仔细配置RBAC权限，避免代理越权操作\n4. 依赖JVM环境，确保系统已安装JDK 17+\n5. 部分MCP工具可能需要额外配置或外部服务支持"
targetAudience: ["AI研究者", "企业团队", "技术负责人", "独立开发者"]
useCases: ["企业级多AI代理统一管理与任务编排", "科研项目中复杂工作流的自动化执行", "开发者在本地安全地测试和调试多个AI代理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source, multi-platform harness for AI agents — a native, multi-threaded operator's console (JVM, not Electron) to run Claude Code, Codex, Gemini or OpenCode with a real browser, terminal, editor, secrets & 100+ MCP tools. Built for enterprises, science & research.

> GitHub: [risa-labs-inc/BossConsole](https://github.com/risa-labs-inc/BossConsole) | ⭐ 199 | Kotlin

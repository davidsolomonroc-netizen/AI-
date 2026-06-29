---
title: "Tupper：AI 代理安全沙箱"
description: "在本地安全运行 AI 生成的代码"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/lightbearco/tupper"
githubStars: 135
githubOwner: "lightbearco"
githubRepo: "tupper"
category: "dev-tools"
tags: ["sandbox", "ai-agents", "code-execution", "containers"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Tupper 为 AI 代理提供本地隔离沙箱，允许安全执行不可信的 AI 生成代码、运行 shell 命令和读写文件。适合需要自托管代码执行环境的开发者团队、AI 研究者和企业，避免依赖第三方云沙箱服务。"
vibeCodingPrompt: "使用 Tupper 搭建一个 AI 代码沙箱服务：
1. 安装 Bun（若未安装）
2. 运行 `bun create tupper` 初始化项目
3. 在 `sandbox.ts` 中导入 `@tupper/sdk`，调用 `createSandbox()` 创建沙箱实例
4. 使用沙箱执行 Python 代码：`sandbox.runCode('print(\"hello\")', { language: 'python' })`
5. 使用沙箱运行 shell 命令：`sandbox.runCommand('ls -la')`
6. 将沙箱暴露为 HTTP API，供外部 AI 代理调用
7. 注意 macOS 上需先安装 Apple Containers，Linux 用户等待 Firecracker 支持"
pitfallGuide: "目前仅支持 macOS（Apple Containers），Linux 和 Windows 支持尚未就绪\n项目处于早期开发阶段，API 可能在 1.0 前变化\n依赖 Apple Containers 或 Firecracker，需要额外安装和配置\n沙箱性能受限于容器化开销，不适合高并发场景\n文档和社区支持有限，遇到问题需自行排查"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "企业团队"]
useCases: ["AI 代理代码执行沙箱", "安全运行用户提交的代码", "本地测试 AI 生成代码", "CI/CD 中隔离代码执行"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source sandboxes for AI agents — run untrusted, AI-generated code safely on your own machine.

> GitHub: [lightbearco/tupper](https://github.com/lightbearco/tupper) | ⭐ 135 | TypeScript

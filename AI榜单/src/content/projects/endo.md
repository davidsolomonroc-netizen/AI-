---
title: "高阶智能体编排器"
description: "统一聊天界面，自由组合多个AI代理。"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/longsurf-ai/endo"
githubStars: 98
githubOwner: "longsurf-ai"
githubRepo: "endo"
category: "agent-framework"
tags: ["agent", "orchestration", "harness", "workflow"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Endo 是一个高阶智能体编排工具，让你在一个聊天界面里自由切换和组合 Codex、Claude Code 等多个 AI 代理，共享对话历史，从而完成复杂任务。适合需要同时使用多个 AI 模型来提升工作效率的独立开发者、产品经理和企业团队。"
vibeCodingPrompt: "1. 下载 Endo 的 macOS 应用（Apple Silicon）并安装。
2. 打开 Endo，在设置中配置你的 AI 代理（如 Codex、Claude Code）的 API 密钥或登录信息。
3. 创建一个新会话，在聊天界面中选择一个代理开始对话。
4. 在对话中，你可以随时切换到另一个代理，新代理会自动继承之前的对话历史。
5. 使用 /best-of-n 命令让多个代理同时回答同一问题，然后选择最佳答案。
6. 将常用的代理组合保存为工作流，方便以后一键调用。
7. 通过 Endo 的界面监控每个代理的响应和工具调用，进行调试和优化。"
pitfallGuide: "需要 macOS Apple Silicon 设备，不支持 Intel Mac 或 Windows。
部分代理可能需要额外的 API 密钥或订阅，确保提前配置好。
切换代理时注意上下文长度限制，过长的历史可能被截断。
/best-of-n 命令会消耗多个代理的调用次数，注意成本控制。
工作流保存后，代理的配置变更可能需要重新调整工作流。"
targetAudience: ["独立开发者", "产品经理", "企业团队", "技术负责人"]
useCases: ["多代理协作完成复杂编程任务", "对比不同 AI 模型的回答质量", "自动化工作流中集成多个 AI 代理", "快速原型开发与测试"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The Higher Order Harness (HOH "/oʊ/" ), projected as a unified chat interface.

> GitHub: [longsurf-ai/endo](https://github.com/longsurf-ai/endo) | ⭐ 98 | TypeScript

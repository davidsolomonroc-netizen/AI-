---
title: "UmaDev：AI 编码治理轨道"
description: "为 AI 编码底座套上可治理的交付流水线"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/umacloud/umadev"
githubStars: 89
githubOwner: "umacloud"
githubRepo: "umadev"
category: "agent-framework"
tags: ["ai-coding", "workflow-automation", "rust", "governance"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "UmaDev 为 Claude Code、Codex、OpenCode 等 AI 编码工具提供一套结构化的 9 阶段交付流程，从需求澄清到质量门禁，确保输出可检查、可恢复、可审计。适合需要管控 AI 编码质量的企业团队和技术负责人，在保持底座工具灵活性的同时增加治理轨道。"
vibeCodingPrompt: "1. 确保已安装 Rust 环境（rustup 和 cargo）。
2. 克隆仓库：git clone https://github.com/umacloud/umadev.git
3. 进入目录：cd umadev
4. 构建项目：cargo build --release
5. 运行：./target/release/umadev init 初始化项目
6. 用 Claude Code 打开项目目录，执行 umadev start 开始治理流程
7. 按提示逐步填写需求，UmaDev 会自动调用底座完成各阶段交付物"
pitfallGuide: "1. 确保 Claude Code/Codex/OpenCode 已登录并可用，否则流水线无法执行。
2. 初始配置需要学习 UMADEV_HOST_SPEC_V1 规范，有一定学习曲线。
3. 不适合纯探索式编码，治理流程会限制自由发挥。
4. 早期版本可能有流程卡顿或异常，需手动干预恢复。
5. 质量门禁规则需根据项目定制，默认规则可能过严或过松。"
targetAudience: ["企业团队", "技术负责人", "独立开发者", "产品经理"]
useCases: ["企业级 AI 编码项目交付管理", "需要审计和合规的软件开发流程", "团队协作中统一 AI 编码行为规范", "从需求到交付的全流程自动化试点"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI 编码项目总监 Agent:驱动你已登录的 Claude Code / Codex / OpenCode，套上 9 阶段可治理的商业级交付流水线。  AI Coding Project Director Agent | Power Claude Code, Codex & OpenCode with a 9-stage governable commercial delivery pipeline.

> GitHub: [umacloud/umadev](https://github.com/umacloud/umadev) | ⭐ 89 | Rust

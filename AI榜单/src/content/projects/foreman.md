---
title: "工头：AI 交付流水线调度器"
description: "用 TUI 监督 Claude Code 代理完成软件交付"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/VisionForge-OU/foreman"
githubStars: 84
githubOwner: "VisionForge-OU"
githubRepo: "foreman"
category: "agent-framework"
tags: ["agent-orchestrator", "claude-code", "devops-pipeline", "tui"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Foreman 是一个面向开发者的 TUI 工具，通过编排本地 Claude Code 代理，自动化软件交付流程（从计划、设计到构建、测试）。它适合希望减少手动编码、加速迭代的独立开发者或小团队，尤其适合需要严格质量门禁（设计审核、TDD）的项目。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：`git clone https://github.com/VisionForge-OU/foreman.git && cd foreman && pip install -e .`。
2. 确保本地已安装 Claude CLI 并配置好 API 密钥，运行 `claude --version` 验证。
3. 在目标仓库目录下运行 `foreman init` 初始化配置，然后启动 TUI：`foreman tui`。
4. 在 TUI 中选择“Plan”阶段，输入需求描述，Foreman 会生成 ADR/PRD 并等待人工审核。
5. 审核通过后，自动进入任务分解（issues）、TDD 构建、端到端测试阶段，全程可监控和干预。
6. 如需集成到 Claude Code 项目，可在 Cursor 或终端中运行 `foreman run --pipeline plan` 触发单步操作。"
pitfallGuide: "1. 必须提前安装并认证 Claude CLI，否则 Foreman 无法启动代理。
2. 管道状态存储在目标仓库的 .foreman/ 目录中，不要手动修改这些文件以免状态不一致。
3. 设计阶段需要人工审核，不要跳过门禁，否则可能导致后续构建混乱。
4. 对大型仓库首次运行可能较慢，因为需要解析完整代码库上下文。
5. 当前仅支持 Claude Code 作为后端代理，切换其他模型需自行修改适配层。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "企业团队"]
useCases: ["自动化软件交付流水线（从需求到测试）", "团队内部代码审查与质量门禁", "快速原型验证与迭代开发", "AI 辅助的 TDD 开发流程"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A Boris-style agentic orchestrator TUI that supervises headless Claude Code agents through a gated software-delivery pipeline — pointed at any repository.

> GitHub: [VisionForge-OU/foreman](https://github.com/VisionForge-OU/foreman) | ⭐ 84 | Python

---
title: "LongHorizon-Harness：长时程智能体运行框架"
description: "跨桌面与CLI的长时程AI代理运行框架"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/AMAP-ML/LongHorizon-Harness"
githubStars: 520
githubOwner: "AMAP-ML"
githubRepo: "LongHorizon-Harness"
category: "agent-framework"
tags: ["long-horizon", "computer-use", "claude-code", "codex"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "LongHorizon-Harness 解决了AI代理在长时间运行中状态丢失、进度不可靠的问题，让AI能连续数小时跨桌面应用和命令行执行复杂任务。适合需要自动化处理多步骤业务流程的企业团队和技术负责人，可显著提升复杂工作流的完成率与可验证性。"
vibeCodingPrompt: "1. 安装 LongHorizon-Harness（pip install longhorizon-harness）。\n2. 在项目根目录运行 `lh-harness init` 初始化配置。\n3. 将需要执行的复杂任务描述（如：整理季度财务报告并生成PPT）写入 `task.md`。\n4. 运行 `lh-harness run --backend claude-code --task task.md`，框架将自动调度Claude Code跨桌面应用和CLI执行。\n5. 使用 `lh-harness audit` 查看每一步的状态验证和进度报告，确保任务可靠推进。"
pitfallGuide: "确保Python版本≥3.10，否则安装失败。\n执行前需配置好Claude Code或Codex的API密钥，否则后端无法启动。\n长时程任务建议使用独立工作目录，避免污染现有项目。\n桌面应用自动化依赖系统权限，需提前授予辅助功能权限。\n若任务涉及敏感数据，建议启用独立审计模式以记录所有操作。"
targetAudience: ["技术负责人", "企业团队", "AI研究者", "独立开发者"]
useCases: ["跨应用多步骤业务流程自动化（如数据收集-分析-报告生成）", "长时间无人值守的复杂任务执行（如代码重构、系统测试）", "AI代理行为研究与基准测试（如OSWorld、Terminal-Bench）", "需要可验证、可审计的AI工作流部署"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The long-horizon computer-use harness. Run AI agents across desktop apps and the CLI for extended periods while preserving task state and making reliable progress on complex workflows. Features fresh-context execution, durable verified state, independent auditing, recoverable progress, and native Claude Code / Codex / OpenClaw integration.

> GitHub: [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) | ⭐ 520 | Python

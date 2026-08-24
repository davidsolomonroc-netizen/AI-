---
title: "Zoetrope：Claude Code 会话实时流程可视化工具"
description: "将 Claude Code 会话实时可视化为流程图的终端与浏览器工具"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/furkankly/zoetrope"
githubStars: 193
githubOwner: "furkankly"
githubRepo: "zoetrope"
category: "dev-tools"
tags: ["agent-visualization", "claude-code", "flow-graph", "rust"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Zoetrope 将 Claude Code 的 JSONL 会话记录转化为实时流程图，帮助开发者直观理解 AI 代理的执行流程、子代理调用及工具使用情况。适合需要调试、优化或展示 AI 代理工作流的开发团队和技术负责人，提升对 AI 行为的透明度和可控性。"
vibeCodingPrompt: "1. 安装 Zoetrope：运行 `cargo install zoetrope` 或从 crates.io 获取二进制。\n2. 确保已有 Claude Code 会话记录（位于 `~/.claude/projects/` 下）。\n3. 在终端运行 `zoetrope` 启动实时流程图查看，或运行 `zoetrope --web` 在浏览器中查看。\n4. 若需集成到 Claude Code 工作流，可在会话结束后运行 `zoetrope <session-id>` 查看指定会话的流程。\n5. 使用快捷键或交互方式探索节点和工具调用详情。"
pitfallGuide: "1. 需要 Rust 环境，非开发者安装可能稍繁琐。\n2. 依赖 Claude Code 的 JSONL 格式，若格式变动可能导致解析失败。\n3. 实时更新需要会话正在运行，已结束的会话只能静态查看。\n4. 浏览器模式需编译为 WASM，首次加载可能较慢。\n5. 目前仅支持 Claude Code，不兼容其他 AI 代理工具。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者"]
useCases: ["调试和优化 Claude Code 工作流", "展示 AI 代理执行过程给团队或客户", "分析子代理调用模式以改进提示词"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Watch a Claude Code session as a live flow graph, in your terminal or your browser.

> GitHub: [furkankly/zoetrope](https://github.com/furkankly/zoetrope) | ⭐ 193 | Rust

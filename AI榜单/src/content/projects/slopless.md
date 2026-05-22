---
title: "Slopless：AI写作质量检查器"
description: "确定性规则检查Markdown中的AI废话"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/seochecks-ai/slopless"
githubStars: 349
githubOwner: "seochecks-ai"
githubRepo: "slopless"
category: "dev-tools"
tags: ["linter", "markdown", "textlint", "cli"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Slopless是一款基于确定性规则的Markdown写作质量检查工具，专门用于捕捉AI或人类写作中常见的冗余、模糊等“废话”。它适合需要确保文档清晰、简洁的技术写作团队或AI辅助写作用户，无需调用LLM即可快速输出结构化JSON报告。"
vibeCodingPrompt: "在Claude Code中，首先运行`npx slopless install-skill claude`安装Slopless技能。然后告诉Claude：“使用Slopless技能。请检查当前项目中的所有Markdown文件，运行`npx slopless \"**/*.md\"`，并基于JSON输出中的发现逐一重写有问题的段落，直到`npx slopless`返回退出码0。” 确保每次修改后重新运行检查，直到无问题。"
pitfallGuide: "1. Slopless仅支持英文Markdown文件，非英文内容会误报。\n2. 首次使用需先运行`install-skill`命令安装对应代理技能，否则无法与Claude Code或Codex集成。\n3. 输出为JSON，需自行重定向到文件保存，项目不自动管理文件名。\n4. 规则是确定性的，无法处理需要语义理解的写作问题（如逻辑错误）。\n5. 要求Node.js 22+，低版本Node可能无法运行。"
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Deterministic textlint rules and CLI for catching prose slop in Markdown

> GitHub: [seochecks-ai/slopless](https://github.com/seochecks-ai/slopless) | ⭐ 349 | TypeScript

---
title: "macOS 智能体操控框架"
description: "赋予 LLM 完全操控 Mac 的极简工具"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/browser-use/macos-harness"
githubStars: 728
githubOwner: "browser-use"
githubRepo: "macos-harness"
category: "agent-framework"
tags: ["macos", "agent", "automation", "cdp"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "macOS Harness 是一个极简框架，让 AI 代理（如 Codex 或 Claude Code）通过六个基础原语（see、key、type、click、ax、script）直接操控 Mac 上的应用、文件和浏览器，无需为每个应用单独编写工具。它适合需要自动化复杂桌面任务的技术团队或个人开发者，可大幅提升 AI 代理在真实 Mac 环境中的执行能力。"
vibeCodingPrompt: "在 Claude Code 中，输入以下 Prompt 来使用 macOS Harness：\n1. 首先，运行 `uv tool install --python 3.12 macos-harness` 安装工具。\n2. 安装后，运行 `macos-harness skill` 获取技能说明，并按照提示注册到 Claude Code 中。\n3. 运行 `macos-harness doctor` 检查权限和依赖，确保一切就绪。\n4. 使用 Python 脚本调用 `mac.see(\"应用名\")` 查看应用界面，然后通过 `mac.click()`、`mac.type()` 等原语执行操作，最后用 `mac.script()` 运行 AppleScript 完成复杂任务。\n5. 例如：`macos-harness <<'PY'` 后编写 Python 代码，实现自动化打开应用、点击按钮、输入文本等操作。"
pitfallGuide: "1. 需要 macOS 系统，且必须授予辅助功能、屏幕录制等权限，否则无法捕获界面或模拟操作。\n2. 安装时需使用 Python 3.12 和 uv，否则可能出现依赖冲突。\n3. 首次使用前务必运行 `doctor` 命令检查环境，权限缺失会导致操作失败。\n4. 操作真实应用时，若应用未在前台，可能需要先通过 `mac.see` 或 AppleScript 激活，否则点击坐标可能无效。\n5. 该工具依赖 Accessibility API，部分应用（如系统设置）可能限制自动化操作，需提前测试兼容性。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "创业者"]
useCases: ["自动化桌面应用测试", "AI 代理执行多步骤 Mac 任务", "构建个人 Mac 自动化工作流", "辅助开发调试跨应用集成"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The simplest, thinnest harness that gives an LLM complete freedom to control a Mac.

> GitHub: [browser-use/macos-harness](https://github.com/browser-use/macos-harness) | ⭐ 728 | Python

---
title: "Magpie 模型聚合器"
description: "菜单栏一键切换所有 AI Agent 的模型配置"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/yetone/magpie"
githubStars: 1411
githubOwner: "yetone"
githubRepo: "magpie"
category: "dev-tools"
tags: ["llm-router", "menu-bar", "multi-agent", "config-manager"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Magpie 解决了一个真实痛点：当你同时用 Claude Code、Codex、Gemini CLI 等多个 AI 编程工具时，每个工具都要单独配置模型和 API Key，切换模型非常麻烦。它把所有 Agent 的模型配置集中到一个菜单栏面板里，点一下就能切换，还内置本地网关统一转发请求。适合同时使用多个 AI 编程工具的开发者，以及想灵活在 DeepSeek、Kimi、GLM 等国产模型间切换以控制成本的团队。"
vibeCodingPrompt: "请帮我用 yetone/magpie 搭建一个多 Agent 模型统一管理环境：
1. 在 macOS 上通过 Homebrew 或从 GitHub Releases 下载安装 magpie（brew install yetone/tap/magpie 或直接下载 dmg）。
2. 安装后启动 magpie，确认菜单栏出现图标，点击打开面板。
3. 在面板中查看自动检测到的 AI Agent 列表（Claude Code、Codex、Gemini CLI 等），确认每个 Agent 当前使用的模型。
4. 配置本地网关：确保 magpie 的本地端点 http://127.0.0.1:3425/v1 已启动，在各 Agent 的配置文件中将其 API base URL 指向该端点。
5. 在 magpie 面板中为 Claude Code 选择 Kimi 模型，为 Codex 选择 DeepSeek 模型，点击保存。
6. 验证切换生效：运行 claude 和 codex 命令，确认它们分别使用了新配置的模型。
7. 使用 magpie tui 在终端中管理配置，或使用 magpie profiles 保存多套配置方案以便快速切换。"
pitfallGuide: "首次运行需要授予菜单栏应用辅助功能权限，否则可能无法读取其他 Agent 的配置文件
本地网关端口 3425 若被占用需手动修改配置，注意同步更新各 Agent 的 base URL
切换模型后部分 Agent 需要重启才能生效，不要以为没生效就反复切换
Windows 和 Linux 版本功能可能不如 macOS 完整，跨平台使用前先确认兼容性
修改配置文件前建议先备份，虽然 magpie 声称原子写入且保留注释，但保险起见仍应备份"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者", "企业团队"]
useCases: ["同时使用 Claude Code 和 Codex 的开发者，需要快速在 Anthropic 和 OpenAI 模型间切换", "想用国产模型（DeepSeek、Kimi、GLM）替代昂贵海外模型来降低 API 成本的团队", "需要为不同项目保存不同模型配置方案（profiles）并快速切换的开发者", "在终端中使用 magpie tui 统一管理多个 AI CLI 工具的配置"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar.

> GitHub: [yetone/magpie](https://github.com/yetone/magpie) | ⭐ 1411 | Go

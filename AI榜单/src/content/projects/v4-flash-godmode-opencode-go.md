---
title: "V4 Flash 神模式：DeepSeek 引导预设"
description: "为 DeepSeek V4 Flash 注入深度思考引导，摆脱鬼模式"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/SheberDavid/v4-flash-godmode-opencode-go"
githubStars: 506
githubOwner: "SheberDavid"
githubRepo: "v4-flash-godmode-opencode-go"
category: "agent-framework"
tags: ["deepseek", "opencode-go", "dsh", "agent-preset"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目通过一个预设配置，让 DeepSeek V4 Flash 模型从“浅思考、草率执行”的鬼模式切换到“深度规划、高质量交付”的神模式。适合依赖 DeepSeek 模型进行复杂编码或仿真任务的开发者，无需修改模型，只需安装预设即可显著提升输出质量。"
vibeCodingPrompt: "首先，确保已安装 DeepSeek Harness (dsh) 并配置好 opencode-go provider 的 deepseek-v4-flash 模型。然后，克隆此仓库并运行 ./install.sh 或手动复制 preset 到 ~/.dsh/.agent-presets，并编辑 settings.yaml 指定默认模型和 preset。重启 dsh 后，直接提交任务，模型会自动应用神模式引导。如需自定义，可修改 preset 中的 persona 提示词。"
pitfallGuide: "确保 dsh 版本为 rc.6 或更高，否则预设可能不兼容。\n安装后务必重启 dsh 才能生效。\n检查 settings.yaml 中模型 provider 和名称必须为 opencode-go 和 deepseek-v4-flash。\nWindows 用户需确认 PowerShell 可用，预设会自动适配但需测试。\n若效果不佳，可尝试调整 reasoningEffort 为 max 或检查网络连接。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["提升 DeepSeek V4 Flash 在复杂编码任务中的规划与执行质量", "用于需要深度数值仿真或几何验证的工程任务", "作为 dsh 环境中优化模型输出的参考预设"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。V4 Flash 神模式 (opencode-go)：让 opencode-go 的 DeepSeek V4 Flash 从鬼模式切换到神模式的 dsh agent preset

> GitHub: [SheberDavid/v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) | ⭐ 506 | JavaScript

---
title: "OpenGrok：Grok Bot 万能模型切换器"
description: "一键更换 Grok Bot 中的任意 AI 模型"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/OnlyTerp/opengrok"
githubStars: 385
githubOwner: "OnlyTerp"
githubRepo: "opengrok"
category: "dev-tools"
tags: ["grok", "model-router", "llm", "openai-compatible"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OpenGrok 让非技术用户也能轻松将 Grok Bot 默认模型替换为其他任意兼容模型（如 Claude、Gemini、本地模型等），通过简单的图形界面选择、测试和保存配置。适合希望摆脱单一模型限制、在不同 AI 模型间灵活切换的个人或团队，无需编写代码或手动修改配置文件。"
vibeCodingPrompt: "请帮我用 OpenGrok 项目搭建一个自定义模型切换器：
1. 克隆仓库并运行 `python setup.py` 完成基础安装；
2. 打开模型选择器界面，为每个 agent 下拉选择目标模型；
3. 点击“测试”按钮验证模型连接是否正常，确认响应质量；
4. 点击“保存”写入配置，之后 Grok Bot 会自动使用新模型；
5. 若遇到问题，运行 `python tools/doctor.py` 诊断并修复。"
pitfallGuide: "1. 安装前确保已安装 Grok Bot 且版本兼容；\n2. 模型 API 密钥需自行准备，且仅保存在本地，不要分享；\n3. 切换模型后需重新测试，部分模型可能不支持 Grok Bot 原生功能；\n4. 若 Grok Bot 更新，需重新运行 doctor.py 检查配置是否失效；\n5. 不要同时运行多个配置修改工具，避免冲突。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI 研究者"]
useCases: ["在 Grok Bot 中接入企业私有模型以节省成本", "开发者快速对比不同 LLM 在特定任务上的表现", "团队统一管理多模型路由策略，提升响应质量"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Run any model in Grok Bot — one-command setup, model picker UI, evidence-based provider wire maps, and an update-proof doctor. Not farming you, arming you.

> GitHub: [OnlyTerp/opengrok](https://github.com/OnlyTerp/opengrok) | ⭐ 385 | JavaScript

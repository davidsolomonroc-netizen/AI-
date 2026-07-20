---
title: "Codex 自动换肤引擎"
description: "传一张图，Codex 自动生成并应用皮肤"
publishDate: 2026-07-20
featured: false
githubUrl: "https://github.com/Finderchangchang/codex-autoskin"
githubStars: 99
githubOwner: "Finderchangchang"
githubRepo: "codex-autoskin"
category: "agent-framework"
tags: ["agent", "skin", "theme", "codex"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Codex AutoSkin 让你只需发送一张图片给 Codex，即可自动生成并应用自定义皮肤，无需手动编辑任何文件。适合希望快速个性化 Codex 桌面应用外观的用户，尤其是设计师和开发者。"
vibeCodingPrompt: "1. 将项目仓库链接和一张图片发送给 Claude Code。
2. 告诉 Claude Code 安装这个皮肤引擎：'Install this Codex skin engine: https://github.com/Finderchangchang/codex-autoskin'
3. 让 Claude Code 使用图片生成主题并应用。
4. 如果需要自定义细节，可参考 THEME-SPEC.md 让 Claude Code 调整。"
pitfallGuide: "1. 图片最好用横屏、主体在右侧、无文字和水印，效果最佳。\n2. 不要用他人肖像或受版权保护的图片公开分发主题，个人使用可以放在 themes-private/ 目录。\n3. 项目只负责生成基础皮肤（背景+调色板），帧、贴纸等高级定制需参考 THEME-SPEC.md 手动扩展。\n4. 确保 Codex 桌面应用已安装且版本兼容。\n5. 恢复默认皮肤只需一条命令，但建议先备份当前配置。"
targetAudience: ["独立开发者", "设计师", "技术负责人"]
useCases: ["快速个性化 Codex 界面", "为团队统一品牌皮肤", "从灵感图秒变应用主题"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。发一张图给你的 Codex，它自己给自己换肤 | Send one image to your Codex and it reskins itself. Agent-native skin engine for the Codex desktop app.

> GitHub: [Finderchangchang/codex-autoskin](https://github.com/Finderchangchang/codex-autoskin) | ⭐ 99 | JavaScript

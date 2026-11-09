---
title: "土耳其语反AI写作去痕工具"
description: "消除土耳其语文本中的AI写作痕迹，重建地道表达"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/yucezerey/turkish-anti-ai-skill"
githubStars: 275
githubOwner: "yucezerey"
githubRepo: "turkish-anti-ai-skill"
category: "dev-tools"
tags: ["Turkish NLP", "AI Humanizer", "Agent Skill", "Text Rewriting"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "解决AI生成的土耳其语文本机械、翻译腔重的问题，让内容读起来像真人写的。适合土耳其语内容创作者、营销团队和本地化公司使用。"
vibeCodingPrompt: "1. 在 Claude Code 中克隆项目：git clone https://github.com/yucezerey/turkish-anti-ai-skill。2. 阅读 README 的安装部分，将 skill 文件夹复制到 Claude Code 的 skills 目录（通常为 ~/.claude/skills/）。3. 重启 Claude Code 并输入 /skill list 确认 turkish-anti-ai-skill 已加载。4. 创建一个测试文件 test.txt，粘贴一段 AI 生成的土耳其语文本。5. 在 Claude Code 中调用 skill：/skill turkish-anti-ai-skill 并指定文件路径，观察输出是否更自然。6. 如需批量处理，编写一个 Python 脚本调用项目的 CLI 检测器（参考 README 的 CLI 部分），遍历文件夹中的 .txt 文件并输出改写结果。"
pitfallGuide: "1. 确保 Claude Code 版本支持 Agent Skills 规范（v1.0），否则无法加载。\n2. 土耳其语字符编码需为 UTF-8，否则处理可能出错。\n3. 该工具主要针对土耳其语，其他语言效果有限。\n4. 改写后需人工校对，避免过度修正导致语义偏差。\n5. 批量处理时注意文件备份，防止原始内容丢失。"
targetAudience: ["内容创作者", "产品经理", "企业团队", "独立开发者"]
useCases: ["土耳其语营销文案去AI化", "本地化翻译文本润色", "社交媒体内容自然化改写", "学术论文语言风格优化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Türkçe metinlerdeki yapay zeka izlerini (AI slop, translationese, çeviri kokan cümle mimarisi ve TDK hatalarını) temizleyen Agent Skill ve Humanizer paketi.

> GitHub: [yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill) | ⭐ 275 | Python

---
title: "SlopTrim：本地AI写作痕迹检测器"
description: "零依赖本地检测AI写作模式，净化文本质量。"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/seyedehsanhadi/sloptrim"
githubStars: 149
githubOwner: "seyedehsanhadi"
githubRepo: "sloptrim"
category: "dev-tools"
tags: ["AI-detection", "prose-linter", "claude-code", "zero-dependency"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "SlopTrim 是一个本地运行的命令行工具，用于检测AI生成的写作痕迹，帮助用户识别并修正文本中的AI腔调。它无需网络和模型，适合需要保证内容自然度的写作者、编辑和AI代理开发者，确保输出更接近人类写作风格。"
vibeCodingPrompt: "1. 首先，安装 sloptrim：使用 pip install sloptrim 或从 GitHub 克隆仓库。\n2. 在 Claude Code 中，添加 sloptrim 作为插件或技能，配置它在每次保存文件后自动运行。\n3. 在你的工作流程中，指示 Claude Code 在生成或修改任何散文文件后调用 sloptrim 检测分数，并根据反馈修改标记的文本片段。\n4. 使用 sloptrim 的 CLI 命令手动扫描特定文件或目录，集成到你的编辑器中。"
pitfallGuide: "1. sloptrim 只检测散文，不处理代码，请勿用于代码文件。\n2. 检测分数仅供参考，并非绝对标准，需结合上下文判断。\n3. 零依赖设计意味着功能有限，不支持复杂模型或网络调用。\n4. 安装时需确保 Python 3.9+ 环境，否则可能无法运行。\n5. 作为命令行工具，无图形界面，非技术用户需熟悉终端操作。"
targetAudience: ["独立开发者", "内容创作者", "AI 研究者", "技术负责人"]
useCases: ["净化AI生成的博客文章或文档，使其更自然", "在AI代理工作流中自动检测并修正写作风格", "作为编辑器插件，实时提示AI写作模式"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A local detector for AI-writing patterns. Scores every prose file your agent saves. Python standard library only, no network, no model.

> GitHub: [seyedehsanhadi/sloptrim](https://github.com/seyedehsanhadi/sloptrim) | ⭐ 149 | Python

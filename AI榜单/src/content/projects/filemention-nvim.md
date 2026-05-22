---
title: "文件路径快速插入器"
description: "Neovim中快速插入@文件路径"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/not-manu/filemention.nvim"
githubStars: 58
githubOwner: "not-manu"
githubRepo: "filemention.nvim"
category: "dev-tools"
tags: ["neovim", "completion", "markdown"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个插件让Neovim用户在编辑Markdown或代码时，通过输入@符号快速搜索并插入文件路径，提升文档链接效率。适合需要频繁引用本地文件的开发者、技术写作者和AI辅助编码场景。"
vibeCodingPrompt: "1. 使用Claude Code打开Neovim，确保已安装not-manu/filemention.nvim。
2. 在Markdown文件中输入@，触发文件路径补全。
3. 继续输入文件名或路径关键词，插件会实时搜索并展示匹配文件。
4. 选择目标文件，自动插入完整路径。
5. 可结合其他补全插件（如cmp）使用，增强AI编码工作流。"
pitfallGuide: "1. 需要Neovim 0.7+版本，旧版本可能不兼容。
2. 默认只搜索当前工作目录，跨项目需要手动配置路径。
3. 如果与其他补全插件冲突，需调整触发键或优先级。
4. 大型项目首次搜索可能较慢，建议限制搜索深度。
5. 不支持Windows路径反斜杠，需确保使用Unix风格路径。"
targetAudience: ["独立开发者", "技术负责人", "内容创作者"]
useCases: ["在Markdown笔记中快速链接项目文件", "在代码注释中引用其他模块路径", "在AI辅助编码时自动补全文件引用", "配合文档生成工具管理资源路径"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Neovim中快速插入@文件路径

> GitHub: [not-manu/filemention.nvim](https://github.com/not-manu/filemention.nvim) | ⭐ 58 | ["neovim",

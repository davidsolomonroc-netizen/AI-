---
title: "Neovim文件提及插件"
description: "Neovim中快速插入@文件路径"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/not-manu/filemention.nvim"
githubStars: 58
githubOwner: "not-manu"
githubRepo: "filemention.nvim"
category: "dev-tools"
tags: ["neovim", "completion", "ai", "markdown"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个Neovim插件，让你在编写提示词、笔记或提交信息时，通过输入@符号快速搜索并插入文件路径，提升工作效率。适合使用Neovim的开发者、AI提示工程师和内容创作者。"
vibeCodingPrompt: "1. 确保已安装Neovim 0.9+和lazy.nvim插件管理器。
2. 在lua配置中添加插件：{ \"not-manu/filemention.nvim\", event = \"InsertEnter\", opts = {} }。
3. 根据你的补全引擎（nvim-cmp或blink.cmp）配置source。
4. 在markdown或文本文件中进入插入模式，输入@开始搜索文件。
5. 使用模糊搜索选择目标文件，自动插入@path/to/file格式的提及。"
pitfallGuide: "默认只在markdown、text和gitcommit文件类型中激活，其他文件类型需手动设置filetypes = \"*\"。
需要配置补全引擎（nvim-cmp或blink.cmp）才能正常使用。
依赖外部查找工具（如fd或find），确保系统已安装。
如果使用git作为root，插件会从git仓库根目录搜索文件。
隐藏文件和node_modules默认被排除，可通过配置调整。"
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。@ file mentions in neovim. for prompts, notes, commits.

> GitHub: [not-manu/filemention.nvim](https://github.com/not-manu/filemention.nvim) | ⭐ 58 | Lua

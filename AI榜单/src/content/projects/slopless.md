---
title: "废话检测器"
description: "检查Markdown中AI废话的确定性规则工具"
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
commercialSummary: "Slopless 自动扫描 Markdown 文档，标记并移除 AI 生成的空洞内容（如“总之”“值得注意的是”等废话），帮助内容创作者和团队提升文档质量，避免被 AI 废话淹没。适合需要维护高质量技术文档或博客的团队。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/seochecks-ai/slopless.git
2. 进入目录：cd slopless
3. 安装依赖：npm install
4. 运行检测：npx slopless check your-doc.md
5. 集成到 Claude Code：在项目根目录创建 .claude.md 文件，写入规则：“运行 slopless 检测所有 .md 文件，自动修复并输出报告。”
6. 使用 Claude Code 执行：claude run \"slopless check --fix *.md\""
pitfallGuide: "1. 规则基于确定性模式，可能漏检变体废话
2. 不支持中文内容，仅适用于英文 Markdown
3. 自动修复可能误删有意使用的短语
4. 需要 Node.js 环境，非纯浏览器工具"
targetAudience: ["内容创作者", "技术文档作者", "技术负责人", "独立开发者"]
useCases: ["技术文档质量审查", "博客文章废话清理", "团队文档规范检查", "AI 生成内容后处理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。确定性规则检查Markdown中的AI废话

> GitHub: [seochecks-ai/slopless](https://github.com/seochecks-ai/slopless) | ⭐ 349 | ["linter",

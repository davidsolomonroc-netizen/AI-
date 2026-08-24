---
title: "叙灯 NarraLume"
description: "开源 AI 辅助长篇小说写作工作台"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/abligail/narralume"
githubStars: 89
githubOwner: "abligail"
githubRepo: "narralume"
category: "other"
tags: ["ai-writing", "long-form", "self-hosted", "creative-writing"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "NarraLume 是一个面向长篇小说的开源写作工具，将故事设定、章节管理、版本控制和 AI 辅助写作整合在一个环境中。它适合需要保持长篇故事连贯性的作者，以及希望将 AI 生成内容严格纳入审阅流程的写作团队。无需 AI 模型即可完成全部核心写作功能，AI 生成的内容始终作为草稿，由作者确认后才纳入正文。"
vibeCodingPrompt: "使用 NarraLume 搭建一个 AI 辅助长篇小说写作环境：
1. 克隆仓库并安装依赖：`git clone https://github.com/abligail/narralume && cd narralume && npm install`
2. 启动开发服务器：`npm run dev`，访问本地地址，创建新项目。
3. 在设置中配置你的 LLM API（如 OpenAI）和接口语言（中文/英文）。
4. 创建故事设定（bible），添加角色、世界观和章节大纲。
5. 开始手写章节，或选中文本、章节，调用 AI 生成续写/修订建议。
6. 审阅 AI 生成的草稿，接受或拒绝，保存版本。
7. 导出最终稿件或备份项目。"
pitfallGuide: "1. 部署需要 Node.js 环境，非技术用户需借助 Docker 或托管版（demo）才能快速体验。\n2. 首次运行需要配置 LLM API 密钥，否则 AI 功能不可用，但核心写作功能不受影响。\n3. 项目目前星数较少，社区和插件生态尚不成熟，遇到问题需自行查阅文档或提 issue。\n4. 长文档性能可能随章节增多而下降，建议定期导出备份，避免数据丢失。\n5. 界面为中文/英文双语，但部分文档可能只提供英文版本，中文用户需切换阅读。"
targetAudience: ["内容创作者", "独立开发者", "产品经理", "AI 研究者"]
useCases: ["长篇小说创作与故事设定管理", "AI 辅助写作草稿生成与人工审阅", "多版本稿件管理和导出交付", "自托管写作工具，保护创作数据隐私"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source AI-assisted writing studio for long-form fiction. 故事设定、正文版本、AI 协作、审稿与交付一体化的长篇小说写作工具。

> GitHub: [abligail/narralume](https://github.com/abligail/narralume) | ⭐ 89 | TypeScript

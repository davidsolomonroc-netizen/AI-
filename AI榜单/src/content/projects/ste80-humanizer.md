---
title: "STE80 文本人性化器"
description: "去除AI写作痕迹，将文本改写至简化技术英语标准"
publishDate: 2026-11-16
featured: false
githubUrl: "https://github.com/Dodaios/ste80-humanizer"
githubStars: 707
githubOwner: "Dodaios"
githubRepo: "ste80-humanizer"
category: "workflow-automation"
tags: ["humanizer", "writing", "claude-skills", "plain-language"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目能自动把AI生成的文字改写成更自然、更像真人写的风格，同时保留原意，特别适合需要发布技术文档、博客或客户沟通内容的场景。适合内容创作者、技术写作者和需要批量处理文案的团队使用。"
vibeCodingPrompt: "1. 在 Claude Code 中安装该技能：运行 `npx skills add Dodaios/ste80-humanizer` 或按 README 指引克隆仓库并配置为 agent skill。
2. 准备一段待处理的 AI 生成文本，保存为 input.txt。
3. 在 Claude Code 中调用该技能，输入提示：“使用 STE80 Humanizer 改写 input.txt 中的文本，去除 AI 写作痕迹并简化到 ASD-STE100 风格”。
4. 检查输出结果，对比原文确保语义未变，必要时手动调整。
5. 将改写后的文本用于你的博客、文档或客户邮件中。"
pitfallGuide: "该技能依赖 agent 环境（如 Claude Code），需先配置好相应工具链。\n改写可能改变专业术语的精确性，技术文档需人工复核。\n过度简化可能导致复杂概念丢失细节，建议保留原文对照。\n非英语文本效果有限，主要针对英文写作优化。\n安装时注意 skills.sh 的版本兼容性，避免与现有技能冲突。"
targetAudience: ["内容创作者", "技术写作者", "产品经理", "独立开发者"]
useCases: ["技术博客去AI化改写", "客户邮件与文档简化", "营销文案人性化处理", "内部技术文档标准化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。STE80 Humanizer: agent skill that removes AI tells and rewrites text 80% of the way to ASD-STE100 (Simplified Technical English), the method Andrej Karpathy shared.

> GitHub: [Dodaios/ste80-humanizer](https://github.com/Dodaios/ste80-humanizer) | ⭐ 707 | Python

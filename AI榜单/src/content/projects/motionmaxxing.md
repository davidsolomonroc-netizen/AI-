---
title: "动效美颜师"
description: "把 AI 生成的粗糙视频变成专业动效作品"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/Tejashmakwana/motionmaxxing"
githubStars: 145
githubOwner: "Tejashmakwana"
githubRepo: "motionmaxxing"
category: "multimodal"
tags: ["motion-graphics", "agent-skill", "video", "claude-code"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个让 AI 代理（如 Claude Code）学会专业动效设计规范的技能包，能把 AI 生成的廉价感视频自动优化成有设计感的影片。适合做短视频、产品演示、品牌宣传的内容创作者和小团队，不需要动效设计经验就能产出专业级效果。"
vibeCodingPrompt: "1. 在 Claude Code 中克隆项目：git clone https://github.com/Tejashmakwana/motionmaxxing，进入目录后阅读 SKILL.md 了解技能定义。
2. 确保环境满足 Node 22+，并安装 Chrome 和 ffmpeg。
3. 在 Claude Code 中加载该技能：将 SKILL.md 内容作为系统提示或使用 /skill 命令加载。
4. 准备一段 AI 生成的视频（或文本脚本），向 Claude 提出：'用 motionmaxxing 技能优化这段视频的动效，输出为 MP4'。
5. Claude 会调用项目中的脚本，应用缓动曲线、排版调整等规范，生成优化后的视频文件。
6. 运行项目自带的 mog check 门禁（G0-G5）验证输出质量，根据报告调整参数。"
pitfallGuide: "需要 Node 22+ 和 Chrome、ffmpeg 环境，安装前先确认版本\n项目处于早期发布阶段，API 和技能定义可能变动，建议锁定版本\n对非技术用户，环境配置（尤其是 ffmpeg）可能耗时超过 10 分钟\n生成的视频效果依赖输入素材质量，AI 原始视频太差可能优化有限\n建议在 Claude Code 中先小规模测试再批量处理，避免资源浪费"
targetAudience: ["内容创作者", "独立开发者", "创业者", "产品经理"]
useCases: ["短视频创作者快速提升 AI 生成视频的动效质感", "产品团队制作品牌宣传片和演示视频", "营销人员批量生成有设计感的社交媒体视频", "设计师用 AI 代理辅助动效设计和迭代"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Looksmaxxing for motion graphics. An agent skill that turns AI slop videos into films that look made by a motion designer.

> GitHub: [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | ⭐ 145 | JavaScript

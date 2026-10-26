---
title: "AI 创业七步 Skill 包"
description: "一人公司做 AI 产品的 7 步 Agent Skill 合集"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/huaxialucaicaizi/ai-startup-skills"
githubStars: 236
githubOwner: "huaxialucaicaizi"
githubRepo: "ai-startup-skills"
category: "workflow-automation"
tags: ["agent-skills", "startup", "claude-code", "entrepreneurship"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 5
commercialSummary: "把创业从想法验证到公司注册的七个关键环节，做成 AI 编程助手可以直接调用的技能包。适合想用 AI 工具独立做产品、但不知道从哪一步开始的个人创业者。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/huaxialucaicaizi/ai-startup-skills，进入目录阅读 README 的快速开始部分。
2. 按 README 说明把 skills 目录链接或复制到你的 Claude Code / Cursor 技能目录（通常是 ~/.claude/skills 或项目内 .claude/skills）。
3. 在 Claude Code 中打开一个新会话，输入你的创业想法，例如「我想做一个面向小商家的 AI 记账工具」，让总入口 skill 判断你处于哪个阶段。
4. 按引导依次调用子 skill：先用 MVP 验证 skill 生成用户访谈问卷和验证清单，收集 10 条反馈后再进入 BP skill 生成商业计划书草稿。
5. 用定价 skill 设计三档价格方案，用获客 skill 生成冷启动渠道清单，最后用注册 skill 列出注册公司所需材料和流程。
6. 每一步的产出保存到项目 docs 目录，方便后续 skill 串联引用。"
pitfallGuide: "技能包是流程引导而非自动执行，需要你主动提供真实业务信息和用户反馈，否则产出会很空泛
七个 skill 之间有依赖顺序，跳过验证直接写 BP 会导致后续定价和获客缺乏依据
政策导航和公司注册部分可能偏向特定地区（如中国），海外创业者需自行核实当地法规
建议先只安装总入口 skill 和当前阶段对应的子 skill，一次装全套容易在会话中选错技能
AI 生成的 BP 和定价方案需人工复核，不要直接用于融资路演或对外报价"
targetAudience: ["独立开发者", "创业者", "产品经理"]
useCases: ["个人开发者从零验证 AI 产品想法并撰写商业计划书", "一人公司设计定价策略和冷启动获客方案", "创业大赛或孵化器申请前快速生成路演材料和政策补贴清单"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。创业公司做 AI 产品的 7 步 Agent Skill 合集：验证 → BP → 政策 → 路演 → 获客 → 定价 → 注册。

> GitHub: [huaxialucaicaizi/ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) | ⭐ 236 | Python

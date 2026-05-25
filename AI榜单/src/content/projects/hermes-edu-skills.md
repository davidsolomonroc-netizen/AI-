---
title: "Hermes Edu Skills 中文教育 Agent 技能包"
description: "188个结构化教育技能，让AI理解中国课堂"
publishDate: 2026-05-25
featured: false
githubUrl: "https://github.com/zhongweiv/hermes-edu-skills"
githubStars: 90
githubOwner: "zhongweiv"
githubRepo: "hermes-edu-skills"
category: "agent-framework"
tags: ["education", "k12", "hermes-agent", "china-edtech"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一套专为中国教育场景设计的 Agent Skill Pack，覆盖学前启蒙、教材同步、备考复习、拍照答疑、错题复盘等188个结构化技能。适合AI学习助手开发者、教育科技公司、教师和培训机构，可直接接入Hermes Agent或导出到Cursor/Claude Code等工具，快速构建懂中国教材的AI教育应用。"
vibeCodingPrompt: "1. 克隆项目到本地：git clone https://github.com/zhongweiv/hermes-edu-skills.git\n2. 查看catalog.json了解所有188个技能的元数据，包括触发信号、适用角色、参数维度。\n3. 选择具体技能（例如“同步练习”）的SKILL.md文件，了解其输入输出规范。\n4. 在Claude Code中加载该技能目录，或通过Hermes Agent的skills命令安装。\n5. 编写自定义Prompt调用技能：例如“请根据人教版数学三年级上册第三单元生成5道同步练习题，难度中等”。\n6. 如需二次开发，可修改SKILL.md中的参数和触发规则，或新增自定义技能。"
pitfallGuide: "1. 部分技能依赖Hermes Agent的特定路由机制，非Hermes环境需手动适配\n2. 技能覆盖中国教材版本（人教版/苏教版等），其他版本需自行扩展\n3. demo视频约800KB，首次访问可能加载较慢\n4. 拍照答疑技能需要图片输入能力，需确保Agent支持多模态\n5. 教师工具类技能涉及家校沟通，需注意数据隐私合规"
targetAudience: ["独立开发者", "创业者", "产品经理", "企业团队", "AI 研究者", "内容创作者"]
useCases: ["构建AI学习助手，提供教材同步练习和错题复盘", "开发教师备课工具，自动生成教案和练习题", "搭建亲子陪学应用，实现自然问答和阅读写作辅导", "集成到企业级教育平台，支持拍照答疑和考试备考"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。中文教育 Agent Skill Pack：教材同步、备考复习、拍照答疑、错题复盘、亲子陪学、阅读写作和教师工具，Hermes Agent 可直接使用，也可导出到 OpenClaw/Codex/Cursor/Claude Code。

> GitHub: [zhongweiv/hermes-edu-skills](https://github.com/zhongweiv/hermes-edu-skills) | ⭐ 90 | JavaScript

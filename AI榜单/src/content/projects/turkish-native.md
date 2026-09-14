---
title: "土耳其语母语写作技能"
description: "让 AI 写出地道土耳其语，消除翻译腔。"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/oguzhankayan/turkish-native"
githubStars: 71
githubOwner: "oguzhankayan"
githubRepo: "turkish-native"
category: "workflow-automation"
tags: ["turkish", "localization", "agent-skill", "copywriting"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 4
commercialSummary: "土耳其语市场出海的产品文案和本地化内容常带有翻译腔，读起来像机翻，影响品牌信任和转化。这个开源技能包让 Claude、ChatGPT 等 AI 代理在写作时自动检查并重写不自然的土耳其语句式，适合出海土耳其市场的产品经理、本地化团队和内容运营使用。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/oguzhankayan/turkish-native，将 SKILL.md 和 examples 目录复制到你的项目 skills 文件夹。\n2. 在 Claude Code 或 Cursor 中，把 SKILL.md 作为系统提示或技能文件加载，确保代理在生成土耳其语文案时引用其中的检查清单。\n3. 准备一份待审校的土耳其语文本（如产品落地页、邮件模板），保存为 input.txt。\n4. 向代理发送指令：读取 input.txt，按 SKILL.md 的规则逐句重写，输出前后对比表格，并标注每处修改的原因（如从句结构、格后缀、动词搭配）。\n5. 将结果保存为 output.md，人工抽查 3-5 条修改是否符合母语习惯，必要时在 SKILL.md 中补充你的品牌术语表。"
pitfallGuide: "技能包仅提供写作规则，不包含土耳其语语法检查器，需要依赖 AI 代理本身的土耳其语能力。\n对高度专业领域（法律、医疗）的术语，需人工确认，避免过度改写导致语义偏差。\n该技能针对土耳其语，其他语言不适用，不要混用。\n部署前确保代理有足够的上下文窗口，长文档建议分段处理。\n示例中的修改风格偏营销文案，正式文档可能需要调整语气规则。"
targetAudience: ["产品经理", "内容创作者", "企业团队", "独立开发者"]
useCases: ["土耳其语产品落地页和营销文案的 AI 生成与润色", "本地化团队审校翻译腔，提升母语自然度", "出海土耳其市场的邮件、推送通知批量改写", "为 AI 代理配置土耳其语写作规范，集成到内容工作流"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Agent skill for writing native Turkish and removing translationese from AI and localized copy.

> GitHub: [oguzhankayan/turkish-native](https://github.com/oguzhankayan/turkish-native) | ⭐ 71 | Python

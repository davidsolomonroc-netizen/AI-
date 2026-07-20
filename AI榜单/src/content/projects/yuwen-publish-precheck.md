---
title: "发布前审"
description: "AI预审抖音小红书视频号内容合规"
publishDate: 2026-07-20
featured: false
githubUrl: "https://github.com/yuwen-cool/yuwen-publish-precheck"
githubStars: 329
githubOwner: "yuwen-cool"
githubRepo: "yuwen-publish-precheck"
category: "other"
tags: ["content-compliance", "ai-review", "chinese-platforms", "agent-skills"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "帮助内容创作者在发布前用AI检测抖音、小红书、视频号的违规风险，定位问题句子并给出合规修改建议。适合内容运营、自媒体博主和品牌团队，减少因违规导致的限流或下架。"
vibeCodingPrompt: "1. 克隆仓库到本地并安装Python 3。\n2. 在项目根目录运行`python precheck.py`启动交互式审核。\n3. 粘贴你的稿件（如带货口播、小红书笔记），AI会逐句分析违规风险并给出修改建议。\n4. 根据输出修改稿件后，可再次运行复检直到零命中。\n5. 如需定制规则，修改`rules/`目录下的规则文件。"
pitfallGuide: "1. 项目依赖本地Python环境，非技术人员需简单命令行操作。\n2. 审核结果基于公开规则和AI模型，不保证100%过审，平台算法可能动态调整。\n3. 建议定期更新规则库（从GitHub拉取最新版）。\n4. 敏感词库不包含所有平台黑话，需结合自身经验补充。\n5. 修改建议仅供参考，最终发布前应人工复核。"
targetAudience: ["内容创作者", "创业者", "产品经理", "企业团队"]
useCases: ["带货口播稿发布前合规检查", "小红书笔记内容预审", "视频号文案违规风险排查", "自媒体团队批量内容审核"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。发布前审｜发抖音/小红书/视频号前先让 AI 审一遍：哪句踩线、依据哪条官方规则、给能直接用的改法。38 篇真实样本校准判定尺度，72 条官方原文引文可查证，你踩过的坑沉淀成本地规则库越用越准。不承诺过审，不教绕审。

> GitHub: [yuwen-cool/yuwen-publish-precheck](https://github.com/yuwen-cool/yuwen-publish-precheck) | ⭐ 329 | Python

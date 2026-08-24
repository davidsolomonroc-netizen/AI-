---
title: "Emotion Ball 表情引擎"
description: "AI 助手的 32 种 SVG 表情实时驱动引擎"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/sam70361/emotion-ball"
githubStars: 245
githubOwner: "sam70361"
githubRepo: "emotion-ball"
category: "multimodal"
tags: ["emotion-engine", "svg-animation", "ai-agent", "vanilla-js"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Emotion Ball 为 AI 助手（聊天机器人、桌面宠物等）提供即插即用的情绪表达层，通过一个 emotionId 即可切换 32 种表情，无需图片资源或框架。适合希望快速为 AI 产品增加拟人化交互的开发者和产品团队，但注意球形角色视觉形象仅限学习，商业使用需获取引擎授权。"
vibeCodingPrompt: "在 Claude Code 中集成 Emotion Ball：
1. 克隆仓库并运行 npm install（若有依赖，实际为零依赖）
2. 将 emotion-ball/ 目录复制到你的项目，引入 emotion-engine.js 和 styles.css
3. 创建 EmotionBall 实例：const ball = new EmotionBall({ container: '#app', shape: 'blob', theme: 'dark' })
4. 监听 AI 输出，当收到 emotionId 时调用 ball.setEmotion(emotionId)
5. 如需自定义表情，编辑 emotion-config.js 中的表情数据（眼形、嘴形参数）
6. 测试不同情绪切换，确保动画流畅"
pitfallGuide: "1. 球形角色视觉形象仅供学习，商业使用需获取引擎授权，避免侵权
2. 确保 emotionId 与配置中的 ID 严格匹配，否则表情不切换
3. 零依赖但需现代浏览器支持 SVG 和 ES6，老浏览器可能不兼容
4. 多实例时注意容器 ID 唯一性，避免状态冲突
5. 自定义表情时需理解动画原语和关键帧序列，否则可能动画异常"
targetAudience: ["独立开发者", "创业者", "产品经理", "企业团队", "AI 研究者"]
useCases: ["聊天机器人情绪反馈", "桌面宠物表情动画", "悬浮助手动态提示", "AI 教育工具互动"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Emotion Ball 是一套面向 AI 助手的表情引擎:32 种状态表情全部由纯 SVG 与原生 JavaScript 实时驱动,零框架、零图片资源。AI 侧只需输出一个 emotionId,小球即可切换到对应表情,可直接用作聊天机器人、桌面宠物、悬浮助手的情绪表达层。

> GitHub: [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | ⭐ 245 | JavaScript

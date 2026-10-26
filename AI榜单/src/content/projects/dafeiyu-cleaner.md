---
title: "大肥鱼消除计划"
description: "识别并清理B站AI机器人评论的浏览器插件"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/liyupi/dafeiyu-cleaner"
githubStars: 94
githubOwner: "liyupi"
githubRepo: "dafeiyu-cleaner"
category: "other"
tags: ["browser-extension", "bot-detection", "bilibili", "deepseek"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个插件帮你自动识别并隐藏B站评论区里由DeepSeek等大模型驱动的机器人账号，让评论区回归真实交流。适合经常刷B站、反感AI水军和自动回复的普通用户，也适合想研究AI内容检测的开发者参考。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/liyupi/dafeiyu-cleaner.git 并进入目录。2. 阅读 README 和 docs 了解插件架构（manifest.json、content scripts、背景脚本）。3. 在 Chrome 中打开扩展管理页面，开启开发者模式，点击“加载已解压的扩展程序”，选择项目根目录。4. 打开 B 站任意视频评论区，观察插件是否自动标记疑似 AI 评论。5. 如需 DeepSeek API 精判，在插件设置中填入 API Key 并测试。6. 根据需求修改识别规则（如关键词列表、检测阈值），重新加载插件验证效果。7. 可基于现有代码开发类似插件，用于其他平台的 AI 内容检测。"
pitfallGuide: "安装前确认浏览器版本（Chrome MV3 或 Firefox 140+）
DeepSeek API 精判需要自行申请 API Key 并注意调用成本
插件仅本地隐藏评论，不会真正删除或举报，需理解其作用范围
自定义规则时避免误伤正常用户，建议先小范围测试
Firefox 安装包与 Chromium 版不同，需从 Releases 下载对应版本"
targetAudience: ["内容创作者", "独立开发者", "AI 研究者"]
useCases: ["B站评论区净化，隐藏AI机器人评论", "研究AI生成内容的检测与识别方法", "作为浏览器插件开发的学习案例", "基于现有代码定制其他平台的AI内容过滤工具"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。DeepSeek 蓝色大肥鱼消除计划：识别并清理 B 站（Bilibili）评论区中由 DeepSeek 大模型、AI Agent 驱动的机器人账号（大肥鱼）的 Chrome / Edge / Firefox 浏览器插件。离线规则 + DeepSeek API 精判，AI 评论检测、空间主页鉴定、鲸鱼娘一键清场。DeepSeek AI bot detector for Bilibili comments.

> GitHub: [liyupi/dafeiyu-cleaner](https://github.com/liyupi/dafeiyu-cleaner) | ⭐ 94 | JavaScript

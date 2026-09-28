---
title: "JevChat 聊天回复助手"
description: "截屏 OCR 读聊天，AI 给三条候选回复，手动发送"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/jev-chat/jev-chat-windows"
githubStars: 630
githubOwner: "jev-chat"
githubRepo: "jev-chat-windows"
category: "workflow-automation"
tags: ["ocr", "chat-assistant", "local-first", "pyqt"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "JevChat 是一款挂在聊天窗口旁的辅助工具，能自动读取对方发来的消息，用 AI 判断对方情绪和意图，并给出三条候选回复，你只需点一下填入、自己确认后发送。适合经常用微信等聊天工具沟通、希望提高回复效率又不想让 AI 替自己发送消息的普通用户和职场人士。"
vibeCodingPrompt: "1. 从 GitHub Releases 页面下载 jev-chat-windows 最新版 zip 包并解压到固定目录。
2. 双击运行 jev-chat-windows.exe，首次启动会弹出设置页。
3. 在设置页的『判断 · Jev』卡片中填入 OpenRouter 或 TypeSafe 的 API key（用于判断意图和情绪）。
4. 在『起草 · 语言模型』卡片中填入 DeepSeek 官网的 API key（用于生成候选回复）。
5. 选择你们的关系（恋人/朋友/同事/家人/自定义），保存设置。
6. 打开聊天窗口（如微信），保持窗口可见，不要最小化。
7. 对方发来消息后，悬浮窗会自动显示判断摘要和三条候选回复，点击『填入』将文字放入输入框，手动检查后按发送。
8. 如需群聊指定回复对象，在设置中开启对应选项；暂停读取可拨动标题栏开关。"
pitfallGuide: "exe 未签名，Windows SmartScreen 会拦截，需点击『更多信息』→『仍要运行』。
首次使用必须配置两个 API key（判断和起草各一个），且需确保网络能访问对应服务。
起草默认使用 DeepSeek 官网直连，若使用其他服务需自行修改配置。
聊天窗口必须保持可见（可被其他窗口覆盖），最小化后无法读取消息。
程序不会自动发送消息，所有回复都需手动确认后发送，避免误操作。"
targetAudience: ["独立开发者", "产品经理", "内容创作者", "企业团队"]
useCases: ["日常微信聊天中快速生成回复建议", "客服或销售场景中辅助回复客户消息", "社交恐惧或沟通困难者辅助表达", "多语言聊天时辅助生成得体的回复"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。JevChat-Windows：聊天窗口旁挂的回复辅助。窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动

> GitHub: [jev-chat/jev-chat-windows](https://github.com/jev-chat/jev-chat-windows) | ⭐ 630 | Python

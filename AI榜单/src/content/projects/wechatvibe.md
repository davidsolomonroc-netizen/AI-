---
title: "微信聊天情绪分析器"
description: "本地或API驱动的微信聊天情感与人格分析工具"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/tswawa/WechatVibe"
githubStars: 129
githubOwner: "tswawa"
githubRepo: "WechatVibe"
category: "data-analysis"
tags: ["wechat-analysis", "emotion-recognition", "personality-insights", "local-llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "WechatVibe 能帮你分析微信聊天中的情绪变化、交流意图和对方性格，甚至推测好感度和 MBTI。适合想深入了解聊天对象、回顾关系动态的普通用户，无需技术背景即可上手。"
vibeCodingPrompt: "1. 从 GitHub 克隆项目：git clone https://github.com/tswawa/WechatVibe
2. 安装 Python 依赖：pip install -r requirements.txt
3. 下载本地 Laya ONNX 模型（或准备兼容 API 的密钥）
4. 运行主程序：python main.py，按提示登录微信
5. 在界面中选择聊天，开启「意图识别」和「情绪感知」
6. 进入「人物画像」查看互动风格、好感度和 MBTI 推测
7. 如需 API 模式，在设置中填入 API 地址和密钥，切换分析引擎"
pitfallGuide: "确保微信已登录且版本兼容，否则无法读取本地数据库
本地模型需提前下载，路径配置错误会导致分析失败
API 模式需注意密钥安全和费用，避免泄露
分析结果仅供参考，不要用于骚扰或侵犯他人隐私
首次分析大量消息可能耗时较长，建议分批处理"
targetAudience: ["独立开发者", "产品经理", "AI 研究者", "内容创作者"]
useCases: ["回顾与恋人或朋友的聊天记录，了解情绪变化和好感度趋势", "分析群聊氛围和成员互动风格，辅助社群运营", "研究聊天数据中的情感和人格特征，用于学术或产品设计", "个人使用，探索日常交流中的意图和情绪模式"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。微信聊天分析工具，支持本地 Laya 与 API 模型，提供意图识别、情绪感知、人物画像、群聊画像、好感度分析和 MBTI 聊天推测。

> GitHub: [tswawa/WechatVibe](https://github.com/tswawa/WechatVibe) | ⭐ 129 | Python

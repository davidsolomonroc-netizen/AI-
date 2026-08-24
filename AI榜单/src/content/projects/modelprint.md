---
title: "模型指纹识别器"
description: "探测API背后真实模型身份"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/unclecode/modelprint"
githubStars: 79
githubOwner: "unclecode"
githubRepo: "modelprint"
category: "dev-tools"
tags: ["fingerprinting", "llm", "openrouter", "ai-tools"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个工具能帮你识别API背后真正运行的模型，防止供应商偷换模型。适合需要透明和可控AI服务的开发者、企业团队，以及关注AI安全的研究者。无需安装，浏览器直接使用，保护API密钥安全。"
vibeCodingPrompt: "1. 打开 https://unclecode.github.io/modelprint/ 页面。
2. 在输入框中粘贴你要测试的OpenAI兼容API端点（如OpenRouter、DeepSeek等）。
3. 填写API密钥（可选，但建议使用）。
4. 点击运行，页面会执行9个基础设施探针，并显示与已知模型的指纹对比。
5. 查看结果，重点关注tokenizer匹配度（如4/4表示完全匹配）。
6. 如有需要，可参考README中的探针列表，了解每个探针的意义。"
pitfallGuide: "1. 浏览器直接调用可能触发CORS限制，部分API可能无法测试。\n2. API密钥仅在浏览器本地使用，但建议使用低权限测试密钥。\n3. 探针结果受网络延迟和API版本影响，建议多次测试取平均。\n4. 模型可能动态更新，指纹库需要社区持续维护。\n5. 结果仅提供概率性匹配，非绝对证据。"
targetAudience: ["AI研究者", "技术负责人", "开发者", "企业团队"]
useCases: ["验证API提供商是否悄悄更换模型", "对比不同供应商的模型性能", "识别OpenRouter上的神秘模型身份"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Who is really behind that API? Fingerprint any OpenAI-compatible endpoint in the browser: 9 infrastructure probes, side-by-side comparison, community-extensible.

> GitHub: [unclecode/modelprint](https://github.com/unclecode/modelprint) | ⭐ 79 | JavaScript

---
title: "DSH 破甲闪插件"
description: "轻量级 LLM 破甲插件，省 token 且零补丁"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/jadezane6634-ops/dsh-purge-flash"
githubStars: 99
githubOwner: "jadezane6634-ops"
githubRepo: "dsh-purge-flash"
category: "dev-tools"
tags: ["jailbreak", "prompt-engineering", "token-efficiency", "deepseek"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个面向 DeepSeek 等大模型的插件，通过精简的提示词工程和请求体整形，降低模型拒答率并节省每轮对话的 token 消耗。适合需要高频调用 LLM、对上下文窗口敏感，或希望绕过内容限制的开发者与研究者使用。"
vibeCodingPrompt: "1. 克隆仓库并运行 npm install；2. 阅读 README 了解 DSH 事件面和插件注册方式；3. 在 DSH 配置中启用该插件，设置 DSH_HOME 环境变量并创建 prompt-inject.md 写入你的操作稿；4. 运行 npm test 验证 188 项测试通过；5. 启动你的 DSH 会话，观察 token 消耗和拒答率变化；6. 根据输出形态调整分级 prefill 模板和拒答阶梯策略。"
pitfallGuide: "需要先安装 DSH 宿主环境，非独立应用
操作稿注入是强度主来源，务必配置 prompt-inject.md
从 dsh-purge 迁移时旧会话可能消失，需运行修复命令
请求体整形依赖 provider 别名代理，需确认适配器兼容
破甲行为可能违反模型服务条款，注意合规风险"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["高频 LLM 对话场景节省 token", "红队测试与安全研究", "需要绕过模型拒答的内容生成", "上下文窗口敏感的长对话应用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。DSH 破甲插件：token 级重试环 + 十片按需叶子（含邻近交付）+ 分级 prefill + 拒答阶梯 L0–L3 + finish_reason 四路分流 + 请求体级整形。零宿主补丁，188 项测试 / 56 条探针。

> GitHub: [jadezane6634-ops/dsh-purge-flash](https://github.com/jadezane6634-ops/dsh-purge-flash) | ⭐ 99 | JavaScript

---
title: "OC Ferry 摆渡桥"
description: "把 OpenCode 免费模型接入 WorkBuddy 的托盘转发工具"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/HRuiCcc/RuiC-oc-ferry"
githubStars: 72
githubOwner: "HRuiCcc"
githubRepo: "RuiC-oc-ferry"
category: "workflow-automation"
tags: ["opencode", "openai-compatible", "electron", "free-models"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OC Ferry 解决的是「免费大模型额度无法直接给工具类应用使用」的问题：它在本地隔离运行 OpenCode，按价格筛出真正免费的模型，自动测试它们能否支持工具调用，然后把可用的写进 WorkBuddy 配置并开一个本机转发口。适合想零成本给 WorkBuddy 挂上免费模型、又不想折腾 API Key 的个人用户和小团队。"
vibeCodingPrompt: "我想用 OC Ferry 给 WorkBuddy 接上免费模型。请按以下步骤帮我操作：1) 先确认我本机已装 Node.js >=22，并从 GitHub 克隆 HRuiCcc/RuiC-oc-ferry 仓库；2) 阅读 README 的「工作流程」和安装说明，识别出启动托盘应用的命令（通常是 npm install 后 npm start 或直接下载 release 安装包）；3) 启动后引导我在控制面板点击「检测」，观察并发检测进度，区分「可用·支持工具」和「可用·仅对话」两档状态；4) 选中通过工具协议检测的模型，点击「一键导入」写入 WorkBuddy 的 models.json；5) 确认本机转发口 127.0.0.1:41980 已启动，并在 WorkBuddy 里发起一次简单对话验证链路；6) 如果检测失败，帮我查看行内详情里的失败原因（超时/限流/无权限），并按提示等待自动重试或只重测单个模型。"
pitfallGuide: "Node 版本必须 >=22，低版本会导致隔离运行时启动失败
免费模型池随时上下线，检测通过不代表长期可用，建议保留缓存并定期重测
「仅对话」模型不能产生工具调用，导入 WorkBuddy 后工具类功能会失效，需按需选择
转发口只监听 127.0.0.1，不要改成 0.0.0.0，否则会把免费额度暴露到局域网
首次检测会并发跑多个模型，可能触发限流，失败后等 10 分钟再试更稳"
targetAudience: ["独立开发者", "创业者", "技术负责人"]
useCases: ["给 WorkBuddy 零成本接入免费大模型", "本地快速验证哪些免费模型支持工具调用", "为团队搭建不依赖 API Key 的模型转发层", "在 macOS/Windows 上做托盘式模型管理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。把 OpenCode 的免费模型摆渡给 WorkBuddy —— 隔离运行时、并发检测、判定缓存、一键导入、本机 OpenAI 兼容转发口

> GitHub: [HRuiCcc/RuiC-oc-ferry](https://github.com/HRuiCcc/RuiC-oc-ferry) | ⭐ 72 | JavaScript

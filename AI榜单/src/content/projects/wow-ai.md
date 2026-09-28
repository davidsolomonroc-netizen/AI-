---
title: "WoW AI 游戏内编程助手"
description: "在魔兽世界里直接对话本地编程智能体"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/chelinho139/wow-ai"
githubStars: 112
githubOwner: "chelinho139"
githubRepo: "wow-ai"
category: "workflow-automation"
tags: ["wow-addon", "claude-code", "in-game-agent", "local-bridge"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这款插件让你在玩魔兽世界时不用切出游戏，就能把任务发给本地的 Claude Code 或 Codex 等编程智能体，等结果出来后游戏里会收到提醒。适合既爱打游戏又是程序员的玩家，边刷副本边等代码跑完。"
vibeCodingPrompt: "1. 克隆仓库 git clone https://github.com/chelinho139/wow-ai，阅读 README 的安装章节。2. 确认本地已安装 Claude Code 或 Codex 等 CLI 智能体，并记录其可执行路径。3. 按照 README 启动 companion bridge（通常是 Node.js 脚本），配置好智能体类型和允许访问的文件夹。4. 将 addon 文件夹复制到 World of Warcraft 的 Interface/AddOns 目录。5. 进入游戏后输入 /wow-ai 打开聊天窗口，新建一个 chat，选择智能体并发一条测试消息如 '列出当前目录文件'。6. 验证游戏内能否收到回复，再尝试 shift-click 物品或使用 /wow-ai map ore 查看地图标注功能。"
pitfallGuide: "需要本地已安装并配置好 Claude Code / Codex 等 CLI 工具，否则 bridge 无法工作。
游戏必须使用支持 addon 的客户端版本（Forever），普通正式服可能不兼容。
Linux 下游戏跑在 Wine 里时，bridge 的文件路径和权限要单独配置。
Beta 客户端可能清空插件数据，注意用自带的恢复功能备份聊天和地图图层。
智能体执行命令需要授权，遇到 allowlist 外操作要在游戏里点 Allow & retry。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["边打副本边让 Claude Code 跑代码任务，完成后游戏内收到通知", "在游戏里快速生成宏命令并一键放到动作栏", "让智能体根据角色等级、天赋和任务日志给出游戏内建议", "在世界地图上标注采集路线和任务点，配合导航箭头使用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Addon to use AI (Claude, Codex, Grok, Antigravity and Hermes) inside World of Warcraft  (WoW)

> GitHub: [chelinho139/wow-ai](https://github.com/chelinho139/wow-ai) | ⭐ 112 | JavaScript

---
title: "Godcoder：本地优先AI编程助手"
description: "开源桌面AI代理，代码不出本机"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/eli-labz/Godcoder"
githubStars: 246
githubOwner: "eli-labz"
githubRepo: "Godcoder"
category: "agent-framework"
tags: ["coding-agent", "local-first", "rust", "tauri"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Godcoder是一款本地优先的开源AI编程代理，代码始终留在你的机器上，不经过第三方服务器。它适合注重数据隐私的开发者，可以自动构建和优化自身的代理工具，甚至通过GUI自动化执行人类操作任务。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/eli-labz/Godcoder.git\n2. 安装依赖：确保Rust和Tauri环境已安装\n3. 配置LLM密钥：在设置中输入你的OpenAI或Anthropic API密钥\n4. 启动应用：使用`cargo tauri dev`运行开发模式\n5. 选择模式：Harness模式让AI自动构建工具链，CoWork模式用于桌面自动化\n6. 开始编码：在应用内打开项目文件夹，用自然语言描述任务"
pitfallGuide: "1. 需要Rust和Tauri开发环境，非技术用户安装可能耗时超过10分钟\n2. 自带LLM密钥，需自行支付API费用，无免费额度\n3. 自动化功能（CoWork模式）可能受操作系统权限限制\n4. 当前为早期版本，文档和社区支持有限\n5. 本地优先意味着无云同步，多设备使用需手动管理"
targetAudience: ["独立开发者", "AI研究者", "技术负责人"]
useCases: ["本地代码生成与重构", "自动化GUI操作任务", "构建自定义AI工具链", "隐私敏感场景的编程辅助"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A local-first, open-source coding agent for your desktop. Bring your own LLM key; your code stays on your machine and only ever leaves to the model provider. The AI Agent builds its own Harnes.

> GitHub: [eli-labz/Godcoder](https://github.com/eli-labz/Godcoder) | ⭐ 246 | Rust

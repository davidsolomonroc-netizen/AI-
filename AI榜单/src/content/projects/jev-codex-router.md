---
title: "Jev Codex 智能路由"
description: "按轮次动态选择模型与推理深度的 Codex 路由器"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/0xNatoshi/jev-codex-router"
githubStars: 113
githubOwner: "0xNatoshi"
githubRepo: "jev-codex-router"
category: "dev-tools"
tags: ["model-routing", "codex", "llm", "cost-optimization"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "它能在每次调用 AI 模型时自动挑选最合适的模型和思考深度，避免用最强模型处理简单问题，从而节省约六成配额。适合重度使用 Codex 的开发者、小团队和想控制 AI 成本的创业者。"
vibeCodingPrompt: "1. 先确认本地已安装并运行 Codex Router（监听 4202 端口）。2. 克隆本项目：git clone https://github.com/0xNatoshi/jev-codex-router，进入目录。3. 安装 Python 依赖（如 pip install -r requirements.txt 或查看 AGENTS.md 说明）。4. 启动 jev_server.py，确保它监听 127.0.0.1:4319。5. 按照 README 的说明，在 Codex Router 的配置里添加 generic provider 和 curated model，把 'jev/auto' 指向 LiteLLM 转发到本地 Jev 服务。6. 重启 Codex Router，然后在 Codex 中把模型切换为 'jev/auto'。7. 发起一次对话，观察日志确认 Jev 已根据任务难度选择不同模型和推理深度。8. 如需临时关闭，创建哨兵文件即可让路由回退到默认策略。"
pitfallGuide: "依赖本地已运行的 Codex Router，未安装则无法工作\n需要配置 LiteLLM 和 API forwarder，步骤略多，建议按 AGENTS.md 逐步操作\n项目处于早期，文档和兼容性可能变化，注意查看 BACKTEST.md 了解策略限制\n节省配额的数据来自历史模拟，并非实测当前策略，效果可能因使用模式而异\n遇到 Jev 服务错误时会自动回退，但可能影响路由效果，建议监控日志"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI 研究者"]
useCases: ["在 Codex 中自动为简单任务选择轻量模型，为复杂任务选择强模型，节省配额", "多模型混合使用场景下统一路由，避免手动切换", "团队内部共享 Codex 配额时，通过智能路由降低整体消耗", "研究模型路由策略对成本与效果的影响"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> GitHub: [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | ⭐ 113 | Python

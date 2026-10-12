---
title: "Asamana 涌现叙事引擎"
description: "给主题即自动生成AI角色与故事的引擎"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/dreamscroll-lab/asamana"
githubStars: 65
githubOwner: "dreamscroll-lab"
githubRepo: "asamana"
category: "agent-framework"
tags: ["multi-agent", "emergent-narrative", "generative-agents", "simulation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Asamana 是一个让 AI 角色自主生活的叙事引擎：你只需给一个主题，它就会生成一个共享世界和一群性格各异的 AI 角色，故事从他们的互动中自然浮现，无需剧本。适合内容创作者、游戏设计者和想探索 AI 叙事可能性的团队，用来快速生成互动故事、角色模拟或剧情灵感。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/dreamscroll-lab/asamana && cd asamana。2. 阅读 README 和 docs，了解配置格式（主题、角色数量、LLM 设置）。3. 安装依赖：pip install -r requirements.txt（或使用 uv/poetry，以仓库说明为准）。4. 设置 LLM API 密钥（如 OpenAI 或兼容接口），在配置文件中填入。5. 运行示例脚本或 CLI 命令启动模拟，观察角色自主对话和事件发展。6. 修改主题配置，生成你自己的故事世界，并导出叙事日志。7. 可选：将引擎封装为 FastAPI 服务，供前端调用，实现交互式叙事应用。"
pitfallGuide: "项目处于早期开发，API 和配置格式可能随时变化，不建议用于生产环境
提示词和生成的叙事目前仅支持中文，英文用户需自行调整
依赖 LLM API，运行成本随角色数量和模拟轮次增加，需控制预算
需要 Python 环境配置经验，非技术用户可能需协助
保存格式可能不兼容旧版本，升级前备份存档"
targetAudience: ["独立开发者", "AI 研究者", "内容创作者", "产品经理"]
useCases: ["互动小说与游戏剧情自动生成", "AI 角色行为模拟与社交实验", "创意写作辅助与故事灵感激发", "多智能体协作研究平台"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Asamana is an AI-driven emergent narrative engine.  

> GitHub: [dreamscroll-lab/asamana](https://github.com/dreamscroll-lab/asamana) | ⭐ 65 | Python

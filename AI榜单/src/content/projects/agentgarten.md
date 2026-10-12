---
title: "AgentGarten 智能体演化世界"
description: "用代码构建可自我演化智能体的实时交互世界"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/MirroS-Lab/AgentGarten"
githubStars: 161
githubOwner: "MirroS-Lab"
githubRepo: "AgentGarten"
category: "agent-framework"
tags: ["self-evolving", "multimodal", "neural-renderer", "agent-training"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "AgentGarten 让 AI 智能体在仿真环境中反复练习并沉淀经验，像游戏引擎一样持续迭代升级。它适合 AI 研究团队和希望训练专属智能体的企业，用更低的成本获得更强的自主决策能力。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/MirroS-Lab/AgentGarten，进入目录后创建 Python 虚拟环境并安装依赖（pip install -r requirements.txt）。
2. 从 Hugging Face 下载神经渲染器权重：huggingface-cli download MirroS-Lab/AgentGarten-renderer --local-dir ./checkpoints。
3. 查看 README 中的 streaming inference 示例脚本，运行最小 demo 验证渲染器能根据深度图和法线图生成观测画面。
4. 编写一个自定义代码世界：定义状态变量和规则函数，导出深度图与表面法线，接入共享渲染器。
5. 启动智能体练习循环：让智能体在环境中交互，每轮结束后把经验蒸馏成 playbook 文件，供下一轮智能体继承。
6. 用可视化脚本对比不同轮次智能体的表现，迭代优化世界规则和 playbook 内容。"
pitfallGuide: "需要 GPU 和较大的显存才能跑神经渲染器，纯 CPU 环境基本不可用
代码世界与练习循环部分尚未完全开源，需关注仓库后续更新
Hugging Face 权重下载可能受网络限制，建议提前配置镜像
神经渲染质量依赖深度图和法线图的准确性，自定义世界需仔细调试
项目较新、社区小，遇到问题优先查阅论文和项目主页而非搜索"
targetAudience: ["AI 研究者", "技术负责人", "独立开发者", "企业团队"]
useCases: ["训练可自我演化的自主智能体", "构建高保真仿真训练环境", "多模态世界模型研究与实验", "游戏 NPC 或虚拟角色的智能升级"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AgentGarten: Code Worlds for Evolving Agents

> GitHub: [MirroS-Lab/AgentGarten](https://github.com/MirroS-Lab/AgentGarten) | ⭐ 161 | Python

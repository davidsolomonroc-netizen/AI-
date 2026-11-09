---
title: "Axion 1.0 智能体基座模型"
description: "用简单训练配方打造前沿智能体能力"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/bytedance/axion1_0"
githubStars: 63
githubOwner: "bytedance"
githubRepo: "axion1_0"
category: "agent-framework"
tags: ["agentic-ai", "llm", "reinforcement-learning", "open-source"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Axion 1.0 是一套开源智能体训练方案，通过两阶段微调加强化学习，让企业用高质量数据和简单流程训练出具备前沿能力的智能体模型。适合希望自建智能体能力、降低对闭源模型依赖的 AI 团队和技术负责人。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone https://github.com/bytedance/axion1_0 && cd axion1_0 && pip install -e .
2. 从 Hugging Face 下载 Axion-1.0-35B 模型和训练数据，放到本地 models/ 和 data/ 目录。
3. 查看 configs/ 下的训练配置，修改数据路径和输出目录。
4. 运行第一阶段 SFT：python train_sft.py --config configs/sft_stage1.yaml
5. 运行第二阶段 SFT：python train_sft.py --config configs/sft_stage2.yaml
6. 运行 RL 训练：python train_rl.py --config configs/rl.yaml
7. 使用推理脚本测试模型：python infer.py --model ./output/axion-1.0 --prompt \"你的任务\"
8. 基于示例代码封装一个简单的智能体 API 服务，集成到你的应用中。"
pitfallGuide: "需要多卡 GPU 环境，35B 模型对显存要求较高，建议至少 8 张 A100/H100\n训练数据需提前下载并预处理，注意检查数据格式与配置文件一致\nRL 训练可能不稳定，建议先小规模试跑并调整超参数\n仓库较新，文档和脚本可能不完整，遇到问题可参考 issue 或论文\n推理部署需额外配置量化或分布式方案以降低资源消耗"
targetAudience: ["AI 研究者", "技术负责人", "企业团队"]
useCases: ["企业自建智能体模型", "智能体能力研究与复现", "多智能体工作流开发", "定制化任务自动化"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Frontier-level agent capabilities with nothing more than high-quality data and a simple training recipe: 2 SFT + RL, no mid-training/DPO/OPD. Full recipe released.

> GitHub: [bytedance/axion1_0](https://github.com/bytedance/axion1_0) | ⭐ 63 | Python

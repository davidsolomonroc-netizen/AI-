---
title: "点反射：AI代理执行恢复控制器"
description: "为编码AI代理提供执行恢复控制的开源控制器"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/usedotai/dot-reflex"
githubStars: 80
githubOwner: "usedotai"
githubRepo: "dot-reflex"
category: "agent-framework"
tags: ["agent-supervision", "recovery-controller", "QLoRA", "Qwen3"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Dot Reflex 是一个执行恢复控制器，它监控 AI 代理的工作轨迹，并在代理出错时提供十种控制决策（如重试、回滚、切换模型等），从而提高 AI 代理的可靠性和自主性。适合需要构建稳定 AI 代理系统的开发团队，尤其是那些依赖编码或工具使用代理的企业。它不替代代理本身，而是作为监督层，与 GPT、Claude 等主流模型兼容。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：`git clone https://github.com/usedotai/dot-reflex && cd dot-reflex && pip install -r requirements.txt`。
2. 下载预训练权重：从 Hugging Face 下载 Dot-Reflex-14B 的 QLoRA 适配器，并放置在 `models/` 目录。
3. 编写一个简单的 Python 脚本，导入 `dot_reflex` 模块，将你的代理轨迹（JSON 格式）作为输入，调用 `controller.decide()` 方法获取控制决策。
4. 将控制器集成到你的代理循环中：在每次代理执行后，生成轨迹摘要并调用控制器，根据返回的决策（如 'retry_differently' 或 'rollback'）调整代理的下一步行动。
5. 运行示例脚本 `examples/integrate_with_agent.py` 查看完整流程。"
pitfallGuide: "1. 不要将合成基准的 100% 结果视为普适可靠性，实际生产环境需另行验证。
2. 控制器返回的是决策，不负责执行，你需要自己实现回滚、重试等动作。
3. 输入轨迹需要结构化 JSON，需确保你的代理框架能输出兼容格式。
4. 模型基于 Qwen3-14B，需要足够的 GPU 内存（约 16GB+）才能运行推理。
5. 目前是 QLoRA 适配器，不能独立运行，必须配合 Qwen3-14B-Base 基础模型。"
targetAudience: ["AI 研究者", "技术负责人", "独立开发者"]
useCases: ["为编码代理添加监督和控制层，减少错误", "在复杂工具使用场景中自动恢复代理执行", "作为研究实验，探索代理自我修正机制"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source agent execution-recovery controller for coding and tool-using AI agents.

> GitHub: [usedotai/dot-reflex](https://github.com/usedotai/dot-reflex) | ⭐ 80 | Python

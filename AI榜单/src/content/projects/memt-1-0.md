---
title: "MemT-1.0 记忆原生模型"
description: "让大模型拥有持久且动态演化的长期记忆能力"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/MemTensor/MemT-1.0"
githubStars: 406
githubOwner: "MemTensor"
githubRepo: "MemT-1.0"
category: "agent-framework"
tags: ["long-term-memory", "llm", "ai-agents", "long-context"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 4
commercialSummary: "MemT-1.0 让 AI 模型能够长期记住历史对话与经验，而不必每次重新读取超长上下文，从而在智能体编程、长期陪伴助手等场景中大幅降低存储与推理成本。适合需要构建长期记忆型 AI 应用的开发团队与 AI 研究者。"
vibeCodingPrompt: "1. 克隆仓库 git clone https://github.com/MemTensor/MemT-1.0 并安装依赖（参考 README 的安装章节，准备 Python 环境与 SGLang 推理后端）。\n2. 从 HuggingFace 的 MemTensor/memt-1 集合下载对应模型权重（如 Qwen 或 DeepSeek 基座版本），配置本地模型路径。\n3. 启动推理服务：使用 SGLang 加载 MemT 模型，开启 memory 相关参数，验证基础对话可用。\n4. 编写一个简单的 Python 脚本，调用推理接口进行多轮对话，观察模型在跨轮次中是否保留历史信息。\n5. 基于该接口搭建一个「长期记忆型编程助手」Demo：用户提出代码需求，模型记住之前的偏好与项目结构，输出代码建议。\n6. 加入持久化存储：将 memory state 定期保存到磁盘，重启服务后加载，验证记忆延续性。\n7. 用 Claude Code 生成测试用例，覆盖长上下文（如 128K）场景，对比启用/禁用记忆时的效果与存储占用。"
pitfallGuide: "需要一定的 GPU 资源与 Python 环境配置经验，非技术用户难以在 10 分钟内跑通\n模型权重较大，下载与加载耗时较长，建议提前准备高速网络与足够显存\n依赖 SGLang 推理框架，版本兼容性需按 README 要求严格匹配\n记忆状态持久化需自行实现存储与加载逻辑，官方未提供开箱即用的服务端方案\n长上下文评测需构造专门数据集，直接使用通用对话可能无法体现记忆优势"
targetAudience: ["AI 研究者", "独立开发者", "技术负责人", "企业团队"]
useCases: ["长期记忆型编程助手", "跨会话的个性化 AI 客服", "长文档/代码库的持续理解与问答", "智能体的经验积累与复用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Official repository for MemT-1.0

> GitHub: [MemTensor/MemT-1.0](https://github.com/MemTensor/MemT-1.0) | ⭐ 406 | Python

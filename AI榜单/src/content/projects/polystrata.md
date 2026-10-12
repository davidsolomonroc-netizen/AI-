---
title: "PolyStrata 本地大模型引擎"
description: "一键在个人电脑上运行大模型并提供本地 API"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/VecSzn/PolyStrata"
githubStars: 93
githubOwner: "VecSzn"
githubRepo: "PolyStrata"
category: "dev-tools"
tags: ["local-llm", "openai-api", "cuda", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "PolyStrata 让普通个人电脑也能跑起通常需要服务器级别才能运行的大模型，支持 Qwen、GLM、Gemma 等主流模型，并对外提供 OpenAI/Anthropic 兼容的本地接口。适合注重数据隐私、想低成本自建 AI 能力的个人开发者和中小团队，所有数据都留在本机不外传。"
vibeCodingPrompt: "1. 从 GitHub 克隆 PolyStrata 仓库，按 README 在 Windows 或 Linux 上完成一键安装，确认显卡驱动（NVIDIA/AMD，≥12GB 显存）就绪。
2. 启动 PolyStrata 服务，默认会在 localhost 暴露 OpenAI/Anthropic 兼容 API 端口，记录下端口号和模型名。
3. 在 Claude Code 或 Cursor 中，把 API base URL 指向 http://localhost:<端口>/v1，API Key 随便填，模型名用 PolyStrata 中已加载的模型（如 Qwen3.6-35B-A3B）。
4. 让 Claude Code 写一个小的 Python/Node 脚本，调用这个本地接口完成一次对话，验证连通性。
5. 在此基础上扩展一个实际应用，比如本地文档问答：读取本地 PDF 切分后调用本地模型做摘要与检索问答，全程不联网。
6. 若需图片输入，切换到支持视觉的 Qwen3.8-Flash-Next 模型，在请求中按 OpenAI 多模态格式传入图片。"
pitfallGuide: "显存不足会直接失败或降速，务必确认显卡显存 ≥12GB，低于此建议改用更小的量化模型。
首次加载模型需要下载 GGUF 权重，体积大、耗时长，请预留足够磁盘空间和稳定网络。
AMD 显卡与 CUDA 生态兼容性不如 NVIDIA，遇到编译或算子报错优先查官方 issue。
本地 API 默认无鉴权，不要暴露到公网，仅监听 127.0.0.1。
不同模型量化等级（IQ3_S、Q3_K_M 等）会影响质量与速度，需按硬件实测取舍。"
targetAudience: ["独立开发者", "创业者", "AI 研究者", "技术负责人"]
useCases: ["本地隐私敏感的文档问答与摘要", "为 Claude Code/Cursor 提供免费本地模型后端", "无网络环境下的代码辅助与生成", "多模态图片理解与描述的原型验证"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Run large AI models on your own PC: Qwen3.8-Flash-Next, GLM 5.3 Flash, Qwen3.6, Ornith 1.5 and Gemma 4. One-click install for Windows and Linux, OpenAI/Anthropic API on localhost, image input. Built on Strata.

> GitHub: [VecSzn/PolyStrata](https://github.com/VecSzn/PolyStrata) | ⭐ 93 | C++

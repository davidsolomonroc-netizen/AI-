---
title: "Tessera: 从零构建的LLM蒸馏与推理引擎"
description: "自研LLM蒸馏与高效推理全栈"
publishDate: 2026-06-08
featured: false
githubUrl: "https://github.com/zengxiao-he/tessera"
githubStars: 63
githubOwner: "zengxiao-he"
githubRepo: "tessera"
category: "other"
tags: ["LLM", "distillation", "inference", "CUDA"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Tessera 提供了一个从零开始构建的LLM蒸馏与推理全栈方案，适合希望深入理解LLM训练、压缩和部署流程的AI研究者与工程师。它集成了自定义CUDA/Triton内核、FSDP分布式训练、分页KV缓存连续批处理、投机解码、Rust网关等工业级组件，但当前主要面向实验与学习，直接用于生产尚需更多打磨。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖（参考README）。\n2. 使用默认配置运行蒸馏流程：python -m tessera.distill --teacher tessera/configs/teacher_40M.yaml --student tessera/configs/student_6M.yaml。\n3. 启动推理引擎：python -m tessera.serve --model checkpoints/student_final.pt。\n4. 用Rust网关接收HTTP请求：cd gateway && cargo run -- --model-path ../checkpoints/student_final.pt。\n5. 发送测试请求：curl -X POST http://localhost:8080/generate -d '{\"prompt\":\"Hello, world!\",\"max_tokens\":50}'。"
pitfallGuide: "1. 当前仅支持NVIDIA GPU运行自定义CUDA/Triton内核，其他设备自动回退到PyTorch参考实现，性能会大幅下降。\n2. 蒸馏配置（教师/学生模型大小、损失权重等）需要根据硬件资源调整，默认配置在显存不足时可能OOM。\n3. Rust网关依赖PyO3，编译环境需要匹配Python版本和Rust工具链，初次构建可能遇到链接错误。\n4. 分页KV缓存和投机解码功能尚在实验阶段，生产使用前需充分测试。\n5. 项目文档以英文为主，部分内部接口缺乏详细注释，二次开发需要阅读源码。"
targetAudience: ["AI研究者", "技术负责人", "独立开发者"]
useCases: ["LLM蒸馏教学与实验", "自定义小模型推理服务搭建", "CUDA/Triton内核开发学习", "分布式训练与推理全栈原型验证"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。From teacher to tiles — a from-scratch LLM distillation & serving engine: custom Triton/CUDA kernels, FSDP distillation, paged-KV continuous batching, speculative decoding, a Rust gateway, a JAX oracle, and interpretability tooling.

> GitHub: [zengxiao-he/tessera](https://github.com/zengxiao-he/tessera) | ⭐ 63 | Python

---
title: "苹果 Core AI 模型库与知识库"
description: "为 Apple 设备优化的开源 LLM 模型集合"
publishDate: 2026-06-15
featured: false
githubUrl: "https://github.com/john-rocky/coreai-model-zoo"
githubStars: 133
githubOwner: "john-rocky"
githubRepo: "coreai-model-zoo"
category: "other"
tags: ["CoreAI", "iOS", "macOS", "LLM"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目为 Apple 设备（iPhone、Mac）提供了可直接运行的先进大语言模型（如 Qwen、Gemma）及其转换工具链。适合需要本地运行 AI 模型的 iOS/macOS 应用开发者，无需依赖云端即可实现智能功能，保护用户隐私并降低延迟。"
vibeCodingPrompt: "1. 克隆项目仓库到本地。\n2. 阅读 README 了解支持的模型列表和下载链接。\n3. 从 Hugging Face 下载所需的 .aimodel 文件。\n4. 使用 Swift 项目中的 Core AI 框架加载模型。\n5. 编写一个简单的聊天界面，调用模型进行推理。\n6. 测试在 iPhone 或 Mac 上的运行效果，调整参数优化性能。"
pitfallGuide: "1. 部分大模型（如 35B、31B）仅支持 Mac，无法在 iPhone 上运行。\n2. 下载的模型文件较大，请确保有足够存储空间。\n3. 首次运行可能需要较长时间加载模型，建议在后台线程执行。\n4. 不同模型需要不同的转换代码，务必参考项目中的转换指南。\n5. 自定义 Metal 内核可能在某些旧设备上不兼容，请检查设备型号。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "企业团队"]
useCases: ["在 iOS 应用中集成本地智能助手", "为 macOS 开发离线文本生成工具", "研究 Apple 芯片上的模型优化技术", "构建隐私敏感型 AI 应用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Community model zoo + knowledge base for Apple Core AI (iOS/macOS 27): Qwen3.5 & Gemma 4 converted end-to-end, verified on-device (iPhone 17 Pro GPU/ANE), conversion gotchas, custom Metal kernels, Swift runner

> GitHub: [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) | ⭐ 133 | Swift

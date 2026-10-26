---
title: "AbliteratedOutTheBox"
description: "推理时解除模型拒绝行为的 llama.cpp 分支"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/heterodoxin/AbliteratedOutTheBox"
githubStars: 135
githubOwner: "heterodoxin"
githubRepo: "AbliteratedOutTheBox"
category: "dev-tools"
tags: ["llama.cpp", "abliteration", "inference", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个让本地大模型在推理时绕过安全拒绝、直接回答敏感问题的工具，无需重新训练或修改模型文件。适合需要测试模型边界、进行安全研究或构建不受限对话系统的开发者和研究者使用。"
vibeCodingPrompt: "请按照以下步骤用 AbliteratedOutTheBox 搭建一个本地无限制问答应用：1. 克隆仓库并进入目录；2. 运行 cmake -S . -B build -DCMAKE_BUILD_TYPE=Release 和 cmake --build build --target llama-abliterate -j 编译；3. 用 python3 convert_hf_to_gguf.py 将你的 HuggingFace 模型转换为 GGUF 格式；4. 运行 ./build/bin/llama-abliterate -m 模型.gguf -ngl 99 -n 256 -p \"你的问题\" 测试；5. 编写一个简单的 Python 脚本，通过 subprocess 调用 llama-abliterate 并传入用户输入，实现交互式问答；6. 调整 --ff-threshold、--edit-strength 参数观察效果。"
pitfallGuide: "需要自行编译 C++ 项目，对非技术用户有一定门槛
模型转换需要 Python 环境及 torch、transformers、gguf 依赖
解除拒绝行为可能涉及伦理和法律风险，请确保合规使用
不同模型架构效果可能不同，需测试调整阈值参数
仅支持 GGUF 格式模型，需先转换"
targetAudience: ["AI 研究者", "独立开发者", "技术负责人"]
useCases: ["安全研究与红队测试", "构建不受限的本地对话助手", "模型行为分析与调试", "隐私敏感场景下的本地推理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。llama.cpp fork that abliterates at inference

> GitHub: [heterodoxin/AbliteratedOutTheBox](https://github.com/heterodoxin/AbliteratedOutTheBox) | ⭐ 135 | C++

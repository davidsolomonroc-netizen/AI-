---
title: "夜跑：裸机直启大语言模型"
description: "无操作系统，从USB直接启动运行LLM"
publishDate: 2026-08-03
featured: false
githubUrl: "https://github.com/hardrave/NIGHTRUN"
githubStars: 120
githubOwner: "hardrave"
githubRepo: "NIGHTRUN"
category: "other"
tags: ["llm", "rust", "uefi", "bare-metal"]
editorialScore: 4
deploymentRating: 2
vibeCodingRating: 3
commercialSummary: "NIGHTRUN 是一个极简的本地大语言模型运行时，它绕过操作系统，直接从 UEFI 启动进入聊天界面。适合需要极致隐私、专用硬件或对底层技术感兴趣的开发者，用于构建离线、安全的 AI 对话设备或研究项目。"
vibeCodingPrompt: "1. 克隆仓库并阅读 README，理解其架构和启动流程。\n2. 检查 install.sh 脚本，确保理解其操作。\n3. 在安全环境（如虚拟机）中运行安装脚本，选择目标平台和模型。\n4. 使用 QEMU 或实际硬件测试启动，观察日志输出。\n5. 若需自定义模型或提示词，修改 Rust 源码中的相关配置并重新编译。"
pitfallGuide: "安装脚本会格式化U盘或SD卡，务必确认设备名无误。\n项目处于早期阶段，可能缺少某些模型支持或存在稳定性问题。\n需要 Rust 编译环境和 UEFI 启动知识才能定制。\n在真实硬件上测试前，建议先在 QEMU 中验证镜像。\n模型文件较大（1-2GB），需确保存储介质容量足够。"
targetAudience: ["AI研究者", "技术负责人", "独立开发者"]
useCases: ["构建专用离线AI对话设备", "研究无操作系统环境下的AI推理", "教学演示UEFI启动与裸机编程", "探索极致隐私保护的本地AI方案"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Boot your PC straight into an LLM. Rust, UEFI-resident, no operating system underneath.

> GitHub: [hardrave/NIGHTRUN](https://github.com/hardrave/NIGHTRUN) | ⭐ 120 | Rust

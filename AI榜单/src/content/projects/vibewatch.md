---
title: "Vibe Watch 触觉秒表控制器"
description: "为AI辅助编程打造的腕上触觉控制设备"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/GOROman/vibewatch"
githubStars: 115
githubOwner: "GOROman"
githubRepo: "vibewatch"
category: "dev-tools"
tags: ["vibe-coding", "esp32-s3", "m5stack", "ble-hid"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Vibe Watch 是一款基于 M5Stack StopWatch 的可穿戴设备，将 AI 编程中的常见操作（如批准/拒绝、切换会话、语音输入）从桌面界面移到手腕上，让开发者无需切换窗口即可掌控多个 AI 代理会话。适合频繁使用 AI 结对编程的开发者、技术爱好者和希望优化人机交互效率的团队。"
vibeCodingPrompt: "1. 克隆项目仓库并安装 PlatformIO。\n2. 在 PlatformIO 中打开项目，选择 M5Stack StopWatch 开发板。\n3. 编译并烧录固件到设备。\n4. 连接设备到电脑（通过 BLE HID）。\n5. 在 Claude Code 中配置自定义快捷键，映射到设备的物理按键（如批准、拒绝、切换会话）。\n6. 测试按键触发对应操作，并根据需要调整按键映射。"
pitfallGuide: "需要 M5Stack StopWatch 硬件，非通用设备。\n固件编译需要 PlatformIO 环境，有一定配置门槛。\nBLE HID 连接可能在部分操作系统上不稳定，需调试。\n自定义按键映射需要修改源码，需了解 C++ 和 ESP32 开发。\n官方文档以英文为主，中文资源较少。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者"]
useCases: ["多 AI 代理会话的快速切换与控制", "在编码过程中无需键盘即可批准或拒绝 AI 操作", "通过语音输入快速向 AI 发送指令", "作为可穿戴设备展示 AI 交互创新"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A tactile M5Stack StopWatch controller for AI-assisted Vibe Coding

> GitHub: [GOROman/vibewatch](https://github.com/GOROman/vibewatch) | ⭐ 115 | C++

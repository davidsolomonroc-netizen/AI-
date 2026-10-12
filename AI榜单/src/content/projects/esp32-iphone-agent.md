---
title: "ESP32 iPhone 智能体"
description: "用7美元ESP32让AI操控真实iPhone"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/onehumanbeing/esp32-iphone-agent"
githubStars: 55
githubOwner: "onehumanbeing"
githubRepo: "esp32-iphone-agent"
category: "agent-framework"
tags: ["AI Agent", "iPhone Automation", "ESP32", "Computer Use"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目让 AI 模型通过一块廉价 ESP32 芯片和 AirPlay 投屏，直接操控真实 iPhone，无需苹果开发者账号、Xcode 或越狱。适合需要自动化测试 iOS 应用、做手机端 AI 代理或研究计算机使用能力的团队和个人。"
vibeCodingPrompt: "请基于 onehumanbeing/esp32-iphone-agent 项目搭建一个 iPhone 自动化代理。步骤：1) 克隆仓库并安装 Python 依赖；2) 将 ESP32-S3 开发板烧录固件并插入 iPhone USB 口，使其被识别为鼠标键盘；3) 配置 AirPlay 投屏，让代理能截取 iPhone 屏幕；4) 在配置文件中填入任意 OpenAI 兼容的视觉模型 API Key（如 GPT-4o 或本地模型）；5) 运行主程序，通过 Web UI 观察代理的实时屏幕、操作日志和计划；6) 用自然语言下达任务，例如“打开设置并连接 Wi-Fi”，代理会自动规划并执行点击、滑动、输入。"
pitfallGuide: "需要一块 ESP32-S3 开发板并正确烧录固件，普通 ESP32 可能不兼容 USB HID。\nAirPlay 投屏需要 iPhone 与电脑在同一局域网，且 iPhone 需信任该电脑。\n首次使用需在 iPhone 上开启“USB 配件”并信任电脑，否则 HID 无法工作。\n视觉模型需支持图像输入，纯文本模型无法理解屏幕内容。\n操作延迟受网络和模型响应速度影响，复杂任务可能较慢。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "创业者"]
useCases: ["iOS 应用自动化测试，无需 Xcode 和开发者账号", "构建手机端 AI 代理，让大模型直接操作真实 App", "研究计算机使用（Computer Use）在移动端的落地", "批量执行重复性 iPhone 操作，如数据录入、消息发送"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No developer account, no Xcode, no jailbreak.

> GitHub: [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) | ⭐ 55 | Python

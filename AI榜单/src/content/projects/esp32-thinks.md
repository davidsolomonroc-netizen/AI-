---
title: "ESP32 智能语音助手"
description: "可自由组合多模型的ESP32个人AI语音助手。"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/raullenchai/esp32-thinks"
githubStars: 223
githubOwner: "raullenchai"
githubRepo: "esp32-thinks"
category: "multimodal"
tags: ["ESP32", "voice-assistant", "OpenAI-compatible", "embedded"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个运行在ESP32硬件上的开源语音助手固件，用户可以用自己的OpenAI兼容模型（语音识别、聊天、语音合成可分别配置）打造不依赖单一厂商的智能音箱。适合硬件爱好者、独立开发者和小团队快速验证语音交互产品原型。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/raullenchai/esp32-thinks && cd esp32-thinks；2. 安装ESP-IDF v6.0.1（参考官方文档），并设置环境变量；3. 准备SenseCAP Watcher开发板，连接USB；4. 复制配置模板（如 sdkconfig.defaults 或 config.example），填入你的OpenAI兼容API密钥和端点（STT/chat/TTS可分别设置）；5. 运行构建命令：idf.py build；6. 烧录固件：idf.py -p /dev/ttyUSB0 flash monitor；7. 设备启动后说“Hi, ESP”或按旋钮测试语音交互；8. 根据日志调整模型参数，完成部署。"
pitfallGuide: "需要ESP-IDF v6.0.1环境，版本不匹配可能导致编译失败。\n仅支持SenseCAP Watcher开发板，其他ESP32-S3板需自行适配引脚。\nAPI端点需兼容OpenAI接口，且网络需能访问对应服务。\n首次烧录需安装USB驱动并确保串口权限。\n语音唤醒词和语言支持有限，中文/英文/韩文需确认模型能力。"
targetAudience: ["独立开发者", "硬件爱好者", "创业者", "技术负责人"]
useCases: ["个人智能音箱DIY", "语音交互产品原型验证", "多模型AI助手集成测试", "嵌入式AI教学演示"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A multi-model Muse: personal AI voice assistant on ESP32 - wake word or knob, any OpenAI-compatible brain (STT/chat/TTS mix-and-match), streaming replies, out of the box. Built on muse-gadget-sdk.

> GitHub: [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) | ⭐ 223 | Shell

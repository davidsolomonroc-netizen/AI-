---
title: "Jarvis 聊天悬浮窗助手"
description: "macOS 本地只读聊天意图与风险分析助手"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/jev-chat/jev-chat-jarvis-mac"
githubStars: 428
githubOwner: "jev-chat"
githubRepo: "jev-chat-jarvis-mac"
category: "workflow-automation"
tags: ["macos", "local-first", "privacy", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "在 macOS 上实时读取聊天窗口消息，用本地小模型判断对方意图和风险等级，并生成多风格回复候选，全程只读不上传数据。适合注重隐私的个人用户、销售客服和需要快速应对复杂沟通场景的人。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/jev-chat/jev-chat-jarvis-mac 并进入目录。\n2. 创建 Python 虚拟环境并安装依赖：python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt。\n3. 下载项目指定的小模型权重，放到 README 中说明的模型路径下。\n4. 在 macOS 系统设置中为终端或 Python 开启辅助功能权限。\n5. 运行启动脚本：python main.py，首次启动会自动弹出配置向导，按提示设置聊天应用和话术分组。\n6. 打开任意支持的聊天应用，发送一条测试消息，确认悬浮窗能识别消息并给出意图、风险和回复候选。\n7. 根据需要调整环境变量，如 JEV_BOXES=1 开启 YOLO 检测框，或修改 JEV_MESSAGE_REGION 手动校准消息区域。\n8. 若识别不准，使用菜单栏 J → 校准区域… 手动框选消息区和输入区，点击预览识别并确认启用。"
pitfallGuide: "需要 macOS 辅助功能权限，否则无法读取聊天窗口内容。\n首次使用必须手动校准消息区域，否则可能漏消息或读到联系人列表。\n本地模型需要一定显存和内存，M1 Pro 上推理约 1.5-2 秒，低配 Mac 可能更慢。\n仅支持 macOS，且部分聊天应用界面更新后可能需要重新校准。\n所有数据仅在本地处理，但请勿在公共电脑上保存敏感聊天记录。"
targetAudience: ["独立开发者", "产品经理", "内容创作者", "企业团队"]
useCases: ["实时判断客户消息意图和风险，辅助销售快速回复。\n在恋爱或社交聊天中获取多风格回复建议。\n客服人员快速识别用户情绪和风险等级。\n隐私敏感用户在不泄露聊天内容的前提下获得 AI 辅助。"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。聊天悬浮窗助手（macOS）：屏幕感知 + 本地小模型判断意图与风险，按话术生成回复候选。纯只读。

> GitHub: [jev-chat/jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac) | ⭐ 428 | Python

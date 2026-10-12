---
title: "Hermes 官方插件集"
description: "Nous Research 官方 Hermes Agent 插件合集，一行安装"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/NousResearch/hermes-official-plugins"
githubStars: 210
githubOwner: "NousResearch"
githubRepo: "hermes-official-plugins"
category: "agent-framework"
tags: ["agent-plugins", "hermes-agent", "home-assistant", "llm"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 5
commercialSummary: "这是 Nous Research 为自家 AI 智能体 Hermes Agent 提供的官方插件包，让智能体可以一键接入 Home Assistant 智能家居、Spotify 音乐、Claude 订阅等服务。适合已经使用 Hermes Agent 的个人用户或团队，快速扩展智能体的实际动手能力，无需自己从零开发集成。"
vibeCodingPrompt: "1. 先克隆仓库：git clone https://github.com/NousResearch/hermes-official-plugins && cd hermes-official-plugins。2. 阅读 README 和 docs 目录，确认 Hermes Agent 已安装（参考 github.com/NousResearch/hermes-agent）。3. 运行 pip install -e . 安装依赖，并执行 tests 目录下的测试确认环境正常。4. 在 Hermes Agent 配置文件中启用所需插件（如 Home Assistant 或 Spotify），按插件目录下的 config 示例填入 API Token。5. 通过 Hermes 插件目录命令（hermes plugin install <name>）安装单个插件，启动 Hermes Agent 后测试对话触发插件功能。6. 根据需求修改插件源码或新增自定义插件，遵循现有插件目录结构，最后运行 CI 测试脚本验证。"
pitfallGuide: "必须先安装并运行 Hermes Agent 本体，单独使用本仓库无意义
各插件需要独立的第三方 API Key（Spotify、Home Assistant 等），需提前申请
Python 版本和依赖版本可能较新，建议使用虚拟环境避免冲突
插件配置写在 Hermes Agent 侧，修改本仓库不会自动生效，需重新加载
部分插件依赖外部服务网络（如 Spotify），国内环境可能需要代理"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人", "创业者"]
useCases: ["让 Hermes 智能体语音控制 Home Assistant 智能家居设备", "通过 Hermes 智能体管理 Spotify 播放列表和音乐推荐", "为 Hermes Agent 开发第三方插件并发布到官方目录", "将 Claude 订阅能力集成进个人 AI 助理工作流"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。☤ The official plugins for Hermes Agent, built and maintained by Nous Research: Home Assistant, Spotify, Claude Subscription DirectSDK and more, one install away from the Hermes plugin catalog.

> GitHub: [NousResearch/hermes-official-plugins](https://github.com/NousResearch/hermes-official-plugins) | ⭐ 210 | Python

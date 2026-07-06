---
title: "Talos 工人"
description: "共享 GPU 赚取收益的 AI 推理客户端"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/jmerelnyc/Talos"
githubStars: 687
githubOwner: "jmerelnyc"
githubRepo: "Talos"
category: "other"
tags: ["GPU", "inference", "ollama", "distributed"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Talos 是一个去中心化 GPU 算力共享网络，允许用户将本地 GPU 接入网络，为开源模型推理任务提供算力并获取报酬。适合拥有闲置 NVIDIA GPU 的个人开发者或矿工，在后台运行即可自动赚取收入。"
vibeCodingPrompt: "使用 Talos 客户端将闲置 GPU 接入网络：
1. 确保已安装 Python 3.9+ 和 Ollama，并拉取一个模型（如 llama3.1:8b）
2. 在终端运行 `pip install -e .` 安装客户端
3. 登录 Talos 网页获得配对码，运行 `talos-worker pair --code TALOS-XXXX-XXXX`
4. 运行 `talos-worker run --allocation 0.5` 启动服务，打开 http://127.0.0.1:8674 监控状态
5. 在 Claude Code 中，你可以通过系统提示让 AI 自动执行上述步骤，并检查 Ollama 是否运行、GPU 是否可用。"
pitfallGuide: "1. 必须提前安装并运行 Ollama，且至少拉取一个模型
2. 配对码需从 Talos 网页生成，且有时效性
3. --allocation 参数控制并发/占空比，不是实际功率百分比
4. 默认连接的是 usetalos.xyz 服务器，需确保网络可访问 WebSocket
5. 仅 NVIDIA GPU 自动检测，CPU 也可运行但收益低"
targetAudience: ["独立开发者", "创业者", "技术负责人"]
useCases: ["闲置 GPU 变现", "参与去中心化 AI 计算网络", "后台运行赚取被动收入"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

> GitHub: [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | ⭐ 687 | Python

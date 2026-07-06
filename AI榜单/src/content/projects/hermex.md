---
title: "Hermex：iPhone 上的 Hermes 智能体控制台"
description: "用 iPhone 控制自托管 AI 智能体"
publishDate: 2026-07-06
featured: false
githubUrl: "https://github.com/uzairansaruzi/hermex"
githubStars: 627
githubOwner: "uzairansaruzi"
githubRepo: "hermex"
category: "agent-framework"
tags: ["hermes", "ios", "swiftui", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Hermex 让你用 iPhone 远程控制自托管的 Hermes AI 智能体，无需第三方中继，数据完全保留在你的服务器上。适合重视隐私、希望拥有完全控制权的个人开发者或小团队。"
vibeCodingPrompt: "请用 Hermex 项目搭建一个 iPhone 上使用的自托管 AI 助手：
1. 在服务器上部署 Hermes WebUI（参考 hermes-webui 项目文档）。
2. 确保服务器与 iPhone 在同一网络或可通过 VPN 访问。
3. 从 App Store 下载 Hermex 或在 Xcode 中构建项目。
4. 打开 Hermex，输入服务器地址和 API 密钥（如有）。
5. 开始通过 iPhone 向 Hermes 发送任务、查看会话记录和管理智能体技能。"
pitfallGuide: "1. 必须预先部署 hermes-webui 服务器，Hermex 本身不包含服务器功能。\n2. 服务器与 iPhone 网络连通性需自行保障，建议使用 Tailscale 等工具。\n3. 当前仅支持 iOS 18+，旧设备无法使用。\n4. 若服务器未配置 SSL，需在 iPhone 上允许 HTTP 连接（不安全）。\n5. 项目仍处于早期阶段，部分功能（如文件上传）可能不完善。"
targetAudience: ["独立开发者", "创业者", "AI 研究者", "技术负责人"]
useCases: ["在移动端管理自托管 AI 智能体", "远程调试和监控 AI 工作流", "安全地通过手机与私有 AI 对话", "作为个人知识库或任务管理的移动入口"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Native iPhone app for your Hermes agent

> GitHub: [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) | ⭐ 627 | Swift

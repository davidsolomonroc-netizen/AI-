---
title: "TokenBar：AI 额度一屏掌握"
description: "跨平台 AI 用量与额度监控工具"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/lwh0630/TokenBar"
githubStars: 60
githubOwner: "lwh0630"
githubRepo: "TokenBar"
category: "dev-tools"
tags: ["quota-monitor", "cross-platform", "flutter", "llm-usage"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "TokenBar 把 Codex、Claude、Cursor 等 50 个 AI 服务的剩余额度、余额和重置倒计时集中到一个跨平台桌面/手机应用里。适合同时订阅多个 AI 工具、需要随时掌握用量和成本的人，避免超额或断供。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/lwh0630/TokenBar 并进入目录。2. 安装 Flutter 3.47+ 及对应平台桌面支持（Windows/macOS/Linux）。3. 运行 flutter pub get 安装依赖。4. 用 flutter run -d <你的平台> 启动应用，桌面端会读取已登录 CLI 的凭证，移动端需粘贴 API key 或 cookie。5. 在设置中按需配置同步服务器（可选，仅接收用量快照）。6. 基于现有 provider 适配器结构，参考 lib/providers 新增一个自定义 AI 服务端点，实现 fetchQuota 方法并注册到 provider 列表。7. 运行 flutter test 和 CI 检查，最后用 flutter build 打包目标平台安装包。"
pitfallGuide: "桌面端凭证读取依赖官方 CLI 已登录，未登录会显示空数据；移动端需手动粘贴 API key/cookie，注意不要提交到版本库；同步服务器仅接收快照，不要自行扩展为上传凭证；Flutter 3.47 版本较新，旧环境需先升级 SDK；部分 provider 接口可能随官方变更失效，需关注 issue 和更新。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI 研究者"]
useCases: ["同时使用多个 AI 编程助手时统一查看剩余额度", "监控 API 余额和重置时间避免工作中断", "团队评估各 AI 服务用量成本", "桌面托盘常驻快速 glance 用量"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source, cross-platform AI quota monitor (Codex, Claude, Cursor and 47 more). Windows, macOS, Linux, Android and iOS. Built with Flutter.

> GitHub: [lwh0630/TokenBar](https://github.com/lwh0630/TokenBar) | ⭐ 60 | Dart

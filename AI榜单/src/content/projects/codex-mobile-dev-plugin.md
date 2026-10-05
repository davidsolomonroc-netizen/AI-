---
title: "Codex 移动开发插件"
description: "让 Codex 实时控制 iOS/Android 设备的开发插件"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/callstackincubator/codex-mobile-dev-plugin"
githubStars: 112
githubOwner: "callstackincubator"
githubRepo: "codex-mobile-dev-plugin"
category: "dev-tools"
tags: ["mobile-dev", "codex-plugin", "react-native", "agent"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这款插件把 iOS 模拟器、Android 模拟器和真机直接搬到 Codex 聊天窗口旁边，让 AI 能实时看屏幕、点按钮、读日志、查性能，帮助开发者更快定位移动端问题。适合用 React Native、Expo、SwiftUI 做 App 的独立开发者和移动端团队，尤其是已经在用 Codex 做 AI 辅助编程的人。"
vibeCodingPrompt: "1. 确认你已安装 Codex 桌面版并能访问 GitHub 私有仓库（需要 read 权限和 Git 认证）。
2. 在终端执行：codex plugin marketplace add https://github.com/callstackincubator/codex-mobile-dev-plugin.git --ref release/latest
3. 再执行：codex plugin add mobile-dev@mobile-dev
4. 关闭并重新打开一个新的 Codex 聊天窗口，插件会自动加载。
5. 启动你的移动项目：如果是 Expo/React Native，运行 npx expo start；如果是 SwiftUI，用 Xcode 打开模拟器。
6. 在 Codex 聊天里说：'帮我启动 iOS 模拟器并打开我的 App，然后截图当前界面。'
7. 用自然语言让 Codex 执行操作，例如：'点击登录按钮，读取 Metro 日志，把报错和堆栈发给我。'
8. 需要调试 UI 时，让 Codex 检查无障碍元素，或选中屏幕区域并留言说明问题。
9. 性能调优时，让 Codex 录制一段交互，查看 CPU/内存/FPS 图表，并对比两次运行结果。"
pitfallGuide: "仓库当前为私有，安装需要 GitHub 读权限和可用的 Git 认证，否则会拉取失败。
安装后必须新开聊天窗口，旧窗口不会加载插件。
插件依赖 Codex 桌面版，纯命令行环境无法使用设备控制功能。
部分设备控制能力（如输入文字、Display FPS）只在特定平台或真机支持，模拟器上可能受限。
更新插件要用 codex plugin marketplace upgrade mobile-dev，升级后同样需要新开聊天。"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["用 AI 实时调试 React Native/Expo 应用的 UI 和日志", "同时查看 iOS 和 Android 模拟器，对比两端表现", "让 Codex 自动录制交互并分析 CPU/内存/FPS 性能瓶颈", "在聊天中直接标注屏幕元素，让 AI 定位对应源码并修复"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A Codex plugin for a better mobile development experience for android and iOS

> GitHub: [callstackincubator/codex-mobile-dev-plugin](https://github.com/callstackincubator/codex-mobile-dev-plugin) | ⭐ 112 | C++

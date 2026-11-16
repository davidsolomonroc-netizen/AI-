---
title: "Gemini 配置检测器"
description: "检测能访问 Gemini 的代理配置"
publishDate: 2026-11-16
featured: false
githubUrl: "https://github.com/VisionWormStudio/Gemini-Config-Checker-"
githubStars: 473
githubOwner: "VisionWormStudio"
githubRepo: "Gemini-Config-Checker-"
category: "dev-tools"
tags: ["proxy", "gemini", "network", "cli"]
editorialScore: 3
deploymentRating: 3
vibeCodingRating: 3
commercialSummary: "帮助用户找出真正能访问 Google AI Studio 和 Gemini 的代理配置，避免反复试错。适合需要稳定访问 AI 服务的技术用户和网络管理员。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/VisionWormStudio/Gemini-Config-Checker-.git
2. 安装 Go 环境并构建：go build -o checker
3. 准备代理配置文件（链接或 base64）
4. 运行：./checker --configs your_configs.txt
5. 查看输出结果，筛选可用配置
6. 可选：集成到自己的监控脚本中定期检测"
pitfallGuide: "项目处于早期预发布阶段，仅在 Windows 上测试过，其他平台可能不稳定
需要自行准备代理配置，且部分功能依赖外部服务
反 DPI 功能可能受网络环境影响
免费配置列表可能失效，需定期更新
导出功能需检查格式兼容性"
targetAudience: ["独立开发者", "技术负责人"]
useCases: ["筛选可用的代理配置以访问 Gemini", "定期检测代理配置的有效性", "为团队提供稳定的 AI 服务访问方案"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Chain region scanner: find proxy configs that get you into Google AI Studio and Gemini (signed-in browser check, anti-DPI, Windows/macOS/Linux/Android) 

> GitHub: [VisionWormStudio/Gemini-Config-Checker-](https://github.com/VisionWormStudio/Gemini-Config-Checker-) | ⭐ 473 | Go

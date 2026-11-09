---
title: "Kota 用量面板"
description: "GNOME 顶栏实时显示 AI 服务用量与余额"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/ensignalp/kota"
githubStars: 67
githubOwner: "ensignalp"
githubRepo: "kota"
category: "dev-tools"
tags: ["GNOME", "AI用量监控", "Rust", "开发者工具"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Kota 把 Claude、Codex、Gemini、Copilot 等 AI 服务的用量额度直接放到 Linux 桌面顶栏，让你随时看到还剩多少额度、多久重置、会不会很快用完。适合每天同时用多个 AI 工具的开发者、独立开发者和技术团队，避免超额或突然断供。"
vibeCodingPrompt: "1. 在 Linux（GNOME 桌面）上克隆仓库：git clone https://github.com/ensignalp/kota。2. 按 README 安装依赖（Rust 工具链、GNOME Shell 扩展构建工具）。3. 运行构建与安装命令，把扩展加载到 GNOME Shell。4. 打开 Kota 设置，在“提供方”里添加 Claude/Codex（CLI 登录自动检测）或填入 API Key。5. 在“布局”里选择顶栏显示位置与格式。6. 用 Claude Code 写一个小脚本，定期读取 Kota 的本地日志或配置，生成团队每日 AI 用量报告，并接入内部通知。"
pitfallGuide: "需要 GNOME 桌面环境，非 GNOME 用户无法直接使用
部分提供方依赖 CLI 登录状态，需先安装并登录对应 CLI
API Key 保存在本地配置中，注意文件权限与共享机器安全
刷新频率过高可能触发服务方限流，建议按需调整
扩展升级后可能需要重启 GNOME Shell 才能生效"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["多 AI 工具额度集中监控", "团队 AI 成本与用量日报", "避免 API 余额耗尽导致工作中断", "个人开发者管理订阅与预算"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI kullanım limitleri GNOME üst panelinde — Claude, Codex, Gemini, Copilot, API bakiyeleri · AI usage limits in the GNOME top bar

> GitHub: [ensignalp/kota](https://github.com/ensignalp/kota) | ⭐ 67 | Rust

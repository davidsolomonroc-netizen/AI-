---
title: "Boo：终端会话复用器"
description: "基于Ghostty的GNU screen风格终端复用器"
publishDate: 2026-06-15
featured: false
githubUrl: "https://github.com/coder/boo"
githubStars: 563
githubOwner: "coder"
githubRepo: "boo"
category: "dev-tools"
tags: ["terminal", "multiplexer", "ghostty", "zig"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Boo是一个专为开发者设计的终端会话管理器，它允许你在断开连接后保留终端会话，并支持通过脚本或AI代理精确读取屏幕状态。适合需要远程工作、自动化终端操作或集成AI助手的团队和个人开发者。"
vibeCodingPrompt: "使用Boo项目搭建一个AI辅助的终端会话管理应用：
1. 首先通过一键安装脚本安装Boo：`curl -fsSL https://raw.githubusercontent.com/coder/boo/main/install.sh | sh`
2. 创建并启动一个新会话：`boo new mysession`
3. 在会话中运行你的命令，例如启动一个长时间运行的进程
4. 随时按Ctrl-A d分离会话，或使用`boo attach`重新连接
5. 利用自动化命令：`boo send mysession \"echo hello\"`发送命令，`boo peek mysession --json`获取屏幕状态，`boo wait mysession \"pattern\"`等待特定输出
6. 将以上命令集成到AI代理工作流中，让AI读取终端输出并做出响应"
pitfallGuide: "1. Boo需要libghostty支持，确保系统已安装相关依赖\n2. 目前仅支持Linux和macOS，Windows用户需使用WSL\n3. 自动化命令`peek`和`wait`依赖于终端状态解析，复杂ANSI序列可能解析不完整\n4. 多用户共享会话需要额外配置权限\n5. 首次使用建议先阅读README中的快速入门部分，理解Ctrl-A快捷键绑定"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI研究者"]
useCases: ["远程服务器会话管理，断开后自动保留状态", "CI/CD流水线中自动化终端交互与监控", "AI代理读取并响应终端输出，实现智能运维", "多终端会话集中管理，提升开发效率"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。A GNU screen style terminal multiplexer built on libghostty.

> GitHub: [coder/boo](https://github.com/coder/boo) | ⭐ 563 | Zig

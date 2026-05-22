---
title: "RMUX：通用终端复用器"
description: "用Rust重写tmux，支持AI代理集成"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/Helvesec/rmux"
githubStars: 624
githubOwner: "Helvesec"
githubRepo: "rmux"
category: "dev-tools"
tags: ["tmux", "terminal", "agent", "rust"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "RMUX是一个高性能的终端复用器，兼容tmux命令，但提供类型化SDK和持久化会话，适合需要远程管理、自动化脚本或与AI代理集成的开发者。它解决了tmux在可编程性和现代工具链集成上的不足。"
vibeCodingPrompt: "使用Claude Code通过RMUX SDK创建一个Python脚本：
1. 创建新会话：rmux new-session -s myapp -d
2. 在会话中运行命令：rmux send-keys -t myapp 'python my_script.py' Enter
3. 等待输出并捕获结果：使用rmux capture-pane -t myapp
4. 若需分窗格：rmux split-window -h -t myapp
5. 最后关闭会话：rmux kill-session -t myapp"
pitfallGuide: "1. 目前为v0.2.0预览版，可能有bug，建议先在非生产环境测试。\n2. 虽然兼容tmux命令，但并非100%功能一致，迁移时需验证关键命令。\n3. 依赖Rust环境，非技术用户安装可能需额外步骤。\n4. SDK目前只提供Rust绑定，其他语言需自行封装。\n5. Windows下PowerShell支持可能不如Linux/macOS稳定。"
targetAudience: ["独立开发者", "技术负责人"]
useCases: ["开发效率提升", "代码审查", "CI/CD 集成"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

> GitHub: [Helvesec/rmux](https://github.com/Helvesec/rmux) | ⭐ 624 | Rust

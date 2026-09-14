---
title: "9Router模型切换器"
description: "VSCode Copilot Chat 零重载动态切换 AI 模型"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/yudaprasetya007/routeVSCODE"
githubStars: 239
githubOwner: "yudaprasetya007"
githubRepo: "routeVSCODE"
category: "dev-tools"
tags: ["vscode-extension", "model-switcher", "local-proxy", "copilot"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "解决开发者频繁手动修改配置来切换 AI 模型的问题，通过本地代理和 VSCode 扩展实现一键切换。适合使用 GitHub Copilot Chat 并希望快速试用不同 AI 模型（如 GPT-4o、Claude 3.5、DeepSeek）的开发者。"
vibeCodingPrompt: "1. 在 VSCode 中安装 9Router Model Connector 扩展（从 VSIX 或市场）。
2. 安装并启动 9Router 本地代理服务（参考 9router npm 包文档）。
3. 在扩展设置中配置 9Router 的本地地址和端口。
4. 打开 Copilot Chat，点击状态栏的模型切换按钮，选择所需模型（如 Claude 3.5 Sonnet）。
5. 验证模型切换后无需重启 VSCode，即可在 Chat 中使用新模型进行对话。"
pitfallGuide: "确保 9Router 代理服务已正确安装并运行，否则扩展无法连接。
部分模型可能需要 API 密钥或额外配置，需在 9Router 中提前设置。
扩展版本需与 9Router 版本兼容，建议使用最新版。
若切换模型后无响应，检查 VSCode 输出面板中的代理日志。
企业网络可能限制本地代理端口，需调整防火墙规则。"
targetAudience: ["独立开发者", "技术负责人", "AI 研究者"]
useCases: ["快速对比不同 AI 模型在代码生成中的表现", "在 Copilot Chat 中无缝切换模型以利用各自优势", "为团队统一配置多模型访问入口", "本地开发时测试不同模型的响应质量"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。⚡ Zero-reload dynamic AI model switcher & local proxy for VSCode Copilot Chat via 9Router

> GitHub: [yudaprasetya007/routeVSCODE](https://github.com/yudaprasetya007/routeVSCODE) | ⭐ 239 | JavaScript

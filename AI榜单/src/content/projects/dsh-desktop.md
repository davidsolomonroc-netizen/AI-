---
title: "DSH 桌面版"
description: "把 DeepSeek Harness 打包成双击即用的独立窗口应用"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/LuxUmbra697/DSH-Desktop"
githubStars: 61
githubOwner: "LuxUmbra697"
githubRepo: "DSH-Desktop"
category: "dev-tools"
tags: ["deepseek", "desktop-app", "webview2", "agent"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 3
commercialSummary: "它把原本需要在终端敲命令、开浏览器才能用的 DeepSeek Harness 封装成一个 Windows 桌面窗口，双击就能用，还支持便携携带和插件改造。适合不熟悉命令行、但想用 AI 助手的普通用户和希望快速分发给客户的小团队。"
vibeCodingPrompt: "1. 从 GitHub Releases 下载 DSH-Desktop 的便携包并解压到任意目录。
2. 双击启动 exe，等待内置 Node 与 DSH 运行时自动启动，WebView2 窗口会加载 DSH 界面。
3. 在设置中配置 DeepSeek API Key，确认服务地址与工作区路径。
4. 打开插件列表，参考两个示例插件（启动器插件改窗口标题/品牌色，DSH 宿主插件通过 --patch 挂入插件树）编写自己的插件。
5. 用 Claude Code 或 Cursor 打开插件源码目录，让 AI 生成新的插件逻辑（例如自定义主题、快捷指令、注入脚本），保存后重启应用验证效果。
6. 若需精简体积，在运行环境管理里删除内置 Node（前提是系统 Node 版本满足要求），把 app 目录整体复制即可分发。"
pitfallGuide: "需要 Windows 10/11 且已安装 WebView2 运行时，否则窗口无法加载界面
删除内置 Node 前务必确认系统 Node 版本满足 DSH 要求，否则启动失败
便携包的 data 目录保存 DSH_HOME、工作区和窗口状态，迁移时不要遗漏
插件通过 --patch 挂入 DSH 插件树，修改后需重启服务才生效
首次启动会下载或初始化运行时，网络不通时可能卡在启动阶段"
targetAudience: ["独立开发者", "创业者", "产品经理", "内容创作者"]
useCases: ["非技术用户本地使用 DeepSeek AI 助手", "把 DSH 打包分发给客户或团队成员", "基于插件系统定制品牌化 AI 桌面工具", "在无终端环境的 Windows 机器上部署 AI Agent"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。把 DeepSeek Harness 装进一个独立窗口：双击即用、免终端、免浏览器，支持插件改造，载荷可裁到 210 MB（便携包 74.8 MB），内置运行环境探测与 DSH 就地更新。

> GitHub: [LuxUmbra697/DSH-Desktop](https://github.com/LuxUmbra697/DSH-Desktop) | ⭐ 61 | C#

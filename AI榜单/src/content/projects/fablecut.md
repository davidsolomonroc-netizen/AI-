---
title: "FableCut：AI驱动的浏览器视频编辑器"
description: "零依赖、JSON时间线的浏览器视频编辑器，AI可操控"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/ronak-create/FableCut"
githubStars: 379
githubOwner: "ronak-create"
githubRepo: "FableCut"
category: "agent-framework"
tags: ["video-editing", "ai-agent", "mcp", "zero-dependency"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "FableCut是一个完全在浏览器中运行的非线性视频编辑器，其时间线以JSON文档形式暴露，AI代理（如Claude Code）可通过MCP/REST接口直接编辑视频。适合需要快速迭代短视频、社交媒体内容或原型验证的内容创作者和开发者，无需安装复杂软件，只需一个node server.js即可启动。"
vibeCodingPrompt: "1. 克隆项目并运行node server.js启动服务。\n2. 打开浏览器访问http://localhost:3000，确认编辑器界面加载。\n3. 通过AI代理（如Claude Code）调用REST API（POST /api/project）更新project.json中的时间线数据。\n4. 示例：让AI生成一个包含3个视频片段、1个标题和1个过渡效果的JSON时间线，并发送到API。\n5. 观察浏览器界面实时热更新，验证时间线变化。\n6. 可进一步让AI根据用户指令（如“添加一个淡入效果”）自动修改JSON并推送。"
pitfallGuide: "1. 确保Node.js版本>=14，否则server.js可能无法运行。\n2. 视频文件需可跨域访问（如本地文件或CORS启用的URL），否则无法加载。\n3. JSON时间线格式需严格遵循项目文档中的schema，错误格式会导致编辑器崩溃。\n4. 实时热更新依赖Server-Sent Events，确保浏览器支持且无防火墙拦截。\n5. 对于大型视频文件，浏览器性能可能受限，建议使用短片段。"
targetAudience: ["内容创作者", "独立开发者", "AI研究者", "技术负责人"]
useCases: ["AI自动生成短视频广告或社交媒体内容", "快速原型验证视频编辑逻辑", "教育与培训中的交互式视频编辑演示", "与AI代理协作完成视频剪辑工作流"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Zero-dependency browser video editor that AI agents can drive — JSON timeline, MCP + REST, live-reloading UI

> GitHub: [ronak-create/FableCut](https://github.com/ronak-create/FableCut) | ⭐ 379 | JavaScript

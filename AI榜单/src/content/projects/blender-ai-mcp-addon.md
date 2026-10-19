---
title: "Blender AI 助手"
description: "在 Blender 中通过对话驱动 3D 场景构建与编辑的 MCP 集成工具。"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/LiCinCan/blender-ai-mcp-addon"
githubStars: 790
githubOwner: "LiCinCan"
githubRepo: "blender-ai-mcp-addon"
category: "workflow-automation"
tags: ["blender", "mcp", "ai-assistant", "3d"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目将 AI 对话与 Blender 3D 创作流程深度结合，让用户通过自然语言指令完成场景检查、建模、材质编辑等复杂操作。适合 3D 艺术家、技术美术和需要快速迭代创意的设计师，能显著减少重复性手动操作。"
vibeCodingPrompt: "1. 克隆项目仓库并安装依赖：git clone https://github.com/LiCinCan/blender-ai-mcp-addon.git && cd blender-ai-mcp-addon && pip install -r requirements.txt。
2. 在 Blender 4.2+ 中安装插件：将 addon 文件夹复制到 Blender 的 scripts/addons 目录，或在 Blender 偏好设置中安装 ZIP 包。
3. 配置 AI 模型连接：在插件设置中填入 OpenAI、Claude 或 Ollama 的 API 密钥/本地地址。
4. 启动 MCP 服务器：运行 python mcp_server.py 或通过插件内置启动按钮。
5. 打开 Blender 的 AI Studio 面板，输入自然语言指令（如“创建一个产品展示布局”），观察场景自动生成并调整。
6. 使用内置任务板跟踪多步骤工作流，并通过视口预览实时查看结果。"
pitfallGuide: "确保 Blender 版本为 4.2 或更高，否则插件可能不兼容。
需要有效的 AI 模型 API 密钥或本地 Ollama 服务，否则无法使用对话功能。
MCP 服务器默认端口可能被占用，需检查并修改配置。
复杂场景操作可能消耗较多 token，建议设置预算限制。
Windows 用户需注意路径权限，避免插件安装失败。"
targetAudience: ["独立开发者", "内容创作者", "技术负责人"]
useCases: ["快速生成产品展示场景", "自动化重复性 3D 建模任务", "通过对话辅助材质编辑与调整", "多步骤 3D 工作流编排"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI assistant and MCP server for Blender: visual chat, scene tools, multi-agent workflows. Works with OpenAI, ChatGPT, Claude, Gemini, Ollama, OpenCode. Blender AI addon and plugin, copilot for 3D, bpy Python scripting, MCP integration.

> GitHub: [LiCinCan/blender-ai-mcp-addon](https://github.com/LiCinCan/blender-ai-mcp-addon) | ⭐ 790 | Python

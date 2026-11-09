---
title: "Sandflow 3D 建模库"
description: "用 Python 编写 3D 模型的 LLM 友好库"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/Sandflow-ai/sand3d"
githubStars: 1511
githubOwner: "Sandflow-ai"
githubRepo: "sand3d"
category: "code-generation"
tags: ["3d-modeling", "python", "llm", "blender"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "sand3d 让用户用简短的 Python 代码描述 3D 物体的构造过程，特别适合让大语言模型生成可读、可编辑的 3D 模型代码。它解决了传统 3D 建模门槛高、LLM 难以直接生成复杂几何体的问题，适合独立开发者、产品设计师和 AI 研究者快速原型化 3D 内容。"
vibeCodingPrompt: "1. 安装 Blender 和 sand3d：pip install sand3d（确保已安装 Blender 并配置 bpy）。2. 在 Claude Code 中创建一个新 Python 文件，导入 sand3d 并定义一个简单函数，例如生成一个带圆角的立方体。3. 使用 sand3d 的 API 描述形状的剖面、拉伸和编辑步骤，让 Claude 根据自然语言描述生成对应的 Python 代码。4. 运行脚本，在 Blender 中查看结果，根据反馈调整代码。5. 将常用形状封装成可复用的函数，并让 Claude 生成一个包含多个零件的装配体示例。"
pitfallGuide: "需要预先安装 Blender 并确保 bpy 模块可用，否则无法运行
sand3d 依赖 Blender 的 Python 环境，建议在 Blender 自带的 Python 中安装
LLM 生成的代码可能包含不支持的几何操作，需逐步验证
复杂模型可能超出 token 限制，建议分块生成
文档和示例较少，遇到问题需参考 GitHub issues 或社区"
targetAudience: ["独立开发者", "AI 研究者", "产品经理", "内容创作者"]
useCases: ["用自然语言快速生成 3D 原型", "为 LLM 构建 3D 建模数据集", "教育场景中讲解几何构造", "游戏或 AR 中的程序化资产生成"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。3D modeling in Python, built for LLMs.

> GitHub: [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d) | ⭐ 1511 | HTML

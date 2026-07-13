---
title: "潜台词"
description: "实时观察语言模型的内部思考过程"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/ninjahawk/Subtext"
githubStars: 193
githubOwner: "ninjahawk"
githubRepo: "Subtext"
category: "data-analysis"
tags: ["interpretability", "visualization", "llm", "mechanistic-interpretability"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Subtext 是一个实时可视化工具，能展示语言模型在推理过程中的内部表征（J-space）。适合AI研究者或开发者深入理解模型如何思考、推理和生成答案，从而调试模型行为或进行可解释性研究。"
vibeCodingPrompt: "首先，克隆仓库并安装依赖：pip install -r requirements.txt。然后，运行主脚本启动本地Web服务器：python subtext/run_server.py。接着，在浏览器中打开 http://localhost:7860，加载一个Qwen3.5-4B模型（自动下载）。最后，在输入框中输入提示词，观察右侧可视化面板中模型各层的激活状态和J-space变化。如需扩展，可修改subtext/visualizer.py自定义可视化样式。"
pitfallGuide: "需要CUDA支持的GPU，否则性能严重下降\n模型下载可能因网络问题失败，建议提前下载到本地\n仅支持Qwen3.5-4B模型，其他模型需适配\n实时可视化对显存要求高，建议至少8GB VRAM\n浏览器端渲染大量数据可能卡顿，可降低刷新率"
targetAudience: ["AI研究者", "技术负责人", "机器学习工程师"]
useCases: ["调试模型推理过程中的错误行为", "研究语言模型的可解释性和内部机制", "教学演示LLM的内部工作原理", "比较不同提示词对模型思考路径的影响"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。To know what models don't say out loud.

> GitHub: [ninjahawk/Subtext](https://github.com/ninjahawk/Subtext) | ⭐ 193 | HTML

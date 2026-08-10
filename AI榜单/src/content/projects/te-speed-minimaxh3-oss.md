---
title: "MiniMax-H3 超速缓存加速器"
description: "为 ComfyUI 视频生成模型提供高达45%的推理加速"
publishDate: 2026-08-10
featured: false
githubUrl: "https://github.com/HELPMEEADICE/TE-Speed-MiniMaxH3-OSS"
githubStars: 203
githubOwner: "HELPMEEADICE"
githubRepo: "TE-Speed-MiniMaxH3-OSS"
category: "dev-tools"
tags: ["comfyui", "video-generation", "inference-speedup", "minimax-h3"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "本插件通过缓存残差和部分块计算，显著加速 MiniMax-H3 视频生成模型的推理速度，无需牺牲画质即可将生成时间缩短近一半。适合使用 ComfyUI 进行 AI 视频创作的创作者、工作室和内容团队，能大幅提升产出效率。"
vibeCodingPrompt: "1. 在 ComfyUI 的 custom_nodes 目录下安装此插件，并运行 python patch_model.py 完成模型补丁。\n2. 加载示例工作流 minimax_h3_TE_Speed加速高达45%(示例工作流).json，或手动将 UNETLoader 的输出连接到 TESpeedMiniMaxH3 节点。\n3. 根据需求调整节点参数：processing_control_value 控制缓存灵敏度，processing_percent_1/2 设置缓存窗口，mcs 限制连续缓存步数。\n4. 运行工作流，观察控制台输出的加速百分比，并根据结果微调参数以平衡速度与质量。"
pitfallGuide: "1. 首次使用前务必运行 patch_model.py，且确认已备份原文件，以便回退。\n2. 若使用 CPU 存储缓存，会引入搬运开销，可能降低实际加速效果。\n3. 缓存窗口和 mcs 参数设置不当可能导致画质下降，建议从默认值开始调整。\n4. 插件仅适用于 MiniMax-H3 模型，其他模型无法使用。\n5. 确保 ComfyUI 版本兼容，否则钩子可能无法正确注入。"
targetAudience: ["独立开发者", "内容创作者", "AI 研究者", "技术负责人"]
useCases: ["加速 AI 视频生成工作流，提升创作效率", "在资源受限环境下降低视频生成耗时", "批量生成视频内容时减少总处理时间", "实验不同缓存参数以优化画质与速度平衡"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。MiniMax-H3超级缓存加速插件

> GitHub: [HELPMEEADICE/TE-Speed-MiniMaxH3-OSS](https://github.com/HELPMEEADICE/TE-Speed-MiniMaxH3-OSS) | ⭐ 203 | Python

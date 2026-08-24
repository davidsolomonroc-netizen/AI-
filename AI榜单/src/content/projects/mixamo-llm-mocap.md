---
title: "Mixamo LLM 动捕管道"
description: "视频转 Mixamo 骨骼动画，AI 全流程自动操作"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/squall01337/mixamo-llm-mocap"
githubStars: 173
githubOwner: "squall01337"
githubRepo: "mixamo-llm-mocap"
category: "workflow-automation"
tags: ["mocap", "blender", "ai-agent", "retargeting"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目能把普通视频（手机拍摄或AI生成）自动变成 Mixamo 角色的骨骼动画，无需动捕设备和手动K帧。适合动画师、游戏开发者、内容创作者快速制作角色动作，或需要批量生成动画的团队。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖（见 README，需 CUDA GPU 约8GB显存）。\n2. 准备一段锁定的相机视频，开头和结尾有 T-pose 作为校准。\n3. 运行 estimate_pose_gvhmr.py 提取姿态数据。\n4. 运行 analyze_landmarks.py 生成节拍数据，并编写动作规格 JSON。\n5. 使用 lift_to_mixamo.py 重定向到你的 Mixamo 角色。\n6. 启动 Blender 并启用 MCP 服务器，运行 apply_mixamo_fk.py 应用动画。\n7. 用 qa_clip.py 自动检查动画质量，必要时迭代。"
pitfallGuide: "需要 CUDA GPU（约8GB显存），CPU 可能跑不动\n视频必须是锁定相机，且需要 T-pose 书挡（开头和结尾）\nBlender 版本需 5.1+ 且需配置 MCP 服务器\n多角色场景需按屏幕侧分离，注意角色比例差异\n动作规格 JSON 需根据节拍数据手动调整，不适合完全零干预"
targetAudience: ["独立开发者", "内容创作者", "AI 研究者", "技术负责人"]
useCases: ["快速制作游戏角色动画原型", "将 AI 生成视频转为动画资产", "批量生成动作库", "教学演示动捕流程"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Turn any video into a Mixamo-rig animation - GVHMR estimator, spec-driven retarget, FK apply in Blender via MCP. Works with any Mixamo character; built to be operated end-to-end by an AI agent.

> GitHub: [squall01337/mixamo-llm-mocap](https://github.com/squall01337/mixamo-llm-mocap) | ⭐ 173 | Python

---
title: "J-Wash: 模型身份重塑工具"
description: "通过编辑令牌方向重塑LLM行为并导出检查点"
publishDate: 2026-07-20
featured: false
githubUrl: "https://github.com/Extraltodeus/J-Wash"
githubStars: 182
githubOwner: "Extraltodeus"
githubRepo: "J-Wash"
category: "other"
tags: ["model-editing", "interpretability", "alignment", "visualization"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "J-Wash 让用户无需训练或数据集即可手动编辑大型语言模型的身份和行为，通过可视化 Jacobian 空间进行令牌方向调整，并导出可运行的检查点。适合 AI 研究者、模型对齐工程师以及需要快速定制模型个性的技术团队。"
vibeCodingPrompt: "使用 J-Wash 项目进行模型编辑：
1. 克隆仓库并按照 README 的安装指南（原生或 Docker）设置环境。
2. 启动 FastAPI + React 本地工作室。
3. 加载一个 Hugging Face 模型（例如 Qwen2.5-0.5B）。
4. 加载预计算或实时拟合的 Jacobian 透镜。
5. 在聊天界面中与模型交互，同时观察各层“读取”的令牌方向。
6. 使用“洗”功能编辑令牌（例如将“我是一个大型语言模型”改为“我是一个大型语言鱼”）。
7. 导出编辑后的模型为 safetensors 检查点（完整、修改层或 LoRA）。
8. 在任何支持 transformers 的环境中加载并使用导出的模型。"
pitfallGuide: "1. 确保显卡内存足够，编辑大型模型（如 7B 参数）需要较高资源。
2. 编辑效果依赖透镜质量，首次使用建议先拟合透镜（fit your own lens）。
3. 导出检查点后需验证行为是否与预览一致，避免意外副作用。
4. 令牌编辑可能引入不可逆变化，建议在副本模型上操作。
5. 项目仍在早期阶段（0.0.1），API 和 UI 可能不稳定。"
targetAudience: ["AI研究者", "技术负责人", "独立开发者"]
useCases: ["快速定制开源模型的身份和对话风格", "研究模型内部表示和机械可解释性", "生成特定角色或领域专用的轻量级模型变体"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Jacobian-Brainwash : A manual alignment tool for large language models built on Anthropic's Jacobian Lens. Results are exportable.

> GitHub: [Extraltodeus/J-Wash](https://github.com/Extraltodeus/J-Wash) | ⭐ 182 | Python

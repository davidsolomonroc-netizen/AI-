---
title: "CDAF：视频AI缓存描述文件格式"
description: "让AI代理不再重复分析视频的开放侧车格式"
publishDate: 2026-08-31
featured: false
githubUrl: "https://github.com/UditAkhourii/cdaf"
githubStars: 101
githubOwner: "UditAkhourii"
githubRepo: "cdaf"
category: "multimodal"
tags: ["video-understanding", "sidecar", "token-optimization", "agent-skill"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "CDAF 是一种开放的视频侧车文件格式，为每个视频生成一份带时间戳的文本描述，AI代理只需读取几百个token即可理解视频内容，无需重复进行视频分析。适用于需要频繁处理视频素材的团队，如内容审核、视频检索、自动剪辑等场景，可大幅降低AI计算成本和延迟。"
vibeCodingPrompt: "1. 首先，在项目中安装 CDAF CLI：`pip install \"cdaf[generate] @ git+https://github.com/UditAkhourii/cdaf.git#subdirectory=cli\"`
2. 然后，对你的视频文件夹运行 `cdaf generate ./footage` 生成 .cdaf 描述文件。
3. 在你的 Claude Code 项目中，添加 CDAF 技能：运行 `npx cdaf-skill` 安装 agent skill。
4. 之后，你的 AI 代理会自动检查 .cdaf 文件，在分析视频前先读取描述，避免重复计算。
5. 如需自定义描述格式，可参照 SPEC.md 调整生成参数。"
pitfallGuide: "1. 确保视频文件与 .cdaf 文件同名且在同一目录，否则代理无法找到对应描述。
2. 首次生成描述仍需消耗视频分析token，但只需一次，后续所有代理复用。
3. 描述文件需与视频哈希校验，若视频被修改需重新生成，否则代理可能使用过期描述。
4. 当前 CLI 依赖 Python 环境，需确保 pip 安装成功。
5. 基准测试基于特定模型，实际效果可能因模型而异，建议先在小规模数据上验证。"
targetAudience: ["AI研究者", "内容创作者", "企业团队", "独立开发者"]
useCases: ["视频素材库的AI检索与索引", "自动化视频剪辑中的场景识别", "视频内容审核的预筛选", "多代理协作中的视频理解复用"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。CDAF (Cached Descriptive Asset Files) - open sidecar format for video so AI agents stop re-analyzing the same footage. Spec, CLI, agent skill, reproducible benchmark.

> GitHub: [UditAkhourii/cdaf](https://github.com/UditAkhourii/cdaf) | ⭐ 101 | Python

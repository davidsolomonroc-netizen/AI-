---
title: "FigMirror：一键复现论文图表风格"
description: "上传参考图和数据，自动生成可编辑的matplotlib脚本和PDF。"
publishDate: 2026-05-25
featured: false
githubUrl: "https://github.com/VILA-Lab/FigMirror"
githubStars: 264
githubOwner: "VILA-Lab"
githubRepo: "FigMirror"
category: "data-analysis"
tags: ["data-visualization", "LLM-agents", "paper-figures", "matplotlib"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "FigMirror能帮你省去手动调整图表样式的时间：只需提供一张参考图和你自己的数据，AI就能生成风格一致的matplotlib脚本和出版级PDF。适合科研人员、数据分析师、自媒体作者等需要频繁制作美观图表的人群。"
vibeCodingPrompt: "你是一个数据可视化助手，使用FigMirror项目。请按以下步骤操作：
1. 从用户处获取一张参考图（任意论文或报告的图表）和用户的数据（CSV/Excel/JSON格式）。
2. 运行项目的Web UI（`python app.py`）或通过Claude Code skill接口调用。
3. 将参考图上传至FigMirror，粘贴或上传用户数据。
4. 点击“生成”按钮，等待AI返回matplotlib脚本和PDF预览。
5. 若结果不满意，可要求调整参数（如颜色、字体、图例位置）后重新生成。
6. 最终导出可编辑的.py脚本和PDF文件。"
pitfallGuide: "1. 参考图需清晰且风格统一，模糊或混合多风格图可能导致输出混乱。\n2. 数据格式必须与参考图匹配（如柱状图需要分类和数值列），否则AI可能无法正确映射。\n3. 复杂图表（如3D图、多子图嵌套）可能生成失败，建议先试简单样式。\n4. 生成的matplotlib脚本可能需要手动微调（如字体大小、坐标轴范围）。\n5. Web UI依赖本地Python环境，确保已安装所有依赖（见requirements.txt）。"
targetAudience: ["科研人员", "数据分析师", "内容创作者", "产品经理"]
useCases: ["科研论文中复现他人图表风格", "数据报告快速生成统一风格的图表", "自媒体文章配图风格化", "教学材料中制作风格一致的示意图"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。An Automated AI Agent Tool for Plotting Your Data in Any Paper's Figure Style.

> GitHub: [VILA-Lab/FigMirror](https://github.com/VILA-Lab/FigMirror) | ⭐ 264 | Python

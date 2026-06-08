---
title: "演讲者笔记生成器"
description: "为学术PPT自动生成逐页演讲稿"
publishDate: 2026-06-08
featured: false
githubUrl: "https://github.com/AI272/speaker"
githubStars: 149
githubOwner: "AI272"
githubRepo: "speaker"
category: "workflow-automation"
tags: ["pptx", "speaker-notes", "ocr", "vision-review"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该工具自动从PPTX中提取文本、表格、图表和图像，结合OCR和视觉审查生成逐页演讲稿，并直接写入PPT备注区。适合需要快速准备高质量演讲备注的学者、教师和商务人士。"
vibeCodingPrompt: "请使用speaker技能包处理我的.pptx文件：1. 读取PPTX并提取所有可见元素（文本、表格、图表、图像）。2. 将每页幻灯片渲染为PNG图像。3. 对图像执行OCR和视觉审查，识别图表、截图中的文字。4. 基于所有证据生成逐页演讲稿（展示版和干净版）。5. 将干净版演讲稿注入PPTX的备注区。6. 输出包含备注的最终PPTX文件。"
pitfallGuide: "1. 确保输入的.pptx文件路径正确且文件可读。\n2. OCR和视觉审查依赖外部模型，首次运行可能需要下载模型文件。\n3. 复杂图表（如SmartArt、3D图表）的识别可能不完美，建议手动复核。\n4. 生成的演讲稿是英文的，中文支持取决于底层OCR模型。\n5. 注入备注会覆盖原有备注，请提前备份原始文件。"
targetAudience: ["学者", "教师", "商务人士", "内容创作者"]
useCases: ["学术会议演讲准备", "课堂教学备注生成", "商务演示脚本撰写", "在线课程内容整理"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Speaker is a Codex skill project for academic presentations: read real.pptx, combine text extraction, PPTX structure parsing, page-by-page rendering, OCR, and visual review to generate page-by-page speaker notes, and write a clean version of the lecture into the PowerPoint comment area.

> GitHub: [AI272/speaker](https://github.com/AI272/speaker) | ⭐ 149 | Python

---
title: "Indra OCR：极速CPU文档识别"
description: "每秒49页的CPU OCR，PDF转Markdown"
publishDate: 2026-10-19
featured: false
githubUrl: "https://github.com/datalab-to/indra"
githubStars: 640
githubOwner: "datalab-to"
githubRepo: "indra"
category: "multimodal"
tags: ["OCR", "CPU", "PDF", "Markdown"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Indra OCR 是一个超高速的 CPU 文字识别工具，能把 PDF 和图片快速转成 Markdown 或结构化文本，速度比传统方案快 10 倍以上。适合需要批量处理文档的团队，比如财务、法务、档案管理，也适合开发者集成到自己的应用里。"
vibeCodingPrompt: "1. 安装依赖：pip install indra-ocr（或从 GitHub 克隆并安装）。2. 下载模型权重（参考 README 的 Hugging Face 链接）。3. 写一个 Python 脚本，用 indra 的 API 读取本地 PDF 文件，输出 Markdown。4. 将脚本封装成命令行工具，支持批量处理文件夹。5. 用 FastAPI 搭建一个简单服务，上传 PDF 返回 Markdown 结果。6. 用 Claude Code 生成测试用例，验证不同版式的 PDF 识别效果。"
pitfallGuide: "模型权重需要单独下载，注意存储空间。
CPU 推理需要足够内存，建议至少 4GB 可用。
复杂版式（多栏、表格）可能需后处理。
输出格式为 JSON 时注意字段解析。
商业使用需遵守 OpenRAIL-M 模型许可证。"
targetAudience: ["独立开发者", "企业团队", "产品经理", "数据分析师"]
useCases: ["批量将扫描版 PDF 转为可编辑 Markdown", "发票、合同等文档的结构化信息提取", "构建文档问答系统的预处理管道", "在无 GPU 环境下快速部署 OCR 服务"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Fast CPU OCR: line detection, CTC recognition, reading order, markdown

> GitHub: [datalab-to/indra](https://github.com/datalab-to/indra) | ⭐ 640 | Python

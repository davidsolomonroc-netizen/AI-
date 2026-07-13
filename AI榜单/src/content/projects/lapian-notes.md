---
title: "拉片笔记"
description: "AI辅助电影拉片笔记工具"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/bkingfilm/lapian-notes"
githubStars: 293
githubOwner: "bkingfilm"
githubRepo: "lapian-notes"
category: "other"
tags: ["film-analysis", "ai", "notetaking", "react"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "拉片笔记是一款将电影转化为可编辑拉片笔记的本地工具，适合电影学习者和创作者。它自动抽帧、生成剧情泳道图、结构树和情绪曲线，并支持AI分析，全程数据不上传服务器。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖: git clone https://github.com/bkingfilm/lapian-notes.git && cd lapian-notes && npm install
2. 启动开发服务器: npm run dev
3. 在浏览器中打开应用，导入一部电影文件
4. 按照顶部四步向导操作：导入电影 -> 生成AI分析包 -> 将ZIP发给AI（如ChatGPT）并粘贴指令 -> 导入AI返回的JSON结果
5. 在泳道时间轴、结构树和情绪曲线视图中查看分析结果，并手动精修段落笔记
6. 使用播放器联动功能跳转到任意时间点进行深入分析
7. 导出笔记为Markdown、剧本正文或分享长图"
pitfallGuide: "1. 目前UI仅支持中文，非中文用户需等待国际化更新
2. 需要本地运行，首次使用需等待依赖安装和浏览器自动打开
3. AI分析需要自行准备AI服务（如ChatGPT），项目不内置AI API
4. 抽帧和转码过程可能较慢，取决于电影文件大小和电脑性能
5. 自动字幕搜索可能不完美，需手动检查或补充"
targetAudience: ["内容创作者", "产品经理", "独立开发者"]
useCases: ["电影学习者系统分析影片叙事结构", "编剧或导演拆解经典电影的剧情线、情绪节奏", "内容创作者将拉片笔记导出为分享内容", "AI辅助电影分析教学和研究"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。拉片笔记:把电影变成 AI 辅助的拉片笔记 - 本地抽帧/剧情泳道时间轴/结构树/情绪曲线/段落深拆

> GitHub: [bkingfilm/lapian-notes](https://github.com/bkingfilm/lapian-notes) | ⭐ 293 | TypeScript

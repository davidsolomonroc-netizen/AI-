---
title: "AI 图像扩展器"
description: "用AI无缝扩展任意图像并生成2D游戏素材"
publishDate: 2026-06-01
featured: false
githubUrl: "https://github.com/boona13/image-extender"
githubStars: 319
githubOwner: "boona13"
githubRepo: "image-extender"
category: "multimodal"
tags: ["outpainting", "game-art", "gemini", "openrouter"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个开源网页应用，允许用户通过AI扩展图像边缘，并生成2D游戏艺术素材（如视差背景、自动图块、精灵动画和装饰道具）。适合独立游戏开发者、设计师和内容创作者，无需编程即可在浏览器中完成图像外延和游戏素材制作。"
vibeCodingPrompt: "1. 使用boona13/image-extender项目搭建一个本地的AI图像扩展服务。
2. 确保Node.js和npm已安装，然后克隆仓库并运行npm install和npm run dev启动开发服务器。
3. 在浏览器中打开http://localhost:3000，上传一张图片，选择扩展方向（上下左右）并点击“Extend”按钮。
4. 如需生成游戏素材，切换到Parallax Studio、Tile Studio或Sprite Studio模式，按照界面提示设置层数和生成参数。
5. 导出生成的素材时，注意检查泊松融合效果，必要时使用best-of-3变体选择器优化接缝。"
pitfallGuide: "1. 需要自备OpenRouter API密钥，密钥存储在浏览器本地，不会上传到服务器。\n2. 泊松融合对复杂背景（如密集纹理）可能产生不自然接缝，建议多次尝试不同变体。\n3. 生成游戏素材时，AI提示词需要精确描述每层风格，否则层间风格不统一。\n4. 大尺寸图像扩展（如超过1024x1024）可能消耗较多API配额，注意控制成本。\n5. 项目依赖Next.js和Tailwind CSS，部署到生产环境前需配置环境变量。"
targetAudience: ["独立开发者", "游戏开发者", "内容创作者", "设计师"]
useCases: ["将手机竖拍照片扩展为宽屏电影画面", "为2D平台游戏生成自动图块和视差背景", "创建角色精灵动画序列", "制作游戏装饰道具和场景元素"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Seamlessly extend any image in any direction with AI. Open-source web app powered by Gemini via OpenRouter, with Poisson-blended seams and best-of-3 variant picker.

> GitHub: [boona13/image-extender](https://github.com/boona13/image-extender) | ⭐ 319 | TypeScript

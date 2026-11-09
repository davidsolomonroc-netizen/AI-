---
title: "AI 同事工牌生成器"
description: "为九位 AI 同事制作可拖拽、可翻面的 3D 工牌，支持中英文和透明 PNG 下载。"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/fanhuayishiy/ai-crew-pass"
githubStars: 111
githubOwner: "fanhuayishiy"
githubRepo: "ai-crew-pass"
category: "other"
tags: ["3D", "React", "Astro", "AI 同人"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个趣味性的 AI 同人工具，让用户为常见的 AI 模型（如 DeepSeek、ChatGPT 等）生成可交互的 3D 工牌，并下载为图片。适合 AI 爱好者、内容创作者用于社交媒体分享或活动展示，也适合作为教学演示或团队品牌宣传的创意素材。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/fanhuayishiy/ai-crew-pass.git 并进入目录。
2. 安装依赖：确保 Node.js 22.12+，运行 npm install --no-package-lock。
3. 启动开发服务器：npm run dev -- --host 127.0.0.1，在浏览器打开 http://127.0.0.1:4321 查看效果。
4. 自定义角色：编辑 src/data/characters.ts 修改 AI 同事名称、配色和头像素材；编辑 src/data/i18n.ts 和 memes.ts 调整中英文文案和口头禅。
5. 更新卡面素材：如需修改工牌正面设计，运行 python -X utf8 scripts/export-badge-faces.py 和 python -X utf8 scripts/export-downloads.py 重新生成下载文件。
6. 构建与部署：运行 npm run build 生成静态文件，可将 dist 目录部署到任意静态托管（如 GitHub Pages、Vercel）。
7. 集成到现有项目：可将 BadgeExperience.astro 组件嵌入 Astro 页面，或参考其逻辑用 React 重构。"
pitfallGuide: "需要 Node.js 22.12 或更高版本，低版本可能无法运行。
修改卡面后必须运行导出脚本更新下载文件，否则下载内容不会同步。
WebGL 不可用时自动降级为静态预览，但 3D 交互效果会丢失。
音频素材默认开启，首次交互后加载，若需静音可点击右上角按钮。
部署到 GitHub Pages 时需正确配置 GITHUB_PAGES_URL 或 CNAME，否则资源路径可能错误。"
targetAudience: ["独立开发者", "内容创作者", "产品经理", "AI 爱好者"]
useCases: ["为 AI 模型制作趣味工牌并分享到社交媒体", "在技术分享或活动中展示 AI 同事形象", "作为教学案例学习 3D 交互与前端工程化", "自定义团队 AI 助手品牌素材"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。非人类员工｜九位 AI 同事的 3D 工牌领取处，中英文、透明 PNG 下载。微信公众号：风花AI实验室。

> GitHub: [fanhuayishiy/ai-crew-pass](https://github.com/fanhuayishiy/ai-crew-pass) | ⭐ 111 | TypeScript

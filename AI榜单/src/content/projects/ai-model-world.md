---
title: "大模型像素世界"
description: "556 个大模型拟人化像素小人可视化站点"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/liyupi/ai-model-world"
githubStars: 153
githubOwner: "liyupi"
githubRepo: "ai-model-world"
category: "data-analysis"
tags: ["llm-leaderboard", "data-visualization", "nextjs", "static-site"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 3
commercialSummary: "把五百多个 AI 大模型做成像素小人可视化看板，一眼看清谁最强、谁最便宜、谁刚发布。适合 AI 从业者、产品经理和内容创作者快速了解行业格局，无需登录、零后端、可静态部署。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/liyupi/ai-model-world && cd ai-model-world。2. 安装依赖：npm install（Node 18+）。3. 运行 npm run dev 本地预览，确认像素广场、时间线、排行榜页面正常。4. 修改 src/data 目录下的模型数据源配置或同步脚本，接入你自己的模型数据（如公司内部模型清单）。5. 用 npm run build 生成静态导出，部署到 Vercel/Netlify/任意静态托管。6. 如需定制像素角色外观，参考 docs/DESIGN.md 修改属性到形象的映射阈值和厂商母题。"
pitfallGuide: "数据来自 Epoch AI、models.dev 等外部源，同步脚本可能因对方 API 变更或限流失败，需检查 fallback 逻辑
跨赛制的编程分数不可混算，同一模型换评测脚手架能差二三十分，展示时要保留原始来源标注
厂商自报成绩需带「自报」标识，避免与第三方评测混淆
静态导出无后端，搜索是前端本地索引，模型量再增大时注意首屏包体积
像素角色与能力条是两套系统，改外观不影响数据，改数据阈值会触发角色形象变化，需同步更新 DESIGN.md"
targetAudience: ["产品经理", "内容创作者", "AI 研究者", "独立开发者"]
useCases: ["快速了解当前大模型格局与厂商分布", "横向对比模型能力、价格与上下文长度", "追踪模型发布时间线与新模型动态", "作为 AI 资讯或课程的可视化素材"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI 大模型世界，把 556 个大模型拟人化成像素小人的可视化站点。进来就能看到此刻谁最聪明、谁最会写代码、谁最便宜、谁刚发布，往下是国内与国外分区的厂商广场、完整的发布时间线和多维排行榜。搜索认模型名、厂商和能力，输入「多模态」会直接列出全部多模态模型。数据取自 Epoch AI、models.dev、LiveBench 与 Hugging Face，每小时自动同步，所有文案由真实数据生成，不调用任何 LLM。Next.js 静态导出，零后端。

> GitHub: [liyupi/ai-model-world](https://github.com/liyupi/ai-model-world) | ⭐ 153 | TypeScript

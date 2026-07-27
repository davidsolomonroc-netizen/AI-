---
title: "播客短视频工厂"
description: "十位AI代理自动将播客转为短视频"
publishDate: 2026-07-27
featured: false
githubUrl: "https://github.com/krakonjac300-pixel/podcast-shorts-factory"
githubStars: 76
githubOwner: "krakonjac300-pixel"
githubRepo: "podcast-shorts-factory"
category: "workflow-automation"
tags: ["podcast", "video-automation", "ai-agents", "youtube-shorts"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该工具通过十个协作AI代理，自动将长播客内容提取精彩片段、剪辑为竖屏短视频并发布到YouTube Shorts，适合内容创作者和播客运营者低成本批量生产短视频。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：git clone && cd podcast-shorts-factory && pip install -r requirements.txt
2. 配置免费AI提供商（如OpenRouter、Groq）的API密钥到.env文件
3. 运行主脚本：python main.py --url <播客YouTube链接>
4. 系统自动执行下载、转录、剪辑、添加字幕和特效、质量检查、标题生成及发布流程
5. 可设置定时任务（cron）实现每日无人值守运行"
pitfallGuide: "1. 免费AI提供商可能有速率限制，需合理安排任务队列\n2. 首次运行需要下载whisper模型和ffmpeg，确保网络和系统依赖完备\n3. 视频渲染对GPU有一定要求，纯CPU环境可能会很慢\n4. YouTube API上传需要OAuth认证，需提前配置开发者项目"
targetAudience: ["内容创作者", "创业者", "独立开发者"]
useCases: ["播客频道自动生成YouTube Shorts", "知识类播客批量剪辑分发", "个人博客或课程内容短视频化", "自动化社交媒体内容矩阵运营"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Ten cooperating AI agents that turn long podcasts into short-form videos, automatically. Free and open source, runs on free AI providers.

> GitHub: [krakonjac300-pixel/podcast-shorts-factory](https://github.com/krakonjac300-pixel/podcast-shorts-factory) | ⭐ 76 | Python

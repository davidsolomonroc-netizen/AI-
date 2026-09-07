---
title: "AI短视频生成器"
description: "将YouTube长视频自动转为爆款短视频的开源工具"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/pierrenade/short-video-generator-AI"
githubStars: 1064
githubOwner: "pierrenade"
githubRepo: "short-video-generator-AI"
category: "multimodal"
tags: ["video-generation", "youtube-to-shorts", "highlight-detection", "auto-subtitles"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个免费开源的视频处理工具，可自动将YouTube长视频中的高光片段提取出来，配上字幕、翻译和AI配音，生成适合抖音、Reels等平台的9:16竖屏短视频。特别适合需要大量剪辑内容的自媒体创作者和视频营销团队，无需付费订阅即可替代OpusClip等商业服务。"
vibeCodingPrompt: "请帮我使用pierrenade/short-video-generator-AI项目搭建一个自动生成短视频的流水线。
1. 先克隆仓库并安装依赖：git clone https://github.com/pierrenade/short-video-generator-AI.git && cd short-video-generator-AI && pip install -r requirements.txt
2. 配置LLM API密钥（如OpenAI或本地模型），在.env文件中设置LLM_PROVIDER=openai和API_KEY
3. 运行命令行处理第一个视频：python main.py --youtube-url \"https://youtube.com/...\" --output-dir ./output
4. 如需添加AI钩子开头，加上--with-hook参数
5. 若想使用图形界面，运行python webui.py并访问localhost:5000
6. 检查output目录中的生成结果，调整highlight阈值和字幕样式参数优化输出"
pitfallGuide: "需要Python 3.10+环境，建议使用虚拟环境或Docker避免依赖冲突\n首次运行会下载whisper模型（约1GB），需要稳定网络和足够磁盘空间\nYouTube链接下载可能受地区限制或反爬策略影响，建议使用本地文件路径作为备选\nLLM API调用会产生费用，若使用免费本地模型需配置Ollama等额外服务\n处理长视频时耗时较长，建议先用5-10分钟的视频测试流程"
targetAudience: ["内容创作者", "创业者", "独立开发者", "技术负责人"]
useCases: ["自动将TED演讲、播客等长内容生成多个短视频用于多平台分发", "为YouTube频道制作预告片和精彩片段", "批量生成产品演示视频的社交媒体版本", "教育机构将在线课程转化为短视频知识点"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Free open-source project designed for turning youtube-viedos into viral short videos. Highlight detection, subtitles, translation, voiceover, all in one for your content.

> GitHub: [pierrenade/short-video-generator-AI](https://github.com/pierrenade/short-video-generator-AI) | ⭐ 1064 | Python

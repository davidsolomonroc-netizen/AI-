---
title: "DramaLens 短剧创作拆解助手"
description: "本地优先的短剧转写与创作结构分析工具"
publishDate: 2026-08-17
featured: false
githubUrl: "https://github.com/dengzi008/DramaLens"
githubStars: 122
githubOwner: "dengzi008"
githubRepo: "DramaLens"
category: "multimodal"
tags: ["speech-to-text", "chrome-extension", "local-first", "drama-analysis"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "DramaLens 帮助短剧创作者、编剧和内容分析者将视频素材自动转写为带时间码的文本，并生成可人工复核的剧情结构分析（如冲突节点、情绪曲线、反转等）。它本地运行语音识别，保护隐私，适合需要高效拆解大量短剧内容的个人或团队。"
vibeCodingPrompt: "1. 克隆项目仓库并安装依赖：`git clone https://github.com/dengzi008/DramaLens && cd DramaLens`。
2. 运行安装脚本 `install-local-asr.cmd`（Windows）或阅读 `docs/MACOS.md` 完成 macOS 配置。
3. 复制 `.env.example` 为 `.env`，如需 AI 分析则填入 `OPENAI_API_KEY` 和 `OPENAI_BASE_URL`。
4. 启动本地服务：双击 `start-asr.cmd` 或运行 `python server.py`，确保 `http://127.0.0.1:3211/api/health` 返回 `ok`。
5. 在 Chrome 中加载 `extension` 目录（开启开发者模式 → 加载已解压的扩展程序）。
6. 打开有权限处理的视频，在扩展中填写项目名称和集数范围，点击“开始采集”，按 F8/F10 控制录制结束。
7. 等待转写完成后，可手动校对时间轴和角色，再点击“AI校对并生成报告”调用配置的模型。
8. 导出 Word 报告或进行整体分析。"
pitfallGuide: "首次运行需下载 faster-whisper 模型（medium 约 1.5GB），建议预留足够磁盘空间。\nWindows 需确保系统音频设备支持 WASAPI Loopback，macOS 需安装 BlackHole 虚拟声卡。\nAI 分析仅在你显式点击后才会发送文本到外部 API，请确保配置正确的接口地址和密钥。\n转写和角色推断可能出错，务必人工复核才能用于正式创作。\n建议 8GB 以上内存，否则本地推理可能较慢或卡顿。"
targetAudience: ["内容创作者", "编剧", "短剧研究者", "产品经理"]
useCases: ["批量拆解短剧的节奏、冲突和反转结构", "快速整理访谈或课程视频的逐字稿和要点", "为短剧创作提供结构化的参考报告", "内容团队内部进行竞品分析"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Local-first Chrome extension for timestamped transcription and human-reviewed short-form drama analysis.

> GitHub: [dengzi008/DramaLens](https://github.com/dengzi008/DramaLens) | ⭐ 122 | JavaScript

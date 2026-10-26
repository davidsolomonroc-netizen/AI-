---
title: "37Studio"
description: "自托管AI视频制作与社媒管理平台"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/Shaitrish/37studio"
githubStars: 68
githubOwner: "Shaitrish"
githubRepo: "37studio"
category: "workflow-automation"
tags: ["self-hosted", "video-editing", "social-media", "claude-code"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "37Studio 是一个开源的 AI 视频工作室和社交媒体管理工具，能自动为品牌制作视频、一键发布到 9 个平台并起草回复。适合需要低成本运营多个社媒账号的创业者、内容创作者和小团队，用自己的 API 密钥，无需月费。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/Shaitrish/37studio.git 并进入目录。
2. 复制环境变量模板：cp .env.example .env，填入你的 Claude API 密钥、各社媒平台 API 凭证（如 Twitter、Instagram 等）以及视频渲染相关配置。
3. 使用 Docker 启动：docker compose up -d，等待服务启动后访问 http://localhost:3000。
4. 在网页中点击“添加品牌”，输入品牌网站 URL，系统会自动构建品牌库和知识库。
5. 创建视频项目，在聊天框输入视频简报（例如“制作一个 30 秒的产品介绍视频”），Claude Code 代理会生成 HyperFrames 合成并渲染视频。
6. 视频完成后，选择要发布的平台，填写或让 AI 生成各平台文案，点击发布（可立即、定时或自动模式）。
7. 在收件箱中查看所有平台的消息和评论，使用 AI 起草回复并发送。
8. 如需自定义，修改 worker 目录下的 Go 代码或前端组件，重新构建 Docker 镜像即可。"
pitfallGuide: "需要自行准备 Claude API 密钥和各社媒平台的开发者凭证，部分平台申请流程较复杂。
视频渲染依赖本地算力，低配机器可能较慢，建议分配足够 CPU 和内存。
Docker 部署需确保端口 3000 未被占用，且网络能访问外部 API。
首次使用需在网页中完成品牌设置和平台授权，否则无法发布。
自动发布功能需谨慎测试，避免误发内容到生产账号。"
targetAudience: ["独立开发者", "创业者", "内容创作者", "企业团队"]
useCases: ["为品牌批量制作并发布短视频到多个社媒平台", "统一管理多个社媒账号的消息和评论并自动回复", "为小型企业提供低成本的社媒运营方案", "内容创作者快速生成带品牌风格的视频内容"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Open-source AI alternative to Buffer and Opus Clip: Claude Code makes on-brand videos, posts them to 9 platforms and drafts replies. Self-hosted, your own keys.

> GitHub: [Shaitrish/37studio](https://github.com/Shaitrish/37studio) | ⭐ 68 | Go

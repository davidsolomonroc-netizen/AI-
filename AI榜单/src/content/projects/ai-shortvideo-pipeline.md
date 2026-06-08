---
title: "AI 短视频生产流水线"
description: "端到端自动化短视频制作平台"
publishDate: 2026-06-08
featured: false
githubUrl: "https://github.com/myccarl/ai-shortVideo-pipeline"
githubStars: 75
githubOwner: "myccarl"
githubRepo: "ai-shortVideo-pipeline"
category: "workflow-automation"
tags: ["video-generation", "ai-pipeline", "multi-model", "observability"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个开源的自动化短视频生产平台，覆盖从选题、脚本、画面、配音到后期发布的完整流程。适合内容创作者、新媒体团队或营销部门快速批量生成高质量短视频，降低人工剪辑成本。"
vibeCodingPrompt: "1. 克隆仓库并阅读 README.md 了解七层流水线架构。
2. 使用 docker-compose up 启动所有服务（包括 FastAPI 编排层、Java 网关、数据库和 AI 模型代理）。
3. 配置 Java 网关的 application.yml，填入 DeepSeek/Qwen/GLM 等模型的 API Key 和 fallback 策略。
4. 通过 FastAPI 的 /pipeline/start 接口提交一个视频主题，观察 SSE 流式进度。
5. 如果生成失败，检查 Langfuse 或日志中的 trace_id 定位问题环节，并手动触发单段重生成。
6. 调整 prompt_anchoring 模板或 CLIP 阈值，优化画面一致性。
7. 集成到自己的前端或定时任务中，实现自动化分发。"
pitfallGuide: "1. 需要同时配置 Python 和 Java 环境，部署复杂度较高，不适合纯小白。
2. 多模型 API Key 必须全部有效，否则 fallback 机制可能仍会超时。
3. CLIP 一致性检查会增加额外延迟，对实时性要求高的场景需调低阈值。
4. 视频生成依赖 ffmpeg，确保版本兼容且支持 GPU 加速。
5. 日志和计量数据默认存储在数据库，生产环境需配置持久化存储和备份。"
targetAudience: ["内容创作者", "企业团队", "技术负责人", "创业者"]
useCases: ["热点新闻自动解说视频生成", "知识科普类短视频批量生产", "情感故事类短视频创作", "社交媒体内容自动化分发"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。End-to-end AI short-video production pipeline. FastAPI orchestration + Spring Boot gateway with multi-model failover, circuit breaker, metering, and full-stack observability. AI quality gating: prompt anchoring, CLIP consistency, AV sync auto-rescue.

> GitHub: [myccarl/ai-shortVideo-pipeline](https://github.com/myccarl/ai-shortVideo-pipeline) | ⭐ 75 | Python

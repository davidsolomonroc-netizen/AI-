---
title: "AgentScope Java"
description: "企业级分布式长时运行智能体框架"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/agentscope-ai-java/agentscope-java"
githubStars: 108
githubOwner: "agentscope-ai-java"
githubRepo: "agentscope-java"
category: "agent-framework"
tags: ["Java", "Agent Framework", "Distributed", "Enterprise"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "AgentScope Java 是一个帮企业在 Java 技术栈上快速搭建 AI 智能体应用的框架，支持智能体长时间稳定运行、多智能体协作和实时前端交互。适合已有 Java 团队、希望把 AI 能力嵌入现有业务系统的企业使用。"
vibeCodingPrompt: "请帮我用 AgentScope Java 搭建一个客服智能体应用：1) 在 Maven 项目中引入 io.agentscope:agentscope 依赖（JDK 17+）；2) 参考官方文档 https://java.agentscope.io/ 创建 ReActAgent，配置 OpenAI 或 DashScope 模型；3) 添加一个查询订单状态的自定义工具函数并注册到 Agent；4) 通过事件流订阅 Agent 的回复事件，把结果输出到控制台；5) 最后写一个简单的 HTTP 接口（Spring Boot）接收用户问题并返回 Agent 回答。请给出完整可运行的代码和 pom.xml。"
pitfallGuide: "需要 JDK 17 及以上版本，低版本 JDK 无法运行
首次使用需正确配置模型 API Key（OpenAI/DashScope 等），否则 Agent 无法调用大模型
事件系统有 31 种类型事件，需按文档订阅正确的事件类型才能拿到输出
长时运行智能体要考虑会话状态持久化，避免重启后上下文丢失
分布式部署时注意多实例间的会话路由和并发控制"
targetAudience: ["企业团队", "技术负责人", "独立开发者"]
useCases: ["企业级客服智能体", "多智能体协作工作流", "长时运行的业务自动化助手", "Java 后端系统集成 AI 能力"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Build distributed, production-grade, long-running agents.

> GitHub: [agentscope-ai-java/agentscope-java](https://github.com/agentscope-ai-java/agentscope-java) | ⭐ 108 | Java

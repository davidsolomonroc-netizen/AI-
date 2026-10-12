---
title: "FDE 实战评测场"
description: "用编码智能体完成真实客户交付的在线评测系统"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/deeplethe/fde-gym"
githubStars: 82
githubOwner: "deeplethe"
githubRepo: "fde-gym"
category: "agent-framework"
tags: ["agent-evaluation", "coding-agent", "benchmark", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "传统编程评测只看代码对不对，但 AI 时代代码正确已不足以衡量工程师能力。FDE Gym 把真实客户交付场景变成评测题，要求你带着编码智能体完成从开发到上线的全流程，系统上线后才评分。适合想验证 AI 智能体实战能力的团队、招聘方和独立开发者。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/deeplethe/fde-gym && cd fde-gym。2. 用 Docker 启动本地环境：docker compose up -d，等待 PostgreSQL 和前端服务就绪。3. 打开 http://localhost:3000 查看评测面板，注册账号。4. 从 Hugging Face 数据集下载示例案例，或自己创建一个案例：定义客户需求、验收标准、上线检查项。5. 用 Claude Code 或 Cursor 打开案例工作区，让智能体根据需求生成完整交付系统。6. 将智能体产出的代码部署到案例指定的运行环境（Docker 容器或云服务）。7. 回到 FDE Gym 面板提交上线后的系统地址，系统自动运行验收测试并给出评分。8. 根据评分反馈迭代，重复 5-7 步直到通过所有验收项。"
pitfallGuide: "自托管需要 Docker 和 PostgreSQL 基础，纯小白建议先用官方托管版 fde-gym.com 体验
案例数据需从 Hugging Face 手动下载，国内网络可能需配置镜像
评测的是「上线后的系统」而非代码本身，必须确保服务可被外部访问
编码智能体生成的代码需要人工审查安全性，避免评测环境被注入攻击
免费自托管资源有限，并发评测多个案例时注意容器资源占用"
targetAudience: ["技术负责人", "独立开发者", "企业团队", "AI 研究者"]
useCases: ["招聘时评估工程师与 AI 协作的实战能力", "团队内部训练 FDE（前向部署工程师）交付流程", "对比不同编码智能体在真实交付场景中的表现", "作为教学工具演示从需求到上线的完整工程闭环"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The online judge for the LLM era. Every case is a real customer delivery: you work it with a coding agent, and your system is judged once it is live.

> GitHub: [deeplethe/fde-gym](https://github.com/deeplethe/fde-gym) | ⭐ 82 | TypeScript

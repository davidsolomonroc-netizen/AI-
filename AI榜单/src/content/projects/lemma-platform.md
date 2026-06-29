---
title: "Lemma：人机协作工作空间"
description: "开源的人与AI代理协作工作空间"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/lemma-work/lemma-platform"
githubStars: 170
githubOwner: "lemma-work"
githubRepo: "lemma-platform"
category: "workflow-automation"
tags: ["ai-agents", "workspace", "collaboration", "open-source"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Lemma 是一个开源工作空间，让人类和AI代理像团队一样协作。代理可以拥有角色、任务和权限，输出直接写入数据表而非聊天记录。适合需要将AI代理整合到业务流程中的团队，尤其是那些希望让AI承担具体岗位职责而非简单对话的组织。"
vibeCodingPrompt: "1. 克隆项目仓库: git clone https://github.com/lemma-work/lemma-platform.git\n2. 进入目录并安装依赖: cd lemma-platform && pip install -r requirements.txt\n3. 配置环境变量: 设置 LLM_API_KEY 为你的 Claude 或 ChatGPT API 密钥\n4. 启动服务: python run.py\n5. 创建第一个 Pod，定义任务和代理角色，将人类和AI代理分配到同一工作流中\n6. 通过前端界面或 CLI 监控任务执行，体验人机协作"
pitfallGuide: "1. 需要有效的 LLM API 密钥（Claude 或 ChatGPT），免费额度有限\n2. 自托管需要一定的运维经验，生产环境建议使用官方托管服务 lemma.work\n3. 目前社区规模较小（170星），文档和示例可能不够丰富\n4. 权限模型需要仔细设计，避免代理误操作或越权\n5. 与现有工作流工具的集成可能需要额外开发"
targetAudience: ["企业团队", "技术负责人", "独立开发者", "创业者"]
useCases: ["将AI代理作为团队成员参与项目管理与任务执行", "构建自动化审批流程，由AI代理初步处理并等待人类决策", "创建数据驱动的业务工作流，代理直接操作表格数据", "在软件开发中，让AI代理承担代码审查、测试等角色"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The open-source workspace where humans and AI agents work as one team.

> GitHub: [lemma-work/lemma-platform](https://github.com/lemma-work/lemma-platform) | ⭐ 170 | Python

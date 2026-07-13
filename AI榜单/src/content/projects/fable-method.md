---
title: "寓言工作流：思维、行动、验证"
description: "让AI模型按步骤思考、行动并自我验证。"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/Sahir619/fable-method"
githubStars: 300
githubOwner: "Sahir619"
githubRepo: "fable-method"
category: "agent-framework"
tags: ["agent-skills", "claude", "evaluation", "workflow"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目将高级AI模型（Claude Fable 5）的问题解决方法提炼为一套可被任何模型遵循的步骤：先分类任务、定义成功标准、并行收集证据、做出最小改动、观察验证结果。适合需要让AI代理更可靠、可审计的团队，尤其在复杂决策或代码修改场景中。"
vibeCodingPrompt: "使用此项目构建一个AI代理应用：
1. 克隆仓库并安装依赖（npm install）。
2. 阅读skills/目录中的三个核心技能文件：fable-method.md（思考）、fable-loop.md（行动）、fable-judge.md（验证）。
3. 在项目中引入fable-loop.js作为代理循环引擎，设置你的LLM API密钥。
4. 根据你的任务类型（如代码审查、文档生成）调整skills中的规则和阈值。
5. 运行eval/中的测试用例验证代理行为，记录失败案例并迭代规则。"
pitfallGuide: "1. 不要跳过“定义完成标准”步骤，否则代理可能偏离目标。\n2. 验证环节必须基于实际观察（如代码执行结果），而非模型自述。\n3. 初始阈值（如证据数量）需根据任务复杂度调整，避免过度收集。\n4. 确保并行收集证据时不会互相干扰（如文件锁定问题）。\n5. 失败案例是改进规则的黄金素材，务必保留并分析。"
targetAudience: ["AI研究者", "技术负责人", "独立开发者", "企业团队"]
useCases: ["让AI代理按规范流程执行代码修改任务", "构建可审计的自动化决策系统", "评估和比较不同AI模型的问题解决能力", "为AI代理添加自我验证和错误恢复机制"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。The Fable Workflow: how Claude Fable 5 worked, distilled into skills any model can run, with the eval that keeps it honest. Think / act / prove.

> GitHub: [Sahir619/fable-method](https://github.com/Sahir619/fable-method) | ⭐ 300 | JavaScript

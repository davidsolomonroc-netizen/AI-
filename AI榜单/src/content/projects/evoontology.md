---
title: "EvoOntology 自进化本体层"
description: "为数据智能体构建自进化本体层的插件"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/ruc-datalab/EvoOntology"
githubStars: 223
githubOwner: "ruc-datalab"
githubRepo: "EvoOntology"
category: "data-analysis"
tags: ["Agent", "Ontology", "Claude-Code", "Data-Analysis"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "EvoOntology 为 Claude Code 和 Codex 等 AI 编程助手增加一层会自我进化的「数据本体」，让 AI 理解业务数据的含义和关系。适合需要让 AI 自动分析复杂业务数据的数据分析师和企业团队。"
vibeCodingPrompt: "1. 克隆仓库 git clone https://github.com/ruc-datalab/EvoOntology 并阅读 README 与 plugins/claude-code 目录。
2. 按照文档将 evoontology 插件安装到 Claude Code（通常通过 MCP 配置或插件目录拷贝）。
3. 准备一个示例数据集（CSV/数据库表），让 Claude Code 调用 EvoOntology 工具自动抽取字段含义、实体关系，生成初始本体。
4. 基于生成的本体，用自然语言让 Claude Code 写一个数据分析脚本（如销售趋势、用户分群），验证本体是否被正确使用。
5. 运行分析后让本体根据反馈自动进化，再重跑一次分析对比效果提升。"
pitfallGuide: "安装依赖前确认 Python 版本符合要求，避免环境冲突
MCP/插件配置路径需与 Claude Code 或 Codex 的实际版本匹配
本体自动进化可能引入噪声，建议人工定期审查关键实体关系
处理敏感数据时注意本体中可能泄露字段语义信息
首次构建本体耗时较长，建议先用小数据集验证流程"
targetAudience: ["数据分析师", "AI 研究者", "企业团队", "技术负责人"]
useCases: ["让 Claude Code 自动理解企业数据库结构并生成分析报告", "为多源异构数据构建统一语义本体层", "辅助非技术用户用自然语言查询复杂业务数据", "在数据科学工作流中自动维护和演进数据字典"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。EvoOntology: A Self-Evolving Ontology Layer for Data Agents ⚙️ EvoOntology插件为Claude Code/Codex 建立&进化本体层

> GitHub: [ruc-datalab/EvoOntology](https://github.com/ruc-datalab/EvoOntology) | ⭐ 223 | Python

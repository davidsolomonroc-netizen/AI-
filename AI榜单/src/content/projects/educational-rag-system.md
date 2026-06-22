---
title: "教育场景智能问答系统"
description: "融合关键词与语义检索的双引擎RAG问答系统"
publishDate: 2026-06-22
featured: false
githubUrl: "https://github.com/Happy-Chen-CH/Educational_RAG_System"
githubStars: 137
githubOwner: "Happy-Chen-CH"
githubRepo: "Educational_RAG_System"
category: "agent-framework"
tags: ["RAG", "Education", "Milvus", "LLM"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "EduRAG面向教育行业，解决教材、题库等知识库的智能问答需求。它先通过MySQL关键词匹配快速回答常见问题，未命中时再使用Milvus向量检索和LLM生成答案，适合学校、培训机构或在线教育平台构建内部问答助手。"
vibeCodingPrompt: "使用此项目搭建一个教育问答系统：1. 克隆仓库并安装requirements.txt中的依赖；2. 配置config.ini中的MySQL、Redis、Milvus和DashScope API密钥；3. 准备教材/题库文档（支持PDF、Word、TXT），放入data/目录；4. 运行数据导入脚本将文档嵌入到Milvus知识库；5. 启动main.py并通过Web界面或API进行问答测试。"
pitfallGuide: "需要先启动MySQL、Redis和Milvus三个外部服务，对新手不友好\n依赖DashScope（通义千问）API，需申请并配置有效的API Key\n中文分词依赖jieba，专业术语可能需要自定义词典\nMilvus向量数据库的部署和配置较复杂，建议使用官方Docker镜像"
targetAudience: ["企业团队", "技术负责人", "AI 研究者"]
useCases: ["学校教材智能问答", "培训机构题库答疑", "在线教育平台知识库", "企业内部培训资料检索"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。面向教育场景的RAG智能问答系统，融合关键词匹配与语义检索双引擎，融合MySQL和RAG技术，先经过MySQL数据库的检索(还融合了Redis辅助储存和搜索)，若无符合条件答案，则进入RAG系统，RAG知识库中的知识储存在Milvus向量数据库中

> GitHub: [Happy-Chen-CH/Educational_RAG_System](https://github.com/Happy-Chen-CH/Educational_RAG_System) | ⭐ 137 | Python

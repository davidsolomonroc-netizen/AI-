---
title: "AI第二大脑操作系统"
description: "AI自动构建和维护的Markdown知识库系统"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/undefined-ui/second-brain-os"
githubStars: 59
githubOwner: "undefined-ui"
githubRepo: "second-brain-os"
category: "workflow-automation"
tags: ["second-brain", "obsidian", "claude-code", "knowledge-management"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目解决的是「收藏了但从不回看」的问题。它让AI代理自动把你保存的网页、视频、笔记整理成互相链接的wiki页面，存储在你自己的Markdown文件里。适合知识工作者、研究者和内容创作者，用Obsidian加Claude Code就能搭建一个会自我生长的个人知识库。"
vibeCodingPrompt: "我想用 second-brain-os 项目搭建一个自动维护的个人知识库。请帮我按以下步骤操作：
1. 克隆仓库：git clone https://github.com/undefined-ui/second-brain-os.git
2. 复制模板到我的知识库目录：cp -r second-brain-os/vault-template ~/brain
3. 创建Claude配置目录并复制技能、命令和代理：mkdir -p ~/brain/.claude && cp -r second-brain-os/skills ~/brain/.claude/skills && cp -r second-brain-os/commands ~/brain/.claude/commands && cp -r second-brain-os/agents ~/brain/.claude/agents
4. 进入目录启动Claude Code：cd ~/brain && claude
5. 阅读 docs/02-setup/ 下的安装文档，帮我完成Obsidian安装、Claude Code配置和可选的MCP连接
6. 根据文档引导我完成CLAUDE.md的访谈配置，让代理了解我的知识领域和偏好
7. 测试一个实际场景：我保存一篇文章，让代理自动生成wiki页面并链接到已有笔记"
pitfallGuide: "需要同时安装Obsidian和Claude Code，非技术用户可能卡在环境配置上
MCP连接是可选的，第一天可以跳过，不要被复杂配置劝退
CLAUDE.md的访谈环节很重要，跳过会导致代理不理解你的知识组织偏好
项目是纯Markdown文件方案，没有数据库，大量笔记时搜索性能取决于Obsidian本身
仓库语言标注为HTML但实际核心是文档和配置，不要被语言标签误导"
targetAudience: ["独立开发者", "内容创作者", "AI 研究者", "产品经理"]
useCases: ["自动整理收藏的网页和文章为互链wiki", "构建个人研究知识图谱并支持问答检索", "将碎片化阅读笔记自动归档和关联", "用AI代理持续维护Obsidian知识库"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。An AI second brain that maintains itself. Full guide, starter vault, agent skills and scripts for a self-organizing knowledge base in Claude Code and Obsidian.

> GitHub: [undefined-ui/second-brain-os](https://github.com/undefined-ui/second-brain-os) | ⭐ 59 | HTML

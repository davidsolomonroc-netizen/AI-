---
title: "Yowes 教师文档生成器"
description: "通过 MCP 生成 13 国教师证件与信函"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/hirotomasato/yowes"
githubStars: 111
githubOwner: "hirotomasato"
githubRepo: "yowes"
category: "workflow-automation"
tags: ["MCP", "document-generator", "Pillow", "agent"]
editorialScore: 3
deploymentRating: 4
vibeCodingRating: 4
commercialSummary: "Yowes 是一个可通过 AI 助手调用的文档生成工具，能自动产出 13 个国家的教师工作证明、教师证、工资单等文件。适合需要批量制作教育行业文档的机构、HR 团队或做教育类 demo 的开发者。"
vibeCodingPrompt: "1. 克隆仓库并安装依赖：pip install -e .，确认 Python 3.10+。
2. 在 Claude Code 或 Cursor 的 MCP 配置文件中添加 yowes 为 stdio server（参考 README 的 MCP server 章节）。
3. 重启编辑器，确认 MCP 工具列表中已出现 yowes 的文档生成工具。
4. 用自然语言让 AI 调用工具，例如：'生成一份美国教师的雇佣信，姓名 Jane Doe，学校 Lincoln High School'。
5. 检查输出 PNG 目录，验证生成的文档内容、字体和照片是否符合预期。
6. 如需新增国家，参考 README 的 'Adding a new country' 章节扩展模板和数据。"
pitfallGuide: "仅用于演示或内部测试，伪造官方证件在多国属违法，切勿用于真实身份验证场景
MCP 需手动配置到 Claude Code/Cursor，非技术用户可能卡在配置环节
输出为 PNG 图片，若需 PDF 或可编辑格式需自行转换
新增国家需手动补充学校数据库和模板，工作量不小
依赖 DejaVu 字体，特殊字符或本地化排版可能显示异常"
targetAudience: ["独立开发者", "产品经理", "内容创作者"]
useCases: ["教育类 AI Agent 的文档生成能力演示", "教师培训或招聘流程中的示例文档制作", "多国教育系统文档格式对比研究", "MCP 工具集成到 Claude Code 的实战案例"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Generate realistic teacher documents (ID cards, licenses, letters) for 13 countries via MCP.

> GitHub: [hirotomasato/yowes](https://github.com/hirotomasato/yowes) | ⭐ 111 | Python

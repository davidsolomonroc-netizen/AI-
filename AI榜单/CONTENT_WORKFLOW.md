# 内容维护指南

## 如何添加新项目

### 方式一：通过 Decap CMS（推荐，无需写代码）

1. 访问你的网站 `/admin/`（例如 `https://你的域名.pages.dev/admin/`）
2. 使用 GitHub 账号登录
3. 点击 "New Project"（新建项目）
4. 填写表单：
   - 项目名称（中文）
   - 一句话描述
   - 发布日期、GitHub 链接、星数
   - 选择分类和标签
   - 评分（1-5星）
   - 商业价值摘要
   - Vibe Coding 实战 Prompt
   - 避坑指南
   - 详细评测（可选，Markdown 格式）
5. 点击 "Publish"（发布）
6. 等待 1-2 分钟，Cloudflare Pages 会自动重新构建网站

### 方式二：直接在 GitHub 上操作

1. 打开 `github.com/你的用户名/ai-leaderboard`
2. 进入 `src/content/projects/` 目录
3. 点击 "Add file" → "Create new file"
4. 文件名使用英文短横线格式，例如 `my-new-project.md`
5. 复制以下模板并填写：

```markdown
---
title: "项目名称"
description: "一句话描述"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/作者/仓库名"
githubStars: 1000
githubOwner: "作者"
githubRepo: "仓库名"
category: "dev-tools"
tags: ["tag1", "tag2"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 4
commercialSummary: "商业价值摘要，2-3句话说明这个项目能解决什么业务问题"
vibeCodingPrompt: "给 Claude Code 或 Cursor 使用的 Prompt 模板"
pitfallGuide: "避坑要点，每行一条，用数字编号"
---
详细评测内容（Markdown）...
```

6. Commit 到 main 分支，网站会自动重新构建

### 如何更新 GitHub 星数（手动）

- 访问项目的 GitHub 页面获取当前星数
- 修改该项目的 `githubStars` 字段
- 后续可以用脚本自动化（v2 功能）

## 可用分类

| 分类 slug | 中文名 | 说明 |
|-----------|--------|------|
| agent-framework | Agent 框架 | 多 Agent 协作、任务编排 |
| dev-tools | 开发工具 | 开发效率工具 |
| multimodal | 多模态 | 图像、视频、音频工具 |
| code-generation | 代码生成 | 代码自动生成 |
| workflow-automation | 工作流自动化 | 业务流程自动化 |
| data-analysis | 数据分析 | 数据分析工具 |
| other | 其他 | 其他 |

## 评分标准

- **综合评分**：项目整体质量、创新性、社区活跃度（1-5）
- **开箱即用度**：非技术用户能否在 10 分钟内跑通（1-5）
- **Vibe Coding 友好度**：是否适合用 AI 编程工具集成（1-5）

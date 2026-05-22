---
title: "逃课通"
description: "AI分析课表生成逃课方案"
publishDate: 2026-05-22
featured: false
githubUrl: "https://github.com/haoaaa-111/taoketong"
githubStars: 53
githubOwner: "haoaaa-111"
githubRepo: "taoketong"
category: "workflow-automation"
tags: ["agent-skill", "claude-code", "nextjs", "typescript"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这是一个基于AI的课表分析工具，能帮助学生根据课程重要性、教师点名频率等因素智能生成逃课建议。适合大学生、课业规划者以及对时间管理有需求的学生群体使用。"
vibeCodingPrompt: "1. 克隆项目仓库并安装依赖：git clone https://github.com/haoaaa-111/taoketong.git && cd taoketong && npm install
2. 配置环境变量，在 .env.local 中设置 AI API Key（如 OpenAI API Key）
3. 运行开发服务器：npm run dev
4. 在浏览器中打开 http://localhost:3000，上传或输入课表数据（如课程名称、时间、教师、考勤规则）
5. 点击“生成逃课方案”，AI 将分析课表并输出建议（如哪些课可逃、风险等级、替代学习计划）
6. 如需自定义分析逻辑，修改 src/agents/skill.ts 中的 prompt 模板"
pitfallGuide: "1. 部分学校课表格式不统一，需手动调整输入格式
2. AI 建议仅供参考，实际逃课需结合学校考勤政策
3. 依赖外部 AI API，需确保 API Key 有效且有配额
4. 首次部署需安装 Node.js 18+ 和 npm
5. 前端展示可能不兼容老旧浏览器"
targetAudience: ["学生", "创业者", "产品经理", "独立开发者"]
useCases: ["大学生规划每周出勤与自学时间", "课业压力大的学生优化时间分配", "开发者学习AI agent技能与Next.js集成", "教育类产品原型验证与演示"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI课表分析逃课方案生成器

> GitHub: [haoaaa-111/taoketong](https://github.com/haoaaa-111/taoketong) | ⭐ 53 | ["agent-skill",

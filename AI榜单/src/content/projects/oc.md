---
title: "网页精简CLI"
description: "将任意网页转为AI友好的紧凑命令行视图"
publishDate: 2026-08-24
featured: false
githubUrl: "https://github.com/only-cli/oc"
githubStars: 233
githubOwner: "only-cli"
githubRepo: "oc"
category: "dev-tools"
tags: ["web-scraping", "ai-agents", "cli", "browser-automation"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个工具能帮助AI代理（如Claude Code）以极低的token消耗浏览网页，将原本数万token的HTML压缩成几百token的编号列表，大大节省API成本。适合需要频繁抓取网页内容进行数据分析或自动化的个人开发者与企业团队，无需编写复杂的爬虫代码。"
vibeCodingPrompt: "1. 首先安装工具：在终端运行 `npm install -g @only-cli/oc`（需要Node 20+）。\n2. 为Claude Code添加技能：运行 `npx skills add https://github.com/only-cli/oc --skill web-browsing-cli`，并在CLAUDE.md中注明使用`npx @only-cli/oc open <url>`来获取网页内容。\n3. 在Claude Code中直接调用：例如，让Claude分析Hacker News首页，它会自动运行`oc open news.ycombinator.com`，得到紧凑的编号列表，然后通过`oc do <编号>`或`oc read <编号>`深入查看具体条目。\n4. 集成到工作流：编写脚本，循环调用`oc open`和`oc read`来批量抓取多个页面，提取关键信息，用于摘要生成、竞品分析或内容监控。"
pitfallGuide: "需要Node.js 20或更高版本，旧版本无法运行。\n某些网站可能仍会阻止请求，虽然工具模拟浏览器，但复杂验证码可能无法绕过。\n输出是纯文本视图，无法处理动态加载的内容（如无限滚动页面），可能需要多次`next`操作。\n安装技能时需确保网络可访问skills.sh，否则无法添加Claude Code技能。\n对于非技术用户，命令行操作有一定门槛，建议在AI代理环境中使用以获得最佳体验。"
targetAudience: ["独立开发者", "AI研究者", "技术负责人", "数据分析师"]
useCases: ["AI代理网页浏览与信息提取", "低成本网页内容监控与摘要", "批量抓取网页数据用于分析", "集成到Claude Code或Cursor等AI编码工具中"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Turn any website into a compact CLI tailored for AI agents. Browse the web in hundreds of tokens, not tens of thousands.

> GitHub: [only-cli/oc](https://github.com/only-cli/oc) | ⭐ 233 | JavaScript

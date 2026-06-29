---
title: "土豆：AI品牌可见性检测工具"
description: "一键测量品牌在Claude搜索回答中的提及率"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/onism1767-creator/potato"
githubStars: 58
githubOwner: "onism1767-creator"
githubRepo: "potato"
category: "data-analysis"
tags: ["brand-monitoring", "ai-visibility", "claude", "seo"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Potato帮助品牌方和SEO人员了解自己的品牌在Claude AI搜索回答中被提及和引用的频率。它通过固定问题集和确定性评分规则，生成可复现的可见性报告，适合企业品牌团队、AI内容营销人员使用，无需编程基础也可通过Windows一键工具运行。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/onism1767-creator/potato.git\n2. 安装依赖：pip install -r requirements.txt\n3. 设置你的Anthropic API Key：export ANTHROPIC_API_KEY=你的key\n4. 运行CLI：python -m potato --brand \"你的品牌\" --domain \"你的域名\" --category \"类别\"\n5. 查看生成的报告（HTML格式），分析品牌在Claude回答中的提及和引用情况。\n6. 可选：使用--questions参数自定义问题集，或使用--competitors参数添加竞品对比。"
pitfallGuide: "1. 结果仅反映Potato引擎在特定配置下的表现，不代表真实AI可见性全貌\n2. 默认使用免费模板（$0），但AI草拟问题需要自己的API Key\n3. 运行前确保网络稳定，Claude API可能有速率限制\n4. 报告中的置信区间基于确定性规则，非统计置信度\n5. 品牌名称和域名需准确输入，否则可能漏检"
targetAudience: ["企业团队", "内容创作者", "数据分析师", "技术负责人"]
useCases: ["监测品牌在AI搜索中的可见度变化", "对比自家品牌与竞品在Claude回答中的提及率", "评估SEO策略对AI搜索结果的影响", "生成定期品牌可见性报告供团队决策"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Free Easy AI visibility check - measure how often a brand is mentioned & cited in Claude's web-search answers. Deterministic, reproducible, runs 100% locally, $0 mock by default.

> GitHub: [onism1767-creator/potato](https://github.com/onism1767-creator/potato) | ⭐ 58 | Python

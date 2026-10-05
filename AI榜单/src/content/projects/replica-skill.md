---
title: "Replica 克隆技能包"
description: "11 个 Claude 技能，一键逆向并重建任意应用"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/Jakeschincariol/replica-skill"
githubStars: 417
githubOwner: "Jakeschincariol"
githubRepo: "replica-skill"
category: "code-generation"
tags: ["claude-skills", "app-clone", "reverse-engineering", "indie-hacker"]
editorialScore: 4
deploymentRating: 4
vibeCodingRating: 5
commercialSummary: "这是一套让 Claude 自动分析现有 App 的功能与流程，再帮你从零重建一个属于自己版本的技能包，还附带品牌命名、落地页与上线部署。适合想快速验证产品想法的独立开发者和创业者，无需懂代码即可让 AI 完成大部分工作。"
vibeCodingPrompt: "1. 在 Claude Code 中执行 /plugin marketplace add Jakeschincariol/replica-skill 然后 /plugin install replica-skill@replica-skill 安装技能。2. 用 /replica-recon 输入你想克隆的目标 App 链接或截图，让它输出功能清单、数据模型与页面结构。3. 用 /replica-architect 让它规划技术栈、数据库 Schema 和 API。4. 用 /replica-design 重建设计系统，并用 /replica-build 生成前端代码。5. 用 /replica-auth 和 /replica-payments 接入登录与支付。6. 用 /replica-test 自动跑测试找出 bug，再用 /replica-fix 修复。7. 用 /replica-entrepreneur 读取原 App 用户差评，改进你的版本。8. 最后用 /replica-brand 和 /replica-launch 生成品牌、落地页并部署到你的域名。"
pitfallGuide: "克隆仅限功能与流程，不可复制原 App 的代码、Logo、文案或内容，避免侵权。\n需要 Python 3.8+ 环境，但无需 pip 安装任何依赖。\n作为插件安装时命令会带命名空间前缀，如 /replica-skill:replica-recon。\n没有 Claude Code 时可直接把 SKILL.md 粘贴到聊天窗口，但会失去 Python 工具支持。\n重建后的产品需自行验证法律合规性，尤其是涉及用户数据和支付功能。"
targetAudience: ["独立开发者", "创业者", "产品经理"]
useCases: ["快速克隆竞品 App 并添加差异化功能", "为已有产品做功能逆向分析与重构", "独立开发者从零搭建 SaaS 产品原型", "用 AI 自动生成落地页与品牌并上线"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Eleven free Claude skills that clone any app: reverse-engineer it, rebuild it, test it for bugs, then fix what its users hate. Free, MIT.

> GitHub: [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) | ⭐ 417 | Python

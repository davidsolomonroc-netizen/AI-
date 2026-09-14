---
title: "退款 AI 提示词"
description: "用 AI 生成礼貌退款信函与法律升级方案"
publishDate: 2026-09-14
featured: false
githubUrl: "https://github.com/paveldevyatov/refund-anything-ai-prompt"
githubStars: 78
githubOwner: "paveldevyatov"
githubRepo: "refund-anything-ai-prompt"
category: "workflow-automation"
tags: ["refund", "prompt", "consumer-rights", "legal"]
editorialScore: 4
deploymentRating: 5
vibeCodingRating: 4
commercialSummary: "这个项目是一个可直接粘贴到 Claude 或 ChatGPT 的提示词，帮助普通消费者针对订阅、数字购买、预订等场景生成退款申请信，并在被拒后提供法律升级方案。它适合想省律师费、快速拿回钱款的个人用户，尤其是跨境消费或遇到商家拖延的情况。"
vibeCodingPrompt: "1. 克隆或下载 paveldevyatov/refund-anything-ai-prompt 仓库，找到 PROMPT.md 文件。
2. 在 Claude Code 中打开一个项目文件夹，复制 PROMPT.md 的全部内容。
3. 将提示词粘贴到 Claude Code 的对话中，并附上你的收据或订单截图。
4. 按照 AI 的提问回答公司名称、金额、日期、支付方式等信息。
5. 让 AI 生成第一阶段礼貌退款信，并发送到它找到的客服渠道。
6. 如果被拒绝，回到对话中要求生成第二阶段法律升级信，并按照 AI 指示发送。
7. 可选：将整个流程封装成一个简单的本地脚本，用 Claude API 自动读取收据并生成信件。"
pitfallGuide: "提示词需要 AI 能读取附件，确保使用支持图片或 PDF 的模型（如 Claude 3.5 Sonnet、GPT-4o）。
不同司法管辖区的法律差异较大，AI 可能给出不准确的法律建议，重要案件建议咨询律师。
第一阶段务必保持礼貌，直接威胁法律行动可能导致客服转交慢速队列。
退款成功与否取决于商家政策和支付平台，提示词不能保证结果。
如果涉及大额或复杂纠纷，建议先核实 AI 引用的法律条款是否适用于你的所在地。"
targetAudience: ["独立开发者", "内容创作者", "产品经理", "普通消费者"]
useCases: ["取消不想要的订阅并申请退款", "数字产品（如软件、课程）购买后不满意要求退款", "航班、酒店等预订取消后的退款交涉", "被商家拒绝退款后生成法律升级信函"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。AI prompt that gets your money back — subscriptions, digital purchases, bookings. Polite letter first, legal escalation second. 30+ jurisdictions.

> GitHub: [paveldevyatov/refund-anything-ai-prompt](https://github.com/paveldevyatov/refund-anything-ai-prompt) | ⭐ 78 | 多种语言

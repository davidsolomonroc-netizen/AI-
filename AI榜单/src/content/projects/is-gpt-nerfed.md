---
title: "GPT缩水检测器"
description: "检测Codex是否偷偷降级模型的工具"
publishDate: 2026-09-21
featured: false
githubUrl: "https://github.com/kiyoakii/is-gpt-nerfed"
githubStars: 162
githubOwner: "kiyoakii"
githubRepo: "is-gpt-nerfed"
category: "dev-tools"
tags: ["codex", "model-detection", "llm-nerf", "openai"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "当你在 Codex 里选用了某个 GPT 模型时，这个工具能验证实际回答你的到底是不是同一个模型。它适合对 API 成本敏感、担心服务商偷偷降级模型的开发者和 AI 产品团队，帮助避免为高价模型支付却得到低配服务。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/kiyoakii/is-gpt-nerfed && cd is-gpt-nerfed
2. 安装依赖：pip install -r requirements.txt（或按 README 使用 uv/pipx）
3. 运行检测脚本：python -m is_gpt_nerfed --model gpt-4o --session latest
4. 查看输出中的指纹比对结果，确认实际模型是否与请求一致
5. 若需集成到自己的应用，可导入核心检测函数，在每次 API 调用后自动校验模型指纹
6. 设置定时任务（如 cron）定期运行，记录历史降级事件
7. 根据返回的置信度阈值（如 91%）决定是否告警或切换备用模型"
pitfallGuide: "需要 macOS 环境，Windows/Linux 可能无法完整运行
检测依赖 Codex 的本地会话记录，若使用纯 API 调用需自行适配
随机数指纹方法存在误报可能，建议结合多个会话结果综合判断
项目较新，API 可能不稳定，关注 issue 更新
不要用于绕过服务商条款，仅作为质量监控工具"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["监控 Codex 模型是否被降级", "对比不同时间段的模型响应质量", "为 AI 应用选择稳定模型提供数据支持", "自动化测试中验证模型一致性"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Shrinkflation detector for Codex

> GitHub: [kiyoakii/is-gpt-nerfed](https://github.com/kiyoakii/is-gpt-nerfed) | ⭐ 162 | Python

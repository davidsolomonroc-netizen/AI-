---
title: "Ditto - AI代理个性化配置挖掘工具"
description: "从编码会话中提取个性化配置，提升AI代理表现"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/ohad6k/ditto"
githubStars: 145
githubOwner: "ohad6k"
githubRepo: "ditto"
category: "dev-tools"
tags: ["agent-memory", "local-first", "personalization", "developer-tools"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Ditto 通过分析 Claude Code 和 Codex 等编码代理的日志，自动生成个性化配置文件，让AI代理在每次任务前了解你的编码风格和偏好。适合频繁使用AI编码工具的开发者，无需手动维护规则文件即可提升协作效率。"
vibeCodingPrompt: "首先，克隆项目并安装依赖：`git clone https://github.com/ohad6k/ditto.git && cd ditto && pip install -r requirements.txt`。然后，运行 `python main.py` 并指定日志路径（如 `--logs ~/.claude/logs`），选择要提取的会话。最后，将生成的配置文件（如 `you.md`）添加到你的 Claude Code 或 Codex 配置中，让AI代理在启动时自动加载。"
pitfallGuide: "1. 确保日志文件路径正确，否则无法提取数据。\n2. 生成的配置文件可能包含敏感信息，注意保护隐私。\n3. 仅支持特定代理（Claude Code、Codex、Copilot CLI），其他工具需手动适配。\n4. 首次运行可能需要手动选择会话，自动化程度有限。\n5. 配置文件过大可能影响代理启动速度，建议定期清理。"
targetAudience: ["独立开发者", "技术负责人", "AI研究者"]
useCases: ["提升AI编码代理的个性化响应", "自动化提取开发者编码习惯", "跨项目共享编码规范", "优化团队协作中的AI辅助体验"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Mine your Claude Code and Codex logs into a local you.md agent profile.

> GitHub: [ohad6k/ditto](https://github.com/ohad6k/ditto) | ⭐ 145 | Python

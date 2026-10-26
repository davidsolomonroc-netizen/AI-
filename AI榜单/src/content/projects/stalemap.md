---
title: "依赖变更感知器"
description: "让编码代理知道训练截止后依赖库的变更"
publishDate: 2026-10-26
featured: false
githubUrl: "https://github.com/Umair/stalemap"
githubStars: 103
githubOwner: "Umair"
githubRepo: "stalemap"
category: "dev-tools"
tags: ["coding-agents", "dependency-management", "changelog", "mcp"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 5
commercialSummary: "解决 AI 编码代理因训练数据过时而使用旧 API 的问题，自动检测并告知依赖库的破坏性变更。适合使用 Claude Code、Cursor 等 AI 编码工具的开发者，减少调试时间，提升代码准确性。"
vibeCodingPrompt: "1. 在项目根目录运行 `npx stalemap init` 初始化配置。
2. 根据提示选择要监控的依赖（如 AI SDK、zod、Next.js）。
3. 运行 `npx stalemap scan` 生成变更笔记并写入 AGENTS.md 或 CLAUDE.md。
4. 在 Claude Code 中打开项目，代理会自动读取笔记。
5. 编辑代码时，stalemap 会通过 MCP 服务器提供实时类型检查和变更提醒。
6. 运行测试验证功能，确保代理使用正确 API。"
pitfallGuide: "确保项目已安装 Node.js 18+ 和 npm。
首次运行 scan 可能需要网络访问 npm registry 获取 changelog。
MCP 服务器需在 Claude Code 设置中正确配置路径。
变更笔记可能较长，建议定期更新以保持相关性。
对于私有包，需配置 registry 认证信息。"
targetAudience: ["独立开发者", "技术负责人", "企业团队"]
useCases: ["使用 AI 编码代理开发新项目时避免旧 API 错误", "维护长期项目时快速了解依赖升级影响", "团队协作中统一依赖变更知识"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Tell your coding agent which dependencies changed after its training cutoff. Diffs types and changelogs, writes a short block into AGENTS.md / CLAUDE.md.

> GitHub: [Umair/stalemap](https://github.com/Umair/stalemap) | ⭐ 103 | TypeScript

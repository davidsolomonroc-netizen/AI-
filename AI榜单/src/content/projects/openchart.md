---
title: "OpenChart 智能交易工作台"
description: "AI Agent 驱动的开源交易图表工作台"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/longsurf-ai/openchart"
githubStars: 164
githubOwner: "longsurf-ai"
githubRepo: "openchart"
category: "agent-framework"
tags: ["trading", "AI-agents", "charting", "pinescript"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "OpenChart 把 AI 智能体直接嵌入交易图表工作流，让量化交易者用自然语言做技术分析、设置行情告警、发现交易机会。适合独立交易者、量化研究者和想用 AI 辅助投资决策的个人用户，桌面端免费下载，也可自托管。"
vibeCodingPrompt: "1. 克隆仓库：git clone https://github.com/longsurf-ai/openchart 并进入目录。
2. 阅读 docs/development.md，按说明安装依赖（pnpm/npm install）。
3. 配置 LLM API Key（如 OpenAI/Anthropic）到 .env 文件，参考 README 中的 agent 配置部分。
4. 运行开发服务器（npm run dev 或 pnpm dev），打开本地桌面/网页界面。
5. 在图表界面加载一个交易对（如 BTC/USDT），用 Tea 编辑器写一段简单的 PineScript 指标。
6. 在 AI Agent 对话面板中输入：'分析当前 BTC 日线趋势并给出支撑阻力位'，观察 Agent 调用图表数据并返回分析。
7. 基于示例代码，新增一个自定义告警：当 RSI 超过 70 时通过 Agent 推送通知。
8. 用 Claude Code 修改 Agent 的系统提示词，让它输出结构化的交易信号 JSON，并接入你的策略回测脚本。"
pitfallGuide: "需要自备 LLM API Key，否则 AI Agent 功能不可用
首次构建依赖较多，Node 版本建议 20+，否则可能编译失败
实时行情数据源可能需要额外配置 API（如 Binance/Polygon），免费额度有限
PineScript v6 语法与 TradingView 有差异，迁移脚本时需逐行核对
自托管部署涉及前端+后端+数据服务，非技术用户建议直接用桌面版 dmg/exe"
targetAudience: ["独立开发者", "量化研究者", "数据分析师", "技术负责人"]
useCases: ["用 AI Agent 自动生成技术分析报告", "在图表上设置智能告警并让 Agent 解读异动", "编写和回测 PineScript 量化策略", "通过自然语言对话发现交易机会并做多因子研究"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。OSS trading workspace with your favorite agents

> GitHub: [longsurf-ai/openchart](https://github.com/longsurf-ai/openchart) | ⭐ 164 | TypeScript

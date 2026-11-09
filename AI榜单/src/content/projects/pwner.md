---
title: "Pwner 智能渗透测试代理"
description: "对话式AI代理，自动执行网络渗透测试"
publishDate: 2026-11-09
featured: false
githubUrl: "https://github.com/0x45dd/pwner"
githubStars: 82
githubOwner: "0x45dd"
githubRepo: "pwner"
category: "agent-framework"
tags: ["pentest", "ai-agent", "network-security", "cli"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Pwner 是一款通过自然语言对话驱动的自动化网络渗透测试工具，帮助安全团队快速发现网络漏洞。适合企业安全部门、渗透测试服务商和需要定期进行安全评估的IT团队使用。"
vibeCodingPrompt: "1. 安装：pip install pwner
2. 配置LLM：设置环境变量如OPENAI_API_KEY或本地模型端点
3. 启动：运行pwner命令进入交互界面
4. 设置目标：输入要测试的IP或域名范围
5. 发起扫描：用自然语言指令如“对目标进行全端口扫描”
6. 查看结果：代理会执行nmap扫描、服务识别、漏洞检查并报告发现
7. 确认操作：代理在敏感操作（如暴力破解）前会请求许可
8. 生成报告：要求代理汇总所有发现并导出报告"
pitfallGuide: "仅在获得授权的网络中使用，未经授权测试可能违法
确保配置的LLM模型具备足够能力处理安全任务
首次运行需正确设置API密钥或本地模型连接
代理可能误报，需人工验证所有发现
敏感操作（如暴力破解）会请求确认，注意审查"
targetAudience: ["企业团队", "技术负责人", "独立开发者"]
useCases: ["企业内部网络漏洞评估", "渗透测试服务自动化", "PCI DSS合规性分段测试", "安全演练与教学"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Autonomous agentic network penetration-testing tool (authorized use only)

> GitHub: [0x45dd/pwner](https://github.com/0x45dd/pwner) | ⭐ 82 | Python

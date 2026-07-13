---
title: "火箭飞机IO：自托管AI SRE，安全修复K8s集群"
description: "AI驱动的Kubernetes运维助手，零侵入eBPF监控与安全修复"
publishDate: 2026-07-13
featured: false
githubUrl: "https://github.com/olemeyer/rocketplaneIO"
githubStars: 137
githubOwner: "olemeyer"
githubRepo: "rocketplaneIO"
category: "dev-tools"
tags: ["aiops", "kubernetes", "ebpf", "self-hosted"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个项目为Kubernetes集群提供自动化的AI运维体验：通过eBPF无侵入采集指标、日志和追踪，AI助手能自主调查并执行30多种安全修复操作（如扩缩容、回滚配置）。适合需要降低运维门槛、提高故障响应速度的团队，尤其适合自托管和离线环境。"
vibeCodingPrompt: "您好，我想用rocketplaneIO为我的K8s集群搭建一个AI运维助手。请按以下步骤操作：
1. 先确认本地已安装minikube并启动集群，然后克隆项目仓库。
2. 运行一键部署脚本（例如`make deploy`或README中的快速开始命令），将rocketplaneIO的eBPF agent和AI copilot部署到集群。
3. 部署完成后，访问提供的dashboard地址，连接你的集群。
4. 使用Demo应用（如在线商店）生成一些异常流量（如高延迟、错误率上升），观察服务地图自动绘制。
5. 在Copilot界面输入问题，如“检查checkout服务的延迟”，它会自动查询eBPF追踪、日志和PromQL指标，并给出根因分析。
6. 如果建议修复（如扩缩容），确认风险等级后点击执行。
7. 最后，验证修复效果并查看事件日志。"
pitfallGuide: "注意：项目仍处于Alpha阶段，API和Schema会随时变更，请勿用于生产环境。
部署前确保K8s集群满足最低资源要求（至少2核4GB内存）。
eBPF功能依赖Linux内核版本≥4.18，且需要适当权限（如CAP_BPF）。
BYO-LLM需要自行配置大模型API（如OpenAI兼容接口），默认无内置模型。
部分破坏性操作（如scale-to-0、drain节点）需要手动输入目标名称确认，注意不要误操作。"
targetAudience: ["技术负责人", "企业团队", "AI研究者"]
useCases: ["Kubernetes集群日常运维与故障排查", "自托管环境下的AI辅助故障修复", "离线环境中的智能运维", "监控告警自动化响应"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Self-hosted AI SRE for Kubernetes — zero-instrumentation eBPF observability plus a copilot that fixes issues through guardrailed, self-verifying actions. BYO-LLM, air-gapped capable.

> GitHub: [olemeyer/rocketplaneIO](https://github.com/olemeyer/rocketplaneIO) | ⭐ 137 | TypeScript

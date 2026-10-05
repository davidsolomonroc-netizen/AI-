---
title: "PS5LM 主机端大模型"
description: "在越狱 PS5 上原生运行 GGUF 大语言模型"
publishDate: 2026-10-05
featured: false
githubUrl: "https://github.com/cobanov/PS5LM"
githubStars: 69
githubOwner: "cobanov"
githubRepo: "PS5LM"
category: "other"
tags: ["llama-cpp", "ps5", "homebrew", "gguf"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 3
commercialSummary: "PS5LM 让越狱后的 PlayStation 5 主机可以直接下载并运行本地大语言模型，无需云端服务器或额外硬件。适合拥有越狱 PS5 的极客玩家和本地 AI 爱好者，用于离线聊天、隐私敏感场景或纯粹的技术尝鲜。"
vibeCodingPrompt: "目标：在越狱 PS5 上部署 PS5LM 并跑通本地聊天。步骤：1) 确认 PS5 固件在 7.00–13.60 且已越狱，并装有 Payload Manager 或 elfldr（端口 9021）；2) 在 Payload Manager 设置中开启 Multiple Payload Sources，添加源 https://ps5lm.cobanov.dev/payloads.json，安装并加载 PS5LM；3) 或在 GitHub Releases 下载 ps5lm.elf，通过 Payload Manager 上传或发送到 9021 端口加载；4) 加载后 PS5 浏览器打开模型库，点击 Download 下载 Qwen3.5 0.8B（≤1.6GB），再点 Run 和 Open chat；5) 用 DualSense 手柄输入文字测试对话；6) 若要在电脑上访问，打开 http://<PS5 IP>:8082 管理模型，聊天 API 在 8081 端口（兼容 OpenAI 格式），可用 curl 调用验证；7) 也可通过 FTP 将 GGUF 文件放入 /data/PS5LM/models 后刷新库。"
pitfallGuide: "必须使用已越狱且固件在 7.00–13.60 的 PS5，未越狱主机无法运行。
当前 payload 内存限制约 1.6GB，只能跑 0.8B/2B 小模型，大模型会拖垮系统界面。
模型文件需为 GGUF 格式，且放入 /data/PS5LM/models 才会被识别。
网络访问需保证 PS5 与手机/电脑同一局域网，端口 8081/8082 未被占用。
越狱操作有封号或变砖风险，请自行评估，不建议在主力账号主机上折腾。"
targetAudience: ["独立开发者", "AI 研究者", "技术负责人"]
useCases: ["在 PS5 上离线运行本地大模型聊天", "通过 OpenAI 兼容 API 将 PS5 作为局域网推理后端", "测试 GGUF 模型在 Zen 2 CPU 上的性能表现", "作为越狱主机 homebrew 开发与演示平台"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。llama.cpp on a jailbroken PS5: run any GGUF model natively on the console, starting with Qwen 3.8

> GitHub: [cobanov/PS5LM](https://github.com/cobanov/PS5LM) | ⭐ 69 | C++

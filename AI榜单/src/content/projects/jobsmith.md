---
title: "Jobsmith：台灣求職 AI 副駕駛"
description: "多代理自動找職缺、履歷健檢與客製投遞包"
publishDate: 2026-06-29
featured: false
githubUrl: "https://github.com/kevin333353/jobsmith"
githubStars: 103
githubOwner: "kevin333353"
githubRepo: "jobsmith"
category: "agent-framework"
tags: ["job-search", "multi-agent", "langgraph", "local-first"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Jobsmith 是專為台灣求職市場設計的開源多代理 AI 工具，能自動搜尋職缺、評分排序、生成客製履歷、求職信、面試準備與公司情報，並提供模擬面試。適合求職者、人資與 AI 開發者，無需 API key 即可透過本機 Claude Code/Codex CLI 運行，也可自備金鑰接 OpenAI 相容模型。"
vibeCodingPrompt: "請先 clone 此專案並安裝相依套件（Python 3.11+ 與 Node.js），然後執行 `python backend/main.py` 啟動後端，以及 `cd frontend && npm install && npm run dev` 啟動前端。接著上傳 PDF 履歷，選擇 AI 引擎（本機 CLI、Ollama 或 BYOK），即可使用自動找職缺、履歷健檢、生成投遞包與模擬面試等功能。"
pitfallGuide: "1. 預設使用本機 Claude Code/Codex CLI，需先安裝並登入對應 CLI。\n2. 若使用 Ollama 本機模型，需確保模型已下載且 API 可訪問。\n3. 資料以本機保存為主，AI 處理時履歷與 prompt 會傳至所選後端，注意隱私。\n4. Windows 版為單一 exe，首次啟動需解壓約 10-30 秒。\n5. 產生投遞包為背景工作，離開頁面不中斷，但需保持後端運行。"
targetAudience: ["求職者", "AI 研究者", "獨立開發者", "人資專業人員"]
useCases: ["自動搜尋台灣多平台職缺並排序適配度", "一鍵生成客製履歷、求職信與面試準備包", "履歷 ATS 健檢與內容完整度分析", "模擬面試練習與公司情報研究"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。針對台灣求職市場的開源多代理 AI 求職 co-pilot：自動找職缺、履歷健檢、一鍵產生客製投遞包（履歷・求職信・面試準備・公司情報）與模擬面試。本機 Claude Code／Codex CLI 免 API key，也可自備金鑰接 OpenAI 相容模型。

> GitHub: [kevin333353/jobsmith](https://github.com/kevin333353/jobsmith) | ⭐ 103 | Python

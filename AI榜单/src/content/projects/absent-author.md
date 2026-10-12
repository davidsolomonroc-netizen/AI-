---
title: "无主作者检测器"
description: "识别AI全自动生成、无人类署名的科研论文"
publishDate: 2026-10-12
featured: false
githubUrl: "https://github.com/THUROI0787/absent-author"
githubStars: 139
githubOwner: "THUROI0787"
githubRepo: "absent-author"
category: "data-analysis"
tags: ["ai-detection", "research-integrity", "agent-skills", "peer-review"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "该项目提供了一份包含83条证据的清单和两个Agent技能，帮助期刊编辑、审稿人和学术机构快速识别那些由AI全程生成、没有任何人类真正参与署名的论文。适合学术出版机构、科研诚信办公室以及高校审稿委员会使用，能有效降低学术不端风险。"
vibeCodingPrompt: "请用 Claude Code 完成以下步骤：1. 克隆仓库 https://github.com/THUROI0787/absent-author 并阅读 README 和 EVIDENCE.md；2. 在项目根目录下找到 skills 文件夹，将其中两个 agent skill 复制到你的 Claude Code 技能目录；3. 编写一个 Python 脚本，调用这些技能，输入一篇论文的 PDF 或文本，输出一个包含83条证据项打分的 JSON 报告；4. 使用 tools/calibration 中的校准报告验证输出是否与79篇已标注论文一致；5. 最后用 Streamlit 做一个简单的网页界面，让用户上传论文后一键生成检测报告。"
pitfallGuide: "需具备基本的 Python 和命令行操作能力，非技术用户可能需他人协助。\n检测结果仅供参考，不能作为学术不端的唯一证据，需人工复核。\nAgent 技能依赖 Claude Code 或 Codex 环境，需提前配置 API 密钥。\n项目针对英文论文校准，中文论文效果可能下降。\n部分证据项涉及隐私或版权内容，使用时需遵守学术伦理。"
targetAudience: ["AI 研究者", "企业团队", "技术负责人", "内容创作者"]
useCases: ["期刊编辑部批量筛查投稿论文", "高校科研诚信办公室调查可疑论文", "学术会议审稿人辅助判断", "研究机构内部自查AI代写风险"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Research and writing can be automated. Authorship cannot. Evidence list + agent skills for spotting AI-produced papers no human stood behind.

> GitHub: [THUROI0787/absent-author](https://github.com/THUROI0787/absent-author) | ⭐ 139 | Python

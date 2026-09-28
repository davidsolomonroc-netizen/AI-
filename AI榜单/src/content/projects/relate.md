---
title: "Relate 私人AI幕僚长"
description: "自托管聊天记忆助手，记住承诺与重要日子"
publishDate: 2026-09-28
featured: false
githubUrl: "https://github.com/georgeding/Relate"
githubStars: 117
githubOwner: "georgeding"
githubRepo: "Relate"
category: "workflow-automation"
tags: ["memory", "self-hosted", "telegram", "mcp"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "Relate 是一个跑在你自己电脑上的私人 AI 助手，能自动读取你的聊天记录，帮你记住对方说过的重要事情、你答应过却可能忘记的承诺，以及各种纪念日。它不会把你的聊天内容上传到云端，所有数据都留在本地。适合需要维护重要人际关系、客户关系或团队协作的独立工作者、销售和创业者使用。"
vibeCodingPrompt: "1. 克隆项目：git clone https://github.com/georgeding/Relate && cd Relate，运行 npm install 和 npm start 启动本地服务（默认 http://127.0.0.1:5080/hub/）。
2. 首次打开会要求设置密码，设置完成后进入「设置 → AI 服务商」，粘贴 OpenAI 兼容的 API Key（也支持 Ollama 本地模型），点击「测试」确认连通。
3. 在 Telegram 上用 @BotFather 创建一个机器人，拿到 token，粘贴到 Relate 的 Telegram 连接器里，并把机器人拉进你想监控的群聊或私聊。
4. 点击「新建空间」，选择「亲密关系」或「生意」模板，连接刚配置好的 Telegram，点击「启动」，系统会自动开始读取历史消息并提取承诺、待办和重要日期。
5. 打开控制台查看仪表盘，尝试提问「我们周六说好了什么？」，验证记忆与出处功能；再让 AI 代拟一条回复，确认发送前需要你手动确认。
6. 如需接入 WhatsApp/Slack 等，参考 docs/INGEST.md 写一个 HTTP 桥接服务推送消息即可。"
pitfallGuide: "Windows 用户直接下载 RelateSetup.exe 最省事，源码运行需 Node.js 22+，版本过低会启动失败。
API Key 和 Telegram token 属于敏感信息，务必只保存在本机，不要提交到 Git 仓库。
微信连接器仅在 Windows 下可用且存在账号风险，使用前请仔细阅读 docs/CONNECTORS-AND-RISK.md。
所有消息发送都需要你手动确认，AI 不会自动回复，别期待全自动代聊。
数据默认存于 %APPDATA%\Relate（Windows）或用户目录，迁移或备份时记得复制该目录，否则升级后可能丢失记忆。"
targetAudience: ["独立开发者", "创业者", "产品经理", "内容创作者"]
useCases: ["维护重要客户关系，自动追踪未回复消息和承诺事项", "亲密关系助手，记住伴侣的喜好、敏感话题和纪念日", "团队协作看板，提取会议承诺和无人认领的任务", "个人知识管理，基于完整聊天记录做可溯源问答"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。记得她说过的每一句话，也记得你答应过的每一件事。A self-hosted AI chief of staff for your chats — remembers what they said and what you promised.

> GitHub: [georgeding/Relate](https://github.com/georgeding/Relate) | ⭐ 117 | JavaScript

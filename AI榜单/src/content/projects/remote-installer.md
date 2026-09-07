---
title: "远程安装器"
description: "通过链接或二维码快速安装iOS/Android构建到真机"
publishDate: 2026-09-07
featured: false
githubUrl: "https://github.com/icodesign/remote-installer"
githubStars: 95
githubOwner: "icodesign"
githubRepo: "remote-installer"
category: "dev-tools"
tags: ["iOS", "Android", "tunnel", "vibecoding"]
editorialScore: 4
deploymentRating: 3
vibeCodingRating: 4
commercialSummary: "这个工具让开发者或AI代理能瞬间把签名好的App安装包分发给真机，无需等待TestFlight或Google Play审核。适合远程开发、内部测试或向客户快速演示，只要手机已包含在配置文件中，扫描二维码即可安装。"
vibeCodingPrompt: "在Claude Code中，你可以这样使用：
1. 确保已安装并配置至少一个隧道提供商（如Cloudflare Quick Tunnel）。
2. 运行`remote-installer share ./MyApp.ipa`命令，它会自动验证构建文件并启动临时HTTPS链接。
3. 复制输出的二维码或链接，通过聊天工具发送给测试人员，他们用手机相机扫描即可安装。
4. 如需限制下载次数或设置过期时间，可查看`--expiry`和`--max-downloads`选项。
5. 生成链接后，可让Claude Code自动执行安装验证（如检查HTTP状态码）。"
pitfallGuide: "iOS构建必须使用开发或ad hoc签名，且目标设备已加入配置文件，否则安装失败。\nAndroid仅支持签名独立的APK，不支持AAB或split APK，需提前转换。\n确保隧道服务（Cloudflare/Tailscale）已正确安装并运行，否则无法生成公网链接。\n分享结束时链接自动失效，需重新生成，适合临时分发而非长期托管。\n不要用于分发模拟器或App Store构建，这些无法直接安装。"
targetAudience: ["独立开发者", "创业者", "技术负责人", "AI研究者"]
useCases: ["远程给客户或团队分发测试版App", "AI代理自动构建后快速推送安装包到真机", "内部工具或原型在无应用商店流程下的快速部署", "跨地域协作时避免上传到第三方存储"]
---
## 🤖 自动发现

本项目由 AI 榜单自动发现系统收录。Quickly install signed iOS and Android builds on real devices over the internet without waiting for Testlight or Play Beta.

> GitHub: [icodesign/remote-installer](https://github.com/icodesign/remote-installer) | ⭐ 95 | Rust

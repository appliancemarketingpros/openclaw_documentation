---
title: 新手引导（macOS 应用）
source_url: https://docs.openclaw.ai/zh-CN/start/onboarding
scraped_at: 2026-05-25
---

本文档描述了**当前** 首次运行设置流程。目标是提供顺畅的“第 0 天”体验：选择 Gateway 网关运行位置、连接凭证、运行向导，并让智能体完成自举。 有关新手引导路径的总体概览，请参阅[新手引导概览](</zh-CN/start/onboarding-overview>)。

* ### 批准 macOS 警告

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### 批准查找本地网络

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### 欢迎和安全提示

阅读显示的安全提示并据此决定 ![](/assets/macos-onboarding/03-security-notice.png)

安全信任模型：

  * 默认情况下，OpenClaw 是个人智能体：单个受信任操作者边界。
  * 共享/多用户设置需要锁定（拆分信任边界、尽量减少工具访问权限，并遵循[安全](</zh-CN/gateway/security>)）。
  * 本地新手引导现在会将新配置默认设为 `tools.profile: "coding"`，因此新的本地设置会保留文件系统/运行时工具，而无需强制使用无限制的 `full` 配置文件。
  * 如果启用了钩子/webhook 或其他不受信任的内容源，请使用强大的现代模型档位，并保持严格的工具策略/沙箱隔离。


* ### 本地与远程

![](/assets/macos-onboarding/04-choose-gateway.png)

**Gateway 网关** 在哪里运行？

  * **这台 Mac（仅本地）：** 新手引导可以在本地配置凭证并写入凭证。
  * **远程（通过 SSH/Tailnet）：** 新手引导**不会** 配置本地凭证；凭证必须已存在于 Gateway 网关主机上。
  * **稍后配置：** 跳过设置，并让应用保持未配置状态。


* ### 权限

选择你要授予 OpenClaw 的权限 ![](/assets/macos-onboarding/05-permissions.png)

新手引导会请求以下所需的 TCC 权限：

  * 自动化（AppleScript）
  * 通知
  * 辅助功能
  * 屏幕录制
  * 麦克风
  * 语音识别
  * 摄像头
  * 位置


* ### CLI

* ### 新手引导聊天（专用会话）

设置完成后，应用会打开一个专用的新手引导聊天会话，让智能体可以 介绍自己并指导后续步骤。这会将首次运行指导与你的常规对话分开。 有关首次智能体运行期间 Gateway 网关主机上发生的事情，请参阅[自举](</zh-CN/start/bootstrapping>)。

## 相关

  * [新手引导概览](</zh-CN/start/onboarding-overview>)
  * [入门指南](</zh-CN/start/getting-started>)


Was this useful?YesNo
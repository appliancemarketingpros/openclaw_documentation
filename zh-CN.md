---
title: OpenClaw
source_url: https://docs.openclaw.ai/zh-CN
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _“脱壳！脱壳！”_ — 大概是一只太空龙虾

**适用于任意操作系统的 AI 智能体 Gateway 网关，可跨 Discord、Google Chat、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo 等使用。**

发送一条消息，就能从口袋里收到智能体回复。在内置渠道、捆绑渠道插件、WebChat 和移动节点之间运行一个 Gateway 网关。

[**开始使用** 安装 OpenClaw，并在几分钟内启动 Gateway 网关。 ](</zh-CN/start/getting-started>) [**运行新手引导** 使用 `openclaw onboard` 和配对流程完成引导式设置。 ](</zh-CN/start/wizard>) [**打开控制 UI** 启动用于聊天、配置和会话的浏览器仪表板。 ](</zh-CN/web/control-ui>)

## 什么是 OpenClaw？

OpenClaw 是一个**自托管 Gateway 网关** ，它把你常用的聊天应用和渠道界面（包括内置渠道，以及 Discord、Google Chat、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo 等捆绑或外部渠道插件）连接到 Pi 等 AI 编码智能体。你在自己的机器（或服务器）上运行单个 Gateway 网关进程，它就会成为你的消息应用和始终可用的 AI 助手之间的桥梁。

**适合谁使用？** 适合希望拥有可从任何地方发消息调用的个人 AI 助手，同时又不想放弃数据控制权或依赖托管服务的开发者和高级用户。

**它有什么不同？**

  * **自托管** ：在你的硬件上运行，遵循你的规则
  * **多渠道** ：一个 Gateway 网关可同时服务内置渠道以及捆绑或外部渠道插件
  * **智能体原生** ：为具备工具使用、会话、记忆和多智能体路由能力的编码智能体而构建
  * **开源** ：MIT 许可，社区驱动


**你需要什么？** Node 24（推荐），或用于兼容性的 Node 22 LTS (`22.16+`)，所选提供商的 API key，以及 5 分钟。为获得最佳质量和安全性，请使用可用的最强最新一代模型。

## 工作原理
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway 网关是会话、路由和渠道连接的单一事实来源。

## 核心能力

[**多渠道 Gateway 网关** 通过单个 Gateway 网关进程使用 Discord、iMessage、Signal、Slack、Telegram、WhatsApp、WebChat 等。 ](</zh-CN/channels>) [**插件渠道** 捆绑插件会在常规当前版本中添加 Matrix、Nostr、Twitch、Zalo 等。 ](</zh-CN/tools/plugin>) [**多智能体路由** 按智能体、工作区或发送者隔离会话。 ](</zh-CN/concepts/multi-agent>) [**媒体支持** 发送和接收图像、音频和文档。 ](</zh-CN/nodes/images>) [**Web 控制 UI** 用于聊天、配置、会话和节点的浏览器仪表板。 ](</zh-CN/web/control-ui>) [**移动节点** 配对 iOS 和 Android 节点，用于 Canvas、相机和支持语音的工作流。 ](</zh-CN/nodes>)

## 快速开始

* ### 安装 OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### 新手引导并安装服务

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### 聊天

在浏览器中打开控制 UI 并发送消息：

bashCopy code
[code]
    openclaw dashboard
[/code]

或者连接一个渠道（[Telegram](</zh-CN/channels/telegram>) 最快），然后从手机聊天。

需要完整安装和开发设置？请参阅[入门指南](</zh-CN/start/getting-started>)。

## 仪表板

Gateway 网关启动后，打开浏览器控制 UI。

  * 本地默认值：<http://127.0.0.1:18789/>
  * 远程访问：[Web 界面](</zh-CN/web>)和 [Tailscale](</zh-CN/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## 配置（可选）

配置位于 `~/.openclaw/openclaw.json`。

  * 如果你**什么都不做** ，OpenClaw 会在 RPC 模式下使用捆绑的 Pi 二进制文件，并为每个发送者使用独立会话。
  * 如果你想锁定访问范围，请从 `channels.whatsapp.allowFrom` 和（用于群组的）提及规则开始。


示例：

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## 从这里开始

[**文档中心** 按用例组织的所有文档和指南。 ](</zh-CN/start/hubs>) [**配置** 核心 Gateway 网关设置、令牌和提供商配置。 ](</zh-CN/gateway/configuration>) [**远程访问** SSH 和 tailnet 访问模式。 ](</zh-CN/gateway/remote>) [**渠道** Feishu、Microsoft Teams、WhatsApp、Telegram、Discord 等的渠道专属设置。 ](</zh-CN/channels/telegram>) [**节点** 带配对、Canvas、相机和设备操作的 iOS 与 Android 节点。 ](</zh-CN/nodes>) [**帮助** 常见修复和故障排除入口点。 ](</zh-CN/help>)

## 了解更多

[**完整功能列表** 完整的渠道、路由和媒体能力。 ](</zh-CN/concepts/features>) [**多智能体路由** 工作区隔离和按智能体划分的会话。 ](</zh-CN/concepts/multi-agent>) [**安全** 令牌、允许列表和安全控制。 ](</zh-CN/gateway/security>) [**故障排除** Gateway 网关诊断和常见错误。 ](</zh-CN/gateway/troubleshooting>) [**关于与致谢** 项目起源、贡献者和许可。 ](</zh-CN/reference/credits>)

Was this useful?YesNo
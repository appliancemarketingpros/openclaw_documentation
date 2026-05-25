---
title: 功能
source_url: https://docs.openclaw.ai/zh-CN/concepts/features
scraped_at: 2026-05-25
---

## 亮点

[**渠道** Discord、iMessage、Signal、Slack、Telegram、WhatsApp、WebChat 等渠道，只需一个 Gateway 网关。 ](</zh-CN/channels>) [**插件** 在正常的当前版本中，内置插件无需单独安装即可添加 Matrix、Nextcloud Talk、Nostr、Twitch、Zalo 等。 ](</zh-CN/tools/plugin>) [**路由** 具有隔离会话的多 Agent 路由。 ](</zh-CN/concepts/multi-agent>) [**媒体** 图片、音频、视频、文档，以及图片/视频生成。 ](</zh-CN/nodes/images>) [**应用和 UI** Web 控制 UI 和 macOS 配套应用。 ](</zh-CN/web/control-ui>) [**移动节点** 支持配对、语音/聊天和丰富设备命令的 iOS 与 Android 节点。 ](</zh-CN/nodes>)

## 完整列表

**渠道：**

  * 内置渠道包括 Discord、Google Chat、iMessage、IRC、Signal、Slack、Telegram、WebChat 和 WhatsApp
  * 内置插件渠道包括 Feishu、LINE、Matrix、Mattermost、Microsoft Teams、Nextcloud Talk、Nostr、QQ Bot、Synology Chat、Tlon、Twitch、Zalo 和 Zalo Personal
  * 可选的单独安装渠道插件包括 Voice Call，以及 WeChat 等第三方包
  * 第三方渠道插件可以进一步扩展 Gateway 网关，例如 WeChat
  * 支持基于提及激活的群聊
  * 通过允许列表和配对保障私信安全


**Agent：**

  * 带工具流式传输的嵌入式 Agent 运行时
  * 按工作区或发送者提供隔离会话的多 Agent 路由
  * 会话：直接聊天会合并到共享的 `main`；群组会被隔离
  * 针对长回复的流式传输和分块


**认证和提供商：**

  * 35+ 个模型提供商（Anthropic、OpenAI、Google 等）
  * 通过 OAuth 进行订阅认证（例如 OpenAI Codex）
  * 支持自定义和自托管提供商（vLLM、SGLang、Ollama，以及任何兼容 OpenAI 或兼容 Anthropic 的端点）


**媒体：**

  * 图片、音频、视频和文档的输入与输出
  * 共享的图片生成和视频生成能力表面
  * 语音消息转录
  * 支持多个提供商的文本转语音


**应用和界面：**

  * WebChat 和浏览器控制 UI
  * macOS 菜单栏配套应用
  * 支持配对、Canvas、摄像头、屏幕录制、位置和语音的 iOS 节点
  * 支持配对、聊天、语音、Canvas、摄像头和设备命令的 Android 节点


**工具和自动化：**

  * 浏览器自动化、exec、沙箱隔离
  * Web 搜索（Brave、DuckDuckGo、Exa、Firecrawl、Gemini、Grok、Kimi、MiniMax Search、Ollama Web 搜索、Perplexity、SearXNG、Tavily）
  * Cron 任务和 Heartbeat 调度
  * Skills、插件和工作流流水线（Lobster）


## 相关内容

[**实验性功能** 尚未交付到默认表面的选择加入功能。 ](</zh-CN/concepts/experimental-features>) [**Agent 运行时** Agent 运行时模型，以及运行如何被分派。 ](</zh-CN/concepts/agent>) [**渠道** 从一个 Gateway 网关连接 Telegram、WhatsApp、Discord、Slack 等。 ](</zh-CN/channels>) [**插件** 扩展 OpenClaw 的内置和第三方插件。 ](</zh-CN/tools/plugin>)

Was this useful?YesNo
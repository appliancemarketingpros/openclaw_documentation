---
title: 机器人循环保护
source_url: https://docs.openclaw.ai/zh-CN/channels/bot-loop-protection
scraped_at: 2026-06-29
---

快速开始

# 机器人循环保护

OpenClaw 可以在支持 `allowBots` 的渠道上接收其他机器人写入的消息。 启用该路径后，成对循环保护会防止两个机器人身份无限互相回复。

该保护由核心入站回复运行器执行。每个支持的渠道都会把自己的入站事件映射为通用事实：账号或作用域、会话 ID、发送方机器人 ID 和接收方机器人 ID。随后，核心会双向跟踪这对参与者，应用滑动窗口配额，并在配额超出后的冷却期内抑制这对参与者。

## 默认值

当某个渠道允许机器人编写的消息进入分发时，成对循环保护会处于启用状态。内置默认值如下：

  * `maxEventsPerWindow: 20` \- 一对机器人可以在窗口内交换 20 个事件
  * `windowSeconds: 60` \- 滑动窗口长度
  * `cooldownSeconds: 60` \- 这对机器人超出配额后的抑制时间


该保护不会影响普通人类编写的消息、单机器人部署、自消息过滤，或保持在配额以内的一次性机器人回复。

## 配置共享默认值

设置一次 `channels.defaults.botLoopProtection`，为每个支持的渠道提供相同基线。渠道和账号覆盖项仍然可以调整各个表面。

json5Copy code
[code]
    {  channels: {    defaults: {      botLoopProtection: {        maxEventsPerWindow: 20,        windowSeconds: 60,        cooldownSeconds: 60,      },    },  },}
[/code]

仅当你的渠道策略有意允许机器人到机器人对话且不进行自动抑制时，才设置 `enabled: false`。

## 按渠道或账号覆盖

支持的渠道会在共享默认值之上叠加自己的配置。优先级如下：

  * `channels.<channel>.<room-or-space>.botLoopProtection`，当渠道支持按会话覆盖时
  * `channels.<channel>.accounts.<account>.botLoopProtection`，当渠道支持账号时
  * `channels.<channel>.botLoopProtection`，当渠道支持顶层默认值时
  * `channels.defaults.botLoopProtection`
  * 内置默认值

json5Copy code
[code]
    {  channels: {    defaults: {      botLoopProtection: {        maxEventsPerWindow: 20,      },    },    discord: {      botLoopProtection: {        maxEventsPerWindow: 8,      },      accounts: {        molty: {          allowBots: "mentions",          botLoopProtection: {            maxEventsPerWindow: 5,            cooldownSeconds: 90,          },        },      },    },    slack: {      allowBots: "mentions",      botLoopProtection: {        maxEventsPerWindow: 8,      },    },    matrix: {      allowBots: "mentions",      groups: {        "!roomid:example.org": {          botLoopProtection: {            maxEventsPerWindow: 5,          },        },      },    },    googlechat: {      allowBots: true,      groups: {        "spaces/AAAA": {          botLoopProtection: {            maxEventsPerWindow: 5,          },        },      },    },  },}
[/code]

## 渠道支持

  * Discord：原生 `author.bot` 事实，按 Discord 账号、渠道和机器人对键控。
  * Slack：已接收机器人编写消息的原生 `bot_id` 事实，按 Slack 账号、渠道和机器人对键控。
  * Matrix：已配置的 Matrix 机器人账号，按 Matrix 账号、房间和已配置机器人对键控。
  * Google Chat：已接收机器人编写消息的原生 `sender.type=BOT` 事实，按账号、空间和机器人对键控。


未暴露可靠入站机器人身份的渠道会继续使用其正常的自消息和访问策略过滤器。在能够识别机器人对中的两个参与者之前，它们不应选择加入此保护。

有关插件实现细节，请参阅 [SDK 运行时](</zh-CN/plugins/sdk-runtime#reusable-runtime-utilities>)。

Was this useful?YesNo

Open issue
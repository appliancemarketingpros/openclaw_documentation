---
title: IRC
source_url: https://docs.openclaw.ai/zh-CN/channels/irc
scraped_at: 2026-05-25
---

在你希望通过经典渠道（`#room`）和私信使用 OpenClaw 时，请使用 IRC。 IRC 作为内置插件提供，但它在主配置的 `channels.irc` 下配置。

## 快速开始

  1. 在 `~/.openclaw/openclaw.json` 中启用 IRC 配置。
  2. 至少设置：

json5Copy code
[code]
    {  channels: {    irc: {      enabled: true,      host: "irc.example.com",      port: 6697,      tls: true,      nick: "openclaw-bot",      channels: ["#openclaw"],    },  },}
[/code]

建议使用私有 IRC 服务器进行机器人协作。如果你有意使用公共 IRC 网络，常见选择包括 Libera.Chat、OFTC 和 Snoonet。避免为机器人或集群后通信流量使用可预测的公共渠道。

  3. 启动/重启 Gateway 网关：

bashCopy code
[code]
    openclaw gateway run
[/code]

## 安全默认值

  * IRC 使用 OpenClaw 操作员管理的转发代理路由之外的原始 TCP/TLS 套接字。在要求所有出站流量都经过该转发代理的部署中，除非明确批准直接 IRC 出站，否则请设置 `channels.irc.enabled=false`。
  * `channels.irc.dmPolicy` 默认值为 `"pairing"`。
  * `channels.irc.groupPolicy` 默认值为 `"allowlist"`。
  * 使用 `groupPolicy="allowlist"` 时，设置 `channels.irc.groups` 来定义允许的渠道。
  * 除非你有意接受明文传输，否则请使用 TLS（`channels.irc.tls=true`）。


## 访问控制

IRC 渠道有两个独立的“门控”：

  1. **渠道访问** （`groupPolicy` \+ `groups`）：机器人是否完全接受来自某个渠道的消息。
  2. **发送者访问** （`groupAllowFrom` / 每渠道 `groups["#channel"].allowFrom`）：允许谁在该渠道内触发机器人。


配置键：

  * 私信 allowlist（私信发送者访问）：`channels.irc.allowFrom`
  * 群组发送者 allowlist（渠道发送者访问）：`channels.irc.groupAllowFrom`
  * 每渠道控制（渠道 + 发送者 + 提及规则）：`channels.irc.groups["#channel"]`
  * `channels.irc.groupPolicy="open"` 允许未配置的渠道（**默认仍受提及门控** ）


Allowlist 条目应使用稳定的发送者身份（`nick!user@host`）。 裸昵称匹配是可变的，并且仅在 `channels.irc.dangerouslyAllowNameMatching: true` 时启用。

### 常见陷阱：`allowFrom` 用于私信，而不是渠道

如果你看到如下日志：

  * `irc: drop group sender alice!ident@host (policy=allowlist)`


……这表示该发送者不允许发送**群组/渠道** 消息。可通过以下任一方式修复：

  * 设置 `channels.irc.groupAllowFrom`（对所有渠道全局生效），或
  * 设置每渠道发送者 allowlist：`channels.irc.groups["#channel"].allowFrom`


示例（允许 `#tuirc-dev` 中的任何人与机器人对话）：

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": { allowFrom: ["*"] },      },    },  },}
[/code]

## 回复触发（提及）

即使某个渠道已允许（通过 `groupPolicy` \+ `groups`），且发送者也已允许，OpenClaw 在群组上下文中默认仍会进行**提及门控** 。

这意味着你可能会看到类似 `drop channel … (missing-mention)` 的日志，除非消息包含与机器人匹配的提及模式。

要让机器人在 IRC 渠道中**无需提及即可回复** ，请为该渠道禁用提及门控：

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": {          requireMention: false,          allowFrom: ["*"],        },      },    },  },}
[/code]

或者允许**所有** IRC 渠道（无每渠道 allowlist），同时仍无需提及即可回复：

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "open",      groups: {        "*": { requireMention: false, allowFrom: ["*"] },      },    },  },}
[/code]

## 安全说明（公共渠道推荐）

如果你在公共渠道中允许 `allowFrom: ["*"]`，任何人都可以向机器人发送提示。 为降低风险，请限制该渠道可用的工具。

### 渠道中所有人使用相同工具

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          tools: {            deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],          },        },      },    },  },}
[/code]

### 每个发送者使用不同工具（所有者获得更多权限）

使用 `toolsBySender` 对 `"*"` 应用更严格的策略，并对你的昵称应用更宽松的策略：

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          toolsBySender: {            "*": {              deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],            },            "id:eigen": {              deny: ["gateway", "nodes", "cron"],            },          },        },      },    },  },}
[/code]

注意：

  * `toolsBySender` 键应对 IRC 发送者身份值使用 `id:`： `id:eigen`，或使用 `id:eigen!~eigen@174.127.248.171` 进行更强匹配。
  * 旧版未加前缀的键仍会被接受，并且仅按 `id:` 匹配。
  * 第一个匹配的发送者策略生效；`"*"` 是通配符回退。


有关群组访问与提及门控（以及它们如何相互作用）的更多信息，请参阅：[/channels/groups](</zh-CN/channels/groups>)。

## NickServ

要在连接后向 NickServ 进行身份识别：

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        enabled: true,        service: "NickServ",        password: "your-nickserv-password",      },    },  },}
[/code]

连接时可选的一次性注册：

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        register: true,        registerEmail: "bot@example.com",      },    },  },}
[/code]

昵称注册完成后请禁用 `register`，以避免重复尝试 REGISTER。

## 环境变量

默认账号支持：

  * `IRC_HOST`
  * `IRC_PORT`
  * `IRC_TLS`
  * `IRC_NICK`
  * `IRC_USERNAME`
  * `IRC_REALNAME`
  * `IRC_PASSWORD`
  * `IRC_CHANNELS`（逗号分隔）
  * `IRC_NICKSERV_PASSWORD`
  * `IRC_NICKSERV_REGISTER_EMAIL`


`IRC_HOST` 不能从工作区 `.env` 设置；请参阅 [工作区 `.env` 文件](</zh-CN/gateway/security>)。

## 故障排除

  * 如果机器人已连接但从不在渠道中回复，请检查 `channels.irc.groups` **以及** 提及门控是否正在丢弃消息（`missing-mention`）。如果你希望它无需 ping 即可回复，请为该渠道设置 `requireMention:false`。
  * 如果登录失败，请检查昵称可用性和服务器密码。
  * 如果 TLS 在自定义网络上失败，请检查主机/端口和证书设置。


## 相关内容

  * [渠道概览](</zh-CN/channels>) — 所有支持的渠道
  * [配对](</zh-CN/channels/pairing>) — 私信身份验证和配对流程
  * [群组](</zh-CN/channels/groups>) — 群聊行为和提及门控
  * [渠道路由](</zh-CN/channels/channel-routing>) — 消息的会话路由
  * [安全](</zh-CN/gateway/security>) — 访问模型和加固


Was this useful?YesNo
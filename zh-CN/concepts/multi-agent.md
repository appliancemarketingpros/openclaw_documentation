---
title: 多智能体路由
source_url: https://docs.openclaw.ai/zh-CN/concepts/multi-agent
scraped_at: 2026-05-25
---

运行多个_隔离_智能体，每个智能体都有自己的工作区、状态目录（`agentDir`）和会话历史，同时在一个运行中的 Gateway 网关中运行多个渠道账号（例如两个 WhatsApp）。入站消息通过绑定路由到正确的智能体。

这里的**智能体** 是完整的按人格划分的作用域：工作区文件、凭证配置、模型注册表和会话存储。`agentDir` 是磁盘上的状态目录，用于在 `~/.openclaw/agents/<agentId>/` 保存这个按智能体划分的配置。**绑定** 会把一个渠道账号（例如 Slack 工作区或 WhatsApp 号码）映射到其中一个智能体。

## 什么是“一个智能体”？

**智能体** 是一个完整划定作用域的大脑，拥有自己的：

  * **工作区** （文件、[AGENTS.md/SOUL.md/USER.md、本地笔记、人格规则）。](<http://AGENTS.md/SOUL.md/USER.md%E3%80%81%E6%9C%AC%E5%9C%B0%E7%AC%94%E8%AE%B0%E3%80%81%E4%BA%BA%E6%A0%BC%E8%A7%84%E5%88%99%EF%BC%89%E3%80%82>)
  * **状态目录** （`agentDir`），用于凭证配置、模型注册表和按智能体划分的配置。
  * **会话存储** （聊天历史 + 路由状态），位于 `~/.openclaw/agents/<agentId>/sessions` 下。


凭证配置是**按智能体划分** 的。每个智能体都会从自己的以下位置读取：

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

Skills 会从每个智能体工作区以及 `~/.openclaw/skills` 等共享根目录加载，然后在配置了有效的智能体技能允许列表时进行过滤。使用 `agents.defaults.skills` 设置共享基线，使用 `agents.list[].skills` 设置按智能体替换。参见 [Skills：按智能体 vs 共享](</zh-CN/tools/skills#per-agent-vs-shared-skills>) 和 [Skills：智能体技能允许列表](</zh-CN/tools/skills#agent-skill-allowlists>)。

Gateway 网关可以托管**一个智能体** （默认）或**多个智能体** 并排运行。

## 路径（速查）

  * 配置：`~/.openclaw/openclaw.json`（或 `OPENCLAW_CONFIG_PATH`）
  * 状态目录：`~/.openclaw`（或 `OPENCLAW_STATE_DIR`）
  * 工作区：`~/.openclaw/workspace`（或 `~/.openclaw/workspace-<agentId>`）
  * 智能体目录：`~/.openclaw/agents/<agentId>/agent`（或 `agents.list[].agentDir`）
  * 会话：`~/.openclaw/agents/<agentId>/sessions`


### 单智能体模式（默认）

如果你什么都不做，OpenClaw 会运行单个智能体：

  * `agentId` 默认为 **`main`** 。
  * 会话键为 `agent:main:<mainKey>`。
  * 工作区默认为 `~/.openclaw/workspace`（设置 `OPENCLAW_PROFILE` 时为 `~/.openclaw/workspace-<profile>`）。
  * 状态默认为 `~/.openclaw/agents/main/agent`。


## 智能体助手

使用智能体向导添加新的隔离智能体：

bashCopy code
[code]
    openclaw agents add work
[/code]

然后添加 `bindings`（或让向导来做）以路由入站消息。

使用以下命令验证：

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## 快速开始

* ### 创建每个智能体工作区

使用向导，或手动创建工作区：

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

每个智能体都会获得自己的工作区，其中包含 `SOUL.md`、`AGENTS.md` 和可选的 `USER.md`，并且在 `~/.openclaw/agents/<agentId>` 下拥有专用的 `agentDir` 和会话存储。

* ### 创建渠道账号

在你偏好的渠道上为每个智能体创建一个账号：

  * Discord：每个智能体一个机器人，启用 Message Content Intent，复制每个令牌。
  * Telegram：通过 BotFather 为每个智能体创建一个机器人，复制每个令牌。
  * WhatsApp：为每个账号关联一个电话号码。

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

参见渠道指南：[Discord](</zh-CN/channels/discord>)、[Telegram](</zh-CN/channels/telegram>)、[WhatsApp](</zh-CN/channels/whatsapp>)。

* ### 添加智能体、账号和绑定

在 `agents.list` 下添加智能体，在 `channels.<channel>.accounts` 下添加渠道账号，并使用 `bindings` 将它们连接起来（示例如下）。

* ### 重启并验证

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## 多个智能体 = 多个人、多个个性

使用**多个智能体** 时，每个 `agentId` 都会成为一个**完全隔离的人格** ：

  * **不同的电话号码/账号** （按渠道 `accountId`）。
  * **不同的个性** （按智能体划分的工作区文件，例如 `AGENTS.md` 和 `SOUL.md`）。
  * **独立的凭证 + 会话** （除非明确启用，否则不会串话）。


这允许**多人** 共享一台 Gateway 网关服务器，同时让他们的 AI“大脑”和数据保持隔离。

## 跨智能体 QMD 记忆搜索

如果一个智能体需要搜索另一个智能体的 QMD 会话转录，请在 `agents.list[].memorySearch.qmd.extraCollections` 下添加额外集合。只有当每个智能体都应该继承相同的共享转录集合时，才使用 `agents.defaults.memorySearch.qmd.extraCollections`。

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

额外集合路径可以在智能体之间共享，但当路径位于智能体工作区外部时，集合名称会保持显式。工作区内的路径仍然按智能体划定作用域，因此每个智能体都会保留自己的转录搜索集。

## 一个 WhatsApp 号码，多个人（私信拆分）

你可以在保持**一个 WhatsApp 账号** 的同时，把**不同的 WhatsApp 私信** 路由到不同智能体。通过 `peer.kind: "direct"` 按发送者 E.164（如 `+15551234567`）匹配。回复仍然来自同一个 WhatsApp 号码（没有按智能体划分的发送者身份）。

示例：

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

注意：

  * 私信访问控制是**每个 WhatsApp 账号全局** 的（配对/允许列表），不是按智能体划分。
  * 对于共享群组，请把群组绑定到一个智能体，或使用[广播群组](</zh-CN/channels/broadcast-groups>)。


## 路由规则（消息如何选择智能体）

绑定是**确定性的** ，并且**最具体者优先** ：

* ### peer 匹配

精确私信/群组/渠道 ID。

* ### parentPeer 匹配

线程继承。

* ### guildId + roles

Discord 角色路由。

* ### guildId

Discord。

* ### teamId

Slack。

* ### 某个渠道的 accountId 匹配

按账号回退。

* ### 渠道级匹配

`accountId: "*"`。

* ### 默认智能体

回退到 `agents.list[].default`，否则使用列表中的第一项，默认值：`main`。

平局处理和 AND 语义

  * 如果多个绑定在同一层级匹配，配置顺序中的第一个胜出。
  * 如果一个绑定设置了多个匹配字段（例如 `peer` \+ `guildId`），所有指定字段都必须满足（`AND` 语义）。

账号作用域细节

  * 省略 `accountId` 的绑定只匹配默认账号。
  * 使用 `accountId: "*"` 作为跨所有账号的渠道级回退。
  * 如果你之后为同一个智能体添加带显式账号 ID 的相同绑定，OpenClaw 会把现有的仅渠道绑定升级为账号作用域，而不是复制一个绑定。


## 多个账号/电话号码

支持**多个账号** 的渠道（例如 WhatsApp）使用 `accountId` 标识每次登录。每个 `accountId` 都可以路由到不同智能体，因此一台服务器可以托管多个电话号码而不会混合会话。

如果你希望在省略 `accountId` 时使用渠道级默认账号，请设置 `channels.<channel>.defaultAccount`（可选）。未设置时，OpenClaw 会回退到 `default`（如果存在），否则使用按排序后的第一个已配置账号 ID。

支持这种模式的常见渠道包括：

  * `whatsapp`、`telegram`、`discord`、`slack`、`signal`、`imessage`
  * `irc`、`line`、`googlechat`、`mattermost`、`matrix`、`nextcloud-talk`
  * `zalo`、`zalouser`、`nostr`、`feishu`


## 概念

  * `agentId`：一个“大脑”（工作区、按智能体划分的凭证、按智能体划分的会话存储）。
  * `accountId`：一个渠道账号实例（例如 WhatsApp 账号 `"personal"` 与 `"biz"`）。
  * `binding`：按 `(channel, accountId, peer)` 以及可选的 guild/team ID，将入站消息路由到某个 `agentId`。
  * 直接聊天会折叠到 `agent:<agentId>:<mainKey>`（按智能体划分的“main”；`session.mainKey`）。


## 平台示例

每个智能体一个 Discord 机器人

每个 Discord 机器人账号都映射到唯一的 `accountId`。将每个账号绑定到一个智能体，并为每个机器人保留允许列表。

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * 邀请每个 bot 加入 guild，并启用 Message Content Intent。
  * token 存放在 `channels.discord.accounts.<id>.token` 中（默认账户可以使用 `DISCORD_BOT_TOKEN`）。

每个 agent 一个 Telegram bot json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * 使用 BotFather 为每个 agent 创建一个 bot，并复制每个 token。
  * token 存放在 `channels.telegram.accounts.<id>.botToken` 中（默认账户可以使用 `TELEGRAM_BOT_TOKEN`）。

每个 agent 一个 WhatsApp 号码

在启动 Gateway 网关前先关联每个账户：

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## 常见模式

### WhatsApp 日常 + Telegram 深度工作

按 channel 拆分：将 WhatsApp 路由到快速的日常 agent，将 Telegram 路由到 Opus agent。

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp" } },    { agentId: "opus", match: { channel: "telegram" } },  ],}
[/code]

说明：

  * 如果一个 channel 有多个账户，请向 binding 添加 `accountId`（例如 `{ channel: "whatsapp", accountId: "personal" }`）。
  * 若要将单个私信/群组路由到 Opus，同时让其余内容继续留在 chat 上，请为该 peer 添加 `match.peer` binding；peer 匹配始终优先于 channel 范围的规则。


### 同一 channel，将一个 peer 路由到 Opus

让 WhatsApp 继续使用快速 agent，但将一个私信路由到 Opus：

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp" } },  ],}
[/code]

peer binding 始终优先，因此请把它们放在 channel 范围规则的上方。

### 绑定到 WhatsApp 群组的家庭 agent

将一个专用家庭 agent 绑定到单个 WhatsApp 群组，并配置 mention 门控和更严格的工具策略：

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

说明：

  * 工具允许/拒绝列表是**工具** ，不是 Skills。如果一个 skill 需要运行二进制文件，请确保允许 `exec`，且该二进制文件存在于沙箱中。
  * 对于更严格的门控，请设置 `agents.list[].groupChat.mentionPatterns`，并让该 channel 的群组允许列表保持启用。


## 每个 agent 的沙箱和工具配置

每个 agent 都可以有自己的沙箱和工具限制：

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**优势：**

  * **安全隔离** ：限制不受信任的 agent 可用的工具。
  * **资源控制** ：对特定 agent 使用沙箱，同时让其他 agent 保持在宿主机上运行。
  * **灵活策略** ：为每个 agent 设置不同权限。


请参阅[多 Agent 沙盒和工具](</zh-CN/tools/multi-agent-sandbox-tools>)了解详细示例。

## 相关内容

  * [ACP agents](</zh-CN/tools/acp-agents>) — 运行外部编码 harness
  * [频道路由](</zh-CN/channels/channel-routing>) — 消息如何路由到 agent
  * [Presence](</zh-CN/concepts/presence>) — agent 的 presence 和可用性
  * [Session](</zh-CN/concepts/session>) — session 隔离和路由
  * [Sub-agents](</zh-CN/tools/subagents>) — 生成后台 agent 运行


Was this useful?YesNo
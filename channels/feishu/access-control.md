---
title: Feishu access control
source_url: https://docs.openclaw.ai/channels/feishu/access-control
scraped_at: 2026-09-14
---

ChannelsRegional platforms

Who can talk to the Feishu bot, the group configuration examples that express those rules, and how to look up the IDs they need.

## Access control

### Direct messages

Configure `channels.feishu.dmPolicy` (default: `pairing`) to control who can DM the bot:

Value | Behavior  
---|---  
`"pairing"` | Unknown users receive a pairing code; approve via CLI  
`"allowlist"` | Only users listed in `allowFrom` can chat  
`"open"` | Public DMs; config validation requires `allowFrom` to include `"*"`. Non-wildcard entries still narrow access  
  
**Approve a pairing request:**

bashCopy code
[code]
    openclaw pairing list feishuopenclaw pairing approve feishu <CODE>
[/code]

### Group chats

**Group policy** (`channels.feishu.groupPolicy`, default: `allowlist`):

Value | Behavior  
---|---  
`"open"` | Respond to all messages in groups  
`"allowlist"` | Only respond to groups in `groupAllowFrom` or explicitly configured under `groups.<chat_id>`  
`"disabled"` | Disable all group messages; explicit `groups.<chat_id>` entries do not override this  
  
**Mention requirement** (`channels.feishu.requireMention`):

  * Default: @mention required, except when the effective group policy is `"open"`; there it defaults to `false` so messages that cannot carry mentions (for example images) still reach the agent.
  * Set `true` or `false` explicitly to override; per-group override: `channels.feishu.groups.<chat_id>.requireMention`.
  * Broadcast-only `@all` and `@_all` are not treated as bot mentions. A message that mentions both `@all` and the bot directly still counts as a bot mention.


Mentions of other people stay readable in the text sent to the agent, including when consecutive messages are combined.

## Group configuration examples

### Allow all groups, no @mention required

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "open", // requireMention defaults to false under "open"    },  },}
[/code]

### Allow all groups, still require @mention

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "open",      requireMention: true,    },  },}
[/code]

### Allow specific groups only

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      // Group IDs look like: oc_xxx      groupAllowFrom: ["oc_xxx", "oc_yyy"],    },  },}
[/code]

In `allowlist` mode, you can also admit a group by adding an explicit `groups.<chat_id>` entry. Explicit entries do not override `groupPolicy: "disabled"`. Wildcard defaults under `groups.*` configure matching groups, but they do not admit groups by themselves.

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      groups: {        oc_xxx: {          requireMention: false,        },      },    },  },}
[/code]

### Restrict senders within a group

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      groupAllowFrom: ["oc_xxx"],      groups: {        oc_xxx: {          // User open_ids look like: ou_xxx          allowFrom: ["ou_user1", "ou_user2"],        },      },    },  },}
[/code]

`channels.feishu.groupSenderAllowFrom` sets the same sender allowlist for all groups; a per-group `allowFrom` takes precedence.

### Bot-authored messages

Feishu ignores messages authored by other bots by default. To allow bot-to-bot group conversations, grant the app the `im:message.group_at_msg.include_bot:readonly` and `im:message:readonly` scopes, then set `allowBots`:

json5Copy code
[code]
    {  channels: {    feishu: {      allowBots: true,    },  },}
[/code]

Feishu only delivers bot-authored group events when another bot mentions this bot. Existing group policy, sender allowlists, and mention requirements still apply. OpenClaw drops self-authored messages, mentions the peer bot on every text or card reply, and applies the shared [`channels.defaults.botLoopProtection`](</channels/bot-loop-protection>) guard.

## Get group/user IDs

### Group IDs (`chat_id`, format: `oc_xxx`)

Open the group in Feishu/Lark, click the menu icon in the top-right corner, and go to **Settings**. The group ID (`chat_id`) is listed on the settings page.

![Get Group ID](/images/feishu-get-group-id.png)

### User IDs (`open_id`, format: `ou_xxx`)

Start the gateway, send a DM to the bot, then check the logs:

bashCopy code
[code]
    openclaw logs --follow
[/code]

Look for `open_id` in the log output. You can also check pending pairing requests:

bashCopy code
[code]
    openclaw pairing list feishu
[/code]

Was this useful?YesNo

Open issue
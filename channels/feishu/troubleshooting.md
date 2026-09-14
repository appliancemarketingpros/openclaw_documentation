---
title: Feishu troubleshooting
source_url: https://docs.openclaw.ai/channels/feishu/troubleshooting
scraped_at: 2026-09-14
---

ChannelsRegional platforms

Diagnostics for a Feishu bot that does not respond, does not receive events, or needs its credentials rotated.

## Troubleshooting

### Bot does not respond in group chats

  1. Ensure the bot is added to the group
  2. Ensure you @mention the bot (required by default)
  3. Verify `groupPolicy` is not `"disabled"`
  4. Check logs: `openclaw logs --follow`


### Bot does not receive messages

  1. Ensure the bot is published and approved in Feishu Open Platform / Lark Developer
  2. Ensure event subscription includes `im.message.receive_v1`
  3. For meeting invite auto-join, also subscribe to `vc.bot.meeting_invited_v1`
  4. Ensure **persistent connection** (WebSocket) is selected
  5. Ensure all required permission scopes are granted
  6. Ensure the gateway is running: `openclaw gateway status`
  7. Check logs: `openclaw logs --follow`


Subscribing to `vc.bot.meeting_invited_v1` only delivers the event. Automatic joins are default-off. To enable them globally:

json5Copy code
[code]
    {  channels: {    feishu: {      vcAutoJoin: true,    },  },}
[/code]

To enable only one account, omit the top-level switch and set the account override:

json5Copy code
[code]
    {  channels: {    feishu: {      accounts: {        meetings: { vcAutoJoin: true },      },    },  },}
[/code]

Inviters still pass through the normal Feishu DM policy, allowlist/pairing, session, and reply routing before the agent receives a join turn. Joining also requires an available Feishu VC join tool configured for app identity with the `vc:meeting.bot.join:write` scope. For example, the official [`lark-cli` VC agent skill](<https://github.com/larksuite/cli/tree/main/skills/lark-vc-agent>) provides `vc +meeting-join`.

### Webhook callbacks rejected with 401 Invalid signature

  1. Check the Gateway host clock: webhook mode rejects signed callbacks whose timestamp is more than one hour from the server clock (before or after). Verify NTP sync and that the system time is correct.
  2. Confirm the configured `encryptKey` matches the app's Encrypt Key in Feishu Open Platform / Lark Developer.
  3. Verify the webhook URL path and port match the `channels.feishu.webhook*` configuration.
  4. Check logs: `openclaw logs --follow` for repeated signature failures from unexpected senders.


### QR setup does not react in the Feishu mobile app

  1. Rerun setup: `openclaw channels login --channel feishu`
  2. Choose manual setup
  3. In Feishu Open Platform, create a self-built app and copy its App ID and App Secret
  4. Paste those credentials into the setup wizard


### App Secret leaked

  1. Reset the App Secret in Feishu Open Platform / Lark Developer
  2. Update the value in your config
  3. Verify that [hot reload](</gateway/configuration/hot-reload>) applied the new credentials with `openclaw channels status --probe`.


Was this useful?YesNo

Open issue
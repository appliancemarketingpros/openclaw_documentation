---
title: Telegram setup
source_url: https://docs.openclaw.ai/channels/telegram/setup
scraped_at: 2026-09-14
---

ChannelsMainstream messaging

Create the bot in BotFather, give OpenClaw its token, approve the first DM, and add the bot to a group.

## Quick setup

* ### Create the bot token in BotFather

Both flows end with a token you paste into OpenClaw — pick one:

  * **Chat flow** : open Telegram and chat with **@BotFather**. Confirm the handle is exactly `@BotFather`. Run `/newbot`, follow the prompts, and save the token.
  * **Web flow** : open [BotFather's web app](<https://t.me/BotFather?startapp>). It runs in every Telegram client, including [web.telegram.org](<https://web.telegram.org>). Create the bot in the UI, then copy its token.


* ### Configure token and DM policy

The fastest option is the CLI. It writes the token into your config for you:

bashCopy code
[code]
    openclaw channels add --channel telegram --token <bot-token>
[/code]

To edit config by hand instead, put this in `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {channels: {telegram: {  enabled: true,  botToken: "123:abc",  dmPolicy: "pairing",  groups: { "*": { requireMention: true } },},},}
[/code]

Env fallback: `TELEGRAM_BOT_TOKEN` (default account only). Named accounts must use `botToken` or `tokenFile`. Telegram does **not** use `openclaw channels login telegram`. Set the token in config or env, then start the gateway.

* ### Verify the channel

With the default [hot reload](/gateway/configuration/hot-reload), the running Gateway applies the new channel configuration. Check that Telegram is ready: bashCopy code
[code]
    openclaw channels status --probe
[/code]

If the Gateway is offline, start it with `openclaw gateway start` for a managed service, or `openclaw gateway` to run it in this terminal. If you changed the service environment, restart the Gateway to load it.

* ### Approve your first DM

Open Telegram and send any message to your bot. That message creates the pairing request the next command lists:

bashCopy code
[code]
    openclaw pairing list telegramopenclaw pairing approve telegram <CODE>
[/code]

Pairing codes expire after 1 hour.

* ### Add the bot to a group

Add the bot to your group, then get the two IDs group access needs:

  * your Telegram user ID, for `allowFrom` / `groupAllowFrom`
  * the Telegram group chat ID, as the key under `channels.telegram.groups`


Get the group chat ID from `openclaw logs --follow`, a forwarded-ID bot, or Bot API `getUpdates`. After the group is allowed, `/whoami@<bot_username>` confirms the user and group IDs.

Negative supergroup IDs starting with `-100` are group chat IDs. They go under `channels.telegram.groups`, not `groupAllowFrom`.

## Telegram side settings

Privacy mode and group visibility

Telegram bots default to **Privacy Mode** , which limits which group messages they receive.

To see all group messages, either:

  * disable privacy mode via `/setprivacy`, or
  * make the bot a group admin.


After toggling privacy mode, remove and re-add the bot in each group so Telegram applies the change.

Group permissions

Admin status is controlled in Telegram group settings. Admin bots receive all group messages, useful for always-on group behavior.

Helpful BotFather toggles

  * `/setjoingroups` — allow/deny group adds
  * `/setprivacy` — group visibility behavior


The same settings are available in [BotFather's web app](<https://t.me/BotFather?startapp>) if you prefer a UI over chat commands.

Was this useful?YesNo

Open issue
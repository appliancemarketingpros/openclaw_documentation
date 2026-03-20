---
title: Reactions
source_url: https://docs.openclaw.ai/tools/reactions
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools

Reactions

# 

​

Reactions

The agent can add and remove emoji reactions on messages using the `message` tool with the `react` action. Reaction behavior varies by channel.

## 

​

How it works

Copy
[code]
    {
      "action": "react",
      "messageId": "msg-123",
      "emoji": "thumbsup"
    }
    
[/code]

  * `emoji` is required when adding a reaction.
  * Set `emoji` to an empty string (`""`) to remove the bot’s reaction(s).
  * Set `remove: true` to remove a specific emoji (requires non-empty `emoji`).


## 

​

Channel behavior

Discord and Slack

  * Empty `emoji` removes all of the bot’s reactions on the message.
  * `remove: true` removes just the specified emoji.


Google Chat

  * Empty `emoji` removes the app’s reactions on the message.
  * `remove: true` removes just the specified emoji.


Telegram

  * Empty `emoji` removes the bot’s reactions.
  * `remove: true` also removes reactions but still requires a non-empty `emoji` for tool validation.


WhatsApp

  * Empty `emoji` removes the bot reaction.
  * `remove: true` maps to empty emoji internally (still requires `emoji` in the tool call).


Zalo Personal (zalouser)

  * Requires non-empty `emoji`.
  * `remove: true` removes that specific emoji reaction.


Signal

  * Inbound reaction notifications emit system events when `channels.signal.reactionNotifications` is enabled.


## 

​

Related

  * [Agent Send](</tools/agent-send>) — the `message` tool that includes `react`
  * [Channels](</channels>) — channel-specific configuration


[PDF Tool](</tools/pdf>)[Thinking Levels](</tools/thinking>)

⌘I
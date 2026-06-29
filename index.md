---
title: OpenClaw
source_url: https://docs.openclaw.ai/
scraped_at: 2026-06-29
---

Get startedOverview

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EXFOLIATE! EXFOLIATE!"_ — A space lobster, probably

**Any OS gateway for AI agents across Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more.**

Send a message, get an agent response from your pocket. Run one Gateway across built-in channels, bundled channel plugins, WebChat, and mobile nodes.

[**Get Started** Install OpenClaw and bring up the Gateway in minutes. ](</start/getting-started>) [**Run Onboarding** Guided setup with `openclaw onboard` and pairing flows. ](</start/wizard>) [**Open the Control UI** Launch the browser dashboard for chat, config, and sessions. ](</web/control-ui>)

## What is OpenClaw?

OpenClaw is a **self-hosted gateway** that connects your favorite chat apps and channel surfaces — built-in channels plus bundled or external channel plugins such as Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more — to AI coding agents. You run a single Gateway process on your own machine (or a server), and it becomes the bridge between your messaging apps and an always-available AI assistant.

**Who is it for?** Developers and power users who want a personal AI assistant they can message from anywhere — without giving up control of their data or relying on a hosted service.

**What makes it different?**

  * **Self-hosted** : runs on your hardware, your rules
  * **Multi-channel** : one Gateway serves built-in channels plus bundled or external channel plugins simultaneously
  * **Agent-native** : built for coding agents with tool use, sessions, memory, and multi-agent routing
  * **Open source** : MIT licensed, community-driven


**What do you need?** Node 24 (recommended), or Node 22 LTS (`22.19+`) for compatibility, an API key from your chosen provider, and 5 minutes. For best quality and security, use the strongest latest-generation model available.

## How it works
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["OpenClaw agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

The Gateway is the single source of truth for sessions, routing, and channel connections.

## Key capabilities

[**Multi-channel gateway** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, and more with a single Gateway process. ](</channels>) [**Plugin channels** Bundled plugins add Matrix, Nostr, Twitch, Zalo, and more in normal current releases. ](</tools/plugin>) [**Multi-agent routing** Isolated sessions per agent, workspace, or sender. ](</concepts/multi-agent>) [**Media support** Send and receive images, audio, and documents. ](</nodes/images>) [**Web Control UI** Browser dashboard for chat, config, sessions, and nodes. ](</web/control-ui>) [**Mobile nodes** Pair iOS and Android nodes for Canvas, camera, and voice-enabled workflows. ](</nodes>)

## Quick start

* ### Install OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Onboard and install the service

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chat

Open the Control UI in your browser and send a message:

bashCopy code
[code]
    openclaw dashboard
[/code]

Or connect a channel ([Telegram](</channels/telegram>) is fastest) and chat from your phone.

Need the full install and dev setup? See [Getting Started](</start/getting-started>).

## Dashboard

Open the browser Control UI after the Gateway starts.

  * Local default: <http://127.0.0.1:18789/>
  * Remote access: [Web surfaces](</web>) and [Tailscale](</gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Configuration (optional)

Config lives at `~/.openclaw/openclaw.json`.

  * If you **do nothing** , OpenClaw uses the bundled OpenClaw agent runtime with per-sender sessions.
  * If you want to lock it down, start with `channels.whatsapp.allowFrom` and (for groups) mention rules.


Example:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Start here

[**Docs hubs** All docs and guides, organized by use case. ](</start/hubs>) [**Configuration** Core Gateway settings, tokens, and provider config. ](</gateway/configuration>) [**Remote access** SSH and tailnet access patterns. ](</gateway/remote>) [**Channels** Channel-specific setup for Feishu, Microsoft Teams, WhatsApp, Telegram, Discord, and more. ](</channels/telegram>) [**Nodes** iOS and Android nodes with pairing, Canvas, camera, and device actions. ](</nodes>) [**Help** Common fixes and troubleshooting entry point. ](</help>)

## Learn more

[**Full feature list** Complete channel, routing, and media capabilities. ](</concepts/features>) [**Multi-agent routing** Workspace isolation and per-agent sessions. ](</concepts/multi-agent>) [**Security** Tokens, allowlists, and safety controls. ](</gateway/security>) [**Troubleshooting** Gateway diagnostics and common errors. ](</gateway/troubleshooting>) [**About and credits** Project origins, contributors, and license. ](</reference/credits>)

Was this useful?YesNo

Open issue
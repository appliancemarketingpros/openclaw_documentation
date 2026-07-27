---
title: OpenClaw
source_url: https://docs.openclaw.ai/
scraped_at: 2026-07-27
---

Get startedOverview

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-hero-light.png) ![OpenClaw](/assets/openclaw-hero-dark.png)

> _"EXFOLIATE! EXFOLIATE!"_ — A space lobster, probably

**Any OS gateway for AI agents across Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more.**

Send a message, get an agent response from your pocket. Run one Gateway across channel plugins, WebChat, and mobile nodes.

Developed in the open by the [OpenClaw Foundation](<https://openclaw.org>), a non-profit.

[**Get Started** Install OpenClaw and bring up the Gateway in minutes. ](</start/getting-started>) [**Run Onboarding** Guided setup with `openclaw onboard` and pairing flows. ](</start/wizard>) [**Connect a Channel** Link Discord, Signal, Telegram, WhatsApp, and more to chat from anywhere. ](</channels>) [**Open the Control UI** Launch the browser dashboard for chat, config, and sessions. ](</web/control-ui>)

## Browse docs

Mobile browsers may show the section menu without the full desktop tab bar. Use these hub links to reach the same top-level docs areas from the page body.

[**Get started** Overview, showcase, first steps, and setup guides. ](</>) [**Install** Install paths, updates, containers, hosting, and advanced setup. ](</install>) [**Channels** Messaging channels, pairing, routing, access groups, and channel QA. ](</channels>) [**Agents** Architecture, sessions, context, memory, and multi-agent routing. ](</concepts/architecture>) [**Capabilities** Tools, skills, cron, webhooks, and automation capabilities. ](</tools>) [**ClawHub** Plugin marketplace, publishing, curation, and trust guidance. ](</clawhub>) [**Models** Providers, model configuration, failover, and local model services. ](</providers>) [**Platforms** macOS, Windows, iOS, Android, nodes, and web surfaces. ](</platforms>) [**Gateway & Ops** Gateway configuration, security, diagnostics, and operations. ](</gateway>) [**Reference** CLI reference, schemas, RPC, release notes, and templates. ](</cli>) [**Help** Troubleshooting, FAQs, testing, diagnostics, and environment checks. ](</help>)

## What is OpenClaw?

OpenClaw is a **self-hosted gateway** that connects your favorite chat apps — Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more via channel plugins — to AI coding agents. You run a single Gateway process on your own machine (or a server), and it becomes the bridge between your messaging apps and an always-available AI assistant.

**Who is it for?** Developers and power users who want a personal AI assistant they can message from anywhere — without giving up control of their data or relying on a hosted service.

**What makes it different?**

  * **Self-hosted** : runs on your hardware, your rules
  * **Multi-channel** : one Gateway serves every configured channel plugin simultaneously
  * **Agent-native** : built for coding agents with tool use, sessions, memory, and multi-agent routing
  * **Open source** : MIT licensed, community-driven


**What do you need?** Node 24.15+ (recommended), Node 22 LTS (`22.22.3+`) for compatibility, or Node 25.9+, an API key from your chosen provider, and 5 minutes. For best quality and security, use the strongest latest-generation model available.

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

[**Multi-channel gateway** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, and more with a single Gateway process. ](</channels>) [**Plugin channels** Channel plugins add Matrix, Nostr, Twitch, Zalo, and more; official plugins install on demand. ](</tools/plugin>) [**Multi-agent routing** Isolated sessions per agent, workspace, or sender. ](</concepts/multi-agent>) [**Media support** Send and receive images, audio, and documents. ](</nodes/images>) [**Web Control UI** Browser dashboard for chat, config, sessions, and nodes. ](</web/control-ui>) [**Mobile nodes** Pair iOS and Android nodes for Canvas, camera, and voice-enabled workflows. ](</nodes>)

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

  * If you **do nothing** , OpenClaw uses the bundled OpenClaw agent runtime; DMs share the agent's main session, and each group chat gets its own session.
  * If you want to lock it down, start with `channels.whatsapp.allowFrom` and (for groups) mention rules.


Example:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Start here

[**Docs hubs** All docs and guides, organized by use case. ](</start/hubs>) [**Configuration** Core Gateway settings, tokens, and provider config. ](</gateway/configuration>) [**Remote access** SSH and tailnet access patterns. ](</gateway/remote>) [**Channels** Channel-specific setup for Discord, Feishu, Microsoft Teams, Telegram, WhatsApp, and more. ](</channels/telegram>) [**Nodes** iOS and Android nodes with pairing, Canvas, camera, and device actions. ](</nodes>) [**Help** Common fixes and troubleshooting entry point. ](</help>)

## Learn more

[**Full feature list** Complete channel, routing, and media capabilities. ](</concepts/features>) [**Multi-agent routing** Workspace isolation and per-agent sessions. ](</concepts/multi-agent>) [**Security** Tokens, allowlists, and safety controls. ](</gateway/security>) [**Troubleshooting** Gateway diagnostics and common errors. ](</gateway/troubleshooting>) [**About and credits** Project origins, contributors, and license. ](</reference/credits>)

Was this useful?YesNo

Open issue
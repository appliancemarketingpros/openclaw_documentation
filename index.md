---
title: OpenClawDocs.
source_url: https://docs.openclaw.ai/
scraped_at: 2026-09-28
---

Get startedOverview

[**Get Started** Install OpenClaw and bring up the Gateway in minutes. ](</start/getting-started>) [**Run Onboarding** Guided setup with `openclaw onboard` and pairing flows. ](</start/wizard>) [**Connect a Channel** Link Discord, Signal, Telegram, WhatsApp, and more to chat from anywhere. ](</channels>) [**Open the Control UI** Launch the browser dashboard for chat, config, and sessions. ](</web/control-ui>)

# OpenClaw 🦞

> _"EXFOLIATE! EXFOLIATE!"_ — A space lobster, probably

**Your AI assistant, on your own hardware, in every chat app you already use.**

One Gateway. Any model. Any device. No hosted service in the middle.

Developed in the open by the [OpenClaw Foundation](<https://openclaw.org>), an independent 501(c)(3). No paid tier, no telemetry by default beyond a [version check](</gateway/telemetry>) you can turn off, no lab owns it.

## Browse docs

Mobile browsers may show the section menu without the full desktop tab bar. Use these hub links to reach the same top-level docs areas from the page body.

[**Get started** Overview, showcase, first steps, and setup guides. ](</start/getting-started>) [**Install** Install paths, updates, containers, hosting, and advanced setup. ](</install>) [**Channels** Messaging channels, pairing, routing, access groups, and channel QA. ](</channels>) [**Agents** Architecture, sessions, context, memory, and multi-agent routing. ](</concepts/architecture>) [**Capabilities** Tools, skills, cron, webhooks, and automation capabilities. ](</tools>) [**ClawHub** Plugin marketplace, publishing, curation, and trust guidance. ](</clawhub>) [**Models** Providers, model configuration, failover, and local model services. ](</providers>) [**Platforms** macOS, Windows, iOS, Android, nodes, and web surfaces. ](</platforms>) [**Gateway & Ops** Gateway configuration, security, diagnostics, and operations. ](</gateway>) [**Reference** CLI reference, schemas, RPC, and templates. ](</cli>) [**Releases** Release notes for each version, with highlights and source links. ](</releases>) [**Help** Troubleshooting, FAQs, testing, diagnostics, and environment checks. ](</help>)

## What is OpenClaw?

OpenClaw is a **self-hosted gateway** that connects your favorite chat apps — Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more via channel plugins — to AI coding agents. You run a single Gateway process on your own machine (or a server), and it becomes the bridge between your messaging apps and an always-available AI assistant.

**Who is it for?** Developers, power users, and teams who want an AI assistant they can message from anywhere — without giving up control of their data or relying on a hosted service. The same gateway runs as a personal assistant on one laptop or as a shared [team deployment](</start/teams>); configuration is the only difference.

**What makes it different?**

  * **Self-hosted** : runs on your hardware, your rules
  * **Multi-channel** : one Gateway serves every configured channel plugin simultaneously
  * **Agent-native** : built for coding agents with tool use, sessions, memory, and multi-agent routing
  * **Open source** : MIT licensed, community-driven


The full architecture case — a trusted gateway, untrusted execution, deterministic policy, and how one product spans personal and team use — is in [Why OpenClaw](</start/why-openclaw>).

**What do you need?** Node 26 (recommended), or another supported release: Node 24.16+ or Node 26.1+. You also need an API key from your chosen provider and 5 minutes. For best quality and security, use the strongest latest-generation model available.

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

[**Multi-channel gateway** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, and more with a single Gateway process. ](</channels>) [**Plugin channels** Channel plugins add Matrix, Nostr, Twitch, Zalo, and more; official plugins install on demand. ](</tools/plugin>) [**Multi-agent routing** Isolated sessions per agent, workspace, or sender. ](</concepts/multi-agent>) [**Media support** Send and receive images, audio, and documents. ](</nodes/images>) [**Web Control UI** Browser dashboard for chat, config, sessions, and nodes. ](</web/control-ui>) [**Mobile nodes** Pair iOS and Android nodes for camera, screen, and voice-enabled workflows. ](</nodes>) [**Skills** Teach the agent repeatable procedures it loads on demand. ](</tools/skills>) [**Automation** Run work on a schedule with cron jobs, hooks, and webhooks. ](</automation>) [**Build plugins** Write your own channel, provider, and tool plugins against the plugin SDK. ](</plugins/building-plugins>)

## Quick start

* ### Install OpenClaw

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

The installer detects your OS, installs Node if needed, installs OpenClaw, and then starts onboarding. Other install methods (npm, pnpm, bun, Docker, Nix, from source) are on the [Install](</install>) page.

* ### Complete onboarding

Onboarding offers **Quick start** and **Custom setup**. Quick start reuses detected AI access, verifies it with a real completion, and opens the web dashboard with a Gateway in the foreground. Custom setup walks the full guided flow. `openclaw onboard --classic` opens the classic step-by-step wizard instead.

* ### Install the Gateway service

Quick start leaves the Gateway in the foreground. Press **Ctrl+C** , then install the background service:

bashCopy code
[code]
    openclaw gateway install
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

[**Docs hubs** All docs and guides, organized by use case. ](</start/hubs>) [**Configuration** Core Gateway settings, tokens, and provider config. ](</gateway/configuration>) [**Remote access** SSH and tailnet access patterns. ](</gateway/remote>) [**Channels** Channel-specific setup for Discord, Feishu, Microsoft Teams, Telegram, WhatsApp, and more. ](</channels>) [**Nodes** iOS and Android nodes with pairing, camera, screen, and device actions. ](</nodes>) [**Help** Common fixes and troubleshooting entry point. ](</help>)

## Learn more

[**Full feature list** Complete channel, routing, and media capabilities. ](</concepts/features>) [**Multi-agent routing** Workspace isolation and per-agent sessions. ](</concepts/multi-agent>) [**Security** Tokens, allowlists, and safety controls. ](</gateway/security>) [**Troubleshooting** Gateway diagnostics and common errors. ](</gateway/troubleshooting>) [**About and credits** Project origins, contributors, and license. ](</reference/credits>)

Was this useful?YesNo

Open issue
---
title: Getting Started
source_url: https://docs.openclaw.ai/start/getting-started
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

First steps

Getting Started

# 

​

Getting Started

Install OpenClaw, run onboarding, and chat with your AI assistant — all in about 5 minutes. By the end you will have a running Gateway, configured auth, and a working chat session.

## 

​

What you need

  * **Node.js** — Node 24 recommended (Node 22.16+ also supported)
  * **An API key** from a model provider (Anthropic, OpenAI, Google, etc.) — onboarding will prompt you


Check your Node version with `node --version`. **Windows users:** both native Windows and WSL2 are supported. WSL2 is more stable and recommended for the full experience. See [Windows](</platforms/windows>). Need to install Node? See [Node setup](</install/node>).

## 

​

Quick setup

1

Install OpenClaw

  * macOS / Linux

  * Windows (PowerShell)


Copy
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
    
[/code]

![Install Script Process](https://mintcdn.com/clawdhub/U8jr7qEbUc9OU9YR/assets/install-script.svg?fit=max&auto=format&n=U8jr7qEbUc9OU9YR&q=85&s=50706f81e3210a610262f14facb11f65)

Copy
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
    
[/code]

Other install methods (Docker, Nix, npm): [Install](</install>).

2

Run onboarding

Copy
[code]
    openclaw onboard --install-daemon
    
[/code]

The wizard walks you through choosing a model provider, setting an API key, and configuring the Gateway. It takes about 2 minutes.See [Onboarding (CLI)](</start/wizard>) for the full reference.

3

Verify the Gateway is running

Copy
[code]
    openclaw gateway status
    
[/code]

You should see the Gateway listening on port 18789.

4

Open the dashboard

Copy
[code]
    openclaw dashboard
    
[/code]

This opens the Control UI in your browser. If it loads, everything is working.

5

Send your first message

Type a message in the Control UI chat and you should get an AI reply.Want to chat from your phone instead? The fastest channel to set up is [Telegram](</channels/telegram>) (just a bot token). See [Channels](</channels>) for all options.

## 

​

What to do next

## Connect a channel

WhatsApp, Telegram, Discord, iMessage, and more.

## Pairing and safety

Control who can message your agent.

## Configure the Gateway

Models, tools, sandbox, and advanced settings.

## Browse tools

Browser, exec, web search, skills, and plugins.

Advanced: environment variables

If you run OpenClaw as a service account or want custom paths:

  * `OPENCLAW_HOME` — home directory for internal path resolution
  * `OPENCLAW_STATE_DIR` — override the state directory
  * `OPENCLAW_CONFIG_PATH` — override the config file path

Full reference: [Environment variables](</help/environment>).

[Features](</concepts/features>)[Onboarding Overview](</start/onboarding-overview>)

⌘I
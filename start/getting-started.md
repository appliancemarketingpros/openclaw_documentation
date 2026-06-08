---
title: Getting started
source_url: https://docs.openclaw.ai/start/getting-started
scraped_at: 2026-06-08
---

Get startedFirst steps

Install OpenClaw, run onboarding, and chat with your AI assistant — all in about 5 minutes. By the end you will have a running Gateway, configured auth, and a working chat session.

## What you need

  * **Node.js** — Node 24 recommended (Node 22.19+ also supported)
  * **An API key** from a model provider (Anthropic, OpenAI, Google, etc.) — onboarding will prompt you


## Quick setup

* ### Install OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Install Script Process](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

The wizard walks you through choosing a model provider, setting an API key, and configuring the Gateway. It takes about 2 minutes.

See [Onboarding (CLI)](</start/wizard>) for the full reference.

* ### Verify the Gateway is running

bashCopy code
[code]
    openclaw gateway status
[/code]

You should see the Gateway listening on port 18789.

* ### Open the dashboard

bashCopy code
[code]
    openclaw dashboard
[/code]

This opens the Control UI in your browser. If it loads, everything is working.

* ### Send your first message

Type a message in the Control UI chat and you should get an AI reply.

Want to chat from your phone instead? The fastest channel to set up is [Telegram](</channels/telegram>) (just a bot token). See [Channels](</channels>) for all options.

Advanced: mount a custom Control UI build

If you maintain a localized or customized dashboard build, point `gateway.controlUi.root` to a directory that contains your built static assets and `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Then set:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Restart the gateway and reopen the dashboard:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## What to do next

[**Connect a channel** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more. ](</channels>) [**Pairing and safety** Control who can message your agent. ](</channels/pairing>) [**Configure the Gateway** Models, tools, sandbox, and advanced settings. ](</gateway/configuration>) [**Browse tools** Browser, exec, web search, skills, and plugins. ](</tools>)

Advanced: environment variables

If you run OpenClaw as a service account or want custom paths:

  * `OPENCLAW_HOME` — home directory for internal path resolution
  * `OPENCLAW_STATE_DIR` — override the state directory
  * `OPENCLAW_CONFIG_PATH` — override the config file path


Full reference: [Environment variables](</help/environment>).

## Related

  * [Install overview](</install>)
  * [Channels overview](</channels>)
  * [Setup](</start/setup>)


Was this useful?YesNo

Open issue
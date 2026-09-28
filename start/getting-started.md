---
title: Getting started
source_url: https://docs.openclaw.ai/start/getting-started
scraped_at: 2026-09-28
---

Get startedFirst steps

Install OpenClaw, run onboarding, and chat with your AI assistant in about 5 minutes. By the end you will have a running Gateway, configured auth, and a working chat session.

## What you need

  * **Node.js 24.16+ or 26.1+** (Node 26 is the recommended runtime)
  * **An existing Claude Code or Codex CLI login, or a provider API key** — onboarding can reuse it


## Try it in one command

bashCopy code
[code]
    npx openclaw@latest
[/code]

On a fresh install, choose **Quick start** after a one-line pointer to the [security guide](</gateway/security>). That is the only onboarding prompt when usable AI access is already available: OpenClaw finds an existing Claude Code or Codex CLI login or API key, verifies it with a real completion, saves the config, and opens the web dashboard.

The Gateway runs in this terminal until you press **Ctrl+C** ; your config stays saved. If no detected route works, onboarding opens manual provider setup. Choose **Custom setup** to walk through all guided options instead.

To keep the Gateway running in the background later, install the CLI below and run `openclaw gateway install`. Run `openclaw` for the TUI or `openclaw dashboard` to reopen the web UI.

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

* ### Complete onboarding

The installer starts the guided onboarding wizard automatically. Choose **Quick start** to reuse detected AI access and open the dashboard, or **Custom setup** for the full guided flow. Provider sign-in and optional setup can take longer. Return later with `openclaw configure` for additional settings. `openclaw onboard --classic` opens the classic step-by-step wizard instead.

See [Onboarding (CLI)](</start/wizard>) for the full reference.

* ### Install the Gateway service

Quick start keeps the Gateway in the foreground of this terminal. The next steps need it running in the background. Press **Ctrl+C** to stop the foreground Gateway, then install the service:

bashCopy code
[code]
    openclaw gateway install
[/code]

This installs a LaunchAgent on macOS, a systemd user unit on Linux and WSL2, or a Scheduled Task on native Windows (with a per-user Startup-folder login item as the fallback if task creation is denied). Your config stays saved across the stop and the install.

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
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "${HOME}/.openclaw/control-ui-custom"  }}}
[/code]

Restart the gateway and reopen the dashboard:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## If setup does not work

One command turns the current state of your install into a diagnosis you can act on:

bashCopy code
[code]
    openclaw triage
[/code]

It runs read-only health checks, writes a sanitized prompt describing what it found, and then offers to hand that prompt to a coding agent it detects on your machine — Claude Code, Codex CLI, or the built-in OpenClaw agent — so the agent starts with the diagnosis already loaded. Pick "just print the commands" if you would rather run the handoff yourself.

Nothing leaves your machine until you choose an agent, and secrets, tokens, raw chat payloads, and raw logs are excluded from the prompt.

To read the findings yourself instead, run [`openclaw doctor`](</cli/doctor>). For symptom-first routes, see [Troubleshooting](</help/troubleshooting>).

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
  * [Personal assistant setup](</start/openclaw>) \- end-to-end guide to a dedicated number that behaves like an always-on assistant
  * [Triage](</cli/triage>)
  * [Troubleshooting](</help/troubleshooting>)


Was this useful?YesNo

Open issue
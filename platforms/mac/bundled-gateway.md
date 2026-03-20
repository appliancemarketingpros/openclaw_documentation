---
title: Gateway on macOS
source_url: https://docs.openclaw.ai/platforms/mac/bundled-gateway
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

macOS companion app

Gateway on macOS

# 

​

Gateway on macOS (external launchd)

OpenClaw.app no longer bundles Node/Bun or the Gateway runtime. The macOS app expects an **external** `openclaw` CLI install, does not spawn the Gateway as a child process, and manages a per‑user launchd service to keep the Gateway running (or attaches to an existing local Gateway if one is already running).

## 

​

Install the CLI (required for local mode)

Node 24 is the default runtime on the Mac. Node 22 LTS, currently `22.16+`, still works for compatibility. Then install `openclaw` globally:

Copy
[code]
    npm install -g openclaw@<version>
    
[/code]

The macOS app’s **Install CLI** button runs the same flow via npm/pnpm (bun not recommended for Gateway runtime).

## 

​

Launchd (Gateway as LaunchAgent)

Label:

  * `ai.openclaw.gateway` (or `ai.openclaw.<profile>`; legacy `com.openclaw.*` may remain)

Plist location (per‑user):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (or `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)

Manager:

  * The macOS app owns LaunchAgent install/update in Local mode.
  * The CLI can also install it: `openclaw gateway install`.

Behavior:

  * “OpenClaw Active” enables/disables the LaunchAgent.
  * App quit does **not** stop the gateway (launchd keeps it alive).
  * If a Gateway is already running on the configured port, the app attaches to it instead of starting a new one.

Logging:

  * launchd stdout/err: `/tmp/openclaw/openclaw-gateway.log`


## 

​

Version compatibility

The macOS app checks the gateway version against its own version. If they’re incompatible, update the global CLI to match the app version.

## 

​

Smoke check

Copy
[code]
    openclaw --version
    
    OPENCLAW_SKIP_CHANNELS=1 \
    OPENCLAW_SKIP_CANVAS_HOST=1 \
    openclaw gateway --port 18999 --bind loopback
    
[/code]

Then:

Copy
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
    
[/code]

[macOS Signing](</platforms/mac/signing>)[macOS IPC](</platforms/mac/xpc>)

⌘I
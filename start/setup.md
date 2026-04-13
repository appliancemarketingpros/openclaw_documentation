---
title: Setup
source_url: https://docs.openclaw.ai/start/setup
scraped_at: 2026-04-13
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Developer setup

Setup

# 

​

Setup

If you are setting up for the first time, start with [Getting Started](</start/getting-started>). For onboarding details, see [Onboarding (CLI)](</start/wizard>).

## 

​

TL;DR

  * **Tailoring lives outside the repo:** `~/.openclaw/workspace` (workspace) + `~/.openclaw/openclaw.json` (config).
  * **Stable workflow:** install the macOS app; let it run the bundled Gateway.
  * **Bleeding edge workflow:** run the Gateway yourself via `pnpm gateway:watch`, then let the macOS app attach in Local mode.


## 

​

Prereqs (from source)

  * Node 24 recommended (Node 22 LTS, currently `22.14+`, still supported)
  * `pnpm` preferred (or Bun if you intentionally use the [Bun workflow](</install/bun>))
  * Docker (optional; only for containerized setup/e2e — see [Docker](</install/docker>))


## 

​

Tailoring strategy (so updates do not hurt)

If you want “100% tailored to me” _and_ easy updates, keep your customization in:

  * **Config:** `~/.openclaw/openclaw.json` (JSON/JSON5-ish)
  * **Workspace:** `~/.openclaw/workspace` (skills, prompts, memories; make it a private git repo)

Bootstrap once:
[code] 
    openclaw setup
    
[/code]

From inside this repo, use the local CLI entry:
[code] 
    openclaw setup
    
[/code]

If you don’t have a global install yet, run it via `pnpm openclaw setup` (or `bun run openclaw setup` if you are using the Bun workflow).

## 

​

Run the Gateway from this repo

After `pnpm build`, you can run the packaged CLI directly:
[code] 
    node openclaw.mjs gateway --port 18789 --verbose
    
[/code]

## 

​

Stable workflow (macOS app first)

  1. Install + launch **OpenClaw.app** (menu bar).
  2. Complete the onboarding/permissions checklist (TCC prompts).
  3. Ensure Gateway is **Local** and running (the app manages it).
  4. Link surfaces (example: WhatsApp):


[code] 
    openclaw channels login
    
[/code]

  5. Sanity check:


[code] 
    openclaw health
    
[/code]

If onboarding is not available in your build:

  * Run `openclaw setup`, then `openclaw channels login`, then start the Gateway manually (`openclaw gateway`).


## 

​

Bleeding edge workflow (Gateway in a terminal)

Goal: work on the TypeScript Gateway, get hot reload, keep the macOS app UI attached.

### 

​

0) (Optional) Run the macOS app from source too

If you also want the macOS app on the bleeding edge:
[code] 
    ./scripts/restart-mac.sh
    
[/code]

### 

​

1) Start the dev Gateway
[code] 
    pnpm install
    pnpm gateway:watch
    
[/code]

`gateway:watch` runs the gateway in watch mode and reloads on relevant source, config, and bundled-plugin metadata changes. If you are intentionally using the Bun workflow, the equivalent commands are:
[code] 
    bun install
    bun run gateway:watch
    
[/code]

### 

​

2) Point the macOS app at your running Gateway

In **OpenClaw.app** :

  * Connection Mode: **Local** The app will attach to the running gateway on the configured port.


### 

​

3) Verify

  * In-app Gateway status should read **“Using existing gateway …”**
  * Or via CLI:


[code] 
    openclaw health
    
[/code]

### 

​

Common footguns

  * **Wrong port:** Gateway WS defaults to `ws://127.0.0.1:18789`; keep app + CLI on the same port.
  * **Where state lives:**
    * Channel/provider state: `~/.openclaw/credentials/`
    * Model auth profiles: `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
    * Sessions: `~/.openclaw/agents/<agentId>/sessions/`
    * Logs: `/tmp/openclaw/`


## 

​

Credential storage map

Use this when debugging auth or deciding what to back up:

  * **WhatsApp** : `~/.openclaw/credentials/whatsapp/<accountId>/creds.json`
  * **Telegram bot token** : config/env or `channels.telegram.tokenFile` (regular file only; symlinks rejected)
  * **Discord bot token** : config/env or SecretRef (env/file/exec providers)
  * **Slack tokens** : config/env (`channels.slack.*`)
  * **Pairing allowlists** :
    * `~/.openclaw/credentials/<channel>-allowFrom.json` (default account)
    * `~/.openclaw/credentials/<channel>-<accountId>-allowFrom.json` (non-default accounts)
  * **Model auth profiles** : `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * **File-backed secrets payload (optional)** : `~/.openclaw/secrets.json`
  * **Legacy OAuth import** : `~/.openclaw/credentials/oauth.json` More detail: [Security](</gateway/security#credential-storage-map>).


## 

​

Updating (without wrecking your setup)

  * Keep `~/.openclaw/workspace` and `~/.openclaw/` as “your stuff”; don’t put personal prompts/config into the `openclaw` repo.
  * Updating source: `git pull` \+ your chosen package-manager install step (`pnpm install` by default; `bun install` for Bun workflow) + keep using the matching `gateway:watch` command.


## 

​

Linux (systemd user service)

Linux installs use a systemd **user** service. By default, systemd stops user services on logout/idle, which kills the Gateway. Onboarding attempts to enable lingering for you (may prompt for sudo). If it’s still off, run:
[code] 
    sudo loginctl enable-linger $USER
    
[/code]

For always-on or multi-user servers, consider a **system** service instead of a user service (no lingering needed). See [Gateway runbook](</gateway>) for the systemd notes.

## 

​

Related docs

  * [Gateway runbook](</gateway>) (flags, supervision, ports)
  * [Gateway configuration](</gateway/configuration>) (config schema + examples)
  * [Discord](</channels/discord>) and [Telegram](</channels/telegram>) (reply tags + replyToMode settings)
  * [OpenClaw assistant setup](</start/openclaw>)
  * [macOS app](</platforms/macos>) (gateway lifecycle)


[Session Management Deep Dive](</reference/session-management-compaction>)[Pi Development Workflow](</pi-dev>)

⌘I
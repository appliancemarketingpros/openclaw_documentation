---
title: Linux App
source_url: https://docs.openclaw.ai/platforms/linux
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Platforms overview

Linux App

# 

​

Linux App

The Gateway is fully supported on Linux. **Node is the recommended runtime**. Bun is not recommended for the Gateway (WhatsApp/Telegram bugs). Native Linux companion apps are planned. Contributions are welcome if you want to help build one.

## 

​

Beginner quick path (VPS)

  1. Install Node 24 (recommended; Node 22 LTS, currently `22.16+`, still works for compatibility)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. From your laptop: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. Open `http://127.0.0.1:18789/` and paste your token

Full Linux server guide: [Linux Server](</vps>). Step-by-step VPS example: [exe.dev](</install/exe-dev>)

## 

​

Install

  * [Getting Started](</start/getting-started>)
  * [Install & updates](</install/updating>)
  * Optional flows: [Bun (experimental)](</install/bun>), [Nix](</install/nix>), [Docker](</install/docker>)


## 

​

Gateway

  * [Gateway runbook](</gateway>)
  * [Configuration](</gateway/configuration>)


## 

​

Gateway service install (CLI)

Use one of these:

Copy
[code]
    openclaw onboard --install-daemon
    
[/code]

Or:

Copy
[code]
    openclaw gateway install
    
[/code]

Or:

Copy
[code]
    openclaw configure
    
[/code]

Select **Gateway service** when prompted. Repair/migrate:

Copy
[code]
    openclaw doctor
    
[/code]

## 

​

System control (systemd user unit)

OpenClaw installs a systemd **user** service by default. Use a **system** service for shared or always-on servers. The full unit example and guidance live in the [Gateway runbook](</gateway>). Minimal setup: Create `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

Copy
[code]
    [Unit]
    Description=OpenClaw Gateway (profile: <profile>, v<version>)
    After=network-online.target
    Wants=network-online.target
    
    [Service]
    ExecStart=/usr/local/bin/openclaw gateway --port 18789
    Restart=always
    RestartSec=5
    
    [Install]
    WantedBy=default.target
    
[/code]

Enable it:

Copy
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
    
[/code]

[macOS App](</platforms/macos>)[Windows](</platforms/windows>)

⌘I
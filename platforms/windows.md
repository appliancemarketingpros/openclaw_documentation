---
title: Windows
source_url: https://docs.openclaw.ai/platforms/windows
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

Windows

# 

​

Windows

OpenClaw supports both **native Windows** and **WSL2**. WSL2 is the more stable path and recommended for the full experience — the CLI, Gateway, and tooling run inside Linux with full compatibility. Native Windows works for core CLI and Gateway use, with some caveats noted below. Native Windows companion apps are planned.

## 

​

WSL2 (recommended)

  * [Getting Started](</start/getting-started>) (use inside WSL)
  * [Install & updates](</install/updating>)
  * Official WSL2 guide (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## 

​

Native Windows status

Native Windows CLI flows are improving, but WSL2 is still the recommended path. What works well on native Windows today:

  * website installer via `install.ps1`
  * local CLI use such as `openclaw --version`, `openclaw doctor`, and `openclaw plugins list --json`
  * embedded local-agent/provider smoke such as:


Copy
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
    
[/code]

Current caveats:

  * `openclaw onboard --non-interactive` still expects a reachable local gateway unless you pass `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` and `openclaw gateway install` try Windows Scheduled Tasks first
  * if Scheduled Task creation is denied, OpenClaw falls back to a per-user Startup-folder login item and starts the gateway immediately
  * if `schtasks` itself wedges or stops responding, OpenClaw now aborts that path quickly and falls back instead of hanging forever
  * Scheduled Tasks are still preferred when available because they provide better supervisor status

If you want the native CLI only, without gateway service install, use one of these:

Copy
[code]
    openclaw onboard --non-interactive --skip-health
    openclaw gateway run
    
[/code]

If you do want managed startup on native Windows:

Copy
[code]
    openclaw gateway install
    openclaw gateway status --json
    
[/code]

If Scheduled Task creation is blocked, the fallback service mode still auto-starts after login through the current user’s Startup folder.

## 

​

Gateway

  * [Gateway runbook](</gateway>)
  * [Configuration](</gateway/configuration>)


## 

​

Gateway service install (CLI)

Inside WSL2:

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

Gateway auto-start before Windows login

For headless setups, ensure the full boot chain runs even when no one logs into Windows.

### 

​

1) Keep user services running without login

Inside WSL:

Copy
[code]
    sudo loginctl enable-linger "$(whoami)"
    
[/code]

### 

​

2) Install the OpenClaw gateway user service

Inside WSL:

Copy
[code]
    openclaw gateway install
    
[/code]

### 

​

3) Start WSL automatically at Windows boot

In PowerShell as Administrator:

Copy
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
    
[/code]

Replace `Ubuntu` with your distro name from:

Copy
[code]
    wsl --list --verbose
    
[/code]

### 

​

Verify startup chain

After a reboot (before Windows sign-in), check from WSL:

Copy
[code]
    systemctl --user is-enabled openclaw-gateway
    systemctl --user status openclaw-gateway --no-pager
    
[/code]

## 

​

Advanced: expose WSL services over LAN (portproxy)

WSL has its own virtual network. If another machine needs to reach a service running **inside WSL** (SSH, a local TTS server, or the Gateway), you must forward a Windows port to the current WSL IP. The WSL IP changes after restarts, so you may need to refresh the forwarding rule. Example (PowerShell **as Administrator**):

Copy
[code]
    $Distro = "Ubuntu-24.04"
    $ListenPort = 2222
    $TargetPort = 22
    
    $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]
    if (-not $WslIp) { throw "WSL IP not found." }
    
    netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `
      connectaddress=$WslIp connectport=$TargetPort
    
[/code]

Allow the port through Windows Firewall (one-time):

Copy
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `
      -Protocol TCP -LocalPort $ListenPort -Action Allow
    
[/code]

Refresh the portproxy after WSL restarts:

Copy
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Null
    netsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `
      connectaddress=$WslIp connectport=$TargetPort | Out-Null
    
[/code]

Notes:

  * SSH from another machine targets the **Windows host IP** (example: `ssh user@windows-host -p 2222`).
  * Remote nodes must point at a **reachable** Gateway URL (not `127.0.0.1`); use `openclaw status --all` to confirm.
  * Use `listenaddress=0.0.0.0` for LAN access; `127.0.0.1` keeps it local only.
  * If you want this automatic, register a Scheduled Task to run the refresh step at login.


## 

​

Step-by-step WSL2 install

### 

​

1) Install WSL2 + Ubuntu

Open PowerShell (Admin):

Copy
[code]
    wsl --install
    # Or pick a distro explicitly:
    wsl --list --online
    wsl --install -d Ubuntu-24.04
    
[/code]

Reboot if Windows asks.

### 

​

2) Enable systemd (required for gateway install)

In your WSL terminal:

Copy
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'
    [boot]
    systemd=true
    EOF
    
[/code]

Then from PowerShell:

Copy
[code]
    wsl --shutdown
    
[/code]

Re-open Ubuntu, then verify:

Copy
[code]
    systemctl --user status
    
[/code]

### 

​

3) Install OpenClaw (inside WSL)

Follow the Linux Getting Started flow inside WSL:

Copy
[code]
    git clone https://github.com/openclaw/openclaw.git
    cd openclaw
    pnpm install
    pnpm ui:build # auto-installs UI deps on first run
    pnpm build
    openclaw onboard
    
[/code]

Full guide: [Getting Started](</start/getting-started>)

## 

​

Windows companion app

We do not have a Windows companion app yet. Contributions are welcome if you want contributions to make it happen.

[Linux App](</platforms/linux>)[Android App](</platforms/android>)

⌘I
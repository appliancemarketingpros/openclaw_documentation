---
title: Install
source_url: https://docs.openclaw.ai/install
scraped_at: 2026-04-06
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Install overview

Install

# 

​

Install

## 

​

Recommended: installer script

The fastest way to install. It detects your OS, installs Node if needed, installs OpenClaw, and launches onboarding.

  * macOS / Linux / WSL2

  * Windows (PowerShell)


[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
    
[/code]
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
    
[/code]

To install without running onboarding:

  * macOS / Linux / WSL2

  * Windows (PowerShell)


[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
    
[/code]
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
    
[/code]

For all flags and CI/automation options, see [Installer internals](</install/installer>).

## 

​

System requirements

  * **Node 24** (recommended) or Node 22.14+ — the installer script handles this automatically
  * **macOS, Linux, or Windows** — both native Windows and WSL2 are supported; WSL2 is more stable. See [Windows](</platforms/windows>).
  * `pnpm` is only needed if you build from source


## 

​

Alternative install methods

### 

​

Local prefix installer (`install-cli.sh`)

Use this when you want OpenClaw and Node kept under a local prefix such as `~/.openclaw`, without depending on a system-wide Node install:
[code] 
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
    
[/code]

It supports npm installs by default, plus git-checkout installs under the same prefix flow. Full reference: [Installer internals](</install/installer#install-clish>).

### 

​

npm, pnpm, or bun

If you already manage Node yourself:

  * npm

  * pnpm

  * bun


[code]
    npm install -g openclaw@latest
    openclaw onboard --install-daemon
    
[/code]
[code]
    pnpm add -g openclaw@latest
    pnpm approve-builds -g
    openclaw onboard --install-daemon
    
[/code]

pnpm requires explicit approval for packages with build scripts. Run `pnpm approve-builds -g` after the first install.
[code]
    bun add -g openclaw@latest
    openclaw onboard --install-daemon
    
[/code]

Bun is supported for the global CLI install path. For the Gateway runtime, Node remains the recommended daemon runtime.

Troubleshooting: sharp build errors (npm)

If `sharp` fails due to a globally installed libvips:
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
    
[/code]

### 

​

From source

For contributors or anyone who wants to run from a local checkout:
[code] 
    git clone https://github.com/openclaw/openclaw.git
    cd openclaw
    pnpm install && pnpm ui:build && pnpm build
    pnpm link --global
    openclaw onboard --install-daemon
    
[/code]

Or skip the link and use `pnpm openclaw ...` from inside the repo. See [Setup](</start/setup>) for full development workflows.

### 

​

Install from GitHub main
[code] 
    npm install -g github:openclaw/openclaw#main
    
[/code]

### 

​

Containers and package managers

## Docker

Containerized or headless deployments.

## Podman

Rootless container alternative to Docker.

## Nix

Declarative install via Nix flake.

## Ansible

Automated fleet provisioning.

## Bun

CLI-only usage via the Bun runtime.

## 

​

Verify the install
[code] 
    openclaw --version      # confirm the CLI is available
    openclaw doctor         # check for config issues
    openclaw gateway status # verify the Gateway is running
    
[/code]

If you want managed startup after install:

  * macOS: LaunchAgent via `openclaw onboard --install-daemon` or `openclaw gateway install`
  * Linux/WSL2: systemd user service via the same commands
  * Native Windows: Scheduled Task first, with a per-user Startup-folder login item fallback if task creation is denied


## 

​

Hosting and deployment

Deploy OpenClaw on a cloud server or VPS:

## VPS

Any Linux VPS

## Docker VM

Shared Docker steps

## Kubernetes

K8s

## Fly.io

Fly.io

## Hetzner

Hetzner

## GCP

Google Cloud

## Azure

Azure

## Railway

Railway

## Render

Render

## Northflank

Northflank

## 

​

Update, migrate, or uninstall

## Updating

Keep OpenClaw up to date.

## Migrating

Move to a new machine.

## Uninstall

Remove OpenClaw completely.

## 

​

Troubleshooting: `openclaw` not found

If the install succeeded but `openclaw` is not found in your terminal:
[code] 
    node -v           # Node installed?
    npm prefix -g     # Where are global packages?
    echo "$PATH"      # Is the global bin dir in PATH?
    
[/code]

If `$(npm prefix -g)/bin` is not in your `$PATH`, add it to your shell startup file (`~/.zshrc` or `~/.bashrc`):
[code] 
    export PATH="$(npm prefix -g)/bin:$PATH"
    
[/code]

Then open a new terminal. See [Node setup](</install/node>) for more details.

[Installer Internals](</install/installer>)

⌘I
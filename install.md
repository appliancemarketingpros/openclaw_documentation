---
title: Install
source_url: https://docs.openclaw.ai/install
scraped_at: 2026-09-28
---

InstallInstall overview

## System requirements

  * **Node 24.16+ or 26.1+** \- Node 26 is recommended; the installer provisions Node 26 on macOS and Node 24 LTS on Linux when Node is missing (see [Node.js compatibility](</install/node-compatibility>)).
  * **macOS, Linux, or Windows** \- Windows users can start with the native Windows Hub app, the PowerShell CLI installer, or a WSL2 Gateway. See [Windows](</platforms/windows>).
  * `pnpm` is only needed if you build from source.


## Download the desktop app

Prefer a normal app download over the CLI? OpenClaw ships desktop companions:

  * **Windows** : the [Windows Hub](</platforms/windows#recommended-windows-hub>) companion app — a signed installer you download and run like any Windows app, with setup, tray status, chat, and node mode: 
    * [OpenClawCompanion-Setup-x64.exe](<https://github.com/openclaw/openclaw-windows-node/releases/latest/download/OpenClawCompanion-Setup-x64.exe>)
    * [OpenClawCompanion-Setup-arm64.exe](<https://github.com/openclaw/openclaw-windows-node/releases/latest/download/OpenClawCompanion-Setup-arm64.exe>)
    * All Hub releases: [Windows Hub releases page](<https://github.com/openclaw/openclaw-windows-node/releases/latest>)
  * **macOS** : the [macOS menu bar app](</platforms/macos>) — download the `OpenClaw-<version>.dmg` (preferred) or `.zip` asset from [OpenClaw GitHub releases](<https://github.com/openclaw/openclaw/releases>), then install and launch **OpenClaw.app**. See the [macOS app page](</platforms/macos>) for details, including what to do when the newest release ships no macOS asset.


Both desktop apps can provision a local Gateway during first-run setup, or connect to an existing remote Gateway.

## Recommended: installer script

The fastest way to install. It detects your OS, installs Node if needed, installs OpenClaw, and launches onboarding.

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

To install without running onboarding:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

For all flags and CI/automation options, see [Installer internals](</install/installer>).

## Alternative install methods

### Local prefix installer (`install-cli.sh`)

Use this when you want OpenClaw and Node kept under a local prefix such as `~/.openclaw`, without depending on a system-wide Node install:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

It supports npm installs by default, plus git-checkout installs under the same prefix flow. Full reference: [Installer internals](</install/installer#install-clish>).

Already installed? Switch between package and git installs with `openclaw update --channel dev` and `openclaw update --channel stable`. See [Updating](</install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm, or bun

If you already manage Node yourself:

### npm

On npm 12 or npm 11.16+:

bashCopy code
[code]
    npm install -g openclaw@latest --allow-scripts=openclawopenclaw onboard --install-daemon
[/code]

On npm 11.15 and earlier, use the same command without `--allow-scripts=openclaw`.

### pnpm

bashCopy code
[code]
    pnpm add -g --allow-build=openclaw openclaw@latestopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g --trust openclaw@latestbun run --bun openclaw onboard --install-daemon --daemon-runtime bun
[/code]

### From source

For contributors or anyone who wants to run from a local checkout:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawcorepack enablepnpm install && pnpm build && pnpm ui:buildpnpm add --global "openclaw@link:$PWD"openclaw onboard --install-daemon
[/code]

`pnpm add --global "openclaw@link:$PWD"` links the CLI to this checkout without changing its package files. If pnpm reports that its global bin directory is not on `PATH`, run `pnpm setup`, reopen your shell, and retry.

Corepack selects the exact pnpm version from `package.json` (currently pnpm 12). If Corepack is unavailable, install that version explicitly with `npm install -g pnpm@12.3.4 --allow-scripts=pnpm@12.3.4`; keep npm install scripts and optional dependencies enabled so pnpm can provision its native executable.

Or skip the global install and use `pnpm openclaw ...` from inside the repo. See [Setup](</start/setup>) for full development workflows.

### Install from the GitHub main checkout

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git --version main
[/code]

### Containers and package managers

[**Ansible** Automated fleet provisioning. ](</install/ansible>) [**Bun** Optional dependency installer and package-script runner. ](</install/bun>) [**Docker** Containerized or headless deployments. ](</install/docker>) [**Nix** Declarative install via Nix flake. ](</install/nix>) [**Podman** Rootless container alternative to Docker. ](</install/podman>)

## Verify the install

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

If you want managed startup after install:

  * macOS: LaunchAgent via `openclaw onboard --install-daemon` or `openclaw gateway install`
  * Linux/WSL2: systemd user service via the same commands
  * Native Windows: Scheduled Task first, with a per-user Startup-folder login item fallback if task creation is denied


## Next: run onboarding and connect a channel

[**Getting started** Run onboarding, install the Gateway service, and open the dashboard. ](</start/getting-started>) [**Connect a channel** Message your agent from Telegram, Discord, Slack, WhatsApp, and more. ](</channels>)

## Hosting and deployment

Deploy OpenClaw on a cloud server or VPS. See [Linux server](</vps>) for the full provider picker (DigitalOcean, Hetzner, Hostinger, Fly.io, GCP, Azure, Railway, Northflank, Oracle Cloud, Raspberry Pi, and more), deploy declaratively on [Render](</install/render>), or try the experimental [Cloudflare Containers](</install/cloudflare>) template.

[**Cloudflare** Experimental Worker + Container deployment. ](</install/cloudflare>) [**Docker VM** Shared Docker steps. ](</install/docker-vm-runtime>) [**Kubernetes** K8s deployment. ](</install/kubernetes>) [**macOS VM** Isolated local or hosted macOS deployment. ](</install/macos-vm>) [**Upstash Box** Managed Linux host with SSH-tunneled access. ](</install/upstash>) [**VPS** Pick a provider. ](</vps>)

## Back up, update, migrate, or uninstall

[**Backups** Create, verify, and restore state archives. ](</install/backups>) [**Updating** Keep OpenClaw up to date. ](</install/updating>) [**Migrating** Move to a new machine. ](</install/migrating>) [**Uninstall** Remove OpenClaw completely. ](</install/uninstall>)

## Troubleshooting: `openclaw` not found

Almost always a PATH issue: npm's global bin directory isn't on your shell's `PATH`. See [Node.js troubleshooting](</install/node#troubleshooting>) for the full fix, including the Windows path.

bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Was this useful?YesNo

Open issue
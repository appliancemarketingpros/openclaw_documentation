---
title: Install
source_url: https://docs.openclaw.ai/install
scraped_at: 2026-06-22
---

InstallInstall overview

## System requirements

  * **Node 24** (recommended) or Node 22.19+ - the installer script handles this automatically
  * **macOS, Linux, or Windows** \- Windows users can start with the native Windows Hub app, the PowerShell CLI installer, or a WSL2 Gateway. See [Windows](</platforms/windows>).
  * `pnpm` is only needed if you build from source


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

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### From source

For contributors or anyone who wants to run from a local checkout:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Or skip the link and use `pnpm openclaw ...` from inside the repo. See [Setup](</start/setup>) for full development workflows.

### Install from the GitHub main checkout

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git --version main
[/code]

### Containers and package managers

[**Docker** Containerized or headless deployments. ](</install/docker>) [**Podman** Rootless container alternative to Docker. ](</install/podman>) [**Nix** Declarative install via Nix flake. ](</install/nix>) [**Ansible** Automated fleet provisioning. ](</install/ansible>) [**Bun** CLI-only usage via the Bun runtime. ](</install/bun>)

## Verify the install

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

If you want managed startup after install:

  * macOS: LaunchAgent via `openclaw onboard --install-daemon` or `openclaw gateway install`
  * Linux/WSL2: systemd user service via the same commands
  * Native Windows: Scheduled Task first, with a per-user Startup-folder login item fallback if task creation is denied


## Hosting and deployment

Deploy OpenClaw on a cloud server or VPS:

[**VPS** Any Linux VPS. ](</vps>) [**Docker VM** Shared Docker steps. ](</install/docker-vm-runtime>) [**Kubernetes** K8s deployment. ](</install/kubernetes>) [**Fly.io** Deploy on Fly.io. ](</install/fly>) [**Hetzner** Hetzner deployment. ](</install/hetzner>) [**GCP** Google Cloud deployment. ](</install/gcp>) [**Azure** Azure deployment. ](</install/azure>) [**Railway** Railway deployment. ](</install/railway>) [**Render** Render deployment. ](</install/render>) [**Northflank** Northflank deployment. ](</install/northflank>)

## Update, migrate, or uninstall

[**Updating** Keep OpenClaw up to date. ](</install/updating>) [**Migrating** Move to a new machine. ](</install/migrating>) [**Uninstall** Remove OpenClaw completely. ](</install/uninstall>)

## Troubleshooting: `openclaw` not found

If the install succeeded but `openclaw` is not found in your terminal:

bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

If `$(npm prefix -g)/bin` is not in your `$PATH`, add it to your shell startup file (`~/.zshrc` or `~/.bashrc`):

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Then open a new terminal. See [Node setup](</install/node>) for more details.

Was this useful?YesNo

Open issue
---
title: Uninstall
source_url: https://docs.openclaw.ai/install/uninstall
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Maintenance

Uninstall

# 

​

Uninstall

Two paths:

  * **Easy path** if `openclaw` is still installed.
  * **Manual service removal** if the CLI is gone but the service is still running.


## 

​

Easy path (CLI still installed)

Recommended: use the built-in uninstaller:

Copy
[code]
    openclaw uninstall
    
[/code]

Non-interactive (automation / npx):

Copy
[code]
    openclaw uninstall --all --yes --non-interactive
    npx -y openclaw uninstall --all --yes --non-interactive
    
[/code]

Manual steps (same result):

  1. Stop the gateway service:


Copy
[code]
    openclaw gateway stop
    
[/code]

  2. Uninstall the gateway service (launchd/systemd/schtasks):


Copy
[code]
    openclaw gateway uninstall
    
[/code]

  3. Delete state + config:


Copy
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
    
[/code]

If you set `OPENCLAW_CONFIG_PATH` to a custom location outside the state dir, delete that file too.

  4. Delete your workspace (optional, removes agent files):


Copy
[code]
    rm -rf ~/.openclaw/workspace
    
[/code]

  5. Remove the CLI install (pick the one you used):


Copy
[code]
    npm rm -g openclaw
    pnpm remove -g openclaw
    bun remove -g openclaw
    
[/code]

  6. If you installed the macOS app:


Copy
[code]
    rm -rf /Applications/OpenClaw.app
    
[/code]

Notes:

  * If you used profiles (`--profile` / `OPENCLAW_PROFILE`), repeat step 3 for each state dir (defaults are `~/.openclaw-<profile>`).
  * In remote mode, the state dir lives on the **gateway host** , so run steps 1-4 there too.


## 

​

Manual service removal (CLI not installed)

Use this if the gateway service keeps running but `openclaw` is missing.

### 

​

macOS (launchd)

Default label is `ai.openclaw.gateway` (or `ai.openclaw.<profile>`; legacy `com.openclaw.*` may still exist):

Copy
[code]
    launchctl bootout gui/$UID/ai.openclaw.gateway
    rm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
    
[/code]

If you used a profile, replace the label and plist name with `ai.openclaw.<profile>`. Remove any legacy `com.openclaw.*` plists if present.

### 

​

Linux (systemd user unit)

Default unit name is `openclaw-gateway.service` (or `openclaw-gateway-<profile>.service`):

Copy
[code]
    systemctl --user disable --now openclaw-gateway.service
    rm -f ~/.config/systemd/user/openclaw-gateway.service
    systemctl --user daemon-reload
    
[/code]

### 

​

Windows (Scheduled Task)

Default task name is `OpenClaw Gateway` (or `OpenClaw Gateway (<profile>)`). The task script lives under your state dir.

Copy
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"
    Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
    
[/code]

If you used a profile, delete the matching task name and `~\.openclaw-<profile>\gateway.cmd`.

## 

​

Normal install vs source checkout

### 

​

Normal install (install.sh / npm / pnpm / bun)

If you used `https://openclaw.ai/install.sh` or `install.ps1`, the CLI was installed with `npm install -g openclaw@latest`. Remove it with `npm rm -g openclaw` (or `pnpm remove -g` / `bun remove -g` if you installed that way).

### 

​

Source checkout (git clone)

If you run from a repo checkout (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Uninstall the gateway service **before** deleting the repo (use the easy path above or manual service removal).
  2. Delete the repo directory.
  3. Remove state + workspace as shown above.


[Migration Guide](</install/migrating>)[Release Channels](</install/development-channels>)

⌘I
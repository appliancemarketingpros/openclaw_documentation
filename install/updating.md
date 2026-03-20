---
title: Updating
source_url: https://docs.openclaw.ai/install/updating
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

Updating

# 

​

Updating

Keep OpenClaw up to date.

## 

​

Recommended: `openclaw update`

The fastest way to update. It detects your install type (npm or git), fetches the latest version, runs `openclaw doctor`, and restarts the gateway.

Copy
[code]
    openclaw update
    
[/code]

To switch channels or target a specific version:

Copy
[code]
    openclaw update --channel beta
    openclaw update --tag main
    openclaw update --dry-run   # preview without applying
    
[/code]

See [Development channels](</install/development-channels>) for channel semantics.

## 

​

Alternative: re-run the installer

Copy
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
    
[/code]

Add `--no-onboard` to skip onboarding. For source installs, pass `--install-method git --no-onboard`.

## 

​

Alternative: manual npm or pnpm

Copy
[code]
    npm i -g openclaw@latest
    
[/code]

Copy
[code]
    pnpm add -g openclaw@latest
    
[/code]

## 

​

Auto-updater

The auto-updater is off by default. Enable it in `~/.openclaw/openclaw.json`:

Copy
[code]
    {
      update: {
        channel: "stable",
        auto: {
          enabled: true,
          stableDelayHours: 6,
          stableJitterHours: 12,
          betaCheckIntervalHours: 1,
        },
      },
    }
    
[/code]

Channel| Behavior  
---|---  
`stable`| Waits `stableDelayHours`, then applies with deterministic jitter across `stableJitterHours` (spread rollout).  
`beta`| Checks every `betaCheckIntervalHours` (default: hourly) and applies immediately.  
`dev`| No automatic apply. Use `openclaw update` manually.  
  
The gateway also logs an update hint on startup (disable with `update.checkOnStart: false`).

## 

​

After updating

1

Run doctor

2
[code]
    openclaw doctor
    
[/code]

3

Migrates config, audits DM policies, and checks gateway health. Details: [Doctor](</gateway/doctor>)

4

Restart the gateway

5
[code]
    openclaw gateway restart
    
[/code]

6

Verify

7
[code]
    openclaw health
    
[/code]

## 

​

Rollback

### 

​

Pin a version (npm)

Copy
[code]
    npm i -g openclaw@<version>
    openclaw doctor
    openclaw gateway restart
    
[/code]

Tip: `npm view openclaw version` shows the current published version.

### 

​

Pin a commit (source)

Copy
[code]
    git fetch origin
    git checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"
    pnpm install && pnpm build
    openclaw gateway restart
    
[/code]

To return to latest: `git checkout main && git pull`.

## 

​

If you are stuck

  * Run `openclaw doctor` again and read the output carefully.
  * Check: [Troubleshooting](</gateway/troubleshooting>)
  * Ask in Discord: <https://discord.gg/clawd>


[Render](</install/render>)[Migration Guide](</install/migrating>)

⌘I
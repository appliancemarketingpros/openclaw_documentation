---
title: Migration Guide
source_url: https://docs.openclaw.ai/install/migrating
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

Migration Guide

# 

​

Migrating OpenClaw to a New Machine

This guide moves an OpenClaw gateway to a new machine without redoing onboarding.

## 

​

What Gets Migrated

When you copy the **state directory** (`~/.openclaw/` by default) and your **workspace** , you preserve:

  * **Config** — `openclaw.json` and all gateway settings
  * **Auth** — API keys, OAuth tokens, credential profiles
  * **Sessions** — conversation history and agent state
  * **Channel state** — WhatsApp login, Telegram session, etc.
  * **Workspace files** — `MEMORY.md`, `USER.md`, skills, and prompts


Run `openclaw status` on the old machine to confirm your state directory path. Custom profiles use `~/.openclaw-<profile>/` or a path set via `OPENCLAW_STATE_DIR`.

## 

​

Migration Steps

1

Stop the gateway and back up

On the **old** machine, stop the gateway so files are not changing mid-copy, then archive:

Copy
[code]
    openclaw gateway stop
    cd ~
    tar -czf openclaw-state.tgz .openclaw
    
[/code]

If you use multiple profiles (e.g. `~/.openclaw-work`), archive each separately.

2

Install OpenClaw on the new machine

[Install](</install>) the CLI (and Node if needed) on the new machine. It is fine if onboarding creates a fresh `~/.openclaw/` — you will overwrite it next.

3

Copy state directory and workspace

Transfer the archive via `scp`, `rsync -a`, or an external drive, then extract:

Copy
[code]
    cd ~
    tar -xzf openclaw-state.tgz
    
[/code]

Ensure hidden directories were included and file ownership matches the user that will run the gateway.

4

Run doctor and verify

On the new machine, run [Doctor](</gateway/doctor>) to apply config migrations and repair services:

Copy
[code]
    openclaw doctor
    openclaw gateway restart
    openclaw status
    
[/code]

## 

​

Common Pitfalls

Profile or state-dir mismatch

If the old gateway used `--profile` or `OPENCLAW_STATE_DIR` and the new one does not, channels will appear logged out and sessions will be empty. Launch the gateway with the **same** profile or state-dir you migrated, then rerun `openclaw doctor`.

Copying only openclaw.json

The config file alone is not enough. Credentials live under `credentials/`, and agent state lives under `agents/`. Always migrate the **entire** state directory.

Permissions and ownership

If you copied as root or switched users, the gateway may fail to read credentials. Ensure the state directory and workspace are owned by the user running the gateway.

Remote mode

If your UI points at a **remote** gateway, the remote host owns sessions and workspace. Migrate the gateway host itself, not your local laptop. See [FAQ](</help/faq#where-does-openclaw-store-its-data>).

Secrets in backups

The state directory contains API keys, OAuth tokens, and channel credentials. Store backups encrypted, avoid insecure transfer channels, and rotate keys if you suspect exposure.

## 

​

Verification Checklist

On the new machine, confirm:

  * `openclaw status` shows the gateway running
  * Channels are still connected (no re-pairing needed)
  * The dashboard opens and shows existing sessions
  * Workspace files (memory, configs) are present


[Updating](</install/updating>)[Uninstall](</install/uninstall>)

⌘I
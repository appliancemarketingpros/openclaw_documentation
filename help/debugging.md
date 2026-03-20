---
title: Debugging
source_url: https://docs.openclaw.ai/help/debugging
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Environment and debugging

Debugging

# 

​

Debugging

This page covers debugging helpers for streaming output, especially when a provider mixes reasoning into normal text.

## 

​

Runtime debug overrides

Use `/debug` in chat to set **runtime-only** config overrides (memory, not disk). `/debug` is disabled by default; enable with `commands.debug: true`. This is handy when you need to toggle obscure settings without editing `openclaw.json`. Examples:

Copy
[code]
    /debug show
    /debug set messages.responsePrefix="[openclaw]"
    /debug unset messages.responsePrefix
    /debug reset
    
[/code]

`/debug reset` clears all overrides and returns to the on-disk config.

## 

​

Gateway watch mode

For fast iteration, run the gateway under the file watcher:

Copy
[code]
    pnpm gateway:watch
    
[/code]

This maps to:

Copy
[code]
    node scripts/watch-node.mjs gateway --force
    
[/code]

The watcher restarts on build-relevant files under `src/`, extension source files, extension `package.json` and `openclaw.plugin.json` metadata, `tsconfig.json`, `package.json`, and `tsdown.config.ts`. Extension metadata changes restart the gateway without forcing a `tsdown` rebuild; source and config changes still rebuild `dist` first. Add any gateway CLI flags after `gateway:watch` and they will be passed through on each restart.

## 

​

Dev profile + dev gateway (—dev)

Use the dev profile to isolate state and spin up a safe, disposable setup for debugging. There are **two** `--dev` flags:

  * **Global`--dev` (profile):** isolates state under `~/.openclaw-dev` and defaults the gateway port to `19001` (derived ports shift with it).
  * **`gateway --dev`: tells the Gateway to auto-create a default config + workspace** when missing (and skip BOOTSTRAP.md).

Recommended flow (dev profile + dev bootstrap):

Copy
[code]
    pnpm gateway:dev
    OPENCLAW_PROFILE=dev openclaw tui
    
[/code]

If you don’t have a global install yet, run the CLI via `pnpm openclaw ...`. What this does:

  1. **Profile isolation** (global `--dev`)
     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001` (browser/canvas shift accordingly)
  2. **Dev bootstrap** (`gateway --dev`)
     * Writes a minimal config if missing (`gateway.mode=local`, bind loopback).
     * Sets `agent.workspace` to the dev workspace.
     * Sets `agent.skipBootstrap=true` (no BOOTSTRAP.md).
     * Seeds the workspace files if missing: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`.
     * Default identity: **C3‑PO** (protocol droid).
     * Skips channel providers in dev mode (`OPENCLAW_SKIP_CHANNELS=1`).

Reset flow (fresh start):

Copy
[code]
    pnpm gateway:dev:reset
    
[/code]

Note: `--dev` is a **global** profile flag and gets eaten by some runners. If you need to spell it out, use the env var form:

Copy
[code]
    OPENCLAW_PROFILE=dev openclaw gateway --dev --reset
    
[/code]

`--reset` wipes config, credentials, sessions, and the dev workspace (using `trash`, not `rm`), then recreates the default dev setup. Tip: if a non‑dev gateway is already running (launchd/systemd), stop it first:

Copy
[code]
    openclaw gateway stop
    
[/code]

## 

​

Raw stream logging (OpenClaw)

OpenClaw can log the **raw assistant stream** before any filtering/formatting. This is the best way to see whether reasoning is arriving as plain text deltas (or as separate thinking blocks). Enable it via CLI:

Copy
[code]
    pnpm gateway:watch --raw-stream
    
[/code]

Optional path override:

Copy
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
    
[/code]

Equivalent env vars:

Copy
[code]
    OPENCLAW_RAW_STREAM=1
    OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
    
[/code]

Default file: `~/.openclaw/logs/raw-stream.jsonl`

## 

​

Raw chunk logging (pi-mono)

To capture **raw OpenAI-compat chunks** before they are parsed into blocks, pi-mono exposes a separate logger:

Copy
[code]
    PI_RAW_STREAM=1
    
[/code]

Optional path:

Copy
[code]
    PI_RAW_STREAM_PATH=~/.pi-mono/logs/raw-openai-completions.jsonl
    
[/code]

Default file: `~/.pi-mono/logs/raw-openai-completions.jsonl`

> Note: this is only emitted by processes using pi-mono’s `openai-completions` provider.

## 

​

Safety notes

  * Raw stream logs can include full prompts, tool output, and user data.
  * Keep logs local and delete them after debugging.
  * If you share logs, scrub secrets and PII first.


[Environment Variables](</help/environment>)[Testing](</help/testing>)

⌘I
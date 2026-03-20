---
title: Bun (Experimental)
source_url: https://docs.openclaw.ai/install/bun
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Containers

Bun (Experimental)

# 

​

Bun (Experimental)

Bun is **not recommended for gateway runtime** (known issues with WhatsApp and Telegram). Use Node for production.

Bun is an optional local runtime for running TypeScript directly (`bun run ...`, `bun --watch ...`). The default package manager remains `pnpm`, which is fully supported and used by docs tooling. Bun cannot use `pnpm-lock.yaml` and will ignore it.

## 

​

Install

1

Install dependencies

Copy
[code]
    bun install
    
[/code]

`bun.lock` / `bun.lockb` are gitignored, so there is no repo churn. To skip lockfile writes entirely:

Copy
[code]
    bun install --no-save
    
[/code]

2

Build and test

Copy
[code]
    bun run build
    bun run vitest run
    
[/code]

## 

​

Lifecycle Scripts

Bun blocks dependency lifecycle scripts unless explicitly trusted. For this repo, the commonly blocked scripts are not required:

  * `@whiskeysockets/baileys` `preinstall` — checks Node major >= 20 (OpenClaw defaults to Node 24 and still supports Node 22 LTS, currently `22.16+`)
  * `protobufjs` `postinstall` — emits warnings about incompatible version schemes (no build artifacts)

If you hit a runtime issue that requires these scripts, trust them explicitly:

Copy
[code]
    bun pm trust @whiskeysockets/baileys protobufjs
    
[/code]

## 

​

Caveats

Some scripts still hardcode pnpm (for example `docs:build`, `ui:*`, `protocol:check`). Run those via pnpm for now.

[Ansible](</install/ansible>)[Docker](</install/docker>)

⌘I
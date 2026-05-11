---
title: ClawHub
source_url: https://docs.openclaw.ai/clawhub
scraped_at: 2026-05-11
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Overview

ClawHub

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

# 

​

ClawHub

ClawHub is the public registry for OpenClaw skills and plugins.

  * Use native `openclaw` commands to search, install, and update skills and to install plugins from ClawHub.
  * Use the separate `clawhub` CLI for registry auth, publishing, delete/undelete, rescans, and sync workflows.

Site: [clawhub.ai](<https://clawhub.ai>)

## 

​

Quick start

Search and install skills with OpenClaw:
[code] 
    openclaw skills search "calendar"
    openclaw skills install <skill-slug>
    openclaw skills update --all
    
[/code]

Search and install plugins with OpenClaw:
[code] 
    openclaw plugins search "calendar"
    openclaw plugins install clawhub:<package>
    openclaw plugins update --all
    
[/code]

Install the ClawHub CLI when you want registry-authenticated workflows such as publish, sync, delete/undelete, or owner-requested rescans:
[code] 
    npm i -g clawhub
    # or
    pnpm add -g clawhub
    
[/code]

## 

​

What ClawHub hosts

Surface| What it stores| Typical command  
---|---|---  
Skills| Versioned text bundles with `SKILL.md` plus supporting files| `openclaw skills install <slug>`  
Code plugins| OpenClaw plugin packages with compatibility metadata| `openclaw plugins install clawhub:<package>`  
Bundle plugins| Packaged plugin bundles for OpenClaw distribution| `clawhub package publish <source>`  
Souls| `SOUL.md` bundles shown on onlycrabs.ai| Web and API publish flows  
  
ClawHub tracks semver versions, tags such as `latest`, changelogs, files, downloads, stars, and security scan summaries. Public pages show current registry state so users can inspect a skill or plugin before installing it.

## 

​

Native OpenClaw flows

Native OpenClaw commands install into the active OpenClaw workspace and persist source metadata so later update commands can stay on ClawHub. Use `clawhub:<package>` when a plugin install should resolve through ClawHub. Bare npm-safe plugin specs may resolve through npm during launch cutovers, and `npm:<package>` stays npm-only when a source must be explicit. Plugin installs validate advertised `pluginApi` and `minGatewayVersion` compatibility before archive install runs. When a package version publishes a ClawPack artifact, OpenClaw prefers the exact uploaded npm-pack `.tgz`, verifies the ClawHub digest header and downloaded bytes, and records artifact metadata for later updates.

## 

​

ClawHub CLI

The ClawHub CLI is for registry-authenticated work:
[code] 
    clawhub login
    clawhub whoami
    clawhub search "postgres backups"
    clawhub skill publish ./my-skill --slug my-skill --name "My Skill" --version 1.0.0
    clawhub package explore --family code-plugin
    clawhub package inspect episodic-claw
    clawhub package publish your-org/your-plugin --dry-run
    clawhub package publish your-org/your-plugin
    clawhub sync --all
    
[/code]

The CLI also has skill install/update commands for direct registry workflows:
[code] 
    clawhub install <slug>
    clawhub update <slug>
    clawhub update --all
    clawhub list
    
[/code]

Those commands install skills into `./skills` under the current working directory and record installed versions in `.clawhub/lock.json`.

## 

​

Publishing

Publish skills from a local folder containing `SKILL.md`:
[code] 
    clawhub skill publish <path>
    
[/code]

Common publish options:

  * `--slug <slug>`: skill slug.
  * `--name <name>`: display name.
  * `--version <version>`: semver version.
  * `--changelog <text>`: changelog text.
  * `--tags <tags>`: comma-separated tags, defaulting to `latest`.

Publish plugins from a local folder, `owner/repo`, `owner/repo@ref`, or a GitHub URL:
[code] 
    clawhub package publish <source>
    
[/code]

Use `--dry-run` to build the exact publish plan without uploading, and `--json` for CI-friendly output. Code plugins must include the required OpenClaw compatibility metadata in `package.json`, including `openclaw.compat.pluginApi` and `openclaw.build.openclawVersion`. See [CLI](</clawhub/cli>) for the full command reference and [Skill format](</clawhub/skill-format>) for skill metadata.

## 

​

Security and moderation

ClawHub is open by default: anyone can upload, but publishing requires a GitHub account old enough to pass the upload gate. Public detail pages summarize the latest scan state before install or download. ClawHub runs automated checks on published skills and plugin releases. Scan-held or blocked releases may disappear from public catalog and install surfaces while remaining visible to their owner in `/dashboard`. Owners can request limited rescans for false-positive recovery. Platform moderators and admins can request rescans for any skill or package when handling support reports:
[code] 
    clawhub skill rescan <slug>
    clawhub package rescan <name>
    
[/code]

Signed-in users can report skills and packages. Moderators can review reports, hide or restore content, resolve appeals, and ban abusive accounts. See [Acceptable usage](</clawhub/acceptable-usage>) and [Security + moderation](</clawhub/security>) for policy and enforcement details.

## 

​

Telemetry and environment

When you run `clawhub sync` while logged in, the CLI sends a minimal snapshot so ClawHub can compute install counts. Disable this with:
[code] 
    export CLAWHUB_DISABLE_TELEMETRY=1
    
[/code]

Useful environment overrides:

Variable| Effect  
---|---  
`CLAWHUB_SITE`| Override the site URL used for browser login.  
`CLAWHUB_REGISTRY`| Override the registry API URL.  
`CLAWHUB_CONFIG_PATH`| Override where the CLI stores token/config state.  
`CLAWHUB_WORKDIR`| Override the default working directory.  
`CLAWHUB_DISABLE_TELEMETRY=1`| Disable telemetry on `sync`.  
  
See [Telemetry](</clawhub/telemetry>), [HTTP API](</clawhub/http-api>), and [Troubleshooting](</clawhub/troubleshooting>) for deeper reference material.

[Quickstart](</clawhub/quickstart>)

⌘I
---
title: Quickstart
source_url: https://docs.openclaw.ai/clawhub/quickstart
scraped_at: 2026-05-11
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

# 

​

Quickstart

ClawHub is a registry for OpenClaw skills and plugins. Use OpenClaw when you are installing things into OpenClaw. Use the `clawhub` CLI when you are signing in, publishing, managing your own listings, or using registry-specific workflows.

## 

​

Find and install a skill

Search from OpenClaw:
[code] 
    openclaw skills search "calendar"
    
[/code]

Install a skill:
[code] 
    openclaw skills install <skill-slug>
    
[/code]

Update installed skills:
[code] 
    openclaw skills update --all
    
[/code]

OpenClaw records where the skill came from so later updates can continue to resolve through ClawHub.

## 

​

Find and install a plugin

Search from OpenClaw:
[code] 
    openclaw plugins search "calendar"
    
[/code]

Install a ClawHub-hosted plugin with an explicit ClawHub source:
[code] 
    openclaw plugins install clawhub:<package>
    
[/code]

Update installed plugins:
[code] 
    openclaw plugins update --all
    
[/code]

Use the `clawhub:` prefix when you want OpenClaw to resolve the package through ClawHub rather than npm or another source.

## 

​

Sign in for publishing

Install the ClawHub CLI:
[code] 
    npm i -g clawhub
    # or
    pnpm add -g clawhub
    
[/code]

Sign in with GitHub:
[code] 
    clawhub login
    clawhub whoami
    
[/code]

Headless environments can use an API token from the ClawHub web UI:
[code] 
    clawhub login --token clh_...
    
[/code]

## 

​

Publish a skill

A skill is a folder with a required `SKILL.md` file and optional supporting files.
[code] 
    clawhub skill publish ./my-skill \
      --slug my-skill \
      --name "My Skill" \
      --version 1.0.0 \
      --changelog "Initial release"
    
[/code]

Before publishing, check the metadata in `SKILL.md`. Declare required environment variables, tools, and permissions so users can understand what the skill needs before they install it. See [Skill format](</clawhub/skill-format>).

## 

​

Publish a plugin

Publish a plugin from a local folder, a GitHub repo, a GitHub ref, or an existing archive:
[code] 
    clawhub package publish <source> --family code-plugin --dry-run
    clawhub package publish <source> --family code-plugin
    
[/code]

Use `--dry-run` first to preview the resolved package metadata, compatibility fields, source attribution, and upload plan without publishing. Code plugins must include OpenClaw compatibility metadata in `package.json`, including `openclaw.compat.pluginApi` and `openclaw.build.openclawVersion`.

## 

​

Sync skills you maintain

`sync` scans skill folders and publishes new or changed skills that are not already synchronized.
[code] 
    clawhub sync --all --dry-run
    clawhub sync --all
    
[/code]

When you are signed in, `sync` may also send a minimal install snapshot for aggregate install counts. See [Telemetry](</clawhub/telemetry>) for what is reported and how to opt out.

## 

​

Inspect before installing

Before installing, use the ClawHub web page or CLI detail commands to inspect metadata, source links, versions, changelogs, and scan status:
[code] 
    clawhub inspect <skill-slug>
    clawhub package inspect <package>
    
[/code]

Public listings show the latest scan state. Releases that are held or blocked by moderation may be hidden from search and install surfaces until resolved.

[ClawHub](</clawhub>)[How it works](</clawhub/how-it-works>)

⌘I
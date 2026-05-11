---
title: Auth
source_url: https://docs.openclaw.ai/clawhub/auth
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

Auth

ClawHub uses GitHub for web sign-in. The CLI uses ClawHub API tokens created through that signed-in account.

## 

​

Web sign-in

Use GitHub to sign in at [clawhub.ai](<https://clawhub.ai>). Deleted, banned, or disabled accounts cannot complete normal ClawHub sign-in. If sign-in returns you to a logged-out state, your account may not be in good standing.

## 

​

CLI login

The default CLI login flow opens your browser:
[code] 
    clawhub login
    clawhub whoami
    
[/code]

What happens:

  1. The CLI starts a temporary callback server on `127.0.0.1`.
  2. Your browser opens the ClawHub sign-in page.
  3. After GitHub sign-in, ClawHub creates an API token.
  4. The browser redirects back to the local callback.
  5. The CLI stores the token in your ClawHub config file.

If your browser cannot reach the local callback because of firewall, VPN, or proxy rules, use the headless token flow.

## 

​

Headless login

Create a token in the ClawHub web UI, then pass it to the CLI:
[code] 
    clawhub login --token clh_...
    
[/code]

Use this flow for servers, CI jobs, or terminal-only environments. For remote shells where you can open a browser elsewhere, run:
[code] 
    clawhub login --device
    
[/code]

The CLI prints a one-time code and waits while you authorize it at `https://clawhub.ai/cli/device`.

## 

​

Token storage

Default config paths:

  * macOS: `~/Library/Application Support/clawhub/config.json`
  * Linux/XDG: `$XDG_CONFIG_HOME/clawhub/config.json` or `~/.config/clawhub/config.json`
  * Windows: `%APPDATA%\\clawhub\\config.json`

Override the path with:
[code] 
    export CLAWHUB_CONFIG_PATH=/path/to/config.json
    
[/code]

## 

​

Revocation

You can revoke API tokens in the ClawHub web UI. Revoked, invalid, or missing tokens return `401 Unauthorized`. Sign in again with `clawhub login` or provide a fresh token with `clawhub login --token`. Deleted, banned, or disabled accounts cannot continue using existing API tokens.

[Soul format](</clawhub/soul-format>)[Telemetry](</clawhub/telemetry>)

⌘I
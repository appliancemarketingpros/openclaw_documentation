---
title: ClawDock
source_url: https://docs.openclaw.ai/install/clawdock
scraped_at: 2026-03-30
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Containers

ClawDock

# 

​

ClawDock

ClawDock is a small shell-helper layer for Docker-based OpenClaw installs. It gives you short commands like `clawdock-start`, `clawdock-dashboard`, and `clawdock-fix-token` instead of longer `docker compose ...` invocations. If you have not set up Docker yet, start with [Docker](</install/docker>).

## 

​

Install

Use the canonical helper path:
[code] 
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.sh
    echo 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
    
[/code]

If you previously installed ClawDock from `scripts/shell-helpers/clawdock-helpers.sh`, reinstall from the new `scripts/clawdock/clawdock-helpers.sh` path. The old raw GitHub path was removed.

## 

​

What you get

### 

​

Basic operations

Command| Description  
---|---  
`clawdock-start`| Start the gateway  
`clawdock-stop`| Stop the gateway  
`clawdock-restart`| Restart the gateway  
`clawdock-status`| Check container status  
`clawdock-logs`| Follow gateway logs  
  
### 

​

Container access

Command| Description  
---|---  
`clawdock-shell`| Open a shell inside the gateway container  
`clawdock-cli <command>`| Run OpenClaw CLI commands in Docker  
`clawdock-exec <command>`| Execute an arbitrary command in the container  
  
### 

​

Web UI and pairing

Command| Description  
---|---  
`clawdock-dashboard`| Open the Control UI URL  
`clawdock-devices`| List pending device pairings  
`clawdock-approve <id>`| Approve a pairing request  
  
### 

​

Setup and maintenance

Command| Description  
---|---  
`clawdock-fix-token`| Configure the gateway token inside the container  
`clawdock-update`| Pull, rebuild, and restart  
`clawdock-rebuild`| Rebuild the Docker image only  
`clawdock-clean`| Remove containers and volumes  
  
### 

​

Utilities

Command| Description  
---|---  
`clawdock-health`| Run a gateway health check  
`clawdock-token`| Print the gateway token  
`clawdock-cd`| Jump to the OpenClaw project directory  
`clawdock-config`| Open `~/.openclaw`  
`clawdock-show-config`| Print config files with redacted values  
`clawdock-workspace`| Open the workspace directory  
  
## 

​

First-time flow
[code] 
    clawdock-start
    clawdock-fix-token
    clawdock-dashboard
    
[/code]

If the browser says pairing is required:
[code] 
    clawdock-devices
    clawdock-approve <request-id>
    
[/code]

## 

​

Config and secrets

ClawDock works with the same Docker config split described in [Docker](</install/docker>):

  * `<project>/.env` for Docker-specific values like image name, ports, and the gateway token
  * `~/.openclaw/.env` for provider keys and bot tokens
  * `~/.openclaw/openclaw.json` for behavior config

Use `clawdock-show-config` when you want to inspect those files quickly. It redacts `.env` values in its printed output.

## 

​

Related pages

  * [Docker](</install/docker>)
  * [Docker VM Runtime](</install/docker-vm-runtime>)
  * [Updating](</install/updating>)


[Bun (Experimental)](</install/bun>)[Docker](</install/docker>)

⌘I
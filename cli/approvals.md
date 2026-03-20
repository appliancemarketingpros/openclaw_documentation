---
title: approvals
source_url: https://docs.openclaw.ai/cli/approvals
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools and execution

approvals

# 

​

`openclaw approvals`

Manage exec approvals for the **local host** , **gateway host** , or a **node host**. By default, commands target the local approvals file on disk. Use `--gateway` to target the gateway, or `--node` to target a specific node. Related:

  * Exec approvals: [Exec approvals](</tools/exec-approvals>)
  * Nodes: [Nodes](</nodes>)


## 

​

Common commands

Copy
[code]
    openclaw approvals get
    openclaw approvals get --node <id|name|ip>
    openclaw approvals get --gateway
    
[/code]

## 

​

Replace approvals from a file

Copy
[code]
    openclaw approvals set --file ./exec-approvals.json
    openclaw approvals set --node <id|name|ip> --file ./exec-approvals.json
    openclaw approvals set --gateway --file ./exec-approvals.json
    
[/code]

## 

​

Allowlist helpers

Copy
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"
    openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"
    openclaw approvals allowlist add --agent "*" "/usr/bin/uname"
    
    openclaw approvals allowlist remove "~/Projects/**/bin/rg"
    
[/code]

## 

​

Notes

  * `--node` uses the same resolver as `openclaw nodes` (id, name, ip, or id prefix).
  * `--agent` defaults to `"*"`, which applies to all agents.
  * The node host must advertise `system.execApprovals.get/set` (macOS app or headless node host).
  * Approvals files are stored per host at `~/.openclaw/exec-approvals.json`.


[voicecall](</cli/voicecall>)[browser](</cli/browser>)

⌘I
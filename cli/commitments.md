---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/cli/commitments
scraped_at: 2026-05-04
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Agents and sessions

`openclaw commitments`

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

List and manage inferred follow-up commitments. Commitments are opt-in, short-lived follow-up memories created from conversation context. See [Inferred commitments](</concepts/commitments>) for the conceptual guide. With no subcommand, `openclaw commitments` lists pending commitments.

## 

​

Usage
[code] 
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]
    openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]
    openclaw commitments dismiss <id...> [--json]
    
[/code]

## 

​

Options

  * `--all`: show all statuses instead of only pending commitments.
  * `--agent <id>`: filter to one agent id.
  * `--status <status>`: filter by status. Values: `pending`, `sent`, `dismissed`, `snoozed`, or `expired`.
  * `--json`: output machine-readable JSON.


## 

​

Examples

List pending commitments:
[code] 
    openclaw commitments
    
[/code]

List every stored commitment:
[code] 
    openclaw commitments --all
    
[/code]

Filter to one agent:
[code] 
    openclaw commitments --agent main
    
[/code]

Find snoozed commitments:
[code] 
    openclaw commitments --status snoozed
    
[/code]

Dismiss one or more commitments:
[code] 
    openclaw commitments dismiss cm_abc123 cm_def456
    
[/code]

Export as JSON:
[code] 
    openclaw commitments --all --json
    
[/code]

## 

​

Output

Text output includes:

  * commitment id
  * status
  * kind
  * earliest due time
  * scope
  * suggested check-in text

JSON output also includes the commitment store path and full stored records.

## 

​

Related

  * [Inferred commitments](</concepts/commitments>)
  * [Memory overview](</concepts/memory>)
  * [Heartbeat](</gateway/heartbeat>)
  * [Scheduled tasks](</automation/cron-jobs>)


[Memory](</cli/memory>)[Message](</cli/message>)

⌘I
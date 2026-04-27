---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/cli/tasks
scraped_at: 2026-04-27
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Agents and sessions

`openclaw tasks`

Inspect durable background tasks and Task Flow state. With no subcommand, `openclaw tasks` is equivalent to `openclaw tasks list`. See [Background Tasks](</automation/tasks>) for the lifecycle and delivery model.

## 

​

Usage
[code] 
    openclaw tasks
    openclaw tasks list
    openclaw tasks list --runtime acp
    openclaw tasks list --status running
    openclaw tasks show <lookup>
    openclaw tasks notify <lookup> state_changes
    openclaw tasks cancel <lookup>
    openclaw tasks audit
    openclaw tasks maintenance
    openclaw tasks maintenance --apply
    openclaw tasks flow list
    openclaw tasks flow show <lookup>
    openclaw tasks flow cancel <lookup>
    
[/code]

## 

​

Root Options

  * `--json`: output JSON.
  * `--runtime <name>`: filter by kind: `subagent`, `acp`, `cron`, or `cli`.
  * `--status <name>`: filter by status: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled`, or `lost`.


## 

​

Subcommands

### 

​

`list`
[code] 
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
    
[/code]

Lists tracked background tasks newest first.

### 

​

`show`
[code] 
    openclaw tasks show <lookup> [--json]
    
[/code]

Shows one task by task ID, run ID, or session key.

### 

​

`notify`
[code] 
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
    
[/code]

Changes the notification policy for a running task.

### 

​

`cancel`
[code] 
    openclaw tasks cancel <lookup>
    
[/code]

Cancels a running background task.

### 

​

`audit`
[code] 
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
    
[/code]

Surfaces stale, lost, delivery-failed, or otherwise inconsistent task and Task Flow records. Lost tasks retained until `cleanupAfter` are warnings; expired or unstamped lost tasks are errors.

### 

​

`maintenance`
[code] 
    openclaw tasks maintenance [--apply] [--json]
    
[/code]

Previews or applies task and Task Flow reconciliation, cleanup stamping, and pruning. For cron tasks, reconciliation uses persisted run logs/job state before marking an old active task `lost`, so completed cron runs do not become false audit errors just because the in-memory Gateway runtime state is gone. Offline CLI audit is not authoritative for the Gateway’s process-local cron active-job set.

### 

​

`flow`
[code] 
    openclaw tasks flow list [--status <name>] [--json]
    openclaw tasks flow show <lookup> [--json]
    openclaw tasks flow cancel <lookup>
    
[/code]

Inspects or cancels durable Task Flow state under the task ledger.

## 

​

Related

  * [CLI reference](</cli>)
  * [Background tasks](</automation/tasks>)


[System](</cli/system>)[Channels](</cli/channels>)

⌘I
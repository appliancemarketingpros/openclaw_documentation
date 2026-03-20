---
title: cron
source_url: https://docs.openclaw.ai/cli/cron
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

cron

# 

​

`openclaw cron`

Manage cron jobs for the Gateway scheduler. Related:

  * Cron jobs: [Cron jobs](</automation/cron-jobs>)

Tip: run `openclaw cron --help` for the full command surface. Note: isolated `cron add` jobs default to `--announce` delivery. Use `--no-deliver` to keep output internal. `--deliver` remains as a deprecated alias for `--announce`. Note: one-shot (`--at`) jobs delete after success by default. Use `--keep-after-run` to keep them. Note: recurring jobs now use exponential retry backoff after consecutive errors (30s → 1m → 5m → 15m → 60m), then return to normal schedule after the next successful run. Note: `openclaw cron run` now returns as soon as the manual run is queued for execution. Successful responses include `{ ok: true, enqueued: true, runId }`; use `openclaw cron runs --id <job-id>` to follow the eventual outcome. Note: retention/pruning is controlled in config:

  * `cron.sessionRetention` (default `24h`) prunes completed isolated run sessions.
  * `cron.runLog.maxBytes` \+ `cron.runLog.keepLines` prune `~/.openclaw/cron/runs/<jobId>.jsonl`.

Upgrade note: if you have older cron jobs from before the current delivery/store format, run `openclaw doctor --fix`. Doctor now normalizes legacy cron fields (`jobId`, `schedule.cron`, top-level delivery fields, payload `provider` delivery aliases) and migrates simple `notify: true` webhook fallback jobs to explicit webhook delivery when `cron.webhook` is configured.

## 

​

Common edits

Update delivery settings without changing the message:

Copy
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
    
[/code]

Disable delivery for an isolated job:

Copy
[code]
    openclaw cron edit <job-id> --no-deliver
    
[/code]

Enable lightweight bootstrap context for an isolated job:

Copy
[code]
    openclaw cron edit <job-id> --light-context
    
[/code]

Announce to a specific channel:

Copy
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
    
[/code]

Create an isolated job with lightweight bootstrap context:

Copy
[code]
    openclaw cron add \
      --name "Lightweight morning brief" \
      --cron "0 7 * * *" \
      --session isolated \
      --message "Summarize overnight updates." \
      --light-context \
      --no-deliver
    
[/code]

`--light-context` applies to isolated agent-turn jobs only. For cron runs, lightweight mode keeps bootstrap context empty instead of injecting the full workspace bootstrap set.

[browser](</cli/browser>)[node](</cli/node>)

⌘I
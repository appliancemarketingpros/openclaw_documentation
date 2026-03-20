---
title: Scripts
source_url: https://docs.openclaw.ai/help/scripts
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

Scripts

# 

​

Scripts

The `scripts/` directory contains helper scripts for local workflows and ops tasks. Use these when a task is clearly tied to a script; otherwise prefer the CLI.

## 

​

Conventions

  * Scripts are **optional** unless referenced in docs or release checklists.
  * Prefer CLI surfaces when they exist (example: auth monitoring uses `openclaw models status --check`).
  * Assume scripts are host‑specific; read them before running on a new machine.


## 

​

Auth monitoring scripts

Auth monitoring scripts are documented here: [/automation/auth-monitoring](</automation/auth-monitoring>)

## 

​

When adding scripts

  * Keep scripts focused and documented.
  * Add a short entry in the relevant doc (or create one if missing).


[Testing](</help/testing>)[Node + tsx Crash](</debug/node-issue>)

⌘I
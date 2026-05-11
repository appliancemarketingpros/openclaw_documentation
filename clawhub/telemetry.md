---
title: Telemetry
source_url: https://docs.openclaw.ai/clawhub/telemetry
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

Telemetry

ClawHub uses **minimal telemetry** to compute **install counts** (what’s actually in use) and to power better sorting/filtering. This is based on the CLI `clawhub sync` command.

## 

​

When telemetry is collected

Telemetry is only sent when:

  * You are **logged in** in the CLI (we already require auth for sync/publish flows).
  * You run `clawhub sync`.
  * Telemetry is **not disabled** (see “How to disable” below).

If you are not logged in, nothing is reported.

## 

​

What we collect

On each `clawhub sync`, the CLI reports a **full snapshot** of what it found, grouped by scan root (“folder/root”). For each root we store:

  * `rootId`: a **SHA-256 hash** of the canonical root path (server never sees the raw path).
  * `label`: a human-readable label derived from the last two path segments (home paths are shown with `~`).
  * `firstSeenAt`, `lastSeenAt`, optional `expiredAt`.

For each skill found under a root we store:

  * `skillId` (resolved by slug; only skills that exist in the registry are tracked).
  * `firstSeenAt`, `lastSeenAt`.
  * `lastVersion` (best-effort; currently the registry-matched version if known).
  * optional `removedAt` when a previously-reported install disappears from a root.


### 

​

What we do _not_ collect

  * No raw absolute folder paths (only hashed `rootId` \+ a short display label).
  * No file contents.
  * No per-run logs, prompts, or other CLI output.
  * No tracking for skills that aren’t uploaded to the registry (unknown slugs are ignored).


## 

​

Install counts

We maintain two counters per skill:

  * `installsCurrent`: unique users who currently have the skill installed in at least one active root.
  * `installsAllTime`: unique users who have ever reported the skill installed.


### 

​

Multiple roots

If you sync from multiple folders, we treat each scan root independently. A skill is “currently installed” if it exists in **any** active root.

### 

​

Uninstall detection

Because `sync` reports the full set per root:

  * If a skill disappears from a root on the next sync, we mark it removed for that root.
  * If the skill is removed from all of your roots, it no longer counts toward `installsCurrent`.
  * `installsAllTime` never decreases unless you delete telemetry (see below).


### 

​

Staleness (120 days)

Roots that don’t report telemetry for **120 days** are marked stale and their installs stop counting toward `installsCurrent`. This is evaluated lazily (on the next telemetry report) to avoid background jobs.

## 

​

Transparency + user controls

ClawHub provides a private “Installed” tab on your own profile:

  * Shows the exact roots + installed skills we store.
  * Includes a **JSON export** view.
  * Includes a **Delete telemetry** action to remove all stored telemetry for your account.

Everyone else only sees **aggregated install counters** ; no one else can see your roots/folders. Deleting your account also deletes your telemetry data.

## 

​

How to disable telemetry

Set the environment variable:
[code] 
    export CLAWHUB_DISABLE_TELEMETRY=1
    
[/code]

With this set, the CLI will not send telemetry during `clawhub sync`.

[Auth](</clawhub/auth>)[Troubleshooting](</clawhub/troubleshooting>)

⌘I
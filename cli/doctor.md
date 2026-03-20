---
title: doctor
source_url: https://docs.openclaw.ai/cli/doctor
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Gateway and service

doctor

# 

​

`openclaw doctor`

Health checks + quick fixes for the gateway and channels. Related:

  * Troubleshooting: [Troubleshooting](</gateway/troubleshooting>)
  * Security audit: [Security](</gateway/security>)


## 

​

Examples

Copy
[code]
    openclaw doctor
    openclaw doctor --repair
    openclaw doctor --deep
    
[/code]

Notes:

  * Interactive prompts (like keychain/OAuth fixes) only run when stdin is a TTY and `--non-interactive` is **not** set. Headless runs (cron, Telegram, no terminal) will skip prompts.
  * `--fix` (alias for `--repair`) writes a backup to `~/.openclaw/openclaw.json.bak` and drops unknown config keys, listing each removal.
  * State integrity checks now detect orphan transcript files in the sessions directory and can archive them as `.deleted.<timestamp>` to reclaim space safely.
  * Doctor also scans `~/.openclaw/cron/jobs.json` (or `cron.store`) for legacy cron job shapes and can rewrite them in place before the scheduler has to auto-normalize them at runtime.
  * Doctor includes a memory-search readiness check and can recommend `openclaw configure --section model` when embedding credentials are missing.
  * If sandbox mode is enabled but Docker is unavailable, doctor reports a high-signal warning with remediation (`install Docker` or `openclaw config set agents.defaults.sandbox.mode off`).
  * If `gateway.auth.token`/`gateway.auth.password` are SecretRef-managed and unavailable in the current command path, doctor reports a read-only warning and does not write plaintext fallback credentials.
  * If channel SecretRef inspection fails in a fix path, doctor continues and reports a warning instead of exiting early.
  * Telegram `allowFrom` username auto-resolution (`doctor --fix`) requires a resolvable Telegram token in the current command path. If token inspection is unavailable, doctor reports a warning and skips auto-resolution for that pass.


## 

​

macOS: `launchctl` env overrides

If you previously ran `launchctl setenv OPENCLAW_GATEWAY_TOKEN ...` (or `...PASSWORD`), that value overrides your config file and can cause persistent “unauthorized” errors.

Copy
[code]
    launchctl getenv OPENCLAW_GATEWAY_TOKEN
    launchctl getenv OPENCLAW_GATEWAY_PASSWORD
    
    launchctl unsetenv OPENCLAW_GATEWAY_TOKEN
    launchctl unsetenv OPENCLAW_GATEWAY_PASSWORD
    
[/code]

[daemon](</cli/daemon>)[gateway](</cli/gateway>)

⌘I
---
title: agent
source_url: https://docs.openclaw.ai/cli/agent
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Agents and sessions

agent

# 

​

`openclaw agent`

Run an agent turn via the Gateway (use `--local` for embedded). Use `--agent <id>` to target a configured agent directly. Related:

  * Agent send tool: [Agent send](</tools/agent-send>)


## 

​

Examples

Copy
[code]
    openclaw agent --to +15555550123 --message "status update" --deliver
    openclaw agent --agent ops --message "Summarize logs"
    openclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium
    openclaw agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"
    
[/code]

## 

​

Notes

  * When this command triggers `models.json` regeneration, SecretRef-managed provider credentials are persisted as non-secret markers (for example env var names, `secretref-env:ENV_VAR_NAME`, or `secretref-managed`), not resolved secret plaintext.
  * Marker writes are source-authoritative: OpenClaw persists markers from the active source config snapshot, not from resolved runtime secret values.


[update](</cli/update>)[agents](</cli/agents>)

⌘I
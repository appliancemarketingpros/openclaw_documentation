---
title: Gateway protocol RPC methods
source_url: https://docs.openclaw.ai/gateway/protocol/rpc-methods
scraped_at: 2026-09-14
---

Gateway & OpsGateway

The gateway method surface, grouped into families, plus the session list bootstrap, the common event families, and the node helper and exec lifecycle contracts.

## RPC method families

`hello-ok.features.methods` is a conservative discovery list built from `src/gateway/server-methods-list.ts` plus loaded plugin/channel method exports — it is not a generated dump of every method, and some methods (for example `push.test`, `web.login.start`, `web.login.wait`, `sessions.usage`) are intentionally excluded from discovery even though they are real, callable methods. Treat this as feature discovery, not a full enumeration of `src/gateway/server-methods/*.ts`.

## What each page covers

  * [System and channel methods](</gateway/protocol/rpc-system-and-channels>) — system and identity, models and usage, channels and login helpers, plugin management, messaging and logs, and the operator terminal.
  * [Talk, config, and agent methods](</gateway/protocol/rpc-talk-config-and-agents>) — Talk and TTS, secrets, config, update, and wizard, and agent and workspace helpers.
  * [Session control](</gateway/protocol/rpc-session-control>) — the session control family: listing, sending, streaming, run lifecycle, and session maintenance.
  * [Devices, nodes, and approvals](</gateway/protocol/rpc-devices-nodes-and-approvals>) — device pairing and device tokens, node pairing and invoke, approval families, Control UI commands, and automation, skills, and tools.
  * [Session list bootstrap and events](</gateway/protocol/rpc-bootstrap-and-events>) — the session list bootstrap, the common event families, and the node helper and exec lifecycle contracts.


## Where each section moved

Every section heading from the previous single-page version keeps its anchor here, so an existing link to this page with a fragment still resolves. Each entry points at the page that now holds the content.

  * [System and identity](</gateway/protocol/rpc-system-and-channels#system-and-identity>)
  * [Models and usage](</gateway/protocol/rpc-system-and-channels#models-and-usage>)
  * [Channels and login helpers](</gateway/protocol/rpc-system-and-channels#channels-and-login-helpers>)
  * [Plugin management](</gateway/protocol/rpc-system-and-channels#plugin-management>)
  * [Messaging and logs](</gateway/protocol/rpc-system-and-channels#messaging-and-logs>)
  * [Operator terminal](</gateway/protocol/rpc-system-and-channels#operator-terminal>)
  * [Talk and TTS](</gateway/protocol/rpc-talk-config-and-agents#talk-and-tts>)
  * [Secrets, config, update, and wizard](</gateway/protocol/rpc-talk-config-and-agents#secrets%2C-config%2C-update%2C-and-wizard>)
  * [Secrets, config, update, and wizard](</gateway/protocol/rpc-talk-config-and-agents#secrets-config-update-and-wizard>)
  * [Agent and workspace helpers](</gateway/protocol/rpc-talk-config-and-agents#agent-and-workspace-helpers>)
  * [Session control](</gateway/protocol/rpc-session-control#session-control>)
  * [Device pairing and device tokens](</gateway/protocol/rpc-devices-nodes-and-approvals#device-pairing-and-device-tokens>)
  * [Node pairing, invoke, and pending work](</gateway/protocol/rpc-devices-nodes-and-approvals#node-pairing%2C-invoke%2C-and-pending-work>)
  * [Node pairing, invoke, and pending work](</gateway/protocol/rpc-devices-nodes-and-approvals#node-pairing-invoke-and-pending-work>)
  * [Approval families](</gateway/protocol/rpc-devices-nodes-and-approvals#approval-families>)
  * [Control UI commands](</gateway/protocol/rpc-devices-nodes-and-approvals#control-ui-commands>)
  * [Automation, skills, and tools](</gateway/protocol/rpc-devices-nodes-and-approvals#automation%2C-skills%2C-and-tools>)
  * [Automation, skills, and tools](</gateway/protocol/rpc-devices-nodes-and-approvals#automation-skills-and-tools>)
  * [Session list bootstrap](</gateway/protocol/rpc-bootstrap-and-events#session-list-bootstrap>)
  * [Common event families](</gateway/protocol/rpc-bootstrap-and-events#common-event-families>)
  * [Node helper methods](</gateway/protocol/rpc-bootstrap-and-events#node-helper-methods>)
  * [Node exec lifecycle events](</gateway/protocol/rpc-bootstrap-and-events#node-exec-lifecycle-events>)


Was this useful?YesNo

Open issue
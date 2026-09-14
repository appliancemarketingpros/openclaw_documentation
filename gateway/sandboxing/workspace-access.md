---
title: Workspace access
source_url: https://docs.openclaw.ai/gateway/sandboxing/workspace-access
scraped_at: 2026-09-14
---

Gateway & OpsGateway

What `workspaceAccess` exposes to the sandbox, how a role-required sandbox caps it, and how skills are mirrored into the sandbox workspace.

## Workspace access

`agents.defaults.sandbox.workspaceAccess` controls what the sandbox can see:

Value | Behavior  
---|---  
`none` (default) | Tools can read and write an isolated sandbox workspace under `~/.openclaw/sandboxes`; the agent workspace is not exposed.  
`ro` | Mounts the agent workspace read-only at `/agent` (disables `write`/`edit`/`apply_patch`).  
`rw` | Mounts the agent workspace read/write at `/workspace`.  
  
For a role-required sandbox, OpenClaw caps configured `rw` workspace access at `ro` and logs an `agent/sandbox` warning. The guest keeps a separate sandbox workspace, while the shared agent workspace is available only as a read-only mount. This prevents guests from sharing the writable agent workspace; `none` and `ro` remain unchanged. Sessions without a role-required sandbox retain their configured workspace access.

With the OpenShell backend, `mirror` mode still uses the local workspace as the canonical source between exec turns, and `remote` mode uses the remote OpenShell workspace as canonical after the initial seed. The same access rules apply: `none` permits private workspace writes, while `ro` disables writes.

Inbound media is copied into the active sandbox workspace (`media/inbound/*`).

Was this useful?YesNo

Open issue
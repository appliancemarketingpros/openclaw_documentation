---
title: Multiple folders for one agent
source_url: https://docs.openclaw.ai/gateway/sandboxing/multiple-folders-for-one-agent
scraped_at: 2026-09-14
---

Gateway & OpsGateway

Giving a sandboxed agent extra host folders through bind mounts, how bind modes relate to workspace access, and the sources OpenClaw blocks by default.

## Multiple folders for one agent

Use Docker bind mounts when one sandboxed agent needs more than its primary workspace. Each entry maps a host folder to a container path with an explicit access mode:

textCopy code
[code]
    host-directory:container-directory:rohost-directory:container-directory:rw
[/code]

  * `ro` makes the mounted folder read-only inside the sandbox.
  * `rw` lets sandboxed tools and processes change the host folder.
  * The container path is the path the agent uses. Host paths are not exposed automatically.


This example gives the `research` agent a writable primary workspace, read-only reference material at `/reference`, and a separate writable output folder at `/drafts`:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        scope: "agent",      },    },    entries: {      research: {        default: true,        workspace: "/srv/openclaw/research-workspace",        sandbox: {          workspaceAccess: "rw",          docker: {            binds: ["/srv/shared/reference:/reference:ro", "/srv/shared/drafts:/drafts:rw"],            // Required because these sources are outside the agent workspace.            dangerouslyAllowExternalBindSources: true,          },        },      },    },  },}
[/code]

`workspaceAccess` and bind modes are independent:

Setting | Controls  
---|---  
`workspaceAccess: "none"` | Uses a writable isolated sandbox workspace; does not expose the agent workspace.  
`workspaceAccess: "ro"` | Mounts the agent workspace read-only at `/agent`.  
`workspaceAccess: "rw"` | Mounts the agent workspace read/write at `/workspace`.  
`docker.binds` entry `:ro`/`:rw` | Controls only that additional host folder at its configured container path.  
  
Changing `workspaceAccess` does not change an additional bind from `ro` to `rw`, or vice versa. Global and per-agent `docker.binds` are merged. Keep `scope: "agent"` or `"session"` for per-agent binds; `scope: "shared"` ignores all per-agent Docker overrides and uses only global binds.

Bind mounts are the supported multi-folder boundary because Docker constructs the container's filesystem view with mount isolation, and the `ro`/`rw` mode applies to every process in the sandbox. That boundary covers `exec`, filesystem tools, child processes, and libraries without duplicating path-authorization checks across each OpenClaw code path. A host-side path allowlist cannot provide the same complete boundary when an allowed shell or dependency can access files directly.

The opt-in `dangerouslyAllowExternalBindSources` only permits sources outside the workspace roots. It does not disable OpenClaw's blocked system, credential, Docker socket, symlink-parent, or reserved-target checks. Prefer the smallest folder, use `ro` unless writes are required, and recreate the sandbox after changing mounts:

bashCopy code
[code]
    openclaw sandbox recreate --agent research
[/code]

### Other bind behavior

`agents.defaults.sandbox.docker.binds` configures global mounts. The format is the same `host:container:mode` form (for example, `"/home/user/source:/source:rw"`).

`agents.defaults.sandbox.browser.binds` mounts additional host directories into the **sandbox browser** container only. When set (including `[]`), it replaces `docker.binds` for the browser container; when omitted, the browser container falls back to `docker.binds`.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    entries: {      build: {        default: true,        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    },  },}
[/code]

Was this useful?YesNo

Open issue
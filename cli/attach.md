---
title: Attach CLI
source_url: https://docs.openclaw.ai/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` launches Claude Code with a strict temporary MCP config bound to one Gateway session.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Options:

  * `--session <key>` binds the grant to a Gateway session. Defaults to the main session.
  * `--ttl <ms>` requests a positive grant TTL in milliseconds. The Gateway applies its own ceiling.
  * `--bin <path>` selects the Claude Code binary. Default: `claude`.
  * `--print-config` writes the temporary `.mcp.json`, prints the launch command and env, and leaves the grant live until TTL expiry (it does not spawn Claude Code or revoke the grant).


The bearer token is passed through environment variables, not argv. OpenClaw launches Claude Code with `--strict-mcp-config --mcp-config <path>` so ambient Claude MCP servers do not join the attached session. Normal launches (without `--print-config`) revoke the grant when the Claude Code process exits.

See also: [Gateway CLI](</cli/gateway>), [MCP CLI](</cli/mcp>), and [ACP CLI](</cli/acp>).

Was this useful?YesNo

Open issue
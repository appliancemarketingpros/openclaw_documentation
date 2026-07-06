---
title: CLI koppelen
source_url: https://docs.openclaw.ai/nl/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` start Claude Code met een strikte tijdelijke MCP-configuratie die aan één Gateway-sessie is gebonden.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Opties:

  * `--session <key>` bindt de toekenning aan een Gateway-sessie. Standaard is dit de hoofdsessie.
  * `--ttl <ms>` vraagt een positieve TTL voor de toekenning aan in milliseconden. De Gateway past zijn eigen bovengrens toe.
  * `--bin <path>` selecteert het Claude Code-binaire bestand. Standaard is `claude`.
  * `--print-config` schrijft de tijdelijke `.mcp.json`, drukt de startopdracht en env af, en laat de toekenning actief tot de TTL verloopt.


Het bearer-token wordt doorgegeven via omgevingsvariabelen, niet argv. OpenClaw start Claude Code met `--strict-mcp-config --mcp-config <path>`, zodat omgevingsgebonden Claude MCP-servers niet deelnemen aan de gekoppelde sessie. Normale starts trekken de toekenning in wanneer het Claude Code-proces afsluit.

Zie ook: [Gateway CLI](</nl/cli/gateway>), [MCP CLI](</nl/cli/mcp>) en [ACP CLI](</nl/cli/acp>).

Was this useful?YesNo

Open issue
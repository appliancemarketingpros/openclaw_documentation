---
title: CLI anhängen
source_url: https://docs.openclaw.ai/de/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` startet Claude Code mit einer strikt temporären MCP-Konfiguration, die an eine Gateway-Sitzung gebunden ist.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Optionen:

  * `--session <key>` bindet die Berechtigung an eine Gateway-Sitzung. Standardmäßig wird die Hauptsitzung verwendet.
  * `--ttl <ms>` fordert eine positive Berechtigungs-TTL in Millisekunden an. Der Gateway wendet seine eigene Obergrenze an.
  * `--bin <path>` wählt die Claude Code-Binärdatei aus. Standardwert ist `claude`.
  * `--print-config` schreibt die temporäre `.mcp.json`, gibt den Startbefehl und die Umgebung aus und lässt die Berechtigung bis zum Ablauf der TTL aktiv.


Das Bearer-Token wird über Umgebungsvariablen übergeben, nicht über argv. OpenClaw startet Claude Code mit `--strict-mcp-config --mcp-config <path>`, damit Claude-MCP-Server aus der Umgebung nicht der angehängten Sitzung beitreten. Normale Starts widerrufen die Berechtigung, wenn der Claude Code-Prozess beendet wird.

Siehe auch: [Gateway CLI](</de/cli/gateway>), [MCP CLI](</de/cli/mcp>) und [ACP CLI](</de/cli/acp>).

Was this useful?YesNo

Open issue
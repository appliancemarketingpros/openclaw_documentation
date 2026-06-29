---
title: Codex Supervisor-plugin
source_url: https://docs.openclaw.ai/nl/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor-Plugin

Beheer Codex app-server-sessies vanuit OpenClaw.

## Distributie

  * Pakket: `@openclaw/codex-supervisor`
  * Installatieroute: inbegrepen in OpenClaw


## Oppervlak

contracten: tools

## Sessielijst

`codex_sessions_list` gebruikt standaard alleen geladen Codex-sessies. Stel `include_stored` in om opgeslagen geschiedenis op te nemen; de plugin gebruikt het alleen-state-DB-lijstpad van Codex app-server en beperkt opgeslagen resultaten standaard tot 200. Geef `max_stored_sessions` door om die limiet te verlagen of te verhogen, tot maximaal 1000.

Was this useful?YesNo

Open issue
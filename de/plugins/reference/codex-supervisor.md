---
title: Codex-Supervisor-Plugin
source_url: https://docs.openclaw.ai/de/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor-Plugin

Überwachen Sie Codex App-Server-Sitzungen von OpenClaw aus.

## Distribution

  * Paket: `@openclaw/codex-supervisor`
  * Installationsweg: in OpenClaw enthalten


## Oberfläche

contracts: tools

## Sitzungsauflistung

`codex_sessions_list` ist standardmäßig nur auf geladene Codex-Sitzungen beschränkt. Setzen Sie `include_stored`, um gespeicherte Historie einzubeziehen; das Plugin verwendet den reinen State-DB-Auflistungspfad des Codex App-Servers und begrenzt gespeicherte Ergebnisse standardmäßig auf 200. Übergeben Sie `max_stored_sessions`, um diese Obergrenze zu senken oder bis auf 1000 anzuheben.

Was this useful?YesNo

Open issue
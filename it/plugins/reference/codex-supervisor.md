---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/it/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin supervisore Codex

Supervisiona le sessioni app-server di Codex da OpenClaw.

## Distribuzione

  * Pacchetto: `@openclaw/codex-supervisor`
  * Percorso di installazione: incluso in OpenClaw


## Superficie

contratti: strumenti

## Elenco delle sessioni

`codex_sessions_list` restituisce per impostazione predefinita solo le sessioni Codex caricate. Imposta `include_stored` per includere la cronologia archiviata; il Plugin usa il percorso di elenco solo state-DB dell'app-server Codex e limita per impostazione predefinita i risultati archiviati a 200. Passa `max_stored_sessions` per abbassare o aumentare quel limite, fino a 1000.

Was this useful?YesNo

Open issue
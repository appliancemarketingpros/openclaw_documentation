---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/it/platforms/mac/skills
scraped_at: 2026-05-25
---

L'app macOS espone Skills di OpenClaw tramite il gateway; non analizza le Skills localmente.

## Origine dei dati

  * `skills.status` (gateway) restituisce tutte le Skills più idoneità e requisiti mancanti (inclusi i blocchi allowlist per le Skills integrate).
  * I requisiti derivano da `metadata.openclaw.requires` in ogni `SKILL.md`.


## Azioni di installazione

  * `metadata.openclaw.install` definisce le opzioni di installazione (brew/node/go/uv).
  * L'app chiama `skills.install` per eseguire gli installer sull'host gateway.
  * Le rilevazioni `critical` integrate di dangerous-code bloccano `skills.install` per impostazione predefinita; le rilevazioni sospette continuano solo a emettere avvisi. L'override dangerous esiste sulla richiesta gateway, ma il flusso predefinito dell'app resta fail-closed.
  * Se ogni opzione di installazione è `download`, il gateway espone tutte le scelte di download.
  * In caso contrario, il gateway sceglie un installer preferito usando le preferenze di installazione correnti e i binari host: prima Homebrew quando `skills.install.preferBrew` è abilitato e `brew` esiste, poi `uv`, poi il gestore Node configurato da `skills.install.nodeManager`, poi fallback successivi come `go` o `download`.
  * Le etichette di installazione Node riflettono il gestore Node configurato, incluso `yarn`.


## Env/API key

  * L'app memorizza le chiavi in `~/.openclaw/openclaw.json` sotto `skills.entries.<skillKey>`.
  * `skills.update` applica patch a `enabled`, `apiKey` ed `env`.


## Modalità remota

  * Installazione + aggiornamenti di configurazione avvengono sull'host gateway (non sul Mac locale).


## Correlati

  * [Skills](</it/tools/skills>)
  * [App macOS](</it/platforms/macos>)


Was this useful?YesNo
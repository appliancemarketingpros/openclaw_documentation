---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/pl/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin Codex Supervisor

Nadzoruj sesje serwera aplikacji Codex z OpenClaw.

## Dystrybucja

  * Pakiet: `@openclaw/codex-supervisor`
  * Ścieżka instalacji: dołączony do OpenClaw


## Powierzchnia

kontrakty: narzędzia

## Lista sesji

`codex_sessions_list` domyślnie obejmuje tylko załadowane sesje Codex. Ustaw `include_stored`, aby uwzględnić zapisaną historię; Plugin używa ścieżki listowania serwera aplikacji Codex opartej wyłącznie na bazie danych stanu i domyślnie ogranicza zapisane wyniki do 200. Przekaż `max_stored_sessions`, aby obniżyć lub podnieść ten limit, maksymalnie do 1000.

Was this useful?YesNo

Open issue
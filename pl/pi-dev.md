---
title: Przepływ pracy przy rozwoju Pi
source_url: https://docs.openclaw.ai/pl/pi-dev
scraped_at: 2026-05-25
---

Rozsądny przepływ pracy przy pracy nad integracją Pi w OpenClaw.

## Sprawdzanie typów i linting

  * Domyślna lokalna bramka: `pnpm check`
  * Bramka kompilacji: `pnpm build`, gdy zmiana może wpłynąć na wynik kompilacji, pakietowanie lub granice lazy-loading/modułów
  * Pełna bramka przed scaleniem dla zmian silnie związanych z Pi: `pnpm check && pnpm test`


## Uruchamianie testów Pi

Uruchom zestaw testów skoncentrowanych na Pi bezpośrednio za pomocą Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Aby uwzględnić ćwiczenie dostawcy na żywo:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Obejmuje to główne zestawy testów jednostkowych Pi:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Testowanie ręczne

Zalecany przepływ:

  * Uruchom Gateway w trybie deweloperskim: 
    * `pnpm gateway:dev`
  * Wyzwól agenta bezpośrednio: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Użyj TUI do interaktywnego debugowania: 
    * `pnpm tui`


Aby sprawdzić zachowanie wywołań narzędzi, poproś o akcję `read` lub `exec`, aby zobaczyć przesyłanie strumieniowe narzędzi i obsługę ładunku.

## Reset do czystego stanu

Stan znajduje się w katalogu stanu OpenClaw. Domyślnie jest to `~/.openclaw`. Jeśli ustawiono `OPENCLAW_STATE_DIR`, użyj zamiast tego wskazanego katalogu.

Aby zresetować wszystko:

  * `openclaw.json` dla konfiguracji
  * `agents/<agentId>/agent/auth-profiles.json` dla profili uwierzytelniania modelu (klucze API + OAuth)
  * `credentials/` dla stanu dostawcy/kanału, który nadal znajduje się poza magazynem profili uwierzytelniania
  * `agents/<agentId>/sessions/` dla historii sesji agenta
  * `agents/<agentId>/sessions/sessions.json` dla indeksu sesji
  * `sessions/`, jeśli istnieją starsze ścieżki
  * `workspace/`, jeśli chcesz mieć pustą przestrzeń roboczą


Jeśli chcesz zresetować tylko sesje, usuń `agents/<agentId>/sessions/` dla tego agenta. Jeśli chcesz zachować uwierzytelnianie, pozostaw `agents/<agentId>/agent/auth-profiles.json` oraz dowolny stan dostawcy w `credentials/` bez zmian.

## Odniesienia

  * [Testowanie](</pl/help/testing>)
  * [Pierwsze kroki](</pl/start/getting-started>)


## Powiązane

  * [Architektura integracji Pi](</pl/pi>)


Was this useful?YesNo
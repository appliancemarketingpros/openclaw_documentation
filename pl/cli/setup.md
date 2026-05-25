---
title: Konfiguracja
source_url: https://docs.openclaw.ai/pl/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Inicjalizuje bazową konfigurację i obszar roboczy agenta. Gdy obecna jest dowolna flaga onboardingu, uruchamia też kreator.

## Opcje

Flaga | Opis  
---|---  
`--workspace <dir>` | Katalog obszaru roboczego agenta (domyślnie `~/.openclaw/workspace`; przechowywany jako `agents.defaults.workspace`).  
`--wizard` | Uruchom interaktywny onboarding.  
`--non-interactive` | Uruchom onboarding bez monitów.  
`--mode <mode>` | Tryb onboardingu: `local` albo `remote`.  
`--import-from <provider>` | Dostawca migracji do uruchomienia podczas onboardingu.  
`--import-source <path>` | Źródłowy katalog domowy agenta dla `--import-from`.  
`--import-secrets` | Importuj obsługiwane sekrety podczas migracji w onboardingu.  
`--remote-url <url>` | Adres URL WebSocket zdalnego Gateway.  
`--remote-token <token>` | Token zdalnego Gateway (opcjonalny).  
  
### Automatyczne wyzwalanie kreatora

`openclaw setup` uruchamia kreator, gdy którakolwiek z tych flag jest jawnie obecna, nawet bez `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Przykłady

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Uwagi

  * Zwykłe `openclaw setup` inicjalizuje konfigurację i obszar roboczy bez uruchamiania pełnego procesu onboardingu.
  * Po zwykłym setupie uruchom `openclaw onboard`, aby przejść pełną ścieżkę z przewodnikiem, `openclaw configure`, aby wprowadzić ukierunkowane zmiany, albo `openclaw channels add`, aby dodać konta kanałów.
  * Jeśli wykryto stan Hermes, interaktywny onboarding może automatycznie zaoferować migrację. Importowanie podczas onboardingu wymaga świeżego setupu; użyj [Migrate](</pl/cli/migrate>), aby przygotować plany próbne, kopie zapasowe i tryb nadpisywania poza onboardingiem.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Onboarding (CLI)](</pl/start/wizard>)
  * [Pierwsze kroki](</pl/start/getting-started>)
  * [Omówienie instalacji](</pl/install>)


Was this useful?YesNo
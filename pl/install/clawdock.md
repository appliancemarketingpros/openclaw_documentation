---
title: ClawDock
source_url: https://docs.openclaw.ai/pl/install/clawdock
scraped_at: 2026-05-25
---

ClawDock to niewielka warstwa pomocniczych funkcji powłoki dla instalacji OpenClaw opartych na Docker.

Daje krótkie polecenia, takie jak `clawdock-start`, `clawdock-dashboard` i `clawdock-fix-token`, zamiast dłuższych wywołań `docker compose ...`.

Jeśli Docker nie jest jeszcze skonfigurowany, zacznij od [Docker](</pl/install/docker>).

## Instalacja

Użyj kanonicznej ścieżki helpera:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Jeśli wcześniej zainstalowano ClawDock z `scripts/shell-helpers/clawdock-helpers.sh`, zainstaluj go ponownie z nowej ścieżki `scripts/clawdock/clawdock-helpers.sh`. Stara surowa ścieżka GitHub została usunięta.

## Co otrzymujesz

### Podstawowe operacje

Polecenie | Opis  
---|---  
`clawdock-start` | Uruchom Gateway  
`clawdock-stop` | Zatrzymaj Gateway  
`clawdock-restart` | Uruchom ponownie Gateway  
`clawdock-status` | Sprawdź stan kontenera  
`clawdock-logs` | Śledź logi Gateway  
  
### Dostęp do kontenera

Polecenie | Opis  
---|---  
`clawdock-shell` | Otwórz powłokę w kontenerze Gateway  
`clawdock-cli <command>` | Uruchom polecenia CLI OpenClaw w Docker  
`clawdock-exec <command>` | Wykonaj dowolne polecenie w kontenerze  
  
### Web UI i parowanie

Polecenie | Opis  
---|---  
`clawdock-dashboard` | Otwórz URL Control UI  
`clawdock-devices` | Wyświetl oczekujące parowania urządzeń  
`clawdock-approve <id>` | Zatwierdź prośbę o parowanie  
  
### Konfiguracja i konserwacja

Polecenie | Opis  
---|---  
`clawdock-fix-token` | Skonfiguruj token Gateway wewnątrz kontenera  
`clawdock-update` | Pobierz, przebuduj i uruchom ponownie  
`clawdock-rebuild` | Przebuduj tylko obraz Docker  
`clawdock-clean` | Usuń kontenery i wolumeny  
  
### Narzędzia

Polecenie | Opis  
---|---  
`clawdock-health` | Uruchom sprawdzanie kondycji Gateway  
`clawdock-token` | Wypisz token Gateway  
`clawdock-cd` | Przejdź do katalogu projektu OpenClaw  
`clawdock-config` | Otwórz `~/.openclaw`  
`clawdock-show-config` | Wypisz pliki konfiguracyjne z zredagowanymi wartościami  
`clawdock-workspace` | Otwórz katalog obszaru roboczego  
  
## Pierwszy przepływ

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Jeśli przeglądarka informuje, że parowanie jest wymagane:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Konfiguracja i sekrety

ClawDock działa z tym samym podziałem konfiguracji Docker opisanym w [Docker](</pl/install/docker>):

  * `<project>/.env` dla wartości specyficznych dla Docker, takich jak nazwa obrazu, porty i token Gateway
  * `~/.openclaw/.env` dla kluczy dostawców i tokenów botów opartych na env
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` dla przechowywanego uwierzytelniania dostawcy OAuth/klucza API
  * `~/.openclaw/openclaw.json` dla konfiguracji zachowania


Użyj `clawdock-show-config`, gdy chcesz szybko przejrzeć pliki `.env` i `openclaw.json`. W wypisywanych danych redaguje wartości `.env`.

## Powiązane

[**Docker** Kanoniczna instalacja Docker dla OpenClaw. ](</pl/install/docker>) [**Środowisko uruchomieniowe Docker VM** Zarządzane przez Docker środowisko uruchomieniowe VM z utwardzoną izolacją. ](</pl/install/docker-vm-runtime>) [**Aktualizowanie** Aktualizowanie pakietu OpenClaw i zarządzanych usług. ](</pl/install/updating>)

Was this useful?YesNo
---
title: Przegląd wdrażania
source_url: https://docs.openclaw.ai/pl/start/onboarding-overview
scraped_at: 2026-05-25
---

OpenClaw ma dwie ścieżki wdrażania. Obie konfigurują uwierzytelnianie, Gateway oraz opcjonalne kanały czatu — różnią się tylko sposobem interakcji z konfiguracją.

## Której ścieżki użyć?

| Wdrażanie CLI | Wdrażanie w aplikacji macOS  
---|---|---  
**Platformy** | macOS, Linux, Windows (natywnie lub WSL2) | Tylko macOS  
**Interfejs** | Kreator w terminalu | Prowadzony interfejs w aplikacji  
**Najlepsze dla** | Serwery, tryb bez interfejsu, pełna kontrola | Mac stacjonarny, konfiguracja wizualna  
**Automatyzacja** | `--non-interactive` dla skryptów | Tylko ręcznie  
**Polecenie** | `openclaw onboard` | Uruchom aplikację  
  
Większość użytkowników powinna zacząć od **wdrażania CLI** — działa wszędzie i daje największą kontrolę.

## Co konfiguruje wdrażanie

Niezależnie od wybranej ścieżki wdrażanie konfiguruje:

  1. **Dostawca modelu i uwierzytelnianie** — klucz API, OAuth lub token konfiguracji dla wybranego dostawcy
  2. **Obszar roboczy** — katalog na pliki agentów, szablony startowe i pamięć
  3. **Gateway** — port, adres powiązania, tryb uwierzytelniania
  4. **Kanały** (opcjonalnie) — wbudowane i dołączone kanały czatu, takie jak iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, Telegram, WhatsApp i inne
  5. **Demon** (opcjonalnie) — usługa w tle, dzięki której Gateway uruchamia się automatycznie


## Wdrażanie CLI

Uruchom w dowolnym terminalu:

bashCopy code
[code]
    openclaw onboard
[/code]

Dodaj `--install-daemon`, aby w jednym kroku zainstalować także usługę w tle.

Pełna dokumentacja: [Wdrażanie (CLI)](</pl/start/wizard>) Dokumentacja polecenia CLI: [`openclaw onboard`](</pl/cli/onboard>)

## Wdrażanie w aplikacji macOS

Otwórz aplikację OpenClaw. Kreator pierwszego uruchomienia przeprowadzi Cię przez te same kroki za pomocą interfejsu wizualnego.

Pełna dokumentacja: [Wdrażanie (aplikacja macOS)](</pl/start/onboarding>)

## Dostawcy niestandardowi lub spoza listy

Jeśli Twojego dostawcy nie ma na liście we wdrażaniu, wybierz **Dostawca niestandardowy** i wprowadź:

  * Tryb zgodności API (zgodny z OpenAI, zgodny z Anthropic lub automatyczne wykrywanie)
  * Bazowy URL i klucz API
  * Identyfikator modelu i opcjonalny alias


Może współistnieć wiele niestandardowych punktów końcowych — każdy otrzymuje własny identyfikator punktu końcowego.

## Powiązane

  * [Pierwsze kroki](</pl/start/getting-started>)
  * [Dokumentacja konfiguracji CLI](</pl/start/wizard-cli-reference>)


Was this useful?YesNo
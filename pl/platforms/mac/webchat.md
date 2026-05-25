---
title: Czat webowy (macOS)
source_url: https://docs.openclaw.ai/pl/platforms/mac/webchat
scraped_at: 2026-05-25
---

Aplikacja paska menu macOS osadza interfejs WebChat UI jako natywny widok SwiftUI. Łączy się z Gateway i domyślnie używa **sesji głównej** dla wybranego agenta (z przełącznikiem sesji dla innych sesji).

  * **Tryb lokalny** : łączy się bezpośrednio z lokalnym Gateway WebSocket.
  * **Tryb zdalny** : przekazuje port sterowania Gateway przez SSH i używa tego tunelu jako płaszczyzny danych.


## Uruchamianie i debugowanie

  * Ręcznie: menu Lobster → „Otwórz czat”.

  * Automatyczne otwieranie do testów:

bashCopy code
[code]dist/OpenClaw.app/Contents/MacOS/OpenClaw --webchat
[/code]

  * Logi: `./scripts/clawlog.sh` (podsystem `ai.openclaw`, kategoria `WebChatSwiftUI`).


## Jak to jest połączone

  * Płaszczyzna danych: metody Gateway WS `chat.history`, `chat.send`, `chat.abort`, `chat.inject` oraz zdarzenia `chat`, `agent`, `presence`, `tick`, `health`.
  * `chat.history` zwraca wiersze transkryptu znormalizowane do wyświetlania: wbudowane tagi dyrektyw są usuwane z widocznego tekstu, tekstowe ładunki XML wywołań narzędzi (w tym `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` oraz ucięte bloki wywołań narzędzi) i ujawnione tokeny sterujące modelu ASCII/pełnej szerokości są usuwane, czyste wiersze asystenta z cichymi tokenami, takie jak dokładne `NO_REPLY` / `no_reply`, są pomijane, a zbyt duże wiersze mogą zostać zastąpione placeholderami.
  * Sesja: domyślnie używa sesji podstawowej (`main` albo `global`, gdy zakres jest globalny). UI może przełączać się między sesjami.
  * Onboarding używa dedykowanej sesji, aby oddzielić konfigurację pierwszego uruchomienia.


## Powierzchnia bezpieczeństwa

  * Tryb zdalny przekazuje przez SSH tylko port sterowania Gateway WebSocket.


## Znane ograniczenia

  * UI jest zoptymalizowany pod kątem sesji czatu (nie jest pełną piaskownicą przeglądarki).


## Powiązane

  * [WebChat](</pl/web/webchat>)
  * [aplikacja macOS](</pl/platforms/macos>)


Was this useful?YesNo
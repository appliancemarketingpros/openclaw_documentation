---
title: Wybudzanie głosem
source_url: https://docs.openclaw.ai/pl/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw traktuje **słowa wybudzające jako jedną globalną listę** należącą do **Gateway**.

  * Nie ma **niestandardowych słów wybudzających dla poszczególnych węzłów**.
  * **Dowolny interfejs węzła/aplikacji może edytować** tę listę; zmiany są utrwalane przez Gateway i rozgłaszane do wszystkich.
  * macOS i iOS zachowują lokalne przełączniki **włączenia/wyłączenia wybudzania głosem** (lokalny UX i uprawnienia się różnią).
  * Android obecnie utrzymuje wybudzanie głosem wyłączone i używa ręcznego przepływu mikrofonu na karcie Głos.


## Przechowywanie (host Gateway)

Słowa wybudzające są przechowywane na maszynie Gateway w:

  * `~/.openclaw/settings/voicewake.json`


Kształt:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## Protokół

### Metody

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` z parametrami `{ triggers: string[] }` → `{ triggers: string[] }`


Uwagi:

  * Wyzwalacze są normalizowane (przycinane, puste usuwane). Puste listy wracają do wartości domyślnych.
  * Limity są egzekwowane ze względów bezpieczeństwa (ograniczenia liczby/długości).


### Metody routingu (wyzwalacz → cel)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` z parametrami `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


Kształt `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Cele tras obsługują dokładnie jedno z:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### Zdarzenia

  * Ładunek `voicewake.changed` `{ triggers: string[] }`
  * Ładunek `voicewake.routing.changed` `{ config: VoiceWakeRoutingConfig }`


Kto je otrzymuje:

  * Wszyscy klienci WebSocket (aplikacja macOS, WebChat itp.)
  * Wszystkie połączone węzły (iOS/Android), a także przy połączeniu węzła jako początkowe wypchnięcie „bieżącego stanu”.


## Zachowanie klienta

### Aplikacja macOS

  * Używa globalnej listy do bramkowania wyzwalaczy `VoiceWakeRuntime`.
  * Edycja „Słów wyzwalających” w ustawieniach wybudzania głosem wywołuje `voicewake.set`, a następnie polega na rozgłoszeniu, aby utrzymać synchronizację innych klientów.


### Węzeł iOS

  * Używa globalnej listy do wykrywania wyzwalaczy przez `VoiceWakeManager`.
  * Edycja słów wybudzających w Ustawieniach wywołuje `voicewake.set` (przez Gateway WS) i jednocześnie utrzymuje responsywne lokalne wykrywanie słów wybudzających.


### Węzeł Android

  * Wybudzanie głosem jest obecnie wyłączone w środowisku uruchomieniowym/ustawieniach Androida.
  * Głos na Androidzie używa ręcznego przechwytywania mikrofonu na karcie Głos zamiast wyzwalaczy słów wybudzających.


## Powiązane

  * [Tryb rozmowy](</pl/nodes/talk>)
  * [Notatki audio i głosowe](</pl/nodes/audio>)
  * [Rozumienie multimediów](</pl/nodes/media-understanding>)


Was this useful?YesNo
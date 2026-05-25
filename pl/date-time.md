---
title: Data i godzina
source_url: https://docs.openclaw.ai/pl/date-time
scraped_at: 2026-05-25
---

OpenClaw domyślnie używa **lokalnego czasu hosta dla znaczników czasu transportu** oraz **strefy czasowej użytkownika tylko w prompcie systemowym**. Znaczniki czasu dostawcy są zachowywane, aby narzędzia utrzymywały swoją natywną semantykę (bieżący czas jest dostępny przez `session_status`).

## Koperty wiadomości (domyślnie lokalne)

Wiadści przychodzące są opakowywane znacznikiem czasu (precyzja do minuty):

CodeCopy code
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
[/code]

Ten znacznik czasu koperty jest **domyślnie lokalny dla hosta** , niezależnie od strefy czasowej dostawcy.

Możesz nadpisać to zachowanie:

json5Copy code
[code]
    {  agents: {    defaults: {      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone      envelopeTimestamp: "on", // "on" | "off"      envelopeElapsed: "on", // "on" | "off"    },  },}
[/code]

  * `envelopeTimezone: "utc"` używa UTC.
  * `envelopeTimezone: "local"` używa strefy czasowej hosta.
  * `envelopeTimezone: "user"` używa `agents.defaults.userTimezone` (z powrotem do strefy czasowej hosta).
  * Użyj jawnej strefy czasowej IANA (np. `"America/Chicago"`) dla stałej strefy.
  * `envelopeTimestamp: "off"` usuwa bezwzględne znaczniki czasu z nagłówków koperty.
  * `envelopeElapsed: "off"` usuwa sufiksy czasu, który upłynął (styl `+2m`).


### Przykłady

**Lokalna (domyślnie):**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 PST] hello
[/code]

**Strefa czasowa użytkownika:**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 CST] hello
[/code]

**Włączony czas, który upłynął:**

CodeCopy code
[code]
    [WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
[/code]

## Prompt systemowy: bieżąca data i godzina

Jeśli strefa czasowa użytkownika jest znana, prompt systemowy zawiera dedykowaną sekcję **Bieżąca data i godzina** z **samą strefą czasową** (bez formatu zegara/czasu), aby zachować stabilność buforowania promptów:

CodeCopy code
[code]
    Time zone: America/Chicago
[/code]

Gdy agent potrzebuje bieżącego czasu, użyj narzędzia `session_status`; karta statusu zawiera wiersz ze znacznikiem czasu.

## Wiersze zdarzeń systemowych (domyślnie lokalne)

Zdarzenia systemowe w kolejce wstawiane do kontekstu agenta są poprzedzane znacznikiem czasu przy użyciu tego samego wyboru strefy czasowej co koperty wiadomości (domyślnie: lokalna hosta).

CodeCopy code
[code]
    System: [2026-01-12 12:19:17 PST] Model switched.
[/code]

### Konfiguracja strefy czasowej użytkownika i formatu

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",      timeFormat: "auto", // auto | 12 | 24    },  },}
[/code]

  * `userTimezone` ustawia **lokalną strefę czasową użytkownika** dla kontekstu promptu.
  * `timeFormat` kontroluje **wyświetlanie w formacie 12h/24h** w prompcie. `auto` podąża za preferencjami systemu operacyjnego.


## Wykrywanie formatu czasu (auto)

Gdy `timeFormat: "auto"`, OpenClaw sprawdza preferencję systemu operacyjnego (macOS/Windows) i z powrotem używa formatowania ustawień regionalnych. Wykryta wartość jest **buforowana dla procesu** , aby uniknąć powtarzanych wywołań systemowych.

## Ładunki narzędzi i konektory (surowy czas dostawcy + znormalizowane pola)

Narzędzia kanałów zwracają **natywne znaczniki czasu dostawcy** i dodają znormalizowane pola dla spójności:

  * `timestampMs`: milisekundy epoki (UTC)
  * `timestampUtc`: ciąg ISO 8601 UTC


Surowe pola dostawcy są zachowywane, więc nic nie zostaje utracone.

  * Slack: ciągi podobne do epoki z API
  * Discord: znaczniki czasu ISO UTC
  * Telegram/WhatsApp: specyficzne dla dostawcy znaczniki czasu numeryczne/ISO


Jeśli potrzebujesz czasu lokalnego, przekonwertuj go dalej, używając znanej strefy czasowej.

## Powiązane dokumenty

  * [Prompt systemowy](</pl/concepts/system-prompt>)
  * [Strefy czasowe](</pl/concepts/timezone>)
  * [Wiadomości](</pl/concepts/messages>)


Was this useful?YesNo
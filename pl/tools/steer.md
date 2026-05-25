---
title: Steruj
source_url: https://docs.openclaw.ai/pl/tools/steer
scraped_at: 2026-05-25
---

`/steer` wysyła wskazówki do już aktywnego uruchomienia. Służy do sytuacji typu „dostosuj to uruchomienie, gdy nadal pracuje”, a nie do rozpoczynania nowej tury.

## Bieżąca sesja

Użyj najwyższego poziomu `/steer`, aby wskazać aktywne uruchomienie dla bieżącej sesji:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Zachowanie:

  * Wskazuje tylko aktywne uruchomienie bieżącej sesji.
  * Działa niezależnie od trybu `/queue` sesji.
  * Nie rozpoczyna nowego uruchomienia, gdy sesja jest bezczynna.
  * Odpowiada ostrzeżeniem, gdy nie ma aktywnego uruchomienia, którym można pokierować.
  * Używa ścieżki sterowania aktywnego środowiska wykonawczego, więc model widzi wskazówki przy następnej obsługiwanej granicy środowiska wykonawczego.


## Sterowanie a kolejka

`/queue steer` zmienia sposób działania zwykłych wiadomości przychodzących, gdy docierają, kiedy uruchomienie jest aktywne. `/steer <message>` to jawne polecenie, które próbuje wstrzyknąć wiadomość tego polecenia do aktywnego uruchomienia przy następnej obsługiwanej granicy środowiska wykonawczego, niezależnie od zapisanego ustawienia `/queue`.

Używaj:

  * `/steer <message>`, gdy chcesz pokierować aktywnym uruchomieniem teraz.
  * `/queue steer`, gdy chcesz, aby przyszłe zwykłe wiadomości domyślnie sterowały aktywnymi uruchomieniami.
  * `/queue collect` lub `/queue followup`, gdy nowe wiadomości powinny poczekać na późniejszą turę zamiast sterować aktywnym uruchomieniem.


Tryby kolejki i zachowanie awaryjne opisują [Kolejka poleceń](</pl/concepts/queue>) oraz [Kolejka sterowania](</pl/concepts/queue-steering>).

## Podagenci

Użyj `/subagents steer`, gdy celem jest uruchomienie podrzędne:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

Najwyższego poziomu `/steer` nie wybiera podagenta według identyfikatora ani indeksu listy. Zawsze wskazuje aktywne uruchomienie bieżącej sesji. Zobacz [Podagenci](</pl/tools/subagents>), aby poznać identyfikatory, etykiety i polecenia sterujące podagentów.

## Sesje ACP

Użyj `/acp steer`, gdy celem jest sesja uprzęży ACP:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Zobacz [Agenci ACP](</pl/tools/acp-agents>), aby poznać wybór sesji ACP i zachowanie środowiska wykonawczego.

## Powiązane

  * [Polecenia ukośnikowe](</pl/tools/slash-commands>)
  * [Kolejka poleceń](</pl/concepts/queue>)
  * [Kolejka sterowania](</pl/concepts/queue-steering>)
  * [Podagenci](</pl/tools/subagents>)


Was this useful?YesNo
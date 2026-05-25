---
title: Tokenjuice
source_url: https://docs.openclaw.ai/pl/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` to opcjonalny dołączony Plugin, który kompaktuje zaszumione wyniki narzędzi `exec` i `bash` po wykonaniu polecenia.

Zmienia zwracany `tool_result`, a nie samo polecenie. Tokenjuice nie przepisuje danych wejściowych powłoki, nie uruchamia ponownie poleceń ani nie zmienia kodów wyjścia.

Obecnie dotyczy to osadzonych uruchomień PI oraz dynamicznych narzędzi OpenClaw w harnessie app-server Codex. Tokenjuice podłącza się do middleware wyników narzędzi OpenClaw i przycina dane wyjściowe, zanim wrócą do aktywnej sesji harnessu.

## Włącz Plugin

Szybka ścieżka:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Równoważnie:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw już dostarcza ten Plugin. Nie ma osobnego kroku `plugins install` ani `tokenjuice install openclaw`.

Jeśli wolisz edytować konfigurację bezpośrednio:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Co zmienia tokenjuice

  * Kompaktuje zaszumione wyniki `exec` i `bash`, zanim zostaną zwrócone do sesji.
  * Pozostawia samo wykonanie polecenia bez zmian.
  * Zachowuje dokładne odczyty zawartości plików i inne polecenia, które tokenjuice powinien pozostawić w surowej postaci.
  * Pozostaje opcjonalny: wyłącz Plugin, jeśli chcesz dosłownych danych wyjściowych wszędzie.


## Sprawdź, czy działa

  1. Włącz Plugin.
  2. Uruchom sesję, która może wywoływać `exec`.
  3. Uruchom zaszumione polecenie, takie jak `git status`.
  4. Sprawdź, czy zwrócony wynik narzędzia jest krótszy i bardziej uporządkowany niż surowe dane wyjściowe powłoki.


## Wyłącz Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Lub:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Powiązane

  * [Narzędzie Exec](</pl/tools/exec>)
  * [Poziomy myślenia](</pl/tools/thinking>)
  * [Silnik kontekstu](</pl/concepts/context-engine>)


Was this useful?YesNo
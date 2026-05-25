---
title: Wyszukiwanie DuckDuckGo
source_url: https://docs.openclaw.ai/pl/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw obsługuje DuckDuckGo jako dostawcę `web_search` **bez klucza**. Nie jest wymagany klucz API ani konto.

## Konfiguracja

Nie potrzeba klucza API - wystarczy ustawić DuckDuckGo jako dostawcę:

* ### Skonfiguruj

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Konfiguracja

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Opcjonalne ustawienia na poziomie Plugin dla regionu i SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Parametry narzędzia

Zapytanie wyszukiwania.

Liczba wyników do zwrócenia (1-10).

Kod regionu DuckDuckGo (np. `us-en`, `uk-en`, `de-de`).

Poziom SafeSearch.

Region i SafeSearch można też ustawić w konfiguracji Plugin (patrz wyżej) - parametry narzędzia zastępują wartości konfiguracji dla pojedynczego zapytania.

## Uwagi

  * **Brak klucza API** \- działa od razu, bez konfiguracji
  * **Eksperymentalne** \- zbiera wyniki ze stron wyszukiwania DuckDuckGo w formacie HTML bez JavaScriptu, a nie z oficjalnego API ani SDK
  * **Ryzyko wyzwań dla botów** \- DuckDuckGo może wyświetlać CAPTCHA lub blokować żądania przy intensywnym albo zautomatyzowanym użyciu
  * **Parsowanie HTML** \- wyniki zależą od struktury strony, która może się zmienić bez powiadomienia
  * **Kolejność automatycznego wykrywania** \- DuckDuckGo jest pierwszą zapasową opcją bez klucza (kolejność 100) w automatycznym wykrywaniu. Dostawcy oparci na API ze skonfigurowanymi kluczami są uruchamiani jako pierwsi, potem Ollama Web Search (kolejność 110), następnie SearXNG (kolejność 200)
  * **SafeSearch domyślnie ma poziom moderate** , gdy nie jest skonfigurowany


## Powiązane

  * [Omówienie Web Search](</pl/tools/web>) \-- wszyscy dostawcy i automatyczne wykrywanie
  * [Brave Search](</pl/tools/brave-search>) \-- uporządkowane wyniki z darmowym poziomem
  * [Exa Search](</pl/tools/exa-search>) \-- wyszukiwanie neuronowe z wyodrębnianiem treści


Was this useful?YesNo
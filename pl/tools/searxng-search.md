---
title: Wyszukiwanie SearXNG
source_url: https://docs.openclaw.ai/pl/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw obsługuje [SearXNG](<https://docs.searxng.org/>) jako **samodzielnie hostowanego, bezkluczowego** dostawcę `web_search`. SearXNG to otwartoźródłowa metawyszukiwarka, która agreguje wyniki z Google, Bing, DuckDuckGo i innych źródeł.

Zalety:

  * **Bezpłatne i bez limitów** \-- nie wymaga klucza API ani subskrypcji komercyjnej
  * **Prywatność / izolacja sieciowa** \-- zapytania nigdy nie opuszczają Twojej sieci
  * **Działa wszędzie** \-- bez ograniczeń regionalnych komercyjnych API wyszukiwania


## Konfiguracja

* ### Run a SearXNG instance

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Albo użyj dowolnego istniejącego wdrożenia SearXNG, do którego masz dostęp. Zobacz [dokumentację SearXNG](<https://docs.searxng.org/>), aby skonfigurować środowisko produkcyjne.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Albo ustaw zmienną środowiskową i pozwól automatycznemu wykrywaniu ją znaleźć:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Konfiguracja

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Ustawienia na poziomie Plugin dla instancji SearXNG:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

Pole `baseUrl` akceptuje także obiekty SecretRef.

Reguły transportu:

  * `https://` działa dla publicznych lub prywatnych hostów SearXNG
  * `http://` jest akceptowane tylko dla zaufanych hostów w sieci prywatnej lub hostów pętli zwrotnej
  * publiczne hosty SearXNG muszą używać `https://`
  * hosty prywatne/wewnętrzne używają zabezpieczenia sieci samodzielnie hostowanej; publiczne hosty `https://` pozostają przy ścisłym zabezpieczeniu wyszukiwania w sieci i nie mogą przekierowywać na adresy prywatne


## Zmienna środowiskowa

Ustaw `SEARXNG_BASE_URL` jako alternatywę dla konfiguracji:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Gdy `SEARXNG_BASE_URL` jest ustawiona i nie skonfigurowano jawnego dostawcy, automatyczne wykrywanie wybiera SearXNG automatycznie (z najniższym priorytetem -- każdy dostawca oparty na API z kluczem wygrywa jako pierwszy).

## Dokumentacja konfiguracji Plugin

Pole | Opis  
---|---  
`baseUrl` | Bazowy URL Twojej instancji SearXNG (wymagane)  
`categories` | Kategorie rozdzielone przecinkami, takie jak `general`, `news` lub `science`  
`language` | Kod języka wyników, taki jak `en`, `de` lub `fr`  
  
## Uwagi

  * **JSON API** \-- używa natywnego punktu końcowego SearXNG `format=json`, a nie scrapowania HTML
  * **Adresy URL wyników obrazów** \-- wyniki kategorii obrazów zawierają `img_src`, gdy SearXNG zwraca bezpośredni URL obrazu
  * **Brak klucza API** \-- działa od razu z dowolną instancją SearXNG
  * **Walidacja bazowego URL** \-- `baseUrl` musi być prawidłowym adresem URL `http://` lub `https://`; publiczne hosty muszą używać `https://`
  * **Zabezpieczenie sieci** \-- prywatne/wewnętrzne punkty końcowe SearXNG włączają dostęp do sieci prywatnej; publiczne punkty końcowe SearXNG `https://` zachowują ścisłą ochronę przed SSRF
  * **Kolejność automatycznego wykrywania** \-- SearXNG jest sprawdzany jako ostatni (kolejność 200) w automatycznym wykrywaniu. Dostawcy oparci na API ze skonfigurowanymi kluczami uruchamiają się jako pierwsi, następnie DuckDuckGo (kolejność 100), a potem Ollama Web Search (kolejność 110)
  * **Samodzielnie hostowane** \-- kontrolujesz instancję, zapytania i nadrzędne wyszukiwarki
  * **Kategorie** domyślnie przyjmują `general`, gdy nie są skonfigurowane
  * **Rezerwowa kategoria** \-- jeśli żądanie kategorii innej niż `general` powiedzie się, ale zwróci zero wyników, OpenClaw ponawia to samo zapytanie raz z `general` przed zwróceniem pustego zestawu wyników


## Powiązane

  * [Omówienie wyszukiwania w sieci](</pl/tools/web>) \-- wszyscy dostawcy i automatyczne wykrywanie
  * [Wyszukiwanie DuckDuckGo](</pl/tools/duckduckgo-search>) \-- kolejna rezerwowa opcja bez klucza
  * [Brave Search](</pl/tools/brave-search>) \-- ustrukturyzowane wyniki z bezpłatnym poziomem


Was this useful?YesNo
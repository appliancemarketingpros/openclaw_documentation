---
title: Tavily
source_url: https://docs.openclaw.ai/pl/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) to API wyszukiwania zaprojektowane dla aplikacji AI. OpenClaw udostępnia je na dwa sposoby:

  * jako dostawcę `web_search` dla ogólnego narzędzia wyszukiwania
  * jako jawne narzędzia Plugin: `tavily_search` i `tavily_extract`


Tavily zwraca uporządkowane wyniki zoptymalizowane pod użycie przez LLM, z konfigurowalną głębokością wyszukiwania, filtrowaniem tematów, filtrami domen, generowanymi przez AI podsumowaniami odpowiedzi oraz wyodrębnianiem treści z URL-i (w tym stron renderowanych przez JavaScript).

Właściwość | Wartość  
---|---  
Identyfikator Plugin | `tavily`  
Uwierzytelnianie | `TAVILY_API_KEY` lub config `apiKey`  
Bazowy URL | `https://api.tavily.com` (domyślnie)  
Dołączone narzędzia | `tavily_search`, `tavily_extract`  
  
## Pierwsze kroki

* ### Get an API key

Utwórz konto Tavily na [tavily.com](<https://tavily.com>), a następnie wygeneruj klucz API w panelu.

* ### Configure the plugin and provider

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verify search runs

Uruchom `web_search` z dowolnego agenta albo wywołaj bezpośrednio `tavily_search`.

## Dokumentacja narzędzi

### `tavily_search`

Użyj tego, gdy potrzebujesz kontrolek wyszukiwania specyficznych dla Tavily zamiast ogólnego `web_search`.

Parametr | Typ | Ograniczenia / domyślne | Opis  
---|---|---|---  
`query` | string | wymagane | Ciąg zapytania wyszukiwania. Nie przekraczaj 400 znaków.  
`search_depth` | enum | `basic` (domyślnie), `advanced` | `advanced` jest wolniejsze, ale trafniejsze.  
`topic` | enum | `general` (domyślnie), `news`, `finance` | Filtruj według rodziny tematów.  
`max_results` | integer | 1-20 | Liczba wyników.  
`include_answer` | boolean | domyślnie `false` | Dołącz wygenerowane przez Tavily AI podsumowanie odpowiedzi.  
`time_range` | enum | `day`, `week`, `month`, `year` | Filtruj wyniki według aktualności.  
`include_domains` | string array | (brak) | Uwzględniaj tylko wyniki z tych domen.  
`exclude_domains` | string array | (brak) | Wyklucz wyniki z tych domen.  
  
Kompromis głębokości wyszukiwania:

Głębokość | Szybkość | Trafność | Najlepsze do  
---|---|---|---  
`basic` | Szybsze | Wysoka | Zapytania ogólnego przeznaczenia (domyślnie).  
`advanced` | Wolniejsze | Najwyższa | Precyzyjne badania i ustalanie faktów.  
  
### `tavily_extract`

Użyj tego, aby wyodrębnić czystą treść z jednego lub wielu URL-i. Obsługuje strony renderowane przez JavaScript i wspiera dzielenie na fragmenty ukierunkowane zapytaniem na potrzeby celowanego wyodrębniania.

Parametr | Typ | Ograniczenia / domyślne | Opis  
---|---|---|---  
`urls` | string array | wymagane, 1-20 | URL-e, z których należy wyodrębnić treść.  
`query` | string | (opcjonalne) | Ponownie uszereguj wyodrębnione fragmenty według trafności względem tego zapytania.  
`extract_depth` | enum | `basic` (domyślnie), `advanced` | Użyj `advanced` dla stron mocno opartych na JS, SPA lub dynamicznych tabel.  
`chunks_per_source` | integer | 1-5; **wymaga`query`** | Fragmenty zwracane na URL. Zwraca błąd, jeśli ustawione bez `query`.  
`include_images` | boolean | domyślnie `false` | Dołącz URL-e obrazów w wynikach.  
  
Kompromis głębokości wyodrębniania:

Głębokość | Kiedy używać  
---|---  
`basic` | Proste strony. Wypróbuj to najpierw.  
`advanced` | SPA renderowane przez JS, treść dynamiczna, tabele.  
  
## Wybór właściwego narzędzia

Potrzeba | Narzędzie  
---|---  
Szybkie wyszukiwanie w sieci, bez opcji specjalnych | `web_search`  
Wyszukiwanie z głębokością, tematem, odpowiedziami AI | `tavily_search`  
Wyodrębnianie treści z konkretnych URL-i | `tavily_extract`  
  
## Konfiguracja zaawansowana

API key resolution order

Klient Tavily wyszukuje swój klucz API w tej kolejności:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (rozwiązywane przez SecretRefs).
  2. `TAVILY_API_KEY` ze środowiska Gateway.


`tavily_extract` zgłasza błąd konfiguracji, jeśli żadne z nich nie jest dostępne.

Custom base URL

Nadpisz `plugins.entries.tavily.config.webSearch.baseUrl`, jeśli udostępniasz Tavily przez proxy. Domyślna wartość to `https://api.tavily.com`.

`chunks_per_source` requires `query`

`tavily_extract` odrzuca wywołania, które przekazują `chunks_per_source` bez `query`. Tavily szereguje fragmenty według trafności zapytania, więc parametr jest bez niego bez znaczenia.

## Powiązane

[**Web Search overview** Wszyscy dostawcy i reguły automatycznego wykrywania. ](</pl/tools/web>) [**Firecrawl** Wyszukiwanie oraz scraping z wyodrębnianiem treści. ](</pl/tools/firecrawl>) [**Exa Search** Wyszukiwanie neuronowe z wyodrębnianiem treści. ](</pl/tools/exa-search>) [**Configuration** Pełny schemat konfiguracji wpisów Plugin i routingu narzędzi. ](</pl/gateway/configuration>)

Was this useful?YesNo
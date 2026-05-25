---
title: Wyszukiwanie w sieci
source_url: https://docs.openclaw.ai/pl/tools/web
scraped_at: 2026-05-25
---

Narzędzie `web_search` przeszukuje internet przy użyciu skonfigurowanego dostawcy i zwraca wyniki. Wyniki są buforowane według zapytania przez 15 minut (można to skonfigurować).

OpenClaw zawiera też `x_search` dla wpisów z X (dawniej Twitter) oraz `web_fetch` do lekkiego pobierania URL-i. W tej fazie `web_fetch` pozostaje lokalne, a `web_search` i `x_search` mogą używać xAI Responses pod spodem.

## Szybki start

* ### Wybierz dostawcę

Wybierz dostawcę i wykonaj wymaganą konfigurację. Niektórzy dostawcy są bez klucza, a inni używają kluczy API. Szczegóły znajdziesz na stronach dostawców poniżej.

* ### Skonfiguruj

bashCopy code
[code]
    openclaw configure --section web
[/code]

To zapisuje dostawcę i wszelkie potrzebne dane uwierzytelniające. Możesz także ustawić zmienną środowiskową (na przykład `BRAVE_API_KEY`) i pominąć ten krok dla dostawców opartych na API.

* ### Użyj

Agent może teraz wywołać `web_search`:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Dla wpisów z X użyj:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Wybór dostawcy

[**Brave Search** Ustrukturyzowane wyniki z fragmentami. Obsługuje tryb `llm-context` oraz filtry kraju/języka. Dostępny bezpłatny poziom. ](</pl/tools/brave-search>) [**DuckDuckGo** Awaryjna opcja bez klucza. Klucz API nie jest potrzebny. Nieoficjalna integracja oparta na HTML. ](</pl/tools/duckduckgo-search>) [**Exa** Wyszukiwanie neuronowe + słowne z ekstrakcją treści (wyróżnienia, tekst, podsumowania). ](</pl/tools/exa-search>) [**Firecrawl** Ustrukturyzowane wyniki. Najlepiej łączyć z `firecrawl_search` i `firecrawl_scrape` do głębokiej ekstrakcji. ](</pl/tools/firecrawl>) [**Gemini** Odpowiedzi syntetyzowane przez AI z cytowaniami przez ugruntowanie w Google Search. ](</pl/tools/gemini-search>) [**Grok** Odpowiedzi syntetyzowane przez AI z cytowaniami przez ugruntowanie internetowe xAI. ](</pl/tools/grok-search>) [**Kimi** Odpowiedzi syntetyzowane przez AI z cytowaniami przez wyszukiwanie internetowe Moonshot; nieugruntowane awaryjne odpowiedzi czatu jawnie kończą się błędem. ](</pl/tools/kimi-search>) [**MiniMax Search** Ustrukturyzowane wyniki przez API wyszukiwania MiniMax Token Plan. ](</pl/tools/minimax-search>) [**Ollama Web Search** Wyszukiwanie przez zalogowanego lokalnego hosta Ollama lub hostowane API Ollama. ](</pl/tools/ollama-search>) [**Perplexity** Ustrukturyzowane wyniki z kontrolkami ekstrakcji treści i filtrowaniem domen. ](</pl/tools/perplexity-search>) [**SearXNG** Samodzielnie hostowane metawyszukiwanie. Klucz API nie jest potrzebny. Agreguje Google, Bing, DuckDuckGo i inne. ](</pl/tools/searxng-search>) [**Tavily** Ustrukturyzowane wyniki z głębokością wyszukiwania, filtrowaniem tematów i `tavily_extract` do ekstrakcji URL-i. ](</pl/tools/tavily>)

### Porównanie dostawców

Dostawca | Styl wyników | Filtry | Klucz API  
---|---|---|---  
[Brave](</pl/tools/brave-search>) | Ustrukturyzowane fragmenty | Kraj, język, czas, tryb `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</pl/tools/duckduckgo-search>) | Ustrukturyzowane fragmenty | \-- | Brak (bez klucza)  
[Exa](</pl/tools/exa-search>) | Ustrukturyzowane + wyodrębnione | Tryb neuronowy/słowny, data, ekstrakcja treści | `EXA_API_KEY`  
[Firecrawl](</pl/tools/firecrawl>) | Ustrukturyzowane fragmenty | Przez narzędzie `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</pl/tools/gemini-search>) | Syntetyzowane przez AI + cytowania | \-- | `GEMINI_API_KEY`  
[Grok](</pl/tools/grok-search>) | Syntetyzowane przez AI + cytowania | \-- | `XAI_API_KEY`  
[Kimi](</pl/tools/kimi-search>) | Syntetyzowane przez AI + cytowania; kończy się błędem przy nieugruntowanych awaryjnych odpowiedziach czatu | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</pl/tools/minimax-search>) | Ustrukturyzowane fragmenty | Region (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</pl/tools/ollama-search>) | Ustrukturyzowane fragmenty | \-- | Brak dla zalogowanych lokalnych hostów; `OLLAMA_API_KEY` dla bezpośredniego wyszukiwania `https://ollama.com`  
[Perplexity](</pl/tools/perplexity-search>) | Ustrukturyzowane fragmenty | Kraj, język, czas, domeny, limity treści | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</pl/tools/searxng-search>) | Ustrukturyzowane fragmenty | Kategorie, język | Brak (samodzielnie hostowane)  
[Tavily](</pl/tools/tavily>) | Ustrukturyzowane fragmenty | Przez narzędzie `tavily_search` | `TAVILY_API_KEY`  
  
## Automatyczne wykrywanie

## Natywne wyszukiwanie internetowe OpenAI

Bezpośrednie modele OpenAI Responses automatycznie używają hostowanego przez OpenAI narzędzia `web_search`, gdy wyszukiwanie internetowe OpenClaw jest włączone i nie przypięto żadnego zarządzanego dostawcy. Jest to zachowanie należące do dostawcy w dołączonym Plugin OpenAI i dotyczy tylko natywnego ruchu OpenAI API, a nie zgodnych z OpenAI bazowych URL-i proxy ani tras Azure. Ustaw `tools.web.search.provider` na innego dostawcę, takiego jak `brave`, aby zachować zarządzane narzędzie `web_search` dla modeli OpenAI, albo ustaw `tools.web.search.enabled: false`, aby wyłączyć zarówno zarządzane wyszukiwanie, jak i natywne wyszukiwanie OpenAI.

## Natywne wyszukiwanie internetowe Codex

Modele obsługujące Codex mogą opcjonalnie używać natywnego dla dostawcy narzędzia Responses `web_search` zamiast zarządzanej funkcji OpenClaw `web_search`.

  * Skonfiguruj je pod `tools.web.search.openaiCodex`
  * Aktywuje się tylko dla modeli obsługujących Codex (`openai-codex/*` lub dostawców używających `api: "openai-codex-responses"`)
  * Zarządzane `web_search` nadal dotyczy modeli innych niż Codex
  * `mode: "cached"` jest ustawieniem domyślnym i zalecanym
  * `tools.web.search.enabled: false` wyłącza zarówno zarządzane, jak i natywne wyszukiwanie

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Jeśli natywne wyszukiwanie Codex jest włączone, ale bieżący model nie obsługuje Codex, OpenClaw zachowuje normalne zarządzane zachowanie `web_search`.

## Bezpieczeństwo sieci

Zarządzane wywołania dostawcy `web_search` używają chronionej ścieżki pobierania OpenClaw. Dla zaufanych hostów API dostawców OpenClaw zezwala na odpowiedzi DNS fake-IP Surge, Clash i sing-box w `198.18.0.0/15` oraz `fc00::/7` tylko dla tej nazwy hosta dostawcy. Inne prywatne, loopback, link-local i metadane docelowe pozostają zablokowane.

To automatyczne zezwolenie nie dotyczy dowolnych URL-i `web_fetch`. Dla `web_fetch` włącz `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` i `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` jawnie tylko wtedy, gdy zaufane proxy jest właścicielem tych syntetycznych zakresów.

## Konfigurowanie wyszukiwania internetowego

Listy dostawców w dokumentacji i przepływach konfiguracji są alfabetyczne. Automatyczne wykrywanie utrzymuje oddzielną kolejność pierwszeństwa.

Jeśli nie ustawiono `provider`, OpenClaw sprawdza dostawców w tej kolejności i używa pierwszego gotowego:

Najpierw dostawcy oparci na API:

  1. **Brave** \-- `BRAVE_API_KEY` lub `plugins.entries.brave.config.webSearch.apiKey` (kolejność 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` lub `plugins.entries.minimax.config.webSearch.apiKey` (kolejność 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY` lub `models.providers.google.apiKey` (kolejność 20)
  4. **Grok** \-- `XAI_API_KEY` lub `plugins.entries.xai.config.webSearch.apiKey` (kolejność 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` lub `plugins.entries.moonshot.config.webSearch.apiKey` (kolejność 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` lub `plugins.entries.perplexity.config.webSearch.apiKey` (kolejność 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` lub `plugins.entries.firecrawl.config.webSearch.apiKey` (kolejność 60)
  8. **Exa** \-- `EXA_API_KEY` lub `plugins.entries.exa.config.webSearch.apiKey`; opcjonalne `plugins.entries.exa.config.webSearch.baseUrl` zastępuje punkt końcowy Exa (kolejność 65)
  9. **Tavily** \-- `TAVILY_API_KEY` lub `plugins.entries.tavily.config.webSearch.apiKey` (kolejność 70)


Następnie awaryjne opcje bez klucza:

  10. **DuckDuckGo** \-- awaryjna opcja HTML bez klucza, bez konta ani klucza API (kolejność 100)
  11. **Ollama Web Search** \-- awaryjna opcja bez klucza przez skonfigurowanego lokalnego hosta Ollama, gdy jest osiągalny i zalogowany przez `ollama signin`; może ponownie używać uwierzytelniania bearer dostawcy Ollama, gdy host go potrzebuje, i może wywoływać bezpośrednie wyszukiwanie `https://ollama.com`, gdy skonfigurowano `OLLAMA_API_KEY` (kolejność 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` lub `plugins.entries.searxng.config.webSearch.baseUrl` (kolejność 200)


Jeśli nie wykryto żadnego dostawcy, nastąpi powrót do Brave (otrzymasz błąd brakującego klucza z prośbą o skonfigurowanie go).

## Konfiguracja

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

Konfiguracja specyficzna dla dostawcy (klucze API, bazowe adresy URL, tryby) znajduje się pod `plugins.entries.<plugin>.config.webSearch.*`. Gemini może także ponownie używać `models.providers.google.apiKey` oraz `models.providers.google.baseUrl` jako zapasowych opcji o niższym priorytecie po dedykowanej konfiguracji wyszukiwania w sieci i `GEMINI_API_KEY`. Przykłady znajdziesz na stronach dostawców.

`tools.web.search.provider` jest sprawdzane względem identyfikatorów dostawców wyszukiwania w sieci zadeklarowanych w manifestach dołączonych i zainstalowanych pluginów. Literówka taka jak `"brvae"` powoduje błąd walidacji konfiguracji zamiast cichego powrotu do automatycznego wykrywania. Jeśli skonfigurowany dostawca ma tylko nieaktualny dowód pluginu, na przykład pozostały blok `plugins.entries.<plugin>` po odinstalowaniu pluginu innej firmy, OpenClaw zachowuje odporność uruchamiania i zgłasza ostrzeżenie, aby można było ponownie zainstalować plugin albo uruchomić `openclaw doctor --fix`, aby wyczyścić nieaktualną konfigurację.

Wybór dostawcy zapasowego dla `web_fetch` jest osobny:

  * wybierz go przez `tools.web.fetch.provider`
  * albo pomiń to pole i pozwól OpenClaw automatycznie wykryć pierwszego gotowego dostawcę pobierania z sieci na podstawie dostępnych poświadczeń
  * `web_fetch` poza piaskownicą może używać zainstalowanych dostawców pluginów deklarujących `contracts.webFetchProviders`; pobieranie w piaskownicy pozostaje ograniczone do dołączonych dostawców
  * obecnie dołączonym dostawcą pobierania z sieci jest Firecrawl, skonfigurowany pod `plugins.entries.firecrawl.config.webFetch.*`


Gdy wybierzesz **Kimi** podczas `openclaw onboard` albo `openclaw configure --section web`, OpenClaw może także zapytać o:

  * region API Moonshot (`https://api.moonshot.ai/v1` albo `https://api.moonshot.cn/v1`)
  * domyślny model wyszukiwania w sieci Kimi (domyślnie `kimi-k2.6`)


Dla `x_search` skonfiguruj `plugins.entries.xai.config.xSearch.*`. Używa tego samego profilu uwierzytelniania xAI co czat albo `XAI_API_KEY` / poświadczenia wyszukiwania w sieci pluginu używanego przez wyszukiwanie w sieci Grok. Starsza konfiguracja `tools.web.x_search.*` jest automatycznie migrowana przez `openclaw doctor --fix`. Gdy wybierzesz Grok podczas `openclaw onboard` albo `openclaw configure --section web`, OpenClaw może także zaproponować opcjonalną konfigurację `x_search` z tym samym kluczem. To osobny kolejny krok w ścieżce Grok, a nie osobny wybór dostawcy wyszukiwania w sieci na najwyższym poziomie. Jeśli wybierzesz innego dostawcę, OpenClaw nie pokaże monitu `x_search`.

### Przechowywanie kluczy API

### Plik konfiguracyjny

Uruchom `openclaw configure --section web` albo ustaw klucz bezpośrednio:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Zmienna środowiskowa

Ustaw zmienną środowiskową dostawcy w środowisku procesu Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

W przypadku instalacji Gateway umieść ją w `~/.openclaw/.env`. Zobacz [Zmienne środowiskowe](</pl/help/faq#env-vars-and-env-loading>).

## Parametry narzędzia

Parametr | Opis  
---|---  
`query` | Zapytanie wyszukiwania (wymagane)  
`count` | Liczba wyników do zwrócenia (1-10, domyślnie: 5)  
`country` | 2-literowy kod kraju ISO (np. "US", "DE")  
`language` | Kod języka ISO 639-1 (np. "en", "de")  
`search_lang` | Kod języka wyszukiwania (tylko Brave)  
`freshness` | Filtr czasu: `day`, `week`, `month` albo `year`  
`date_after` | Wyniki po tej dacie (YYYY-MM-DD)  
`date_before` | Wyniki przed tą datą (YYYY-MM-DD)  
`ui_lang` | Kod języka interfejsu użytkownika (tylko Brave)  
`domain_filter` | Tablica listy dozwolonych/zablokowanych domen (tylko Perplexity)  
`max_tokens` | Całkowity budżet treści, domyślnie 25000 (tylko Perplexity)  
`max_tokens_per_page` | Limit tokenów na stronę, domyślnie 2048 (tylko Perplexity)  
  
## x_search

`x_search` odpytuje wpisy X (dawniej Twitter) przy użyciu xAI i zwraca odpowiedzi syntetyzowane przez AI z cytowaniami. Akceptuje zapytania w języku naturalnym oraz opcjonalne filtry strukturalne. OpenClaw włącza wbudowane narzędzie xAI `x_search` tylko dla żądania obsługującego to wywołanie narzędzia.

### Konfiguracja x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` wysyła wpisy do `<baseUrl>/responses`, gdy `plugins.entries.xai.config.xSearch.baseUrl` jest ustawione. Jeśli to pole zostanie pominięte, następuje powrót do `plugins.entries.xai.config.webSearch.baseUrl`, następnie do starszego `tools.web.search.grok.baseUrl`, a na końcu do publicznego punktu końcowego xAI.

### Parametry x_search

Parametr | Opis  
---|---  
`query` | Zapytanie wyszukiwania (wymagane)  
`allowed_x_handles` | Ogranicz wyniki do określonych uchwytów X  
`excluded_x_handles` | Wyklucz określone uchwyty X  
`from_date` | Uwzględnij tylko wpisy z tej daty lub późniejsze (YYYY-MM-DD)  
`to_date` | Uwzględnij tylko wpisy z tej daty lub wcześniejsze (YYYY-MM-DD)  
`enable_image_understanding` | Pozwól xAI analizować obrazy dołączone do pasujących wpisów  
`enable_video_understanding` | Pozwól xAI analizować filmy dołączone do pasujących wpisów  
  
### Przykład x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Przykłady

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Profile narzędzi

Jeśli używasz profili narzędzi albo list dozwolonych, dodaj `web_search`, `x_search` albo `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Powiązane

  * [Web Fetch](</pl/tools/web-fetch>) \-- pobierz adres URL i wyodrębnij czytelną treść
  * [Web Browser](</pl/tools/browser>) \-- pełna automatyzacja przeglądarki dla witryn mocno opartych na JS
  * [Grok Search](</pl/tools/grok-search>) \-- Grok jako dostawca `web_search`
  * [Ollama Web Search](</pl/tools/ollama-search>) \-- wyszukiwanie w sieci bez klucza przez host Ollama


Was this useful?YesNo
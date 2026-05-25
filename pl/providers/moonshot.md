---
title: Moonshot AI
source_url: https://docs.openclaw.ai/pl/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot udostępnia Kimi API z punktami końcowymi zgodnymi z OpenAI. Skonfiguruj dostawcę i ustaw domyślny model na `moonshot/kimi-k2.6` albo użyj Kimi Coding z `kimi/kimi-for-coding`.

## Wbudowany katalog modeli

Odwołanie do modelu | Nazwa | Rozumowanie | Wejście | Kontekst | Maks. wyjście  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Nie | tekst, obraz | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Nie | tekst, obraz | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Tak | tekst | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Tak | tekst | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Nie | tekst | 256,000 | 16,384  
  
Dołączone szacunki kosztów dla obecnych modeli K2 hostowanych przez Moonshot używają opublikowanych przez Moonshot stawek płatności według zużycia: Kimi K2.6 kosztuje $0.16/MTok przy trafieniu w pamięć podręczną, $0.95/MTok wejścia i $4.00/MTok wyjścia; Kimi K2.5 kosztuje $0.10/MTok przy trafieniu w pamięć podręczną, $0.60/MTok wejścia i $3.00/MTok wyjścia. Pozostałe starsze wpisy katalogu zachowują zerokosztowe symbole zastępcze, chyba że nadpiszesz je w konfiguracji.

## Pierwsze kroki

Wybierz dostawcę i wykonaj kroki konfiguracji.

### Moonshot API

**Najlepsze do:** modeli Kimi K2 przez Moonshot Open Platform.

* ### Wybierz region punktu końcowego

Wybór uwierzytelniania | Punkt końcowy | Region  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | Międzynarodowy  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | Chiny  
* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Albo dla punktu końcowego w Chinach:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Uruchom test smoke na żywo

Użyj izolowanego katalogu stanu, gdy chcesz zweryfikować dostęp do modelu i śledzenie kosztów bez naruszania zwykłych sesji:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

Odpowiedź JSON powinna zgłosić `provider: "moonshot"` i `model: "kimi-k2.6"`. Wpis transkrypcji asystenta przechowuje znormalizowane użycie tokenów oraz szacowany koszt w `usage.cost`, gdy Moonshot zwraca metadane użycia.

### Przykład konfiguracji

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Najlepsze do:** zadań skoncentrowanych na kodzie przez punkt końcowy Kimi Coding.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Przykład konfiguracji

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Wyszukiwanie internetowe Kimi

OpenClaw dostarcza też **Kimi** jako dostawcę `web_search`, opartego na wyszukiwaniu w sieci Moonshot.

* ### Uruchom interaktywną konfigurację wyszukiwania w sieci

bashCopy code
[code]
    openclaw configure --section web
[/code]

Wybierz **Kimi** w sekcji wyszukiwania w sieci, aby zapisać `plugins.entries.moonshot.config.webSearch.*`.

* ### Skonfiguruj region i model wyszukiwania w sieci

Interaktywna konfiguracja pyta o:

Ustawienie | Opcje  
---|---  
Region API | `https://api.moonshot.ai/v1` (międzynarodowy) lub `https://api.moonshot.cn/v1` (Chiny)  
Model wyszukiwania w sieci | Domyślnie `kimi-k2.6`  
  
Konfiguracja znajduje się w `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Konfiguracja zaawansowana

Natywny tryb myślenia

Moonshot Kimi obsługuje binarny natywny tryb myślenia:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Skonfiguruj go dla każdego modelu przez `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw mapuje też poziomy runtime `/think` dla Moonshot:

Poziom `/think` | Zachowanie Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
Dowolny poziom inny niż off | `thinking.type=enabled`  
  
Kimi K2.6 akceptuje też opcjonalne pole `thinking.keep`, które kontroluje wieloturowe zachowywanie `reasoning_content`. Ustaw je na `"all"`, aby zachować pełne rozumowanie między turami; pomiń je (albo pozostaw jako `null`), aby użyć domyślnej strategii serwera. OpenClaw przekazuje `thinking.keep` tylko dla `moonshot/kimi-k2.6` i usuwa je z innych modeli.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Sanityzacja identyfikatorów wywołań narzędzi

Moonshot Kimi udostępnia identyfikatory tool_call w formacie `functions.<name>:<index>`. OpenClaw zachowuje je bez zmian, dzięki czemu wieloturowe wywołania narzędzi nadal działają.

Aby wymusić ścisłą sanityzację dla niestandardowego dostawcy zgodnego z OpenAI, ustaw `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Zgodność użycia w streamingu

Natywne endpointy Moonshot (`https://api.moonshot.ai/v1` i `https://api.moonshot.cn/v1`) deklarują zgodność użycia w streamingu we współdzielonym transporcie `openai-completions`. OpenClaw opiera to na możliwościach endpointu, więc zgodne identyfikatory niestandardowych dostawców kierujące do tych samych natywnych hostów Moonshot dziedziczą to samo zachowanie użycia w streamingu.

Przy dołączonej wycenie K2.6 streamowane użycie, które obejmuje tokeny wejściowe, wyjściowe i odczytu z pamięci podręcznej, jest też przeliczane na lokalnie szacowany koszt w USD dla `/status`, `/usage full`, `/usage cost` oraz rozliczania sesji opartego na transkrypcji.

Odwołanie do punktów końcowych i odwołań do modeli Dostawca | Prefiks odwołania do modelu | Punkt końcowy | Zmienna środowiskowa uwierzytelniania  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Punkt końcowy Kimi Coding | `KIMI_API_KEY`  
Wyszukiwanie w sieci | N/A | Taki sam jak region API Moonshot | `KIMI_API_KEY` lub `MOONSHOT_API_KEY`  
  
  * Wyszukiwanie w sieci Kimi używa `KIMI_API_KEY` lub `MOONSHOT_API_KEY` i domyślnie korzysta z `https://api.moonshot.ai/v1` z modelem `kimi-k2.6`.
  * W razie potrzeby nadpisz cennik oraz metadane kontekstu w `models.providers`.
  * Jeśli Moonshot opublikuje inne limity kontekstu dla modelu, odpowiednio dostosuj `contextWindow`.


## Powiązane

[**Wybór modelu** Wybieranie dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Wyszukiwanie w sieci** Konfigurowanie dostawców wyszukiwania w sieci, w tym Kimi. ](</pl/tools/web>) [**Odwołanie do konfiguracji** Pełny schemat konfiguracji dla dostawców, modeli i plugins. ](</pl/gateway/configuration-reference>) [**Moonshot Open Platform** Zarządzanie kluczami API Moonshot i dokumentacja. ](<https://platform.moonshot.ai>)

Was this useful?YesNo
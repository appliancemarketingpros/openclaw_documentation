---
title: Dokumentacja referencyjna konfiguracji pamięci
source_url: https://docs.openclaw.ai/pl/reference/memory-config
scraped_at: 2026-05-25
---

Ta strona zawiera listę wszystkich ustawień konfiguracji wyszukiwania w pamięci OpenClaw. Omówienia koncepcyjne znajdziesz tutaj:

[**Omówienie pamięci** Jak działa pamięć. ](</pl/concepts/memory>) [**Wbudowany silnik** Domyślny backend SQLite. ](</pl/concepts/memory-builtin>) [**Silnik QMD** Lokalny sidecar. ](</pl/concepts/memory-qmd>) [**Wyszukiwanie w pamięci** Potok wyszukiwania i dostrajanie. ](</pl/concepts/memory-search>) [**Active Memory** Subagent pamięci dla sesji interaktywnych. ](</pl/concepts/active-memory>)

Wszystkie ustawienia wyszukiwania w pamięci znajdują się w `agents.defaults.memorySearch` w `openclaw.json`, o ile nie wskazano inaczej.

* * *

## Wybór dostawcy

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`provider` | `string` | wykrywane automatycznie | Identyfikator adaptera osadzania, taki jak `bedrock`, `deepinfra`, `gemini`, `github-copilot`, `local`, `mistral`, `ollama`, `openai` lub `voyage`; może też być skonfigurowanym `models.providers.<id>`, którego `api` wskazuje jeden z tych adapterów  
`model` | `string` | domyślne dostawcy | Nazwa modelu osadzania  
`fallback` | `string` | `"none"` | Identyfikator adaptera zapasowego, gdy podstawowy zawiedzie  
`enabled` | `boolean` | `true` | Włącza lub wyłącza wyszukiwanie w pamięci  
  
### Kolejność automatycznego wykrywania

Gdy `provider` nie jest ustawione, OpenClaw wybiera pierwszą dostępną opcję:

* ### local

Wybrane, jeśli skonfigurowano `memorySearch.local.modelPath` i plik istnieje.

* ### github-copilot

Wybrane, jeśli można rozpoznać token GitHub Copilot (zmienna środowiskowa lub profil uwierzytelniania).

* ### openai

Wybrane, jeśli można rozpoznać klucz OpenAI.

* ### gemini

Wybrane, jeśli można rozpoznać klucz Gemini.

* ### voyage

Wybrane, jeśli można rozpoznać klucz Voyage.

* ### mistral

Wybrane, jeśli można rozpoznać klucz Mistral.

* ### deepinfra

Wybrane, jeśli można rozpoznać klucz DeepInfra.

* ### bedrock

Wybrane, jeśli łańcuch poświadczeń AWS SDK zostanie rozpoznany (rola instancji, klucze dostępu, profil, SSO, tożsamość internetowa lub współdzielona konfiguracja).

`ollama` jest obsługiwane, ale nie jest wykrywane automatycznie (ustaw je jawnie).

### Niestandardowe identyfikatory dostawców

`memorySearch.provider` może wskazywać niestandardowy wpis `models.providers.<id>`. OpenClaw rozpoznaje właściciela `api` tego dostawcy dla adaptera osadzania, zachowując niestandardowy identyfikator dostawcy na potrzeby obsługi punktu końcowego, uwierzytelniania i prefiksu modelu. Dzięki temu konfiguracje z wieloma GPU lub wieloma hostami mogą przypisać osadzania pamięci do konkretnego lokalnego punktu końcowego:

json5Copy code
[code]
    {  models: {    providers: {      "ollama-5080": {        api: "ollama",        baseUrl: "http://gpu-box.local:11435",        apiKey: "ollama-local",        models: [{ id: "qwen3-embedding:0.6b" }],      },    },  },  agents: {    defaults: {      memorySearch: {        provider: "ollama-5080",        model: "qwen3-embedding:0.6b",      },    },  },}
[/code]

### Rozpoznawanie klucza API

Zdalne osadzania wymagają klucza API. Bedrock używa zamiast tego domyślnego łańcucha poświadczeń AWS SDK (role instancji, SSO, klucze dostępu).

Dostawca | Zmienna środowiskowa | Klucz konfiguracji  
---|---|---  
Bedrock | Łańcuch poświadczeń AWS | Klucz API nie jest potrzebny  
DeepInfra | `DEEPINFRA_API_KEY` | `models.providers.deepinfra.apiKey`  
Gemini | `GEMINI_API_KEY` | `models.providers.google.apiKey`  
GitHub Copilot | `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN` | Profil uwierzytelniania przez logowanie urządzenia  
Mistral | `MISTRAL_API_KEY` | `models.providers.mistral.apiKey`  
Ollama | `OLLAMA_API_KEY` (placeholder) | \--  
OpenAI | `OPENAI_API_KEY` | `models.providers.openai.apiKey`  
Voyage | `VOYAGE_API_KEY` | `models.providers.voyage.apiKey`  
  
* * *

## Konfiguracja zdalnego punktu końcowego

Dla niestandardowych punktów końcowych zgodnych z OpenAI lub nadpisywania ustawień domyślnych dostawcy:

Niestandardowy bazowy URL API.

Nadpisanie klucza API.

Dodatkowe nagłówki HTTP (scalane z ustawieniami domyślnymi dostawcy).

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",        remote: {          baseUrl: "https://api.example.com/v1/",          apiKey: "YOUR_KEY",        },      },    },  },}
[/code]

* * *

## Konfiguracja specyficzna dla dostawcy

Gemini Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`model` | `string` | `gemini-embedding-001` | Obsługuje także `gemini-embedding-2-preview`  
`outputDimensionality` | `number` | `3072` | Dla Embedding 2: 768, 1536 lub 3072  
Typy danych wejściowych zgodne z OpenAI

Punkty końcowe osadzania zgodne z OpenAI mogą włączyć specyficzne dla dostawcy pola żądania `input_type`. Jest to przydatne w przypadku asymetrycznych modeli osadzania, które wymagają różnych etykiet dla osadzań zapytań i dokumentów.

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`inputType` | `string` | nieustawione | Wspólne `input_type` dla osadzań zapytań i dokumentów  
`queryInputType` | `string` | nieustawione | `input_type` w czasie zapytania; nadpisuje `inputType`  
`documentInputType` | `string` | nieustawione | `input_type` indeksu/dokumentu; nadpisuje `inputType`  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        remote: {          baseUrl: "https://embeddings.example/v1",          apiKey: "env:EMBEDDINGS_API_KEY",        },        model: "asymmetric-embedder",        queryInputType: "query",        documentInputType: "passage",      },    },  },}
[/code]

Zmiana tych wartości wpływa na tożsamość pamięci podręcznej osadzania dla indeksowania wsadowego dostawcy i powinna być po niej wykonana ponowna indeksacja pamięci, gdy model nadrzędny różnie traktuje etykiety.

Bedrock

### Konfiguracja osadzania Bedrock

Bedrock używa domyślnego łańcucha poświadczeń AWS SDK — klucze API nie są potrzebne. Jeśli OpenClaw działa na EC2 z rolą instancji z włączonym Bedrock, wystarczy ustawić dostawcę i model:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0",      },    },  },}
[/code]

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`model` | `string` | `amazon.titan-embed-text-v2:0` | Dowolny identyfikator modelu osadzania Bedrock  
`outputDimensionality` | `number` | domyślne modelu | Dla Titan V2: 256, 512 lub 1024  
  
**Obsługiwane modele** (z wykrywaniem rodziny i domyślnymi wymiarami):

Identyfikator modelu | Dostawca | Domyślne wymiary | Konfigurowalne wymiary  
---|---|---|---  
`amazon.titan-embed-text-v2:0` | Amazon | 1024 | 256, 512, 1024  
`amazon.titan-embed-text-v1` | Amazon | 1536 | \--  
`amazon.titan-embed-g1-text-02` | Amazon | 1536 | \--  
`amazon.titan-embed-image-v1` | Amazon | 1024 | \--  
`amazon.nova-2-multimodal-embeddings-v1:0` | Amazon | 1024 | 256, 384, 1024, 3072  
`cohere.embed-english-v3` | Cohere | 1024 | \--  
`cohere.embed-multilingual-v3` | Cohere | 1024 | \--  
`cohere.embed-v4:0` | Cohere | 1536 | 256-1536  
`twelvelabs.marengo-embed-3-0-v1:0` | TwelveLabs | 512 | \--  
`twelvelabs.marengo-embed-2-7-v1:0` | TwelveLabs | 1024 | \--  
  
Warianty z sufiksem przepustowości (np. `amazon.titan-embed-text-v1:2:8k`) dziedziczą konfigurację modelu bazowego.

**Uwierzytelnianie:** uwierzytelnianie Bedrock używa standardowej kolejności rozpoznawania poświadczeń AWS SDK:

  1. Zmienne środowiskowe (`AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`)
  2. Pamięć podręczna tokenów SSO
  3. Poświadczenia tokenu tożsamości internetowej
  4. Współdzielone poświadczenia i pliki konfiguracyjne
  5. Poświadczenia metadanych ECS lub EC2


Region jest rozpoznawany z `AWS_REGION`, `AWS_DEFAULT_REGION`, `baseUrl` dostawcy `amazon-bedrock` albo domyślnie ustawiany na `us-east-1`.

**Uprawnienia IAM:** rola lub użytkownik IAM potrzebuje:

jsonCopy code
[code]
    {  "Effect": "Allow",  "Action": "bedrock:InvokeModel",  "Resource": "*"}
[/code]

Aby zastosować zasadę najmniejszych uprawnień, ogranicz `InvokeModel` do konkretnego modelu:

CodeCopy code
[code]
    arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0
[/code]

Lokalne (GGUF + node-llama-cpp) Klucz | Typ | Domyślne | Opis  
---|---|---|---  
`local.modelPath` | `string` | pobierany automatycznie | Ścieżka do pliku modelu GGUF  
`local.modelCacheDir` | `string` | domyślne node-llama-cpp | Katalog pamięci podręcznej dla pobranych modeli  
`local.contextSize` | `number | "auto"` | `4096` | Rozmiar okna kontekstu dla kontekstu embeddingów. 4096 obejmuje typowe fragmenty (128–512 tokenów), ograniczając jednocześnie pamięć VRAM poza wagami. Obniż do 1024–2048 na hostach z ograniczeniami. `"auto"` używa wytrenowanego maksimum modelu — niezalecane dla modeli 8B+ (Qwen3-Embedding-8B: 40 960 tokenów → ~32 GB VRAM vs ~8,8 GB przy 4096).  
  
Model domyślny: `embeddinggemma-300m-qat-Q8_0.gguf` (~0,6 GB, pobierany automatycznie). Check-outy źródłowe nadal wymagają zatwierdzenia natywnej kompilacji: `pnpm approve-builds`, a następnie `pnpm rebuild node-llama-cpp`.

Użyj samodzielnego CLI, aby zweryfikować tę samą ścieżkę dostawcy, której używa Gateway:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Jeśli `provider` to `auto`, `local` jest wybierany tylko wtedy, gdy `local.modelPath` wskazuje istniejący plik lokalny. Odwołania do modeli `hf:` i HTTP(S) nadal mogą być używane jawnie z `provider: "local"`, ale nie powodują, że `auto` wybierze lokalnego dostawcę, zanim model będzie dostępny na dysku.

### Limit czasu embeddingów inline

Nadpisz limit czasu dla partii embeddingów inline podczas indeksowania pamięci.

Brak ustawienia używa wartości domyślnej dostawcy: 600 sekund dla dostawców lokalnych/samodzielnie hostowanych, takich jak `local`, `ollama` i `lmstudio`, oraz 120 sekund dla dostawców hostowanych. Zwiększ tę wartość, gdy lokalne partie embeddingów ograniczone CPU działają poprawnie, ale wolno.

* * *

## Konfiguracja wyszukiwania hybrydowego

Wszystko w `memorySearch.query.hybrid`:

Klucz | Typ | Domyślne | Opis  
---|---|---|---  
`enabled` | `boolean` | `true` | Włącz hybrydowe wyszukiwanie BM25 + wektorowe  
`vectorWeight` | `number` | `0.7` | Waga wyników wektorowych (0-1)  
`textWeight` | `number` | `0.3` | Waga wyników BM25 (0-1)  
`candidateMultiplier` | `number` | `4` | Mnożnik rozmiaru puli kandydatów  
  
### MMR (różnorodność)

Klucz | Typ | Domyślne | Opis  
---|---|---|---  
`mmr.enabled` | `boolean` | `false` | Włącz ponowne rangowanie MMR  
`mmr.lambda` | `number` | `0.7` | 0 = maks. różnorodność, 1 = maks. trafność  
  
### Wygaszanie czasowe (aktualność)

Klucz | Typ | Domyślne | Opis  
---|---|---|---  
`temporalDecay.enabled` | `boolean` | `false` | Włącz podbicie aktualności  
`temporalDecay.halfLifeDays` | `number` | `30` | Wynik zmniejsza się o połowę co N dni  
  
Pliki ponadczasowe (`MEMORY.md`, niedatowane pliki w `memory/`) nigdy nie podlegają wygaszaniu.

### Pełny przykład

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        query: {          hybrid: {            vectorWeight: 0.7,            textWeight: 0.3,            mmr: { enabled: true, lambda: 0.7 },            temporalDecay: { enabled: true, halfLifeDays: 30 },          },        },      },    },  },}
[/code]

* * *

## Dodatkowe ścieżki pamięci

Klucz | Typ | Opis  
---|---|---  
`extraPaths` | `string[]` | Dodatkowe katalogi lub pliki do indeksowania  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        extraPaths: ["../team-docs", "/srv/shared-notes"],      },    },  },}
[/code]

Ścieżki mogą być bezwzględne lub względne względem przestrzeni roboczej. Katalogi są skanowane rekurencyjnie pod kątem plików `.md`. Obsługa dowiązań symbolicznych zależy od aktywnego backendu: wbudowany silnik ignoruje dowiązania symboliczne, natomiast QMD stosuje zachowanie bazowego skanera QMD.

Do wyszukiwania transkryptów między agentami w zakresie agenta użyj `agents.list[].memorySearch.qmd.extraCollections` zamiast `memory.qmd.paths`. Te dodatkowe kolekcje używają tego samego kształtu `{ path, name, pattern? }`, ale są scalane osobno dla każdego agenta i mogą zachować jawne współdzielone nazwy, gdy ścieżka wskazuje poza bieżącą przestrzeń roboczą. Jeśli ta sama rozwiązana ścieżka pojawi się zarówno w `memory.qmd.paths`, jak i `memorySearch.qmd.extraCollections`, QMD zachowuje pierwszy wpis i pomija duplikat.

* * *

## Pamięć multimodalna (Gemini)

Indeksuj obrazy i audio obok Markdown przy użyciu Gemini Embedding 2:

Klucz | Typ | Domyślne | Opis  
---|---|---|---  
`multimodal.enabled` | `boolean` | `false` | Włącz indeksowanie multimodalne  
`multimodal.modalities` | `string[]` | \-- | `["image"]`, `["audio"]` lub `["all"]`  
`multimodal.maxFileBytes` | `number` | `10000000` | Maks. rozmiar pliku do indeksowania  
  
Obsługiwane formaty: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.heic`, `.heif` (obrazy); `.mp3`, `.wav`, `.ogg`, `.opus`, `.m4a`, `.aac`, `.flac` (audio).

* * *

## Pamięć podręczna embeddingów

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`cache.enabled` | `boolean` | `false` | Buforuj embeddingi fragmentów w SQLite  
`cache.maxEntries` | `number` | `50000` | Maksymalna liczba buforowanych embeddingów  
  
Zapobiega ponownemu tworzeniu embeddingów dla niezmienionego tekstu podczas ponownego indeksowania lub aktualizacji transkrypcji.

* * *

## Indeksowanie wsadowe

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`remote.nonBatchConcurrency` | `number` | `4` | Równoległe embeddingi inline  
`remote.batch.enabled` | `boolean` | `false` | Włącz API embeddingów wsadowych  
`remote.batch.concurrency` | `number` | `2` | Równoległe zadania wsadowe  
`remote.batch.wait` | `boolean` | `true` | Czekaj na zakończenie wsadu  
`remote.batch.pollIntervalMs` | `number` | \-- | Interwał odpytywania  
`remote.batch.timeoutMinutes` | `number` | \-- | Limit czasu wsadu  
  
Dostępne dla `openai`, `gemini` i `voyage`. W przypadku dużych uzupełnień OpenAI batch jest zwykle najszybszy i najtańszy.

`remote.nonBatchConcurrency` steruje wywołaniami embeddingów inline używanymi przez lokalnych/samodzielnie hostowanych dostawców oraz dostawców hostowanych, gdy API wsadowe dostawcy nie są aktywne. Ollama domyślnie używa `1` dla indeksowania niewsadowego, aby nie przeciążać mniejszych hostów lokalnych; ustaw wyższą wartość na większych maszynach.

To ustawienie jest niezależne od `sync.embeddingBatchTimeoutSeconds`, które kontroluje limit czasu dla wywołań embeddingów inline.

* * *

## Wyszukiwanie w pamięci sesji (eksperymentalne)

Indeksuj transkrypcje sesji i udostępniaj je przez `memory_search`:

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`experimental.sessionMemory` | `boolean` | `false` | Włącz indeksowanie sesji  
`sources` | `string[]` | `["memory"]` | Dodaj `"sessions"`, aby uwzględnić transkrypcje  
`sync.sessions.deltaBytes` | `number` | `100000` | Próg bajtów do ponownego indeksowania  
`sync.sessions.deltaMessages` | `number` | `50` | Próg wiadomości do ponownego indeksowania  
  
* * *

## Przyspieszenie wektorowe SQLite (sqlite-vec)

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`store.vector.enabled` | `boolean` | `true` | Użyj sqlite-vec do zapytań wektorowych  
`store.vector.extensionPath` | `string` | bundled | Zastąp ścieżkę sqlite-vec  
  
Gdy sqlite-vec jest niedostępny, OpenClaw automatycznie wraca do podobieństwa cosinusowego obliczanego w procesie.

* * *

## Przechowywanie indeksu

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`store.path` | `string` | `~/.openclaw/memory/{agentId}.sqlite` | Lokalizacja indeksu (obsługuje token `{agentId}`)  
`store.fts.tokenizer` | `string` | `unicode61` | Tokenizer FTS5 (`unicode61` lub `trigram`)  
  
* * *

## Konfiguracja backendu QMD

Ustaw `memory.backend = "qmd"`, aby włączyć. Wszystkie ustawienia QMD znajdują się w `memory.qmd`:

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`command` | `string` | `qmd` | Ścieżka do pliku wykonywalnego QMD; ustaw ścieżkę bezwzględną, gdy `PATH` usługi różni się od powłoki  
`searchMode` | `string` | `search` | Polecenie wyszukiwania: `search`, `vsearch`, `query`  
`includeDefaultMemory` | `boolean` | `true` | Automatycznie indeksuj `MEMORY.md` \+ `memory/**/*.md`  
`paths[]` | `array` | \-- | Dodatkowe ścieżki: `{ name, path, pattern? }`  
`sessions.enabled` | `boolean` | `false` | Indeksuj transkrypcje sesji  
`sessions.retentionDays` | `number` | \-- | Przechowywanie transkrypcji  
`sessions.exportDir` | `string` | \-- | Katalog eksportu  
  
`searchMode: "search"` jest wyłącznie leksykalne/BM25. OpenClaw nie uruchamia sond gotowości wektorów semantycznych ani konserwacji osadzeń QMD dla tego trybu, także podczas `memory status --deep`; `vsearch` i `query` nadal wymagają gotowości wektorów QMD oraz osadzeń.

OpenClaw preferuje bieżącą kolekcję QMD i kształty zapytań MCP, ale zachowuje działanie starszych wydań QMD, próbując w razie potrzeby zgodnych flag wzorców kolekcji i starszych nazw narzędzi MCP. Gdy QMD ogłasza obsługę wielu filtrów kolekcji, kolekcje z tego samego źródła są przeszukiwane za pomocą jednego procesu QMD; starsze kompilacje QMD zachowują ścieżkę zgodności dla poszczególnych kolekcji. To samo źródło oznacza, że trwałe kolekcje pamięci są grupowane razem, natomiast kolekcje transkryptów sesji pozostają osobną grupą, dzięki czemu dywersyfikacja źródeł nadal ma oba wejścia.

Harmonogram aktualizacji Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`update.interval` | `string` | `5m` | Interwał odświeżania  
`update.debounceMs` | `number` | `15000` | Debounce zmian plików  
`update.onBoot` | `boolean` | `true` | Odświeżaj, gdy długotrwały menedżer QMD się otwiera; steruje też opcjonalnym odświeżaniem przy starcie  
`update.startup` | `string` | `off` | Opcjonalne odświeżanie przy starcie bramy: `off`, `idle` albo `immediate`  
`update.startupDelayMs` | `number` | `120000` | Opóźnienie przed uruchomieniem odświeżania `startup: "idle"`  
`update.waitForBootSync` | `boolean` | `false` | Blokuj otwarcie menedżera do czasu zakończenia jego początkowego odświeżenia  
`update.embedInterval` | `string` | \-- | Osobny rytm osadzeń  
`update.commandTimeoutMs` | `number` | \-- | Limit czasu dla poleceń QMD  
`update.updateTimeoutMs` | `number` | \-- | Limit czasu dla operacji aktualizacji QMD  
`update.embedTimeoutMs` | `number` | \-- | Limit czasu dla operacji osadzania QMD  
Limity Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`limits.maxResults` | `number` | `6` | Maksymalna liczba wyników wyszukiwania  
`limits.maxSnippetChars` | `number` | \-- | Ogranicz długość fragmentu  
`limits.maxInjectedChars` | `number` | \-- | Ogranicz łączną liczbę wstrzykiwanych znaków  
`limits.timeoutMs` | `number` | `4000` | Limit czasu wyszukiwania  
Zakres

Kontroluje, które sesje mogą otrzymywać wyniki wyszukiwania QMD. Ten sam schemat co [`session.sendPolicy`](</pl/gateway/config-agents#session>):

json5Copy code
[code]
    {  memory: {    qmd: {      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },    },  },}
[/code]

Domyślna konfiguracja dostarczana z produktem zezwala na sesje bezpośrednie i kanałowe, nadal odmawiając grupom.

Domyślnie tylko DM. `match.keyPrefix` dopasowuje znormalizowany klucz sesji; `match.rawKeyPrefix` dopasowuje surowy klucz wraz z `agent:<id>:`.

Cytowania

`memory.citations` dotyczy wszystkich backendów:

Wartość | Zachowanie  
---|---  
`auto` (domyślnie) | Dołącz stopkę `Source: <path#line>` do fragmentów  
`on` | Zawsze dołączaj stopkę  
`off` | Pomijaj stopkę (ścieżka nadal jest przekazywana wewnętrznie do agenta)  
  
Odświeżenia QMD przy rozruchu używają jednorazowej ścieżki podprocesu podczas startu bramy. Długotrwały menedżer QMD nadal odpowiada za zwykły obserwator plików i timery interwałów, gdy wyszukiwanie w pamięci zostanie otwarte do użytku interaktywnego.

### Pełny przykład QMD

json5Copy code
[code]
    {  memory: {    backend: "qmd",    citations: "auto",    qmd: {      includeDefaultMemory: true,      update: { interval: "5m", debounceMs: 15000 },      limits: { maxResults: 6, timeoutMs: 4000 },      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },      paths: [{ name: "docs", path: "~/notes", pattern: "**/*.md" }],    },  },}
[/code]

* * *

## Dreaming

Dreaming konfiguruje się w `plugins.entries.memory-core.config.dreaming`, a nie w `agents.defaults.memorySearch`.

Dreaming działa jako jeden zaplanowany przebieg i używa wewnętrznych faz light/deep/REM jako szczegółu implementacyjnego.

Opis zachowania koncepcyjnego i poleceń ukośnikowych znajdziesz w [Dreaming](</pl/concepts/dreaming>).

### Ustawienia użytkownika

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`enabled` | `boolean` | `false` | Włącz lub wyłącz Dreaming w całości  
`frequency` | `string` | `0 3 * * *` | Opcjonalny rytm Cron dla pełnego przebiegu Dreaming  
`model` | `string` | model domyślny | Opcjonalne nadpisanie modelu subagenta Dream Diary  
  
### Przykład

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-core": {        subagent: {          allowModelOverride: true,          allowedModels: ["anthropic/claude-sonnet-4-6"],        },        config: {          dreaming: {            enabled: true,            frequency: "0 3 * * *",            model: "anthropic/claude-sonnet-4-6",          },        },      },    },  },}
[/code]

## Powiązane

  * [Dokumentacja konfiguracji](</pl/gateway/configuration-reference>)
  * [Omówienie pamięci](</pl/concepts/memory>)
  * [Wyszukiwanie w pamięci](</pl/concepts/memory-search>)


Was this useful?YesNo
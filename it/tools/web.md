---
title: Ricerca web
source_url: https://docs.openclaw.ai/it/tools/web
scraped_at: 2026-05-25
---

Lo strumento `web_search` cerca nel web usando il provider configurato e restituisce risultati. I risultati sono memorizzati nella cache per query per 15 minuti (configurabile).

OpenClaw include anche `x_search` per i post di X (in precedenza Twitter) e `web_fetch` per il recupero leggero di URL. In questa fase, `web_fetch` resta locale mentre `web_search` e `x_search` possono usare xAI Responses internamente.

## Avvio rapido

* ### Scegli un provider

Scegli un provider e completa l'eventuale configurazione richiesta. Alcuni provider sono senza chiave, mentre altri usano chiavi API. Consulta le pagine dei provider qui sotto per i dettagli.

* ### Configura

bashCopy code
[code]
    openclaw configure --section web
[/code]

Questo memorizza il provider e le eventuali credenziali necessarie. Puoi anche impostare una variabile d'ambiente (per esempio `BRAVE_API_KEY`) e saltare questo passaggio per i provider basati su API.

* ### Usalo

L'agente ora può chiamare `web_search`:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Per i post di X, usa:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Scegliere un provider

[**Brave Search** Risultati strutturati con frammenti. Supporta la modalità `llm-context` e filtri per paese/lingua. È disponibile un piano gratuito. ](</it/tools/brave-search>) [**DuckDuckGo** Ripiego senza chiave. Non è richiesta alcuna chiave API. Integrazione non ufficiale basata su HTML. ](</it/tools/duckduckgo-search>) [**Exa** Ricerca neurale + per parole chiave con estrazione dei contenuti (evidenziazioni, testo, riepiloghi). ](</it/tools/exa-search>) [**Firecrawl** Risultati strutturati. Da usare preferibilmente con `firecrawl_search` e `firecrawl_scrape` per l'estrazione approfondita. ](</it/tools/firecrawl>) [**Gemini** Risposte sintetizzate dall'IA con citazioni tramite ancoraggio a Google Search. ](</it/tools/gemini-search>) [**Grok** Risposte sintetizzate dall'IA con citazioni tramite ancoraggio web di xAI. ](</it/tools/grok-search>) [**Kimi** Risposte sintetizzate dall'IA con citazioni tramite la ricerca web Moonshot; i ripieghi chat non ancorati falliscono esplicitamente. ](</it/tools/kimi-search>) [**MiniMax Search** Risultati strutturati tramite l'API di ricerca MiniMax Token Plan. ](</it/tools/minimax-search>) [**Ollama Web Search** Ricerca tramite un host Ollama locale con accesso effettuato o l'API Ollama ospitata. ](</it/tools/ollama-search>) [**Perplexity** Risultati strutturati con controlli per l'estrazione dei contenuti e filtro per domini. ](</it/tools/perplexity-search>) [**SearXNG** Metaricerca ospitata in autonomia. Non è richiesta alcuna chiave API. Aggrega Google, Bing, DuckDuckGo e altro. ](</it/tools/searxng-search>) [**Tavily** Risultati strutturati con profondità di ricerca, filtro per argomento e `tavily_extract` per l'estrazione da URL. ](</it/tools/tavily>)

### Confronto tra provider

Provider | Stile dei risultati | Filtri | Chiave API  
---|---|---|---  
[Brave](</it/tools/brave-search>) | Frammenti strutturati | Paese, lingua, periodo, modalità `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</it/tools/duckduckgo-search>) | Frammenti strutturati | \-- | Nessuna (senza chiave)  
[Exa](</it/tools/exa-search>) | Strutturati + estratti | Modalità neurale/per parole chiave, data, estrazione dei contenuti | `EXA_API_KEY`  
[Firecrawl](</it/tools/firecrawl>) | Frammenti strutturati | Tramite lo strumento `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</it/tools/gemini-search>) | Sintetizzati dall'IA + citazioni | \-- | `GEMINI_API_KEY`  
[Grok](</it/tools/grok-search>) | Sintetizzati dall'IA + citazioni | \-- | `XAI_API_KEY`  
[Kimi](</it/tools/kimi-search>) | Sintetizzati dall'IA + citazioni; fallisce sui ripieghi chat non ancorati | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</it/tools/minimax-search>) | Frammenti strutturati | Regione (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</it/tools/ollama-search>) | Frammenti strutturati | \-- | Nessuna per host locali con accesso effettuato; `OLLAMA_API_KEY` per la ricerca diretta su `https://ollama.com`  
[Perplexity](</it/tools/perplexity-search>) | Frammenti strutturati | Paese, lingua, periodo, domini, limiti dei contenuti | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</it/tools/searxng-search>) | Frammenti strutturati | Categorie, lingua | Nessuna (ospitato in autonomia)  
[Tavily](</it/tools/tavily>) | Frammenti strutturati | Tramite lo strumento `tavily_search` | `TAVILY_API_KEY`  
  
## Rilevamento automatico

## Ricerca web nativa di OpenAI

I modelli diretti OpenAI Responses usano automaticamente lo strumento `web_search` ospitato da OpenAI quando la ricerca web di OpenClaw è abilitata e non è fissato alcun provider gestito. Questo comportamento è gestito dal provider nel Plugin OpenAI incluso e si applica solo al traffico API OpenAI nativo, non agli URL base di proxy compatibili con OpenAI o alle route Azure. Imposta `tools.web.search.provider` su un altro provider, come `brave`, per mantenere lo strumento `web_search` gestito per i modelli OpenAI, oppure imposta `tools.web.search.enabled: false` per disabilitare sia la ricerca gestita sia la ricerca OpenAI nativa.

## Ricerca web nativa di Codex

I modelli compatibili con Codex possono facoltativamente usare lo strumento `web_search` Responses nativo del provider invece della funzione `web_search` gestita di OpenClaw.

  * Configuralo in `tools.web.search.openaiCodex`
  * Si attiva solo per i modelli compatibili con Codex (`openai-codex/*` o provider che usano `api: "openai-codex-responses"`)
  * `web_search` gestito continua ad applicarsi ai modelli non Codex
  * `mode: "cached"` è l'impostazione predefinita e consigliata
  * `tools.web.search.enabled: false` disabilita sia la ricerca gestita sia quella nativa

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Se la ricerca Codex nativa è abilitata ma il modello corrente non è compatibile con Codex, OpenClaw mantiene il normale comportamento `web_search` gestito.

## Sicurezza di rete

Le chiamate dei provider `web_search` gestiti usano il percorso di recupero protetto di OpenClaw. Per gli host API dei provider attendibili, OpenClaw consente risposte DNS fake-IP di Surge, Clash e sing-box in `198.18.0.0/15` e `fc00::/7` solo per quel nome host del provider. Le altre destinazioni private, di loopback, link-local e di metadati restano bloccate.

Questa autorizzazione automatica non si applica a URL `web_fetch` arbitrari. Per `web_fetch`, abilita esplicitamente `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` e `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` solo quando il tuo proxy attendibile possiede quegli intervalli sintetici.

## Configurare la ricerca web

Gli elenchi dei provider nella documentazione e nei flussi di configurazione sono alfabetici. Il rilevamento automatico mantiene un ordine di precedenza separato.

Se non è impostato alcun `provider`, OpenClaw controlla i provider in quest'ordine e usa il primo pronto:

Prima i provider basati su API:

  1. **Brave** \-- `BRAVE_API_KEY` o `plugins.entries.brave.config.webSearch.apiKey` (ordine 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` o `plugins.entries.minimax.config.webSearch.apiKey` (ordine 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY` o `models.providers.google.apiKey` (ordine 20)
  4. **Grok** \-- `XAI_API_KEY` o `plugins.entries.xai.config.webSearch.apiKey` (ordine 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` o `plugins.entries.moonshot.config.webSearch.apiKey` (ordine 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` o `plugins.entries.perplexity.config.webSearch.apiKey` (ordine 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` o `plugins.entries.firecrawl.config.webSearch.apiKey` (ordine 60)
  8. **Exa** \-- `EXA_API_KEY` o `plugins.entries.exa.config.webSearch.apiKey`; l'opzionale `plugins.entries.exa.config.webSearch.baseUrl` sostituisce l'endpoint Exa (ordine 65)
  9. **Tavily** \-- `TAVILY_API_KEY` o `plugins.entries.tavily.config.webSearch.apiKey` (ordine 70)


Poi i ripieghi senza chiave:

  10. **DuckDuckGo** \-- ripiego HTML senza chiave, senza account né chiave API (ordine 100)
  11. **Ollama Web Search** \-- ripiego senza chiave tramite l'host Ollama locale configurato quando è raggiungibile e l'accesso è stato effettuato con `ollama signin`; può riutilizzare l'autenticazione bearer del provider Ollama quando l'host la richiede, e può chiamare la ricerca diretta su `https://ollama.com` quando configurato con `OLLAMA_API_KEY` (ordine 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` o `plugins.entries.searxng.config.webSearch.baseUrl` (ordine 200)


Se non viene rilevato alcun provider, viene usato Brave come ripiego (verrà visualizzato un errore di chiave mancante che richiede di configurarne una).

## Configurazione

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

La configurazione specifica del provider (chiavi API, URL di base, modalità) si trova in `plugins.entries.<plugin>.config.webSearch.*`. Gemini può anche riutilizzare `models.providers.google.apiKey` e `models.providers.google.baseUrl` come fallback a priorità inferiore dopo la sua configurazione dedicata per la ricerca web e `GEMINI_API_KEY`. Consulta le pagine dei provider per esempi.

`tools.web.search.provider` viene convalidato rispetto agli ID dei provider di ricerca web dichiarati dai manifest dei Plugin inclusi e installati. Un errore di battitura come `"brvae"` fa fallire la convalida della configurazione invece di ricorrere silenziosamente al rilevamento automatico. Se un provider configurato ha solo prove obsolete del Plugin, come un blocco residuo `plugins.entries.<plugin>` dopo la disinstallazione di un Plugin di terze parti, OpenClaw mantiene resiliente l'avvio e segnala un avviso, così puoi reinstallare il Plugin o eseguire `openclaw doctor --fix` per ripulire la configurazione obsoleta.

La selezione del provider di fallback `web_fetch` è separata:

  * sceglilo con `tools.web.fetch.provider`
  * oppure ometti quel campo e lascia che OpenClaw rilevi automaticamente il primo provider web-fetch pronto tra le credenziali disponibili
  * `web_fetch` non in sandbox può usare provider di Plugin installati che dichiarano `contracts.webFetchProviders`; i recuperi in sandbox restano limitati a quelli inclusi
  * oggi il provider web-fetch incluso è Firecrawl, configurato in `plugins.entries.firecrawl.config.webFetch.*`


Quando scegli **Kimi** durante `openclaw onboard` o `openclaw configure --section web`, OpenClaw può anche chiedere:

  * la regione API Moonshot (`https://api.moonshot.ai/v1` o `https://api.moonshot.cn/v1`)
  * il modello predefinito di ricerca web Kimi (predefinito: `kimi-k2.6`)


Per `x_search`, configura `plugins.entries.xai.config.xSearch.*`. Usa lo stesso profilo di autenticazione xAI della chat, oppure la credenziale `XAI_API_KEY` / di ricerca web del Plugin usata dalla ricerca web Grok. La configurazione legacy `tools.web.x_search.*` viene migrata automaticamente da `openclaw doctor --fix`. Quando scegli Grok durante `openclaw onboard` o `openclaw configure --section web`, OpenClaw può anche offrire la configurazione facoltativa di `x_search` con la stessa chiave. Questo è un passaggio successivo separato all'interno del percorso Grok, non una scelta separata di provider di ricerca web di primo livello. Se scegli un altro provider, OpenClaw non mostra il prompt `x_search`.

### Archiviazione delle chiavi API

### Config file

Esegui `openclaw configure --section web` oppure imposta direttamente la chiave:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Environment variable

Imposta la variabile d'ambiente del provider nell'ambiente del processo Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Per un'installazione del gateway, inseriscila in `~/.openclaw/.env`. Consulta [Variabili d'ambiente](</it/help/faq#env-vars-and-env-loading>).

## Parametri dello strumento

Parametro | Descrizione  
---|---  
`query` | Query di ricerca (obbligatoria)  
`count` | Risultati da restituire (1-10, predefinito: 5)  
`country` | Codice paese ISO a 2 lettere (ad es. "US", "DE")  
`language` | Codice lingua ISO 639-1 (ad es. "en", "de")  
`search_lang` | Codice lingua di ricerca (solo Brave)  
`freshness` | Filtro temporale: `day`, `week`, `month` o `year`  
`date_after` | Risultati dopo questa data (AAAA-MM-GG)  
`date_before` | Risultati prima di questa data (AAAA-MM-GG)  
`ui_lang` | Codice lingua dell'interfaccia utente (solo Brave)  
`domain_filter` | Array di allowlist/denylist dei domini (solo Perplexity)  
`max_tokens` | Budget totale dei contenuti, predefinito 25000 (solo Perplexity)  
`max_tokens_per_page` | Limite di token per pagina, predefinito 2048 (solo Perplexity)  
  
## x_search

`x_search` interroga i post di X (in precedenza Twitter) usando xAI e restituisce risposte sintetizzate dall'IA con citazioni. Accetta query in linguaggio naturale e filtri strutturati facoltativi. OpenClaw abilita lo strumento `x_search` xAI integrato solo nella richiesta che serve questa chiamata allo strumento.

### Configurazione di x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` invia richieste POST a `<baseUrl>/responses` quando `plugins.entries.xai.config.xSearch.baseUrl` è impostato. Se quel campo viene omesso, ripiega su `plugins.entries.xai.config.webSearch.baseUrl`, poi sul legacy `tools.web.search.grok.baseUrl` e infine sull'endpoint pubblico xAI.

### Parametri di x_search

Parametro | Descrizione  
---|---  
`query` | Query di ricerca (obbligatoria)  
`allowed_x_handles` | Limita i risultati a specifici handle X  
`excluded_x_handles` | Escludi specifici handle X  
`from_date` | Includi solo post in questa data o successivi (AAAA-MM-GG)  
`to_date` | Includi solo post in questa data o precedenti (AAAA-MM-GG)  
`enable_image_understanding` | Consenti a xAI di ispezionare le immagini allegate ai post corrispondenti  
`enable_video_understanding` | Consenti a xAI di ispezionare i video allegati ai post corrispondenti  
  
### Esempio di x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Esempi

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Profili degli strumenti

Se usi profili degli strumenti o allowlist, aggiungi `web_search`, `x_search` o `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Correlati

  * [Web Fetch](</it/tools/web-fetch>) \-- recupera un URL ed estrae contenuto leggibile
  * [Browser web](</it/tools/browser>) \-- automazione completa del browser per siti con molto JavaScript
  * [Ricerca Grok](</it/tools/grok-search>) \-- Grok come provider `web_search`
  * [Ricerca web Ollama](</it/tools/ollama-search>) \-- ricerca web senza chiave tramite il tuo host Ollama


Was this useful?YesNo
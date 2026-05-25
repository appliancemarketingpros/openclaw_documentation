---
title: Websuche
source_url: https://docs.openclaw.ai/de/tools/web
scraped_at: 2026-05-25
---

Das Tool `web_search` durchsucht das Web mit Ihrem konfigurierten Provider und gibt Ergebnisse zurück. Ergebnisse werden pro Abfrage 15 Minuten lang im Cache gespeichert (konfigurierbar).

OpenClaw enthält außerdem `x_search` für Beiträge auf X (früher Twitter) und `web_fetch` für leichtgewichtiges Abrufen von URLs. In dieser Phase bleibt `web_fetch` lokal, während `web_search` und `x_search` intern xAI Responses verwenden können.

## Schnellstart

* ### Choose a provider

Wählen Sie einen Provider aus und schließen Sie alle erforderlichen Einrichtungsschritte ab. Einige Provider sind schlüsselfrei, während andere API-Schlüssel verwenden. Details finden Sie auf den Provider-Seiten unten.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web
[/code]

Dadurch werden der Provider und alle benötigten Zugangsdaten gespeichert. Sie können auch eine Umgebungsvariable setzen (zum Beispiel `BRAVE_API_KEY`) und diesen Schritt bei API-gestützten Providern überspringen.

* ### Use it

Der Agent kann jetzt `web_search` aufrufen:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Für Beiträge auf X verwenden Sie:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Provider auswählen

[**Brave Search** Strukturierte Ergebnisse mit Snippets. Unterstützt den Modus `llm-context` sowie Länder-/Sprachfilter. Kostenloser Tarif verfügbar. ](</de/tools/brave-search>) [**DuckDuckGo** Schlüsselfreier Fallback. Kein API-Schlüssel erforderlich. Inoffizielle HTML-basierte Integration. ](</de/tools/duckduckgo-search>) [**Exa** Neuronale Suche plus Stichwortsuche mit Inhaltsextraktion (Hervorhebungen, Text, Zusammenfassungen). ](</de/tools/exa-search>) [**Firecrawl** Strukturierte Ergebnisse. Am besten mit `firecrawl_search` und `firecrawl_scrape` für tiefgehende Extraktion kombiniert. ](</de/tools/firecrawl>) [**Gemini** KI-synthetisierte Antworten mit Zitaten über Google-Search-Grounding. ](</de/tools/gemini-search>) [**Grok** KI-synthetisierte Antworten mit Zitaten über xAI-Web-Grounding. ](</de/tools/grok-search>) [**Kimi** KI-synthetisierte Antworten mit Zitaten über Moonshot-Websuche; nicht geerdete Chat-Fallbacks schlagen explizit fehl. ](</de/tools/kimi-search>) [**MiniMax Search** Strukturierte Ergebnisse über die Such-API des MiniMax Token Plan. ](</de/tools/minimax-search>) [**Ollama Web Search** Suche über einen angemeldeten lokalen Ollama-Host oder die gehostete Ollama-API. ](</de/tools/ollama-search>) [**Perplexity** Strukturierte Ergebnisse mit Steuerelementen für Inhaltsextraktion und Domain-Filterung. ](</de/tools/perplexity-search>) [**SearXNG** Selbst gehostete Metasuche. Kein API-Schlüssel erforderlich. Aggregiert Google, Bing, DuckDuckGo und weitere. ](</de/tools/searxng-search>) [**Tavily** Strukturierte Ergebnisse mit Suchtiefe, Themenfilterung und `tavily_extract` für URL-Extraktion. ](</de/tools/tavily>)

### Provider-Vergleich

Provider | Ergebnisstil | Filter | API-Schlüssel  
---|---|---|---  
[Brave](</de/tools/brave-search>) | Strukturierte Snippets | Land, Sprache, Zeit, Modus `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</de/tools/duckduckgo-search>) | Strukturierte Snippets | \-- | Keiner (schlüsselfrei)  
[Exa](</de/tools/exa-search>) | Strukturiert plus extrahiert | Neuronaler/Stichwort-Modus, Datum, Inhaltsextraktion | `EXA_API_KEY`  
[Firecrawl](</de/tools/firecrawl>) | Strukturierte Snippets | Über das Tool `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</de/tools/gemini-search>) | KI-synthetisiert plus Zitate | \-- | `GEMINI_API_KEY`  
[Grok](</de/tools/grok-search>) | KI-synthetisiert plus Zitate | \-- | `XAI_API_KEY`  
[Kimi](</de/tools/kimi-search>) | KI-synthetisiert plus Zitate; schlägt bei nicht geerdeten Chat-Fallbacks fehl | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</de/tools/minimax-search>) | Strukturierte Snippets | Region (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</de/tools/ollama-search>) | Strukturierte Snippets | \-- | Keiner für angemeldete lokale Hosts; `OLLAMA_API_KEY` für direkte Suche über `https://ollama.com`  
[Perplexity](</de/tools/perplexity-search>) | Strukturierte Snippets | Land, Sprache, Zeit, Domains, Inhaltslimits | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</de/tools/searxng-search>) | Strukturierte Snippets | Kategorien, Sprache | Keiner (selbst gehostet)  
[Tavily](</de/tools/tavily>) | Strukturierte Snippets | Über das Tool `tavily_search` | `TAVILY_API_KEY`  
  
## Automatische Erkennung

## Native OpenAI-Websuche

Direkte OpenAI-Responses-Modelle verwenden automatisch das gehostete Tool `web_search` von OpenAI, wenn die OpenClaw-Websuche aktiviert und kein verwalteter Provider festgelegt ist. Dies ist Provider-eigenes Verhalten im gebündelten OpenAI-Plugin und gilt nur für nativen OpenAI-API-Datenverkehr, nicht für OpenAI-kompatible Proxy-Basis-URLs oder Azure-Routen. Setzen Sie `tools.web.search.provider` auf einen anderen Provider wie `brave`, um das verwaltete Tool `web_search` für OpenAI-Modelle beizubehalten, oder setzen Sie `tools.web.search.enabled: false`, um sowohl die verwaltete Suche als auch die native OpenAI-Suche zu deaktivieren.

## Native Codex-Websuche

Codex-fähige Modelle können optional das Provider-native Responses-Tool `web_search` anstelle der verwalteten Funktion `web_search` von OpenClaw verwenden.

  * Konfigurieren Sie es unter `tools.web.search.openaiCodex`
  * Es wird nur für Codex-fähige Modelle aktiviert (`openai-codex/*` oder Provider mit `api: "openai-codex-responses"`)
  * Verwaltetes `web_search` gilt weiterhin für Nicht-Codex-Modelle
  * `mode: "cached"` ist die Standardeinstellung und die empfohlene Einstellung
  * `tools.web.search.enabled: false` deaktiviert sowohl verwaltete als auch native Suche

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Wenn die native Codex-Suche aktiviert ist, das aktuelle Modell aber nicht Codex-fähig ist, behält OpenClaw das normale verwaltete Verhalten von `web_search` bei.

## Netzwerksicherheit

Verwaltete `web_search`-Provider-Aufrufe verwenden den geschützten Fetch-Pfad von OpenClaw. Für vertrauenswürdige Provider-API-Hosts erlaubt OpenClaw Surge-, Clash- und sing-box-Fake-IP- DNS-Antworten in `198.18.0.0/15` und `fc00::/7` nur für diesen Provider-Hostnamen. Andere private, loopback-, link-local- und Metadaten-Ziele bleiben blockiert.

Diese automatische Zulassung gilt nicht für beliebige `web_fetch`-URLs. Für `web_fetch` aktivieren Sie `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` und `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` ausdrücklich nur dann, wenn Ihr vertrauenswürdiger Proxy diese synthetischen Bereiche besitzt.

## Websuche einrichten

Provider-Listen in Dokumentation und Einrichtungsabläufen sind alphabetisch sortiert. Die automatische Erkennung verwendet eine separate Prioritätsreihenfolge.

Wenn kein `provider` festgelegt ist, prüft OpenClaw Provider in dieser Reihenfolge und verwendet den ersten, der bereit ist:

Zuerst API-gestützte Provider:

  1. **Brave** \-- `BRAVE_API_KEY` oder `plugins.entries.brave.config.webSearch.apiKey` (Reihenfolge 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` oder `plugins.entries.minimax.config.webSearch.apiKey` (Reihenfolge 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY` oder `models.providers.google.apiKey` (Reihenfolge 20)
  4. **Grok** \-- `XAI_API_KEY` oder `plugins.entries.xai.config.webSearch.apiKey` (Reihenfolge 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` oder `plugins.entries.moonshot.config.webSearch.apiKey` (Reihenfolge 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` oder `plugins.entries.perplexity.config.webSearch.apiKey` (Reihenfolge 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` oder `plugins.entries.firecrawl.config.webSearch.apiKey` (Reihenfolge 60)
  8. **Exa** \-- `EXA_API_KEY` oder `plugins.entries.exa.config.webSearch.apiKey`; optional überschreibt `plugins.entries.exa.config.webSearch.baseUrl` den Exa-Endpunkt (Reihenfolge 65)
  9. **Tavily** \-- `TAVILY_API_KEY` oder `plugins.entries.tavily.config.webSearch.apiKey` (Reihenfolge 70)


Danach schlüsselfreie Fallbacks:

  10. **DuckDuckGo** \-- schlüsselfreier HTML-Fallback ohne Konto oder API-Schlüssel (Reihenfolge 100)
  11. **Ollama Web Search** \-- schlüsselfreier Fallback über Ihren konfigurierten lokalen Ollama-Host, wenn er erreichbar und mit `ollama signin` angemeldet ist; kann die Bearer-Authentifizierung des Ollama-Providers wiederverwenden, wenn der Host sie benötigt, und kann die direkte Suche über `https://ollama.com` aufrufen, wenn mit `OLLAMA_API_KEY` konfiguriert (Reihenfolge 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` oder `plugins.entries.searxng.config.webSearch.baseUrl` (Reihenfolge 200)


Wenn kein Provider erkannt wird, fällt es auf Brave zurück (Sie erhalten einen Fehler wegen fehlendem Schlüssel, der Sie zur Konfiguration eines Schlüssels auffordert).

## Konfiguration

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

Provider-spezifische Konfiguration (API-Schlüssel, Basis-URLs, Modi) liegt unter `plugins.entries.<plugin>.config.webSearch.*`. Gemini kann außerdem `models.providers.google.apiKey` und `models.providers.google.baseUrl` als nachrangige Fallbacks nach seiner dedizierten Websuche-Konfiguration und `GEMINI_API_KEY` wiederverwenden. Beispiele finden Sie auf den Provider-Seiten.

`tools.web.search.provider` wird gegen die Websuche-Provider-IDs validiert, die von gebündelten und installierten Plugin-Manifesten deklariert werden. Ein Tippfehler wie `"brvae"` lässt die Konfigurationsvalidierung fehlschlagen, statt stillschweigend auf automatische Erkennung zurückzufallen. Wenn ein konfigurierter Provider nur veraltete Plugin-Nachweise hat, etwa einen übrig gebliebenen `plugins.entries.<plugin>`-Block nach der Deinstallation eines Drittanbieter-Plugins, hält OpenClaw den Start robust und meldet eine Warnung, damit Sie das Plugin neu installieren oder `openclaw doctor --fix` ausführen können, um die veraltete Konfiguration zu bereinigen.

Die Auswahl des Fallback-Providers für `web_fetch` ist separat:

  * wählen Sie ihn mit `tools.web.fetch.provider`
  * oder lassen Sie dieses Feld weg und OpenClaw erkennt automatisch den ersten bereiten Web-Fetch-Provider aus den verfügbaren Anmeldedaten
  * nicht sandboxed `web_fetch` kann installierte Plugin-Provider verwenden, die `contracts.webFetchProviders` deklarieren; sandboxed Abrufe bleiben auf gebündelte Provider beschränkt
  * derzeit ist der gebündelte Web-Fetch-Provider Firecrawl, konfiguriert unter `plugins.entries.firecrawl.config.webFetch.*`


Wenn Sie während `openclaw onboard` oder `openclaw configure --section web` **Kimi** wählen, kann OpenClaw außerdem nach Folgendem fragen:

  * der Moonshot-API-Region (`https://api.moonshot.ai/v1` oder `https://api.moonshot.cn/v1`)
  * dem Standardmodell für die Kimi-Websuche (Standard: `kimi-k2.6`)


Für `x_search` konfigurieren Sie `plugins.entries.xai.config.xSearch.*`. Es verwendet dasselbe xAI-Auth-Profil wie Chat oder den von der Grok-Websuche verwendeten `XAI_API_KEY` bzw. die Plugin-Websuche-Anmeldedaten. Legacy-Konfiguration unter `tools.web.x_search.*` wird von `openclaw doctor --fix` automatisch migriert. Wenn Sie während `openclaw onboard` oder `openclaw configure --section web` Grok wählen, kann OpenClaw außerdem eine optionale `x_search`-Einrichtung mit demselben Schlüssel anbieten. Dies ist ein separater Folgeschritt innerhalb des Grok-Pfads, keine separate übergeordnete Auswahl eines Websuche-Providers. Wenn Sie einen anderen Provider wählen, zeigt OpenClaw die `x_search`-Eingabeaufforderung nicht an.

### API-Schlüssel speichern

### Konfigurationsdatei

Führen Sie `openclaw configure --section web` aus oder setzen Sie den Schlüssel direkt:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Umgebungsvariable

Setzen Sie die Provider-Umgebungsvariable in der Prozessumgebung des Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Legen Sie sie bei einer Gateway-Installation in `~/.openclaw/.env` ab. Siehe [Umgebungsvariablen](</de/help/faq#env-vars-and-env-loading>).

## Tool-Parameter

Parameter | Beschreibung  
---|---  
`query` | Suchanfrage (erforderlich)  
`count` | Zurückzugebende Ergebnisse (1-10, Standard: 5)  
`country` | ISO-Ländercode mit 2 Buchstaben (z. B. "US", "DE")  
`language` | ISO-639-1-Sprachcode (z. B. "en", "de")  
`search_lang` | Suchsprachcode (nur Brave)  
`freshness` | Zeitfilter: `day`, `week`, `month` oder `year`  
`date_after` | Ergebnisse nach diesem Datum (YYYY-MM-DD)  
`date_before` | Ergebnisse vor diesem Datum (YYYY-MM-DD)  
`ui_lang` | UI-Sprachcode (nur Brave)  
`domain_filter` | Domain-Allowlist-/Denylist-Array (nur Perplexity)  
`max_tokens` | Gesamtes Inhaltsbudget, Standard 25000 (nur Perplexity)  
`max_tokens_per_page` | Token-Limit pro Seite, Standard 2048 (nur Perplexity)  
  
## x_search

`x_search` fragt X-Beiträge (ehemals Twitter) mithilfe von xAI ab und gibt KI-synthetisierte Antworten mit Quellenangaben zurück. Es akzeptiert natürlichsprachliche Abfragen und optionale strukturierte Filter. OpenClaw aktiviert das integrierte xAI-Tool `x_search` nur für die Anfrage, die diesen Tool-Aufruf bedient.

### x_search-Konfiguration

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` sendet an `<baseUrl>/responses`, wenn `plugins.entries.xai.config.xSearch.baseUrl` gesetzt ist. Wenn dieses Feld weggelassen wird, fällt es auf `plugins.entries.xai.config.webSearch.baseUrl`, dann auf die Legacy-Einstellung `tools.web.search.grok.baseUrl` und schließlich auf den öffentlichen xAI-Endpunkt zurück.

### x_search-Parameter

Parameter | Beschreibung  
---|---  
`query` | Suchanfrage (erforderlich)  
`allowed_x_handles` | Ergebnisse auf bestimmte X-Handles beschränken  
`excluded_x_handles` | Bestimmte X-Handles ausschließen  
`from_date` | Nur Beiträge an oder nach diesem Datum einschließen (YYYY-MM-DD)  
`to_date` | Nur Beiträge an oder vor diesem Datum einschließen (YYYY-MM-DD)  
`enable_image_understanding` | xAI angehängte Bilder passender Beiträge prüfen lassen  
`enable_video_understanding` | xAI angehängte Videos passender Beiträge prüfen lassen  
  
### x_search-Beispiel

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Beispiele

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Tool-Profile

Wenn Sie Tool-Profile oder Allowlists verwenden, fügen Sie `web_search`, `x_search` oder `group:web` hinzu:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Verwandte Themen

  * [Web-Abruf](</de/tools/web-fetch>) \-- eine URL abrufen und lesbaren Inhalt extrahieren
  * [Webbrowser](</de/tools/browser>) \-- vollständige Browserautomatisierung für JS-lastige Websites
  * [Grok-Suche](</de/tools/grok-search>) \-- Grok als `web_search`-Provider
  * [Ollama-Websuche](</de/tools/ollama-search>) \-- schlüsselfreie Websuche über Ihren Ollama-Host


Was this useful?YesNo
---
title: Perplexity-Suche
source_url: https://docs.openclaw.ai/de/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt die Perplexity Search API als `web_search`-Provider. Sie gibt strukturierte Ergebnisse mit den Feldern `title`, `url` und `snippet` zurück.

Aus Kompatibilitätsgründen unterstützt OpenClaw außerdem ältere Setups mit Perplexity Sonar/OpenRouter. Wenn Sie `OPENROUTER_API_KEY`, einen `sk-or-...`-Schlüssel in `plugins.entries.perplexity.config.webSearch.apiKey` verwenden oder `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` setzen, wechselt der Provider zum Chat-Completions-Pfad und gibt KI-generierte Antworten mit Zitaten statt strukturierter Search-API-Ergebnisse zurück.

## Einen Perplexity-API-Schlüssel erhalten

  1. Erstellen Sie ein Perplexity-Konto unter [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Generieren Sie im Dashboard einen API-Schlüssel
  3. Speichern Sie den Schlüssel in der Konfiguration oder setzen Sie `PERPLEXITY_API_KEY` in der Gateway-Umgebung.


## OpenRouter-Kompatibilität

Wenn Sie bereits OpenRouter für Perplexity Sonar verwendet haben, behalten Sie `provider: "perplexity"` bei und setzen Sie `OPENROUTER_API_KEY` in der Gateway-Umgebung, oder speichern Sie einen `sk-or-...`-Schlüssel in `plugins.entries.perplexity.config.webSearch.apiKey`.

Optionale Kompatibilitätssteuerungen:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Konfigurationsbeispiele

### Native Perplexity Search API

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### OpenRouter-/Sonar-Kompatibilität

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Wo der Schlüssel gesetzt wird

**Über die Konfiguration:** Führen Sie `openclaw configure --section web` aus. Der Schlüssel wird in `~/.openclaw/openclaw.json` unter `plugins.entries.perplexity.config.webSearch.apiKey` gespeichert. Dieses Feld akzeptiert auch SecretRef-Objekte.

**Über die Umgebung:** Setzen Sie `PERPLEXITY_API_KEY` oder `OPENROUTER_API_KEY` in der Prozessumgebung des Gateway. Bei einer Gateway-Installation legen Sie den Wert in `~/.openclaw/.env` (oder Ihrer Dienstumgebung) ab. Siehe [Umgebungsvariablen](</de/help/faq#env-vars-and-env-loading>).

Wenn `provider: "perplexity"` konfiguriert ist und die Perplexity-Schlüssel-SecretRef nicht aufgelöst werden kann und kein Env-Fallback vorhanden ist, schlägt Start/Neuladen schnell fehl.

## Tool-Parameter

Diese Parameter gelten für den nativen Perplexity-Search-API-Pfad.

Suchanfrage.

Anzahl der zurückzugebenden Ergebnisse (1-10).

2-stelliger ISO-Ländercode (z. B. `US`, `DE`).

ISO-639-1-Sprachcode (z. B. `en`, `de`, `fr`).

Zeitfilter - `day` entspricht 24 Stunden.

Nur Ergebnisse, die nach diesem Datum veröffentlicht wurden (`YYYY-MM-DD`).

Nur Ergebnisse, die vor diesem Datum veröffentlicht wurden (`YYYY-MM-DD`).

Domain-Allowlist-/Denylist-Array (max. 20).

Gesamtes Inhaltsbudget (max. 1000000).

Token-Limit pro Seite.

Für den älteren Sonar-/OpenRouter-Kompatibilitätspfad:

  * `query`, `count` und `freshness` werden akzeptiert
  * `count` dient dort nur der Kompatibilität; die Antwort ist weiterhin eine einzige synthetisierte Antwort mit Zitaten statt einer Liste mit N Ergebnissen
  * Filter, die nur für die Search API gelten, wie `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` und `max_tokens_per_page`, geben explizite Fehler zurück


**Beispiele:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Regeln für Domain-Filter

  * Maximal 20 Domains pro Filter
  * Allowlist und Denylist können nicht in derselben Anfrage kombiniert werden
  * Verwenden Sie das Präfix `-` für Denylist-Einträge (z. B. `["-reddit.com"]`)


## Hinweise

  * Die Perplexity Search API gibt strukturierte Websuche-Ergebnisse zurück (`title`, `url`, `snippet`)
  * OpenRouter oder explizite Werte für `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` schalten Perplexity aus Kompatibilitätsgründen zurück auf Sonar-Chat-Completions
  * Sonar-/OpenRouter-Kompatibilität gibt eine synthetisierte Antwort mit Zitaten zurück, keine strukturierten Ergebniszeilen
  * Ergebnisse werden standardmäßig 15 Minuten lang zwischengespeichert (konfigurierbar über `cacheTtlMinutes`)


## Verwandt

[**Websuche-Überblick** Alle Provider und Regeln zur automatischen Erkennung. ](</de/tools/web>) [**Brave-Suche** Strukturierte Ergebnisse mit Länder- und Sprachfiltern. ](</de/tools/brave-search>) [**Exa-Suche** Neurale Suche mit Inhaltsextraktion. ](</de/tools/exa-search>) [**Perplexity-Search-API-Dokumentation** Offizielle Schnellstartanleitung und Referenz zur Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo
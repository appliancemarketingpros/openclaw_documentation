---
title: Parallele Suche
source_url: https://docs.openclaw.ai/de/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

Das Parallel-Plugin stellt zwei [Parallel](<https://parallel.ai/>) `web_search`-Provider bereit:

  * **Parallel Search (Free)** (`parallel-free`) -- Parallels kostenloses [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>). Erfordert kein Konto und keinen API-Schlüssel. Wählen Sie ihn explizit aus, wenn Sie Parallels gehosteten Suchpfad ohne Schlüssel verwenden möchten.
  * **Parallel Search** (`parallel`) -- Parallels kostenpflichtige Search API. Erfordert einen `PARALLEL_API_KEY` und bietet höhere Ratenlimits sowie Objective-Tuning.


Beide geben gerankte, LLM-optimierte Auszüge aus einem Webindex zurück, der für KI-Agenten gebaut ist. Setzen Sie `tools.web.search.provider` auf `parallel-free` oder `parallel`, um einen explizit auszuwählen.

## Plugin installieren

Installieren Sie das offizielle Plugin und starten Sie dann Gateway neu:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## API-Schlüssel (kostenpflichtiger Provider)

`parallel-free` erfordert keinen API-Schlüssel, muss aber trotzdem als verwalteter Provider ausgewählt werden. Der kostenpflichtige `parallel`-Provider benötigt einen API-Schlüssel:

* ### Create an account

Registrieren Sie sich unter [platform.parallel.ai](<https://platform.parallel.ai>) und generieren Sie einen API-Schlüssel in Ihrem Dashboard.

* ### Store the key

Setzen Sie `PARALLEL_API_KEY` in der Gateway-Umgebung oder konfigurieren Sie ihn über:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfiguration

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**Alternative per Umgebung:** Setzen Sie `PARALLEL_API_KEY` in der Gateway-Umgebung. Bei einer Gateway-Installation legen Sie ihn in `~/.openclaw/.env` ab.

## Basis-URL überschreiben

Die Basis-URL-Überschreibung gilt nur für den kostenpflichtigen `parallel`-Provider. Der kostenlose `parallel-free`-Provider verwendet immer `https://search.parallel.ai/mcp`.

Setzen Sie `plugins.entries.parallel.config.webSearch.baseUrl`, wenn Parallel-Anfragen über einen kompatiblen Proxy oder einen alternativen Parallel-Endpunkt laufen sollen (zum Beispiel den Cloudflare AI Gateway). OpenClaw normalisiert reine Hosts, indem `https://` vorangestellt wird, und hängt `/v1/search` an, sofern der Pfad nicht bereits damit endet. Der aufgelöste Endpunkt wird in den Such-Cache-Schlüssel aufgenommen, sodass Ergebnisse von verschiedenen Parallel-Endpunkten nicht geteilt werden.

## Tool-Parameter

OpenClaw stellt Parallels native Suchstruktur bereit, damit das Modell sowohl das natürlichsprachliche Ziel als auch einige kurze Keyword-Abfragen ausfüllen kann — diese Kombination [empfiehlt](<https://docs.parallel.ai/search/best-practices>) Parallel für beste Ergebnisse.

Natürlichsprachliche Beschreibung der zugrunde liegenden Frage oder des Ziels (max. 5000 Zeichen). Sollte in sich geschlossen sein.

Prägnante Keyword-Suchabfragen mit jeweils 3-6 Wörtern (1-5 Einträge, max. 200 Zeichen pro Eintrag). Geben Sie für beste Ergebnisse 2-3 unterschiedliche Abfragen an.

Zurückzugebende Ergebnisse (1-40).

Optionale Parallel-Sitzungs-ID (max. 1000 Zeichen bei `parallel`; das kostenlose `parallel-free` Search MCP begrenzt sie auf 100). Übergeben Sie die `sessionId` aus einem vorherigen Parallel-Ergebnis bei Folgesuchen, die Teil derselben Aufgabe sind, damit Parallel zugehörige Aufrufe gruppieren und spätere Ergebnisse verbessern kann. Eine ID über dem Limit wird verworfen und eine neue wird generiert.

Optionaler Bezeichner des Modells, das den Aufruf ausführt (z. B. `claude-opus-4-7`, `gpt-5.5`). Dadurch kann Parallel Standardeinstellungen auf die Fähigkeiten Ihres Modells abstimmen. Übergeben Sie den exakt aktiven Model-Slug; kürzen Sie ihn nicht auf einen Familienalias.

## Hinweise

  * Parallel rankt und komprimiert Ergebnisse anhand ihres Nutzens für LLM-Reasoning, nicht anhand menschlicher Klickrate; erwarten Sie dichte Auszüge in jedem Ergebnis statt vollständiger Seiteninhalte
  * Ergebnisauszüge kommen als `excerpts`-Array zurück und werden außerdem in das Feld `description` zusammengeführt, um mit dem generischen `web_search`-Vertrag kompatibel zu sein
  * Parallel gibt bei jeder Antwort eine `session_id` zurück; OpenClaw stellt sie als `sessionId` im Tool-Payload bereit, damit Aufrufer Folgesuchen gruppieren können
  * `searchId`, `warnings` und `usage` von Parallel werden durchgereicht, wenn vorhanden
  * OpenClaw leitet immer eine aufgelöste Ergebnisanzahl als `advanced_settings.max_results` an Parallel weiter. Das `count`-Argument des Aufrufers hat Vorrang, danach die Top-Level-Einstellung `tools.web.search.maxResults`, andernfalls OpenClaws generischer `web_search`-Standardwert (5). Dadurch bleibt das Ergebnisvolumen konsistent, wenn zwischen Providern gewechselt wird; Parallel selbst verwendet standardmäßig 10
  * Ergebnisse werden standardmäßig 15 Minuten zwischengespeichert (konfigurierbar über `cacheTtlMinutes`)
  * Der kostenlose `parallel-free`-Provider akzeptiert dieselben Parameter. Er wendet `count` clientseitig an und generiert pro Aufruf eine `session_id`, wenn keine angegeben wird.


## Verwandte Themen

  * [Websuche: Übersicht](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [Exa-Suche](</de/tools/exa-search>) \-- neuronale Suche mit Inhaltsextraktion
  * [Perplexity Search](</de/tools/perplexity-search>) \-- strukturierte Ergebnisse mit Domain-Filterung


Was this useful?YesNo

Open issue
---
title: Grok-Suche
source_url: https://docs.openclaw.ai/de/tools/grok-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt Grok als `web_search`-Provider und nutzt webgestützte Antworten von xAI, um KI-synthetisierte Antworten zu erzeugen, die durch Live-Suchergebnisse mit Zitaten belegt sind.

Derselbe xAI-API-Schlüssel kann auch das integrierte Tool `x_search` für die Suche nach X-Posts (ehemals Twitter) und das Tool `code_execution` betreiben. Wenn Sie den Schlüssel unter `plugins.entries.xai.config.webSearch.apiKey` speichern, verwendet OpenClaw ihn jetzt auch als Fallback für den gebündelten xAI-Modell-Provider.

Für postbezogene X-Metriken wie Reposts, Antworten, Lesezeichen oder Aufrufe sollten Sie `x_search` mit der exakten Post-URL oder Status-ID statt einer breiten Suchabfrage verwenden.

## Onboarding und Konfiguration

Wenn Sie **Grok** während eines der folgenden Abläufe auswählen:

  * `openclaw onboard`
  * `openclaw configure --section web`


kann OpenClaw einen separaten Folgeschritt anzeigen, um `x_search` mit demselben `XAI_API_KEY` zu aktivieren. Dieser Folgeschritt:

  * erscheint nur, nachdem Sie Grok für `web_search` ausgewählt haben
  * ist keine separate, übergeordnete Auswahl für einen Websuche-Provider
  * kann optional während desselben Ablaufs das Modell für `x_search` festlegen


Wenn Sie ihn überspringen, können Sie `x_search` später in der Konfiguration aktivieren oder ändern.

## API-Schlüssel abrufen

* ### Create a key

Rufen Sie einen API-Schlüssel von [xAI](<https://console.x.ai/>) ab.

* ### Store the key

Legen Sie `XAI_API_KEY` in der Gateway-Umgebung fest, oder konfigurieren Sie ihn über:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfiguration

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...", // optional if XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional Responses API proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "grok",      },    },  },}
[/code]

**Alternative über die Umgebung:** Legen Sie `XAI_API_KEY` in der Gateway-Umgebung fest. Für eine Gateway-Installation legen Sie ihn in `~/.openclaw/.env` ab.

## Funktionsweise

Grok nutzt webgestützte Antworten von xAI, um Antworten mit Inline-Zitaten zu synthetisieren, ähnlich dem Google-Search-Grounding-Ansatz von Gemini.

## Unterstützte Parameter

Die Grok-Suche unterstützt `query`.

`count` wird aus Kompatibilitätsgründen mit dem gemeinsamen `web_search` akzeptiert, aber Grok gibt weiterhin eine synthetisierte Antwort mit Zitaten zurück und keine Liste mit N Ergebnissen.

Provider-spezifische Filter werden derzeit nicht unterstützt.

Grok verwendet ein Provider-spezifisches Standard-Timeout von 60 Sekunden, da webgestützte Suchen mit xAI Responses länger laufen können als der gemeinsame Standardwert für `web_search`. Legen Sie `tools.web.search.timeoutSeconds` fest, um es zu überschreiben.

## Base-URL-Überschreibungen

Legen Sie `plugins.entries.xai.config.webSearch.baseUrl` fest, wenn die Grok-Websuche über einen Betreiber-Proxy oder einen xAI-kompatiblen Responses-Endpunkt geleitet werden soll. OpenClaw sendet nach dem Entfernen abschließender Schrägstriche an `<baseUrl>/responses`. `x_search` verwendet denselben Fallback aus `webSearch.baseUrl`, sofern `plugins.entries.xai.config.xSearch.baseUrl` nicht festgelegt ist.

## Verwandte Themen

  * [Übersicht zur Websuche](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [x_search in der Websuche](</de/tools/web#x_search>) \-- erstklassige X-Suche über xAI
  * [Gemini-Suche](</de/tools/gemini-search>) \-- KI-synthetisierte Antworten über Google-Grounding


Was this useful?YesNo
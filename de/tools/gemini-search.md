---
title: Gemini-Suche
source_url: https://docs.openclaw.ai/de/tools/gemini-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt Gemini-Modelle mit integriertem [Google Search-Grounding](<https://ai.google.dev/gemini-api/docs/grounding>), das KI-synthetisierte Antworten zurückgibt, die durch Live-Ergebnisse von Google Search mit Quellenangaben belegt sind.

## API-Schlüssel abrufen

* ### Schlüssel erstellen

Gehen Sie zu [Google AI Studio](<https://aistudio.google.com/apikey>) und erstellen Sie einen API-Schlüssel.

* ### Schlüssel speichern

Legen Sie `GEMINI_API_KEY` in der Gateway-Umgebung fest, verwenden Sie `models.providers.google.apiKey` erneut oder konfigurieren Sie einen dedizierten Websuchschlüssel über:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfiguration

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // optional; falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash", // default          },        },      },    },  },  tools: {    web: {      search: {        provider: "gemini",      },    },  },}
[/code]

**Reihenfolge der Zugangsdaten:** Die Gemini-Websuche verwendet zuerst `plugins.entries.google.config.webSearch.apiKey`, dann `GEMINI_API_KEY`, dann `models.providers.google.apiKey`. Bei Basis-URLs hat die dedizierte `plugins.entries.google.config.webSearch.baseUrl` Vorrang vor `models.providers.google.baseUrl`.

Bei einer Gateway-Installation legen Sie Env-Schlüssel in `~/.openclaw/.env` ab.

## Funktionsweise

Im Gegensatz zu traditionellen Such-Providern, die eine Liste von Links und Snippets zurückgeben, verwendet Gemini Google Search-Grounding, um KI-synthetisierte Antworten mit Inline-Quellenangaben zu erzeugen. Die Ergebnisse enthalten sowohl die synthetisierte Antwort als auch die Quell- URLs.

  * Quellen-URLs aus Gemini-Grounding werden automatisch von Google- Weiterleitungs-URLs in direkte URLs aufgelöst.
  * Die Weiterleitungsauflösung verwendet den SSRF-Schutzpfad (HEAD + Weiterleitungsprüfungen + http/https-Validierung), bevor die finale Quellen-URL zurückgegeben wird.
  * Die Weiterleitungsauflösung verwendet strikte SSRF-Standards, sodass Weiterleitungen zu privaten/internen Zielen blockiert werden.


## Unterstützte Parameter

Die Gemini-Suche unterstützt `query`, `freshness`, `date_after` und `date_before`.

`count` wird für die gemeinsame `web_search`-Kompatibilität akzeptiert, aber Gemini-Grounding gibt weiterhin eine synthetisierte Antwort mit Quellenangaben zurück statt einer Liste mit N Ergebnissen.

`freshness` akzeptiert `day`, `week`, `month`, `year` sowie die gemeinsamen Kurzformen `pd`, `pw`, `pm` und `py`. OpenClaw wandelt diese Werte oder einen expliziten Bereich aus `date_after`/`date_before` in den `timeRangeFilter` von Gemini Google Search-Grounding um. `country`, `language` und `domain_filter` werden nicht unterstützt.

## Modellauswahl

Das Standardmodell ist `gemini-2.5-flash` (schnell und kosteneffizient). Jedes Gemini- Modell, das Grounding unterstützt, kann über `plugins.entries.google.config.webSearch.model` verwendet werden.

## Basis-URL-Overrides

Legen Sie `plugins.entries.google.config.webSearch.baseUrl` fest, wenn die Gemini-Websuche über einen Operator-Proxy oder einen benutzerdefinierten Gemini-kompatiblen Endpunkt geleitet werden muss. Wenn dies nicht festgelegt ist, verwendet die Gemini-Websuche `models.providers.google.baseUrl` erneut. Ein einfacher Wert `https://generativelanguage.googleapis.com` wird zu `https://generativelanguage.googleapis.com/v1beta` normalisiert; benutzerdefinierte Proxy-Pfade bleiben nach dem Entfernen abschließender Schrägstriche wie angegeben erhalten.

## Verwandte Themen

  * [Web Search-Überblick](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [Brave Search](</de/tools/brave-search>) \-- strukturierte Ergebnisse mit Snippets
  * [Perplexity Search](</de/tools/perplexity-search>) \-- strukturierte Ergebnisse + Inhaltsextraktion


Was this useful?YesNo
---
title: Perplexity
source_url: https://docs.openclaw.ai/de/providers/perplexity-provider
scraped_at: 2026-05-25
---

Das Perplexity-Plugin stellt Websuchfunktionen über die Perplexity Search API oder Perplexity Sonar über OpenRouter bereit.

Eigenschaft | Wert  
---|---  
Typ | Websuch-Provider (kein Modell-Provider)  
Auth | `PERPLEXITY_API_KEY` (direkt) oder `OPENROUTER_API_KEY` (über OpenRouter)  
Konfigurationspfad | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Erste Schritte

* ### API-Schlüssel festlegen

Führen Sie den interaktiven Konfigurationsablauf für die Websuche aus:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Oder legen Sie den Schlüssel direkt fest:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Suche starten

Der Agent verwendet Perplexity automatisch für Websuchen, sobald der Schlüssel konfiguriert ist. Es sind keine weiteren Schritte erforderlich.

## Suchmodi

Das Plugin wählt den Transport automatisch anhand des API-Schlüsselpräfixes aus:

### Native Perplexity API (pplx-)

Wenn Ihr Schlüssel mit `pplx-` beginnt, verwendet OpenClaw die native Perplexity Search API. Dieser Transport gibt strukturierte Ergebnisse zurück und unterstützt Domain-, Sprach- und Datumsfilter (siehe Filteroptionen unten).

### OpenRouter / Sonar (sk-or-)

Wenn Ihr Schlüssel mit `sk-or-` beginnt, leitet OpenClaw über OpenRouter weiter und verwendet das Perplexity Sonar-Modell. Dieser Transport gibt KI-synthetisierte Antworten mit Zitierungen zurück.

Schlüsselpräfix | Transport | Funktionen  
---|---|---  
`pplx-` | Native Perplexity Search API | Strukturierte Ergebnisse, Domain-/Sprach-/Datumsfilter  
`sk-or-` | OpenRouter (Sonar) | KI-synthetisierte Antworten mit Zitierungen  
  
## Native API-Filterung

Bei Verwendung der nativen Perplexity API unterstützen Suchen die folgenden Filter:

Filter | Beschreibung | Beispiel  
---|---|---  
Land | 2-stelliger Ländercode | `us`, `de`, `jp`  
Sprache | ISO-639-1-Sprachcode | `en`, `fr`, `zh`  
Datumsbereich | Aktualitätsfenster | `day`, `week`, `month`, `year`  
Domain-Filter | Allowlist oder Denylist (max. 20 Domains) | `example.com`  
Inhaltsbudget | Token-Limits pro Antwort / pro Seite | `max_tokens`, `max_tokens_per_page`  
  
## Erweiterte Konfiguration

Umgebungsvariable für Daemon-Prozesse

Wenn der OpenClaw Gateway als Daemon (launchd/systemd) läuft, stellen Sie sicher, dass `PERPLEXITY_API_KEY` für diesen Prozess verfügbar ist.

OpenRouter-Proxy-Einrichtung

Wenn Sie Perplexity-Suchen lieber über OpenRouter leiten möchten, legen Sie statt eines nativen Perplexity-Schlüssels einen `OPENROUTER_API_KEY` (Präfix `sk-or-`) fest. OpenClaw erkennt das Präfix und wechselt automatisch zum Sonar-Transport.

## Verwandte Themen

[**Perplexity-Suchtool** Wie der Agent Perplexity-Suchen aufruft und Ergebnisse interpretiert. ](</de/tools/perplexity-search>) [**Konfigurationsreferenz** Vollständige Konfigurationsreferenz einschließlich Plugin-Einträgen. ](</de/gateway/configuration-reference>)

Was this useful?YesNo
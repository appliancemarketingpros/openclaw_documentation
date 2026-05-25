---
title: Arcee AI
source_url: https://docs.openclaw.ai/de/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) bietet Zugriff auf die Trinity-Familie von Mixture-of-Experts-Modellen über eine OpenAI-kompatible API. Alle Trinity-Modelle sind unter Apache 2.0 lizenziert.

Auf Arcee AI-Modelle kann direkt über die Arcee-Plattform oder über [OpenRouter](</de/providers/openrouter>) zugegriffen werden.

Eigenschaft | Wert  
---|---  
Provider | `arcee`  
Auth | `ARCEEAI_API_KEY` (direkt) oder `OPENROUTER_API_KEY` (über OpenRouter)  
API | OpenAI-kompatibel  
Basis-URL | `https://api.arcee.ai/api/v1` (direkt) oder `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Erste Schritte

### Direkt (Arcee-Plattform)

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel bei [Arcee AI](<https://chat.arcee.ai/>).

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Über OpenRouter

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel bei [OpenRouter](<https://openrouter.ai/keys>).

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Dieselben Modell-Refs funktionieren sowohl für direkte als auch für OpenRouter-Setups (zum Beispiel `arcee/trinity-large-thinking`).

## Nicht interaktive Einrichtung

### Direkt (Arcee-Plattform)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Über OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Integrierter Katalog

OpenClaw liefert derzeit diesen gebündelten Arcee-Katalog aus:

Modell-Ref | Name | Eingabe | Kontext | Kosten (Ein-/Ausgabe pro 1 Mio.) | Hinweise  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | Text | 256K | $0.25 / $0.90 | Standardmodell; Reasoning aktiviert  
`arcee/trinity-large-preview` | Trinity Large Preview | Text | 128K | $0.25 / $1.00 | Allzweckmodell; 400B Parameter, 13B aktiv  
`arcee/trinity-mini` | Trinity Mini 26B | Text | 128K | $0.045 / $0.15 | Schnell und kosteneffizient; Function Calling  
  
## Unterstützte Funktionen

Funktion | Unterstützt  
---|---  
Streaming | Ja  
Tool-Nutzung / Function Calling | Ja (Trinity Mini, Trinity Large Preview)  
Strukturierte Ausgabe (JSON-Modus und JSON-Schema) | Ja  
Extended Thinking | Ja (Trinity Large Thinking; Tools deaktiviert)  
  
Hinweis zur Umgebung

Wenn der Gateway als Daemon ausgeführt wird (launchd/systemd), stellen Sie sicher, dass `ARCEEAI_API_KEY` (oder `OPENROUTER_API_KEY`) für diesen Prozess verfügbar ist (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).

OpenRouter-Routing

Wenn Sie Arcee-Modelle über OpenRouter verwenden, gelten dieselben `arcee/*`-Modell-Refs. OpenClaw übernimmt das Routing transparent basierend auf Ihrer Auth-Auswahl. Details zur OpenRouter-spezifischen Konfiguration finden Sie in der [OpenRouter-Provider-Dokumentation](</de/providers/openrouter>).

## Verwandt

[**OpenRouter** Zugriff auf Arcee-Modelle und viele weitere über einen einzigen API-Schlüssel. ](</de/providers/openrouter>) [**Modellauswahl** Provider, Modell-Refs und Failover-Verhalten auswählen. ](</de/concepts/model-providers>)

Was this useful?YesNo
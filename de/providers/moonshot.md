---
title: Moonshot AI
source_url: https://docs.openclaw.ai/de/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot stellt die Kimi API mit OpenAI-kompatiblen Endpunkten bereit. Konfigurieren Sie den Provider und setzen Sie das Standardmodell auf `moonshot/kimi-k2.6`, oder verwenden Sie Kimi Coding mit `kimi/kimi-for-coding`.

## Integrierter Modellkatalog

Modellreferenz | Name | Schlussfolgern | Eingabe | Kontext | Max. Ausgabe  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Nein | Text, Bild | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Nein | Text, Bild | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Ja | Text | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Ja | Text | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Nein | Text | 256,000 | 16,384  
  
Gebündelte Kostenschätzungen für aktuelle von Moonshot gehostete K2-Modelle verwenden die von Moonshot veröffentlichten nutzungsbasierten Tarife: Kimi K2.6 kostet 0,16 USD/MTok bei Cache-Treffern, 0,95 USD/MTok Eingabe und 4,00 USD/MTok Ausgabe; Kimi K2.5 kostet 0,10 USD/MTok bei Cache-Treffern, 0,60 USD/MTok Eingabe und 3,00 USD/MTok Ausgabe. Andere ältere Katalogeinträge behalten Nullkosten-Platzhalter, sofern Sie sie nicht in der Konfiguration überschreiben.

## Erste Schritte

Wählen Sie Ihren Provider und folgen Sie den Einrichtungsschritten.

### Moonshot API

**Am besten geeignet für:** Kimi K2-Modelle über die Moonshot Open Platform.

* ### Endpunktregion auswählen

Authentifizierungsauswahl | Endpunkt | Region  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | International  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | China  
* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Oder für den China-Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verifizieren, dass Modelle verfügbar sind

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Live-Smoke-Test ausführen

Verwenden Sie ein isoliertes Zustandsverzeichnis, wenn Sie Modellzugriff und Kostenverfolgung verifizieren möchten, ohne Ihre normalen Sitzungen zu verändern:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

Die JSON-Antwort sollte `provider: "moonshot"` und `model: "kimi-k2.6"` melden. Der Assistant-Transkripteintrag speichert normalisierte Token-Nutzung plus geschätzte Kosten unter `usage.cost`, wenn Moonshot Nutzungsmetadaten zurückgibt.

### Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Am besten geeignet für:** codefokussierte Aufgaben über den Kimi Coding-Endpunkt.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verifizieren, dass das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Kimi-Websuche

OpenClaw liefert außerdem **Kimi** als `web_search`-Provider aus, gestützt durch Moonshot-Websuche.

* ### Interaktive Einrichtung der Websuche ausführen

bashCopy code
[code]
    openclaw configure --section web
[/code]

Wählen Sie im Websuchabschnitt **Kimi** , um `plugins.entries.moonshot.config.webSearch.*` zu speichern.

* ### Websuchregion und Modell konfigurieren

Die interaktive Einrichtung fragt Folgendes ab:

Einstellung | Optionen  
---|---  
API-Region | `https://api.moonshot.ai/v1` (international) oder `https://api.moonshot.cn/v1` (China)  
Websuchmodell | Standardmäßig `kimi-k2.6`  
  
Die Konfiguration befindet sich unter `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Erweiterte Konfiguration

Nativer Thinking-Modus

Moonshot Kimi unterstützt binäres natives Thinking:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Konfigurieren Sie es pro Modell über `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw ordnet außerdem Laufzeit-`/think`-Stufen für Moonshot zu:

`/think`-Stufe | Moonshot-Verhalten  
---|---  
`/think off` | `thinking.type=disabled`  
Jede Stufe außer off | `thinking.type=enabled`  
  
Kimi K2.6 akzeptiert außerdem ein optionales Feld `thinking.keep`, das die Mehrfachzug-Beibehaltung von `reasoning_content` steuert. Setzen Sie es auf `"all"`, um das vollständige Reasoning über Züge hinweg beizubehalten; lassen Sie es weg (oder belassen Sie es bei `null`), um die Standardstrategie des Servers zu verwenden. OpenClaw leitet `thinking.keep` nur für `moonshot/kimi-k2.6` weiter und entfernt es aus anderen Modellen.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Bereinigung von Tool-Call-IDs

Moonshot Kimi stellt tool_call-IDs in der Form `functions.<name>:<index>` bereit. OpenClaw behält sie unverändert bei, damit Tool-Aufrufe über mehrere Züge hinweg weiterhin funktionieren.

Um eine strikte Bereinigung für einen benutzerdefinierten OpenAI-kompatiblen Provider zu erzwingen, setzen Sie `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Kompatibilität mit Streaming-Nutzungsdaten

Native Moonshot-Endpunkte (`https://api.moonshot.ai/v1` und `https://api.moonshot.cn/v1`) geben Streaming-Nutzungsdaten-Kompatibilität auf dem gemeinsamen `openai-completions`-Transport an. OpenClaw leitet dies aus den Endpunktfähigkeiten ab, sodass kompatible benutzerdefinierte Provider-IDs, die dieselben nativen Moonshot-Hosts ansprechen, dasselbe Streaming-Nutzungsdaten-Verhalten übernehmen.

Mit der gebündelten K2.6-Preisgestaltung wird gestreamte Nutzung, die Eingabe-, Ausgabe- und Cache-Read-Token umfasst, außerdem in lokal geschätzte USD-Kosten für `/status`, `/usage full`, `/usage cost` und transcript-gestützte Sitzungsabrechnung umgerechnet.

Endpunkt- und Modellreferenz Provider | Präfix der Modellreferenz | Endpunkt | Auth-Umgebungsvariable  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Kimi Coding-Endpunkt | `KIMI_API_KEY`  
Websuche | Nicht zutreffend | Identisch mit der Moonshot-API-Region | `KIMI_API_KEY` oder `MOONSHOT_API_KEY`  
  
  * Die Kimi-Websuche verwendet `KIMI_API_KEY` oder `MOONSHOT_API_KEY` und nutzt standardmäßig `https://api.moonshot.ai/v1` mit dem Modell `kimi-k2.6`.
  * Überschreiben Sie Preis- und Kontextmetadaten bei Bedarf in `models.providers`.
  * Wenn Moonshot für ein Modell andere Kontextlimits veröffentlicht, passen Sie `contextWindow` entsprechend an.


## Verwandte Themen

[**Modellauswahl** Auswahl von Providern, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Websuche** Konfiguration von Websuche-Providern einschließlich Kimi. ](</de/tools/web>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema für Provider, Modelle und Plugins. ](</de/gateway/configuration-reference>) [**Moonshot Open Platform** Moonshot-API-Schlüsselverwaltung und Dokumentation. ](<https://platform.moonshot.ai>)

Was this useful?YesNo
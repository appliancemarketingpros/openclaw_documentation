---
title: SGLang
source_url: https://docs.openclaw.ai/de/providers/sglang
scraped_at: 2026-05-25
---

SGLang stellt Open-Weight-Modelle über eine OpenAI-kompatible HTTP-API bereit. OpenClaw verbindet sich mit SGLang über die Provider-Familie `openai-completions` mit automatischer Erkennung verfügbarer Modelle.

Eigenschaft | Wert  
---|---  
Provider-ID | `sglang`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Umgebungsvariable | `SGLANG_API_KEY` (beliebiger nicht leerer Wert, wenn der Server keine Authentifizierung hat)  
Onboarding-Flag | `--auth-choice sglang`  
API | OpenAI-kompatibel (`openai-completions`)  
Standard-Basis-URL | `http://127.0.0.1:30000/v1`  
Standardmodell-Platzhalter | `sglang/Qwen/Qwen3-8B`  
Streaming-Nutzung | Ja (`supportsStreamingUsage: true`)  
Preisgestaltung | Als extern kostenlos markiert (`modelPricing.external: false`)  
  
OpenClaw **erkennt** verfügbare Modelle von SGLang außerdem automatisch, wenn Sie sich mit `SGLANG_API_KEY` dafür entscheiden. Verwenden Sie `sglang/*` in `agents.defaults.models`, um die Erkennung dynamisch zu halten, wenn Sie auch eine benutzerdefinierte SGLang-Basis-URL konfigurieren. Siehe Modellerkennung (impliziter Provider) unten.

## Erste Schritte

* ### SGLang starten

Starten Sie SGLang mit einem OpenAI-kompatiblen Server. Ihre Basis-URL sollte `/v1`-Endpunkte bereitstellen (zum Beispiel `/v1/models`, `/v1/chat/completions`). SGLang läuft häufig auf:

  * `http://127.0.0.1:30000/v1`


* ### API-Schlüssel setzen

Jeder Wert funktioniert, wenn auf Ihrem Server keine Authentifizierung konfiguriert ist:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Onboarding ausführen oder ein Modell direkt festlegen

bashCopy code
[code]
    openclaw onboard
[/code]

Oder konfigurieren Sie das Modell manuell:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Modellerkennung (impliziter Provider)

Wenn `SGLANG_API_KEY` gesetzt ist (oder ein Auth-Profil vorhanden ist) und Sie `models.providers.sglang` **nicht** definieren, fragt OpenClaw Folgendes ab:

  * `GET http://127.0.0.1:30000/v1/models`


und wandelt die zurückgegebenen IDs in Modelleinträge um.

## Explizite Konfiguration (manuelle Modelle)

Verwenden Sie eine explizite Konfiguration, wenn:

  * SGLang auf einem anderen Host/Port läuft.
  * Sie `contextWindow`-/`maxTokens`-Werte fest anheften möchten.
  * Ihr Server einen echten API-Schlüssel erfordert (oder Sie Header steuern möchten).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Erweiterte Konfiguration

Proxy-artiges Verhalten

SGLang wird als proxy-artiges OpenAI-kompatibles `/v1`-Backend behandelt, nicht als nativer OpenAI-Endpunkt.

Verhalten | SGLang  
---|---  
Nur-OpenAI-Anfrageformung | Nicht angewendet  
`service_tier`, Responses `store`, Prompt-Cache-Hinweise | Nicht gesendet  
Reasoning-kompatible Payload-Formung | Nicht angewendet  
Versteckte Attributions-Header (`originator`, `version`, `User-Agent`) | Bei benutzerdefinierten SGLang-Basis-URLs nicht eingefügt  
Fehlerbehebung

**Server nicht erreichbar**

Prüfen Sie, ob der Server läuft und antwortet:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Auth-Fehler**

Wenn Anfragen mit Auth-Fehlern fehlschlagen, setzen Sie einen echten `SGLANG_API_KEY`, der zu Ihrer Serverkonfiguration passt, oder konfigurieren Sie den Provider explizit unter `models.providers.sglang`.

## Verwandte Themen

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema einschließlich Provider-Einträgen. ](</de/gateway/configuration-reference>)

Was this useful?YesNo
---
title: ds4
source_url: https://docs.openclaw.ai/de/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) stellt DeepSeek V4 Flash über ein lokales Metal-Backend mit einer OpenAI-kompatiblen `/v1`-API bereit. OpenClaw verbindet sich mit ds4 über die generische Provider-Familie `openai-completions`.

ds4 ist kein gebündeltes OpenClaw-Provider-Plugin. Konfigurieren Sie es unter `models.providers.ds4` und wählen Sie dann `ds4/deepseek-v4-flash` aus.

  * Provider-ID: `ds4`
  * Plugin: keines
  * API: OpenAI-kompatible Chat Completions (`openai-completions`)
  * Vorgeschlagene Basis-URL: `http://127.0.0.1:18000/v1`
  * Modell-ID: `deepseek-v4-flash`
  * Tool-Aufrufe: unterstützt über OpenAI-ähnliche `tools` und `tool_calls`
  * Reasoning: DeepSeek-ähnliches `thinking` und `reasoning_effort`


## Anforderungen

  * macOS mit Metal-Unterstützung.
  * Ein funktionierender ds4-Checkout mit `ds4-server` und der DeepSeek V4 Flash-GGUF-Datei.
  * Ausreichend Arbeitsspeicher für den von Ihnen gewählten Kontext. Größere `--ctx`-Werte weisen beim Serverstart mehr KV-Speicher zu.


## Schnellstart

* ### Start ds4-server

Ersetzen Sie `&lt;DS4_DIR&gt;` durch den Pfad zu Ihrem ds4-Checkout.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Die Antwort sollte `deepseek-v4-flash` enthalten.

* ### Add the OpenClaw provider config

Fügen Sie die Konfiguration aus Vollständige Konfiguration hinzu und führen Sie dann eine einmalige Modellprüfung aus:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Vollständige Konfiguration

Verwenden Sie diese Konfiguration, wenn ds4 bereits auf `127.0.0.1:18000` läuft.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Halten Sie `contextWindow` mit dem Wert `ds4-server --ctx` synchron. Halten Sie `maxTokens` mit `--tokens` synchron, es sei denn, Sie möchten absichtlich, dass OpenClaw weniger Ausgabe anfordert als die Servervorgabe.

## Start bei Bedarf

OpenClaw kann ds4 nur starten, wenn ein `ds4/...`-Modell ausgewählt ist. Fügen Sie `localService` demselben Provider-Eintrag hinzu:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` muss ein absoluter ausführbarer Pfad sein. Shell-Suche und `~`-Erweiterung werden nicht verwendet. Siehe [Lokale Modelldienste](</de/gateway/local-model-services>) für jedes `localService`-Feld.

## Think Max

ds4 wendet Think Max nur an, wenn beide Bedingungen erfüllt sind:

  * `ds4-server` startet mit `--ctx 393216` oder höher.
  * Die Anfrage verwendet `reasoning_effort: "max"` oder das entsprechende ds4-Effort-Feld.


Wenn Sie diesen großen Kontext ausführen, aktualisieren Sie sowohl die Server-Flags als auch die OpenClaw-Modellmetadaten:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Testen

Beginnen Sie mit einer direkten HTTP-Prüfung:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Testen Sie dann das OpenClaw-Modell-Routing:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Verwenden Sie für einen vollständigen Agent- und Tool-Aufruf-Smoke-Test einen Kontext von mindestens 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Erwartetes Ergebnis:

  * `executionTrace.winnerProvider` ist `ds4`
  * `executionTrace.winnerModel` ist `deepseek-v4-flash`
  * `toolSummary.calls` ist mindestens `1`
  * `finalAssistantVisibleText` beginnt mit `tool-ok`


## Fehlerbehebung

curl /v1/models cannot connect

ds4 läuft nicht oder ist nicht an Host und Port in `baseUrl` gebunden. Starten Sie `ds4-server` und versuchen Sie es dann erneut:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

Das konfigurierte `--ctx` ist für den OpenClaw-Turn zu klein. Erhöhen Sie `ds4-server --ctx` und aktualisieren Sie dann `models.providers.ds4.models[].contextWindow` entsprechend. Vollständige Agent-Turns mit Tools benötigen deutlich mehr Kontext als eine direkte curl-Anfrage mit einer einzelnen Nachricht.

Think Max does not activate

ds4 verwendet Think Max nur, wenn `--ctx` mindestens `393216` beträgt und die Anfrage `reasoning_effort: "max"` anfordert. Kleinere Kontexte fallen auf hohes Reasoning zurück.

The first request is slow

ds4 hat eine kalte Metal-Residency- und Modell-Aufwärmphase. Verwenden Sie `localService.readyTimeoutMs: 300000`, wenn OpenClaw den Server bei Bedarf startet.

## Verwandt

[**Local model services** Starten Sie lokale Modellserver bei Bedarf vor Modellanfragen. ](</de/gateway/local-model-services>) [**Local models** Wählen und betreiben Sie lokale Modell-Backends. ](</de/gateway/local-models>) [**Model providers** Konfigurieren Sie Provider-Refs, Authentifizierung und Failover. ](</de/concepts/model-providers>) [**DeepSeek** Natives DeepSeek-Provider-Verhalten und Thinking-Steuerungen. ](</de/providers/deepseek>)

Was this useful?YesNo

Open issue
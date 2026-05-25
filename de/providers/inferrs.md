---
title: Leitet ab
source_url: https://docs.openclaw.ai/de/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) kann lokale Modelle hinter einer OpenAI-kompatiblen `/v1`-API bereitstellen. OpenClaw funktioniert mit `inferrs` über den generischen `openai-completions`-Pfad.

Eigenschaft | Wert  
---|---  
Provider-ID | `inferrs` (benutzerdefiniert; unter `models.providers.inferrs` konfigurieren)  
Plugin | keines — `inferrs` ist kein gebündeltes OpenClaw-Provider-Plugin  
Auth-Umgebungsvariable | Optional. Jeder Wert funktioniert, wenn Ihr inferrs-Server keine Authentifizierung hat  
API | OpenAI-kompatibel (`openai-completions`)  
Empfohlene Basis-URL | `http://127.0.0.1:8080/v1` (oder dort, wo Ihr inferrs-Server läuft)  
  
## Erste Schritte

* ### inferrs mit einem Modell starten

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Prüfen, ob der Server erreichbar ist

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Einen OpenClaw-Provider-Eintrag hinzufügen

Fügen Sie einen expliziten Provider-Eintrag hinzu und richten Sie Ihr Standardmodell darauf aus. Siehe das vollständige Konfigurationsbeispiel unten.

## Vollständiges Konfigurationsbeispiel

Dieses Beispiel verwendet Gemma 4 auf einem lokalen `inferrs`-Server.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Start bei Bedarf

Inferrs kann auch von OpenClaw nur dann gestartet werden, wenn ein `inferrs/...`-Modell ausgewählt ist. Fügen Sie `localService` demselben Provider-Eintrag hinzu:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` muss absolut sein. Verwenden Sie `which inferrs` auf dem Gateway-Host und tragen Sie diesen Pfad in die Konfiguration ein. Die vollständige Feldreferenz finden Sie unter [Lokale Modelldienste](</de/gateway/local-model-services>).

## Erweiterte Konfiguration

Warum requiresStringContent wichtig ist

Einige `inferrs`-Chat-Completions-Routen akzeptieren nur stringbasierte `messages[].content`, keine strukturierten Content-Part-Arrays.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw fasst reine Text-Content-Parts vor dem Senden der Anfrage zu einfachen Zeichenketten zusammen.

Hinweis zu Gemma und Tool-Schema

Einige aktuelle Kombinationen aus `inferrs` und Gemma akzeptieren kleine direkte `/v1/chat/completions`-Anfragen, schlagen aber weiterhin bei vollständigen OpenClaw-Agent-Runtime- Turns fehl.

Wenn das geschieht, versuchen Sie zuerst Folgendes:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Dadurch wird die Tool-Schema-Oberfläche von OpenClaw für das Modell deaktiviert und die Prompt- Belastung für strengere lokale Backends kann reduziert werden.

Wenn sehr kleine direkte Anfragen weiterhin funktionieren, normale OpenClaw-Agent-Turns jedoch innerhalb von `inferrs` abstürzen, liegt das verbleibende Problem in der Regel am Upstream-Modell- oder Serververhalten und nicht an der Transportschicht von OpenClaw.

Manueller Smoke-Test

Testen Sie nach der Konfiguration beide Ebenen:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Wenn der erste Befehl funktioniert, der zweite jedoch fehlschlägt, prüfen Sie den Abschnitt zur Fehlerbehebung unten.

Proxy-artiges Verhalten

`inferrs` wird als Proxy-artiges OpenAI-kompatibles `/v1`-Backend behandelt, nicht als nativer OpenAI-Endpunkt.

  * Native, nur für OpenAI geltende Anfrageformung wird hier nicht angewendet
  * Kein `service_tier`, kein Responses-`store`, keine Prompt-Cache-Hinweise und keine OpenAI-Reasoning-Kompatibilitäts-Payload-Formung
  * Verborgene OpenClaw-Attributions-Header (`originator`, `version`, `User-Agent`) werden bei benutzerdefinierten `inferrs`-Basis-URLs nicht eingefügt


## Fehlerbehebung

curl /v1/models schlägt fehl

`inferrs` läuft nicht, ist nicht erreichbar oder ist nicht an den erwarteten Host/Port gebunden. Stellen Sie sicher, dass der Server gestartet ist und auf der von Ihnen konfigurierten Adresse lauscht.

messages[].content erwartet eine Zeichenkette

Setzen Sie `compat.requiresStringContent: true` im Modelleintrag. Details finden Sie im Abschnitt zu `requiresStringContent` oben.

Direkte /v1/chat/completions-Aufrufe funktionieren, aber openclaw infer model run schlägt fehl

Versuchen Sie, `compat.supportsTools: false` zu setzen, um die Tool-Schema-Oberfläche zu deaktivieren. Siehe den Hinweis zum Gemma-Tool-Schema oben.

inferrs stürzt bei größeren Agent-Turns weiterhin ab

Wenn OpenClaw keine Schemafehler mehr erhält, `inferrs` bei größeren Agent-Turns aber weiterhin abstürzt, behandeln Sie dies als Upstream-`inferrs`\- oder Modellbeschränkung. Reduzieren Sie die Prompt-Belastung oder wechseln Sie zu einem anderen lokalen Backend oder Modell.

## Verwandte Themen

[**Lokale Modelle** OpenClaw mit lokalen Modellservern ausführen. ](</de/gateway/local-models>) [**Lokale Modelldienste** Lokale Modellserver bei Bedarf für konfigurierte Provider starten. ](</de/gateway/local-model-services>) [**Gateway-Fehlerbehebung** Debugging lokaler OpenAI-kompatibler Backends, die Probes bestehen, aber bei Agent-Läufen fehlschlagen. ](</de/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Modellauswahl** Überblick über alle Provider, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>)

Was this useful?YesNo
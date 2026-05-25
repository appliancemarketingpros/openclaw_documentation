---
title: vLLM
source_url: https://docs.openclaw.ai/de/providers/vllm
scraped_at: 2026-05-25
---

vLLM kann Open-Source-Modelle (und einige benutzerdefinierte Modelle) über eine **OpenAI-kompatible** HTTP-API bereitstellen. OpenClaw verbindet sich über die `openai-completions`-API mit vLLM.

OpenClaw kann verfügbare Modelle auch **automatisch erkennen** , wenn Sie dies mit `VLLM_API_KEY` aktivieren (ein beliebiger Wert funktioniert, wenn Ihr Server keine Authentifizierung erzwingt). Verwenden Sie `vllm/*` in `agents.defaults.models`, um die Erkennung dynamisch zu halten, wenn Sie auch eine benutzerdefinierte vLLM-Basis-URL konfigurieren.

OpenClaw behandelt `vllm` als lokalen OpenAI-kompatiblen Provider, der gestreamte Nutzungsabrechnung unterstützt, sodass Status-/Kontext-Token-Zählungen aus `stream_options.include_usage`-Antworten aktualisiert werden können.

Eigenschaft | Wert  
---|---  
Provider-ID | `vllm`  
API | `openai-completions` (OpenAI-kompatibel)  
Authentifizierung | `VLLM_API_KEY`-Umgebungsvariable  
Standard-Basis-URL | `http://127.0.0.1:8000/v1`  
  
## Erste Schritte

* ### vLLM mit einem OpenAI-kompatiblen Server starten

Ihre Basis-URL sollte `/v1`-Endpunkte bereitstellen (z. B. `/v1/models`, `/v1/chat/completions`). vLLM läuft häufig unter:

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### Die API-Schlüssel-Umgebungsvariable festlegen

Ein beliebiger Wert funktioniert, wenn Ihr Server keine Authentifizierung erzwingt:

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### Ein Modell auswählen

Ersetzen Sie dies durch eine Ihrer vLLM-Modell-IDs:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### Prüfen, ob das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## Modellerkennung (impliziter Provider)

Wenn `VLLM_API_KEY` gesetzt ist (oder ein Authentifizierungsprofil vorhanden ist) und Sie `models.providers.vllm` **nicht** definieren, fragt OpenClaw Folgendes ab:

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

und konvertiert die zurückgegebenen IDs in Modelleinträge.

## Explizite Konfiguration (manuelle Modelle)

Verwenden Sie eine explizite Konfiguration, wenn:

  * vLLM auf einem anderen Host oder Port läuft
  * Sie `contextWindow`\- oder `maxTokens`-Werte festlegen möchten
  * Ihr Server einen echten API-Schlüssel erfordert (oder Sie Header steuern möchten)
  * Sie eine Verbindung zu einem vertrauenswürdigen loopback-, LAN- oder Tailscale-vLLM-Endpunkt herstellen

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Um diesen Provider dynamisch zu halten, ohne jedes Modell manuell aufzulisten, fügen Sie dem sichtbaren Modellkatalog einen Provider-Wildcard hinzu:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## Erweiterte Konfiguration

Proxy-artiges Verhalten

vLLM wird als proxy-artiges OpenAI-kompatibles `/v1`-Backend behandelt, nicht als nativer OpenAI-Endpunkt. Das bedeutet:

Verhalten | Angewendet?  
---|---  
Native OpenAI-Anfrageformung | Nein  
`service_tier` | Nicht gesendet  
Responses `store` | Nicht gesendet  
Prompt-Cache-Hinweise | Nicht gesendet  
OpenAI-Reasoning-Kompatibilitäts-Payload-Formung | Nicht angewendet  
Verborgene OpenClaw-Zuordnungsheader | Bei benutzerdefinierten Basis-URLs nicht eingefügt  
Qwen-Thinking-Steuerungen

Legen Sie für Qwen-Modelle, die über vLLM bereitgestellt werden, `params.qwenThinkingFormat: "chat-template"` im Modelleintrag fest, wenn der Server Qwen-Chat-Template-Kwargs erwartet. OpenClaw ordnet `/think off` Folgendem zu:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

Thinking-Stufen außer `off` senden `enable_thinking: true`. Wenn Ihr Endpunkt stattdessen DashScope-artige Top-Level-Flags erwartet, verwenden Sie `params.qwenThinkingFormat: "top-level"`, um `enable_thinking` im Anfrage-Root zu senden. Snake-Case `params.qwen_thinking_format` wird ebenfalls akzeptiert.

Nemotron-3-Thinking-Steuerungen

vLLM/Nemotron 3 kann Chat-Template-Kwargs verwenden, um zu steuern, ob Reasoning als verborgenes Reasoning oder sichtbarer Antworttext zurückgegeben wird. Wenn eine OpenClaw-Sitzung `vllm/nemotron-3-*` mit deaktiviertem Thinking verwendet, sendet das gebündelte vLLM-Plugin:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

Um diese Werte anzupassen, legen Sie `chat_template_kwargs` unter den Modellparametern fest. Wenn Sie auch `params.extra_body.chat_template_kwargs` festlegen, hat dieser Wert endgültigen Vorrang, da `extra_body` die letzte Request-Body-Überschreibung ist.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Qwen-Tool-Calls erscheinen als Text

Stellen Sie zuerst sicher, dass vLLM mit dem richtigen Tool-Call-Parser und Chat- Template für das Modell gestartet wurde. Beispielsweise dokumentiert vLLM `hermes` für Qwen2.5- Modelle und `qwen3_xml` für Qwen3-Coder-Modelle.

Symptome:

  * Skills oder Tools werden nie ausgeführt
  * der Assistent gibt rohes JSON/XML wie `{"name":"read","arguments":...}` aus
  * vLLM gibt ein leeres `tool_calls`-Array zurück, wenn OpenClaw `tool_choice: "auto"` sendet


Einige Qwen/vLLM-Kombinationen geben strukturierte Tool-Calls nur zurück, wenn die Anfrage `tool_choice: "required"` verwendet. Erzwingen Sie für diese Modelleinträge das OpenAI-kompatible Anfragefeld mit `params.extra_body`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

Ersetzen Sie `Qwen-Qwen2.5-Coder-32B-Instruct` durch die exakte ID, die zurückgegeben wird von:

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

Sie können dieselbe Überschreibung über die CLI anwenden:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

Dies ist ein explizit zu aktivierender Kompatibilitäts-Workaround. Er bewirkt, dass jede Modellrunde mit Tools einen Tool-Call erfordert. Verwenden Sie ihn daher nur für einen dedizierten lokalen Modelleintrag, bei dem dieses Verhalten akzeptabel ist. Verwenden Sie ihn nicht als globalen Standard für alle vLLM-Modelle, und verwenden Sie keinen Proxy, der beliebigen Assistententext blind in ausführbare Tool-Calls umwandelt.

Benutzerdefinierte Basis-URL

Wenn Ihr vLLM-Server auf einem nicht standardmäßigen Host oder Port läuft, legen Sie `baseUrl` in der expliziten Provider-Konfiguration fest:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Fehlerbehebung

Langsame erste Antwort oder Timeout des Remote-Servers

Legen Sie für große lokale Modelle, Remote-LAN-Hosts oder Tailnet-Verbindungen ein Provider-spezifisches Anfrage-Timeout fest:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` gilt nur für HTTP-Anfragen an vLLM-Modelle, einschließlich Verbindungsaufbau, Antwortheadern, Body-Streaming und dem gesamten abgesicherten Fetch-Abbruch. Ziehen Sie dies einer Erhöhung von `agents.defaults.timeoutSeconds` vor, das den gesamten Agent-Lauf steuert.

Server nicht erreichbar

Prüfen Sie, ob der vLLM-Server läuft und erreichbar ist:

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

Wenn ein Verbindungsfehler angezeigt wird, prüfen Sie Host, Port und ob vLLM im OpenAI-kompatiblen Servermodus gestartet wurde. Legen Sie für explizite loopback-, LAN- oder Tailscale-Endpunkte außerdem `models.providers.vllm.request.allowPrivateNetwork: true` fest; Provider- Anfragen blockieren URLs in privaten Netzwerken standardmäßig, sofern der Provider nicht explizit als vertrauenswürdig gilt.

Authentifizierungsfehler bei Anfragen

Wenn Anfragen mit Authentifizierungsfehlern fehlschlagen, legen Sie einen echten `VLLM_API_KEY` fest, der Ihrer Serverkonfiguration entspricht, oder konfigurieren Sie den Provider explizit unter `models.providers.vllm`.

Keine Modelle erkannt

Die automatische Erkennung erfordert, dass `VLLM_API_KEY` gesetzt ist. Wenn Sie `models.providers.vllm` definiert haben, verwendet OpenClaw nur Ihre deklarierten Modelle, es sei denn, `agents.defaults.models` enthält `"vllm/*": {}`.

Tools werden als roher Text dargestellt

Wenn ein Qwen-Modell JSON/XML-Tool-Syntax ausgibt, statt einen Skill auszuführen, prüfen Sie die Qwen-Hinweise in der erweiterten Konfiguration oben. Die übliche Lösung ist:

  * vLLM mit dem richtigen Parser/Template für dieses Modell starten
  * die exakte Modell-ID mit `openclaw models list --provider vllm` bestätigen
  * nur dann eine dedizierte modellbezogene Überschreibung `params.extra_body.tool_choice: "required"` hinzufügen, wenn `tool_choice: "auto"` weiterhin leere oder nur textbasierte Tool-Calls zurückgibt


## Verwandt

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**OpenAI** Nativer OpenAI-Provider und OpenAI-kompatibles Routenverhalten. ](</de/providers/openai>) [**OAuth und Authentifizierung** Authentifizierungsdetails und Regeln zur Wiederverwendung von Anmeldedaten. ](</de/gateway/authentication>) [**Fehlerbehebung** Häufige Probleme und wie Sie sie beheben. ](</de/help/troubleshooting>)

Was this useful?YesNo
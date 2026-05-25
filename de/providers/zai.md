---
title: Z.AI
source_url: https://docs.openclaw.ai/de/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) ist die API-Plattform für **GLM** -Modelle. Sie stellt REST-APIs für GLM bereit und verwendet API-Schlüssel für die Authentifizierung. Erstellen Sie Ihren API-Schlüssel in der Z.AI-Konsole. OpenClaw verwendet den `zai`-Provider mit einem Z.AI-API-Schlüssel.

  * Provider: `zai`
  * Authentifizierung: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (Bearer-Authentifizierung)


## Erste Schritte

### Endpoint automatisch erkennen

**Am besten für:** die meisten Nutzer. OpenClaw erkennt den passenden Z.AI-Endpoint aus dem Schlüssel und wendet automatisch die richtige Basis-URL an.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Ein Standardmodell festlegen

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Prüfen, ob das Modell aufgelistet ist

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Expliziter regionaler Endpoint

**Am besten für:** Nutzer, die einen bestimmten Coding Plan oder eine allgemeine API-Oberfläche erzwingen möchten.

* ### Die richtige Onboarding-Auswahl wählen

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Ein Standardmodell festlegen

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Prüfen, ob das Modell aufgelistet ist

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Integrierter Katalog

OpenClaw liefert den gebündelten `zai`-Provider-Katalog im Plugin-Manifest aus, sodass schreibgeschützte Auflistungen bekannte GLM-Zeilen anzeigen können, ohne die Provider-Laufzeit zu laden:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Der manifestgestützte Katalog enthält derzeit:

Modellreferenz | Hinweise  
---|---  
`zai/glm-5.1` | Standardmodell  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Erweiterte Konfiguration

Unbekannte GLM-5-Modelle vorwärtsauflösen

Unbekannte `glm-5*`-IDs werden im gebündelten Provider-Pfad weiterhin vorwärtsaufgelöst, indem Provider-eigene Metadaten aus der `glm-4.7`-Vorlage synthetisiert werden, wenn die ID der aktuellen Form der GLM-5-Familie entspricht.

Tool-Call-Streaming

`tool_stream` ist für Z.AI-Tool-Call-Streaming standardmäßig aktiviert. So deaktivieren Sie es:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking und beibehaltenes Thinking

Z.AI-Thinking folgt den `/think`-Steuerungen von OpenClaw. Wenn Thinking ausgeschaltet ist, sendet OpenClaw `thinking: { type: "disabled" }`, um Antworten zu vermeiden, die das Ausgabebudget für `reasoning_content` vor sichtbarem Text verbrauchen.

Beibehaltenes Thinking ist Opt-in, da [Z.AI](<http://Z.AI>) verlangt, dass der vollständige historische `reasoning_content` erneut abgespielt wird, was die Prompt-Tokens erhöht. Aktivieren Sie es pro Modell:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Wenn es aktiviert ist und Thinking eingeschaltet ist, sendet OpenClaw `thinking: { type: "enabled", clear_thinking: false }` und spielt vorherigen `reasoning_content` für dasselbe OpenAI-kompatible Transkript erneut ab.

Fortgeschrittene Nutzer können die exakte Provider-Payload weiterhin mit `params.extra_body.thinking` überschreiben.

Bildverständnis

Das gebündelte Z.AI-Plugin registriert Bildverständnis.

Eigenschaft | Wert  
---|---  
Modell | `glm-4.6v`  
  
Bildverständnis wird automatisch aus der konfigurierten Z.AI-Authentifizierung aufgelöst; es ist keine zusätzliche Konfiguration erforderlich.

Authentifizierungsdetails

  * [Z.AI](<http://Z.AI>) verwendet Bearer-Authentifizierung mit Ihrem API-Schlüssel.
  * Die Onboarding-Auswahl `zai-api-key` erkennt den passenden Z.AI-Endpoint automatisch aus dem Schlüsselpräfix.
  * Verwenden Sie die expliziten regionalen Auswahlen (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`), wenn Sie eine bestimmte API-Oberfläche erzwingen möchten.


## Verwandte Themen

[**GLM-Modellfamilie** Überblick über die Modellfamilie für GLM. ](</de/providers/glm>) [**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>)

Was this useful?YesNo
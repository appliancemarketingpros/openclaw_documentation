---
title: Qianfan
source_url: https://docs.openclaw.ai/de/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan ist Baidus MaaS-Plattform und stellt eine **vereinheitlichte API** bereit, die Anfragen über einen einzigen Endpunkt und API-Schlüssel an viele Modelle weiterleitet. Sie ist OpenAI-kompatibel, daher funktionieren die meisten OpenAI-SDKs durch Ändern der Basis-URL.

Eigenschaft | Wert  
---|---  
Provider | `qianfan`  
Authentifizierung | `QIANFAN_API_KEY`  
API | OpenAI-kompatibel  
Basis-URL | `https://qianfan.baidubce.com/v2`  
  
## Erste Schritte

* ### Baidu-Cloud-Konto erstellen

Registrieren Sie sich oder melden Sie sich in der [Qianfan-Konsole](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) an und stellen Sie sicher, dass der Qianfan-API-Zugriff für Sie aktiviert ist.

* ### API-Schlüssel generieren

Erstellen Sie eine neue Anwendung oder wählen Sie eine vorhandene aus und generieren Sie dann einen API-Schlüssel. Das Schlüsselformat ist `bce-v3/ALTAK-...`.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Integrierter Katalog

Modellreferenz | Eingabe | Kontext | Maximale Ausgabe | Reasoning | Hinweise  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | Text | 98,304 | 32,768 | Ja | Standardmodell  
`qianfan/ernie-5.0-thinking-preview` | Text, Bild | 119,000 | 64,000 | Ja | Multimodal  
  
## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport und Kompatibilität

Qianfan läuft über den OpenAI-kompatiblen Transportpfad, nicht über natives OpenAI-Request-Shaping. Das bedeutet, dass Standardfunktionen von OpenAI-SDKs funktionieren, Provider-spezifische Parameter jedoch möglicherweise nicht weitergeleitet werden.

Katalog und Überschreibungen

Der gebündelte Katalog enthält derzeit `deepseek-v3.2` und `ernie-5.0-thinking-preview`. Fügen Sie `models.providers.qianfan` nur hinzu oder überschreiben Sie es, wenn Sie eine benutzerdefinierte Basis-URL oder Modellmetadaten benötigen.

Fehlerbehebung

  * Stellen Sie sicher, dass Ihr API-Schlüssel mit `bce-v3/ALTAK-` beginnt und der Qianfan-API-Zugriff in der Baidu-Cloud-Konsole aktiviert ist.
  * Wenn Modelle nicht aufgelistet werden, prüfen Sie, ob der Qianfan-Dienst für Ihr Konto aktiviert ist.
  * Die Standard-Basis-URL ist `https://qianfan.baidubce.com/v2`. Ändern Sie sie nur, wenn Sie einen benutzerdefinierten Endpunkt oder Proxy verwenden.


## Verwandte Themen

[**Modellauswahl** Auswahl von Providern, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständige OpenClaw-Konfigurationsreferenz. ](</de/gateway/configuration-reference>) [**Agent-Einrichtung** Konfiguration von Agent-Standards und Modellzuweisungen. ](</de/concepts/agent>) [**Qianfan-API-Dokumentation** Offizielle Qianfan-API-Dokumentation. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo
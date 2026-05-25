---
title: Qwen
source_url: https://docs.openclaw.ai/de/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw behandelt Qwen jetzt als erstklassigen gebündelten Provider mit der kanonischen ID `qwen`. Der gebündelte Provider zielt auf die Endpunkte von Qwen Cloud / Alibaba DashScope und Coding Plan ab und sorgt dafür, dass ältere `modelstudio`-IDs als Kompatibilitätsalias weiter funktionieren.

  * Provider: `qwen`
  * Bevorzugte Umgebungsvariable: `QWEN_API_KEY`
  * Aus Kompatibilitätsgründen ebenfalls akzeptiert: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * API-Stil: OpenAI-kompatibel


## Erste Schritte

Wählen Sie Ihren Plantyp aus und folgen Sie den Einrichtungsschritten.

### Coding Plan (Abonnement)

**Am besten geeignet für:** abonnementbasierten Zugriff über den Qwen Coding Plan.

* ### API-Schlüssel abrufen

Erstellen oder kopieren Sie einen API-Schlüssel von [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Onboarding ausführen

Für den **globalen** Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

Für den **China** -Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (Pay-as-you-go)

**Am besten geeignet für:** nutzungsabhängigen Zugriff über den Standard-Model-Studio-Endpunkt, einschließlich Modellen wie `qwen3.6-plus`, die im Coding Plan möglicherweise nicht verfügbar sind.

* ### API-Schlüssel abrufen

Erstellen oder kopieren Sie einen API-Schlüssel von [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Onboarding ausführen

Für den **globalen** Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Für den **China** -Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## Plantypen und Endpunkte

Plan | Region | Auth-Choice | Endpunkt  
---|---|---|---  
Standard (Pay-as-you-go) | China | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (Pay-as-you-go) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (Abonnement) | China | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (Abonnement) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
Der Provider wählt den Endpunkt automatisch anhand Ihrer Auth-Choice aus. Kanonische Optionen verwenden die `qwen-*`-Familie; `modelstudio-*` bleibt nur für Kompatibilität erhalten. Sie können dies mit einer benutzerdefinierten `baseUrl` in der Konfiguration überschreiben.

## Integrierter Katalog

OpenClaw liefert derzeit diesen gebündelten Qwen-Katalog aus. Der konfigurierte Katalog ist endpunktbewusst: Coding-Plan-Konfigurationen lassen Modelle aus, von denen nur bekannt ist, dass sie am Standard-Endpunkt funktionieren.

Modellreferenz | Eingabe | Kontext | Hinweise  
---|---|---|---  
`qwen/qwen3.5-plus` | Text, Bild | 1,000,000 | Standardmodell  
`qwen/qwen3.6-plus` | Text, Bild | 1,000,000 | Bevorzugen Sie Standard-Endpunkte, wenn Sie dieses Modell benötigen  
`qwen/qwen3-max-2026-01-23` | Text | 262,144 | Qwen-Max-Reihe  
`qwen/qwen3-coder-next` | Text | 262,144 | Coding  
`qwen/qwen3-coder-plus` | Text | 1,000,000 | Coding  
`qwen/MiniMax-M2.5` | Text | 1,000,000 | Reasoning aktiviert  
`qwen/glm-5` | Text | 202,752 | GLM  
`qwen/glm-4.7` | Text | 202,752 | GLM  
`qwen/kimi-k2.5` | Text, Bild | 262,144 | Moonshot AI über Alibaba  
  
## Thinking-Steuerung

Für Qwen-Cloud-Modelle mit Reasoning-Unterstützung ordnet der gebündelte Provider die Thinking-Stufen von OpenClaw dem DashScope-Anfrageflag `enable_thinking` auf oberster Ebene zu. Deaktiviertes Thinking sendet `enable_thinking: false`; andere Thinking-Stufen senden `enable_thinking: true`.

## Multimodale Add-ons

Das `qwen`-Plugin stellt außerdem multimodale Funktionen auf den **Standard** \- DashScope-Endpunkten bereit (nicht auf den Coding-Plan-Endpunkten):

  * **Videoverstehen** über `qwen-vl-max-latest`
  * **Wan-Videogenerierung** über `wan2.6-t2v` (Standard), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`


So verwenden Sie Qwen als Standard-Provider für Video:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## Erweiterte Konfiguration

Bild- und Videoverstehen

Das gebündelte Qwen-Plugin registriert Medienverstehen für Bilder und Videos auf den **Standard** -DashScope-Endpunkten (nicht auf den Coding-Plan-Endpunkten).

Eigenschaft | Wert  
---|---  
Modell | `qwen-vl-max-latest`  
Unterstützte Eingabe | Bilder, Video  
  
Medienverstehen wird automatisch aus der konfigurierten Qwen-Authentifizierung aufgelöst — es ist keine zusätzliche Konfiguration erforderlich. Stellen Sie sicher, dass Sie einen Standard-Endpunkt (Pay-as-you-go) für Unterstützung beim Medienverstehen verwenden.

Verfügbarkeit von Qwen 3.6 Plus

`qwen3.6-plus` ist auf den Standard-Model-Studio-Endpunkten (Pay-as-you-go) verfügbar:

  * China: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Global: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Wenn die Coding-Plan-Endpunkte für `qwen3.6-plus` einen Fehler wegen eines „nicht unterstützten Modells“ zurückgeben, wechseln Sie zu Standard (Pay-as-you-go) statt zum Endpunkt-/Schlüsselpaar des Coding Plan.

Der gebündelte Qwen-Katalog von OpenClaw bewirbt `qwen3.6-plus` nicht auf Coding- Plan-Endpunkten, aber explizit konfigurierte `qwen/qwen3.6-plus`-Einträge unter `models.providers.qwen.models` werden auf Coding-Plan-BaseUrls berücksichtigt, sodass Sie dieses Modell aktivieren können, falls Aliyun es für Ihr Abonnement freischaltet. Die Upstream-API entscheidet weiterhin, ob der Aufruf erfolgreich ist.

Fähigkeitsplan

Das `qwen`-Plugin wird als Hersteller-Home für die gesamte Qwen- Cloud-Oberfläche positioniert, nicht nur für Coding-/Textmodelle.

  * **Text-/Chatmodelle:** jetzt gebündelt
  * **Tool-Aufrufe, strukturierte Ausgabe, Thinking:** vom OpenAI-kompatiblen Transport geerbt
  * **Bildgenerierung:** auf der Provider-Plugin-Ebene geplant
  * **Bild-/Videoverstehen:** jetzt auf dem Standard-Endpunkt gebündelt
  * **Sprache/Audio:** auf der Provider-Plugin-Ebene geplant
  * **Memory Embeddings/Reranking:** über die Embedding-Adapter-Oberfläche geplant
  * **Videogenerierung:** jetzt über die gemeinsame Videogenerierungsfunktion gebündelt

Details zur Videogenerierung

Für die Videogenerierung ordnet OpenClaw die konfigurierte Qwen-Region dem passenden DashScope-AIGC-Host zu, bevor der Auftrag übermittelt wird:

  * Global/Intl: `https://dashscope-intl.aliyuncs.com`
  * China: `https://dashscope.aliyuncs.com`


Das bedeutet, dass eine normale `models.providers.qwen.baseUrl`, die entweder auf die Coding-Plan- oder Standard-Qwen-Hosts zeigt, die Videogenerierung weiterhin auf dem korrekten regionalen DashScope-Videoendpunkt hält.

Aktuelle gebündelte Limits für Qwen-Videogenerierung:

  * Bis zu **1** Ausgabevideo pro Anfrage
  * Bis zu **1** Eingabebild
  * Bis zu **4** Eingabevideos
  * Bis zu **10 Sekunden** Dauer
  * Unterstützt `size`, `aspectRatio`, `resolution`, `audio` und `watermark`
  * Der Referenzbild-/Referenzvideomodus erfordert derzeit **entfernte http(s)-URLs**. Lokale Dateipfade werden frühzeitig abgelehnt, weil der DashScope-Videoendpunkt keine hochgeladenen lokalen Buffer für diese Referenzen akzeptiert.

Kompatibilität der Streaming-Nutzung

Native Model-Studio-Endpunkte geben die Kompatibilität der Streaming-Nutzung für den gemeinsamen `openai-completions`-Transport an. OpenClaw leitet dies jetzt aus den Endpunktfähigkeiten ab, sodass DashScope-kompatible benutzerdefinierte Provider-IDs, die auf dieselben nativen Hosts zielen, dasselbe Streaming-Nutzungsverhalten erben, anstatt speziell die integrierte `qwen`-Provider-ID zu benötigen.

Die Kompatibilität der nativen Streaming-Nutzung gilt sowohl für die Coding-Plan-Hosts als auch für die Standard-DashScope-kompatiblen Hosts:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Regionen für multimodale Endpunkte

Multimodale Oberflächen (Videoverstehen und Wan-Videogenerierung) verwenden die **Standard** -DashScope-Endpunkte, nicht die Coding-Plan-Endpunkte:

  * Globale/Intl-Standard-Basis-URL: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * China-Standard-Basis-URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`

Umgebungs- und Daemon-Einrichtung

Wenn der Gateway als Daemon ausgeführt wird (launchd/systemd), stellen Sie sicher, dass `QWEN_API_KEY` für diesen Prozess verfügbar ist (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).

## Verwandte Themen

[**Modellauswahl** Auswahl von Providern, Modell-Refs und Failover-Verhalten. ](</de/concepts/model-providers>) [**Videogenerierung** Gemeinsame Parameter für Video-Tools und Provider-Auswahl. ](</de/tools/video-generation>) [**Alibaba (ModelStudio)** Legacy-ModelStudio-Provider und Migrationshinweise. ](</de/providers/alibaba>) [**Fehlerbehebung** Allgemeine Fehlerbehebung und FAQ. ](</de/help/troubleshooting>)

Was this useful?YesNo
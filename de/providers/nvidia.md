---
title: NVIDIA
source_url: https://docs.openclaw.ai/de/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA stellt unter `https://integrate.api.nvidia.com/v1` eine OpenAI-kompatible API für offene Modelle kostenlos bereit. Authentifizieren Sie sich mit einem API-Schlüssel von [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Erste Schritte

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel unter [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Schlüssel exportieren und Onboarding ausführen

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Ein NVIDIA-Modell festlegen

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Für die nicht interaktive Einrichtung können Sie den Schlüssel auch direkt übergeben:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Integrierter Katalog

Modellreferenz | Name | Kontext | Max. Ausgabe  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Erweiterte Konfiguration

Verhalten beim automatischen Aktivieren

Der Provider wird automatisch aktiviert, wenn die Umgebungsvariable `NVIDIA_API_KEY` gesetzt ist. Über den Schlüssel hinaus ist keine explizite Provider-Konfiguration erforderlich.

Katalog und Preise

Der gebündelte Katalog ist statisch. Die Kosten sind im Quellcode standardmäßig auf `0` gesetzt, da NVIDIA derzeit kostenlosen API-Zugriff für die aufgeführten Modelle anbietet.

OpenAI-kompatibler Endpunkt

NVIDIA verwendet den standardmäßigen `/v1`-Completions-Endpunkt. Alle OpenAI-kompatiblen Tools sollten mit der NVIDIA-Basis-URL sofort funktionieren.

Langsame Antworten benutzerdefinierter Provider

Einige von NVIDIA gehostete benutzerdefinierte Modelle können länger brauchen als der standardmäßige Leerlauf- Watchdog des Modells, bevor sie den ersten Antwort-Chunk ausgeben. Erhöhen Sie bei benutzerdefinierten NVIDIA-Provider- Einträgen das Provider-Timeout, statt das Laufzeit-Timeout des gesamten Agenten zu erhöhen:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Verwandte Themen

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständige Konfigurationsreferenz für Agenten, Modelle und Provider. ](</de/gateway/configuration-reference>)

Was this useful?YesNo
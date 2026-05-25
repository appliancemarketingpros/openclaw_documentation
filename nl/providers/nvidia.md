---
title: NVIDIA
source_url: https://docs.openclaw.ai/nl/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA biedt een OpenAI-compatibele API op `https://integrate.api.nvidia.com/v1` voor open modellen gratis aan. Verifieer met een API-sleutel van [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Aan de slag

* ### Haal je API-sleutel op

Maak een API-sleutel aan op [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Exporteer de sleutel en voer onboarding uit

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Stel een NVIDIA-model in

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Voor niet-interactieve configuratie kun je de sleutel ook direct doorgeven:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Ingebouwde catalogus

Modelref | Naam | Context | Maximale uitvoer  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Geavanceerde configuratie

Gedrag voor automatisch inschakelen

De provider wordt automatisch ingeschakeld wanneer de omgevingsvariabele `NVIDIA_API_KEY` is ingesteld. Er is geen expliciete providerconfiguratie vereist buiten de sleutel.

Catalogus en prijzen

De gebundelde catalogus is statisch. Kosten staan standaard op `0` in de broncode, omdat NVIDIA momenteel gratis API-toegang biedt voor de vermelde modellen.

OpenAI-compatibel eindpunt

NVIDIA gebruikt het standaard `/v1`-completions-eindpunt. Alle OpenAI-compatibele tooling zou direct moeten werken met de NVIDIA-basis-URL.

Trage reacties van aangepaste providers

Sommige door NVIDIA gehoste aangepaste modellen kunnen langer nodig hebben dan de standaard model-idle- watchdog voordat ze een eerste antwoordchunk uitsturen. Verhoog voor aangepaste NVIDIA-providervermeldingen de provider-time-out in plaats van de runtime-time-out van de hele agent te verhogen:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Gerelateerd

[**Modelselectie** Providers, modelrefs en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledige configuratiereferentie voor agents, modellen en providers. ](</nl/gateway/configuration-reference>)

Was this useful?YesNo
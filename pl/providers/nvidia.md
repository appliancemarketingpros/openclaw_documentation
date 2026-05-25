---
title: NVIDIA
source_url: https://docs.openclaw.ai/pl/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA udostępnia API zgodne z OpenAI pod adresem `https://integrate.api.nvidia.com/v1` dla otwartych modeli za darmo. Uwierzytelnij się kluczem API z [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Pierwsze kroki

* ### Get your API key

Utwórz klucz API na [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Export the key and run onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Set an NVIDIA model

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

W przypadku konfiguracji nieinteraktywnej możesz też przekazać klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Przykład konfiguracji

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Wbudowany katalog

Odwołanie do modelu | Nazwa | Kontekst | Maks. dane wyjściowe  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Konfiguracja zaawansowana

Auto-enable behavior

Dostawca włącza się automatycznie, gdy ustawiona jest zmienna środowiskowa `NVIDIA_API_KEY`. Poza kluczem nie jest wymagana żadna jawna konfiguracja dostawcy.

Catalog and pricing

Dołączony katalog jest statyczny. Koszty domyślnie wynoszą `0` w źródle, ponieważ NVIDIA obecnie oferuje bezpłatny dostęp API dla wymienionych modeli.

OpenAI-compatible endpoint

NVIDIA używa standardowego punktu końcowego uzupełnień `/v1`. Każde narzędzie zgodne z OpenAI powinno działać od razu z bazowym adresem URL NVIDIA.

Slow custom provider responses

Niektóre modele niestandardowe hostowane przez NVIDIA mogą potrzebować więcej czasu niż domyślny limit bezczynności modelu, zanim wyemitują pierwszy fragment odpowiedzi. Dla niestandardowych wpisów dostawcy NVIDIA zwiększ limit czasu dostawcy zamiast zwiększać limit czasu całego środowiska uruchomieniowego agenta:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Powiązane

[**Model selection** Wybór dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Configuration reference** Pełna dokumentacja konfiguracji agentów, modeli i dostawców. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo
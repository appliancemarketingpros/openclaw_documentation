---
title: Fal
source_url: https://docs.openclaw.ai/pl/providers/fal
scraped_at: 2026-05-25
---

OpenClaw zawiera dołączonego dostawcę `fal` do hostowanego generowania obrazów i wideo.

Właściwość | Wartość  
---|---  
Dostawca | `fal`  
Uwierzytelnianie | `FAL_KEY` (kanoniczne; `FAL_API_KEY` działa także jako opcja zapasowa)  
API | punkty końcowe modeli fal  
  
## Pierwsze kroki

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Set a default image model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Generowanie obrazów

Dołączony dostawca generowania obrazów `fal` domyślnie używa `fal/fal-ai/flux/dev`.

Możliwość | Wartość  
---|---  
Maksymalna liczba obrazów | 4 na żądanie  
Tryb edycji | Flux: 1 obraz referencyjny; GPT Image 2: 10; Nano Banana 2: 14  
Nadpisania rozmiaru | Obsługiwane  
Proporcje obrazu | Obsługiwane dla generowania oraz edycji GPT Image 2/Nano Banana 2  
Rozdzielczość | Obsługiwana  
Format wyjściowy | `png` lub `jpeg`  
  
Użyj `outputFormat: "png"`, gdy chcesz uzyskać wyjście PNG. fal nie deklaruje w OpenClaw jawnej kontroli przezroczystego tła, więc `background: "transparent"` jest zgłaszane jako zignorowane nadpisanie dla modeli fal.

Aby używać fal jako domyślnego dostawcy obrazów:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Generowanie wideo

Dołączony dostawca generowania wideo `fal` domyślnie używa `fal/fal-ai/minimax/video-01-live`.

Możliwość | Wartość  
---|---  
Tryby | Text-to-video, referencja z pojedynczego obrazu, Seedance reference-to-video  
Środowisko uruchomieniowe | Przepływ przesyłania/statusu/wyniku oparty na kolejce dla długotrwałych zadań  
  
Available video models

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 reference-to-video config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video akceptuje do 9 obrazów, 3 wideo i 3 referencji audio za pośrednictwem wspólnych parametrów `video_generate` `images`, `videos` i `audioRefs`, z maksymalnie 12 plikami referencyjnymi łącznie.

HeyGen video-agent config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Powiązane

[**Image generation** Wspólne parametry narzędzia obrazów i wybór dostawcy. ](</pl/tools/image-generation>) [**Video generation** Wspólne parametry narzędzia wideo i wybór dostawcy. ](</pl/tools/video-generation>) [**Configuration reference** Domyślne ustawienia agenta, w tym wybór modelu obrazu i wideo. ](</pl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo
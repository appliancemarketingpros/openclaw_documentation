---
title: Vydra
source_url: https://docs.openclaw.ai/pl/providers/vydra
scraped_at: 2026-05-25
---

Wbudowany Plugin Vydra dodaje:

  * Generowanie obrazów przez `vydra/grok-imagine`
  * Generowanie wideo przez `vydra/veo3` i `vydra/kling`
  * Syntezę mowy przez obsługiwaną przez ElevenLabs trasę TTS Vydra


OpenClaw używa tego samego `VYDRA_API_KEY` dla wszystkich trzech możliwości.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `vydra`  
Plugin | wbudowany, `enabledByDefault: true`  
Zmienna środowiskowa uwierzytelniania | `VYDRA_API_KEY`  
Flaga wdrażania | `--auth-choice vydra-api-key`  
Bezpośrednia flaga CLI | `--vydra-api-key <key>`  
Kontrakty | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
Bazowy URL | `https://www.vydra.ai/api/v1` (użyj hosta `www`)  
  
## Konfiguracja

* ### Uruchom interaktywne wdrażanie

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Albo ustaw zmienną środowiskową bezpośrednio:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Wybierz domyślną możliwość

Wybierz jedną lub więcej z poniższych możliwości (obraz, wideo lub mowa) i zastosuj pasującą konfigurację.

## Możliwości

Generowanie obrazów

Domyślny model obrazu:

  * `vydra/grok-imagine`


Ustaw go jako domyślnego dostawcę obrazów:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Obecna wbudowana obsługa obejmuje tylko przekształcanie tekstu w obraz. Hostowane trasy edycji Vydra oczekują zdalnych adresów URL obrazów, a OpenClaw nie dodaje jeszcze mostka przesyłania specyficznego dla Vydra we wbudowanym Plugin.

Generowanie wideo

Zarejestrowane modele wideo:

  * `vydra/veo3` do przekształcania tekstu w wideo
  * `vydra/kling` do przekształcania obrazu w wideo


Ustaw Vydra jako domyślnego dostawcę wideo:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Uwagi:

  * `vydra/veo3` jest wbudowany tylko jako model przekształcania tekstu w wideo.
  * `vydra/kling` obecnie wymaga odwołania do zdalnego adresu URL obrazu. Przesyłanie plików lokalnych jest odrzucane z góry.
  * Obecna trasa HTTP `kling` Vydra działała niespójnie pod względem tego, czy wymaga `image_url`, czy `video_url`; wbudowany dostawca mapuje ten sam zdalny adres URL obrazu do obu pól.
  * Wbudowany Plugin pozostaje zachowawczy i nie przekazuje nieudokumentowanych pokręteł stylu, takich jak proporcje, rozdzielczość, znak wodny czy wygenerowany dźwięk.

Testy live wideo

Pokrycie live specyficzne dla dostawcy:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Wbudowany plik live Vydra obejmuje teraz:

  * `vydra/veo3` przekształcanie tekstu w wideo
  * `vydra/kling` przekształcanie obrazu w wideo z użyciem zdalnego adresu URL obrazu


W razie potrzeby nadpisz zdalny fixture obrazu:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Synteza mowy

Ustaw Vydra jako dostawcę mowy:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Wartości domyślne:

  * Model: `elevenlabs/tts`
  * Identyfikator głosu: `21m00Tcm4TlvDq8ikWAM`


Wbudowany Plugin obecnie udostępnia jeden sprawdzony domyślny głos i zwraca pliki audio MP3.

## Powiązane

[**Katalog dostawców** Przeglądaj wszystkich dostępnych dostawców. ](</pl/providers>) [**Generowanie obrazów** Wspólne parametry narzędzia obrazu i wybór dostawcy. ](</pl/tools/image-generation>) [**Generowanie wideo** Wspólne parametry narzędzia wideo i wybór dostawcy. ](</pl/tools/video-generation>) [**Dokumentacja konfiguracji** Domyślne ustawienia agentów i konfiguracja modelu. ](</pl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo
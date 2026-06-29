---
title: PixVerse
source_url: https://docs.openclaw.ai/pl/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw udostępnia `pixverse` jako oficjalny zewnętrzny Plugin do hostowanego generowania wideo PixVerse. Plugin rejestruje dostawcę `pixverse` względem kontraktu `videoGenerationProviders`.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `pixverse`  
Pakiet Pluginu | `@openclaw/pixverse-provider`  
Zmienna env auth | `PIXVERSE_API_KEY`  
Flaga onboardingu | `--auth-choice pixverse-api-key`  
Bezpośrednia flaga CLI | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (zgłoszenie `video_id` oraz odpytywanie wyniku)  
Domyślny model | `pixverse/v6`  
Domyślny region API | Międzynarodowy  
  
## Pierwsze kroki

* ### Zainstaluj Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Ustaw klucz API

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

Kreator pyta, czy użyć punktu końcowego International (`https://app-api.pixverse.ai/openapi/v2`), czy punktu końcowego CN (`https://app-api.pixverseai.cn/openapi/v2`), zanim zapisze `region` i `baseUrl` w konfiguracji dostawcy.

* ### Ustaw PixVerse jako domyślnego dostawcę wideo

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Wygeneruj wideo

Poproś agenta o wygenerowanie wideo. PixVerse zostanie użyty automatycznie.

## Obsługiwane tryby i modele

Dostawca udostępnia modele generowania PixVerse przez współdzielone narzędzie wideo OpenClaw.

Tryb | Modele | Wejście referencyjne  
---|---|---  
Tekst na wideo | `v6` (domyślny), `c1` | Brak  
Obraz na wideo | `v6` (domyślny), `c1` | 1 obraz lokalny lub zdalny  
  
Lokalne referencje obrazów są przesyłane do PixVerse przed żądaniem obrazu na wideo. Zdalne adresy URL obrazów są przekazywane przez punkt końcowy przesyłania obrazów PixVerse jako `image_url`.

Opcja | Obsługiwane wartości  
---|---  
Czas trwania | 1-15 sekund  
Rozdzielczość | `360P`, `540P`, `720P`, `1080P`  
Proporcje obrazu | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` dla tekstu na wideo  
Wygenerowany dźwięk | `audio: true`  
  
## Opcje dostawcy

Dostawca wideo akceptuje te opcjonalne klucze specyficzne dla dostawcy:

Opcja | Typ | Efekt  
---|---|---  
`seed` | number | Deterministyczne ziarno, gdy jest obsługiwane  
`negativePrompt` / `negative_prompt` | string | Negatywny prompt  
`quality` | string | Jakość PixVerse, taka jak `720p`  
`motionMode` / `motion_mode` | string | Tryb ruchu dla obrazu na wideo  
`cameraMovement` / `camera_movement` | string | Preset ruchu kamery PixVerse  
`templateId` / `template_id` | number | Aktywowany identyfikator szablonu PixVerse  
  
## Konfiguracja

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Konfiguracja zaawansowana

Region API

OpenClaw domyślnie używa międzynarodowego API PixVerse. Ustaw `models.providers.pixverse.region` ręcznie, gdy Twój klucz należy do konkretnego regionu platformy PixVerse, albo użyj `openclaw onboard --auth-choice pixverse-api-key`, aby wybrać region w kreatorze konfiguracji:

Wartość regionu | Bazowy URL API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Niestandardowy bazowy URL

Ustaw `models.providers.pixverse.baseUrl` tylko podczas routingu przez zaufane, zgodne proxy. `baseUrl` ma pierwszeństwo przed `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Odpytywanie zadania

PixVerse zwraca `video_id` z żądania generowania. OpenClaw odpytuje `/openapi/v2/video/result/{video_id}`, aż zadanie zakończy się powodzeniem, niepowodzeniem albo przekroczy limit czasu.

## Powiązane

[**Generowanie wideo** Współdzielone parametry narzędzia, wybór dostawcy i zachowanie asynchroniczne. ](</pl/tools/video-generation>) [**Informacje referencyjne o konfiguracji** Domyślne ustawienia agenta, w tym model generowania wideo. ](</pl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue
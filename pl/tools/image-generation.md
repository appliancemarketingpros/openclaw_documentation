---
title: Generowanie obrazów
source_url: https://docs.openclaw.ai/pl/tools/image-generation
scraped_at: 2026-05-25
---

Narzędzie `image_generate` pozwala agentowi tworzyć i edytować obrazy za pomocą skonfigurowanych providerów. Wygenerowane obrazy są dostarczane automatycznie jako załączniki multimedialne w odpowiedzi agenta.

## Szybki start

* ### Skonfiguruj uwierzytelnianie

Ustaw klucz API dla co najmniej jednego providera (na przykład `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`) albo zaloguj się za pomocą OpenAI Codex OAuth.

* ### Wybierz model domyślny (opcjonalnie)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth używa tego samego odwołania do modelu `openai/gpt-image-2`. Gdy skonfigurowany jest profil OAuth `openai-codex`, OpenClaw kieruje żądania obrazów przez ten profil OAuth zamiast najpierw próbować `OPENAI_API_KEY`. Jawna konfiguracja `models.providers.openai` (klucz API, niestandardowy/Azure bazowy URL) przełącza z powrotem na bezpośrednią trasę OpenAI Images API.

* ### Zapytaj agenta

_"Wygeneruj obraz przyjaznej maskotki robota."_

Agent automatycznie wywołuje `image_generate`. Lista dozwolonych narzędzi nie jest potrzebna - narzędzie jest domyślnie włączone, gdy dostępny jest provider.

## Typowe trasy

Cel | Odwołanie do modelu | Uwierzytelnianie  
---|---|---  
Generowanie obrazów OpenAI z rozliczaniem przez API | `openai/gpt-image-2` | `OPENAI_API_KEY`  
Generowanie obrazów OpenAI z uwierzytelnianiem subskrypcji Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
PNG/WebP OpenAI z przezroczystym tłem | `openai/gpt-image-1.5` | `OPENAI_API_KEY` lub OpenAI Codex OAuth  
Generowanie obrazów DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
Generowanie obrazów OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
Generowanie obrazów LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
Generowanie obrazów Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` lub `GOOGLE_API_KEY`  
  
To samo narzędzie `image_generate` obsługuje generowanie obrazu z tekstu oraz edycję obrazów referencyjnych. Użyj `image` dla jednej referencji albo `images` dla wielu referencji. Wskazówki wyjścia obsługiwane przez providera, takie jak `quality`, `outputFormat` i `background`, są przekazywane, gdy są dostępne, i zgłaszane jako zignorowane, gdy provider ich nie obsługuje. Wbudowana obsługa przezroczystego tła jest specyficzna dla OpenAI; inni providerzy mogą nadal zachowywać kanał alfa PNG, jeśli emituje go ich backend.

## Obsługiwani providerzy

Provider | Model domyślny | Obsługa edycji | Uwierzytelnianie  
---|---|---|---  
ComfyUI | `workflow` | Tak (1 obraz, skonfigurowane w workflow) | `COMFY_API_KEY` lub `COMFY_CLOUD_API_KEY` dla chmury  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | Tak (1 obraz) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | Tak (limity zależne od modelu) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | Tak | `GEMINI_API_KEY` lub `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | Tak (do 5 obrazów wejściowych) | `LITELLM_API_KEY`  
MiniMax | `image-01` | Tak (referencja obiektu) | `MINIMAX_API_KEY` lub MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | Tak (do 4 obrazów) | `OPENAI_API_KEY` lub OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | Tak (do 5 obrazów wejściowych) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | Nie | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | Tak (do 5 obrazów) | `XAI_API_KEY`  
  
Użyj `action: "list"`, aby sprawdzić dostępnych providerów i modele w czasie działania:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## Możliwości providerów

Możliwość | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
Generowanie (maks. liczba) | Zdefiniowane przez workflow | 4 | 4 | 4 | 9 | 4 | 1 | 4  
Edycja / referencja | 1 obraz (workflow) | 1 obraz | Flux: 1; GPT: 10; NB2: 14 | Do 5 obrazów | 1 obraz (referencja obiektu) | Do 5 obrazów | - | Do 5 obrazów  
Kontrola rozmiaru | - | ✓ | ✓ | ✓ | - | Do 4K | - | -  
Proporcje obrazu | - | - | ✓ | ✓ | ✓ | - | - | ✓  
Rozdzielczość (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## Parametry narzędzia

Prompt generowania obrazu. Wymagany dla `action: "generate"`.

Użyj `"list"`, aby sprawdzić dostępnych providerów i modele w czasie działania.

Nadpisanie providera/modelu (np. `openai/gpt-image-2`). Użyj `openai/gpt-image-1.5` dla przezroczystych teł OpenAI.

Pojedyncza ścieżka obrazu referencyjnego albo URL dla trybu edycji.

Wiele obrazów referencyjnych dla trybu edycji (do 5 u obsługujących providerów).

Wskazówka rozmiaru: `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`.

Proporcje obrazu: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

Wskazówka jakości, gdy provider ją obsługuje.

Wskazówka formatu wyjściowego, gdy provider go obsługuje.

Wskazówka tła, gdy provider ją obsługuje. Użyj `transparent` z `outputFormat: "png"` albo `"webp"` dla providerów obsługujących przezroczystość.

Opcjonalny limit czasu żądania providera w milisekundach. Gdy Codex wywołuje `image_generate` przez narzędzia dynamiczne, ta wartość dla pojedynczego wywołania nadal zastępuje skonfigurowaną wartość domyślną i jest ograniczona do 600000 ms.

Wskazówki tylko dla OpenAI: `background`, `moderation`, `outputCompression` i `user`.

## Konfiguracja

### Wybór modelu

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### Kolejność wyboru providerów

OpenClaw próbuje providerów w tej kolejności:

  1. Parametr **`model`** z wywołania narzędzia (jeśli agent go określi).
  2. **`imageGenerationModel.primary`** z konfiguracji.
  3. **`imageGenerationModel.fallbacks`** w kolejności.
  4. **Automatyczne wykrywanie** \- wyłącznie domyślne providery z dostępnym uwierzytelnianiem: 
     * najpierw bieżący domyślny provider;
     * pozostali zarejestrowani providerzy generowania obrazów w kolejności identyfikatorów providerów.


Jeśli provider zawiedzie (błąd uwierzytelniania, limit częstotliwości itd.), następny skonfigurowany kandydat jest próbowany automatycznie. Jeśli wszystkie zawiodą, błąd zawiera szczegóły z każdej próby.

Nadpisania modelu dla pojedynczego wywołania są dokładne

Nadpisanie `model` dla pojedynczego wywołania próbuje tylko tego providera/modelu i nie przechodzi do skonfigurowanego głównego/awaryjnego ani automatycznie wykrytych providerów.

Automatyczne wykrywanie uwzględnia uwierzytelnianie

Domyślny provider trafia na listę kandydatów tylko wtedy, gdy OpenClaw może faktycznie uwierzytelnić tego providera. Ustaw `agents.defaults.mediaGenerationAutoProviderFallback: false`, aby używać tylko jawnych wpisów `model`, `primary` i `fallbacks`.

Limity czasu

Ustaw `agents.defaults.imageGenerationModel.timeoutMs` dla wolnych backendów obrazów. Parametr narzędzia `timeoutMs` dla pojedynczego wywołania zastępuje skonfigurowaną wartość domyślną. Wywołania narzędzi dynamicznych Codex respektują ten sam budżet czasu, ograniczony przez maksymalny limit mostka narzędzi dynamicznych OpenClaw wynoszący 600000 ms.

Sprawdzanie w czasie działania

Użyj `action: "list"`, aby sprawdzić aktualnie zarejestrowanych providerów, ich modele domyślne i wskazówki dotyczące zmiennych środowiskowych uwierzytelniania.

### Edycja obrazów

OpenAI, OpenRouter, Google, DeepInfra, fal, MiniMax, ComfyUI i xAI obsługują edycję obrazów referencyjnych. Przekaż ścieżkę obrazu referencyjnego albo URL:

textCopy code
[code]
    "Generate a watercolor version of this photo" + image: "/path/to/photo.jpg"
[/code]

OpenAI, OpenRouter, Google i xAI obsługują do 5 obrazów referencyjnych przez parametr `images`. fal obsługuje 1 obraz referencyjny dla Flux image-to-image, do 10 dla edycji GPT Image 2 oraz do 14 dla edycji Nano Banana 2. MiniMax i ComfyUI obsługują 1.

## Szczegółowe omówienie dostawców

OpenAI gpt-image-2 (i gpt-image-1.5)

Generowanie obrazów OpenAI domyślnie używa `openai/gpt-image-2`. Jeśli skonfigurowano profil OAuth `openai-codex`, OpenClaw ponownie używa tego samego profilu OAuth, którego używają modele czatu subskrypcji Codex, i wysyła żądanie obrazu przez backend Codex Responses. Starsze bazowe adresy URL Codex, takie jak `https://chatgpt.com/backend-api`, są kanonizowane do `https://chatgpt.com/backend-api/codex` dla żądań obrazów. OpenClaw **nie** przełącza się po cichu na `OPENAI_API_KEY` dla tego żądania - aby wymusić bezpośrednie routowanie przez OpenAI Images API, skonfiguruj jawnie `models.providers.openai` z kluczem API, niestandardowym bazowym adresem URL albo endpointem Azure.

Modele `openai/gpt-image-1.5`, `openai/gpt-image-1` i `openai/gpt-image-1-mini` nadal można wybrać jawnie. Użyj `gpt-image-1.5` do wyjścia PNG/WebP z przezroczystym tłem; obecne API `gpt-image-2` odrzuca `background: "transparent"`.

`gpt-image-2` obsługuje zarówno generowanie tekst-na-obraz, jak i edycję obrazów referencyjnych przez to samo narzędzie `image_generate`. OpenClaw przekazuje do OpenAI `prompt`, `count`, `size`, `quality`, `outputFormat` oraz obrazy referencyjne. OpenAI **nie** otrzymuje bezpośrednio `aspectRatio` ani `resolution`; gdy to możliwe, OpenClaw mapuje je na obsługiwany `size`, w przeciwnym razie narzędzie zgłasza je jako zignorowane nadpisania.

Opcje specyficzne dla OpenAI znajdują się w obiekcie `openai`:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` przyjmuje `transparent`, `opaque` albo `auto`; przezroczyste wyniki wymagają `outputFormat` `png` albo `webp` oraz modelu obrazów OpenAI obsługującego przezroczystość. OpenClaw kieruje domyślne żądania `gpt-image-2` z przezroczystym tłem do `gpt-image-1.5`. `openai.outputCompression` stosuje się do wyjść JPEG/WebP.

Wskazówka najwyższego poziomu `background` jest neutralna względem dostawcy i obecnie mapuje się na to samo pole żądania OpenAI `background`, gdy wybrany jest dostawca OpenAI. Dostawcy, którzy nie deklarują obsługi tła, zwracają ją w `ignoredOverrides`, zamiast otrzymać nieobsługiwany parametr.

Aby kierować generowanie obrazów OpenAI przez wdrożenie Azure OpenAI zamiast `api.openai.com`, zobacz [endpointy Azure OpenAI](</pl/providers/openai#azure-openai-endpoints>).

Modele obrazów OpenRouter

Generowanie obrazów OpenRouter używa tego samego `OPENROUTER_API_KEY` i jest routowane przez API obrazów chat completions OpenRouter. Wybieraj modele obrazów OpenRouter z prefiksem `openrouter/`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw przekazuje do OpenRouter `prompt`, `count`, obrazy referencyjne oraz zgodne z Gemini wskazówki `aspectRatio` / `resolution`. Obecne wbudowane skróty modeli obrazów OpenRouter obejmują `google/gemini-3.1-flash-image-preview`, `google/gemini-3-pro-image-preview` i `openai/gpt-5.4-image-2`. Użyj `action: "list"`, aby zobaczyć, co udostępnia skonfigurowany Plugin.

Podwójne uwierzytelnianie MiniMax

Generowanie obrazów MiniMax jest dostępne przez obie dołączone ścieżki uwierzytelniania MiniMax:

  * `minimax/image-01` dla konfiguracji z kluczem API
  * `minimax-portal/image-01` dla konfiguracji OAuth

xAI grok-imagine-image

Dołączony dostawca xAI używa `/v1/images/generations` dla żądań zawierających tylko prompt oraz `/v1/images/edits`, gdy obecne jest `image` albo `images`.

  * Modele: `xai/grok-imagine-image`, `xai/grok-imagine-image-pro`
  * Liczba: do 4
  * Referencje: jedno `image` albo do pięciu `images`
  * Proporcje obrazu: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Rozdzielczości: `1K`, `2K`
  * Wyniki: zwracane jako załączniki obrazów zarządzane przez OpenClaw


OpenClaw celowo nie udostępnia natywnych dla xAI opcji `quality`, `mask`, `user` ani dodatkowych proporcji obrazu dostępnych tylko natywnie, dopóki te kontrolki nie pojawią się we współdzielonym, międzydostawczym kontrakcie `image_generate`.

## Przykłady

### Generowanie (krajobraz 4K)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Generowanie (przezroczysty PNG)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Równoważne CLI:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Generowanie (dwa kwadratowe)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edycja (jedna referencja)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edycja (wiele referencji)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

Te same flagi `--output-format` i `--background` są dostępne w `openclaw infer image edit`; `--openai-background` pozostaje aliasem specyficznym dla OpenAI. Dołączeni dostawcy inni niż OpenAI nie deklarują obecnie jawnej kontroli tła, więc `background: "transparent"` jest dla nich zgłaszane jako zignorowane.

## Powiązane

  * [Przegląd narzędzi](</pl/tools>) \- wszystkie dostępne narzędzia agenta
  * [ComfyUI](</pl/providers/comfy>) \- konfiguracja lokalnego ComfyUI i workflow Comfy Cloud
  * [fal](</pl/providers/fal>) \- konfiguracja dostawcy obrazów i wideo fal
  * [Google (Gemini)](</pl/providers/google>) \- konfiguracja dostawcy obrazów Gemini
  * [MiniMax](</pl/providers/minimax>) \- konfiguracja dostawcy obrazów MiniMax
  * [OpenAI](</pl/providers/openai>) \- konfiguracja dostawcy OpenAI Images
  * [Vydra](</pl/providers/vydra>) \- konfiguracja obrazów, wideo i mowy Vydra
  * [xAI](</pl/providers/xai>) \- konfiguracja obrazów, wideo, wyszukiwania, wykonywania kodu i TTS Grok
  * [Odniesienie konfiguracji](</pl/gateway/config-agents#agent-defaults>) \- konfiguracja `imageGenerationModel`
  * [Modele](</pl/concepts/models>) \- konfiguracja modeli i failover


Was this useful?YesNo
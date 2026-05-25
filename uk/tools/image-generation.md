---
title: Генерація зображень
source_url: https://docs.openclaw.ai/uk/tools/image-generation
scraped_at: 2026-05-25
---

Засіб `image_generate` дає агенту змогу створювати й редагувати зображення за допомогою ваших налаштованих постачальників. Згенеровані зображення автоматично доставляються як медіа вкладення у відповіді агента.

## Швидкий старт

* ### Configure auth

Задайте API-ключ принаймні для одного постачальника (наприклад `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`) або увійдіть через OpenAI Codex OAuth.

* ### Pick a default model (optional)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth використовує той самий ref моделі `openai/gpt-image-2`. Коли налаштовано OAuth-профіль `openai-codex`, OpenClaw маршрутизує запити на зображення через цей OAuth-профіль, замість того щоб спершу пробувати `OPENAI_API_KEY`. Явна конфігурація `models.providers.openai` (API-ключ, користувацький/Azure базовий URL) знову вмикає прямий маршрут через OpenAI Images API.

* ### Ask the agent

_"Згенеруй зображення дружнього робота-маскота."_

Агент автоматично викликає `image_generate`. Список дозволених засобів не потрібен — він увімкнений за замовчуванням, коли доступний постачальник.

## Поширені маршрути

Ціль | Ref моделі | Автентифікація  
---|---|---  
Генерація зображень OpenAI з API-білінгом | `openai/gpt-image-2` | `OPENAI_API_KEY`  
Генерація зображень OpenAI з автентифікацією передплати Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
OpenAI PNG/WebP з прозорим тлом | `openai/gpt-image-1.5` | `OPENAI_API_KEY` або OpenAI Codex OAuth  
Генерація зображень DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
Генерація зображень OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
Генерація зображень LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
Генерація зображень Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` або `GOOGLE_API_KEY`  
  
Той самий засіб `image_generate` обробляє перетворення тексту на зображення й редагування за референсними зображеннями. Використовуйте `image` для одного референсу або `images` для кількох референсів. Підказки виводу, підтримувані постачальником, як-от `quality`, `outputFormat` і `background`, передаються, коли доступні, і повідомляються як проігноровані, коли постачальник їх не підтримує. Вбудована підтримка прозорого тла специфічна для OpenAI; інші постачальники все одно можуть зберігати PNG alpha, якщо їхній backend її видає.

## Підтримувані постачальники

Постачальник | Модель за замовчуванням | Підтримка редагування | Автентифікація  
---|---|---|---  
ComfyUI | `workflow` | Так (1 зображення, налаштовано workflow) | `COMFY_API_KEY` або `COMFY_CLOUD_API_KEY` для хмари  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | Так (1 зображення) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | Так (ліміти залежать від моделі) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | Так | `GEMINI_API_KEY` або `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | Так (до 5 вхідних зображень) | `LITELLM_API_KEY`  
MiniMax | `image-01` | Так (референс суб’єкта) | `MINIMAX_API_KEY` або MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | Так (до 4 зображень) | `OPENAI_API_KEY` або OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | Так (до 5 вхідних зображень) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | Ні | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | Так (до 5 зображень) | `XAI_API_KEY`  
  
Використовуйте `action: "list"`, щоб перевірити доступних постачальників і моделі під час виконання:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## Можливості постачальників

Можливість | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
Генерація (макс. кількість) | Визначено workflow | 4 | 4 | 4 | 9 | 4 | 1 | 4  
Редагування / референс | 1 зображення (workflow) | 1 зображення | Flux: 1; GPT: 10; NB2: 14 | До 5 зображень | 1 зображення (ref суб’єкта) | До 5 зображень | - | До 5 зображень  
Керування розміром | - | ✓ | ✓ | ✓ | - | До 4K | - | -  
Співвідношення сторін | - | - | ✓ | ✓ | ✓ | - | - | ✓  
Роздільна здатність (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## Параметри засобу

Prompt для генерації зображення. Обов’язковий для `action: "generate"`.

Використовуйте `"list"`, щоб перевірити доступних постачальників і моделі під час виконання.

Перевизначення постачальника/моделі (наприклад `openai/gpt-image-2`). Використовуйте `openai/gpt-image-1.5` для прозорих фонів OpenAI.

Шлях або URL одного референсного зображення для режиму редагування.

Кілька референсних зображень для режиму редагування (до 5 у постачальників із підтримкою).

Підказка розміру: `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`.

Співвідношення сторін: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

Підказка якості, коли постачальник її підтримує.

Підказка формату виводу, коли постачальник його підтримує.

Підказка тла, коли постачальник її підтримує. Використовуйте `transparent` з `outputFormat: "png"` або `"webp"` для постачальників, здатних працювати з прозорістю.

Необов’язковий тайм-аут запиту до постачальника в мілісекундах. Коли Codex викликає `image_generate` через динамічні засоби, це значення для окремого виклику все одно перевизначає налаштоване значення за замовчуванням і обмежується 600000 ms.

Підказки лише для OpenAI: `background`, `moderation`, `outputCompression` і `user`.

## Конфігурація

### Вибір моделі

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### Порядок вибору постачальника

OpenClaw пробує постачальників у такому порядку:

  1. Параметр **`model`** з виклику засобу (якщо агент його вказує).
  2. **`imageGenerationModel.primary`** з конфігурації.
  3. **`imageGenerationModel.fallbacks`** за порядком.
  4. **Автовиявлення** — лише стандартні постачальники, підкріплені автентифікацією: 
     * спершу поточний постачальник за замовчуванням;
     * решта зареєстрованих постачальників генерації зображень у порядку provider-id.


Якщо постачальник завершується помилкою (помилка автентифікації, rate limit тощо), наступний налаштований кандидат пробується автоматично. Якщо всі завершуються помилкою, помилка містить подробиці з кожної спроби.

Per-call model overrides are exact

Перевизначення `model` для окремого виклику пробує лише цього постачальника/модель і не переходить до налаштованих primary/fallback або автовиявлених постачальників.

Auto-detection is auth-aware

Значення постачальника за замовчуванням потрапляє до списку кандидатів лише тоді, коли OpenClaw може фактично автентифікувати цього постачальника. Задайте `agents.defaults.mediaGenerationAutoProviderFallback: false`, щоб використовувати лише явні записи `model`, `primary` і `fallbacks`.

Timeouts

Задайте `agents.defaults.imageGenerationModel.timeoutMs` для повільних backend-ів зображень. Параметр засобу `timeoutMs` для окремого виклику перевизначає налаштоване значення за замовчуванням. Динамічні виклики засобів Codex дотримуються того самого бюджету тайм-ауту, обмеженого максимумом 600000 ms для bridge динамічних засобів OpenClaw.

Inspect at runtime

Використовуйте `action: "list"`, щоб перевірити поточно зареєстрованих постачальників, їхні моделі за замовчуванням і підказки щодо env-var для автентифікації.

### Редагування зображень

OpenAI, OpenRouter, Google, DeepInfra, fal, MiniMax, ComfyUI і xAI підтримують редагування референсних зображень. Передайте шлях або URL референсного зображення:

textCopy code
[code]
    "Generate a watercolor version of this photo" + image: "/path/to/photo.jpg"
[/code]

OpenAI, OpenRouter, Google і xAI підтримують до 5 еталонних зображень через параметр `images`. fal підтримує 1 еталонне зображення для Flux image-to-image, до 10 для редагувань GPT Image 2 і до 14 для редагувань Nano Banana 2. MiniMax і ComfyUI підтримують 1.

## Детальні огляди провайдерів

OpenAI gpt-image-2 (and gpt-image-1.5)

Генерація зображень OpenAI за замовчуванням використовує `openai/gpt-image-2`. Якщо налаштовано OAuth-профіль `openai-codex`, OpenClaw повторно використовує той самий OAuth-профіль, який застосовується моделями чату передплати Codex, і надсилає запит на зображення через бекенд Codex Responses. Застарілі базові URL-адреси Codex, як-от `https://chatgpt.com/backend-api`, канонізуються до `https://chatgpt.com/backend-api/codex` для запитів на зображення. OpenClaw **не** виконує непомітний fallback до `OPENAI_API_KEY` для цього запиту - щоб примусово спрямувати запит напряму до OpenAI Images API, явно налаштуйте `models.providers.openai` з API-ключем, власною базовою URL-адресою або кінцевою точкою Azure.

Моделі `openai/gpt-image-1.5`, `openai/gpt-image-1` і `openai/gpt-image-1-mini` усе ще можна вибрати явно. Використовуйте `gpt-image-1.5` для виводу PNG/WebP із прозорим фоном; поточний API `gpt-image-2` відхиляє `background: "transparent"`.

`gpt-image-2` підтримує як генерацію text-to-image, так і редагування з еталонними зображеннями через той самий інструмент `image_generate`. OpenClaw передає OpenAI `prompt`, `count`, `size`, `quality`, `outputFormat` і еталонні зображення. OpenAI **не** отримує `aspectRatio` або `resolution` безпосередньо; коли можливо, OpenClaw зіставляє їх із підтримуваним `size`, інакше інструмент повідомляє про них як про проігноровані перевизначення.

Специфічні для OpenAI параметри містяться в об’єкті `openai`:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` приймає `transparent`, `opaque` або `auto`; прозорий вивід потребує `outputFormat` `png` або `webp` і моделі зображень OpenAI, здатної працювати з прозорістю. OpenClaw спрямовує типові запити `gpt-image-2` із прозорим фоном до `gpt-image-1.5`. `openai.outputCompression` застосовується до виводу JPEG/WebP.

Підказка верхнього рівня `background` є нейтральною щодо провайдера й наразі зіставляється з тим самим полем запиту OpenAI `background`, коли вибрано провайдера OpenAI. Провайдери, які не декларують підтримку фону, повертають її в `ignoredOverrides` замість отримання непідтримуваного параметра.

Щоб спрямувати генерацію зображень OpenAI через розгортання Azure OpenAI замість `api.openai.com`, див. [кінцеві точки Azure OpenAI](</uk/providers/openai#azure-openai-endpoints>).

OpenRouter image models

Генерація зображень OpenRouter використовує той самий `OPENROUTER_API_KEY` і спрямовується через image API chat completions OpenRouter. Вибирайте моделі зображень OpenRouter із префіксом `openrouter/`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw передає OpenRouter `prompt`, `count`, еталонні зображення та сумісні з Gemini підказки `aspectRatio` / `resolution`. Поточні вбудовані скорочення моделей зображень OpenRouter включають `google/gemini-3.1-flash-image-preview`, `google/gemini-3-pro-image-preview` і `openai/gpt-5.4-image-2`. Використовуйте `action: "list"`, щоб побачити, що надає ваш налаштований plugin.

MiniMax dual-auth

Генерація зображень MiniMax доступна через обидва вбудовані шляхи автентифікації MiniMax:

  * `minimax/image-01` для налаштувань з API-ключем
  * `minimax-portal/image-01` для налаштувань OAuth

xAI grok-imagine-image

Вбудований провайдер xAI використовує `/v1/images/generations` для запитів лише з prompt і `/v1/images/edits`, коли присутні `image` або `images`.

  * Моделі: `xai/grok-imagine-image`, `xai/grok-imagine-image-pro`
  * Кількість: до 4
  * Еталони: одне `image` або до п’яти `images`
  * Співвідношення сторін: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Роздільні здатності: `1K`, `2K`
  * Вивід: повертається як керовані OpenClaw вкладення зображень


OpenClaw навмисно не надає нативні для xAI `quality`, `mask`, `user` або додаткові лише нативні співвідношення сторін, доки ці елементи керування не з’являться в спільному міжпровайдерному контракті `image_generate`.

## Приклади

### Generate (4K landscape)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Generate (transparent PNG)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Еквівалентний CLI:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Generate (two square)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edit (one reference)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edit (multiple references)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

Ті самі прапорці `--output-format` і `--background` доступні в `openclaw infer image edit`; `--openai-background` залишається специфічним для OpenAI псевдонімом. Вбудовані провайдери, крім OpenAI, наразі не декларують явного керування фоном, тому `background: "transparent"` повідомляється для них як проігнороване.

## Пов’язане

  * [Огляд інструментів](</uk/tools>) \- усі доступні інструменти агента
  * [ComfyUI](</uk/providers/comfy>) \- налаштування локального ComfyUI і workflow Comfy Cloud
  * [fal](</uk/providers/fal>) \- налаштування провайдера зображень і відео fal
  * [Google (Gemini)](</uk/providers/google>) \- налаштування провайдера зображень Gemini
  * [MiniMax](</uk/providers/minimax>) \- налаштування провайдера зображень MiniMax
  * [OpenAI](</uk/providers/openai>) \- налаштування провайдера OpenAI Images
  * [Vydra](</uk/providers/vydra>) \- налаштування зображень, відео й мовлення Vydra
  * [xAI](</uk/providers/xai>) \- налаштування зображень Grok, відео, пошуку, виконання коду та TTS
  * [Довідник конфігурації](</uk/gateway/config-agents#agent-defaults>) \- конфігурація `imageGenerationModel`
  * [Моделі](</uk/concepts/models>) \- конфігурація моделей і failover


Was this useful?YesNo
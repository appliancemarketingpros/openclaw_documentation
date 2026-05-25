---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/uk/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw постачається з вбудованим Plugin `alibaba`, який реєструє провайдера генерації відео для моделей Wan в Alibaba Model Studio (міжнародна назва DashScope). Plugin увімкнено за замовчуванням; потрібно лише встановити API-ключ.

Властивість | Значення  
---|---  
ID провайдера | `alibaba`  
Plugin | вбудований, `enabledByDefault: true`  
Змінні env для auth | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (перемагає перший збіг)  
Прапорець onboarding | `--auth-choice alibaba-model-studio-api-key`  
Прямий прапорець CLI | `--alibaba-model-studio-api-key <key>`  
Модель за замовчуванням | `alibaba/wan2.6-t2v`  
Базовий URL за замовчуванням | `https://dashscope-intl.aliyuncs.com`  
  
## Початок роботи

* ### Установіть API-ключ

Використайте onboarding, щоб зберегти ключ для провайдера `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Або передайте ключ напряму під час встановлення/onboarding:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Або експортуйте будь-яку з прийнятих змінних env перед запуском Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Установіть модель відео за замовчуванням

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Перевірте, що провайдера налаштовано

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

Список має містити всі п’ять вбудованих моделей Wan. Якщо `MODELSTUDIO_API_KEY` не вдалося розв’язати, `openclaw models status --json` повідомить про відсутні облікові дані в `auth.unusableProfiles`.

## Вбудовані моделі Wan

Посилання на модель | Режим  
---|---  
`alibaba/wan2.6-t2v` | Текст-у-відео (за замовчуванням)  
`alibaba/wan2.6-i2v` | Зображення-у-відео  
`alibaba/wan2.6-r2v` | Референс-у-відео  
`alibaba/wan2.6-r2v-flash` | Референс-у-відео (швидкий)  
`alibaba/wan2.7-r2v` | Референс-у-відео  
  
## Можливості й обмеження

Вбудований провайдер віддзеркалює обмеження відео API Wan у DashScope. Усі три режими мають однакові обмеження на кількість відео в одному запиті та тривалість; відрізняється лише форма вхідних даних.

Режим | Макс. вихідних відео | Макс. вхідних зображень | Макс. вхідних відео | Макс. тривалість | Підтримувані елементи керування  
---|---|---|---|---|---  
Текст-у-відео | 1 | n/a | n/a | 10 с | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Зображення-у-відео | 1 | 1 | n/a | 10 с | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Референс-у-відео | 1 | n/a | 4 | 10 с | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Коли запит не містить `durationSeconds`, провайдер надсилає прийняте в DashScope значення за замовчуванням — **5 секунд**. Установіть `durationSeconds` явно в [інструменті генерації відео](</uk/tools/video-generation>), щоб збільшити тривалість до 10 с.

## Розширена конфігурація

Перевизначення базового URL DashScope

Провайдер за замовчуванням використовує міжнародний endpoint DashScope. Щоб націлитися на endpoint китайського регіону, установіть:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Провайдер видаляє кінцеві скісні риски перед побудовою URL завдань AIGC.

Пріоритет env для auth

OpenClaw розв’язує API-ключ Alibaba зі змінних середовища в такому порядку, беручи перше непорожнє значення:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Налаштовані записи `auth.profiles` (установлені через `openclaw models auth login`) перевизначають розв’язання змінних env. Див. [Auth profiles у FAQ моделей](</uk/help/faq-models#what-is-an-auth-profile>), щоб дізнатися про ротацію профілів, cooldown і механіку перевизначення.

Зв’язок із Plugin Qwen

Обидва вбудовані plugins взаємодіють із DashScope і приймають API-ключі, що перетинаються. Використовуйте:

  * ID `alibaba/wan*.*` для керування спеціалізованим провайдером відео Wan, задокументованим на цій сторінці.
  * ID `qwen/*` для чату Qwen, embedding і розуміння медіа (див. [Qwen](</uk/providers/qwen>)).


Одного встановлення `MODELSTUDIO_API_KEY` достатньо для автентифікації обох plugins, оскільки список змінних env для auth навмисно перетинається; проходити onboarding для кожного Plugin окремо не потрібно.

## Пов’язане

[**Генерація відео** Спільні параметри інструмента відео та вибір провайдера. ](</uk/tools/video-generation>) [**Qwen** Налаштування чату Qwen, embedding і розуміння медіа з тією самою auth DashScope. ](</uk/providers/qwen>) [**Довідник конфігурації** Налаштування за замовчуванням для агентів і конфігурація моделей. ](</uk/gateway/config-agents#agent-defaults>) [**FAQ моделей** Auth profiles, перемикання моделей і розв’язання помилок "no profile". ](</uk/help/faq-models>)

Was this useful?YesNo
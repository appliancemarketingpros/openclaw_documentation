---
title: Z.AI
source_url: https://docs.openclaw.ai/uk/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) — це API-платформа для моделей **GLM**. Вона надає REST API для GLM і використовує API-ключі для автентифікації. Створіть свій API-ключ у консолі [Z.AI](<http://Z.AI>). OpenClaw використовує провайдер `zai` з API-ключем [Z.AI](<http://Z.AI>).

  * Провайдер: `zai`
  * Автентифікація: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (автентифікація Bearer)


## Початок роботи

### Автовиявлення кінцевої точки

**Найкраще для:** більшості користувачів. OpenClaw визначає відповідну кінцеву точку [Z.AI](<http://Z.AI>) за ключем і автоматично застосовує правильну базову URL-адресу.

* ### Запустіть початкове налаштування

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Установіть модель за замовчуванням

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Перевірте, що модель є у списку

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Явна регіональна кінцева точка

**Найкраще для:** користувачів, які хочуть примусово вибрати певний Coding Plan або загальну поверхню API.

* ### Виберіть правильний варіант початкового налаштування

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Установіть модель за замовчуванням

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Перевірте, що модель є у списку

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Вбудований каталог

OpenClaw постачається з комплектним каталогом провайдера `zai` у маніфесті Plugin, тому список лише для читання може показувати відомі рядки GLM без завантаження середовища виконання провайдера:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Каталог на основі маніфесту наразі містить:

Посилання на модель | Примітки  
---|---  
`zai/glm-5.1` | Модель за замовчуванням  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Розширена конфігурація

Пряме розпізнавання невідомих моделей GLM-5

Невідомі ідентифікатори `glm-5*` усе одно розпізнаються наперед у комплектному шляху провайдера шляхом синтезу метаданих, якими володіє провайдер, із шаблону `glm-4.7`, коли ідентифікатор відповідає поточній формі сімейства GLM-5.

Потокове передавання викликів інструментів

`tool_stream` увімкнено за замовчуванням для потокового передавання викликів інструментів [Z.AI](<http://Z.AI>). Щоб вимкнути його:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Мислення та збережене мислення

Мислення [Z.AI](<http://Z.AI>) дотримується елементів керування `/think` в OpenClaw. Коли мислення вимкнено, OpenClaw надсилає `thinking: { type: "disabled" }`, щоб уникнути відповідей, які витрачають бюджет виводу на `reasoning_content` перед видимим текстом.

Збережене мислення вмикається явно, тому що [Z.AI](<http://Z.AI>) вимагає повторного відтворення повного історичного `reasoning_content`, що збільшує кількість токенів запиту. Увімкніть його для окремої моделі:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Коли це ввімкнено і мислення активне, OpenClaw надсилає `thinking: { type: "enabled", clear_thinking: false }` і повторно відтворює попередній `reasoning_content` для того самого OpenAI-сумісного транскрипту.

Досвідчені користувачі все ще можуть перевизначити точне корисне навантаження провайдера за допомогою `params.extra_body.thinking`.

Розуміння зображень

Комплектний Plugin [Z.AI](<http://Z.AI>) реєструє розуміння зображень.

Властивість | Значення  
---|---  
Модель | `glm-4.6v`  
  
Розуміння зображень автоматично розпізнається з налаштованої автентифікації [Z.AI](<http://Z.AI>) — жодна додаткова конфігурація не потрібна.

Деталі автентифікації

  * [Z.AI](<http://Z.AI>) використовує автентифікацію Bearer із вашим API-ключем.
  * Варіант початкового налаштування `zai-api-key` автоматично визначає відповідну кінцеву точку [Z.AI](<http://Z.AI>) за префіксом ключа.
  * Використовуйте явні регіональні варіанти (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`), коли потрібно примусово вибрати певну поверхню API.


## Пов’язане

[**Сімейство моделей GLM** Огляд сімейства моделей для GLM. ](</uk/providers/glm>) [**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки резервного перемикання. ](</uk/concepts/model-providers>)

Was this useful?YesNo
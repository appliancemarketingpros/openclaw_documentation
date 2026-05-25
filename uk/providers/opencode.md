---
title: OpenCode
source_url: https://docs.openclaw.ai/uk/providers/opencode
scraped_at: 2026-05-25
---

OpenCode надає два розміщені каталоги в OpenClaw:

Каталог | Префікс | Постачальник середовища виконання  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Обидва каталоги використовують той самий API-ключ OpenCode. OpenClaw зберігає ідентифікатори постачальників середовища виконання розділеними, щоб маршрутизація для кожної моделі на рівні upstream залишалася коректною, але онбординг і документація розглядають їх як єдине налаштування OpenCode.

## Початок роботи

### Каталог Zen

**Найкраще підходить для:** курованого багатомодельного проксі OpenCode (Claude, GPT, Gemini).

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Або передайте ключ напряму:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Установіть модель Zen як стандартну

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Перевірте, що моделі доступні

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Каталог Go

**Найкраще підходить для:** лінійки Kimi, GLM і MiniMax, розміщеної в OpenCode.

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Або передайте ключ напряму:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Установіть модель Go як стандартну

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Перевірте, що моделі доступні

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Приклад конфігурації

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Вбудовані каталоги

### Zen

Властивість | Значення  
---|---  
Постачальник середовища виконання | `opencode`  
Приклади моделей | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Властивість | Значення  
---|---  
Постачальник середовища виконання | `opencode-go`  
Приклади моделей | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Розширена конфігурація

Псевдоніми API-ключа

`OPENCODE_ZEN_API_KEY` також підтримується як псевдонім для `OPENCODE_API_KEY`.

Спільні облікові дані

Введення одного ключа OpenCode під час налаштування зберігає облікові дані для обох постачальників середовища виконання. Вам не потрібно окремо проходити онбординг для кожного каталогу.

Білінг і панель керування

Ви входите в OpenCode, додаєте платіжні дані та копіюєте свій API-ключ. Білінг і доступність каталогів керуються з панелі керування OpenCode.

Поведінка повторного відтворення Gemini

Посилання OpenCode на базі Gemini залишаються на шляху proxy-Gemini, тому OpenClaw зберігає там очищення thought-signature Gemini без увімкнення власної перевірки повторного відтворення Gemini або переписування bootstrap.

Поведінка повторного відтворення не-Gemini

Посилання OpenCode не-Gemini зберігають мінімальну політику повторного відтворення, сумісну з OpenAI.

## Пов’язане

[**Вибір моделі** Вибір постачальників, посилань на моделі та поведінки резервного перемикання. ](</uk/concepts/model-providers>) [**Довідник із конфігурації** Повний довідник із конфігурації для агентів, моделей і постачальників. ](</uk/gateway/configuration-reference>)

Was this useful?YesNo
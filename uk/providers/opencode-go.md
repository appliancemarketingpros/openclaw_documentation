---
title: OpenCode Go
source_url: https://docs.openclaw.ai/uk/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go — це каталог Go у [OpenCode](</uk/providers/opencode>). Він використовує той самий `OPENCODE_API_KEY`, що й каталог Zen, але зберігає ідентифікатор провайдера під час виконання `opencode-go`, щоб маршрутизація upstream для кожної моделі залишалася коректною.

Property | Value  
---|---  
Провайдер під час виконання | `opencode-go`  
Автентифікація | `OPENCODE_API_KEY`  
Батьківське налаштування | [OpenCode](</uk/providers/opencode>)  
  
## Вбудований каталог

OpenClaw бере більшість рядків каталогу Go з вбудованого реєстру моделей pi і доповнює їх актуальними рядками upstream, поки реєстр не буде оновлено. Виконайте `openclaw models list --provider opencode-go`, щоб переглянути поточний список моделей.

Провайдер включає:

Посилання на модель | Назва  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (ліміти 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Початок роботи

### Інтерактивно

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Установіть модель Go як типову

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Переконайтеся, що моделі доступні

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Неінтерактивно

* ### Передайте ключ напряму

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Переконайтеся, що моделі доступні

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Приклад конфігурації

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Розширена конфігурація

Поведінка маршрутизації

OpenClaw автоматично обробляє маршрутизацію для кожної моделі, коли посилання на модель використовує `opencode-go/...`. Додаткова конфігурація провайдера не потрібна.

Угода про посилання під час виконання

Посилання під час виконання залишаються явними: `opencode/...` для Zen, `opencode-go/...` для Go. Це зберігає коректну маршрутизацію upstream для кожної моделі в обох каталогах.

Спільні облікові дані

Той самий `OPENCODE_API_KEY` використовується і для каталогів Zen, і для Go. Введення ключа під час налаштування зберігає облікові дані для обох провайдерів під час виконання.

## Пов’язане

[**OpenCode (батьківський)** Спільний онбординг, огляд каталогу та розширені примітки. ](</uk/providers/opencode>) [**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки резервного перемикання. ](</uk/concepts/model-providers>)

Was this useful?YesNo
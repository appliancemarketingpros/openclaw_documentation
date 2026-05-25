---
title: Claude Max API proxy
source_url: https://docs.openclaw.ai/uk/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** — це спільнотний інструмент, який відкриває вашу підписку Claude Max/Pro як endpoint API, сумісний з OpenAI. Це дає змогу використовувати вашу підписку з будь-яким інструментом, що підтримує формат API OpenAI.

## Навіщо це використовувати?

Підхід | Вартість | Найкраще підходить для  
---|---|---  
Anthropic API | Оплата за токени (~$15/М вхідних, $75/М вихідних для Opus) | Production-застосунків, великих обсягів  
Підписка Claude Max | $200/місяць фіксовано | Особистого використання, розробки, необмеженого використання  
  
Якщо у вас є підписка Claude Max і ви хочете використовувати її з інструментами, сумісними з OpenAI, цей proxy може зменшити витрати для деяких робочих процесів. API-ключі все ще залишаються зрозумілішим шляхом з точки зору політики для production-використання.

## Як це працює

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI → Anthropic (via subscription)     (OpenAI format)              (converts format)      (uses your login)
[/code]

Proxy:

  1. Приймає запити у форматі OpenAI за адресою `http://localhost:3456/v1/chat/completions`
  2. Перетворює їх на команди Claude Code CLI
  3. Повертає відповіді у форматі OpenAI (підтримується потокова передача)


## Початок роботи

* ### Установіть proxy

Потрібні Node.js 20+ і Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### Запустіть сервер

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### Перевірте proxy

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Налаштуйте OpenClaw

Спрямуйте OpenClaw на proxy як на користувацький endpoint, сумісний з OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Вбудований каталог

ID моделі | Відповідає  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Розширена конфігурація

Примітки щодо proxy-стилю, сумісного з OpenAI

Цей шлях використовує той самий proxy-стиль маршруту, сумісного з OpenAI, що й інші користувацькі бекенди `/v1`:

  * Native-формування запитів лише для OpenAI не застосовується
  * Немає `service_tier`, немає Responses `store`, немає підказок prompt-cache і немає формування payload reasoning-compat для OpenAI
  * Приховані заголовки атрибуції OpenClaw (`originator`, `version`, `User-Agent`) не інжектуються в URL proxy

Автозапуск на macOS через LaunchAgent

Створіть LaunchAgent, щоб запускати proxy автоматично:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Посилання

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Примітки

  * Це **спільнотний інструмент** , який офіційно не підтримується ні Anthropic, ні OpenClaw
  * Потрібна активна підписка Claude Max/Pro з автентифікованим Claude Code CLI
  * Proxy працює локально й не надсилає дані на жодні сторонні сервери
  * Потокові відповіді повністю підтримуються


## Пов’язане

[**Провайдер Anthropic** Native-інтеграція OpenClaw з Claude CLI або API-ключами. ](</uk/providers/anthropic>) [**Провайдер OpenAI** Для підписок OpenAI/Codex. ](</uk/providers/openai>) [**Вибір моделі** Огляд усіх провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Конфігурація** Повний довідник конфігурації. ](</uk/gateway/configuration>)

Was this useful?YesNo
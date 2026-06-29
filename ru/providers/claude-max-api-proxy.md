---
title: API-прокси Claude Max
source_url: https://docs.openclaw.ai/ru/providers/claude-max-api-proxy
scraped_at: 2026-06-29
---

ModelsProviders

**claude-max-api-proxy** — это инструмент сообщества, который предоставляет вашу подписку Claude Max/Pro как OpenAI-совместимую конечную точку API. Это позволяет использовать вашу подписку с любым инструментом, поддерживающим формат OpenAI API.

## Зачем это использовать?

Подход | Маршрут оплаты | Лучше всего подходит для  
---|---|---  
Anthropic API | Оплата за токен через Claude Console или облако | Продакшен-приложения, совместная автоматизация, объем  
Прокси подписки Claude | План и кредитные правила Claude Code / `claude -p` | Личные эксперименты с совместимыми инструментами  
  
Если у вас есть подписка Claude Max или Pro и вы хотите использовать ее с OpenAI-совместимыми инструментами, этот прокси может подойти для некоторых личных рабочих процессов. Это не безлимитный путь с фиксированной оплатой. API-ключи остаются более понятным вариантом с точки зрения политики и биллинга для продакшен-использования.

## Как это работает

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI / claude -p → Anthropic     (OpenAI format)              (converts format)          (uses your login)
[/code]

Прокси:

  1. Принимает запросы в формате OpenAI на `http://localhost:3456/v1/chat/completions`
  2. Преобразует их в команды Claude Code CLI
  3. Возвращает ответы в формате OpenAI (поддерживается потоковая передача)


## Начало работы

* ### Установите прокси

Требуется Node.js 22+ и Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### Запустите сервер

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### Проверьте прокси

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Настройте OpenClaw

Укажите OpenClaw на прокси как на пользовательскую OpenAI-совместимую конечную точку:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Встроенный каталог

ID модели | Соответствует  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Расширенная настройка

Примечания о прокси-стиле OpenAI-совместимости

Этот путь использует тот же прокси-стиль OpenAI-совместимого маршрута, что и другие пользовательские бэкенды `/v1`:

  * Нативное формирование запросов только для OpenAI не применяется
  * Нет `service_tier`, нет Responses `store`, нет подсказок prompt-cache и нет формирования payload для совместимости с reasoning OpenAI
  * Скрытые заголовки атрибуции OpenClaw (`originator`, `version`, `User-Agent`) не вставляются в URL прокси

Автозапуск в macOS через LaunchAgent

Создайте LaunchAgent, чтобы запускать прокси автоматически:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Примечания

  * Это **инструмент сообщества** , официально не поддерживаемый Anthropic или OpenClaw
  * Требуется активная подписка Claude Max/Pro с аутентифицированным Claude Code CLI
  * Наследует поведение биллинга, кредитов использования и rate-limit Claude Code `claude -p`
  * Прокси работает локально и не отправляет данные на сторонние серверы
  * Потоковые ответы полностью поддерживаются


## Связанные материалы

[**Провайдер Anthropic** Нативная интеграция OpenClaw с Claude CLI или API-ключами. ](</ru/providers/anthropic>) [**Провайдер OpenAI** Для подписок OpenAI/Codex. ](</ru/providers/openai>) [**Выбор модели** Обзор всех провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Конфигурация** Полный справочник конфигурации. ](</ru/gateway/configuration>)

Was this useful?YesNo

Open issue
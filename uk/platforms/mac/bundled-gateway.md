---
title: Gateway на macOS
source_url: https://docs.openclaw.ai/uk/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app більше не постачає в комплекті Node/Bun або середовище виконання Gateway. Застосунок macOS очікує **зовнішнє** встановлення `openclaw` CLI, не запускає Gateway як дочірній процес і керує службою launchd для кожного користувача, щоб підтримувати Gateway запущеним (або підключається до наявного локального Gateway, якщо він уже працює).

## Установіть CLI (обов’язково для локального режиму)

Node 24 є типовим середовищем виконання на Mac. Node 22 LTS, наразі `22.16+`, усе ще працює для сумісності. Потім установіть `openclaw` глобально:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Кнопка **Install CLI** у застосунку macOS запускає той самий глобальний процес встановлення, який застосунок використовує внутрішньо: спершу він надає перевагу npm, потім pnpm, а потім bun, якщо це єдиний виявлений менеджер пакетів. Node залишається рекомендованим середовищем виконання Gateway.

## Launchd (Gateway як LaunchAgent)

Мітка:

  * `ai.openclaw.gateway` (або `ai.openclaw.<profile>`; застарілі `com.openclaw.*` можуть залишатися)


Розташування plist (для кожного користувача):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (або `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Менеджер:

  * Застосунок macOS відповідає за встановлення/оновлення LaunchAgent у локальному режимі.
  * CLI також може встановити його: `openclaw gateway install`.


Поведінка:

  * "OpenClaw Active" вмикає/вимикає LaunchAgent.
  * Вихід із застосунку **не** зупиняє Gateway (launchd підтримує його роботу).
  * Якщо Gateway уже працює на налаштованому порту, застосунок підключається до нього замість запуску нового.


Журналювання:

  * stdout/err launchd: `/tmp/openclaw/openclaw-gateway.log`


## Сумісність версій

Застосунок macOS перевіряє версію gateway відносно власної версії. Якщо вони несумісні, оновіть глобальний CLI, щоб він відповідав версії застосунку.

## Smoke-перевірка

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Потім:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Пов’язане

  * [застосунок macOS](</uk/platforms/macos>)
  * [операційний посібник Gateway](</uk/gateway>)


Was this useful?YesNo
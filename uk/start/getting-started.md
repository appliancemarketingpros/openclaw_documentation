---
title: Початок роботи
source_url: https://docs.openclaw.ai/uk/start/getting-started
scraped_at: 2026-05-25
---

Install OpenClaw, запустіть онбординг і поспілкуйтеся зі своїм AI-помічником — усе приблизно за 5 хвилин. Наприкінці у вас буде запущений Gateway, налаштована автентифікація та робочий сеанс чату.

## Що вам потрібно

  * **Node.js** — рекомендовано Node 24 (Node 22.16+ також підтримується)
  * **API-ключ** від постачальника моделей (Anthropic, OpenAI, Google тощо) — онбординг попросить вас його ввести


## Швидке налаштування

* ### Установіть OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Процес сценарію встановлення](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Майстер проведе вас через вибір постачальника моделей, встановлення API-ключа та налаштування Gateway. Це займає приблизно 2 хвилини.

Повний довідник див. у [Онбординг (CLI)](</uk/start/wizard>).

* ### Перевірте, що Gateway запущено

bashCopy code
[code]
    openclaw gateway status
[/code]

Ви маєте побачити, що Gateway слухає порт 18789.

* ### Відкрийте панель керування

bashCopy code
[code]
    openclaw dashboard
[/code]

Це відкриє інтерфейс керування у вашому браузері. Якщо він завантажується, усе працює.

* ### Надішліть своє перше повідомлення

Введіть повідомлення в чаті інтерфейсу керування, і ви маєте отримати відповідь AI.

Хочете натомість спілкуватися з телефону? Найшвидший канал для налаштування — [Telegram](</uk/channels/telegram>) (потрібен лише токен бота). Усі варіанти див. у [Канали](</uk/channels>).

Додатково: змонтуйте спеціальну збірку інтерфейсу керування

Якщо ви підтримуєте локалізовану або налаштовану збірку панелі керування, укажіть `gateway.controlUi.root` на каталог, який містить зібрані статичні ресурси та `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Потім задайте:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Перезапустіть gateway і знову відкрийте панель керування:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Що робити далі

[**Підключіть канал** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo та інші. ](</uk/channels>) [**Сполучення та безпека** Контролюйте, хто може надсилати повідомлення вашому агенту. ](</uk/channels/pairing>) [**Налаштуйте Gateway** Моделі, інструменти, sandbox і додаткові налаштування. ](</uk/gateway/configuration>) [**Перегляньте інструменти** Браузер, exec, вебпошук, skills і plugins. ](</uk/tools>)

Додатково: змінні середовища

Якщо ви запускаєте OpenClaw як службовий обліковий запис або хочете використовувати власні шляхи:

  * `OPENCLAW_HOME` — домашній каталог для внутрішнього визначення шляхів
  * `OPENCLAW_STATE_DIR` — перевизначити каталог стану
  * `OPENCLAW_CONFIG_PATH` — перевизначити шлях до конфігураційного файла


Повний довідник: [Змінні середовища](</uk/help/environment>).

## Пов’язане

  * [Огляд установлення](</uk/install>)
  * [Огляд каналів](</uk/channels>)
  * [Налаштування](</uk/start/setup>)


Was this useful?YesNo
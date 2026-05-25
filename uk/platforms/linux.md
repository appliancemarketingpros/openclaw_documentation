---
title: Застосунок для Linux
source_url: https://docs.openclaw.ai/uk/platforms/linux
scraped_at: 2026-05-25
---

Gateway повністю підтримується в Linux. **Node є рекомендованим середовищем виконання**. Bun не рекомендовано для Gateway (помилки WhatsApp/Telegram).

Нативні супутні застосунки для Linux заплановані. Внески вітаються, якщо ви хочете допомогти створити такий застосунок.

## Швидкий шлях для початківців (VPS)

  1. Установіть Node 24 (рекомендовано; Node 22 LTS, наразі `22.16+`, усе ще працює для сумісності)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. З вашого ноутбука: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. Відкрийте `http://127.0.0.1:18789/` і автентифікуйтеся за допомогою налаштованого спільного секрету (токен за замовчуванням; пароль, якщо ви встановили `gateway.auth.mode: "password"`)


Повний посібник із сервера Linux: [Сервер Linux](</uk/vps>). Покроковий приклад VPS: [exe.dev](</uk/install/exe-dev>)

## Встановлення

  * [Початок роботи](</uk/start/getting-started>)
  * [Встановлення та оновлення](</uk/install/updating>)
  * Необов’язкові сценарії: [Bun (експериментально)](</uk/install/bun>), [Nix](</uk/install/nix>), [Docker](</uk/install/docker>)


## Gateway

  * [Операційний посібник Gateway](</uk/gateway>)
  * [Конфігурація](</uk/gateway/configuration>)


## Встановлення служби Gateway (CLI)

Скористайтеся одним із цих варіантів:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Або:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Або:

CodeCopy code
[code]
    openclaw configure
[/code]

Виберіть **Служба Gateway** , коли з’явиться запит.

Відновлення/міграція:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Керування системою (користувацький модуль systemd)

OpenClaw за замовчуванням установлює службу systemd **користувача**. Використовуйте **системну** службу для спільних або постійно ввімкнених серверів. `openclaw gateway install` і `openclaw onboard --install-daemon` уже створюють для вас поточний канонічний модуль; пишіть його вручну лише тоді, коли вам потрібне власне налаштування системи/менеджера служб. Повні вказівки щодо служби наведено в [операційному посібнику Gateway](</uk/gateway>).

Мінімальне налаштування:

Створіть `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

Увімкніть його:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## Тиск на пам’ять і завершення через OOM

У Linux ядро вибирає жертву OOM, коли хост, VM або cgroup контейнера вичерпує пам’ять. Gateway може бути невдалою жертвою, бо він володіє довготривалими сесіями та підключеннями каналів. Тому OpenClaw, коли можливо, зміщує пріоритет так, щоб тимчасові дочірні процеси завершувалися раніше за Gateway.

Для відповідних дочірніх процесів Linux OpenClaw запускає дочірній процес через коротку обгортку `/bin/sh`, яка підвищує власний `oom_score_adj` дочірнього процесу до `1000`, а потім виконує `exec` справжньої команди. Це непривілейована операція, оскільки дочірній процес лише збільшує власну ймовірність завершення через OOM.

Охоплені поверхні дочірніх процесів включають:

  * дочірні процеси команд, керовані супервізором,
  * дочірні процеси оболонки PTY,
  * дочірні процеси stdio-серверів MCP,
  * запущені OpenClaw процеси браузера/Chrome.


Обгортка працює лише в Linux і пропускається, коли `/bin/sh` недоступний. Вона також пропускається, якщо середовище дочірнього процесу встановлює `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`, `false`, `no` або `off`.

Щоб перевірити дочірній процес:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

Очікуване значення для охоплених дочірніх процесів — `1000`. Процес Gateway має зберігати свій звичайний показник, зазвичай `0`.

Це не замінює звичайного налаштування пам’яті. Якщо VPS або контейнер повторно завершує дочірні процеси, збільште ліміт пам’яті, зменште паралельність або додайте суворіші засоби контролю ресурсів, як-от systemd `MemoryMax=` або ліміти пам’яті на рівні контейнера.

## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Сервер Linux](</uk/vps>)
  * [Raspberry Pi](</uk/install/raspberry-pi>)


Was this useful?YesNo
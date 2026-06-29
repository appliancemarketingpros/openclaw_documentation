---
title: Приложение для Linux
source_url: https://docs.openclaw.ai/ru/platforms/linux
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

Gateway полностью поддерживается в Linux. **Node — рекомендуемая среда выполнения**. Bun не рекомендуется для Gateway (ошибки WhatsApp/Telegram).

Нативные сопутствующие приложения для Linux запланированы. Вклад приветствуется, если вы хотите помочь создать такое приложение.

## Быстрый путь для начинающих (VPS)

  1. Установите Node 24 (рекомендуется; Node 22 LTS, сейчас `22.19+`, по-прежнему работает для совместимости)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. С ноутбука: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. Откройте `http://127.0.0.1:18789/` и выполните аутентификацию с настроенным общим секретом (по умолчанию токен; пароль, если вы задали `gateway.auth.mode: "password"`)


Полное руководство по серверу Linux: [Сервер Linux](</ru/vps>). Пошаговый пример VPS: [exe.dev](</ru/install/exe-dev>)

## Установка

  * [Начало работы](</ru/start/getting-started>)
  * [Установка и обновления](</ru/install/updating>)
  * Необязательные сценарии: [Bun (экспериментально)](</ru/install/bun>), [Nix](</ru/install/nix>), [Docker](</ru/install/docker>)


## Gateway

  * [Руководство по эксплуатации Gateway](</ru/gateway>)
  * [Конфигурация](</ru/gateway/configuration>)


## Установка сервиса Gateway (CLI)

Используйте один из этих вариантов:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Или:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Или:

CodeCopy code
[code]
    openclaw configure
[/code]

При запросе выберите **Сервис Gateway**.

Исправить/мигрировать:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Управление системой (пользовательский unit systemd)

OpenClaw по умолчанию устанавливает **пользовательский** сервис systemd. Используйте **системный** сервис для общих или постоянно работающих серверов. `openclaw gateway install` и `openclaw onboard --install-daemon` уже создают для вас текущий канонический unit; пишите его вручную только когда нужна пользовательская настройка системы или менеджера сервисов. Полное руководство по сервису находится в [руководстве по эксплуатации Gateway](</ru/gateway>).

Минимальная настройка:

Создайте `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143OOMPolicy=continueKillMode=control-group [Install]WantedBy=default.target
[/code]

Включите его:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## Нагрузка на память и завершения из-за OOM

В Linux ядро выбирает жертву OOM, когда у хоста, VM или cgroup контейнера заканчивается память. Gateway может быть неудачной жертвой, потому что он владеет долгоживущими сеансами и подключениями каналов. Поэтому OpenClaw по возможности смещает приоритет так, чтобы временные дочерние процессы завершались раньше Gateway.

Для подходящих дочерних процессов Linux OpenClaw запускает дочерний процесс через короткую обертку `/bin/sh`, которая повышает собственное значение `oom_score_adj` дочернего процесса до `1000`, а затем выполняет `exec` реальной команды. Это непривилегированная операция, поскольку дочерний процесс только увеличивает собственную вероятность завершения OOM killer.

Покрываемые поверхности дочерних процессов включают:

  * дочерние процессы команд под управлением supervisor,
  * дочерние процессы оболочки PTY,
  * дочерние процессы stdio-серверов MCP,
  * запущенные OpenClaw процессы браузера/Chrome.


Обертка работает только в Linux и пропускается, если `/bin/sh` недоступен. Она также пропускается, если окружение дочернего процесса задает `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`, `false`, `no` или `off`.

Чтобы проверить дочерний процесс:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

Ожидаемое значение для покрываемых дочерних процессов — `1000`. Процесс Gateway должен сохранять свой обычный показатель, обычно `0`.

Рекомендуемый unit systemd также задает `OOMPolicy=continue`. Это сохраняет unit Gateway активным, когда временный дочерний процесс выбран OOM killer; дочерняя команда/сеанс может завершиться ошибкой и сообщить ее без того, чтобы systemd пометил весь сервис Gateway как сбойный и перезапустил все каналы.

Это не заменяет обычную настройку памяти. Если VPS или контейнер повторно завершает дочерние процессы, увеличьте лимит памяти, уменьшите параллелизм или добавьте более строгие средства контроля ресурсов, такие как systemd `MemoryMax=` или лимиты памяти на уровне контейнера.

## См. также

  * [Обзор установки](</ru/install>)
  * [Сервер Linux](</ru/vps>)
  * [Raspberry Pi](</ru/install/raspberry-pi>)


Was this useful?YesNo

Open issue
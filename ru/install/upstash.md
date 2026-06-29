---
title: Бокс Upstash
source_url: https://docs.openclaw.ai/ru/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Запустите постоянный OpenClaw Gateway в Upstash Box, управляемой среде Linux с поддержкой жизненного цикла keep-alive.

Для доступа к панели управления используйте SSH-туннель. Не открывайте порт Gateway напрямую в публичный интернет.

## Предварительные требования

  * Учетная запись Upstash
  * Upstash Box с keep-alive
  * SSH-клиент на вашем локальном компьютере


## Создание Box

Создайте Box с keep-alive в Upstash Console. Запишите Box ID, например `right-flamingo-14486`, и API-ключ вашего Box.

Upstash поддерживает актуальное руководство по OpenClaw Box по адресу [Настройка OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Подключение через SSH-туннель

Пробросьте порт панели управления OpenClaw на свой локальный компьютер. При запросе используйте API-ключ вашего Box как пароль SSH:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Параметры keepalive уменьшают разрывы неактивного туннеля во время онбординга.

## Установка OpenClaw

Внутри Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Запуск онбординга

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Следуйте подсказкам. Скопируйте URL панели управления и токен после завершения онбординга.

## Запуск Gateway

Настройте Gateway для сети Box и запустите его в фоновом режиме:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

При активном SSH-туннеле откройте URL панели управления локально:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Автоперезапуск

Задайте эту команду как init-скрипт Box, чтобы Gateway перезапускался при запуске Box:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Устранение неполадок

Если SSH зависает во время онбординга, переподключитесь с чистой конфигурацией SSH и keepalive:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Это обходит устаревшие локальные настройки `~/.ssh/config` и поддерживает туннель активным во время периодов простоя сети.

## См. также

  * [Удаленный доступ](</ru/gateway/remote>)
  * [Безопасность Gateway](</ru/gateway/security>)
  * [Обновление OpenClaw](</ru/install/updating>)


Was this useful?YesNo

Open issue
---
title: Бокс Upstash
source_url: https://docs.openclaw.ai/uk/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Запустіть постійний OpenClaw Gateway на Upstash Box, керованому середовищі Linux із підтримкою життєвого циклу keep-alive.

Використовуйте SSH-тунель для доступу до панелі керування. Не відкривайте порт Gateway безпосередньо для публічного інтернету.

## Передумови

  * Обліковий запис Upstash
  * Upstash Box із keep-alive
  * SSH-клієнт на вашій локальній машині


## Створення Box

Створіть Box із keep-alive у Upstash Console. Занотуйте ID Box, наприклад `right-flamingo-14486`, і API-ключ вашого Box.

Upstash підтримує поточний покроковий посібник OpenClaw Box за адресою [Налаштування OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Підключення через SSH-тунель

Переадресуйте порт панелі керування OpenClaw на вашу локальну машину. Використовуйте API-ключ вашого Box як пароль SSH, коли з’явиться запит:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Параметри keepalive зменшують кількість розривів неактивного тунелю під час онбордингу.

## Встановлення OpenClaw

Усередині Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Запуск онбордингу

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Дотримуйтеся підказок. Скопіюйте URL панелі керування та токен після завершення онбордингу.

## Запуск Gateway

Налаштуйте Gateway для мережі Box і запустіть його у фоновому режимі:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

За активного SSH-тунелю відкрийте URL панелі керування локально:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Автоматичний перезапуск

Установіть цю команду як init-скрипт Box, щоб Gateway перезапускався під час запуску Box:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Усунення несправностей

Якщо SSH зависає під час онбордингу, перепідключіться з чистою конфігурацією SSH і keepalive:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Це обходить застарілі локальні налаштування `~/.ssh/config` і підтримує тунель активним під час періодів неактивності мережі.

## Пов’язане

  * [Віддалений доступ](</uk/gateway/remote>)
  * [Безпека Gateway](</uk/gateway/security>)
  * [Оновлення OpenClaw](</uk/install/updating>)


Was this useful?YesNo

Open issue
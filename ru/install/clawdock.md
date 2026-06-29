---
title: ClawDock
source_url: https://docs.openclaw.ai/ru/install/clawdock
scraped_at: 2026-06-29
---

InstallContainers

ClawDock — это небольшой слой вспомогательных shell-команд для установок OpenClaw на базе Docker.

Он дает короткие команды вроде `clawdock-start`, `clawdock-dashboard` и `clawdock-fix-token` вместо более длинных вызовов `docker compose ...`.

Если вы еще не настроили Docker, начните с [Docker](</ru/install/docker>).

## Установка

Используйте канонический путь помощника:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Если раньше вы установили ClawDock из `scripts/shell-helpers/clawdock-helpers.sh`, переустановите его из нового пути `scripts/clawdock/clawdock-helpers.sh`. Старый raw-путь GitHub был удален.

## Что вы получите

### Базовые операции

Команда | Описание  
---|---  
`clawdock-start` | Запустить шлюз  
`clawdock-stop` | Остановить шлюз  
`clawdock-restart` | Перезапустить шлюз  
`clawdock-status` | Проверить состояние контейнера  
`clawdock-logs` | Отслеживать логи шлюза  
  
### Доступ к контейнеру

Команда | Описание  
---|---  
`clawdock-shell` | Открыть shell внутри контейнера шлюза  
`clawdock-cli <command>` | Выполнить команды OpenClaw CLI в Docker  
`clawdock-exec <command>` | Выполнить произвольную команду в контейнере  
  
### Веб-интерфейс и сопряжение

Команда | Описание  
---|---  
`clawdock-dashboard` | Открыть URL Control UI  
`clawdock-devices` | Показать ожидающие сопряжения устройств  
`clawdock-approve <id>` | Одобрить запрос на сопряжение  
  
### Настройка и обслуживание

Команда | Описание  
---|---  
`clawdock-fix-token` | Настроить токен шлюза внутри контейнера  
`clawdock-update` | Скачать, пересобрать и перезапустить  
`clawdock-rebuild` | Только пересобрать образ Docker  
`clawdock-clean` | Удалить контейнеры и тома  
  
### Утилиты

Команда | Описание  
---|---  
`clawdock-health` | Выполнить проверку работоспособности шлюза  
`clawdock-token` | Вывести токен шлюза  
`clawdock-cd` | Перейти в каталог проекта OpenClaw  
`clawdock-config` | Открыть `~/.openclaw`  
`clawdock-show-config` | Вывести файлы конфигурации с замаскированными значениями  
`clawdock-workspace` | Открыть каталог рабочей области  
  
## Первый запуск

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Если браузер сообщает, что требуется сопряжение:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Конфигурация и секреты

ClawDock работает с тем же разделением Docker-конфигурации, которое описано в [Docker](</ru/install/docker>):

  * `<project>/.env` для значений, специфичных для Docker, таких как имя образа, порты и токен шлюза
  * `~/.openclaw/.env` для ключей провайдеров и токенов ботов, задаваемых через env
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` для сохраненной OAuth/API-key-аутентификации провайдеров
  * `~/.openclaw/openclaw.json` для конфигурации поведения


Используйте `clawdock-show-config`, когда нужно быстро просмотреть файлы `.env` и `openclaw.json`. В выводе он маскирует значения `.env`.

## См. также

[**Docker** Каноническая установка Docker для OpenClaw. ](</ru/install/docker>) [**Среда выполнения Docker VM** Управляемая Docker среда выполнения VM для усиленной изоляции. ](</ru/install/docker-vm-runtime>) [**Обновление** Обновление пакета OpenClaw и управляемых сервисов. ](</ru/install/updating>)

Was this useful?YesNo

Open issue
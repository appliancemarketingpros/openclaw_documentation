---
title: Northflank
source_url: https://docs.openclaw.ai/ru/install/northflank
scraped_at: 2026-06-29
---

InstallHosting

# Northflank

Разверните OpenClaw на Northflank с помощью шаблона в один клик и получайте доступ к нему через веб-интерфейс Control UI. Это самый простой путь «без терминала на сервере»: Northflank запускает Gateway за вас.

## Как начать

  1. Нажмите [Развернуть OpenClaw](<https://northflank.com/stacks/deploy-openclaw>), чтобы открыть шаблон.
  2. Создайте [аккаунт на Northflank](<https://app.northflank.com/signup>), если у вас его еще нет.
  3. Нажмите **Развернуть OpenClaw сейчас**.
  4. Задайте обязательную переменную окружения: `OPENCLAW_GATEWAY_TOKEN` (используйте надежное случайное значение).
  5. Нажмите **Развернуть стек** , чтобы собрать и запустить шаблон OpenClaw.
  6. Дождитесь завершения развертывания, затем нажмите **Просмотреть ресурсы**.
  7. Откройте сервис OpenClaw.
  8. Откройте публичный URL OpenClaw по адресу `/openclaw` и подключитесь с помощью настроенного общего секрета. По умолчанию этот шаблон использует `OPENCLAW_GATEWAY_TOKEN`; если вы замените его аутентификацией по паролю, используйте вместо него этот пароль.


## Что вы получите

  * Размещенный OpenClaw Gateway + Control UI
  * Постоянное хранилище через Northflank Volume (`/data`), чтобы `openclaw.json`, `auth-profiles.json` для каждого агента, состояние каналов/провайдеров, сессии и рабочая область сохранялись при повторных развертываниях


## Подключение канала

Используйте Control UI по адресу `/openclaw` или запустите `openclaw onboard` через SSH, чтобы получить инструкции по настройке канала:

  * [Telegram](</ru/channels/telegram>) (самый быстрый вариант — нужен только токен бота)
  * [Discord](</ru/channels/discord>)
  * [Все каналы](</ru/channels>)


## Следующие шаги

  * Настройте каналы обмена сообщениями: [Каналы](</ru/channels>)
  * Настройте Gateway: [Конфигурация Gateway](</ru/gateway/configuration>)
  * Поддерживайте OpenClaw в актуальном состоянии: [Обновление](</ru/install/updating>)


Was this useful?YesNo

Open issue
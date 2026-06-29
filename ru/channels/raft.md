---
title: Raft
source_url: https://docs.openclaw.ai/ru/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Поддержка Raft подключает агента OpenClaw к внешнему агенту Raft через локальный Raft CLI. Raft отправляет аутентифицированные сигналы пробуждения в Gateway. Затем агент использует Raft CLI для проверки и отправки сообщений.

## Установка

Raft — официальный внешний плагин. Установите его на хосте Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Подробнее: [Плагины](</ru/tools/plugin>)

## Предварительные требования

  * Рабочая область Raft с внешним агентом.
  * Raft CLI установлен на том же хосте, что и OpenClaw Gateway.
  * Профиль Raft CLI, в который уже выполнен вход и который связан с этим внешним агентом.


Плагин не хранит учетные данные Raft. Raft CLI хранит эту аутентификацию в собственном профиле.

## Настройка

Задайте профиль в конфигурации:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Для учетной записи по умолчанию вместо этого можно задать `RAFT_PROFILE` в окружении Gateway:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Используйте именованную учетную запись, когда один Gateway подключается к нескольким внешним агентам Raft:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

Интерактивный процесс настройки записывает тот же профиль:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Как это работает

При запуске Gateway плагин:

  1. Открывает HTTP-эндпоинт пробуждения только для loopback на эфемерном порту.
  2. Запускает `raft --profile <profile> agent bridge` с этим эндпоинтом и токеном для текущего процесса.
  3. Принимает только аутентифицированные сигналы пробуждения без содержимого с идентификатором повтора от локального моста.
  4. Требует одно из полей: `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` или `id`.
  5. Дедуплицирует недавние повторные доставки пробуждения по идентификатору события моста, в том числе между перезапусками Gateway.
  6. Возвращает стабильную runtime-сессию для текущего моста и пустой пакет очистки активности для протокола Raft CLI.
  7. Запускает один сериализованный ход агента OpenClaw для каждого принятого пробуждения.


Мост отвечает за повторные попытки доставки Raft и переподключения. Ход OpenClaw получает только уведомление о пробуждении, а не скопированное тело сообщения Raft. Он использует CLI для чтения ожидающих сообщений и отправки ответа:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Проверка

Проверьте, что OpenClaw может найти CLI и имеет настроенный профиль:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Затем отправьте сообщение внешнему агенту Raft. В журнале Gateway должен появиться запуск моста Raft, а затем входящее пробуждение. Агент должен использовать настроенный профиль Raft для проверки ожидающих сообщений.

## Устранение неполадок

Raft CLI отсутствует

Установите Raft CLI на хост Gateway и сделайте `raft` доступным в `PATH` службы. Проверьте это с помощью `raft --help`, затем перезапустите Gateway.

Мост сразу завершает работу

Убедитесь, что для настроенного профиля выполнен вход и что он принадлежит нужному внешнему агенту Raft. Запустите `raft --profile <profile> agent bridge` напрямую, чтобы увидеть диагностическое сообщение CLI.

Пробуждение приходит, но ответ Raft не отправляется

Это ожидаемо, если агент не вызывает Raft CLI. Мост пробуждения не передает тела сообщений или автоматические итоговые ответы. Проверьте политику инструментов агента и убедитесь, что он может запускать `raft --profile <profile> message check` и `message send`.

## Ссылки

  * [Raft](<https://raft.build/>)
  * [Документация Raft](<https://docs.raft.build/welcome/>)
  * [Интеграция Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue
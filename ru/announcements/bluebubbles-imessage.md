---
title: Удаление BlueBubbles и путь imsg iMessage
source_url: https://docs.openclaw.ai/ru/announcements/bluebubbles-imessage
scraped_at: 2026-06-29
---

ChannelsOverview

# Удаление BlueBubbles и путь imsg для iMessage

OpenClaw больше не поставляет канал BlueBubbles. Поддержка iMessage теперь работает через встроенный plugin `imessage`, который запускает [`imsg`](<https://github.com/steipete/imsg>) локально или через SSH-обертку и обменивается JSON-RPC через stdin/stdout.

Если ваша конфигурация все еще содержит `channels.bluebubbles`, перенесите ее в `channels.imessage`. Устаревший URL документации `/channels/bluebubbles` перенаправляет на [Переход с BlueBubbles](</ru/channels/imessage-from-bluebubbles>), где есть полная таблица переноса конфигурации и контрольный список перехода.

## Что изменилось

  * В поддерживаемом пути OpenClaw для iMessage нет HTTP-сервера BlueBubbles, маршрута webhook, пароля REST или runtime plugin BlueBubbles.
  * OpenClaw читает и отслеживает сообщения через `imsg` на Mac, где выполнен вход в Messages.app.
  * Базовая отправка, получение, история и медиа используют обычные интерфейсы `imsg` и разрешения macOS.
  * Расширенные действия, такие как ответы в ветках, tapbacks, редактирование, отмена отправки, эффекты, уведомления о прочтении, индикаторы набора текста и управление группами, требуют `imsg launch` с доступным мостом private API.
  * Шлюзы Linux и Windows все еще могут использовать iMessage, задав `channels.imessage.cliPath` как SSH-обертку, которая запускает `imsg` на Mac с выполненным входом.


## Что сделать

  1. Установите и проверьте `imsg` на Mac с Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Предоставьте разрешения Full Disk Access и Automation контексту процесса, который запускает `imsg` и OpenClaw.

  3. Перенесите старую конфигурацию:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Перезапустите Gateway и проверьте:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Протестируйте личные сообщения, группы, вложения и любые действия private API, от которых вы зависите, прежде чем удалять старый сервер BlueBubbles.


## Примечания по миграции

  * У `channels.bluebubbles.serverUrl` и `channels.bluebubbles.password` нет эквивалента в iMessage.
  * У `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, корней вложений, ограничений размера медиа, разбиения на части и переключателей действий есть эквиваленты в iMessage.
  * `channels.imessage.includeAttachments` по умолчанию все еще отключен. Задайте его явно, если ожидаете, что входящие фотографии, голосовые заметки, видео или файлы будут доходить до агента.
  * С `groupPolicy: "allowlist"` скопируйте старый блок `groups`, включая любую wildcard-запись `"*"`. Списки разрешенных отправителей групп и реестр групп являются отдельными проверками.
  * Привязки ACP, которые совпадали с `channel: "bluebubbles"`, нужно изменить на `channel: "imessage"`.
  * Старые ключи сеансов BlueBubbles не становятся ключами сеансов iMessage. Одобрения pairing переносятся по handle, но история разговоров под ключами сеансов BlueBubbles не переносится.


## См. также

  * [Переход с BlueBubbles](</ru/channels/imessage-from-bluebubbles>)
  * [iMessage](</ru/channels/imessage>)
  * [Справочник конфигурации - iMessage](</ru/gateway/config-channels#imessage>)


Was this useful?YesNo

Open issue
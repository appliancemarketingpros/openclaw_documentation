---
title: Видалення BlueBubbles і шлях imsg для iMessage
source_url: https://docs.openclaw.ai/uk/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Видалення BlueBubbles і шлях imsg для iMessage

OpenClaw більше не постачає канал BlueBubbles. Підтримка iMessage тепер працює через вбудований Plugin `imessage`, який запускає [`imsg`](<https://github.com/steipete/imsg>) локально або через SSH-обгортку та обмінюється JSON-RPC через stdin/stdout.

Якщо ваша конфігурація досі містить `channels.bluebubbles`, перенесіть її до `channels.imessage`. Застаріла URL-адреса документації `/channels/bluebubbles` переспрямовує на [Перехід із BlueBubbles](</uk/channels/imessage-from-bluebubbles>), де є повна таблиця перетворення конфігурації та контрольний список переходу.

## Що змінилося

  * У підтримуваному шляху OpenClaw для iMessage немає HTTP-сервера BlueBubbles, маршруту Webhook, REST-пароля або середовища виконання Plugin BlueBubbles.
  * OpenClaw читає й відстежує Messages через `imsg` на Mac, де виконано вхід у Messages.app.
  * Базове надсилання, отримання, історія та медіа використовують звичайні поверхні `imsg` і дозволи macOS.
  * Розширені дії, як-от відповіді в гілках, tapback-реакції, редагування, скасування надсилання, ефекти, сповіщення про прочитання, індикатори набору тексту та керування групами, потребують `imsg launch` із доступним мостом приватного API.
  * Gateway на Linux і Windows усе ще можуть використовувати iMessage, якщо задати `channels.imessage.cliPath` як SSH-обгортку, що запускає `imsg` на Mac, де виконано вхід.


## Що зробити

  1. Установіть і перевірте `imsg` на Mac із Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Надайте дозволи Full Disk Access і Automation контексту процесу, який запускає `imsg` та OpenClaw.

  3. Перетворіть стару конфігурацію:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Перезапустіть Gateway і перевірте:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Перевірте приватні повідомлення, групи, вкладення та будь-які дії приватного API, від яких ви залежите, перш ніж видаляти старий сервер BlueBubbles.


## Нотатки щодо міграції

  * `channels.bluebubbles.serverUrl` і `channels.bluebubbles.password` не мають відповідника в iMessage.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, корені вкладень, обмеження розміру медіа, розбиття на частини та перемикачі дій мають відповідники в iMessage.
  * `channels.imessage.includeAttachments` досі вимкнено за замовчуванням. Увімкніть це явно, якщо очікуєте, що вхідні фотографії, голосові нотатки, відео або файли потраплятимуть до агента.
  * З `groupPolicy: "allowlist"` скопіюйте старий блок `groups`, зокрема будь-який запис-джокер `"*"`. Списки дозволених відправників груп і реєстр груп є окремими шлюзами.
  * Прив’язки ACP, які відповідали `channel: "bluebubbles"`, потрібно змінити на `channel: "imessage"`.
  * Старі ключі сеансів BlueBubbles не стають ключами сеансів iMessage. Схвалення сполучення переносяться за ідентифікатором, але історія розмов під ключами сеансів BlueBubbles не переноситься.


## Див. також

  * [Перехід із BlueBubbles](</uk/channels/imessage-from-bluebubbles>)
  * [iMessage](</uk/channels/imessage>)
  * [Довідник конфігурації - iMessage](</uk/gateway/config-channels#imessage>)


Was this useful?YesNo
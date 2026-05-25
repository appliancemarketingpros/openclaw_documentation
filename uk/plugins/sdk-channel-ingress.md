---
title: API вхідного потоку каналу
source_url: https://docs.openclaw.ai/uk/plugins/sdk-channel-ingress
scraped_at: 2026-05-25
---

# API вхідного доступу каналу

Вхідний доступ каналу — це експериментальна межа контролю доступу для вхідних подій каналу. Використовуйте `openclaw/plugin-sdk/channel-ingress-runtime` для шляхів отримання. Старіший підшлях `openclaw/plugin-sdk/channel-ingress` залишається експортованим як застарілий фасад сумісності для сторонніх plugins.

Plugins володіють фактами платформи та побічними ефектами. Ядро володіє загальною політикою: списками дозволених DM/груп, DM-записами сховища спарювання, шлюзами маршрутів, шлюзами команд, авторизацією подій, активацією за згадкою, редагованою діагностикою та допуском.

## Розпізнавач часу виконання

tsCopy code
[code]
       defineStableChannelIngressIdentity,  resolveChannelMessageIngress,} from "openclaw/plugin-sdk/channel-ingress-runtime"; const identity = defineStableChannelIngressIdentity({  key: "platform-user-id",  normalize: normalizePlatformUserId,  sensitivity: "pii",}); const result = await resolveChannelMessageIngress({  channelId: "my-channel",  accountId,  identity,  subject: { stableId: platformUserId },  conversation: { kind: isGroup ? "group" : "direct", id: conversationId },  event: { kind: "message", authMode: "inbound", mayPair: !isGroup },  policy: {    dmPolicy: config.dmPolicy,    groupPolicy: config.groupPolicy,    groupAllowFromFallbackToAllowFrom: true,  },  allowFrom: config.allowFrom,  groupAllowFrom: config.groupAllowFrom,  accessGroups: cfg.accessGroups,  route,  readStoreAllowFrom,  command: hasControlCommand ? { allowTextCommands: true, hasControlCommand } : undefined,});
[/code]

Не обчислюйте заздалегідь ефективні списки дозволених, власників команд або групи команд. Розпізнавач виводить їх із сирих списків дозволених, callback-ів сховища, дескрипторів маршрутів, груп доступу, політики та типу розмови.

## Результат

Вбудовані plugins мають напряму споживати сучасні проєкції:

  * `ingress`: впорядковане рішення шлюзу та допуск
  * `senderAccess`: лише авторизація відправника/розмови
  * `routeAccess`: проєкція маршруту та відправника маршруту
  * `commandAccess`: авторизація команди; `false`, коли шлюз команди не запускався
  * `activationAccess`: результат згадки/активації


Авторизація події залишається доступною у впорядкованому `ingress.graph` та вирішальному `ingress.reasonCode`; окрема проєкція події не створюється.

Застарілі допоміжні засоби SDK для сторонніх розробників можуть внутрішньо відновлювати старіші форми. Нові вбудовані шляхи отримання не повинні перетворювати сучасні результати назад у локальні DTO.

## Групи доступу

Записи `accessGroup:<name>` залишаються редагованими. Ядро самостійно розпізнає статичні групи `message.senders` і викликає `resolveAccessGroupMembership` лише для динамічних груп, які потребують пошуку на платформі. Відсутні, непідтримувані та помилкові групи закривають доступ.

## Режими подій

`authMode` | Значення  
---|---  
`inbound` | звичайні шлюзи вхідного відправника  
`command` | шлюзи команд для callback-ів або кнопок з областю дії  
`origin-subject` | актор має збігатися із суб'єктом оригінального повідомлення  
`route-only` | лише шлюзи маршрутів для довірених подій у межах маршруту  
`none` | внутрішні події, що належать plugin, обходять спільну авторизацію  
  
Використовуйте `mayPair: false` для реакцій, кнопок, callback-ів і нативних команд.

## Маршрути та активація

Використовуйте дескриптори маршрутів для політики кімнати, теми, гільдії, потоку або вкладеного маршруту:

tsCopy code
[code]
    route: {  id: "room",  allowed: roomAllowed,  enabled: roomEnabled,  senderPolicy: "replace",  senderAllowFrom: roomAllowFrom,  blockReason: "room_sender_not_allowlisted",}
[/code]

Використовуйте `channelIngressRoutes(...)`, коли plugin має кілька необов'язкових дескрипторів маршрутів; він фільтрує вимкнені гілки, зберігаючи факти маршруту загальними та впорядкованими за `precedence` кожного дескриптора.

Шлюз згадок є шлюзом активації. Пропущена згадка повертає `admission: "skip"`, щоб ядро ходу не обробляло хід лише для спостереження. Більшість каналів мають залишати активацію після шлюзів відправника та команд. Публічні чат-поверхні, які мають приглушувати трафік без згадок до шуму списку дозволених відправників, можуть увімкнути `activation.order: "before-sender"`, коли обхід текстовими командами вимкнено. Канали з неявною активацією, як-от відповіді в потоках бота, можуть передати `activation.allowedImplicitMentionKinds`; спроєктований `activationAccess.shouldBypassMention` тоді повідомляє, коли команда або неявна активація обійшла явну згадку.

## Редагування

Сирі значення відправника та сирі записи списку дозволених є лише вхідними даними розпізнавача. Вони не повинні з'являтися в розпізнаному стані, рішеннях, діагностиці, знімках або фактах сумісності. Використовуйте непрозорі ідентифікатори суб'єктів, ідентифікатори записів, ідентифікатори маршрутів та діагностичні ідентифікатори.

## Перевірка

bashCopy code
[code]
    pnpm test src/channels/message-access/message-access.test.ts src/plugin-sdk/channel-ingress-runtime.test.tspnpm plugin-sdk:api:check
[/code]

Was this useful?YesNo
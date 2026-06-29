---
title: API входа канала
source_url: https://docs.openclaw.ai/ru/plugins/sdk-channel-ingress
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

# API входящих событий каналов

Входящие события каналов — это экспериментальная граница контроля доступа для входящих событий каналов. Используйте `openclaw/plugin-sdk/channel-ingress-runtime` для путей приема. Более старый подпуть `openclaw/plugin-sdk/channel-ingress` остается экспортируемым как устаревший совместимый фасад для сторонних plugins.

Plugins владеют фактами платформы и побочными эффектами. Ядро владеет общей политикой: списками разрешенных DM/групп, DM-записями хранилища сопряжения, шлюзами маршрутов, шлюзами команд, авторизацией событий, активацией по упоминанию, редактированными диагностическими данными и допуском.

## Runtime Resolver

tsCopy code
[code]
       defineStableChannelIngressIdentity,  resolveChannelMessageIngress,} from "openclaw/plugin-sdk/channel-ingress-runtime"; const identity = defineStableChannelIngressIdentity({  key: "platform-user-id",  normalize: normalizePlatformUserId,  sensitivity: "pii",}); const result = await resolveChannelMessageIngress({  channelId: "my-channel",  accountId,  identity,  subject: { stableId: platformUserId },  conversation: { kind: isGroup ? "group" : "direct", id: conversationId },  event: { kind: "message", authMode: "inbound", mayPair: !isGroup },  policy: {    dmPolicy: config.dmPolicy,    groupPolicy: config.groupPolicy,    groupAllowFromFallbackToAllowFrom: true,  },  allowFrom: config.allowFrom,  groupAllowFrom: config.groupAllowFrom,  accessGroups: cfg.accessGroups,  route,  readStoreAllowFrom,  command: hasControlCommand ? { allowTextCommands: true, hasControlCommand } : undefined,});
[/code]

Не вычисляйте заранее эффективные списки разрешенных, владельцев команд или группы команд. Resolver выводит их из исходных списков разрешенных, callback-функций хранилища, дескрипторов маршрутов, групп доступа, политики и типа беседы.

## Результат

Встроенные plugins должны напрямую использовать современные проекции:

  * `ingress`: упорядоченное решение шлюза и допуск
  * `senderAccess`: только авторизация отправителя/беседы
  * `routeAccess`: проекция маршрута и отправителя маршрута
  * `commandAccess`: авторизация команды; `false`, если шлюз команд не запускался
  * `activationAccess`: результат упоминания/активации


Авторизация событий остается доступной в упорядоченном `ingress.graph` и решающем `ingress.reasonCode`; отдельная проекция события не создается.

Устаревшие helpers SDK для сторонних разработчиков могут внутренне пересобирать старые формы. Новые встроенные пути приема не должны переводить современные результаты обратно в локальные DTO.

## Группы доступа

Записи `accessGroup:<name>` остаются редактированными. Ядро само разрешает статические группы `message.senders` и вызывает `resolveAccessGroupMembership` только для динамических групп, которым требуется поиск на платформе. Отсутствующие, неподдерживаемые и сбойные группы закрываются с отказом.

## Режимы событий

`authMode` | Значение  
---|---  
`inbound` | обычные шлюзы входящего отправителя  
`command` | шлюзы команд для callbacks или кнопок с областью  
`origin-subject` | актор должен совпадать с субъектом исходного сообщения  
`route-only` | только шлюзы маршрута для доверенных событий в области маршрута  
`none` | внутренние события, принадлежащие plugin, обходят общую авторизацию  
  
Используйте `mayPair: false` для реакций, кнопок, callbacks и нативных команд.

## Маршруты и активация

Используйте дескрипторы маршрутов для политики комнаты, темы, гильдии, треда или вложенного маршрута:

tsCopy code
[code]
    route: {  id: "room",  allowed: roomAllowed,  enabled: roomEnabled,  senderPolicy: "replace",  senderAllowFrom: roomAllowFrom,  blockReason: "room_sender_not_allowlisted",}
[/code]

Используйте `channelIngressRoutes(...)`, когда у plugin есть несколько необязательных дескрипторов маршрутов; он отфильтровывает отключенные ветви, сохраняя факты маршрута универсальными и упорядоченными по `precedence` каждого дескриптора.

Шлюз упоминаний является шлюзом активации. Промах упоминания возвращает `admission: "skip"`, чтобы ядро turn не обрабатывало turn только для наблюдения. Большинству каналов следует оставлять активацию после шлюзов отправителя и команд. Публичные чат-поверхности, которым нужно приглушать трафик без упоминаний до шума списка разрешенных отправителей, могут включить `activation.order: "before-sender"`, когда обход текстовыми командами отключен. Каналы с неявной активацией, например ответы в bot threads, могут передавать `activation.allowedImplicitMentionKinds`; спроецированное `activationAccess.shouldBypassMention` затем сообщает, когда команда или неявная активация обошли явное упоминание.

## Редактирование

Сырые значения отправителя и сырые записи списков разрешенных являются только входными данными resolver. Они не должны появляться в разрешенном состоянии, решениях, диагностике, снимках или фактах совместимости. Используйте непрозрачные идентификаторы субъектов, идентификаторы записей, идентификаторы маршрутов и диагностические идентификаторы.

## Проверка

bashCopy code
[code]
    pnpm test src/channels/message-access/message-access.test.ts src/plugin-sdk/channel-ingress-runtime.test.tspnpm plugin-sdk:api:check
[/code]

Was this useful?YesNo

Open issue
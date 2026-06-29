---
title: API входящих сообщений канала
source_url: https://docs.openclaw.ai/ru/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Plugin каналов должны моделировать пути получения через существительные inbound и message:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Используйте `openclaw/plugin-sdk/channel-inbound` для нормализации входящих событий, форматирования, корней и оркестрации. Используйте `openclaw/plugin-sdk/channel-outbound` для нативной отправки, подтверждений получения, надежной доставки и поведения живого предпросмотра.

## Основные вспомогательные функции

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: проецирует нормализованные факты канала в контекст промпта/сессии. Используйте `channelContext`, чтобы передавать принадлежащие каналу метаданные отправителя/чата в хук Plugin `ctx.channelContext`; расширяйте `PluginHookChannelSenderContext` или `PluginHookChannelChatContext` из этого подпути для полей, специфичных для канала.
  * `runChannelInboundEvent(...)`: выполняет прием, классификацию, предварительную проверку, разрешение, запись, dispatch и финализацию для одного входящего события платформы.
  * `dispatchChannelInboundReply(...)`: записывает и отправляет уже собранный входящий ответ через адаптер доставки.


Внедренный рантайм Plugin предоставляет те же высокоуровневые вспомогательные функции в `runtime.channel.inbound.*` для встроенных/нативных каналов, которые уже получают объект рантайма.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Диспетчеры совместимости должны собирать входные данные `dispatchChannelInboundReply(...)` и держать доставку платформы в адаптере доставки. Новые пути отправки должны предпочитать адаптеры сообщений и вспомогательные функции надежных сообщений.

## Миграция

Старые псевдонимы рантайма `runtime.channel.turn.*` были удалены. Используйте:

  * `runtime.channel.inbound.run(...)` для сырых входящих событий.
  * `runtime.channel.inbound.dispatchReply(...)` для собранных контекстов ответа.
  * `runtime.channel.inbound.buildContext(...)` для полезных нагрузок входящего контекста.
  * `runtime.channel.inbound.runPreparedReply(...)` только для принадлежащих каналу подготовленных путей dispatch, которые уже собирают собственное замыкание dispatch.


Новый код Plugin не должен вводить API каналов с именем `turn`. Держите лексику model или agent turn внутри кода агентов/провайдеров; Plugin каналов используют термины inbound, message, delivery и reply.

Was this useful?YesNo

Open issue
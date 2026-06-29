---
title: API исходящих каналов
source_url: https://docs.openclaw.ai/ru/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel plugins должны предоставлять поведение исходящих сообщений из `openclaw/plugin-sdk/channel-outbound`. Используйте `openclaw/plugin-sdk/channel-inbound` для оркестрации приема/контекста/dispatch.

Ядро отвечает за очереди, надежное хранение, общую политику повторов, hooks, receipts и общий инструмент `message`. Plugin отвечает за нативные вызовы send/edit/delete, нормализацию target, потоки платформы, выбранные цитаты, флаги уведомлений, состояние учетной записи и специфичные для платформы побочные эффекты.

## Адаптер

Большинство plugins определяют один адаптер `message`:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

Объявляйте только те capabilities, которые нативный транспорт действительно сохраняет. Покрывайте каждую объявленную capability для отправки, receipt, live-preview и receive-ack contract helpers, экспортируемыми из этого подпути.

## Существующие исходящие адаптеры

Если у канала уже есть совместимый адаптер `outbound`, создайте message adapter на его основе вместо дублирования кода отправки:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## Надежные отправки

Вспомогательные функции отправки runtime также находятся в `channel-outbound`:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * вспомогательные функции чернового streaming/progress, такие как `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` возвращает один явный outcome:

  * `sent`: доставлено как минимум одно видимое сообщение платформы.
  * `suppressed`: ни одно сообщение платформы не должно считаться отсутствующим.
  * `partial_failed`: как минимум одно сообщение платформы было доставлено до того, как более поздний payload или побочный эффект завершился с ошибкой.
  * `failed`: не был создан platform receipt.


Используйте `payloadOutcomes`, когда batch смешивает отправленные, suppressed и failed payloads. Не выводите отмену hook из пустого legacy результата direct-delivery.

## Dispatch совместимости

Dispatch входящих ответов следует собирать через `dispatchChannelInboundReply(...)` из `channel-inbound`. Держите доставку платформы в delivery adapter; используйте `channel-outbound` для message adapters, durable sends, receipts, live preview и параметров reply pipeline.

Was this useful?YesNo

Open issue
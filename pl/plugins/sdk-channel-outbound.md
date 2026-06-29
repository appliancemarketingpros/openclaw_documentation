---
title: API wychodzące kanału
source_url: https://docs.openclaw.ai/pl/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Pluginy kanałów powinny udostępniać zachowanie wiadomości wychodzących z `openclaw/plugin-sdk/channel-outbound`. Użyj `openclaw/plugin-sdk/channel-inbound` do orkiestracji odbierania, kontekstu i przekazywania.

Core odpowiada za kolejkowanie, trwałość, ogólną politykę ponawiania, hooki, potwierdzenia odbioru oraz wspólne narzędzie `message`. Plugin odpowiada za natywne wywołania send/edit/delete, normalizację celu, wątki platformy, wybrane cytaty, flagi powiadomień, stan konta oraz skutki uboczne specyficzne dla platformy.

## Adapter

Większość Pluginów definiuje jeden adapter `message`:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

Deklaruj tylko możliwości, które natywny transport faktycznie zachowuje. Obejmij każdą zadeklarowaną możliwość wysyłania, potwierdzeń odbioru, podglądu na żywo i potwierdzeń odebrania pomocnikami kontraktu eksportowanymi z tej podścieżki.

## Istniejące adaptery wychodzące

Jeśli kanał ma już zgodny adapter `outbound`, wyprowadź z niego adapter wiadomości zamiast duplikować kod wysyłania:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## Trwałe wysyłanie

Pomocniki wysyłania runtime również znajdują się w `channel-outbound`:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * pomocniki strumieniowania/postępu wersji roboczej, takie jak `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` zwraca jeden jawny wynik:

  * `sent`: dostarczono co najmniej jedną widoczną wiadomość platformy.
  * `suppressed`: żadna wiadomość platformy nie powinna być traktowana jako brakująca.
  * `partial_failed`: dostarczono co najmniej jedną wiadomość platformy, zanim późniejszy payload lub skutek uboczny zakończył się niepowodzeniem.
  * `failed`: nie utworzono żadnego potwierdzenia odbioru platformy.


Użyj `payloadOutcomes`, gdy partia miesza payloady wysłane, pominięte i nieudane. Nie wnioskuj anulowania hooka z pustego wyniku starszego bezpośredniego dostarczania.

## Przekazywanie zgodnościowe

Przekazywanie odpowiedzi przychodzących powinno być składane przez `dispatchChannelInboundReply(...)` z `channel-inbound`. Zachowaj dostarczanie platformowe w adapterze dostarczania; używaj `channel-outbound` do adapterów wiadomości, trwałego wysyłania, potwierdzeń odbioru, podglądu na żywo i opcji potoku odpowiedzi.

Was this useful?YesNo

Open issue
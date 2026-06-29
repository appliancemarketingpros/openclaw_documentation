---
title: API in uscita del canale
source_url: https://docs.openclaw.ai/it/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

I Plugin di canale devono esporre il comportamento dei messaggi in uscita da `openclaw/plugin-sdk/channel-outbound`. Usa `openclaw/plugin-sdk/channel-inbound` per l’orchestrazione di ricezione/contesto/invio.

Il core gestisce accodamento, durabilità, criterio generico di ripetizione, hook, ricevute e lo strumento `message` condiviso. Il Plugin gestisce chiamate native di invio/modifica/eliminazione, normalizzazione della destinazione, threading della piattaforma, citazioni selezionate, flag di notifica, stato dell’account ed effetti collaterali specifici della piattaforma.

## Adattatore

La maggior parte dei Plugin definisce un adattatore `message`:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

Dichiara solo le funzionalità che il trasporto nativo conserva effettivamente. Copri ogni funzionalità dichiarata di invio, ricevuta, anteprima live e conferma di ricezione con gli helper di contratto esportati da questo sottopercorso.

## Adattatori in uscita esistenti

Se il canale ha già un adattatore `outbound` compatibile, deriva l’adattatore di messaggio invece di duplicare il codice di invio:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## Invii durabili

Gli helper di invio runtime si trovano anche in `channel-outbound`:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * helper di streaming/avanzamento bozza come `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` restituisce un risultato esplicito:

  * `sent`: almeno un messaggio visibile della piattaforma è stato consegnato.
  * `suppressed`: nessun messaggio della piattaforma deve essere trattato come mancante.
  * `partial_failed`: almeno un messaggio della piattaforma è stato consegnato prima che un payload successivo o un effetto collaterale non riuscisse.
  * `failed`: non è stata prodotta alcuna ricevuta della piattaforma.


Usa `payloadOutcomes` quando un batch combina payload inviati, soppressi e non riusciti. Non dedurre l’annullamento degli hook da un risultato di consegna diretta legacy vuoto.

## Dispatch di compatibilità

Il dispatch delle risposte in entrata deve essere assemblato tramite `dispatchChannelInboundReply(...)` da `channel-inbound`. Mantieni la consegna della piattaforma nell’adattatore di consegna; usa `channel-outbound` per adattatori di messaggio, invii durabili, ricevute, anteprima live e opzioni della pipeline di risposta.

Was this useful?YesNo

Open issue
---
title: Reazioni
source_url: https://docs.openclaw.ai/it/tools/reactions
scraped_at: 2026-05-25
---

L'agente può aggiungere e rimuovere reazioni emoji sui messaggi usando lo strumento `message` con l'azione `react`. Il comportamento delle reazioni varia in base al canale e al trasporto.

## Come funziona

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * `emoji` è obbligatorio quando si aggiunge una reazione.
  * Imposta `emoji` su una stringa vuota (`""`) per rimuovere le reazioni del bot.
  * Imposta `remove: true` per rimuovere un emoji specifico (richiede `emoji` non vuoto).
  * Sui canali che supportano le reazioni di stato, `trackToolCalls: true` su una reazione consente al runtime di usare quel messaggio reagito per le reazioni di avanzamento degli strumenti successive durante lo stesso turno.


## Comportamento dei canali

Discord e Slack

  * `emoji` vuoto rimuove tutte le reazioni del bot sul messaggio.
  * `remove: true` rimuove solo l'emoji specificato.

Google Chat

  * `emoji` vuoto rimuove le reazioni dell'app sul messaggio.
  * `remove: true` rimuove solo l'emoji specificato.

Telegram

  * `emoji` vuoto rimuove le reazioni del bot.
  * `remove: true` rimuove anche le reazioni, ma richiede comunque un `emoji` non vuoto per la convalida dello strumento.

WhatsApp

  * `emoji` vuoto rimuove la reazione del bot.
  * `remove: true` viene mappato internamente a un emoji vuoto (richiede comunque `emoji` nella chiamata allo strumento).

Zalo Personal (zalouser)

  * Richiede `emoji` non vuoto.
  * `remove: true` rimuove quella specifica reazione emoji.

Feishu/Lark

  * Usa lo strumento `feishu_reaction` con le azioni `add`, `remove` e `list`.
  * Aggiunta/rimozione richiede `emoji_type`; la rimozione richiede anche `reaction_id`.

Signal

  * Le notifiche delle reazioni in ingresso sono controllate da `channels.signal.reactionNotifications`: `"off"` le disabilita, `"own"` (predefinito) emette eventi quando gli utenti reagiscono ai messaggi del bot e `"all"` emette eventi per tutte le reazioni.

iMessage

  * Le reazioni in uscita sono tapback di iMessage (`love`, `like`, `dislike`, `laugh`, `emphasize` e `question`).
  * Le notifiche dei tapback in ingresso sono controllate da `channels.imessage.reactionNotifications`: `"off"` le disabilita, `"own"` (predefinito) emette eventi quando gli utenti reagiscono ai messaggi scritti dal bot e `"all"` emette eventi per tutti i tapback provenienti da mittenti autorizzati.


## Livello di reazione

La configurazione `reactionLevel` per canale controlla quanto ampiamente l'agente usa le reazioni. I valori sono in genere `off`, `ack`, `minimal` o `extensive`.

  * [Telegram reactionLevel](</it/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</it/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


Imposta `reactionLevel` sui singoli canali per regolare quanto attivamente l'agente reagisce ai messaggi su ogni piattaforma.

## Correlati

  * [Invio dell'agente](</it/tools/agent-send>) — lo strumento `message` che include `react`
  * [Canali](</it/channels>) — configurazione specifica per canale


Was this useful?YesNo
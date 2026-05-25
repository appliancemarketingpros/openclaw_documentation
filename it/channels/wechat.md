---
title: WeChat
source_url: https://docs.openclaw.ai/it/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw si collega a WeChat tramite il Plugin di canale esterno `@tencent-weixin/openclaw-weixin` di Tencent.

Stato: Plugin esterno. Le chat dirette e i media sono supportati. Le chat di gruppo non sono pubblicizzate dai metadati delle capability dell'attuale Plugin.

## Denominazione

  * **WeChat** è il nome rivolto agli utenti in questa documentazione.
  * **Weixin** è il nome usato dal pacchetto di Tencent e dall'id del Plugin.
  * `openclaw-weixin` è l'id del canale OpenClaw.
  * `@tencent-weixin/openclaw-weixin` è il pacchetto npm.


Usa `openclaw-weixin` nei comandi CLI e nei percorsi di configurazione.

## Come funziona

Il codice WeChat non risiede nel repository core di OpenClaw. OpenClaw fornisce il contratto generico del Plugin di canale, e il Plugin esterno fornisce il runtime specifico per WeChat:

  1. `openclaw plugins install` installa `@tencent-weixin/openclaw-weixin`.
  2. Il Gateway rileva il manifest del Plugin e carica l'entrypoint del Plugin.
  3. Il Plugin registra l'id di canale `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` avvia il login tramite QR.
  5. Il Plugin salva le credenziali dell'account nella directory di stato di OpenClaw.
  6. Quando il Gateway si avvia, il Plugin avvia il suo monitor Weixin per ogni account configurato.
  7. I messaggi WeChat in ingresso vengono normalizzati tramite il contratto di canale, instradati all'agente OpenClaw selezionato e inviati di nuovo tramite il percorso in uscita del Plugin.


Questa separazione è importante: il core di OpenClaw deve rimanere indipendente dal canale. Login WeChat, chiamate all'API Tencent iLink, caricamento/scaricamento dei media, token di contesto e monitoraggio degli account sono di competenza del Plugin esterno.

## Installazione

Installazione rapida:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Installazione manuale:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Riavvia il Gateway dopo l'installazione:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Login

Esegui il login tramite QR sulla stessa macchina su cui è in esecuzione il Gateway:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Scansiona il codice QR con WeChat sul telefono e conferma il login. Il Plugin salva il token dell'account localmente dopo una scansione riuscita.

Per aggiungere un altro account WeChat, esegui di nuovo lo stesso comando di login. Per più account, isola le sessioni di messaggio diretto per account, canale e mittente:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Controllo degli accessi

I messaggi diretti usano il normale modello di pairing e allowlist di OpenClaw per i Plugin di canale.

Approva i nuovi mittenti:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Per il modello completo di controllo degli accessi, consulta [Pairing](</it/channels/pairing>).

## Compatibilità

Il Plugin controlla la versione host di OpenClaw all'avvio.

Linea Plugin | Versione OpenClaw | tag npm  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Se il Plugin segnala che la tua versione di OpenClaw è troppo vecchia, aggiorna OpenClaw oppure installa la linea legacy del Plugin:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Processo sidecar

Il Plugin WeChat può eseguire attività helper accanto al Gateway mentre monitora l'API Tencent iLink. Nell'issue #68451, quel percorso helper ha esposto un bug nella pulizia generica dei Gateway obsoleti di OpenClaw: un processo figlio poteva tentare di pulire il processo Gateway padre, causando cicli di riavvio sotto process manager come systemd.

L'attuale pulizia all'avvio di OpenClaw esclude il processo corrente e i suoi antenati, quindi un helper di canale non deve terminare il Gateway che lo ha avviato. Questa correzione è generica; non è un percorso specifico per WeChat nel core.

## Risoluzione dei problemi

Controlla installazione e stato:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Se il canale risulta installato ma non si connette, conferma che il Plugin sia abilitato e riavvia:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Se il Gateway si riavvia ripetutamente dopo aver abilitato WeChat, aggiorna sia OpenClaw sia il Plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Se all'avvio viene segnalato che il pacchetto Plugin installato `requires compiled runtime output for TypeScript entry`, il pacchetto npm è stato pubblicato senza i file runtime JavaScript compilati necessari a OpenClaw. Aggiorna/reinstalla dopo che il publisher del Plugin ha distribuito un pacchetto corretto, oppure disabilita/disinstalla temporaneamente il Plugin.

Disabilitazione temporanea:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Documentazione correlata

  * Panoramica dei canali: [Canali chat](</it/channels>)
  * Pairing: [Pairing](</it/channels/pairing>)
  * Instradamento dei canali: [Instradamento dei canali](</it/channels/channel-routing>)
  * Architettura Plugin: [Architettura Plugin](</it/plugins/architecture>)
  * SDK dei Plugin di canale: [SDK dei Plugin di canale](</it/plugins/sdk-channel-plugins>)
  * Pacchetto esterno: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo
---
title: Zalo ClawBot
source_url: https://docs.openclaw.ai/it/channels/zaloclawbot
scraped_at: 2026-06-29
---

ChannelsRegional platforms

OpenClaw si connette a Zalo ClawBot tramite il Plugin esterno `@zalo-platforms/openclaw-zaloclawbot` elencato nel catalogo. L'accesso usa un codice QR di Zalo Mini App.

## Compatibilità

Versione Plugin | Versione OpenClaw | npm dist-tag | Stato  
---|---|---|---  
0.1.x | >=2026.4.10 | `latest` | Attivo / Beta  
  
## Prerequisiti

  * Node.js **> = 22**
  * [OpenClaw](<https://docs.openclaw.ai/install>) deve essere installato (CLI `openclaw` disponibile).
  * Un account Zalo su un dispositivo mobile per scansionare il codice QR di accesso.


## Installazione con onboard (consigliata)

Esegui la procedura guidata di configurazione iniziale di OpenClaw e scegli **Zalo ClawBot** dal menu dei canali:

bashCopy code
[code]
    openclaw onboard
[/code]

La procedura guidata installa il Plugin dal catalogo ufficiale (con integrità verificata), visualizza il QR di accesso direttamente nel terminale e completa il canale dopo che lo hai scansionato con l'app Zalo. Non sono necessari comandi aggiuntivi.

## Installazione manuale

Per aggiungere il canale a un Gateway già configurato, segui questi passaggi:

### 1\. Installa il Plugin

bashCopy code
[code]
    openclaw plugins install "@zalo-platforms/openclaw-zaloclawbot@0.1.4"
[/code]

Usa la versione esatta fissata mostrata sopra (corrisponde alla voce del catalogo ufficiale), così OpenClaw verifica il pacchetto rispetto all'hash di integrità del catalogo durante l'installazione.

### 2\. Abilita il Plugin nella configurazione

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-zaloclawbot.enabled true
[/code]

### 3\. Genera il codice QR ed effettua l'accesso

bashCopy code
[code]
    openclaw channels login --channel openclaw-zaloclawbot
[/code]

Scansiona il codice QR mostrato nel terminale usando l'app mobile Zalo, accetta i Termini di utilizzo dentro la Zalo Mini App e autorizza la sessione.

### 4\. Riavvia il Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

* * *

## Come funziona

A differenza del canale Zalo standard per sviluppatori, che richiede di registrare un tuo Zalo Official Account (OA) e incollare credenziali sviluppatore statiche, Zalo ClawBot opera come **assistente personale vincolato al proprietario** usando un'infrastruttura ufficiale condivisa:

  1. **Configurazione sicura:** Il codice QR rimanda a una Zalo Mini App sicura che associa un bot privato appena predisposto, sotto un OA ufficiale condiviso, direttamente al tuo Zalo User ID.
  2. **Privacy vincolata al proprietario:** Per progettazione, il bot è limitato a comunicare _solo_ con il suo proprietario. I messaggi provenienti da altri utenti vengono scartati a livello di piattaforma, rendendo la connessione privata e sicura.
  3. **Percorso API ufficiale:** Il Plugin usa le API di Zalo Bot Platform invece di automazioni del browser o della sessione web.


## Dietro le quinte

Il Plugin Zalo ClawBot comunica con le API Zalo tramite un ciclo persistente di messaggi in long-polling. Per mantenere un runtime pulito e leggero:

  * Le connessioni long-poll usano l'endpoint `getUpdates`.
  * I Webhook sono disabilitati per impostazione predefinita per le esecuzioni locali del Gateway desktop/terminale.
  * I messaggi vengono elaborati lato client e mappati direttamente al runtime del tuo agente locale.


Il Plugin esterno gestisce le credenziali del bot nella directory di stato di OpenClaw. Tratta tale directory come sensibile e includila nella stessa policy di controllo degli accessi e backup del resto dello stato di OpenClaw.

* * *

## Risoluzione dei problemi

  * **Timeout dell'accesso QR:** Il token di accesso (`zbsk`) scade dopo 5 minuti per motivi di sicurezza. Se il codice QR scade prima che tu lo scansioni, riesegui semplicemente il comando di accesso per generarne uno nuovo.
  * **Il Gateway non si carica:** Assicurati che la versione host di OpenClaw sia `2026.4.10` o superiore. Le versioni precedenti non supportano il registro di installazione dei Plugin npm esterni.


Was this useful?YesNo

Open issue
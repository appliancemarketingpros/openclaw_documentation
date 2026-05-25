---
title: Hostinger
source_url: https://docs.openclaw.ai/it/install/hostinger
scraped_at: 2026-05-25
---

Esegui un Gateway OpenClaw persistente su [Hostinger](<https://www.hostinger.com/openclaw>) tramite un deployment gestito **1-Click** o un'installazione su **VPS**.

## Prerequisiti

  * Account Hostinger ([registrazione](<https://www.hostinger.com/openclaw>))
  * Circa 5-10 minuti


## Opzione A: OpenClaw 1-Click

Il modo più rapido per iniziare. Hostinger gestisce infrastruttura, Docker e aggiornamenti automatici.

* ### Acquista e avvia

  1. Dalla [pagina OpenClaw di Hostinger](<https://www.hostinger.com/openclaw>), scegli un piano Managed OpenClaw e completa il checkout.


* ### Seleziona un canale di messaggistica

Scegli uno o più canali da connettere:

  * **WhatsApp** \-- scansiona il codice QR mostrato nella procedura guidata di configurazione.
  * **Telegram** \-- incolla il token del bot da [BotFather](<https://t.me/BotFather>).


* ### Completa l'installazione

Fai clic su **Finish** per distribuire l'istanza. Quando è pronta, accedi alla dashboard di OpenClaw da **OpenClaw Overview** in hPanel.

## Opzione B: OpenClaw su VPS

Più controllo sul tuo server. Hostinger distribuisce OpenClaw tramite Docker sul tuo VPS e tu lo gestisci tramite il **Docker Manager** in hPanel.

* ### Acquista un VPS

  1. Dalla [pagina OpenClaw di Hostinger](<https://www.hostinger.com/openclaw>), scegli un piano OpenClaw su VPS e completa il checkout.


* ### Configura OpenClaw

Una volta eseguito il provisioning del VPS, compila i campi di configurazione:

  * **Gateway token** \-- generato automaticamente; salvalo per un uso successivo.
  * **Numero WhatsApp** \-- il tuo numero con prefisso internazionale (facoltativo).
  * **Token del bot Telegram** \-- da [BotFather](<https://t.me/BotFather>) (facoltativo).
  * **Chiavi API** \-- necessarie solo se non hai selezionato crediti Ready-to-Use AI durante il checkout.


* ### Avvia OpenClaw

Fai clic su **Deploy**. Una volta in esecuzione, apri la dashboard di OpenClaw da hPanel facendo clic su **Open**.

Log, riavvii e aggiornamenti vengono gestiti direttamente dall'interfaccia Docker Manager in hPanel. Per aggiornare, premi **Update** in Docker Manager e verrà scaricata l'immagine più recente.

## Verifica la configurazione

Invia "Hi" al tuo assistente sul canale che hai connesso. OpenClaw risponderà e ti guiderà nelle preferenze iniziali.

## Risoluzione dei problemi

**La dashboard non si carica** \-- Attendi qualche minuto affinché il container completi il provisioning. Controlla i log di Docker Manager in hPanel.

**Il container Docker continua a riavviarsi** \-- Apri i log di Docker Manager e cerca errori di configurazione (token mancanti, chiavi API non valide).

**Il bot Telegram non risponde** \-- Invia il messaggio con il tuo codice di associazione direttamente da Telegram come messaggio all'interno della tua chat OpenClaw per completare la connessione.

## Passaggi successivi

  * [Canali](</it/channels>) \-- connetti Telegram, WhatsApp, Discord e altro
  * [Configurazione del Gateway](</it/gateway/configuration>) \-- tutte le opzioni di configurazione


## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Hosting VPS](</it/vps>)
  * [DigitalOcean](</it/install/digitalocean>)


Was this useful?YesNo
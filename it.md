---
title: OpenClaw
source_url: https://docs.openclaw.ai/it
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"ESFOLIARE! ESFOLIARE!"_ — Un'aragosta spaziale, probabilmente

**Gateway per qualsiasi sistema operativo per agenti IA su Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo e altro ancora.**

Invia un messaggio, ricevi una risposta dell'agente dalla tua tasca. Esegui un solo Gateway su canali integrati, Plugin di canale in bundle, WebChat e nodi mobili.

[**Inizia** Installa OpenClaw e avvia il Gateway in pochi minuti. ](</it/start/getting-started>) [**Esegui l'onboarding** Configurazione guidata con `openclaw onboard` e flussi di associazione. ](</it/start/wizard>) [**Apri la Control UI** Avvia la dashboard del browser per chat, configurazione e sessioni. ](</it/web/control-ui>)

## Che cos'è OpenClaw?

OpenClaw è un **gateway self-hosted** che collega le tue app di chat preferite e le superfici di canale — canali integrati più Plugin di canale in bundle o esterni come Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo e altro ancora — ad agenti di programmazione IA come Pi. Esegui un singolo processo Gateway sulla tua macchina (o su un server), e diventa il ponte tra le tue app di messaggistica e un assistente IA sempre disponibile.

**A chi è destinato?** A sviluppatori e utenti esperti che vogliono un assistente IA personale a cui inviare messaggi da ovunque, senza rinunciare al controllo dei propri dati o dipendere da un servizio ospitato.

**Cosa lo rende diverso?**

  * **Self-hosted** : funziona sul tuo hardware, secondo le tue regole
  * **Multicanale** : un Gateway serve contemporaneamente canali integrati più Plugin di canale in bundle o esterni
  * **Nativo per agenti** : creato per agenti di programmazione con uso di strumenti, sessioni, memoria e routing multi-agente
  * **Open source** : con licenza MIT, guidato dalla community


**Di cosa hai bisogno?** Node 24 (consigliato), oppure Node 22 LTS (`22.16+`) per compatibilità, una chiave API del provider scelto e 5 minuti. Per la migliore qualità e sicurezza, usa il modello di ultima generazione più potente disponibile.

## Come funziona
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Il Gateway è l'unica fonte di verità per sessioni, routing e connessioni dei canali.

## Funzionalità principali

[**Gateway multicanale** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat e altro ancora con un singolo processo Gateway. ](</it/channels>) [**Canali Plugin** I Plugin in bundle aggiungono Matrix, Nostr, Twitch, Zalo e altro ancora nelle normali versioni correnti. ](</it/tools/plugin>) [**Routing multi-agente** Sessioni isolate per agente, workspace o mittente. ](</it/concepts/multi-agent>) [**Supporto multimediale** Invia e ricevi immagini, audio e documenti. ](</it/nodes/images>) [**Web Control UI** Dashboard del browser per chat, configurazione, sessioni e nodi. ](</it/web/control-ui>) [**Nodi mobili** Associa nodi iOS e Android per flussi di lavoro con Canvas, fotocamera e voce. ](</it/nodes>)

## Avvio rapido

* ### Installa OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Esegui l'onboarding e installa il servizio

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chat

Apri la Control UI nel browser e invia un messaggio:

bashCopy code
[code]
    openclaw dashboard
[/code]

Oppure collega un canale ([Telegram](</it/channels/telegram>) è il più rapido) e chatta dal telefono.

Ti serve l'installazione completa e la configurazione per lo sviluppo? Vedi [Iniziare](</it/start/getting-started>).

## Dashboard

Apri la Control UI del browser dopo l'avvio del Gateway.

  * Impostazione locale predefinita: <http://127.0.0.1:18789/>
  * Accesso remoto: [Superfici web](</it/web>) e [Tailscale](</it/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Configurazione (facoltativa)

La configurazione si trova in `~/.openclaw/openclaw.json`.

  * Se **non fai nulla** , OpenClaw usa il binario Pi in bundle in modalità RPC con sessioni per mittente.
  * Se vuoi bloccarlo, inizia da `channels.whatsapp.allowFrom` e (per i gruppi) dalle regole di menzione.


Esempio:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Inizia da qui

[**Hub della documentazione** Tutta la documentazione e le guide, organizzate per caso d'uso. ](</it/start/hubs>) [**Configurazione** Impostazioni principali del Gateway, token e configurazione dei provider. ](</it/gateway/configuration>) [**Accesso remoto** Modelli di accesso SSH e tailnet. ](</it/gateway/remote>) [**Canali** Configurazione specifica per canale per Feishu, Microsoft Teams, WhatsApp, Telegram, Discord e altro ancora. ](</it/channels/telegram>) [**Nodi** Nodi iOS e Android con associazione, Canvas, fotocamera e azioni del dispositivo. ](</it/nodes>) [**Aiuto** Correzioni comuni e punto di partenza per la risoluzione dei problemi. ](</it/help>)

## Scopri di più

[**Elenco completo delle funzionalità** Funzionalità complete per canali, routing e contenuti multimediali. ](</it/concepts/features>) [**Routing multi-agente** Isolamento del workspace e sessioni per agente. ](</it/concepts/multi-agent>) [**Sicurezza** Token, allowlist e controlli di sicurezza. ](</it/gateway/security>) [**Risoluzione dei problemi** Diagnostica del Gateway ed errori comuni. ](</it/gateway/troubleshooting>) [**Informazioni e crediti** Origini del progetto, contributori e licenza. ](</it/reference/credits>)

Was this useful?YesNo
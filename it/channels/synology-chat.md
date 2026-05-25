---
title: Synology Chat
source_url: https://docs.openclaw.ai/it/channels/synology-chat
scraped_at: 2026-05-25
---

Stato: canale di messaggistica diretta del Plugin in bundle che usa Webhook di Synology Chat. Il Plugin accetta messaggi in ingresso dai Webhook in uscita di Synology Chat e invia risposte tramite un Webhook in ingresso di Synology Chat.

## Plugin in bundle

Synology Chat viene distribuito come Plugin in bundle nelle versioni correnti di OpenClaw, quindi le normali build pacchettizzate non richiedono un'installazione separata.

Se usi una build precedente o un'installazione personalizzata che esclude Synology Chat, installalo manualmente:

Installa da un checkout locale:

bashCopy code
[code]
    openclaw plugins install ./path/to/local/synology-chat-plugin
[/code]

Dettagli: [Plugins](</it/tools/plugin>)

## Configurazione rapida

  1. Assicurati che il Plugin Synology Chat sia disponibile. 
     * Le versioni pacchettizzate correnti di OpenClaw lo includono già.
     * Le installazioni precedenti/personalizzate possono aggiungerlo manualmente da un checkout del sorgente con il comando sopra.
     * `openclaw onboard` ora mostra Synology Chat nello stesso elenco di configurazione dei canali di `openclaw channels add`.
     * Configurazione non interattiva: `openclaw channels add --channel synology-chat --token <token> --url <incoming-webhook-url>`
  2. Nelle integrazioni di Synology Chat: 
     * Crea un Webhook in ingresso e copiane l'URL.
     * Crea un Webhook in uscita con il tuo token segreto.
  3. Punta l'URL del Webhook in uscita al tuo Gateway OpenClaw: 
     * `https://gateway-host/webhook/synology` per impostazione predefinita.
     * Oppure il tuo `channels.synology-chat.webhookPath` personalizzato.
  4. Completa la configurazione in OpenClaw. 
     * Guidata: `openclaw onboard`
     * Diretta: `openclaw channels add --channel synology-chat --token <token> --url <incoming-webhook-url>`
  5. Riavvia il Gateway e invia un messaggio diretto al bot Synology Chat.


Dettagli di autenticazione del Webhook:

  * OpenClaw accetta il token del Webhook in uscita da `body.token`, poi da `?token=...`, poi dagli header.
  * Forme di header accettate: 
    * `x-synology-token`
    * `x-webhook-token`
    * `x-openclaw-token`
    * `Authorization: Bearer <token>`
  * I token vuoti o mancanti falliscono in modo chiuso.


Configurazione minima:

json5Copy code
[code]
    {  channels: {    "synology-chat": {      enabled: true,      token: "synology-outgoing-token",      incomingUrl: "https://nas.example.com/webapi/entry.cgi?api=SYNO.Chat.External&method=incoming&version=2&token=...",      webhookPath: "/webhook/synology",      dmPolicy: "allowlist",      allowedUserIds: ["123456"],      rateLimitPerMinute: 30,      allowInsecureSsl: false,    },  },}
[/code]

## Variabili d'ambiente

Per l'account predefinito, puoi usare variabili d'ambiente:

  * `SYNOLOGY_CHAT_TOKEN`
  * `SYNOLOGY_CHAT_INCOMING_URL`
  * `SYNOLOGY_NAS_HOST`
  * `SYNOLOGY_ALLOWED_USER_IDS` (separati da virgole)
  * `SYNOLOGY_RATE_LIMIT`
  * `OPENCLAW_BOT_NAME`


I valori di configurazione sovrascrivono le variabili d'ambiente.

`SYNOLOGY_CHAT_INCOMING_URL` non può essere impostato da un file `.env` dell'area di lavoro; vedi [file `.env` dell'area di lavoro](</it/gateway/security>).

## Criterio DM e controllo degli accessi

  * `dmPolicy: "allowlist"` è l'impostazione predefinita consigliata.
  * `allowedUserIds` accetta un elenco (o una stringa separata da virgole) di ID utente Synology.
  * In modalità `allowlist`, un elenco `allowedUserIds` vuoto viene trattato come configurazione errata e la rotta del Webhook non si avvierà (usa `dmPolicy: "open"` con `allowedUserIds: ["*"]` per consentire tutto).
  * `dmPolicy: "open"` consente messaggi diretti pubblici solo quando `allowedUserIds` include `"*"`; con voci restrittive, solo gli utenti corrispondenti possono chattare.
  * `dmPolicy: "disabled"` blocca i messaggi diretti.
  * Il binding del destinatario della risposta resta basato per impostazione predefinita sul valore numerico stabile `user_id`. `channels.synology-chat.dangerouslyAllowNameMatching: true` è una modalità di compatibilità di emergenza che riabilita la ricerca tramite nome utente/nickname mutabili per la consegna delle risposte.
  * Le approvazioni di associazione funzionano con: 
    * `openclaw pairing list synology-chat`
    * `openclaw pairing approve synology-chat &lt;CODE&gt;`


## Consegna in uscita

Usa gli ID utente numerici di Synology Chat come destinazioni.

Esempi:

bashCopy code
[code]
    openclaw message send --channel synology-chat --target 123456 --text "Hello from OpenClaw"openclaw message send --channel synology-chat --target synology-chat:123456 --text "Hello again"openclaw message send --channel synology-chat --target synology:123456 --text "Short prefix"
[/code]

L'invio di media è supportato tramite consegna di file basata su URL. Gli URL dei file in uscita devono usare `http` o `https`, e le destinazioni di rete private o altrimenti bloccate vengono rifiutate prima che OpenClaw inoltri l'URL al Webhook del NAS.

## Account multipli

Sono supportati più account Synology Chat in `channels.synology-chat.accounts`. Ogni account può sovrascrivere token, URL in ingresso, percorso del Webhook, criterio DM e limiti. Le sessioni di messaggi diretti sono isolate per account e utente, quindi lo stesso valore numerico `user_id` su due account Synology diversi non condivide lo stato della trascrizione. Assegna a ogni account abilitato un `webhookPath` distinto. OpenClaw ora rifiuta i percorsi esatti duplicati e si rifiuta di avviare account denominati che ereditano soltanto un percorso Webhook condiviso nelle configurazioni multi-account. Se hai intenzionalmente bisogno dell'ereditarietà legacy per un account denominato, imposta `dangerouslyAllowInheritedWebhookPath: true` su quell'account o in `channels.synology-chat`, ma i percorsi esatti duplicati vengono comunque rifiutati in modo chiuso. Preferisci percorsi espliciti per account.

json5Copy code
[code]
    {  channels: {    "synology-chat": {      enabled: true,      accounts: {        default: {          token: "token-a",          incomingUrl: "https://nas-a.example.com/...token=...",        },        alerts: {          token: "token-b",          incomingUrl: "https://nas-b.example.com/...token=...",          webhookPath: "/webhook/synology-alerts",          dmPolicy: "allowlist",          allowedUserIds: ["987654"],        },      },    },  },}
[/code]

## Note di sicurezza

  * Mantieni segreto `token` e ruotalo se viene divulgato.
  * Mantieni `allowInsecureSsl: false` salvo che tu consideri esplicitamente attendibile un certificato NAS locale autofirmato.
  * Le richieste Webhook in ingresso sono verificate tramite token e soggette a limite di frequenza per mittente.
  * I controlli dei token non validi usano un confronto dei segreti a tempo costante e falliscono in modo chiuso.
  * Preferisci `dmPolicy: "allowlist"` per la produzione.
  * Mantieni `dangerouslyAllowNameMatching` disattivato salvo che tu abbia esplicitamente bisogno della consegna delle risposte legacy basata su nome utente.
  * Mantieni `dangerouslyAllowInheritedWebhookPath` disattivato salvo che tu accetti esplicitamente il rischio di routing con percorso condiviso in una configurazione multi-account.


## Risoluzione dei problemi

  * `Missing required fields (token, user_id, text)`: 
    * nel payload del Webhook in uscita manca uno dei campi obbligatori
    * se Synology invia il token negli header, assicurati che il Gateway/proxy conservi quegli header
  * `Invalid token`: 
    * il segreto del Webhook in uscita non corrisponde a `channels.synology-chat.token`
    * la richiesta sta raggiungendo l'account/percorso Webhook sbagliato
    * un reverse proxy ha rimosso l'header del token prima che la richiesta raggiungesse OpenClaw
  * `Rate limit exceeded`: 
    * troppi tentativi con token non valido dalla stessa origine possono bloccare temporaneamente quell'origine
    * i mittenti autenticati hanno anche un limite di frequenza dei messaggi separato per utente
  * `Allowlist is empty. Configure allowedUserIds or use dmPolicy=open with allowedUserIds=["*"].`: 
    * `dmPolicy="allowlist"` è abilitato ma non sono configurati utenti
  * `User not authorized`: 
    * il valore numerico `user_id` del mittente non è in `allowedUserIds`


## Correlati

  * [Panoramica dei canali](</it/channels>) — tutti i canali supportati
  * [Associazione](</it/channels/pairing>) — autenticazione DM e flusso di associazione
  * [Gruppi](</it/channels/groups>) — comportamento delle chat di gruppo e gating delle menzioni
  * [Routing dei canali](</it/channels/channel-routing>) — routing delle sessioni per i messaggi
  * [Sicurezza](</it/gateway/security>) — modello di accesso e hardening


Was this useful?YesNo
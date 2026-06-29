---
title: SMS
source_url: https://docs.openclaw.ai/it/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw può ricevere e inviare SMS tramite un numero di telefono Twilio o un Messaging Service. Il Gateway registra una route webhook in ingresso, convalida per impostazione predefinita le firme delle richieste Twilio e invia le risposte tramite l'API Messages di Twilio.

[**Pairing** La policy DM predefinita per SMS è l'abbinamento. ](</it/channels/pairing>) [**Gateway security** Esamina l'esposizione del webhook e i controlli di accesso dei mittenti. ](</it/gateway/security>) [**Channel troubleshooting** Diagnostica cross-channel e playbook di riparazione. ](</it/channels/troubleshooting>)

## Prima di iniziare

Ti servono:

  * Il Plugin SMS ufficiale installato con `openclaw plugins install @openclaw/sms`.
  * Un account Twilio con un numero di telefono abilitato agli SMS, oppure un Twilio Messaging Service.
  * Il Twilio Account SID e l'Auth Token.
  * Un URL HTTPS pubblico che raggiunga il tuo OpenClaw Gateway.
  * Una scelta di policy per i mittenti: `pairing` per uso privato, `allowlist` per numeri di telefono preapprovati, oppure `open` solo per accesso SMS intenzionalmente pubblico.


Usa un solo numero Twilio sia per SMS sia per le chiamate vocali se il numero dispone di entrambe le funzionalità. Configura separatamente in Twilio il webhook SMS e il webhook voce; questa pagina copre solo il webhook SMS.

## Configurazione rapida

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Create or choose a Twilio sender

In Twilio, apri **Phone Numbers > Manage > Active numbers** e scegli un numero abilitato agli SMS. Salva:

  * Account SID, per esempio `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Numero di telefono mittente, per esempio `+15551234567`


Se usi un Messaging Service invece di un numero mittente fisso, salva il Messaging Service SID, per esempio `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### Configure the SMS channel

Salva questo come `sms.patch.json5` e modifica i segnaposto:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Applicalo:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Point Twilio at the Gateway webhook

Nelle impostazioni del numero di telefono Twilio, apri **Messaging** e imposta **A message comes in** su:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

Usa HTTP `POST`. Il percorso locale predefinito è `/webhooks/sms`; modifica `channels.sms.webhookPath` se ti serve una route diversa.

* ### Expose the exact SMS webhook path

Il tuo URL pubblico deve instradare il percorso SMS al processo Gateway. Se usi Tailscale Funnel per test locali, esponi esplicitamente `/webhooks/sms`:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Le chiamate vocali e gli SMS usano percorsi webhook separati. Se lo stesso numero Twilio gestisce entrambi, mantieni entrambe le route configurate in Twilio e nel tuo tunnel.

* ### Start the Gateway and approve first sender

bashCopy code
[code]
    openclaw gateway
[/code]

Invia un SMS al numero Twilio. Il primo messaggio crea una richiesta di abbinamento. Approvata:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

I codici di abbinamento scadono dopo 1 ora.

## Esempi di configurazione

### File di configurazione

Usa la configurazione tramite file quando vuoi che la definizione del canale viaggi con la configurazione del Gateway:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Variabili d'ambiente

Usa la configurazione tramite variabili d'ambiente per distribuzioni con un solo account in cui i segreti provengono dall'ambiente host:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Poi abilita il canale nella configurazione:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM` è accettato come alias di `TWILIO_PHONE_NUMBER`. Usa `TWILIO_MESSAGING_SERVICE_SID` invece di un mittente con numero di telefono quando Twilio deve scegliere il mittente da un Messaging Service.

### Auth token SecretRef

`authToken` può essere un SecretRef. Usalo quando il Gateway deve risolvere il Twilio Auth Token dal runtime dei segreti di OpenClaw invece di archiviare la configurazione in chiaro:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

La variabile d'ambiente o il provider di segreti referenziato deve essere visibile al runtime del Gateway. Riavvia i processi Gateway gestiti dopo aver modificato le variabili d'ambiente dell'host.

### Numero privato solo allowlist

Usa `allowlist` quando solo numeri di telefono noti devono poter parlare con l'agente:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Mittente Messaging Service

Usa `messagingServiceSid` invece di `fromNumber` quando Twilio deve scegliere il mittente tramite un Messaging Service:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Se dopo la risoluzione di configurazione e variabili d'ambiente sono presenti sia `fromNumber` sia `messagingServiceSid`, viene usato `fromNumber`.

### Destinazione in uscita predefinita

Imposta `defaultTo` quando l'automazione o la consegna avviata dall'agente devono avere una destinazione predefinita se un flusso di invio omette una destinazione esplicita:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Controllo dell'accesso

`channels.sms.dmPolicy` controlla l'accesso diretto via SMS:

  * `pairing` (predefinito)
  * `allowlist` (richiede almeno un mittente in `allowFrom`)
  * `open` (richiede che `allowFrom` includa `"*"`)
  * `disabled`


Le voci `allowFrom` devono essere numeri di telefono E.164 come `+15551234567`. I prefissi `sms:` sono accettati e normalizzati. Per un assistente privato, preferisci `dmPolicy: "allowlist"` con numeri di telefono espliciti.

## Invio di SMS

Le destinazioni SMS in uscita usano il prefisso di servizio `sms:` con il canale SMS selezionato:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Quando la selezione del canale è implicita, `twilio-sms:+15551234567` seleziona questo canale senza acquisire il prefisso di servizio `sms:` già posseduto dal canale e usato da iMessage.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

La CLI richiede un `--target` esplicito. `defaultTo` è per i percorsi di automazione e consegna avviati dall'agente in cui la destinazione può essere risolta dalla configurazione del canale.

Le risposte dell'agente dalle conversazioni SMS in ingresso tornano automaticamente al mittente tramite il mittente Twilio configurato.

L'output SMS è testo semplice. OpenClaw rimuove il markdown, appiattisce i blocchi di codice recintati, conserva link leggibili e suddivide le risposte lunghe prima di inviarle tramite Twilio.

## Verifica della configurazione

Dopo l'avvio del Gateway:

  1. Conferma che il log del Gateway mostri la route del webhook SMS.
  2. Esegui una sonda lato Twilio:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Invia un SMS al numero Twilio dal tuo telefono.
  4. Esegui `openclaw pairing list sms`.
  5. Approva il codice di abbinamento con `openclaw pairing approve sms &lt;CODE&gt;`.
  6. Invia un altro SMS e conferma che l'agente risponda.


Per test solo in uscita, usa:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### Test end-to-end da macOS iMessage/SMS

Su un Mac che può inviare SMS dell'operatore tramite Messaggi, puoi usare `imsg` per pilotare il lato mittente senza toccare il telefono:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

Il primo messaggio dovrebbe creare una richiesta di abbinamento. Il secondo messaggio dovrebbe ricevere la risposta dell'agente tramite Twilio.

## Sicurezza del Webhook

Per impostazione predefinita, OpenClaw convalida `X-Twilio-Signature` usando `publicWebhookUrl` e `authToken`. Mantieni `publicWebhookUrl` allineato byte per byte con l'URL configurato in Twilio, inclusi schema, host, percorso e stringa di query.

Solo per test con tunnel locale, puoi impostare:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Non usare la convalida della firma disabilitata su un Gateway pubblico.

## Configurazione multi-account

Usa `accounts` quando gestisci più di un numero Twilio:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Ogni account dovrebbe usare un `webhookPath` distinto.

## Risoluzione dei problemi

### Twilio restituisce 403 oppure OpenClaw rifiuta il webhook

Controlla che `publicWebhookUrl` corrisponda esattamente all'URL configurato in Twilio, inclusi schema, host, percorso e stringa di query. Twilio firma la stringa dell'URL pubblico, quindi riscritture del proxy e nomi host alternativi possono interrompere la convalida della firma.

### Non compare alcuna richiesta di abbinamento

Controlla l'URL e il metodo del webhook **Messaging** del numero Twilio. Deve puntare all'URL del webhook SMS e usare `POST`. Conferma anche che il Gateway sia raggiungibile da Internet pubblico o tramite il tuo tunnel.

Se il log dei messaggi Twilio mostra l'errore `11200`, Twilio ha accettato l'SMS in ingresso ma non è riuscito a raggiungere il tuo webhook. Controlla:

  * Twilio **Messaging > A message comes in** punta a `publicWebhookUrl`.
  * Il metodo è `POST`.
  * Il tunnel o reverse proxy espone il `webhookPath` esatto; per Tailscale Funnel, esegui `tailscale funnel status` e conferma che `/webhooks/sms` sia elencato.
  * `publicWebhookUrl` usa lo stesso schema, host, percorso e stringa di query inviati da Twilio, così la convalida della firma può riprodurre l'URL firmato.


### Gli invii in uscita falliscono

Conferma che `accountSid`, `authToken` e `fromNumber` oppure `messagingServiceSid` siano risolti. Se usi un account Twilio di prova, potrebbe essere necessario verificare il numero di destinazione in Twilio prima di poter inviare SMS in uscita.

### I messaggi arrivano ma l'agente non risponde

Controlla `dmPolicy` e `allowFrom`. Con la policy `pairing` predefinita, il mittente deve essere approvato prima che vengano elaborati i normali turni dell'agente.

Was this useful?YesNo

Open issue
---
title: App Android
source_url: https://docs.openclaw.ai/it/platforms/android
scraped_at: 2026-05-25
---

## Riepilogo del supporto

  * Ruolo: app Node companion (Android non ospita il Gateway).
  * Gateway richiesto: sì (eseguilo su macOS, Linux o Windows tramite WSL2).
  * Installazione: [Per iniziare](</it/start/getting-started>) \+ [Abbinamento](</it/channels/pairing>).
  * Gateway: [Runbook](</it/gateway>) \+ [Configurazione](</it/gateway/configuration>). 
    * Protocolli: [protocollo Gateway](</it/gateway/protocol>) (Node + piano di controllo).


## Controllo di sistema

Il controllo di sistema (launchd/systemd) risiede sull'host del Gateway. Consulta [Gateway](</it/gateway>).

## Runbook di connessione

App Node Android ⇄ (mDNS/NSD + WebSocket) ⇄ **Gateway**

Android si connette direttamente al WebSocket del Gateway e usa l'abbinamento del dispositivo (`role: node`).

Per Tailscale o host pubblici, Android richiede un endpoint sicuro:

  * Preferito: Tailscale Serve / Funnel con `https://<magicdns>` / `wss://<magicdns>`
  * Supportato anche: qualsiasi altro URL Gateway `wss://` con un endpoint TLS reale
  * Il testo in chiaro `ws://` rimane supportato sugli indirizzi LAN privati / host `.local`, oltre a `localhost`, `127.0.0.1` e al bridge dell'emulatore Android (`10.0.2.2`)


### Prerequisiti

  * Puoi eseguire il Gateway sulla macchina "master".
  * Il dispositivo/emulatore Android può raggiungere il WebSocket del gateway: 
    * Stessa LAN con mDNS/NSD, **oppure**
    * Stessa tailnet Tailscale usando Wide-Area Bonjour / DNS-SD unicast (vedi sotto), **oppure**
    * Host/porta gateway manuali (fallback)
  * L'abbinamento mobile via tailnet/pubblico **non** usa endpoint IP tailnet grezzi `ws://`. Usa invece Tailscale Serve o un altro URL `wss://`.
  * Puoi eseguire la CLI (`openclaw`) sulla macchina gateway (o tramite SSH).


### 1) Avvia il Gateway

bashCopy code
[code]
    openclaw gateway --port 18789 --verbose
[/code]

Conferma che nei log compaia qualcosa di simile:

  * `listening on ws://0.0.0.0:18789`


Per l'accesso Android remoto tramite Tailscale, preferisci Serve/Funnel invece di un bind tailnet grezzo:

bashCopy code
[code]
    openclaw gateway --tailscale serve
[/code]

Questo fornisce ad Android un endpoint sicuro `wss://` / `https://`. Una semplice configurazione `gateway.bind: "tailnet"` non è sufficiente per il primo abbinamento Android remoto, a meno che tu non termini anche TLS separatamente.

### 2) Verifica la discovery (opzionale)

Dalla macchina gateway:

bashCopy code
[code]
    dns-sd -B _openclaw-gw._tcp local.
[/code]

Altre note di debug: [Bonjour](</it/gateway/bonjour>).

Se hai configurato anche un dominio di discovery wide-area, confrontalo con:

bashCopy code
[code]
    openclaw gateway discover --json
[/code]

Mostra `local.` più il dominio wide-area configurato in un unico passaggio e usa l'endpoint del servizio risolto invece dei soli suggerimenti TXT.

#### Discovery su tailnet (Vienna ⇄ Londra) tramite DNS-SD unicast

La discovery Android NSD/mDNS non attraversa le reti. Se il tuo Node Android e il gateway si trovano su reti diverse ma sono connessi tramite Tailscale, usa invece Wide-Area Bonjour / DNS-SD unicast.

La sola discovery non è sufficiente per l'abbinamento Android via tailnet/pubblico. La route rilevata ha comunque bisogno di un endpoint sicuro (`wss://` o Tailscale Serve):

  1. Configura una zona DNS-SD (esempio `openclaw.internal.`) sull'host gateway e pubblica i record `_openclaw-gw._tcp`.
  2. Configura lo split DNS di Tailscale per il dominio scelto, puntandolo a quel server DNS.


Dettagli e configurazione CoreDNS di esempio: [Bonjour](</it/gateway/bonjour>).

### 3) Connettiti da Android

Nell'app Android:

  * L'app mantiene attiva la connessione al gateway tramite un **servizio in primo piano** (notifica persistente).
  * Apri la scheda **Connetti**.
  * Usa la modalità **Codice di configurazione** o **Manuale**.
  * Se la discovery è bloccata, usa host/porta manuali nei **controlli avanzati**. Per gli host LAN privati, `ws://` funziona ancora. Per gli host Tailscale/pubblici, attiva TLS e usa un endpoint `wss://` / Tailscale Serve.


Dopo il primo abbinamento riuscito, Android si riconnette automaticamente all'avvio:

  * Endpoint manuale (se abilitato), altrimenti
  * L'ultimo gateway rilevato (best-effort).


### Beacon alive di presenza

Dopo che la sessione Node autenticata si connette, e quando l'app passa in background mentre il servizio in primo piano è ancora connesso, Android chiama `node.event` con `event: "node.presence.alive"`. Il gateway lo registra come `lastSeenAtMs`/`lastSeenReason` nei metadati del Node/dispositivo abbinato solo dopo che l'identità del dispositivo Node autenticato è nota.

L'app considera il beacon registrato con successo solo quando la risposta del gateway include `handled: true`. I gateway più vecchi possono confermare `node.event` con `{ "ok": true }`; quella risposta è compatibile ma non conta come aggiornamento last-seen durevole.

### 4) Approva l'abbinamento (CLI)

Sulla macchina gateway:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>openclaw devices reject <requestId>
[/code]

Dettagli sull'abbinamento: [Abbinamento](</it/channels/pairing>).

Opzionale: se il Node Android si connette sempre da una subnet strettamente controllata, puoi aderire all'approvazione automatica del primo abbinamento Node con CIDR espliciti o IP esatti:

json5Copy code
[code]
    {  gateway: {    nodes: {      pairing: {        autoApproveCidrs: ["192.168.1.0/24"],      },    },  },}
[/code]

Questa opzione è disabilitata per impostazione predefinita. Si applica solo al nuovo abbinamento `role: node` senza ambiti richiesti. L'abbinamento operatore/browser e qualsiasi modifica a ruolo, ambito, metadati o chiave pubblica richiede comunque l'approvazione manuale.

### 5) Verifica che il Node sia connesso

  * Tramite stato dei Node:

bashCopy code
[code]openclaw nodes status
[/code]

  * Tramite Gateway:

bashCopy code
[code]openclaw gateway call node.list --params "{}"
[/code]


### 6) Chat + cronologia

La scheda Chat Android supporta la selezione della sessione (predefinita `main`, più altre sessioni esistenti):

  * Cronologia: `chat.history` (normalizzata per la visualizzazione; i tag di direttiva inline vengono rimossi dal testo visibile, i payload XML delle chiamate agli strumenti in testo semplice (inclusi `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` e blocchi di chiamata agli strumenti troncati) e i token di controllo del modello trapelati in ASCII/a larghezza piena vengono rimossi, le righe assistant composte solo da token silenziosi come gli esatti `NO_REPLY` / `no_reply` vengono omesse e le righe sovradimensionate possono essere sostituite con segnaposto)
  * Invio: `chat.send`
  * Aggiornamenti push (best-effort): `chat.subscribe` → `event:"chat"`


### 7) Canvas + fotocamera

#### Host Canvas Gateway (consigliato per contenuti web)

Se vuoi che il Node mostri HTML/CSS/JS reale che l'agente può modificare su disco, punta il Node all'host canvas del Gateway.

  1. Crea `~/.openclaw/workspace/canvas/index.html` sull'host gateway.

  2. Naviga il Node verso di esso (LAN):


bashCopy code
[code]
    openclaw nodes invoke --node "&lt;Android Node&gt;" --command canvas.navigate --params '{"url":"http://<gateway-hostname>.local:18789/__openclaw__/canvas/"}'
[/code]

Tailnet (opzionale): se entrambi i dispositivi sono su Tailscale, usa un nome MagicDNS o un IP tailnet invece di `.local`, ad esempio `http://<gateway-magicdns>:18789/__openclaw__/canvas/`.

Questo server inietta un client live-reload in HTML e ricarica alle modifiche dei file. L'host A2UI risiede in `http://<gateway-host>:18789/__openclaw__/a2ui/`.

Comandi canvas (solo in primo piano):

  * `canvas.eval`, `canvas.snapshot`, `canvas.navigate` (usa `{"url":""}` o `{"url":"/"}` per tornare allo scaffold predefinito). `canvas.snapshot` restituisce `{ format, base64 }` (`format="jpeg"` per impostazione predefinita).
  * A2UI: `canvas.a2ui.push`, `canvas.a2ui.reset` (`canvas.a2ui.pushJSONL` alias legacy)


Comandi fotocamera (solo in primo piano; soggetti ad autorizzazione):

  * `camera.snap` (jpg)
  * `camera.clip` (mp4)


Consulta [Node fotocamera](</it/nodes/camera>) per parametri e helper CLI.

### 8) Voce + superficie comandi Android ampliata

  * Scheda Voce: Android ha due modalità di acquisizione esplicite. **Mic** è una sessione manuale della scheda Voce che invia ogni pausa come turno di chat e si arresta quando l'app lascia il primo piano o l'utente lascia la scheda Voce. **Talk** è la modalità Talk continua e continua ad ascoltare finché non viene disattivata o il Node si disconnette.
  * La modalità Talk promuove il servizio in primo piano esistente da `dataSync` a `dataSync|microphone` prima dell'inizio dell'acquisizione, poi lo declassa quando la modalità Talk si arresta. Android 14+ richiede la dichiarazione `FOREGROUND_SERVICE_MICROPHONE`, la concessione runtime `RECORD_AUDIO` e il tipo di servizio microfono a runtime.
  * Le risposte vocali usano `talk.speak` tramite il provider Talk del gateway configurato. La sintesi vocale di sistema locale viene usata solo quando `talk.speak` non è disponibile.
  * L'attivazione vocale rimane disabilitata nell'UX/runtime Android.
  * Famiglie di comandi Android aggiuntive (la disponibilità dipende da dispositivo + autorizzazioni): 
    * `device.status`, `device.info`, `device.permissions`, `device.health`
    * `notifications.list`, `notifications.actions` (vedi Inoltro notifiche sotto)
    * `photos.latest`
    * `contacts.search`, `contacts.add`
    * `calendar.events`, `calendar.add`
    * `callLog.search`
    * `sms.search`
    * `motion.activity`, `motion.pedometer`


## Entry point assistant

Android supporta l'avvio di OpenClaw dal trigger assistant di sistema (Google Assistant). Quando è configurato, tenendo premuto il pulsante Home o dicendo "Hey Google, ask OpenClaw..." si apre l'app e il prompt viene passato al compositore della chat.

Questo usa i metadati **App Actions** Android dichiarati nel manifest dell'app. Non è necessaria alcuna configurazione aggiuntiva lato gateway: l'intent dell'assistant è gestito interamente dall'app Android e inoltrato come normale messaggio di chat.

## Inoltro notifiche

Android può inoltrare le notifiche del dispositivo al gateway come eventi. Diversi controlli consentono di definire quali notifiche vengono inoltrate e quando.

Chiave | Tipo | Descrizione  
---|---|---  
`notifications.allowPackages` | string[] | Inoltra solo le notifiche da questi nomi di pacchetto. Se impostato, tutti gli altri pacchetti vengono ignorati.  
`notifications.denyPackages` | string[] | Non inoltrare mai le notifiche da questi nomi di pacchetto. Applicato dopo `allowPackages`.  
`notifications.quietHours.start` | string (HH:mm) | Inizio della finestra delle ore di silenzio (ora locale del dispositivo). Le notifiche vengono soppresse in questa finestra.  
`notifications.quietHours.end` | string (HH:mm) | Fine della finestra delle ore di silenzio.  
`notifications.rateLimit` | number | Numero massimo di notifiche inoltrate per pacchetto al minuto. Le notifiche in eccesso vengono scartate.  
  
Il selettore delle notifiche usa inoltre un comportamento più sicuro per gli eventi di notifica inoltrati, impedendo l'inoltro accidentale di notifiche di sistema sensibili.

Configurazione di esempio:

json5Copy code
[code]
    {  notifications: {    allowPackages: ["com.slack", "com.whatsapp"],    denyPackages: ["com.android.systemui"],    quietHours: {      start: "22:00",      end: "07:00",    },    rateLimit: 5,  },}
[/code]

## Correlati

  * [App iOS](</it/platforms/ios>)
  * [Node](</it/nodes>)
  * [Risoluzione dei problemi del Node Android](</it/nodes/troubleshooting>)


Was this useful?YesNo
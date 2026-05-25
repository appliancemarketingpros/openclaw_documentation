---
title: Twitch
source_url: https://docs.openclaw.ai/it/channels/twitch
scraped_at: 2026-05-25
---

Supporto alla chat di Twitch tramite connessione IRC. OpenClaw si connette come utente Twitch (account bot) per ricevere e inviare messaggi nei canali.

## Plugin incluso

Se usi una build precedente o un'installazione personalizzata che esclude Twitch, installa direttamente il pacchetto npm:

### registro npm

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Checkout locale

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Usa il pacchetto senza vincoli per seguire l'attuale tag di rilascio ufficiale. Fissa una versione esatta solo quando hai bisogno di un'installazione riproducibile.

Dettagli: [Plugins](</it/tools/plugin>)

## Configurazione rapida (principiante)

* ### Assicurati che il Plugin sia disponibile

Le versioni pacchettizzate correnti di OpenClaw lo includono già. Le installazioni precedenti/personalizzate possono aggiungerlo manualmente con i comandi sopra.

* ### Crea un account bot Twitch

Crea un account Twitch dedicato per il bot (oppure usa un account esistente).

* ### Genera le credenziali

Usa [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Seleziona **Bot Token**
  * Verifica che gli scope `chat:read` e `chat:write` siano selezionati
  * Copia **Client ID** e **Access Token**


* ### Trova il tuo ID utente Twitch

Usa <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> per convertire un nome utente in un ID utente Twitch.

* ### Configura il token

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (solo account predefinito)
  * Oppure configurazione: `channels.twitch.accessToken`


Se entrambi sono impostati, la configurazione ha la precedenza (il fallback env vale solo per l'account predefinito).

* ### Avvia il Gateway

Avvia il Gateway con il canale configurato.

Configurazione minima:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Che cos'è

  * Un canale Twitch posseduto dal Gateway.
  * Routing deterministico: le risposte tornano sempre a Twitch.
  * Ogni account viene mappato a una chiave di sessione isolata `agent:<agentId>:twitch:<accountName>`.
  * `username` è l'account del bot (chi si autentica), `channel` è la chat room a cui unirsi.


## Configurazione (dettagliata)

### Genera le credenziali

Usa [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Seleziona **Bot Token**
  * Verifica che gli scope `chat:read` e `chat:write` siano selezionati
  * Copia **Client ID** e **Access Token**


### Configura il bot

### Variabile env (solo account predefinito)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Configurazione

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Se sono impostati sia env sia configurazione, la configurazione ha la precedenza.

### Controllo degli accessi (consigliato)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Preferisci `allowFrom` per una allowlist rigida. Usa invece `allowedRoles` se vuoi un accesso basato sui ruoli.

**Ruoli disponibili:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Aggiornamento del token (opzionale)

I token di [Twitch Token Generator](<https://twitchtokengenerator.com/>) non possono essere aggiornati automaticamente: rigenerali quando scadono.

Per l'aggiornamento automatico del token, crea la tua applicazione Twitch in [Twitch Developer Console](<https://dev.twitch.tv/console>) e aggiungi alla configurazione:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Il bot aggiorna automaticamente i token prima della scadenza e registra gli eventi di aggiornamento.

## Supporto multi-account

Usa `channels.twitch.accounts` con token per account. Consulta [Configurazione](</it/gateway/configuration>) per il pattern condiviso.

Esempio (un account bot in due canali):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Controllo degli accessi

### Allowlist di ID utente (più sicura)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Basato sui ruoli

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` è una allowlist rigida. Quando è impostata, sono consentiti solo quegli ID utente. Se vuoi un accesso basato sui ruoli, lascia `allowFrom` non impostato e configura invece `allowedRoles`.

### Disabilita il requisito @mention

Per impostazione predefinita, `requireMention` è `true`. Per disabilitarlo e rispondere a tutti i messaggi:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Risoluzione dei problemi

Per prima cosa, esegui i comandi diagnostici:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Il bot non risponde ai messaggi

  * **Controlla il controllo degli accessi:** assicurati che il tuo ID utente sia in `allowFrom`, oppure rimuovi temporaneamente `allowFrom` e imposta `allowedRoles: ["all"]` per provare.
  * **Controlla che il bot sia nel canale:** il bot deve unirsi al canale specificato in `channel`.

Problemi con il token

Errori "Failed to connect" o di autenticazione:

  * Verifica che `accessToken` sia il valore del token di accesso OAuth (in genere inizia con il prefisso `oauth:`)
  * Controlla che il token abbia gli scope `chat:read` e `chat:write`
  * Se usi l'aggiornamento del token, verifica che `clientSecret` e `refreshToken` siano impostati

L'aggiornamento del token non funziona

Controlla nei log gli eventi di aggiornamento:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Se vedi "token refresh disabled (no refresh token)":

  * Assicurati che `clientSecret` sia fornito
  * Assicurati che `refreshToken` sia fornito


## Configurazione

### Configurazione dell'account

Nome utente del bot.

Token di accesso OAuth con `chat:read` e `chat:write`.

Twitch Client ID (da Token Generator o dalla tua app).

Canale a cui unirsi.

Abilita questo account.

Opzionale: per l'aggiornamento automatico del token.

Opzionale: per l'aggiornamento automatico del token.

Scadenza del token in secondi.

Timestamp di ottenimento del token.

Allowlist di ID utente.

Richiede @mention.

### Opzioni del provider

  * `channels.twitch.enabled` \- Abilita/disabilita l'avvio del canale
  * `channels.twitch.username` \- Nome utente del bot (configurazione semplificata per account singolo)
  * `channels.twitch.accessToken` \- Token di accesso OAuth (configurazione semplificata per account singolo)
  * `channels.twitch.clientId` \- Twitch Client ID (configurazione semplificata per account singolo)
  * `channels.twitch.channel` \- Canale a cui unirsi (configurazione semplificata per account singolo)
  * `channels.twitch.accounts.<accountName>` \- Configurazione multi-account (tutti i campi account sopra)


Esempio completo:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Azioni degli strumenti

L'agente può chiamare `twitch` con l'azione:

  * `send` \- Invia un messaggio a un canale


Esempio:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Sicurezza e operazioni

  * **Tratta i token come password** — Non committare mai token in git.
  * **Usa l'aggiornamento automatico del token** per bot a lunga esecuzione.
  * **Usa allowlist di ID utente** invece dei nomi utente per il controllo degli accessi.
  * **Monitora i log** per gli eventi di aggiornamento del token e lo stato della connessione.
  * **Limita al minimo gli scope dei token** — Richiedi solo `chat:read` e `chat:write`.
  * **Se sei bloccato** : riavvia il Gateway dopo aver confermato che nessun altro processo possieda la sessione.


## Limiti

  * **500 caratteri** per messaggio (suddivisi automaticamente ai confini delle parole).
  * Il Markdown viene rimosso prima della suddivisione.
  * Nessun rate limiting (usa i limiti di frequenza integrati di Twitch).


## Correlati

  * [Routing dei canali](</it/channels/channel-routing>) — routing di sessione per i messaggi
  * [Panoramica dei canali](</it/channels>) — tutti i canali supportati
  * [Gruppi](</it/channels/groups>) — comportamento delle chat di gruppo e gating delle mention
  * [Pairing](</it/channels/pairing>) — autenticazione DM e flusso di pairing
  * [Sicurezza](</it/gateway/security>) — modello di accesso e rafforzamento


Was this useful?YesNo
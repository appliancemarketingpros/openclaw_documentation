---
title: Nostr
source_url: https://docs.openclaw.ai/it/channels/nostr
scraped_at: 2026-05-25
---

**Stato:** Plugin in bundle opzionale (disabilitato per impostazione predefinita finché non viene configurato).

Nostr è un protocollo decentralizzato per i social network. Questo canale consente a OpenClaw di ricevere e rispondere ai messaggi diretti (DM) crittografati tramite NIP-04.

## Plugin in bundle

Le versioni attuali di OpenClaw distribuiscono Nostr come Plugin in bundle, quindi le normali build pacchettizzate non richiedono un'installazione separata.

### Installazioni precedenti/personalizzate

  * L'onboarding (`openclaw onboard`) e `openclaw channels add` mostrano ancora Nostr dal catalogo dei canali condiviso.
  * Se la tua build esclude Nostr in bundle, installa direttamente il pacchetto npm.

bashCopy code
[code]
    openclaw plugins install @openclaw/nostr
[/code]

Usa il pacchetto base per seguire l'attuale tag di rilascio ufficiale. Fissa una versione esatta solo quando hai bisogno di un'installazione riproducibile.

Usa un checkout locale (flussi di lavoro di sviluppo):

bashCopy code
[code]
    openclaw plugins install --link <path-to-local-nostr-plugin>
[/code]

Riavvia il Gateway dopo aver installato o abilitato i Plugin.

### Configurazione non interattiva

bashCopy code
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
[/code]

Usa `--use-env` per mantenere `NOSTR_PRIVATE_KEY` nell'ambiente invece di archiviare la chiave nella configurazione.

## Configurazione rapida

  1. Genera una coppia di chiavi Nostr (se necessario):

bashCopy code
[code]
    # Using naknak key generate
[/code]

  2. Aggiungi alla configurazione:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",    },  },}
[/code]

  3. Esporta la chiave:

bashCopy code
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
[/code]

  4. Riavvia il Gateway.


## Riferimento della configurazione

Chiave | Tipo | Predefinito | Descrizione  
---|---|---|---  
`privateKey` | string | obbligatorio | Chiave privata in formato `nsec` o esadecimale  
`relays` | string[] | `['wss://relay.damus.io', 'wss://nos.lol']` | URL dei relay (WebSocket)  
`dmPolicy` | string | `pairing` | Criterio di accesso ai DM  
`allowFrom` | string[] | `[]` | Pubkey dei mittenti consentiti  
`enabled` | boolean | `true` | Abilita/disabilita il canale  
`name` | string | - | Nome visualizzato  
`profile` | object | - | Metadati del profilo NIP-01  
  
## Metadati del profilo

I dati del profilo vengono pubblicati come evento NIP-01 `kind:0`. Puoi gestirli dalla Control UI (Channels -> Nostr -> Profile) o impostarli direttamente nella configurazione.

Esempio:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      profile: {        name: "openclaw",        displayName: "OpenClaw",        about: "Personal assistant DM bot",        picture: "https://example.com/avatar.png",        banner: "https://example.com/banner.png",        website: "https://example.com",        nip05: "openclaw@example.com",        lud16: "openclaw@example.com",      },    },  },}
[/code]

Note:

  * Gli URL del profilo devono usare `https://`.
  * L'importazione dai relay unisce i campi e conserva le sovrascritture locali.


## Controllo degli accessi

### Criteri DM

  * **pairing** (predefinito): i mittenti sconosciuti ricevono un codice di abbinamento.
  * **allowlist** : solo le pubkey in `allowFrom` possono inviare DM.
  * **open** : DM in ingresso pubblici (richiede `allowFrom: ["*"]`).
  * **disabled** : ignora i DM in ingresso.


Note sull'applicazione:

  * Le firme degli eventi in ingresso vengono verificate prima della policy del mittente e della decrittazione NIP-04, quindi gli eventi falsificati vengono rifiutati in anticipo.
  * Le risposte di pairing vengono inviate senza elaborare il corpo del DM originale.
  * I DM in ingresso sono soggetti a rate limit e i payload sovradimensionati vengono scartati prima della decrittazione.


### Esempio di allowlist

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      dmPolicy: "allowlist",      allowFrom: ["npub1abc...", "npub1xyz..."],    },  },}
[/code]

## Formati delle chiavi

Formati accettati:

  * **Chiave privata:** `nsec...` o esadecimale di 64 caratteri
  * **Chiavi pubbliche (`allowFrom`):** `npub...` o esadecimale


## Relay

Predefiniti: `relay.damus.io` e `nos.lol`.

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],    },  },}
[/code]

Suggerimenti:

  * Usa 2-3 relay per la ridondanza.
  * Evita troppi relay (latenza, duplicazione).
  * I relay a pagamento possono migliorare l'affidabilità.
  * I relay locali vanno bene per i test (`ws://localhost:7777`).


## Supporto del protocollo

NIP | Stato | Descrizione  
---|---|---  
NIP-01 | Supportato | Formato evento di base + metadati profilo  
NIP-04 | Supportato | DM crittografati (`kind:4`)  
NIP-17 | Pianificato | DM con gift-wrap  
NIP-44 | Pianificato | Crittografia versionata  
  
## Test

### Relay locale

bashCopy code
[code]
    # Start strfrydocker run -p 7777:7777 ghcr.io/hoytech/strfry
[/code]

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["ws://localhost:7777"],    },  },}
[/code]

### Test manuale

  1. Prendi nota della chiave pubblica del bot (npub) dai log.
  2. Apri un client Nostr (Damus, Amethyst, ecc.).
  3. Invia un DM alla chiave pubblica del bot.
  4. Verifica la risposta.


## Risoluzione dei problemi

### Messaggi non ricevuti

  * Verifica che la chiave privata sia valida.
  * Assicurati che gli URL dei relay siano raggiungibili e usino `wss://` (o `ws://` per locale).
  * Conferma che `enabled` non sia `false`.
  * Controlla nei log del Gateway la presenza di errori di connessione ai relay.


### Risposte non inviate

  * Controlla che il relay accetti le scritture.
  * Verifica la connettività in uscita.
  * Fai attenzione ai rate limit dei relay.


### Risposte duplicate

  * Previsto quando si usano più relay.
  * I messaggi vengono deduplicati per ID evento; solo la prima consegna attiva una risposta.


## Sicurezza

  * Non committare mai chiavi private.
  * Usa variabili d'ambiente per le chiavi.
  * Considera `allowlist` per i bot di produzione.
  * Le firme vengono verificate prima della policy del mittente, e la policy del mittente viene applicata prima della decrittazione, quindi gli eventi falsificati vengono rifiutati in anticipo e i mittenti sconosciuti non possono forzare il lavoro crittografico completo.


## Limitazioni (MVP)

  * Solo messaggi diretti (nessuna chat di gruppo).
  * Nessun allegato multimediale.
  * Solo NIP-04 (gift-wrap NIP-17 pianificato).


## Correlati

  * [Panoramica dei canali](</it/channels>) — tutti i canali supportati
  * [Pairing](</it/channels/pairing>) — autenticazione DM e flusso di pairing
  * [Gruppi](</it/channels/groups>) — comportamento delle chat di gruppo e gating delle menzioni
  * [Instradamento dei canali](</it/channels/channel-routing>) — instradamento delle sessioni per i messaggi
  * [Sicurezza](</it/gateway/security>) — modello di accesso e hardening


Was this useful?YesNo
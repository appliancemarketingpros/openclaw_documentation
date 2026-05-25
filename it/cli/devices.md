---
title: Dispositivi
source_url: https://docs.openclaw.ai/it/cli/devices
scraped_at: 2026-05-25
---

# `openclaw devices`

Gestisci le richieste di associazione dei dispositivi e i token con ambito dispositivo.

## Comandi

### `openclaw devices list`

Elenca le richieste di associazione in sospeso e i dispositivi associati.

CodeCopy code
[code]
    openclaw devices listopenclaw devices list --json
[/code]

L'output delle richieste in sospeso mostra l'accesso richiesto accanto all'accesso attualmente approvato del dispositivo quando il dispositivo è già associato. Questo rende espliciti gli upgrade di ambito/ruolo invece di farli sembrare una perdita dell'associazione.

### `openclaw devices remove <deviceId>`

Rimuove una voce di dispositivo associato.

Quando sei autenticato con un token di dispositivo associato, i chiamanti non amministratori possono rimuovere solo la voce del **proprio** dispositivo. La rimozione di un altro dispositivo richiede `operator.admin`.

CodeCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices remove <deviceId> --json
[/code]

### `openclaw devices clear --yes [--pending]`

Cancella in blocco i dispositivi associati.

CodeCopy code
[code]
    openclaw devices clear --yesopenclaw devices clear --yes --pendingopenclaw devices clear --yes --pending --json
[/code]

### `openclaw devices approve [requestId] [--latest]`

Approva una richiesta di associazione dispositivo in sospeso tramite `requestId` esatto. Se `requestId` viene omesso o viene passato `--latest`, OpenClaw stampa solo la richiesta in sospeso selezionata ed esce; riesegui l'approvazione con l'ID richiesta esatto dopo aver verificato i dettagli.

Se il dispositivo è già associato e richiede ambiti più ampi o un ruolo più ampio, OpenClaw mantiene l'approvazione esistente e crea una nuova richiesta di upgrade in sospeso. Esamina le colonne `Requested` e `Approved` in `openclaw devices list` oppure usa `openclaw devices approve --latest` per visualizzare l'anteprima dell'upgrade esatto prima di approvarlo.

Se il Gateway è configurato esplicitamente con `gateway.nodes.pairing.autoApproveCidrs`, le richieste iniziali `role: node` da IP client corrispondenti possono essere approvate prima di comparire in questo elenco. Questa policy è disabilitata per impostazione predefinita e non si applica mai ai client operatore/browser o alle richieste di upgrade.

CodeCopy code
[code]
    openclaw devices approveopenclaw devices approve <requestId>openclaw devices approve --latest
[/code]

### `openclaw devices reject <requestId>`

Rifiuta una richiesta di associazione dispositivo in sospeso.

CodeCopy code
[code]
    openclaw devices reject <requestId>
[/code]

### `openclaw devices rotate --device <id> --role <role> [--scope <scope...>]`

Ruota un token dispositivo per un ruolo specifico (aggiornando facoltativamente gli ambiti). Il ruolo di destinazione deve già esistere nel contratto di associazione approvato di quel dispositivo; la rotazione non può creare un nuovo ruolo non approvato. Se ometti `--scope`, le riconnessioni successive con il token ruotato memorizzato riutilizzano gli ambiti approvati memorizzati nella cache di quel token. Se passi valori `--scope` espliciti, questi diventano l'insieme di ambiti memorizzato per le future riconnessioni con token memorizzato nella cache. I chiamanti con dispositivo associato non amministratori possono ruotare solo il token del **proprio** dispositivo. L'insieme di ambiti del token di destinazione deve restare entro gli ambiti operatore della sessione del chiamante; la rotazione non può creare o preservare un token operatore più ampio di quello che il chiamante possiede già.

CodeCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator --scope operator.read --scope operator.write
[/code]

Restituisce i metadati di rotazione come JSON. Se il chiamante sta ruotando il proprio token mentre è autenticato con quel token dispositivo, la risposta include anche il token sostitutivo così il client può conservarlo prima di riconnettersi. Le rotazioni condivise/amministrative non restituiscono il bearer token.

### `openclaw devices revoke --device <id> --role <role>`

Revoca un token dispositivo per un ruolo specifico.

I chiamanti con dispositivo associato non amministratori possono revocare solo il token del **proprio** dispositivo. La revoca del token di un altro dispositivo richiede `operator.admin`. Anche l'insieme di ambiti del token di destinazione deve rientrare negli ambiti operatore della sessione del chiamante; i chiamanti solo con associazione non possono revocare token operatore admin/write.

CodeCopy code
[code]
    openclaw devices revoke --device <deviceId> --role node
[/code]

Restituisce il risultato della revoca come JSON.

## Opzioni comuni

  * `--url <url>`: URL WebSocket del Gateway (predefinito a `gateway.remote.url` quando configurato).
  * `--token <token>`: token del Gateway (se richiesto).
  * `--password <password>`: password del Gateway (autenticazione con password).
  * `--timeout <ms>`: timeout RPC.
  * `--json`: output JSON (consigliato per gli script).


## Note

  * La rotazione dei token restituisce un nuovo token (sensibile). Trattalo come un segreto.
  * Questi comandi richiedono l'ambito `operator.pairing` (o `operator.admin`). Alcune approvazioni richiedono anche che il chiamante possieda gli ambiti operatore che il dispositivo di destinazione creerebbe o erediterebbe; vedi [Ambiti operatore](</it/gateway/operator-scopes>).
  * `gateway.nodes.pairing.autoApproveCidrs` è una policy Gateway facoltativa solo per l'associazione di nuovi dispositivi node; non modifica l'autorità di approvazione della CLI.
  * La rotazione e la revoca dei token restano all'interno dell'insieme di ruoli di associazione approvato e della baseline degli ambiti approvati per quel dispositivo. Una voce token memorizzata nella cache fuori posto non concede una destinazione di gestione token.
  * Per le sessioni con token di dispositivo associato, la gestione tra dispositivi è riservata agli amministratori: `remove`, `rotate` e `revoke` sono limitati al proprio dispositivo a meno che il chiamante non abbia `operator.admin`.
  * Anche la mutazione dei token è contenuta nell'ambito del chiamante: una sessione solo di associazione non può ruotare o revocare un token che attualmente include `operator.admin` o `operator.write`.
  * `devices clear` è intenzionalmente protetto da `--yes`.
  * Se l'ambito di associazione non è disponibile su local loopback (e non viene passato alcun `--url` esplicito), list/approve può usare un fallback di associazione locale.
  * `devices approve` richiede un ID richiesta esplicito prima di creare token; omettere `requestId` o passare `--latest` mostra solo l'anteprima della richiesta in sospeso più recente.


## Checklist di ripristino dal disallineamento dei token

Usala quando la Control UI o altri client continuano a fallire con `AUTH_TOKEN_MISMATCH`, `AUTH_DEVICE_TOKEN_MISMATCH` o `AUTH_SCOPE_MISMATCH`.

  1. Conferma la sorgente corrente del token gateway:

bashCopy code
[code]
    openclaw config get gateway.auth.token
[/code]

  2. Elenca i dispositivi associati e identifica l'id del dispositivo interessato:

bashCopy code
[code]
    openclaw devices list
[/code]

  3. Ruota il token operatore per il dispositivo interessato:

bashCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator
[/code]

  4. Se la rotazione non basta, rimuovi l'associazione obsoleta e approva di nuovo:

bashCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices listopenclaw devices approve <requestId>
[/code]

  5. Ritenta la connessione del client con il token/password condiviso corrente.


Note:

  * La normale precedenza di autenticazione alla riconnessione è prima token/password condiviso esplicito, poi `deviceToken` esplicito, poi token dispositivo memorizzato, poi token di bootstrap.
  * Il ripristino attendibile da `AUTH_TOKEN_MISMATCH` può inviare temporaneamente insieme sia il token condiviso sia il token dispositivo memorizzato per un solo tentativo limitato.
  * `AUTH_SCOPE_MISMATCH` significa che il token dispositivo è stato riconosciuto ma non include l'insieme di ambiti richiesto; correggi il contratto di approvazione associazione/ambiti prima di modificare l'autenticazione gateway condivisa.


Correlati:

  * [Risoluzione dei problemi di autenticazione della dashboard](</it/web/dashboard#if-you-see-unauthorized-1008>)
  * [Risoluzione dei problemi del Gateway](</it/gateway/troubleshooting#dashboard-control-ui-connectivity>)


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Nodes](</it/nodes>)


Was this useful?YesNo
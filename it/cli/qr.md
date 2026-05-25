---
title: QR
source_url: https://docs.openclaw.ai/it/cli/qr
scraped_at: 2026-05-25
---

# `openclaw qr`

Genera un QR di abbinamento mobile e un codice di configurazione dalla configurazione corrente del Gateway.

## Utilizzo

bashCopy code
[code]
    openclaw qropenclaw qr --setup-code-onlyopenclaw qr --jsonopenclaw qr --remoteopenclaw qr --url wss://gateway.example/ws
[/code]

## Opzioni

  * `--remote`: preferisci `gateway.remote.url`; se non è impostato, `gateway.tailscale.mode=serve|funnel` può comunque fornire l'URL pubblico remoto
  * `--url <url>`: sostituisce l'URL del gateway usato nel payload
  * `--public-url <url>`: sostituisce l'URL pubblico usato nel payload
  * `--token <token>`: sostituisce il token del gateway rispetto al quale si autentica il flusso di bootstrap
  * `--password <password>`: sostituisce la password del gateway rispetto alla quale si autentica il flusso di bootstrap
  * `--setup-code-only`: stampa solo il codice di configurazione
  * `--no-ascii`: salta il rendering del QR ASCII
  * `--json`: emette JSON (`setupCode`, `gatewayUrl`, `auth`, `urlSource`)


## Note

  * `--token` e `--password` si escludono a vicenda.
  * Il codice di configurazione ora contiene un `bootstrapToken` opaco e di breve durata, non il token/password condiviso del gateway.
  * Nel flusso di bootstrap integrato del nodo/operatore, il token primario del nodo arriva comunque con `scopes: []`.
  * Se il passaggio di consegne del bootstrap emette anche un token operatore, resta limitato alla allowlist del bootstrap: `operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`.
  * I controlli degli ambiti del bootstrap sono prefissati dal ruolo. Quella allowlist dell'operatore soddisfa solo le richieste dell'operatore; i ruoli non operatore richiedono comunque ambiti sotto il proprio prefisso di ruolo.
  * L'abbinamento mobile fallisce in modo chiuso per gli URL del gateway `ws://` Tailscale/pubblici. Gli indirizzi LAN privati e gli host Bonjour `.local` restano supportati tramite `ws://`, ma le route mobili Tailscale/pubbliche dovrebbero usare Tailscale Serve/Funnel o un URL del gateway `wss://`.
  * Con `--remote`, OpenClaw richiede `gateway.remote.url` oppure `gateway.tailscale.mode=serve|funnel`.
  * Con `--remote`, se le credenziali remote effettivamente attive sono configurate come SecretRefs e non passi `--token` o `--password`, il comando le risolve dallo snapshot del gateway attivo. Se il gateway non è disponibile, il comando fallisce immediatamente.
  * Senza `--remote`, le SecretRefs di autenticazione del gateway locale vengono risolte quando non viene passato alcun override di autenticazione CLI: 
    * `gateway.auth.token` viene risolto quando l'autenticazione tramite token può prevalere (`gateway.auth.mode="token"` esplicito o modalità dedotta in cui nessuna sorgente password prevale).
    * `gateway.auth.password` viene risolto quando l'autenticazione tramite password può prevalere (`gateway.auth.mode="password"` esplicito o modalità dedotta senza un token prevalente da auth/env).
  * Se sono configurati sia `gateway.auth.token` sia `gateway.auth.password` (incluse le SecretRefs) e `gateway.auth.mode` non è impostato, la risoluzione del codice di configurazione fallisce finché la modalità non viene impostata esplicitamente.
  * Nota sul disallineamento di versione del Gateway: questo percorso di comando richiede un gateway che supporti `secrets.resolve`; i gateway meno recenti restituiscono un errore di metodo sconosciuto.
  * Dopo la scansione, approva l'abbinamento del dispositivo con: 
    * `openclaw devices list`
    * `openclaw devices approve <requestId>`


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Abbinamento](</it/cli/pairing>)


Was this useful?YesNo
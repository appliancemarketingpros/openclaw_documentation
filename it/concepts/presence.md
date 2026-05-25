---
title: Presenza
source_url: https://docs.openclaw.ai/it/concepts/presence
scraped_at: 2026-05-25
---

La "presenza" di OpenClaw è una vista leggera, best-effort, di:

  * il **Gateway** stesso, e
  * **i client connessi al Gateway** (app Mac, WebChat, CLI, ecc.)


La presenza viene usata principalmente per renderizzare la scheda **Istanze** dell'app macOS e per fornire visibilità rapida agli operatori.

## Campi di presenza (cosa viene mostrato)

Le voci di presenza sono oggetti strutturati con campi come:

  * `instanceId` (facoltativo ma fortemente consigliato): identità stabile del client (di solito `connect.client.instanceId`)
  * `host`: nome host leggibile
  * `ip`: indirizzo IP best-effort
  * `version`: stringa della versione del client
  * `deviceFamily` / `modelIdentifier`: suggerimenti sull'hardware
  * `mode`: `ui`, `webchat`, `cli`, `backend`, `probe`, `test`, `node`, ...
  * `lastInputSeconds`: "secondi dall'ultimo input dell'utente" (se noto)
  * `reason`: `self`, `connect`, `node-connected`, `periodic`, ...
  * `ts`: timestamp dell'ultimo aggiornamento (ms dall'epoch)


## Produttori (da dove proviene la presenza)

Le voci di presenza sono prodotte da più sorgenti e **unite**.

### 1) Voce self del Gateway

Il Gateway inizializza sempre una voce "self" all'avvio, così le UI mostrano l'host del Gateway anche prima che si connettano client.

### 2) Connessione WebSocket

Ogni client WS inizia con una richiesta `connect`. Dopo un handshake riuscito, il Gateway esegue l'upsert di una voce di presenza per quella connessione.

#### Perché i comandi CLI una tantum non vengono mostrati

La CLI spesso si connette per comandi brevi e una tantum. Per evitare di riempire di rumore l'elenco Istanze, `client.mode === "cli"` **non** viene trasformato in una voce di presenza.

### 3) Beacon `system-event`

I client possono inviare beacon periodici più ricchi tramite il metodo `system-event`. L'app Mac lo usa per segnalare nome host, IP e `lastInputSeconds`.

### 4) Connessioni Node (role: node)

Quando un node si connette tramite il WebSocket del Gateway con `role: node`, il Gateway esegue l'upsert di una voce di presenza per quel node (lo stesso flusso degli altri client WS).

## Regole di unione e deduplicazione (perché `instanceId` è importante)

Le voci di presenza sono memorizzate in una singola mappa in memoria:

  * Le voci sono indicizzate da una **chiave di presenza**.
  * La chiave migliore è un `instanceId` stabile (da `connect.client.instanceId`) che sopravvive ai riavvii.
  * Le chiavi non distinguono tra maiuscole e minuscole.


Se un client si riconnette senza un `instanceId` stabile, può comparire come riga **duplicata**.

## TTL e dimensione limitata

La presenza è intenzionalmente effimera:

  * **TTL:** le voci più vecchie di 5 minuti vengono eliminate
  * **Voci massime:** 200 (le più vecchie vengono rimosse per prime)


Questo mantiene l'elenco aggiornato ed evita una crescita illimitata della memoria.

## Avvertenza su remoto/tunnel (IP di loopback)

Quando un client si connette tramite un tunnel SSH o un inoltro di porta locale, il Gateway può vedere l'indirizzo remoto come `127.0.0.1`. Per evitare di sovrascrivere un IP valido segnalato dal client, gli indirizzi remoti di loopback vengono ignorati.

## Consumatori

### Scheda Istanze di macOS

L'app macOS renderizza l'output di `system-presence` e applica un piccolo indicatore di stato (Attivo/Inattivo/Obsoleto) in base all'età dell'ultimo aggiornamento.

## Suggerimenti per il debug

  * Per vedere l'elenco grezzo, chiama `system-presence` sul Gateway.
  * Se vedi duplicati: 
    * verifica che i client inviino un `client.instanceId` stabile nell'handshake
    * verifica che i beacon periodici usino lo stesso `instanceId`
    * controlla se nella voce derivata dalla connessione manca `instanceId` (in quel caso i duplicati sono previsti)


## Correlati

[**Indicatori di digitazione** Quando vengono inviati gli indicatori di digitazione e come configurarli. ](</it/concepts/typing-indicators>) [**Streaming e suddivisione in chunk** Streaming in uscita, suddivisione in chunk e formattazione per canale. ](</it/concepts/streaming>) [**Architettura del Gateway** Componenti del Gateway e protocollo WebSocket che guida gli aggiornamenti di presenza. ](</it/concepts/architecture>) [**Protocollo del Gateway** Il protocollo wire per `connect`, `system-event` e `system-presence`. ](</it/gateway/protocol>)

Was this useful?YesNo
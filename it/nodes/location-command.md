---
title: Comando di posizione
source_url: https://docs.openclaw.ai/it/nodes/location-command
scraped_at: 2026-05-25
---

## In breve

  * `location.get` è un comando del nodo (tramite `node.invoke`).
  * Disattivato per impostazione predefinita.
  * Le impostazioni dell'app Android usano un selettore: Disattivato / Durante l'uso.
  * Interruttore separato: Posizione precisa.


## Perché un selettore (non solo un interruttore)

Le autorizzazioni del sistema operativo hanno più livelli. Possiamo esporre un selettore nell'app, ma il sistema operativo decide comunque l'autorizzazione effettiva.

  * iOS/macOS possono mostrare **Durante l'uso** o **Sempre** nei prompt di sistema/nelle Impostazioni.
  * L'app Android attualmente supporta solo la posizione in primo piano.
  * La posizione precisa è un'autorizzazione separata (iOS 14+ "Precise", Android "fine" vs "coarse").


Il selettore nell'UI determina la modalità richiesta; l'autorizzazione effettiva risiede nelle impostazioni del sistema operativo.

## Modello delle impostazioni

Per dispositivo nodo:

  * `location.enabledMode`: `off | whileUsing`
  * `location.preciseEnabled`: bool


Comportamento dell'UI:

  * Selezionare `whileUsing` richiede l'autorizzazione in primo piano.
  * Se il sistema operativo nega il livello richiesto, ripristina il livello più alto concesso e mostra lo stato.


## Mappatura delle autorizzazioni (node.permissions)

Facoltativa. Il nodo macOS segnala `location` tramite la mappa delle autorizzazioni; iOS/Android possono ometterla.

## Comando: `location.get`

Chiamato tramite `node.invoke`.

Parametri (suggeriti):

jsonCopy code
[code]
    {  "timeoutMs": 10000,  "maxAgeMs": 15000,  "desiredAccuracy": "coarse|balanced|precise"}
[/code]

Payload di risposta:

jsonCopy code
[code]
    {  "lat": 48.20849,  "lon": 16.37208,  "accuracyMeters": 12.5,  "altitudeMeters": 182.0,  "speedMps": 0.0,  "headingDeg": 270.0,  "timestamp": "2026-01-03T12:34:56.000Z",  "isPrecise": true,  "source": "gps|wifi|cell|unknown"}
[/code]

Errori (codici stabili):

  * `LOCATION_DISABLED`: il selettore è disattivato.
  * `LOCATION_PERMISSION_REQUIRED`: autorizzazione mancante per la modalità richiesta.
  * `LOCATION_BACKGROUND_UNAVAILABLE`: l'app è in background ma è consentito solo Durante l'uso.
  * `LOCATION_TIMEOUT`: nessun fix in tempo.
  * `LOCATION_UNAVAILABLE`: errore di sistema / nessun provider.


## Comportamento in background

  * L'app Android nega `location.get` quando è in background.
  * Tieni OpenClaw aperto quando richiedi la posizione su Android.
  * Altre piattaforme nodo possono comportarsi diversamente.


## Integrazione con modello/strumenti

  * Superficie dello strumento: lo strumento `nodes` aggiunge l'azione `location_get` (nodo obbligatorio).
  * CLI: `openclaw nodes location get --node <id>`.
  * Linee guida per gli agenti: chiamare solo quando l'utente ha abilitato la posizione e comprende l'ambito.


## Testo UX (suggerito)

  * Disattivato: "La condivisione della posizione è disabilitata."
  * Durante l'uso: "Solo quando OpenClaw è aperto."
  * Precisa: "Usa la posizione GPS precisa. Disattiva l'opzione per condividere la posizione approssimativa."


## Correlati

  * [Analisi della posizione del canale](</it/channels/location>)
  * [Acquisizione fotocamera](</it/nodes/camera>)
  * [Modalità conversazione](</it/nodes/talk>)


Was this useful?YesNo
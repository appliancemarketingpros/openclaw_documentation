---
title: Risoluzione dei problemi di Node
source_url: https://docs.openclaw.ai/it/nodes/troubleshooting
scraped_at: 2026-05-25
---

Usa questa pagina quando un Node è visibile nello stato ma gli strumenti del Node non funzionano.

## Scala dei comandi

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

Poi esegui i controlli specifici del Node:

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>
[/code]

Segnali di integrità:

  * Il Node è connesso e associato per il ruolo `node`.
  * `nodes describe` include la capability che stai chiamando.
  * Le approvazioni exec mostrano la modalità/allowlist prevista.


## Requisiti in primo piano

`canvas.*`, `camera.*` e `screen.*` sono disponibili solo in primo piano sui Node iOS/Android.

Controllo e correzione rapidi:

bashCopy code
[code]
    openclaw nodes describe --node <idOrNameOrIp>openclaw nodes canvas snapshot --node <idOrNameOrIp>openclaw logs --follow
[/code]

Se vedi `NODE_BACKGROUND_UNAVAILABLE`, porta l'app del Node in primo piano e riprova.

## Matrice delle autorizzazioni

Capability | iOS | Android | app Node macOS | Codice di errore tipico  
---|---|---|---|---  
`camera.snap`, `camera.clip` | Fotocamera (+ microfono per l'audio della clip) | Fotocamera (+ microfono per l'audio della clip) | Fotocamera (+ microfono per l'audio della clip) | `*_PERMISSION_REQUIRED`  
`screen.record` | Registrazione schermo (+ microfono opzionale) | Prompt di acquisizione schermo (+ microfono opzionale) | Registrazione schermo | `*_PERMISSION_REQUIRED`  
`location.get` | Mentre usi l'app o Sempre (dipende dalla modalità) | Posizione in primo piano/sfondo in base alla modalità | Autorizzazione posizione | `LOCATION_PERMISSION_REQUIRED`  
`system.run` | n/d (percorso host del Node) | n/d (percorso host del Node) | Approvazioni exec richieste | `SYSTEM_RUN_DENIED`  
  
## Associazione rispetto ad approvazioni

Sono gate diversi:

  1. **Associazione dispositivo** : questo Node può connettersi al Gateway?
  2. **Policy dei comandi del Node nel Gateway** : l'ID comando RPC è consentito da `gateway.nodes.allowCommands` / `denyCommands` e dai default della piattaforma?
  3. **Approvazioni exec** : questo Node può eseguire localmente uno specifico comando shell?


Controlli rapidi:

bashCopy code
[code]
    openclaw devices listopenclaw nodes statusopenclaw approvals get --node <idOrNameOrIp>openclaw approvals allowlist add --node <idOrNameOrIp> "/usr/bin/uname"
[/code]

Se manca l'associazione, approva prima il dispositivo Node. Se in `nodes describe` manca un comando, controlla la policy dei comandi del Node nel Gateway e se il Node ha effettivamente dichiarato quel comando alla connessione. Se l'associazione è corretta ma `system.run` fallisce, correggi le approvazioni exec/allowlist su quel Node.

L'associazione del Node è un gate di identità/fiducia, non una superficie di approvazione per comando. Per `system.run`, la policy per Node risiede nel file delle approvazioni exec di quel Node (`openclaw approvals get --node ...`), non nel record di associazione del Gateway.

Per le esecuzioni `host=node` basate su approvazione, il Gateway vincola anche l'esecuzione al `systemRunPlan` canonico preparato. Se un chiamante successivo modifica comando/cwd o metadati della sessione prima che l'esecuzione approvata venga inoltrata, il Gateway rifiuta l'esecuzione come mancata corrispondenza dell'approvazione invece di fidarsi del payload modificato.

## Codici di errore comuni del Node

  * `NODE_BACKGROUND_UNAVAILABLE` → l'app è in background; portala in primo piano.
  * `CAMERA_DISABLED` → toggle della fotocamera disattivato nelle impostazioni del Node.
  * `*_PERMISSION_REQUIRED` → autorizzazione del sistema operativo mancante/negata.
  * `LOCATION_DISABLED` → la modalità posizione è disattivata.
  * `LOCATION_PERMISSION_REQUIRED` → la modalità posizione richiesta non è stata concessa.
  * `LOCATION_BACKGROUND_UNAVAILABLE` → l'app è in background ma è presente solo l'autorizzazione Mentre usi l'app.
  * `SYSTEM_RUN_DENIED: approval required` → la richiesta exec richiede approvazione esplicita.
  * `SYSTEM_RUN_DENIED: allowlist miss` → comando bloccato dalla modalità allowlist. Sugli host Node Windows, forme shell-wrapper come `cmd.exe /c ...` sono trattate come allowlist miss in modalità allowlist, a meno che non siano approvate tramite flusso di richiesta.


## Ciclo di ripristino rapido

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --follow
[/code]

Se sei ancora bloccato:

  * Riapprova l'associazione del dispositivo.
  * Riapri l'app del Node (in primo piano).
  * Concedi di nuovo le autorizzazioni del sistema operativo.
  * Ricrea/modifica la policy di approvazione exec.


## Correlati

  * [Panoramica dei Node](</it/nodes>)
  * [Node fotocamera](</it/nodes/camera>)
  * [Comando posizione](</it/nodes/location-command>)
  * [Approvazioni exec](</it/tools/exec-approvals>)
  * [Associazione Gateway](</it/gateway/pairing>)
  * [Risoluzione dei problemi del Gateway](</it/gateway/troubleshooting>)
  * [Risoluzione dei problemi dei canali](</it/channels/troubleshooting>)


Was this useful?YesNo
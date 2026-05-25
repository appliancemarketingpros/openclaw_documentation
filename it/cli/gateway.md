---
title: Gateway
source_url: https://docs.openclaw.ai/it/cli/gateway
scraped_at: 2026-05-25
---

Il Gateway è il server WebSocket di OpenClaw (canali, nodi, sessioni, hook). I sottocomandi in questa pagina sono sotto `openclaw gateway …`.

[**Rilevamento Bonjour** Configurazione mDNS locale + DNS-SD wide-area. ](</it/gateway/bonjour>) [**Panoramica del rilevamento** Come OpenClaw pubblicizza e trova i gateway. ](</it/gateway/discovery>) [**Configurazione** Chiavi di configurazione del gateway di livello superiore. ](</it/gateway/configuration>)

## Eseguire il Gateway

Esegui un processo Gateway locale:

bashCopy code
[code]
    openclaw gateway
[/code]

Alias in primo piano:

bashCopy code
[code]
    openclaw gateway run
[/code]

Comportamento all'avvio

  * Per impostazione predefinita, il Gateway rifiuta di avviarsi a meno che `gateway.mode=local` sia impostato in `~/.openclaw/openclaw.json`. Usa `--allow-unconfigured` per esecuzioni ad hoc/di sviluppo.
  * `openclaw onboard --mode local` e `openclaw setup` dovrebbero scrivere `gateway.mode=local`. Se il file esiste ma `gateway.mode` manca, considerala una configurazione danneggiata o sovrascritta e riparala invece di presupporre implicitamente la modalità locale.
  * Se il file esiste e `gateway.mode` manca, il Gateway tratta la situazione come un danno sospetto alla configurazione e rifiuta di "indovinare local" per te.
  * Il binding oltre il loopback senza autenticazione è bloccato (misura di sicurezza).
  * `SIGUSR1` attiva un riavvio nel processo quando autorizzato (`commands.restart` è abilitato per impostazione predefinita; imposta `commands.restart: false` per bloccare il riavvio manuale, mentre l'applicazione/aggiornamento tramite strumento/config del gateway rimane consentita).
  * I gestori `SIGINT`/`SIGTERM` arrestano il processo gateway, ma non ripristinano alcuno stato personalizzato del terminale. Se incapsuli la CLI con una TUI o input in raw mode, ripristina il terminale prima dell'uscita.


### Opzioni

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> Porta WebSocket (il valore predefinito proviene da config/env; di solito `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Override del token (imposta anche `OPENCLAW_GATEWAY_TOKEN` per il processo).

Reimposta la configurazione serve/funnel di Tailscale allo spegnimento.

Consenti l'avvio del gateway senza `gateway.mode=local` nella configurazione. Aggira la protezione di avvio solo per bootstrap ad hoc/di sviluppo; non scrive né ripara il file di configurazione.

Crea una configurazione di sviluppo + workspace se mancanti (salta [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).

Reimposta configurazione di sviluppo + credenziali + sessioni + workspace (richiede `--dev`).

Termina qualsiasi listener esistente sulla porta selezionata prima dell'avvio.

Log dettagliati.

Mostra nella console solo i log del backend CLI (e abilita stdout/stderr).

Alias per `--ws-log compact`.

Registra gli eventi del flusso raw del modello in jsonl.

## Riavviare il Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` chiede al Gateway in esecuzione di eseguire un preflight del lavoro OpenClaw attivo prima del riavvio. Se sono attive operazioni in coda, consegna delle risposte, esecuzioni incorporate o task run, il Gateway segnala i blocchi, accorpa le richieste duplicate di riavvio sicuro e riavvia quando il lavoro attivo si esaurisce. Il semplice `restart` mantiene il comportamento esistente del gestore del servizio per compatibilità. Usa `--force` solo quando vuoi esplicitamente il percorso di override immediato.

`openclaw gateway restart --safe --skip-deferral` esegue lo stesso riavvio coordinato e consapevole di OpenClaw di `--safe`, ma aggira il gate di rinvio del lavoro attivo, così il Gateway emette subito il riavvio anche quando vengono segnalati blocchi. Usalo come via di uscita per l'operatore quando un rinvio è stato bloccato da un task run incastrato e `--safe` da solo attenderebbe indefinitamente. `--skip-deferral` richiede `--safe`.

### Profilazione dell'avvio

  * Imposta `OPENCLAW_GATEWAY_STARTUP_TRACE=1` per registrare i tempi delle fasi durante l'avvio del Gateway, inclusi il ritardo `eventLoopMax` per fase e i tempi delle tabelle di lookup dei plugin per installed-index, registro dei manifest, pianificazione dell'avvio e lavoro owner-map.
  * Imposta `OPENCLAW_DIAGNOSTICS=timeline` con `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` per scrivere una timeline diagnostica di avvio JSONL best-effort per harness QA esterni. Puoi anche abilitare il flag con `diagnostics.flags: ["timeline"]` nella configurazione; il percorso è comunque fornito tramite env. Aggiungi `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` per includere campioni dell'event loop.
  * Esegui `pnpm test:startup:gateway -- --runs 5 --warmup 1` per misurare le prestazioni dell'avvio del Gateway. Il benchmark registra il primo output del processo, `/healthz`, `/readyz`, i tempi della traccia di avvio, il ritardo dell'event loop e i dettagli sui tempi delle tabelle di lookup dei plugin.


## Interrogare un Gateway in esecuzione

Tutti i comandi di query usano RPC WebSocket.

### Modalità di output

  * Predefinita: leggibile da persone (colorata in TTY).
  * `--json`: JSON leggibile da macchina (senza stile/spinner).
  * `--no-color` (o `NO_COLOR=1`): disabilita ANSI mantenendo il layout umano.


### Opzioni condivise

  * `--url <url>`: URL WebSocket del Gateway.
  * `--token <token>`: token del Gateway.
  * `--password <password>`: password del Gateway.
  * `--timeout <ms>`: timeout/budget (varia per comando).
  * `--expect-final`: attendi una risposta "final" (chiamate agente).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

L'endpoint HTTP `/healthz` è un probe di liveness: restituisce una risposta quando il server può rispondere via HTTP. L'endpoint HTTP `/readyz` è più rigoroso e resta rosso mentre sidecar dei plugin di avvio, canali o hook configurati si stanno ancora stabilizzando. Le risposte di readiness dettagliate locali o autenticate includono un blocco diagnostico `eventLoop` con ritardo dell'event loop, utilizzo dell'event loop, rapporto dei core CPU e un flag `degraded`.

### `gateway usage-cost`

Recupera riepiloghi usage-cost dai log delle sessioni.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

Recupera il recorder diagnostico di stabilità recente da un Gateway in esecuzione.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Numero massimo di eventi recenti da includere (max `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> Filtra per tipo di evento diagnostico, come `payload.large` o `diagnostic.memory.pressure`.

Leggi un bundle di stabilità persistito invece di chiamare il Gateway in esecuzione. Usa `--bundle latest` (o solo `--bundle`) per il bundle più recente nella directory di stato, oppure passa direttamente un percorso JSON del bundle.

Scrivi uno zip di diagnostica di supporto condivisibile invece di stampare i dettagli di stabilità.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> Percorso di output per `--export`.

Privacy e comportamento dei bundle

  * I record mantengono metadati operativi: nomi degli eventi, conteggi, dimensioni in byte, letture della memoria, stato di code/sessioni, nomi di canali/plugin e riepiloghi delle sessioni redatti. Non mantengono testo delle chat, corpi webhook, output degli strumenti, corpi raw di richiesta o risposta, token, cookie, valori segreti, nomi host o ID sessione raw. Imposta `diagnostics.enabled: false` per disabilitare completamente il recorder.
  * In caso di uscite fatali del Gateway, timeout di spegnimento e fallimenti di avvio del riavvio, OpenClaw scrive lo stesso snapshot diagnostico in `~/.openclaw/logs/stability/openclaw-stability-*.json` quando il recorder ha eventi. Ispeziona il bundle più recente con `openclaw gateway stability --bundle latest`; `--limit`, `--type` e `--since-seq` si applicano anche all'output del bundle.


### `gateway diagnostics export`

Scrive uno zip di diagnostica locale progettato per essere allegato alle segnalazioni di bug. Per il modello di privacy e i contenuti del bundle, vedi [Esportazione diagnostica](</it/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Salta la ricerca del bundle di stabilità persistito.

Stampa il percorso scritto, la dimensione e il manifest come JSON.

L'esportazione contiene un manifest, un riepilogo Markdown, la forma della configurazione, dettagli di configurazione sanitizzati, riepiloghi dei log sanitizzati, snapshot sanitizzati di stato/health del Gateway e il bundle di stabilità più recente quando esiste.

È pensata per essere condivisa. Mantiene dettagli operativi che aiutano il debug, come campi di log OpenClaw sicuri, nomi dei sottosistemi, codici di stato, durate, modalità configurate, porte, ID plugin, ID provider, impostazioni di funzionalità non segrete e messaggi di log operativi redatti. Omette o redige testo delle chat, corpi webhook, output degli strumenti, credenziali, cookie, identificatori di account/messaggio, testo di prompt/istruzioni, nomi host e valori segreti. Quando un messaggio in stile LogTape sembra testo di payload utente/chat/strumento, l'esportazione mantiene solo l'indicazione che un messaggio è stato omesso più il relativo conteggio di byte.

### `gateway status`

`gateway status` mostra il servizio Gateway (launchd/systemd/schtasks) più un probe facoltativo della capacità di connettività/autenticazione.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Salta il probe di connettività (vista solo servizio).

Analizza anche i servizi a livello di sistema.

Aggiorna il probe di connettività predefinito a un probe di lettura ed esce con codice diverso da zero quando quel probe di lettura fallisce. Non può essere combinato con `--no-probe`.

Semantica dello stato

  * `gateway status` resta disponibile per la diagnostica anche quando la configurazione della CLI locale è mancante o non valida.
  * `gateway status` predefinito verifica lo stato del servizio, la connessione WebSocket e la capacità di autenticazione visibile al momento dell'handshake. Non verifica operazioni di lettura/scrittura/amministrazione.
  * I probe diagnostici non apportano modifiche per l'autenticazione iniziale del dispositivo: riutilizzano un token dispositivo esistente nella cache quando presente, ma non creano una nuova identità dispositivo CLI o un record di abbinamento dispositivo in sola lettura solo per controllare lo stato.
  * `gateway status` risolve i SecretRef di autenticazione configurati per l'autenticazione del probe quando possibile.
  * Se un SecretRef di autenticazione richiesto non viene risolto in questo percorso di comando, `gateway status --json` segnala `rpc.authWarning` quando la connettività/autenticazione del probe fallisce; passa `--token`/`--password` esplicitamente o risolvi prima la sorgente del segreto.
  * Se il probe riesce, gli avvisi sugli auth-ref non risolti vengono soppressi per evitare falsi positivi.
  * Usa `--require-rpc` negli script e nell'automazione quando un servizio in ascolto non basta e hai bisogno che anche le chiamate RPC con ambito di lettura siano integre.
  * `--deep` aggiunge un'analisi best-effort per installazioni aggiuntive launchd/systemd/schtasks. Quando vengono rilevati più servizi simili a Gateway, l'output umano stampa suggerimenti di pulizia e avvisa che la maggior parte delle configurazioni dovrebbe eseguire un solo Gateway per macchina.
  * `--deep` segnala anche un recente passaggio di riavvio del supervisore Gateway quando il processo del servizio è uscito correttamente per un riavvio da parte di un supervisore esterno.
  * `--deep` esegue la convalida della configurazione in modalità consapevole dei Plugin (`pluginValidation: "full"`) ed espone gli avvisi dei manifest Plugin configurati (per esempio metadati di configurazione del canale mancanti), così i controlli smoke di installazione e aggiornamento li intercettano. `gateway status` predefinito mantiene il percorso rapido in sola lettura che salta la convalida dei Plugin.
  * L'output umano include il percorso del log su file risolto più l'istantanea dei percorsi/validità della configurazione CLI-vs-servizio per aiutare a diagnosticare la deriva di profilo o state-dir.

Controlli di deriva dell'autenticazione systemd Linux

  * Nelle installazioni systemd Linux, i controlli di deriva dell'autenticazione del servizio leggono sia i valori `Environment=` sia `EnvironmentFile=` dall'unità (inclusi `%h`, percorsi quotati, più file e file opzionali `-`).
  * I controlli di deriva risolvono i SecretRef `gateway.auth.token` usando l'env di runtime unito (prima l'env del comando del servizio, poi il fallback dell'env di processo).
  * Se l'autenticazione tramite token non è effettivamente attiva (`gateway.auth.mode` esplicito pari a `password`/`none`/`trusted-proxy`, oppure modalità non impostata dove la password può prevalere e nessun candidato token può prevalere), i controlli di deriva del token saltano la risoluzione del token di configurazione.


### `gateway probe`

`gateway probe` è il comando "debug di tutto". Esegue sempre il probe di:

  * il tuo Gateway remoto configurato (se impostato), e
  * localhost (loopback) **anche se il remoto è configurato**.


Se passi `--url`, quella destinazione esplicita viene aggiunta prima di entrambe. L'output umano etichetta le destinazioni come:

  * `URL (explicit)`
  * `Remote (configured)` o `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Interpretazione

  * `Reachable: yes` significa che almeno una destinazione ha accettato una connessione WebSocket.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` segnala ciò che il probe ha potuto verificare sull'autenticazione. È separato dalla raggiungibilità.
  * `Read probe: ok` significa che anche le chiamate RPC di dettaglio con ambito di lettura (`health`/`status`/`system-presence`/`config.get`) sono riuscite.
  * `Read probe: limited - missing scope: operator.read` significa che la connessione è riuscita, ma l'RPC con ambito di lettura è limitato. Questo viene segnalato come raggiungibilità **degradata** , non come fallimento completo.
  * `Read probe: failed` dopo `Connect: ok` significa che il Gateway ha accettato la connessione WebSocket, ma la diagnostica di lettura successiva è andata in timeout o è fallita. Anche questa è raggiungibilità **degradata** , non un Gateway non raggiungibile.
  * Come `gateway status`, il probe riutilizza l'autenticazione dispositivo esistente nella cache ma non crea un'identità dispositivo iniziale o uno stato di abbinamento.
  * Il codice di uscita è diverso da zero solo quando nessuna destinazione sottoposta a probe è raggiungibile.

Output JSON

Livello superiore:

  * `ok`: almeno una destinazione è raggiungibile.
  * `degraded`: almeno una destinazione ha accettato una connessione ma non ha completato la diagnostica RPC di dettaglio completa.
  * `capability`: migliore capacità vista tra le destinazioni raggiungibili (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` o `unknown`).
  * `primaryTargetId`: migliore destinazione da trattare come vincitore attivo in questo ordine: URL esplicito, tunnel SSH, remoto configurato, quindi local loopback.
  * `warnings[]`: record di avviso best-effort con `code`, `message` e `targetIds` opzionali.
  * `network`: suggerimenti di URL local loopback/tailnet derivati dalla configurazione corrente e dalla rete dell'host.
  * `discovery.timeoutMs` e `discovery.count`: il budget/numero di risultati di discovery effettivamente usato per questo passaggio di probe.


Per destinazione (`targets[].connect`):

  * `ok`: raggiungibilità dopo connessione + classificazione degradata.
  * `rpcOk`: successo RPC di dettaglio completo.
  * `scopeLimited`: RPC di dettaglio fallito a causa dell'ambito operatore mancante.


Per destinazione (`targets[].auth`):

  * `role`: ruolo di autenticazione segnalato in `hello-ok` quando disponibile.
  * `scopes`: ambiti concessi segnalati in `hello-ok` quando disponibili.
  * `capability`: classificazione della capacità di autenticazione esposta per quella destinazione.

Codici di avviso comuni

  * `ssh_tunnel_failed`: configurazione del tunnel SSH fallita; il comando è tornato ai probe diretti.
  * `multiple_gateways`: più di una destinazione era raggiungibile; è insolito a meno che tu non stia eseguendo intenzionalmente profili isolati, come un bot di soccorso.
  * `auth_secretref_unresolved`: un SecretRef di autenticazione configurato non poteva essere risolto per una destinazione fallita.
  * `probe_scope_limited`: connessione WebSocket riuscita, ma il probe di lettura era limitato dalla mancanza di `operator.read`.


#### Remoto via SSH (parità app Mac)

La modalità "Remote over SSH" dell'app macOS usa un port-forward locale in modo che il Gateway remoto (che potrebbe essere associato solo a loopback) diventi raggiungibile su `ws://127.0.0.1:<port>`.

Equivalente CLI:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` o `user@host:port` (la porta predefinita è `22`).

Sceglie il primo host Gateway rilevato come destinazione SSH dall'endpoint di discovery risolto (`local.` più il dominio wide-area configurato, se presente). I suggerimenti solo TXT vengono ignorati.

Configurazione (opzionale, usata come predefinita):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Helper RPC di basso livello.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

Principalmente per RPC in stile agent che trasmettono eventi intermedi prima di un payload finale.

Output JSON leggibile dalla macchina.

## Gestire il servizio Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Installare con un wrapper

Usa `--wrapper` quando il servizio gestito deve avviarsi tramite un altro eseguibile, per esempio uno shim di gestione dei segreti o un helper run-as. Il wrapper riceve gli argomenti normali del Gateway ed è responsabile di eseguire infine `openclaw` o Node con quegli argomenti.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Puoi impostare il wrapper anche tramite l'ambiente. `gateway install` convalida che il percorso sia un file eseguibile, scrive il wrapper in `ProgramArguments` del servizio e persiste `OPENCLAW_WRAPPER` nell'ambiente del servizio per successive reinstallazioni forzate, aggiornamenti e riparazioni tramite doctor.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Per rimuovere un wrapper persistito, svuota `OPENCLAW_WRAPPER` durante la reinstallazione:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Opzioni dei comandi

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Comportamento del ciclo di vita

  * Usa `gateway restart` per riavviare un servizio gestito. Non concatenare `gateway stop` e `gateway start` come sostituto del riavvio.
  * Su macOS, `gateway stop` usa `launchctl bootout` per impostazione predefinita, che rimuove il LaunchAgent dalla sessione di avvio corrente senza rendere persistente una disabilitazione — il ripristino automatico KeepAlive rimane attivo per arresti anomali futuri e `gateway start` lo riabilita in modo pulito senza un `launchctl enable` manuale. Passa `--disable` per sopprimere in modo persistente KeepAlive e RunAtLoad affinché il Gateway non si riavvii fino al successivo `gateway start` esplicito; usalo quando un arresto manuale deve sopravvivere a riavvii o riavvii del sistema.
  * `gateway restart --safe` chiede al Gateway in esecuzione di eseguire un controllo preliminare del lavoro OpenClaw attivo e di rinviare il riavvio finché la consegna delle risposte, le esecuzioni incorporate e le esecuzioni delle attività non si svuotano. `--safe` non può essere combinato con `--force` o `--wait`.
  * `gateway restart --wait 30s` sovrascrive il budget di svuotamento del riavvio configurato per quel riavvio. I numeri senza unità sono millisecondi; sono accettate unità come `s`, `m` e `h`. `--wait 0` attende indefinitamente.
  * `gateway restart --safe --skip-deferral` esegue il riavvio sicuro consapevole di OpenClaw ma aggira il gate di rinvio, quindi il Gateway emette immediatamente il riavvio anche quando vengono segnalati blocchi. Via d'uscita per l'operatore per rinvii di esecuzioni di attività bloccate; richiede `--safe`.
  * `gateway restart --force` salta lo svuotamento del lavoro attivo e riavvia immediatamente. Usalo quando un operatore ha già ispezionato i blocchi di attività elencati e vuole ripristinare subito il gateway.
  * I comandi del ciclo di vita accettano `--json` per lo scripting.

Auth e SecretRefs al momento dell'installazione

  * Quando l'autenticazione tramite token richiede un token e `gateway.auth.token` è gestito da SecretRef, `gateway install` verifica che il SecretRef sia risolvibile ma non persiste il token risolto nei metadati dell'ambiente del servizio.
  * Se l'autenticazione tramite token richiede un token e il SecretRef del token configurato non è risolto, l'installazione fallisce in modo chiuso invece di persistere testo normale di fallback.
  * Per l'autenticazione tramite password su `gateway run`, preferisci `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` o un `gateway.auth.password` supportato da SecretRef rispetto a `--password` inline.
  * In modalità di autenticazione inferita, `OPENCLAW_GATEWAY_PASSWORD` solo shell non allenta i requisiti del token di installazione; usa una configurazione durevole (`gateway.auth.password` o `env` di configurazione) quando installi un servizio gestito.
  * Se sono configurati sia `gateway.auth.token` sia `gateway.auth.password` e `gateway.auth.mode` non è impostato, l'installazione viene bloccata finché la modalità non viene impostata esplicitamente.


## Rilevare gateway (Bonjour)

`gateway discover` esegue la scansione dei beacon del Gateway (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): scegli un dominio (esempio: `openclaw.internal.`) e configura split DNS + un server DNS; vedi [Bonjour](</it/gateway/bonjour>).


Solo i gateway con rilevamento Bonjour abilitato (impostazione predefinita) pubblicizzano il beacon.

I record di rilevamento wide-area possono includere questi suggerimenti TXT:

  * `role` (suggerimento sul ruolo del gateway)
  * `transport` (suggerimento sul trasporto, ad esempio `gateway`)
  * `gatewayPort` (porta WebSocket, solitamente `18789`)
  * `sshPort` (solo modalità di rilevamento completa; i client impostano per impostazione predefinita i target SSH su `22` quando è assente)
  * `tailnetDns` (nome host MagicDNS, quando disponibile)
  * `gatewayTls` / `gatewayTlsSha256` (TLS abilitato + impronta digitale del certificato)
  * `cliPath` (solo modalità di rilevamento completa)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Output leggibile dalla macchina (disabilita anche stile/spinner).

Esempi:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Runbook del Gateway](</it/gateway>)


Was this useful?YesNo
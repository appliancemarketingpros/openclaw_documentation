---
title: Manuale operativo del Gateway
source_url: https://docs.openclaw.ai/it/gateway
scraped_at: 2026-05-25
---

Usa questa pagina per l'avvio del giorno 1 e le operazioni del giorno 2 del servizio Gateway.

[**Risoluzione approfondita dei problemi** Diagnostica basata sui sintomi con sequenze di comandi esatte e firme dei log. ](</it/gateway/troubleshooting>) [**Configurazione** Guida alla configurazione orientata alle attività + riferimento completo della configurazione. ](</it/gateway/configuration>) [**Gestione dei segreti** Contratto SecretRef, comportamento degli snapshot a runtime e operazioni di migrazione/ricaricamento. ](</it/gateway/secrets>) [**Contratto del piano dei segreti** Regole esatte di destinazione/percorso di `secrets apply` e comportamento dei profili di autenticazione solo tramite riferimento. ](</it/gateway/secrets-plan-contract>)

## Avvio locale in 5 minuti

* ### Avvia il Gateway

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### Verifica lo stato del servizio

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Baseline sana: `Runtime: running`, `Connectivity probe: ok` e `Capability: ...` che corrisponde a ciò che ti aspetti. Usa `openclaw gateway status --require-rpc` quando ti serve una prova RPC con ambito di lettura, non solo la raggiungibilità.

* ### Convalida la prontezza del canale

bashCopy code
[code]
    openclaw channels status --probe
[/code]

Con un gateway raggiungibile, questo esegue probe live dei canali per account e audit opzionali. Se il gateway non è raggiungibile, la CLI ripiega invece su riepiloghi dei canali basati solo sulla configurazione anziché sull'output dei probe live.

## Modello a runtime

  * Un processo sempre attivo per routing, piano di controllo e connessioni dei canali.
  * Un'unica porta multiplexata per: 
    * Controllo/RPC WebSocket
    * API HTTP compatibili con OpenAI (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * UI di controllo e hook
  * Modalità di binding predefinita: `loopback`.
  * L'autenticazione è richiesta per impostazione predefinita. Le configurazioni con segreto condiviso usano `gateway.auth.token` / `gateway.auth.password` (oppure `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`) e le configurazioni reverse proxy non loopback possono usare `gateway.auth.mode: "trusted-proxy"`.


## Endpoint compatibili con OpenAI

La superficie di compatibilità a maggiore leva di OpenClaw ora è:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Perché questo insieme è importante:

  * La maggior parte delle integrazioni Open WebUI, LobeChat e LibreChat interroga prima `/v1/models`.
  * Molte pipeline RAG e di memoria si aspettano `/v1/embeddings`.
  * I client agent-native preferiscono sempre più spesso `/v1/responses`.


Nota di pianificazione:

  * `/v1/models` è agent-first: restituisce `openclaw`, `openclaw/default` e `openclaw/<agentId>`.
  * `openclaw/default` è l'alias stabile che punta sempre all'agente predefinito configurato.
  * Usa `x-openclaw-model` quando vuoi sovrascrivere provider/modello del backend; altrimenti la normale configurazione di modello ed embedding dell'agente selezionato resta in controllo.


Tutti questi endpoint vengono eseguiti sulla porta principale del Gateway e usano lo stesso confine di autenticazione dell'operatore fidato del resto dell'API HTTP del Gateway.

### Precedenza di porta e binding

Impostazione | Ordine di risoluzione  
---|---  
Porta Gateway | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Modalità di binding | CLI/override → `gateway.bind` → `loopback`  
  
I servizi gateway installati registrano il `--port` risolto nei metadati del supervisore. Dopo aver modificato `gateway.port`, esegui `openclaw doctor --fix` oppure `openclaw gateway install --force` in modo che launchd/systemd/schtasks avvii il processo sulla nuova porta.

L'avvio del Gateway usa la stessa porta e lo stesso binding effettivi quando inizializza le origini locali della UI di controllo per binding non loopback. Ad esempio, `--bind lan --port 3000` inizializza `http://localhost:3000` e `http://127.0.0.1:3000` prima che venga eseguita la convalida a runtime. Aggiungi esplicitamente qualsiasi origine di browser remoto, come URL proxy HTTPS, a `gateway.controlUi.allowedOrigins`.

### Modalità di hot reload

`gateway.reload.mode` | Comportamento  
---|---  
`off` | Nessun ricaricamento della configurazione  
`hot` | Applica solo modifiche hot-safe  
`restart` | Riavvia in caso di modifiche che richiedono ricaricamento  
`hybrid` (predefinito) | Applica a caldo quando sicuro, riavvia quando richiesto  
  
## Set di comandi dell'operatore

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` serve per ulteriore individuazione dei servizi (LaunchDaemons/unità systemd di sistema /schtasks), non per un probe di salute RPC più approfondito.

## Gateway multipli (stesso host)

La maggior parte delle installazioni dovrebbe eseguire un gateway per macchina. Un singolo gateway può ospitare più agenti e canali.

Servono più gateway solo quando vuoi intenzionalmente isolamento o un bot di ripristino.

Controlli utili:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

Cosa aspettarsi:

  * `gateway status --deep` può segnalare `Other gateway-like services detected (best effort)` e stampare suggerimenti di pulizia quando sono ancora presenti installazioni launchd/systemd/schtasks obsolete.
  * `gateway probe` può avvisare di `multiple reachable gateways` quando risponde più di un target.
  * Se è intenzionale, isola porte, configurazione/stato e radici workspace per ogni gateway.


Checklist per istanza:

  * `gateway.port` univoco
  * `OPENCLAW_CONFIG_PATH` univoco
  * `OPENCLAW_STATE_DIR` univoco
  * `agents.defaults.workspace` univoco


Esempio:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Configurazione dettagliata: [/gateway/multiple-gateways](</it/gateway/multiple-gateways>).

## Accesso remoto

Preferito: Tailscale/VPN. Fallback: tunnel SSH.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Poi connetti i client localmente a `ws://127.0.0.1:18789`.

Vedi: [Gateway remoto](</it/gateway/remote>), [Autenticazione](</it/gateway/authentication>), [Tailscale](</it/gateway/tailscale>).

## Supervisione e ciclo di vita del servizio

Usa esecuzioni supervisionate per un'affidabilità simile alla produzione.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Usa `openclaw gateway restart` per i riavvii. Non concatenare `openclaw gateway stop` e `openclaw gateway start` come sostituto del riavvio.

Su macOS, `gateway stop` usa `launchctl bootout` per impostazione predefinita: questo rimuove il LaunchAgent dalla sessione di avvio corrente senza rendere persistente una disabilitazione, quindi il recupero automatico KeepAlive continua a funzionare dopo arresti inattesi e `gateway start` riabilita in modo pulito. Per sopprimere in modo persistente il riavvio automatico tra i reboot, passa `--disable`: `openclaw gateway stop --disable`.

Le etichette LaunchAgent sono `ai.openclaw.gateway` (predefinito) oppure `ai.openclaw.<profile>` (profilo con nome). `openclaw doctor` verifica e ripara la deriva della configurazione del servizio.

### Linux (utente systemd)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Per la persistenza dopo il logout, abilita il lingering:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Esempio manuale di unità utente quando serve un percorso di installazione personalizzato:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (nativo)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

L'avvio gestito nativo di Windows usa un'attività pianificata chiamata `OpenClaw Gateway` (oppure `OpenClaw Gateway (<profile>)` per i profili con nome). Se la creazione dell'attività pianificata viene negata, OpenClaw ripiega su un launcher nella cartella Startup per utente che punta a `gateway.cmd` dentro la directory di stato.

### Linux (servizio di sistema)

Usa un'unità di sistema per host multiutente/sempre attivi.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Usa lo stesso corpo del servizio dell'unità utente, ma installalo sotto `/etc/systemd/system/openclaw-gateway[-<profile>].service` e modifica `ExecStart=` se il binario `openclaw` si trova altrove.

Non lasciare che anche `openclaw doctor --fix` installi un servizio gateway a livello utente per lo stesso profilo/porta. Doctor rifiuta quell'installazione automatica quando trova un servizio gateway OpenClaw a livello di sistema; usa `OPENCLAW_SERVICE_REPAIR_POLICY=external` quando l'unità di sistema possiede il ciclo di vita.

## Percorso rapido del profilo di sviluppo

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

I valori predefiniti includono stato/configurazione isolati e porta gateway di base `19001`.

## Riferimento rapido del protocollo (vista operatore)

  * Il primo frame del client deve essere `connect`.
  * Il Gateway restituisce lo snapshot `hello-ok` (`presence`, `health`, `stateVersion`, `uptimeMs`, limiti/policy).
  * `hello-ok.features.methods` / `events` sono un elenco di discovery conservativo, non un dump generato di ogni rotta helper chiamabile.
  * Richieste: `req(method, params)` → `res(ok/payload|error)`.
  * Gli eventi comuni includono `connect.challenge`, `agent`, `chat`, `session.message`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, eventi del ciclo di vita di pairing/approvazione e `shutdown`.


Le esecuzioni degli agenti sono in due fasi:

  1. Ack di accettazione immediato (`status:"accepted"`)
  2. Risposta finale di completamento (`status:"ok"|"error"`), con eventi `agent` in streaming nel mezzo.


Vedi la documentazione completa del protocollo: [Protocollo Gateway](</it/gateway/protocol>).

## Controlli operativi

### Liveness

  * Apri WS e invia `connect`.
  * Attendi una risposta `hello-ok` con snapshot.


### Readiness

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Recupero dei gap

Gli eventi non vengono riprodotti. In caso di gap di sequenza, aggiorna lo stato (`health`, `system-presence`) prima di continuare.

## Firme di errore comuni

Firma | Problema probabile  
---|---  
`refusing to bind gateway ... without auth` | Associazione non-loopback senza un percorso di autenticazione Gateway valido  
`another gateway instance is already listening` / `EADDRINUSE` | Conflitto di porta  
`Gateway start blocked: set gateway.mode=local` | Configurazione impostata in modalità remota, oppure il contrassegno della modalità locale manca da una configurazione danneggiata  
`unauthorized` durante la connessione | Mancata corrispondenza di autenticazione tra client e Gateway  
  
Per le scalette diagnostiche complete, usa [Risoluzione dei problemi del Gateway](</it/gateway/troubleshooting>).

## Garanzie di sicurezza

  * I client del protocollo Gateway falliscono rapidamente quando Gateway non è disponibile (nessun fallback implicito a canale diretto).
  * I primi frame non validi/non di connessione vengono rifiutati e chiusi.
  * L'arresto controllato emette l'evento `shutdown` prima della chiusura del socket.


* * *

Correlati:

  * [Risoluzione dei problemi](</it/gateway/troubleshooting>)
  * [Processo in background](</it/gateway/background-process>)
  * [Configurazione](</it/gateway/configuration>)
  * [Stato](</it/gateway/health>)
  * [Doctor](</it/gateway/doctor>)
  * [Autenticazione](</it/gateway/authentication>)


## Correlati

  * [Configurazione](</it/gateway/configuration>)
  * [Risoluzione dei problemi del Gateway](</it/gateway/troubleshooting>)
  * [Accesso remoto](</it/gateway/remote>)
  * [Gestione dei segreti](</it/gateway/secrets>)


Was this useful?YesNo
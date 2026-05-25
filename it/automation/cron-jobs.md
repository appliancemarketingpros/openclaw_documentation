---
title: Attività pianificate
source_url: https://docs.openclaw.ai/it/automation/cron-jobs
scraped_at: 2026-05-25
---

Cron è lo scheduler integrato del Gateway. Mantiene i job, risveglia l'agente al momento giusto e può restituire l'output a un canale chat o a un endpoint webhook.

## Avvio rapido

* ### Aggiungi un promemoria una tantum

bashCopy code
[code]
    openclaw cron add \  --name "Reminder" \  --at "2026-02-01T16:00:00Z" \  --session main \  --system-event "Reminder: check the cron docs draft" \  --wake now \  --delete-after-run
[/code]

* ### Controlla i tuoi job

bashCopy code
[code]
    openclaw cron listopenclaw cron get <job-id>openclaw cron show <job-id>
[/code]

* ### Vedi la cronologia delle esecuzioni

bashCopy code
[code]
    openclaw cron runs --id <job-id>
[/code]

## Come funziona cron

  * Cron viene eseguito **dentro il processo Gateway** (non dentro il modello).
  * Le definizioni dei job persistono in `~/.openclaw/cron/jobs.json`, quindi i riavvii non perdono le pianificazioni.
  * Lo stato di esecuzione runtime persiste accanto a esso in `~/.openclaw/cron/jobs-state.json`. Se tieni traccia delle definizioni cron in git, traccia `jobs.json` e aggiungi `jobs-state.json` a gitignore.
  * Dopo la separazione, le versioni precedenti di OpenClaw possono leggere `jobs.json` ma potrebbero trattare i job come nuovi perché i campi runtime ora risiedono in `jobs-state.json`.
  * Quando `jobs.json` viene modificato mentre il Gateway è in esecuzione o arrestato, OpenClaw confronta i campi di pianificazione modificati con i metadati degli slot runtime in sospeso e cancella i valori obsoleti di `nextRunAtMs`. Le riscritture di sola formattazione o solo ordine delle chiavi preservano lo slot in sospeso.
  * Tutte le esecuzioni cron creano record di [attività in background](</it/automation/tasks>).
  * All'avvio del Gateway, i job isolati di turno agente scaduti vengono ripianificati fuori dalla finestra di connessione del canale invece di essere riprodotti immediatamente, così l'avvio di Discord/Telegram e la configurazione dei comandi nativi restano reattivi dopo i riavvii.
  * I job una tantum (`--at`) vengono eliminati automaticamente dopo il successo per impostazione predefinita.
  * Le esecuzioni cron isolate chiudono con il massimo impegno le schede/processi browser tracciati per la loro sessione `cron:<jobId>` al completamento dell'esecuzione, così l'automazione browser scollegata non lascia processi orfani.
  * Le esecuzioni cron isolate che ricevono la concessione ristretta di autopulizia cron possono comunque leggere lo stato dello scheduler, un elenco autofilterato del loro job corrente e la cronologia delle esecuzioni di quel job, così i controlli di stato/heartbeat possono ispezionare la propria pianificazione senza ottenere un accesso più ampio alla mutazione cron.
  * Le esecuzioni cron isolate proteggono anche dalle risposte di conferma obsolete. Se il primo risultato è solo un aggiornamento di stato provvisorio (`on it`, `pulling everything together` e suggerimenti simili) e nessuna esecuzione di subagent discendente è ancora responsabile della risposta finale, OpenClaw richiede una volta il risultato effettivo prima della consegna.
  * Le esecuzioni cron isolate preferiscono i metadati strutturati di negazione dell'esecuzione provenienti dall'esecuzione incorporata, poi ripiegano su marcatori noti di riepilogo/output finale come `SYSTEM_RUN_DENIED` e `INVALID_REQUEST`, così un comando bloccato non viene segnalato come esecuzione riuscita.
  * Le esecuzioni cron isolate trattano anche gli errori dell'agente a livello di esecuzione come errori del job anche quando non viene prodotto alcun payload di risposta, così gli errori di modello/provider incrementano i contatori di errore e attivano notifiche di errore invece di contrassegnare il job come riuscito.
  * Quando un job isolato di turno agente raggiunge `timeoutSeconds`, cron interrompe l'esecuzione dell'agente sottostante e gli concede una breve finestra di pulizia. Se l'esecuzione non si svuota, la pulizia di proprietà del Gateway forza la rimozione della proprietà della sessione di quell'esecuzione prima che cron registri il timeout, così il lavoro chat in coda non resta bloccato dietro una sessione di elaborazione obsoleta.
  * Se un turno agente isolato si blocca prima dell'avvio del runner o prima della prima chiamata al modello, cron registra un timeout specifico della fase come `setup timed out before runner start` o `stalled before first model call (last phase: context-engine)`. Questi watchdog coprono provider incorporati e provider basati su CLI prima che il loro processo CLI esterno venga effettivamente avviato, e hanno limiti indipendenti dai valori lunghi di `timeoutSeconds` così gli errori di avvio a freddo/auth/contesto emergono rapidamente invece di attendere l'intero budget del job.


## Tipi di pianificazione

Tipo | Flag CLI | Descrizione  
---|---|---  
`at` | `--at` | Timestamp una tantum (ISO 8601 o relativo come `20m`)  
`every` | `--every` | Intervallo fisso  
`cron` | `--cron` | Espressione cron a 5 o 6 campi con `--tz` opzionale  
  
I timestamp senza fuso orario vengono trattati come UTC. Aggiungi `--tz America/New_York` per la pianificazione con orario locale.

Le espressioni ricorrenti a inizio ora vengono automaticamente scaglionate fino a 5 minuti per ridurre i picchi di carico. Usa `--exact` per forzare una temporizzazione precisa o `--stagger 30s` per una finestra esplicita.

### Giorno del mese e giorno della settimana usano logica OR

Le espressioni Cron vengono analizzate da [croner](<https://github.com/Hexagon/croner>). Quando sia il campo giorno del mese sia il campo giorno della settimana non sono wildcard, croner corrisponde quando **uno dei due** campi corrisponde, non entrambi. Questo è il comportamento standard di Vixie cron.

CodeCopy code
[code]
    # Intended: "9 AM on the 15th, only if it's a Monday"# Actual:   "9 AM on every 15th, AND 9 AM on every Monday"0 9 15 * 1
[/code]

Questo scatta circa 5-6 volte al mese invece di 0-1 volte al mese. OpenClaw usa qui il comportamento OR predefinito di Croner. Per richiedere entrambe le condizioni, usa il modificatore di giorno della settimana `+` di Croner (`0 9 15 * +1`) oppure pianifica su un campo e controlla l'altro nel prompt o comando del tuo job.

## Stili di esecuzione

Stile | Valore `--session` | Viene eseguito in | Ideale per  
---|---|---|---  
Sessione principale | `main` | Prossimo turno heartbeat | Promemoria, eventi di sistema  
Isolato | `isolated` | `cron:<jobId>` dedicato | Report, attività in background  
Sessione corrente | `current` | Associata al momento della creazione | Lavoro ricorrente consapevole del contesto  
Sessione personalizzata | `session:custom-id` | Sessione denominata persistente | Workflow che si basano sulla cronologia  
  
Sessione principale vs isolata vs personalizzata

I job della **sessione principale** mettono in coda un evento di sistema e, opzionalmente, risvegliano l'heartbeat (`--wake now` o `--wake next-heartbeat`). Questi eventi di sistema non estendono la freschezza del reset giornaliero/inattivo per la sessione di destinazione. I job **isolati** eseguono un turno agente dedicato con una sessione nuova. Le **sessioni personalizzate** (`session:xxx`) mantengono il contesto tra le esecuzioni, abilitando workflow come standup quotidiani che si basano sui riepiloghi precedenti.

Cosa significa 'sessione nuova' per i job isolati

Per i job isolati, "sessione nuova" significa un nuovo ID transcript/sessione per ogni esecuzione. OpenClaw può portare preferenze sicure come impostazioni di pensiero/veloce/verboso, etichette e override espliciti selezionati dall'utente per modello/auth, ma non eredita il contesto conversazionale ambientale da una riga cron precedente: routing canale/gruppo, criterio di invio o coda, elevazione, origine o binding runtime ACP. Usa `current` o `session:<id>` quando un job ricorrente deve deliberatamente basarsi sullo stesso contesto conversazionale.

Pulizia runtime

Per i job isolati, lo smontaggio runtime ora include la pulizia browser con il massimo impegno per quella sessione cron. Gli errori di pulizia vengono ignorati, così il risultato cron effettivo resta prevalente.

Le esecuzioni cron isolate eliminano anche tutte le istanze runtime MCP incluse create per il job tramite il percorso condiviso di pulizia runtime. Questo corrisponde al modo in cui i client MCP della sessione principale e della sessione personalizzata vengono smontati, così i job cron isolati non perdono processi figli stdio o connessioni MCP di lunga durata tra le esecuzioni.

Consegna di subagent e Discord

Quando le esecuzioni cron isolate orchestrano subagent, la consegna preferisce anche l'output finale del discendente rispetto al testo provvisorio obsoleto del genitore. Se i discendenti sono ancora in esecuzione, OpenClaw sopprime quell'aggiornamento parziale del genitore invece di annunciarlo.

Per le destinazioni di annuncio Discord solo testo, OpenClaw invia una sola volta il testo finale canonico dell'assistente invece di riprodurre sia i payload di testo in streaming/intermedi sia la risposta finale. I payload multimediali e strutturati di Discord vengono comunque consegnati come payload separati, così allegati e componenti non vengono scartati.

### Opzioni payload per job isolati

Testo del prompt (obbligatorio per isolati).

Override del modello; usa il modello consentito selezionato per il job.

Override del livello di pensiero.

Salta l'iniezione del file di bootstrap dell'area di lavoro.

Limita quali strumenti può usare il job, per esempio `--tools exec,read`.

`--model` usa il modello consentito selezionato come modello primario di quel job. Non è lo stesso di un override `/model` della sessione chat: le catene di fallback configurate si applicano comunque quando il primario del job fallisce. Se il modello richiesto non è consentito o non può essere risolto, cron fa fallire l'esecuzione con un errore di validazione esplicito invece di ripiegare silenziosamente sulla selezione agente/modello predefinita del job.

I job Cron possono anche contenere `fallbacks` a livello di payload. Quando presente, quell'elenco sostituisce la catena di fallback configurata per il job. Usa `fallbacks: []` nel payload/API del job quando vuoi un'esecuzione cron rigorosa che provi solo il modello selezionato. Se un job ha `--model` ma non ha fallback né di payload né configurati, OpenClaw passa un override di fallback vuoto esplicito così il primario dell'agente non viene aggiunto come destinazione di riprova extra nascosta.

La precedenza di selezione del modello per i job isolati è:

  1. Override del modello dell'hook Gmail (quando l'esecuzione proviene da Gmail e quell'override è consentito)
  2. `model` del payload per job
  3. Override del modello della sessione cron memorizzato selezionato dall'utente
  4. Selezione agente/modello predefinita


Anche la modalità veloce segue la selezione live risolta. Se la configurazione del modello selezionato ha `params.fastMode`, cron isolato la usa per impostazione predefinita. Un override `fastMode` della sessione memorizzata prevale comunque sulla configurazione in entrambe le direzioni.

Se un'esecuzione isolata incontra un passaggio live di cambio modello, cron riprova con il provider/modello cambiato e persiste quella selezione live per l'esecuzione attiva prima di riprovare. Quando il cambio porta anche un nuovo profilo auth, cron persiste anche quell'override del profilo auth per l'esecuzione attiva. I tentativi sono limitati: dopo il tentativo iniziale più 2 tentativi di cambio, cron interrompe invece di continuare all'infinito.

Prima che un'esecuzione Cron isolata entri nel runner dell'agente, OpenClaw controlla gli endpoint dei provider locali raggiungibili per i provider configurati `api: "ollama"` e `api: "openai-completions"` il cui `baseUrl` è loopback, rete privata o `.local`. Se quell'endpoint non è attivo, l'esecuzione viene registrata come `skipped` con un chiaro errore provider/modello invece di avviare una chiamata al modello. Il risultato dell'endpoint viene memorizzato nella cache per 5 minuti, quindi molti job scaduti che usano lo stesso server locale Ollama, vLLM, SGLang o LM Studio non funzionante condividono un piccolo probe invece di creare una tempesta di richieste. Le esecuzioni saltate dal preflight del provider non incrementano il backoff degli errori di esecuzione; abilita `failureAlert.includeSkipped` quando vuoi notifiche ripetute per i salti.

## Consegna e output

Modalità | Cosa succede  
---|---  
`announce` | Consegna di fallback del testo finale al target se l'agente non lo ha inviato  
`webhook` | POST del payload dell'evento completato a un URL  
`none` | Nessuna consegna di fallback del runner  
  
Usa `--announce --channel telegram --to "-1001234567890"` per la consegna al canale. Per gli argomenti dei forum Telegram, usa `-1001234567890:topic:123`; i chiamanti RPC/config diretti possono anche passare `delivery.threadId` come stringa o numero. I target Slack/Discord/Mattermost dovrebbero usare prefissi espliciti (`channel:<id>`, `user:<id>`). Gli ID delle stanze Matrix fanno distinzione tra maiuscole e minuscole; usa l'ID stanza esatto o la forma `room:!room:server` da Matrix.

Quando la consegna announce usa `channel: "last"` oppure omette `channel`, un target con prefisso provider come `telegram:123` può selezionare il canale prima che Cron ripieghi sulla cronologia della sessione o su un singolo canale configurato. Solo i prefissi dichiarati dal plugin caricato sono selettori di provider. Se `delivery.channel` è esplicito, il prefisso del target deve indicare lo stesso provider; per esempio, `channel: "whatsapp"` con `to: "telegram:123"` viene rifiutato invece di lasciare che WhatsApp interpreti l'ID Telegram come un numero di telefono. I prefissi di tipo target e servizio come `channel:<id>`, `user:<id>`, `imessage:<handle>` e `sms:<number>` restano sintassi target di proprietà del canale, non selettori di provider.

Per i job isolati, la consegna chat è condivisa. Se è disponibile una route chat, l'agente può usare lo strumento `message` anche quando il job usa `--no-deliver`. Se l'agente invia al target configurato/corrente, OpenClaw salta l'annuncio di fallback. Altrimenti `announce`, `webhook` e `none` controllano solo cosa fa il runner con la risposta finale dopo il turno dell'agente.

Quando un agente crea un promemoria isolato da una chat attiva, OpenClaw archivia il target di consegna live preservato per la route announce di fallback. Le chiavi di sessione interne possono essere minuscole; i target di consegna del provider non vengono ricostruiti da quelle chiavi quando il contesto chat corrente è disponibile.

La consegna announce implicita usa allowlist di canale configurate per convalidare e reinstradare target obsoleti. Le approvazioni DM del pairing store non sono destinatari dell'automazione di fallback; imposta `delivery.to` oppure configura la voce `allowFrom` del canale quando un job pianificato deve inviare proattivamente a un DM.

Le notifiche di errore seguono un percorso di destinazione separato:

  * `cron.failureDestination` imposta un valore predefinito globale per le notifiche di errore.
  * `job.delivery.failureDestination` lo sovrascrive per singolo job.
  * Se nessuno dei due è impostato e il job consegna già tramite `announce`, le notifiche di errore ora ripiegano su quel target announce primario.
  * `delivery.failureDestination` è supportato solo sui job `sessionTarget="isolated"`, a meno che la modalità di consegna primaria sia `webhook`.
  * `failureAlert.includeSkipped: true` abilita per un job o per la policy globale degli avvisi Cron gli avvisi ripetuti per le esecuzioni saltate. Le esecuzioni saltate mantengono un contatore consecutivo separato, quindi non influiscono sul backoff degli errori di esecuzione.


## Esempi CLI

### Promemoria una tantum

bashCopy code
[code]
    openclaw cron add \  --name "Calendar check" \  --at "20m" \  --session main \  --system-event "Next heartbeat: check calendar." \  --wake now
[/code]

### Job isolato ricorrente

bashCopy code
[code]
    openclaw cron add \  --name "Morning brief" \  --cron "0 7 * * *" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Summarize overnight updates." \  --announce \  --channel slack \  --to "channel:C1234567890"
[/code]

### Sovrascrittura di modello e ragionamento

bashCopy code
[code]
    openclaw cron add \  --name "Deep analysis" \  --cron "0 6 * * 1" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Weekly deep analysis of project progress." \  --model "opus" \  --thinking high \  --announce
[/code]

## Webhook

Gateway può esporre endpoint Webhook HTTP per trigger esterni. Abilita nella configurazione:

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",  },}
[/code]

### Autenticazione

Ogni richiesta deve includere il token dell'hook tramite header:

  * `Authorization: Bearer <token>` (consigliato)
  * `x-openclaw-token: <token>`


I token nella query string vengono rifiutati.

POST /hooks/wake

Accoda un evento di sistema per la sessione principale:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/wake \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"text":"New email received","mode":"now"}'
[/code]

Descrizione dell'evento.

`now` o `next-heartbeat`.

POST /hooks/agent

Esegue un turno agente isolato:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/agent \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"message":"Summarize inbox","name":"Email","model":"openai/gpt-5.4"}'
[/code]

Campi: `message` (obbligatorio), `name`, `agentId`, `wakeMode`, `deliver`, `channel`, `to`, `model`, `fallbacks`, `thinking`, `timeoutSeconds`.

OPENCLAW_DOCS_MARKER:accordionOpen:IHRpdGxlPSJIb29rIG1hcHBhdGkgKFBPU1QgL2hvb2tzLzxuYW1l )"> I nomi degli hook personalizzati vengono risolti tramite `hooks.mappings` nella configurazione. Le mappature possono trasformare payload arbitrari in azioni `wake` o `agent` con template o trasformazioni di codice.

## Integrazione Gmail PubSub

Collega i trigger della posta in arrivo Gmail a OpenClaw tramite Google PubSub.

### Configurazione guidata (consigliata)

bashCopy code
[code]
    openclaw webhooks gmail setup --account openclaw@gmail.com
[/code]

Questo scrive la configurazione `hooks.gmail`, abilita il preset Gmail e usa Tailscale Funnel per l'endpoint push.

### Avvio automatico del Gateway

Quando `hooks.enabled=true` e `hooks.gmail.account` è impostato, il Gateway avvia `gog gmail watch serve` al boot e rinnova automaticamente il watch. Imposta `OPENCLAW_SKIP_GMAIL_WATCHER=1` per disattivarlo.

### Configurazione manuale una tantum

* ### Seleziona il progetto GCP

Seleziona il progetto GCP proprietario del client OAuth usato da `gog`:

bashCopy code
[code]
    gcloud auth logingcloud config set project <project-id>gcloud services enable gmail.googleapis.com pubsub.googleapis.com
[/code]

* ### Crea il topic e concedi l'accesso push a Gmail

bashCopy code
[code]
    gcloud pubsub topics create gog-gmail-watchgcloud pubsub topics add-iam-policy-binding gog-gmail-watch \  --member=serviceAccount:gmail-api-push@system.gserviceaccount.com \  --role=roles/pubsub.publisher
[/code]

* ### Avvia il watch

bashCopy code
[code]
    gog gmail watch start \  --account openclaw@gmail.com \  --label INBOX \  --topic projects/<project-id>/topics/gog-gmail-watch
[/code]

### Sovrascrittura del modello Gmail

json5Copy code
[code]
    {  hooks: {    gmail: {      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",      thinking: "off",    },  },}
[/code]

## Gestione dei job

bashCopy code
[code]
    # List all jobsopenclaw cron list # Get one stored job as JSONopenclaw cron get <jobId> # Show one job, including resolved delivery routeopenclaw cron show <jobId> # Edit a jobopenclaw cron edit <jobId> --message "Updated prompt" --model "opus" # Force run a job nowopenclaw cron run <jobId> # Run only if dueopenclaw cron run <jobId> --due # View run historyopenclaw cron runs --id <jobId> --limit 50 # Delete a jobopenclaw cron remove <jobId> # Agent selection (multi-agent setups)openclaw cron add --name "Ops sweep" --cron "0 6 * * *" --session isolated --message "Check ops queue" --agent opsopenclaw cron edit <jobId> --clear-agent
[/code]

## Configurazione

json5Copy code
[code]
    {  cron: {    enabled: true,    store: "~/.openclaw/cron/jobs.json",    maxConcurrentRuns: 1,    retry: {      maxAttempts: 3,      backoffMs: [60000, 120000, 300000],      retryOn: ["rate_limit", "overloaded", "network", "server_error"],    },    webhookToken: "replace-with-dedicated-webhook-token",    sessionRetention: "24h",    runLog: { maxBytes: "2mb", keepLines: 2000 },  },}
[/code]

`maxConcurrentRuns` limita sia il dispatch Cron pianificato sia l'esecuzione dei turni agente isolati. I turni agente Cron isolati usano internamente la lane di esecuzione dedicata `cron-nested` della coda, quindi aumentare questo valore consente a esecuzioni LLM Cron indipendenti di avanzare in parallelo invece di avviare solo i rispettivi wrapper Cron esterni. La lane condivisa non-Cron `nested` non viene ampliata da questa impostazione.

Il sidecar di stato runtime è derivato da `cron.store`: uno store `.json` come `~/clawd/cron/jobs.json` usa `~/clawd/cron/jobs-state.json`, mentre un percorso store senza suffisso `.json` aggiunge `-state.json`.

Se modifichi manualmente `jobs.json`, lascia `jobs-state.json` fuori dal controllo versione. OpenClaw usa quel sidecar per slot in sospeso, marker attivi, metadati dell'ultima esecuzione e identità della pianificazione che indica allo scheduler quando un job modificato esternamente richiede un nuovo `nextRunAtMs`.

Disabilita Cron: `cron.enabled: false` o `OPENCLAW_SKIP_CRON=1`.

Comportamento di retry

**Retry una tantum** : gli errori transitori (limite di frequenza, sovraccarico, rete, errore server) vengono ritentati fino a 3 volte con backoff esponenziale. Gli errori permanenti disabilitano immediatamente.

**Retry ricorrente** : backoff esponenziale (da 30s a 60m) tra i retry. Il backoff viene reimpostato dopo la successiva esecuzione riuscita.

Manutenzione

`cron.sessionRetention` (predefinito `24h`) elimina le voci isolate delle sessioni di esecuzione. `cron.runLog.maxBytes` / `cron.runLog.keepLines` eliminano automaticamente i file dei log di esecuzione.

## Risoluzione dei problemi

### Sequenza di comandi

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw cron statusopenclaw cron listopenclaw cron runs --id <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --followopenclaw doctor
[/code]

Cron non si attiva

  * Controlla `cron.enabled` e la variabile d'ambiente `OPENCLAW_SKIP_CRON`.
  * Conferma che il Gateway sia in esecuzione in modo continuativo.
  * Per le pianificazioni `cron`, verifica il fuso orario (`--tz`) rispetto al fuso orario dell'host.
  * `reason: not-due` nell'output dell'esecuzione significa che l'esecuzione manuale è stata verificata con `openclaw cron run <jobId> --due` e che il job non era ancora dovuto.

Cron attivato ma nessuna consegna

  * La modalità di consegna `none` significa che non è previsto alcun invio di fallback del runner. L'agente può comunque inviare direttamente con lo strumento `message` quando è disponibile una route di chat.
  * Destinazione di consegna mancante/non valida (`channel`/`to`) significa che l'invio in uscita è stato saltato.
  * Per Matrix, i job copiati o legacy con ID stanza `delivery.to` in minuscolo possono non riuscire perché gli ID stanza Matrix distinguono tra maiuscole e minuscole. Modifica il job impostando il valore esatto `!room:server` o `room:!room:server` da Matrix.
  * Gli errori di autenticazione del canale (`unauthorized`, `Forbidden`) significano che la consegna è stata bloccata dalle credenziali.
  * Se l'esecuzione isolata restituisce solo il token silenzioso (`NO_REPLY` / `no_reply`), OpenClaw sopprime la consegna diretta in uscita e sopprime anche il percorso di riepilogo accodato di fallback, quindi non viene pubblicato nulla di nuovo nella chat.
  * Se l'agente deve inviare un messaggio all'utente autonomamente, controlla che il job abbia una route utilizzabile (`channel: "last"` con una chat precedente, oppure un canale/target esplicito).

Cron o Heartbeat sembrano impedire il rollover in stile /new

  * La freschezza del reset giornaliero e per inattività non si basa su `updatedAt`; consulta [Gestione delle sessioni](</it/concepts/session#session-lifecycle>).
  * Le riattivazioni di Cron, le esecuzioni di Heartbeat, le notifiche exec e la contabilità del Gateway possono aggiornare la riga della sessione per instradamento/stato, ma non estendono `sessionStartedAt` o `lastInteractionAt`.
  * Per le righe legacy create prima che quei campi esistessero, OpenClaw può recuperare `sessionStartedAt` dall'intestazione di sessione JSONL della trascrizione quando il file è ancora disponibile. Le righe legacy inattive senza `lastInteractionAt` usano quell'ora di inizio recuperata come riferimento di inattività.

Problemi comuni con i fusi orari

  * Cron senza `--tz` usa il fuso orario dell'host Gateway.
  * Le pianificazioni `at` senza fuso orario sono trattate come UTC.
  * `activeHours` di Heartbeat usa la risoluzione del fuso orario configurata.


## Correlati

  * [Automazione](</it/automation>) — tutti i meccanismi di automazione in sintesi
  * [Attività in background](</it/automation/tasks>) — registro delle attività per le esecuzioni Cron
  * [Heartbeat](</it/gateway/heartbeat>) — turni periodici della sessione principale
  * [Fuso orario](</it/concepts/timezone>) — configurazione del fuso orario


Was this useful?YesNo
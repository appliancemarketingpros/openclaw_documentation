---
title: Plugin Google Meet
source_url: https://docs.openclaw.ai/it/plugins/google-meet
scraped_at: 2026-05-25
---

Supporto dei partecipanti di Google Meet per OpenClaw: il plugin è esplicito per progettazione:

  * Si unisce solo a un URL esplicito `https://meet.google.com/...`.
  * Può creare un nuovo spazio Meet tramite l'API Google Meet, quindi unirsi all'URL restituito.
  * `agent` è la modalità talk-back predefinita: la trascrizione in tempo reale ascolta, l'agente OpenClaw configurato risponde e il normale TTS di OpenClaw parla in Meet.
  * `bidi` rimane disponibile come modalità di ripiego diretta del modello vocale in tempo reale.
  * Gli agenti scelgono il comportamento di accesso con `mode`: usa `agent` per ascolto/talk-back dal vivo, `bidi` per il fallback vocale diretto in tempo reale, oppure `transcribe` per unirsi/controllare il browser senza il bridge di talk-back.
  * L'autenticazione parte come OAuth Google personale o come profilo Chrome già connesso.
  * Non esiste alcun annuncio automatico di consenso.
  * Il backend audio predefinito di Chrome è `BlackHole 2ch`.
  * Chrome può essere eseguito localmente o su un host node associato.
  * Twilio accetta un numero di accesso telefonico più un PIN o una sequenza DTMF opzionale; non può chiamare direttamente un URL Meet.
  * Il comando CLI è `googlemeet`; `meet` è riservato a flussi di lavoro più ampi di teleconferenza degli agenti.


## Avvio rapido

Installa le dipendenze audio locali e configura un provider di trascrizione in tempo reale più il normale TTS di OpenClaw. OpenAI è il provider di trascrizione predefinito; anche Google Gemini Live funziona come fallback vocale `bidi` separato con `realtime.voiceProvider: "google"`:

bashCopy code
[code]
    brew install blackhole-2ch soxexport OPENAI_API_KEY=sk-...# only needed when realtime.voiceProvider is "google" for bidi modeexport GEMINI_API_KEY=...
[/code]

`blackhole-2ch` installa il dispositivo audio virtuale `BlackHole 2ch`. Il programma di installazione di Homebrew richiede un riavvio prima che macOS esponga il dispositivo:

bashCopy code
[code]
    sudo reboot
[/code]

Dopo il riavvio, verifica entrambi i componenti:

bashCopy code
[code]
    system_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Abilita il plugin:

json5Copy code
[code]
    {  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {},      },    },  },}
[/code]

Controlla la configurazione:

bashCopy code
[code]
    openclaw googlemeet setup
[/code]

L'output di setup è pensato per essere leggibile dagli agenti e consapevole della modalità. Riporta il profilo Chrome, il pinning del node e, per gli accessi Chrome in tempo reale, il bridge audio BlackHole/SoX e i controlli ritardati dell'introduzione in tempo reale. Per gli accessi in sola osservazione, controlla lo stesso trasporto con `--mode transcribe`; questa modalità salta i prerequisiti audio in tempo reale perché non ascolta né parla tramite il bridge:

bashCopy code
[code]
    openclaw googlemeet setup --transport chrome-node --mode transcribe
[/code]

Quando la delega Twilio è configurata, setup riporta anche se il plugin `voice-call`, le credenziali Twilio e l'esposizione pubblica del webhook sono pronti. Tratta qualsiasi controllo `ok: false` come un blocco per il trasporto e la modalità controllati prima di chiedere a un agente di unirsi. Usa `openclaw googlemeet setup --json` per script o output leggibile da macchina. Usa `--transport chrome`, `--transport chrome-node` o `--transport twilio` per eseguire il preflight di uno specifico trasporto prima che un agente lo provi.

Per Twilio, esegui sempre esplicitamente il preflight del trasporto quando il trasporto predefinito è Chrome:

bashCopy code
[code]
    openclaw googlemeet setup --transport twilio
[/code]

Questo intercetta cablaggio `voice-call` mancante, credenziali Twilio o esposizione webhook non raggiungibile prima che l'agente provi a chiamare la riunione.

Unisciti a una riunione:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij
[/code]

Oppure lascia che un agente si unisca tramite lo strumento `google_meet`:

jsonCopy code
[code]
    {  "action": "join",  "url": "https://meet.google.com/abc-defg-hij",  "transport": "chrome-node",  "mode": "agent"}
[/code]

Lo strumento `google_meet` rivolto agli agenti rimane disponibile su host non macOS per flussi di artefatti, calendario, setup, trascrizione, Twilio e `chrome-node`. Le azioni locali di talk-back Chrome sono bloccate lì perché il percorso audio Chrome incluso attualmente dipende da `BlackHole 2ch` di macOS. Su Linux, usa `mode: "transcribe"`, l'accesso telefonico Twilio o un host `chrome-node` macOS per la partecipazione talk-back con Chrome.

Crea una nuova riunione e unisciti:

bashCopy code
[code]
    openclaw googlemeet create --transport chrome-node --mode agent
[/code]

Per stanze create tramite API, usa `SpaceConfig.accessType` di Google Meet quando vuoi che la policy no-knock della stanza sia esplicita invece di essere ereditata dai valori predefiniti dell'account Google:

bashCopy code
[code]
    openclaw googlemeet create --access-type OPEN --transport chrome-node --mode agent
[/code]

`OPEN` permette a chiunque abbia l'URL Meet di unirsi senza bussare. `TRUSTED` permette agli utenti attendibili dell'organizzazione host, agli utenti esterni invitati e agli utenti con accesso telefonico di unirsi senza bussare. `RESTRICTED` limita l'ingresso senza bussare agli invitati. Queste impostazioni si applicano solo al percorso ufficiale di creazione tramite API Google Meet, quindi le credenziali OAuth devono essere configurate.

Se hai autenticato Google Meet prima che questa opzione fosse disponibile, riesegui `openclaw googlemeet auth login --json` dopo aver aggiunto lo scope `meetings.space.settings` alla schermata di consenso OAuth di Google.

Crea solo l'URL senza unirti:

bashCopy code
[code]
    openclaw googlemeet create --no-join
[/code]

`googlemeet create` ha due percorsi:

  * Creazione API: usata quando sono configurate le credenziali OAuth Google Meet. Questo è il percorso più deterministico e non dipende dallo stato dell'interfaccia del browser.
  * Fallback del browser: usato quando le credenziali OAuth sono assenti. OpenClaw usa il node Chrome bloccato, apre `https://meet.google.com/new`, attende che Google reindirizzi a un vero URL con codice riunione, quindi restituisce quell'URL. Questo percorso richiede che il profilo Chrome di OpenClaw sul node sia già connesso a Google. L'automazione del browser gestisce il prompt iniziale del microfono proprio di Meet; quel prompt non viene trattato come errore di login Google. I flussi di unione e creazione provano anche a riutilizzare una scheda Meet esistente prima di aprirne una nuova. La corrispondenza ignora stringhe di query URL innocue come `authuser`, quindi un nuovo tentativo dell'agente dovrebbe mettere a fuoco la riunione già aperta invece di creare una seconda scheda Chrome.


L'output del comando/strumento include un campo `source` (`api` o `browser`) così gli agenti possono spiegare quale percorso è stato usato. `create` si unisce alla nuova riunione per impostazione predefinita e restituisce `joined: true` più la sessione di unione. Per generare solo l'URL, usa `create --no-join` nella CLI o passa `"join": false` allo strumento.

Oppure di' a un agente: "Crea un Google Meet, unisciti con la modalità talk-back dell'agente e inviami il link." L'agente dovrebbe chiamare `google_meet` con `action: "create"` e poi condividere il `meetingUri` restituito.

jsonCopy code
[code]
    {  "action": "create",  "transport": "chrome-node",  "mode": "agent"}
[/code]

Per un accesso in sola osservazione/controllo browser, imposta `"mode": "transcribe"`. Questo non avvia il bridge vocale duplex in tempo reale, non richiede BlackHole o SoX e non parlerà nella riunione. Gli accessi Chrome in questa modalità evitano anche la concessione dei permessi microfono/fotocamera di OpenClaw ed evitano il percorso **Usa microfono** di Meet. Se Meet mostra un interstitial di scelta audio, l'automazione prova il percorso senza microfono e altrimenti segnala un'azione manuale invece di aprire il microfono locale. In modalità transcribe, i trasporti Chrome gestiti installano anche un osservatore delle didascalie Meet best-effort. `googlemeet status --json` e `googlemeet doctor` mostrano `captioning`, `captionsEnabledAttempted`, `transcriptLines`, `lastCaptionAt`, `lastCaptionSpeaker`, `lastCaptionText` e una breve coda `recentTranscript` così gli operatori possono capire se il browser si è unito alla chiamata e se le didascalie Meet stanno producendo testo. Usa `openclaw googlemeet test-listen <meet-url> --transport chrome-node` quando ti serve una verifica sì/no: si unisce in modalità transcribe, attende nuove didascalie o movimento della trascrizione e restituisce `listenVerified`, `listenTimedOut`, campi di azione manuale e lo stato più recente delle didascalie.

Durante le sessioni in tempo reale, lo stato `google_meet` include lo stato di salute del browser e del bridge audio, come `inCall`, `manualActionRequired`, `providerConnected`, `realtimeReady`, `audioInputActive`, `audioOutputActive`, timestamp dell'ultimo input/output, contatori di byte e stato di chiusura del bridge. Se appare un prompt sicuro della pagina Meet, l'automazione del browser lo gestisce quando può. Login, ammissione da parte dell'host e prompt di autorizzazione del browser/OS sono segnalati come azione manuale con un motivo e un messaggio da far riferire all'agente. Le sessioni Chrome gestite emettono la frase introduttiva o di test solo dopo che lo stato del browser riporta `inCall: true`; altrimenti lo stato riporta `speechReady: false` e il tentativo di parlato viene bloccato invece di fingere che l'agente abbia parlato nella riunione.

Gli accessi Chrome locali passano tramite il profilo browser OpenClaw connesso. La modalità in tempo reale richiede `BlackHole 2ch` per il percorso microfono/altoparlante usato da OpenClaw. Per audio duplex pulito, usa dispositivi virtuali separati o un grafo in stile Loopback; un singolo dispositivo BlackHole è sufficiente per un primo smoke test ma può creare eco.

### Gateway locale + Chrome Parallels

Non hai **bisogno** di un Gateway OpenClaw completo o di una chiave API del modello dentro una VM macOS solo per fare in modo che la VM possieda Chrome. Esegui Gateway e agente localmente, poi esegui un host node nella VM. Abilita una volta il plugin incluso nella VM così il node pubblicizza il comando Chrome:

Cosa viene eseguito dove:

  * Host Gateway: OpenClaw Gateway, workspace dell'agente, chiavi modello/API, provider in tempo reale e configurazione del plugin Google Meet.
  * VM macOS Parallels: CLI/host node OpenClaw, Google Chrome, SoX, BlackHole 2ch e un profilo Chrome connesso a Google.
  * Non necessari nella VM: servizio Gateway, configurazione agente, chiave OpenAI/GPT o configurazione del provider del modello.


Installa le dipendenze della VM:

bashCopy code
[code]
    brew install blackhole-2ch sox
[/code]

Riavvia la VM dopo aver installato BlackHole così macOS espone `BlackHole 2ch`:

bashCopy code
[code]
    sudo reboot
[/code]

Dopo il riavvio, verifica che la VM possa vedere il dispositivo audio e i comandi SoX:

bashCopy code
[code]
    system_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Installa o aggiorna OpenClaw nella VM, quindi abilita lì il plugin incluso:

bashCopy code
[code]
    openclaw plugins enable google-meet
[/code]

Avvia l'host node nella VM:

bashCopy code
[code]
    openclaw node run --host <gateway-host> --port 18789 --display-name parallels-macos
[/code]

Se `<gateway-host>` è un IP LAN e non stai usando TLS, il node rifiuta il WebSocket in chiaro a meno che tu non scelga esplicitamente quella rete privata attendibile:

bashCopy code
[code]
    OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node run --host <gateway-lan-ip> --port 18789 --display-name parallels-macos
[/code]

Usa la stessa variabile di ambiente quando installi il node come LaunchAgent:

bashCopy code
[code]
    OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node install --host <gateway-lan-ip> --port 18789 --display-name parallels-macos --forceopenclaw node restart
[/code]

`OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` è un ambiente di processo, non un'impostazione `openclaw.json`. `openclaw node install` lo memorizza nell'ambiente LaunchAgent quando è presente nel comando di installazione.

Approva il node dall'host Gateway:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>
[/code]

Conferma che il Gateway veda il node e che questo pubblicizzi sia `googlemeet.chrome` sia la capability browser/`browser.proxy`:

bashCopy code
[code]
    openclaw nodes status
[/code]

Instrada Meet tramite quel node sull'host Gateway:

json5Copy code
[code]
    {  gateway: {    nodes: {      allowCommands: ["googlemeet.chrome", "browser.proxy"],    },  },  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {          defaultTransport: "chrome-node",          chrome: {            guestName: "OpenClaw Agent",            autoJoin: true,            reuseExistingTab: true,          },          chromeNode: {            node: "parallels-macos",          },        },      },    },  },}
[/code]

Ora unisciti normalmente dall'host Gateway:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij
[/code]

oppure chiedi all'agente di usare lo strumento `google_meet` con `transport: "chrome-node"`.

Per uno smoke test con un solo comando che crea o riutilizza una sessione, pronuncia una frase nota e stampa lo stato della sessione:

bashCopy code
[code]
    openclaw googlemeet test-speech https://meet.google.com/abc-defg-hij
[/code]

Durante la partecipazione in tempo reale, l'automazione del browser di OpenClaw compila il nome dell'ospite, fa clic su Partecipa/Chiedi di partecipare e accetta la scelta "Usa il microfono" al primo avvio di Meet quando quel prompt appare. Durante la partecipazione in sola osservazione o la creazione di una riunione solo tramite browser, prosegue oltre lo stesso prompt senza microfono quando tale scelta è disponibile. Se il profilo del browser non ha effettuato l'accesso, Meet è in attesa dell'ammissione da parte dell'host, Chrome richiede l'autorizzazione a microfono/fotocamera per una partecipazione in tempo reale, oppure Meet è bloccato su un prompt che l'automazione non è riuscita a risolvere, il risultato di join/test-speech segnala `manualActionRequired: true` con `manualActionReason` e `manualActionMessage`. Gli agenti devono smettere di riprovare la partecipazione, segnalare esattamente quel messaggio più gli attuali `browserUrl`/`browserTitle`, e riprovare solo dopo che l'azione manuale nel browser è completa.

Se `chromeNode.node` viene omesso, OpenClaw seleziona automaticamente solo quando esattamente un nodo connesso dichiara sia `googlemeet.chrome` sia il controllo del browser. Se sono connessi diversi nodi compatibili, imposta `chromeNode.node` sull'id del nodo, sul nome visualizzato o sull'IP remoto.

Controlli per errori comuni:

  * `Configured Google Meet node ... is not usable: offline`: il nodo fissato è noto al Gateway ma non disponibile. Gli agenti devono trattare quel nodo come stato diagnostico, non come host Chrome utilizzabile, e segnalare il blocco di configurazione invece di ripiegare su un altro trasporto, a meno che l'utente non lo abbia richiesto.
  * `No connected Google Meet-capable node`: avvia `openclaw node run` nella VM, approva l'abbinamento e assicurati che `openclaw plugins enable google-meet` e `openclaw plugins enable browser` siano stati eseguiti nella VM. Conferma anche che l'host Gateway consenta entrambi i comandi del nodo con `gateway.nodes.allowCommands: ["googlemeet.chrome", "browser.proxy"]`.
  * `BlackHole 2ch audio device not found`: installa `blackhole-2ch` sull'host verificato e riavvia prima di usare l'audio Chrome locale.
  * `BlackHole 2ch audio device not found on the node`: installa `blackhole-2ch` nella VM e riavvia la VM.
  * Chrome si apre ma non riesce a partecipare: accedi al profilo del browser dentro la VM, oppure mantieni `chrome.guestName` impostato per la partecipazione come ospite. La partecipazione automatica come ospite usa l'automazione del browser di OpenClaw tramite il proxy browser del nodo; assicurati che la configurazione del browser del nodo punti al profilo desiderato, per esempio `browser.defaultProfile: "user"` o un profilo di sessione esistente denominato.
  * Schede Meet duplicate: lascia `chrome.reuseExistingTab: true` abilitato. OpenClaw attiva una scheda esistente per lo stesso URL Meet prima di aprirne una nuova, e la creazione di riunioni tramite browser riusa una scheda `https://meet.google.com/new` o del prompt dell'account Google già in corso prima di aprirne un'altra.
  * Nessun audio: in Meet, instrada l'audio di microfono/altoparlante tramite il percorso del dispositivo audio virtuale usato da OpenClaw; usa dispositivi virtuali separati o un routing in stile Loopback per audio duplex pulito.


## Note di installazione

Il valore predefinito di talk-back di Chrome usa due strumenti esterni:

  * `sox`: utilità audio da riga di comando. Il Plugin usa comandi CoreAudio espliciti per il bridge audio PCM16 predefinito a 24 kHz.
  * `blackhole-2ch`: driver audio virtuale per macOS. Crea il dispositivo audio `BlackHole 2ch` che Chrome/Meet può instradare.


OpenClaw non include né ridistribuisce nessuno dei due pacchetti. La documentazione chiede agli utenti di installarli come dipendenze host tramite Homebrew. SoX è concesso in licenza come `LGPL-2.0-only AND GPL-2.0-only`; BlackHole è GPL-3.0. Se crei un installer o un'appliance che include BlackHole con OpenClaw, rivedi i termini di licenza upstream di BlackHole oppure ottieni una licenza separata da Existential Audio.

## Trasporti

### Chrome

Il trasporto Chrome apre l'URL Meet tramite il controllo browser di OpenClaw e partecipa come profilo browser OpenClaw con accesso effettuato. Su macOS, il Plugin verifica la presenza di `BlackHole 2ch` prima dell'avvio. Se configurato, esegue anche un comando di integrità del bridge audio e un comando di avvio prima di aprire Chrome. Usa `chrome` quando Chrome/audio sono sull'host Gateway; usa `chrome-node` quando Chrome/audio sono su un nodo abbinato, come una VM macOS Parallels. Per Chrome locale, scegli il profilo con `browser.defaultProfile`; `chrome.browserProfile` viene passato agli host `chrome-node`.

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij --transport chromeopenclaw googlemeet join https://meet.google.com/abc-defg-hij --transport chrome-node
[/code]

Instrada l'audio di microfono e altoparlante di Chrome tramite il bridge audio locale di OpenClaw. Se `BlackHole 2ch` non è installato, la partecipazione fallisce con un errore di configurazione invece di entrare silenziosamente senza un percorso audio.

### Twilio

Il trasporto Twilio è un piano di chiamata rigoroso delegato al Plugin Voice Call. Non analizza le pagine Meet per cercare numeri di telefono.

Usalo quando la partecipazione con Chrome non è disponibile o vuoi un fallback di accesso telefonico. Google Meet deve esporre un numero di accesso telefonico e un PIN per la riunione; OpenClaw non li scopre dalla pagina Meet.

Abilita il Plugin Voice Call sull'host Gateway, non sul nodo Chrome:

json5Copy code
[code]
    {  plugins: {    allow: ["google-meet", "voice-call", "google"],    entries: {      "google-meet": {        enabled: true,        config: {          defaultTransport: "chrome-node",          // or set "twilio" if Twilio should be the default        },      },      "voice-call": {        enabled: true,        config: {          provider: "twilio",          inboundPolicy: "allowlist",          realtime: {            enabled: true,            provider: "google",            instructions: "Join this Google Meet as an OpenClaw agent. Be brief.",            toolPolicy: "safe-read-only",            providers: {              google: {                silenceDurationMs: 500,                startSensitivity: "high",              },            },          },        },      },      google: {        enabled: true,      },    },  },}
[/code]

Fornisci le credenziali Twilio tramite ambiente o configurazione. L'ambiente mantiene i segreti fuori da `openclaw.json`:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID=AC...export TWILIO_AUTH_TOKEN=...export TWILIO_FROM_NUMBER=+15550001234export GEMINI_API_KEY=...
[/code]

Usa invece `realtime.provider: "openai"` con il Plugin provider OpenAI e `OPENAI_API_KEY` se quello è il tuo provider voce in tempo reale.

Riavvia o ricarica il Gateway dopo aver abilitato `voice-call`; le modifiche alla configurazione del Plugin non compaiono in un processo Gateway già in esecuzione finché non viene ricaricato.

Poi verifica:

bashCopy code
[code]
    openclaw config validateopenclaw plugins list | grep -E 'google-meet|voice-call'openclaw googlemeet setup
[/code]

Quando la delega Twilio è collegata, `googlemeet setup` include controlli riusciti `twilio-voice-call-plugin`, `twilio-voice-call-credentials` e `twilio-voice-call-webhook`.

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --pin 123456
[/code]

Usa `--dtmf-sequence` quando la riunione richiede una sequenza personalizzata:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --dtmf-sequence ww123456#
[/code]

## OAuth e verifiche preliminari

OAuth è opzionale per creare un link Meet perché `googlemeet create` può ripiegare sull'automazione del browser. Configura OAuth quando vuoi la creazione tramite API ufficiale, la risoluzione degli spazi o i controlli preliminari della Meet Media API.

L'accesso alla Google Meet API usa OAuth utente: crea un client OAuth Google Cloud, richiedi gli ambiti necessari, autorizza un account Google, quindi salva il token di aggiornamento risultante nella configurazione del Plugin Google Meet oppure fornisci le variabili d'ambiente `OPENCLAW_GOOGLE_MEET_*`.

OAuth non sostituisce il percorso di partecipazione Chrome. I trasporti Chrome e Chrome-node partecipano comunque tramite un profilo Chrome con accesso effettuato, BlackHole/SoX e un nodo connesso quando usi la partecipazione tramite browser. OAuth serve solo per il percorso ufficiale della Google Meet API: creare spazi riunione, risolvere spazi ed eseguire controlli preliminari della Meet Media API.

### Crea credenziali Google

In Google Cloud Console:

  1. Crea o seleziona un progetto Google Cloud.

  2. Abilita **Google Meet REST API** per quel progetto.

  3. Configura la schermata di consenso OAuth.

     * **Interno** è la soluzione più semplice per un'organizzazione Google Workspace.
     * **Esterno** funziona per configurazioni personali/di test; mentre l'app è in Testing, aggiungi ogni account Google che autorizzerà l'app come utente di test.
  4. Aggiungi gli ambiti richiesti da OpenClaw:

     * `https://www.googleapis.com/auth/meetings.space.created`
     * `https://www.googleapis.com/auth/meetings.space.readonly`
     * `https://www.googleapis.com/auth/meetings.space.settings`
     * `https://www.googleapis.com/auth/meetings.conference.media.readonly`
  5. Crea un ID client OAuth.

     * Tipo di applicazione: **Applicazione web**.

     * URI di reindirizzamento autorizzato:

textCopy code
[code]http://localhost:8085/oauth2callback
[/code]

  6. Copia l'ID client e il segreto client.


`meetings.space.created` è richiesto da Google Meet `spaces.create`. `meetings.space.readonly` consente a OpenClaw di risolvere URL/codici Meet in spazi. `meetings.space.settings` consente a OpenClaw di passare impostazioni `SpaceConfig` come `accessType` durante la creazione della stanza tramite API. `meetings.conference.media.readonly` serve per le verifiche preliminari e il lavoro multimediale della Meet Media API; Google potrebbe richiedere l'iscrizione alla Developer Preview per l'uso effettivo della Media API. Se ti servono solo partecipazioni Chrome basate su browser, salta completamente OAuth.

### Genera il token di aggiornamento

Configura `oauth.clientId` e facoltativamente `oauth.clientSecret`, oppure passali come variabili d'ambiente, poi esegui:

bashCopy code
[code]
    openclaw googlemeet auth login --json
[/code]

Il comando stampa un blocco di configurazione `oauth` con un token di aggiornamento. Usa PKCE, callback localhost su `http://localhost:8085/oauth2callback` e un flusso manuale copia/incolla con `--manual`.

Esempi:

bashCopy code
[code]
    OPENCLAW_GOOGLE_MEET_CLIENT_ID="your-client-id" \OPENCLAW_GOOGLE_MEET_CLIENT_SECRET="your-client-secret" \openclaw googlemeet auth login --json
[/code]

Usa la modalità manuale quando il browser non può raggiungere la callback locale:

bashCopy code
[code]
    OPENCLAW_GOOGLE_MEET_CLIENT_ID="your-client-id" \OPENCLAW_GOOGLE_MEET_CLIENT_SECRET="your-client-secret" \openclaw googlemeet auth login --json --manual
[/code]

L'output JSON include:

jsonCopy code
[code]
    {  "oauth": {    "clientId": "your-client-id",    "clientSecret": "your-client-secret",    "refreshToken": "refresh-token",    "accessToken": "access-token",    "expiresAt": 1770000000000  },  "scope": "..."}
[/code]

Salva l'oggetto `oauth` sotto la configurazione del Plugin Google Meet:

json5Copy code
[code]
    {  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {          oauth: {            clientId: "your-client-id",            clientSecret: "your-client-secret",            refreshToken: "refresh-token",          },        },      },    },  },}
[/code]

Preferisci le variabili d'ambiente quando non vuoi il token di aggiornamento nella configurazione. Se sono presenti sia valori di configurazione sia valori d'ambiente, il Plugin risolve prima la configurazione e poi il fallback d'ambiente.

Il consenso OAuth include la creazione di spazi Meet, l'accesso in lettura agli spazi Meet e l'accesso in lettura ai contenuti multimediali delle conferenze Meet. Se hai effettuato l'autenticazione prima che esistesse il supporto alla creazione di riunioni, riesegui `openclaw googlemeet auth login --json` così il token di aggiornamento ha l'ambito `meetings.space.created`.

### Verifica OAuth con doctor

Esegui il doctor OAuth quando vuoi un controllo di integrità rapido e privo di segreti:

bashCopy code
[code]
    openclaw googlemeet doctor --oauth --json
[/code]

Questo non carica il runtime Chrome né richiede un nodo Chrome connesso. Verifica che la configurazione OAuth esista e che il token di aggiornamento possa generare un token di accesso. Il report JSON include solo campi di stato come `ok`, `configured`, `tokenSource`, `expiresAt` e messaggi di controllo; non stampa il token di accesso, il token di aggiornamento o il segreto client.

Risultati comuni:

Controllo | Significato  
---|---  
`oauth-config` | Sono presenti `oauth.clientId` più `oauth.refreshToken`, oppure un token di accesso memorizzato nella cache.  
`oauth-token` | Il token di accesso memorizzato nella cache è ancora valido, oppure il token di aggiornamento ha emesso un nuovo token di accesso.  
`meet-spaces-get` | Il controllo facoltativo `--meeting` ha risolto uno spazio Meet esistente.  
`meet-spaces-create` | Il controllo facoltativo `--create-space` ha creato un nuovo spazio Meet.  
  
Per verificare anche l'abilitazione dell'API Google Meet e l'ambito `spaces.create`, esegui il controllo di creazione con effetti collaterali:

bashCopy code
[code]
    openclaw googlemeet doctor --oauth --create-space --jsonopenclaw googlemeet create --no-join --json
[/code]

`--create-space` crea un URL Meet temporaneo. Usalo quando devi confermare che il progetto Google Cloud abbia l'API Meet abilitata e che l'account autorizzato abbia l'ambito `meetings.space.created`.

Per verificare l'accesso in lettura a uno spazio riunione esistente:

bashCopy code
[code]
    openclaw googlemeet doctor --oauth --meeting https://meet.google.com/abc-defg-hij --jsonopenclaw googlemeet resolve-space --meeting https://meet.google.com/abc-defg-hij
[/code]

`doctor --oauth --meeting` e `resolve-space` verificano l'accesso in lettura a uno spazio esistente a cui l'account Google autorizzato può accedere. Un `403` da questi controlli di solito significa che l'API REST Google Meet è disabilitata, che al token di aggiornamento autorizzato manca l'ambito richiesto oppure che l'account Google non può accedere a quello spazio Meet. Un errore del token di aggiornamento significa che devi rieseguire `openclaw googlemeet auth login --json` e salvare il nuovo blocco `oauth`.

Non sono necessarie credenziali OAuth per il fallback del browser. In questa modalità, l'autenticazione Google proviene dal profilo Chrome con accesso eseguito sul node selezionato, non dalla configurazione OpenClaw.

Queste variabili d'ambiente sono accettate come fallback:

  * `OPENCLAW_GOOGLE_MEET_CLIENT_ID` o `GOOGLE_MEET_CLIENT_ID`
  * `OPENCLAW_GOOGLE_MEET_CLIENT_SECRET` o `GOOGLE_MEET_CLIENT_SECRET`
  * `OPENCLAW_GOOGLE_MEET_REFRESH_TOKEN` o `GOOGLE_MEET_REFRESH_TOKEN`
  * `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN` o `GOOGLE_MEET_ACCESS_TOKEN`
  * `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN_EXPIRES_AT` o `GOOGLE_MEET_ACCESS_TOKEN_EXPIRES_AT`
  * `OPENCLAW_GOOGLE_MEET_DEFAULT_MEETING` o `GOOGLE_MEET_DEFAULT_MEETING`
  * `OPENCLAW_GOOGLE_MEET_PREVIEW_ACK` o `GOOGLE_MEET_PREVIEW_ACK`


Risolvi un URL Meet, un codice o `spaces/{id}` tramite `spaces.get`:

bashCopy code
[code]
    openclaw googlemeet resolve-space --meeting https://meet.google.com/abc-defg-hij
[/code]

Esegui il preflight prima del lavoro sui media:

bashCopy code
[code]
    openclaw googlemeet preflight --meeting https://meet.google.com/abc-defg-hij
[/code]

Elenca gli artefatti della riunione e le presenze dopo che Meet ha creato i record della conferenza:

bashCopy code
[code]
    openclaw googlemeet artifacts --meeting https://meet.google.com/abc-defg-hijopenclaw googlemeet attendance --meeting https://meet.google.com/abc-defg-hijopenclaw googlemeet export --meeting https://meet.google.com/abc-defg-hij --output ./meet-export
[/code]

Con `--meeting`, `artifacts` e `attendance` usano per impostazione predefinita il record della conferenza più recente. Passa `--all-conference-records` quando vuoi ogni record conservato per quella riunione.

La ricerca nel calendario può risolvere l'URL della riunione da Google Calendar prima di leggere gli artefatti Meet:

bashCopy code
[code]
    openclaw googlemeet latest --todayopenclaw googlemeet calendar-events --today --jsonopenclaw googlemeet artifacts --event "Weekly sync"openclaw googlemeet attendance --today --format csv --output attendance.csv
[/code]

`--today` cerca nel calendario `primary` di oggi un evento Calendar con un link Google Meet. Usa `--event <query>` per cercare testo dell'evento corrispondente e `--calendar <id>` per un calendario non principale. La ricerca nel calendario richiede un nuovo accesso OAuth che includa l'ambito in sola lettura degli eventi Calendar. `calendar-events` mostra in anteprima gli eventi Meet corrispondenti e contrassegna l'evento che `latest`, `artifacts`, `attendance` o `export` sceglierà.

Se conosci già l'ID del record della conferenza, indirizzalo direttamente:

bashCopy code
[code]
    openclaw googlemeet latest --meeting https://meet.google.com/abc-defg-hijopenclaw googlemeet artifacts --conference-record conferenceRecords/abc123 --jsonopenclaw googlemeet attendance --conference-record conferenceRecords/abc123 --json
[/code]

Termina una conferenza attiva per uno spazio creato tramite API quando vuoi chiudere la stanza dopo la chiamata:

bashCopy code
[code]
    openclaw googlemeet end-active-conference https://meet.google.com/abc-defg-hij
[/code]

Questo chiama Google Meet `spaces.endActiveConference` e richiede OAuth con l'ambito `meetings.space.created` per uno spazio che l'account autorizzato può gestire. OpenClaw accetta come input un URL Meet, un codice riunione o `spaces/{id}` e lo risolve nella risorsa spazio dell'API prima di terminare la conferenza attiva. È separato da `googlemeet leave`: `leave` interrompe la partecipazione locale/di sessione di OpenClaw, mentre `end-active-conference` chiede a Google Meet di terminare la conferenza attiva per lo spazio.

Scrivi un report leggibile:

bashCopy code
[code]
    openclaw googlemeet artifacts --conference-record conferenceRecords/abc123 \  --format markdown --output meet-artifacts.mdopenclaw googlemeet attendance --conference-record conferenceRecords/abc123 \  --format markdown --output meet-attendance.mdopenclaw googlemeet attendance --conference-record conferenceRecords/abc123 \  --format csv --output meet-attendance.csvopenclaw googlemeet export --conference-record conferenceRecords/abc123 \  --include-doc-bodies --zip --output meet-exportopenclaw googlemeet export --conference-record conferenceRecords/abc123 \  --include-doc-bodies --dry-run
[/code]

`artifacts` restituisce i metadati del record della conferenza più i metadati delle risorse relative a partecipanti, registrazioni, trascrizioni, voci di trascrizione strutturate e note intelligenti quando Google li espone per la riunione. Usa `--no-transcript-entries` per saltare la ricerca delle voci nelle riunioni di grandi dimensioni. `attendance` espande i partecipanti in righe di sessione partecipante con orari di prima/ultima presenza, durata totale della sessione, flag di ritardo/uscita anticipata e risorse partecipante duplicate unite per utente con accesso eseguito o nome visualizzato. Passa `--no-merge-duplicates` per mantenere separate le risorse partecipante grezze, `--late-after-minutes` per regolare il rilevamento dei ritardi e `--early-before-minutes` per regolare il rilevamento delle uscite anticipate.

`export` scrive una cartella contenente `summary.md`, `attendance.csv`, `transcript.md`, `artifacts.json`, `attendance.json` e `manifest.json`. `manifest.json` registra l'input scelto, le opzioni di esportazione, i record della conferenza, i file di output, i conteggi, l'origine del token, l'evento Calendar quando ne è stato usato uno e gli eventuali avvisi di recupero parziale. Passa `--zip` per scrivere anche un archivio portabile accanto alla cartella. Passa `--include-doc-bodies` per esportare il testo dei documenti Google Docs collegati a trascrizioni e note intelligenti tramite Google Drive `files.export`; questo richiede un nuovo accesso OAuth che includa l'ambito Drive Meet in sola lettura. Senza `--include-doc-bodies`, le esportazioni includono solo i metadati Meet e le voci di trascrizione strutturate. Se Google restituisce un errore parziale di artefatto, come un errore di elenco delle note intelligenti, di voce di trascrizione o di corpo documento Drive, il riepilogo e il manifesto mantengono l'avviso invece di far fallire l'intera esportazione. Usa `--dry-run` per recuperare gli stessi dati di artefatti/presenze e stampare il JSON del manifesto senza creare la cartella o lo ZIP. È utile prima di scrivere un'esportazione grande o quando un agente ha bisogno solo di conteggi, record selezionati e avvisi.

Gli agenti possono anche creare lo stesso bundle tramite lo strumento `google_meet`:

jsonCopy code
[code]
    {  "action": "export",  "conferenceRecord": "conferenceRecords/abc123",  "includeDocumentBodies": true,  "outputDir": "meet-export",  "zip": true}
[/code]

Imposta `"dryRun": true` per restituire solo il manifesto di esportazione e saltare la scrittura dei file.

Gli agenti possono anche creare una stanza supportata da API con una policy di accesso esplicita:

jsonCopy code
[code]
    {  "action": "create",  "transport": "chrome-node",  "mode": "agent",  "accessType": "OPEN"}
[/code]

E possono terminare la conferenza attiva per una stanza nota:

jsonCopy code
[code]
    {  "action": "end_active_conference",  "meeting": "https://meet.google.com/abc-defg-hij"}
[/code]

Per la validazione con ascolto prioritario, gli agenti devono usare `test_listen` prima di dichiarare che la riunione è utile:

jsonCopy code
[code]
    {  "action": "test_listen",  "url": "https://meet.google.com/abc-defg-hij",  "transport": "chrome-node",  "timeoutMs": 30000}
[/code]

Esegui il live smoke protetto su una riunione reale conservata:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_GOOGLE_MEET_LIVE_MEETING=https://meet.google.com/abc-defg-hij \pnpm test:live -- extensions/google-meet/google-meet.live.test.ts
[/code]

Esegui la sonda browser live con ascolto prioritario su una riunione in cui qualcuno parlerà con i sottotitoli Meet disponibili:

bashCopy code
[code]
    openclaw googlemeet setup --transport chrome-node --mode transcribeopenclaw googlemeet test-listen https://meet.google.com/abc-defg-hij --transport chrome-node --timeout-ms 30000
[/code]

Ambiente live smoke:

  * `OPENCLAW_LIVE_TEST=1` abilita i test live protetti.
  * `OPENCLAW_GOOGLE_MEET_LIVE_MEETING` punta a un URL Meet, codice o `spaces/{id}` conservato.
  * `OPENCLAW_GOOGLE_MEET_CLIENT_ID` o `GOOGLE_MEET_CLIENT_ID` fornisce l'ID client OAuth.
  * `OPENCLAW_GOOGLE_MEET_REFRESH_TOKEN` o `GOOGLE_MEET_REFRESH_TOKEN` fornisce il token di aggiornamento.
  * Facoltativo: `OPENCLAW_GOOGLE_MEET_CLIENT_SECRET`, `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN` e `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN_EXPIRES_AT` usano gli stessi nomi di fallback senza il prefisso `OPENCLAW_`.


Il live smoke di base per artefatti/presenze richiede `https://www.googleapis.com/auth/meetings.space.readonly` e `https://www.googleapis.com/auth/meetings.conference.media.readonly`. La ricerca nel calendario richiede `https://www.googleapis.com/auth/calendar.events.readonly`. L'esportazione del corpo documento Drive richiede `https://www.googleapis.com/auth/drive.meet.readonly`.

Crea un nuovo spazio Meet:

bashCopy code
[code]
    openclaw googlemeet create
[/code]

Il comando stampa il nuovo `meeting uri`, l'origine e la sessione di partecipazione. Con credenziali OAuth usa l'API Google Meet ufficiale. Senza credenziali OAuth usa come fallback il profilo browser con accesso eseguito del node Chrome fissato. Gli agenti possono usare lo strumento `google_meet` con `action: "create"` per creare e partecipare in un solo passaggio. Per la creazione del solo URL, passa `"join": false`.

Esempio di output JSON dal fallback del browser:

jsonCopy code
[code]
    {  "source": "browser",  "meetingUri": "https://meet.google.com/abc-defg-hij",  "joined": true,  "browser": {    "nodeId": "ba0f4e4bc...",    "targetId": "tab-1"  },  "join": {    "session": {      "id": "meet_...",      "url": "https://meet.google.com/abc-defg-hij"    }  }}
[/code]

Se il fallback del browser incontra un blocco di accesso Google o di autorizzazione Meet prima di poter creare l'URL, il metodo Gateway restituisce una risposta non riuscita e lo strumento `google_meet` restituisce dettagli strutturati invece di una stringa semplice:

jsonCopy code
[code]
    {  "source": "browser",  "error": "google-login-required: Sign in to Google in the OpenClaw browser profile, then retry meeting creation.",  "manualActionRequired": true,  "manualActionReason": "google-login-required",  "manualActionMessage": "Sign in to Google in the OpenClaw browser profile, then retry meeting creation.",  "browser": {    "nodeId": "ba0f4e4bc...",    "targetId": "tab-1",    "browserUrl": "https://accounts.google.com/signin",    "browserTitle": "Sign in - Google Accounts"  }}
[/code]

Quando un agente vede `manualActionRequired: true`, deve segnalare il `manualActionMessage` più il contesto node/scheda del browser e smettere di aprire nuove schede Meet finché l'operatore non completa il passaggio nel browser.

Esempio di output JSON dalla creazione tramite API:

jsonCopy code
[code]
    {  "source": "api",  "meetingUri": "https://meet.google.com/abc-defg-hij",  "joined": true,  "space": {    "name": "spaces/abc-defg-hij",    "meetingCode": "abc-defg-hij",    "meetingUri": "https://meet.google.com/abc-defg-hij"  },  "join": {    "session": {      "id": "meet_...",      "url": "https://meet.google.com/abc-defg-hij"    }  }}
[/code]

La creazione di un Meet partecipa per impostazione predefinita. Il trasporto Chrome o Chrome-node richiede comunque un profilo Google Chrome autenticato per partecipare tramite il browser. Se il profilo è disconnesso, OpenClaw segnala `manualActionRequired: true` o un errore di fallback del browser e chiede all'operatore di completare l'accesso a Google prima di riprovare.

Imposta `preview.enrollmentAcknowledged: true` solo dopo aver confermato che il progetto Cloud, il principale OAuth e i partecipanti alla riunione sono iscritti al Programma Google Workspace Developer Preview per le API multimediali di Meet.

## Configurazione

Il percorso comune dell'agente Chrome richiede solo il Plugin abilitato, BlackHole, SoX, una chiave per un provider di trascrizione in tempo reale e un provider TTS OpenClaw configurato. OpenAI è il provider di trascrizione predefinito; imposta `realtime.voiceProvider` su `"google"` e `realtime.model` per usare Google Gemini Live per la modalità `bidi` senza modificare il provider di trascrizione predefinito della modalità agente:

bashCopy code
[code]
    brew install blackhole-2ch soxexport OPENAI_API_KEY=sk-...# orexport GEMINI_API_KEY=...
[/code]

Imposta la configurazione del Plugin in `plugins.entries.google-meet.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {},      },    },  },}
[/code]

Valori predefiniti:

  * `defaultTransport: "chrome"`
  * `defaultMode: "agent"` (`"realtime"` è accettato solo come alias di compatibilità legacy per `"agent"`; le nuove chiamate agli strumenti dovrebbero indicare `"agent"`)
  * `chromeNode.node`: ID/nome/IP del Node opzionale per `chrome-node`
  * `chrome.audioBackend: "blackhole-2ch"`
  * `chrome.guestName: "OpenClaw Agent"`: nome usato nella schermata ospite di Meet quando non è stato effettuato l'accesso
  * `chrome.autoJoin: true`: inserimento best-effort del nome ospite e clic su Partecipa ora tramite l'automazione browser di OpenClaw su `chrome-node`
  * `chrome.reuseExistingTab: true`: attiva una scheda Meet esistente invece di aprire duplicati
  * `chrome.waitForInCallMs: 20000`: attende che la scheda Meet segnali lo stato in chiamata prima di attivare l'introduzione talk-back
  * `chrome.audioFormat: "pcm16-24khz"`: formato audio della coppia di comandi. Usa `"g711-ulaw-8khz"` solo per coppie di comandi legacy/personalizzate che emettono ancora audio telefonico.
  * `chrome.audioBufferBytes: 4096`: buffer di elaborazione SoX per i comandi audio generati della coppia di comandi Chrome. È metà del buffer predefinito di SoX da 8192 byte, riducendo la latenza predefinita della pipe e lasciando margine per aumentarlo su host occupati. I valori inferiori al minimo di SoX vengono limitati a 17 byte.
  * `chrome.audioInputCommand`: comando SoX che legge da CoreAudio `BlackHole 2ch` e scrive audio in `chrome.audioFormat`
  * `chrome.audioOutputCommand`: comando SoX che legge audio in `chrome.audioFormat` e scrive su CoreAudio `BlackHole 2ch`
  * `chrome.bargeInInputCommand`: comando opzionale del microfono locale che scrive PCM mono little-endian con segno a 16 bit per rilevare le interruzioni umane mentre la riproduzione dell'assistente è attiva. Questo attualmente si applica al bridge della coppia di comandi `chrome` ospitato dal Gateway.
  * `chrome.bargeInRmsThreshold: 650`: livello RMS che viene conteggiato come interruzione umana su `chrome.bargeInInputCommand`
  * `chrome.bargeInPeakThreshold: 2500`: livello di picco che viene conteggiato come interruzione umana su `chrome.bargeInInputCommand`
  * `chrome.bargeInCooldownMs: 900`: ritardo minimo tra cancellazioni ripetute di interruzioni umane
  * `mode: "agent"`: modalità talk-back predefinita. Il parlato dei partecipanti viene trascritto dal provider di trascrizione in tempo reale configurato, inviato all'agente OpenClaw configurato in una sessione di sotto-agente per riunione e riprodotto vocalmente tramite il normale runtime TTS di OpenClaw.
  * `mode: "bidi"`: modalità di fallback con modello bidirezionale diretto in tempo reale. Il provider vocale in tempo reale risponde direttamente al parlato dei partecipanti e può chiamare `openclaw_agent_consult` per risposte più approfondite/supportate da strumenti.
  * `mode: "transcribe"`: modalità di sola osservazione senza bridge talk-back.
  * `realtime.provider: "openai"`: fallback di compatibilità usato quando i campi provider con ambito sotto sono non impostati.
  * `realtime.transcriptionProvider: "openai"`: ID provider usato dalla modalità `agent` per la trascrizione in tempo reale.
  * `realtime.voiceProvider`: ID provider usato dalla modalità `bidi` per la voce diretta in tempo reale. Impostalo su `"google"` per usare Gemini Live mantenendo la trascrizione in modalità agente su OpenAI.
  * `realtime.toolPolicy: "safe-read-only"`
  * `realtime.instructions`: brevi risposte vocali, con `openclaw_agent_consult` per risposte più approfondite
  * `realtime.introMessage`: breve controllo vocale di disponibilità quando il bridge in tempo reale si connette; impostalo su `""` per partecipare in silenzio
  * `realtime.agentId`: ID agente OpenClaw opzionale per `openclaw_agent_consult`; il valore predefinito è `main`


Override opzionali:

json5Copy code
[code]
    {  defaults: {    meeting: "https://meet.google.com/abc-defg-hij",  },  browser: {    defaultProfile: "openclaw",  },  chrome: {    guestName: "OpenClaw Agent",    waitForInCallMs: 30000,    bargeInInputCommand: [      "sox",      "-q",      "-t",      "coreaudio",      "External Microphone",      "-r",      "24000",      "-c",      "1",      "-b",      "16",      "-e",      "signed-integer",      "-t",      "raw",      "-",    ],  },  chromeNode: {    node: "parallels-macos",  },  defaultMode: "agent",  realtime: {    provider: "openai",    transcriptionProvider: "openai",    voiceProvider: "google",    model: "gemini-2.5-flash-native-audio-preview-12-2025",    agentId: "jay",    toolPolicy: "owner",    introMessage: "Say exactly: I'm here.",    providers: {      google: {        voice: "Kore",      },    },  },}
[/code]

ElevenLabs sia per l'ascolto sia per il parlato in modalità agente:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "elevenlabs",      providers: {        elevenlabs: {          modelId: "eleven_v3",          voiceId: "pMsXgVXv3BLzUgSXRplE",        },      },    },  },  plugins: {    entries: {      "google-meet": {        config: {          realtime: {            transcriptionProvider: "elevenlabs",            providers: {              elevenlabs: {                modelId: "scribe_v2_realtime",                audioFormat: "ulaw_8000",                sampleRate: 8000,                commitStrategy: "vad",              },            },          },        },      },    },  },}
[/code]

La voce Meet persistente proviene da `messages.tts.providers.elevenlabs.voiceId`. Le risposte dell'agente possono anche usare direttive per risposta `[[tts:voiceId=... model=eleven_v3]]` quando gli override del modello TTS sono abilitati, ma la configurazione è l'impostazione predefinita deterministica per le riunioni. Alla partecipazione, i log dovrebbero mostrare `transcriptionProvider=elevenlabs` e ogni risposta parlata dovrebbe registrare `provider=elevenlabs model=eleven_v3 voice=<voiceId>`.

Configurazione solo Twilio:

json5Copy code
[code]
    {  defaultTransport: "twilio",  twilio: {    defaultDialInNumber: "+15551234567",    defaultPin: "123456",  },  voiceCall: {    gatewayUrl: "ws://127.0.0.1:18789",  },}
[/code]

`voiceCall.enabled` ha valore predefinito `true`; con il trasporto Twilio delega la chiamata PSTN effettiva, DTMF e il saluto introduttivo al Plugin Voice Call. Voice Call riproduce la sequenza DTMF prima di aprire il flusso multimediale in tempo reale, poi usa il testo introduttivo salvato come saluto iniziale in tempo reale. Se `voice-call` non è abilitato, Google Meet può comunque validare e registrare il piano di composizione, ma non può effettuare la chiamata Twilio.

## Strumento

Gli agenti possono usare lo strumento `google_meet`:

jsonCopy code
[code]
    {  "action": "join",  "url": "https://meet.google.com/abc-defg-hij",  "transport": "chrome-node",  "mode": "agent"}
[/code]

Usa `transport: "chrome"` quando Chrome viene eseguito sull'host Gateway. Usa `transport: "chrome-node"` quando Chrome viene eseguito su un Node associato, ad esempio una VM Parallels. In entrambi i casi, i provider del modello e `openclaw_agent_consult` vengono eseguiti sull'host Gateway, quindi le credenziali del modello restano lì. Con il valore predefinito `mode: "agent"`, il provider di trascrizione in tempo reale gestisce l'ascolto, l'agente OpenClaw configurato produce la risposta e il normale TTS di OpenClaw la pronuncia in Meet. Usa `mode: "bidi"` quando vuoi che il modello vocale in tempo reale risponda direttamente. Il valore grezzo `mode: "realtime"` resta accettato come alias di compatibilità legacy per `mode: "agent"`, ma non è più pubblicizzato nello schema dello strumento dell'agente. I log della modalità agente includono il provider/modello di trascrizione risolto all'avvio del bridge e il provider TTS, il modello, la voce, il formato di output e la frequenza di campionamento dopo ogni risposta sintetizzata.

Usa `action: "status"` per elencare le sessioni attive o ispezionare un ID sessione. Usa `action: "speak"` con `sessionId` e `message` per far parlare immediatamente l'agente in tempo reale. Usa `action: "test_speech"` per creare o riutilizzare la sessione, attivare una frase nota e restituire lo stato di salute `inCall` quando l'host Chrome può segnalarlo. `test_speech` forza sempre `mode: "agent"` e fallisce se viene richiesto di essere eseguito in `mode: "transcribe"` perché le sessioni di sola osservazione intenzionalmente non possono emettere parlato. Il risultato `speechOutputVerified` si basa sull'aumento dei byte di output audio in tempo reale durante questa chiamata di test, quindi una sessione riutilizzata con audio precedente non conta come nuovo controllo vocale riuscito. Usa `action: "leave"` per contrassegnare una sessione come terminata.

`status` include lo stato di salute di Chrome quando disponibile:

  * `inCall`: Chrome sembra essere all'interno della chiamata Meet
  * `micMuted`: stato best-effort del microfono Meet
  * `manualActionRequired` / `manualActionReason` / `manualActionMessage`: il profilo del browser richiede accesso manuale, ammissione da parte dell'host Meet, autorizzazioni o riparazione del controllo browser prima che il parlato possa funzionare
  * `speechReady` / `speechBlockedReason` / `speechBlockedMessage`: indica se il parlato Chrome gestito è consentito ora. `speechReady: false` significa che OpenClaw non ha inviato la frase introduttiva/di test nel bridge audio.
  * `providerConnected` / `realtimeReady`: stato del bridge vocale in tempo reale
  * `lastInputAt` / `lastOutputAt`: ultimo audio visto dal bridge o inviato al bridge
  * `audioOutputRouted` / `audioOutputDeviceLabel`: indica se l'output multimediale della scheda Meet è stato instradato attivamente al dispositivo BlackHole usato dal bridge
  * `lastSuppressedInputAt` / `suppressedInputBytes`: input di loopback ignorato mentre la riproduzione dell'assistente è attiva

jsonCopy code
[code]
    {  "action": "speak",  "sessionId": "meet_...",  "message": "Say exactly: I'm here and listening."}
[/code]

## Modalità agente e bidi

La modalità Chrome `agent` è ottimizzata per il comportamento "il mio agente è nella riunione". Il provider di trascrizione in tempo reale ascolta l'audio della riunione, le trascrizioni finali dei partecipanti vengono instradate attraverso l'agente OpenClaw configurato e la risposta viene pronunciata tramite il normale runtime TTS di OpenClaw. Imposta `mode: "bidi"` quando vuoi che il modello vocale in tempo reale risponda direttamente. I frammenti di trascrizione finali vicini vengono uniti prima della consultazione, così un singolo turno parlato non produce più risposte parziali obsolete. Anche l'input in tempo reale viene soppresso mentre l'audio dell'assistente in coda è ancora in riproduzione, e gli echi recenti di trascrizione simili all'assistente vengono ignorati prima della consultazione dell'agente, così il local loopback di BlackHole non fa rispondere l'agente al proprio parlato.

Modalità | Chi decide la risposta | Percorso di output vocale | Usala quando  
---|---|---|---  
`agent` | L'agente OpenClaw configurato | Normale runtime TTS di OpenClaw | Vuoi il comportamento "il mio agente è nella riunione"  
`bidi` | Il modello vocale in tempo reale | Risposta audio del provider vocale in tempo reale | Vuoi il loop vocale conversazionale a latenza più bassa  
  
In modalità `bidi`, quando il modello in tempo reale richiede ragionamento più approfondito, informazioni aggiornate o i normali strumenti OpenClaw, può chiamare `openclaw_agent_consult`.

Lo strumento consult esegue dietro le quinte il normale agente OpenClaw con il contesto recente della trascrizione della riunione e restituisce una risposta parlata concisa. In modalità `agent`, OpenClaw invia quella risposta direttamente al runtime TTS; in modalità `bidi`, il modello vocale realtime può pronunciare il risultato di consult nella riunione. Usa lo stesso meccanismo consult condiviso di Voice Call.

Per impostazione predefinita, i consult vengono eseguiti sull'agente `main`. Imposta `realtime.agentId` quando una corsia Meet deve consultare un workspace agente OpenClaw dedicato, impostazioni predefinite del modello, policy degli strumenti, memoria e cronologia della sessione.

I consult in modalità agente usano una chiave di sessione per riunione `agent:<id>:subagent:google-meet:<session>`, così le domande di follow-up mantengono il contesto della riunione ereditando al tempo stesso la normale policy dell'agente dall'agente configurato.

`realtime.toolPolicy` controlla l'esecuzione di consult:

  * `safe-read-only`: espone lo strumento consult e limita l'agente normale a `read`, `web_search`, `web_fetch`, `x_search`, `memory_search` e `memory_get`.
  * `owner`: espone lo strumento consult e consente all'agente normale di usare la normale policy degli strumenti dell'agente.
  * `none`: non espone lo strumento consult al modello vocale realtime.


La chiave di sessione consult è limitata per sessione Meet, quindi le chiamate consult di follow-up possono riutilizzare il contesto consult precedente durante la stessa riunione.

Per forzare un controllo di prontezza parlato dopo che Chrome ha completato l'accesso alla chiamata:

bashCopy code
[code]
    openclaw googlemeet speak meet_... "Say exactly: I'm here and listening."
[/code]

Per lo smoke completo di accesso e parlato:

bashCopy code
[code]
    openclaw googlemeet test-speech https://meet.google.com/abc-defg-hij \  --transport chrome-node \  --message "Say exactly: I'm here and listening."
[/code]

## Checklist dei test live

Usa questa sequenza prima di affidare una riunione a un agente non presidiato:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw nodes statusopenclaw googlemeet test-speech https://meet.google.com/abc-defg-hij \  --transport chrome-node \  --message "Say exactly: Google Meet speech test complete."
[/code]

Stato Chrome-node atteso:

  * `googlemeet setup` è tutto verde.
  * `googlemeet setup` include `chrome-node-connected` quando Chrome-node è il trasporto predefinito o un nodo è fissato.
  * `nodes status` mostra il nodo selezionato connesso.
  * Il nodo selezionato pubblicizza sia `googlemeet.chrome` sia `browser.proxy`.
  * La scheda Meet entra nella chiamata e `test-speech` restituisce lo stato di salute di Chrome con `inCall: true`.


Per un host Chrome remoto, come una VM macOS Parallels, questo è il controllo sicuro più breve dopo l'aggiornamento del Gateway o della VM:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw nodes status --connectedopenclaw nodes invoke \  --node parallels-macos \  --command googlemeet.chrome \  --params '{"action":"setup"}'
[/code]

Questo dimostra che il Plugin Gateway è caricato, il nodo VM è connesso con il token corrente e il bridge audio Meet è disponibile prima che un agente apra una vera scheda riunione.

Per uno smoke Twilio, usa una riunione che espone i dettagli di accesso telefonico:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --pin 123456
[/code]

Stato Twilio atteso:

  * `googlemeet setup` include controlli verdi `twilio-voice-call-plugin`, `twilio-voice-call-credentials` e `twilio-voice-call-webhook`.
  * `voicecall` è disponibile nella CLI dopo il ricaricamento del Gateway.
  * La sessione restituita ha `transport: "twilio"` e un `twilio.voiceCallId`.
  * `openclaw logs --follow` mostra il TwiML DTMF servito prima del TwiML realtime, quindi un bridge realtime con il saluto iniziale in coda.
  * `googlemeet leave <sessionId>` termina la chiamata vocale delegata.


## Risoluzione dei problemi

### L'agente non vede lo strumento Google Meet

Conferma che il Plugin sia abilitato nella configurazione del Gateway e ricarica il Gateway:

bashCopy code
[code]
    openclaw plugins list | grep google-meetopenclaw googlemeet setup
[/code]

Se hai appena modificato `plugins.entries.google-meet`, riavvia o ricarica il Gateway. L'agente in esecuzione vede solo gli strumenti Plugin registrati dal processo Gateway corrente.

Sugli host Gateway non macOS, lo strumento rivolto all'agente `google_meet` resta visibile, ma le azioni di risposta audio con Chrome locale vengono bloccate prima di raggiungere il bridge audio. L'audio di risposta con Chrome locale attualmente dipende da `BlackHole 2ch` su macOS, quindi gli agenti Linux dovrebbero usare `mode: "transcribe"`, l'accesso telefonico Twilio o un host `chrome-node` macOS invece del percorso agente predefinito con Chrome locale.

### Nessun nodo compatibile con Google Meet connesso

Sull'host del nodo, esegui:

bashCopy code
[code]
    openclaw plugins enable google-meetopenclaw plugins enable browserOPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node run --host <gateway-lan-ip> --port 18789 --display-name parallels-macos
[/code]

Sull'host Gateway, approva il nodo e verifica i comandi:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>openclaw nodes status
[/code]

Il nodo deve essere connesso ed elencare `googlemeet.chrome` più `browser.proxy`. La configurazione Gateway deve consentire quei comandi del nodo:

json5Copy code
[code]
    {  gateway: {    nodes: {      allowCommands: ["browser.proxy", "googlemeet.chrome"],    },  },}
[/code]

Se `googlemeet setup` fallisce su `chrome-node-connected` o il log del Gateway segnala `gateway token mismatch`, reinstalla o riavvia il nodo con il token Gateway corrente. Per un Gateway LAN questo di solito significa:

bashCopy code
[code]
    OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node install \  --host <gateway-lan-ip> \  --port 18789 \  --display-name parallels-macos \  --force
[/code]

Poi ricarica il servizio del nodo ed esegui di nuovo:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw nodes status --connected
[/code]

### Il browser si apre ma l'agente non riesce a entrare

Esegui `googlemeet test-listen` per accessi in sola osservazione o `googlemeet test-speech` per accessi realtime, quindi ispeziona lo stato di salute di Chrome restituito. Se una delle due sonde segnala `manualActionRequired: true`, mostra `manualActionMessage` all'operatore e smetti di riprovare finché l'azione nel browser non è completata.

Azioni manuali comuni:

  * Accedi al profilo Chrome.
  * Ammetti l'ospite dall'account host di Meet.
  * Concedi a Chrome le autorizzazioni per microfono/fotocamera quando compare il prompt di autorizzazione nativo di Chrome.
  * Chiudi o ripara una finestra di dialogo di autorizzazione Meet bloccata.


Non segnalare "accesso non effettuato" solo perché Meet mostra "Do you want people to hear you in the meeting?" Quello è l'interstiziale di scelta audio di Meet; OpenClaw fa clic su **Use microphone** tramite automazione del browser quando disponibile e continua ad attendere il vero stato della riunione. Per il fallback browser di sola creazione, OpenClaw può fare clic su **Continue without microphone** perché la creazione dell'URL non richiede il percorso audio realtime.

### Creazione della riunione non riuscita

`googlemeet create` usa prima l'endpoint Google Meet API `spaces.create` quando sono configurate credenziali OAuth. Senza credenziali OAuth, ripiega sul browser del nodo Chrome fissato. Conferma:

  * Per la creazione tramite API: `oauth.clientId` e `oauth.refreshToken` sono configurati, oppure sono presenti variabili di ambiente `OPENCLAW_GOOGLE_MEET_*` corrispondenti.
  * Per la creazione tramite API: il token di aggiornamento è stato emesso dopo l'aggiunta del supporto alla creazione. I token più vecchi potrebbero non avere lo scope `meetings.space.created`; riesegui `openclaw googlemeet auth login --json` e aggiorna la configurazione del Plugin.
  * Per il fallback browser: `defaultTransport: "chrome-node"` e `chromeNode.node` puntano a un nodo connesso con `browser.proxy` e `googlemeet.chrome`.
  * Per il fallback browser: il profilo Chrome OpenClaw su quel nodo ha effettuato l'accesso a Google e può aprire `https://meet.google.com/new`.
  * Per il fallback browser: i tentativi riutilizzano una scheda esistente `https://meet.google.com/new` o una scheda di prompt dell'account Google prima di aprire una nuova scheda. Se un agente va in timeout, riprova la chiamata allo strumento invece di aprire manualmente un'altra scheda Meet.
  * Per il fallback browser: se lo strumento restituisce `manualActionRequired: true`, usa `browser.nodeId`, `browser.targetId`, `browserUrl` e `manualActionMessage` restituiti per guidare l'operatore. Non riprovare in ciclo finché quell'azione non è completata.
  * Per il fallback browser: se Meet mostra "Do you want people to hear you in the meeting?", lascia la scheda aperta. OpenClaw dovrebbe fare clic su **Use microphone** o, per il fallback di sola creazione, su **Continue without microphone** tramite automazione del browser e continuare ad attendere l'URL Meet generato. Se non può farlo, l'errore dovrebbe menzionare `meet-audio-choice-required`, non `google-login-required`.


### L'agente entra ma non parla

Controlla il percorso realtime:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw googlemeet doctor
[/code]

Usa `mode: "agent"` per il normale percorso di risposta audio STT -> agente OpenClaw -> TTS, oppure `mode: "bidi"` per il fallback vocale realtime diretto. `mode: "transcribe"` intenzionalmente non avvia il bridge di risposta audio. Per il debug in sola osservazione, esegui `openclaw googlemeet status --json <session-id>` dopo che i partecipanti parlano e controlla `captioning`, `transcriptLines` e `lastCaptionText`. Se `inCall` è true ma `transcriptLines` resta a `0`, i sottotitoli di Meet potrebbero essere disabilitati, nessuno ha parlato da quando l'osservatore è stato installato, l'interfaccia utente di Meet è cambiata o i sottotitoli live non sono disponibili per la lingua o l'account della riunione.

`googlemeet test-speech` controlla sempre il percorso realtime e segnala se per quella invocazione sono stati osservati byte di output del bridge. Se `speechOutputVerified` è false e `speechOutputTimedOut` è true, il provider realtime potrebbe aver accettato l'enunciato, ma OpenClaw non ha visto nuovi byte di output raggiungere il bridge audio Chrome.

Verifica anche:

  * Una chiave provider realtime è disponibile sull'host Gateway, come `OPENAI_API_KEY` o `GEMINI_API_KEY`.
  * `BlackHole 2ch` è visibile sull'host Chrome.
  * `sox` esiste sull'host Chrome.
  * Il microfono e l'altoparlante Meet sono instradati attraverso il percorso audio virtuale usato da OpenClaw. `doctor` dovrebbe mostrare `meet output routed: yes` per accessi realtime con Chrome locale.


`googlemeet doctor [session-id]` stampa la sessione, il nodo, lo stato in chiamata, il motivo dell'azione manuale, la connessione al provider realtime, `realtimeReady`, l'attività audio in input/output, gli ultimi timestamp audio, i contatori di byte e l'URL del browser. Usa `googlemeet status [session-id] --json` quando ti serve il JSON grezzo. Usa `googlemeet doctor --oauth` quando devi verificare l'aggiornamento OAuth di Google Meet senza esporre token; aggiungi `--meeting` o `--create-space` quando ti serve anche una prova Google Meet API.

Se un agente è andato in timeout e puoi vedere una scheda Meet già aperta, ispeziona quella scheda senza aprirne un'altra:

bashCopy code
[code]
    openclaw googlemeet recover-tabopenclaw googlemeet recover-tab https://meet.google.com/abc-defg-hij
[/code]

L'azione strumento equivalente è `recover_current_tab`. Porta in primo piano e ispeziona una scheda Meet esistente per il trasporto selezionato. Con `chrome`, usa il controllo del browser locale tramite il Gateway; con `chrome-node`, usa il nodo Chrome configurato. Non apre una nuova scheda né crea una nuova sessione; segnala il blocco corrente, come stato di accesso, ammissione, autorizzazioni o scelta audio. Il comando CLI parla con il Gateway configurato, quindi il Gateway deve essere in esecuzione; `chrome-node` richiede anche che il nodo Chrome sia connesso.

### I controlli di configurazione Twilio falliscono

`twilio-voice-call-plugin` fallisce quando `voice-call` non è consentito o non è abilitato. Aggiungilo a `plugins.allow`, abilita `plugins.entries.voice-call` e ricarica il Gateway.

`twilio-voice-call-credentials` fallisce quando nel backend Twilio mancano account SID, token di autenticazione o numero chiamante. Impostali sull'host Gateway:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID=AC...export TWILIO_AUTH_TOKEN=...export TWILIO_FROM_NUMBER=+15550001234
[/code]

`twilio-voice-call-webhook` fallisce quando `voice-call` non ha esposizione Webhook pubblica, o quando `publicUrl` punta a local loopback o a spazio di rete privata. Imposta `plugins.entries.voice-call.config.publicUrl` sull'URL pubblico del provider oppure configura un'esposizione tunnel/Tailscale per `voice-call`.

Gli URL loopback e privati non sono validi per i callback dei carrier. Non usare `localhost`, `127.0.0.1`, `0.0.0.0`, `10.x`, `172.16.x`-`172.31.x`, `192.168.x`, `169.254.x`, `fc00::/7` o `fd00::/8` come `publicUrl`.

Per un URL pubblico stabile:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          fromNumber: "+15550001234",          publicUrl: "https://voice.example.com/voice/webhook",        },      },    },  },}
[/code]

Per lo sviluppo locale, usa un tunnel o un'esposizione Tailscale invece di un URL host privato:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          tunnel: { provider: "ngrok" },          // or          tailscale: { mode: "funnel", path: "/voice/webhook" },        },      },    },  },}
[/code]

Poi riavvia o ricarica il Gateway ed esegui:

bashCopy code
[code]
    openclaw googlemeet setup --transport twilioopenclaw voicecall setupopenclaw voicecall smoke
[/code]

`voicecall smoke` per impostazione predefinita verifica solo la prontezza. Per simulare l'esecuzione con un numero specifico:

bashCopy code
[code]
    openclaw voicecall smoke --to "+15555550123"
[/code]

Aggiungi `--yes` solo quando vuoi intenzionalmente effettuare una chiamata di notifica in uscita live:

bashCopy code
[code]
    openclaw voicecall smoke --to "+15555550123" --yes
[/code]

### La chiamata Twilio parte ma non entra mai nella riunione

Conferma che l'evento Meet esponga i dettagli di accesso telefonico. Passa il numero di accesso esatto e il PIN oppure una sequenza DTMF personalizzata:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --dtmf-sequence ww123456#
[/code]

Usa `w` iniziali o virgole in `--dtmf-sequence` se il provider richiede una pausa prima di inserire il PIN.

Se la chiamata telefonica viene creata ma l'elenco partecipanti di Meet non mostra mai il partecipante in accesso telefonico:

  * Esegui `openclaw googlemeet doctor <session-id>` per confermare l'ID della chiamata Twilio delegata, se il DTMF è stato accodato e se è stato richiesto il saluto introduttivo.
  * Esegui `openclaw voicecall status --call-id <id>` e conferma che la chiamata sia ancora attiva.
  * Esegui `openclaw voicecall tail` e verifica che i Webhook Twilio arrivino al Gateway.
  * Esegui `openclaw logs --follow` e cerca la sequenza Twilio Meet: Google Meet delega l'accesso, Voice Call memorizza e serve il TwiML DTMF pre-connessione, Voice Call serve il TwiML realtime per la chiamata Twilio, quindi Google Meet richiede il parlato introduttivo con `voicecall.speak`.
  * Riesegui `openclaw googlemeet setup --transport twilio`; è richiesto un controllo di configurazione riuscito, ma non dimostra che la sequenza del PIN della riunione sia corretta.
  * Conferma che il numero di accesso appartenga allo stesso invito Meet e alla stessa regione del PIN.
  * Aumenta `voiceCall.dtmfDelayMs` rispetto al valore predefinito di 12 secondi se Meet risponde lentamente o se la trascrizione della chiamata mostra ancora il prompt che chiede un PIN dopo l'invio del DTMF pre-connessione.
  * Se il partecipante entra ma non senti il saluto, controlla `openclaw logs --follow` per la richiesta `voicecall.speak` post-DTMF e la riproduzione TTS del flusso multimediale oppure il fallback Twilio `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5`. Se la trascrizione della chiamata contiene ancora "enter the meeting PIN", il tratto telefonico non è ancora entrato nella stanza Meet, quindi i partecipanti alla riunione non sentiranno il parlato.


Se i Webhook non arrivano, esegui prima il debug del Plugin Voice Call: il provider deve raggiungere `plugins.entries.voice-call.config.publicUrl` o il tunnel configurato. Vedi [Risoluzione dei problemi delle chiamate vocali](</it/plugins/voice-call#troubleshooting>).

## Note

L'API multimediale ufficiale di Google Meet è orientata alla ricezione, quindi parlare in una chiamata Meet richiede ancora un percorso partecipante. Questo Plugin mantiene visibile quel confine: Chrome gestisce la partecipazione tramite browser e l'instradamento audio locale; Twilio gestisce la partecipazione tramite accesso telefonico.

Le modalità talk-back di Chrome richiedono `BlackHole 2ch` più una delle seguenti opzioni:

  * `chrome.audioInputCommand` più `chrome.audioOutputCommand`: OpenClaw possiede il bridge e convoglia l'audio in `chrome.audioFormat` tra quei comandi e il provider selezionato. La modalità agent usa trascrizione realtime più TTS regolare; la modalità bidi usa il provider vocale realtime. Il percorso Chrome predefinito è PCM16 a 24 kHz con `chrome.audioBufferBytes: 4096`; G.711 mu-law a 8 kHz resta disponibile per le coppie di comandi legacy.
  * `chrome.audioBridgeCommand`: un comando bridge esterno possiede l'intero percorso audio locale e deve terminare dopo aver avviato o convalidato il proprio daemon. Questo è valido solo per `bidi` perché la modalità `agent` richiede accesso diretto alla coppia di comandi per il TTS.


Quando un agent chiama lo strumento `google_meet` in modalità agent, la sessione del consulente della riunione effettua il fork della trascrizione corrente del chiamante prima di rispondere al parlato dei partecipanti. La sessione Meet rimane comunque separata (`agent:<agentId>:subagent:google-meet:<sessionId>`) così i follow-up della riunione non mutano direttamente la trascrizione del chiamante.

Per un audio duplex pulito, instrada l'output di Meet e il microfono di Meet attraverso dispositivi virtuali separati o un grafo di dispositivi virtuali in stile Loopback. Un singolo dispositivo BlackHole condiviso può far rientrare l'audio degli altri partecipanti nella chiamata.

Con il bridge Chrome a coppia di comandi, `chrome.bargeInInputCommand` può ascoltare un microfono locale separato e cancellare la riproduzione dell'assistente quando l'umano inizia a parlare. Questo mantiene il parlato umano davanti all'output dell'assistente anche quando l'input loopback BlackHole condiviso è temporaneamente soppresso durante la riproduzione dell'assistente. Come `chrome.audioInputCommand` e `chrome.audioOutputCommand`, è un comando locale configurato dall'operatore. Usa un percorso di comando attendibile esplicito o un elenco di argomenti e non puntarlo a script in posizioni non attendibili.

`googlemeet speak` attiva il bridge audio talk-back attivo per una sessione Chrome. `googlemeet leave` arresta quel bridge. Per le sessioni Twilio delegate tramite il Plugin Voice Call, `leave` riaggancia anche la chiamata vocale sottostante. Usa `googlemeet end-active-conference` quando vuoi anche chiudere la conferenza Google Meet attiva per uno spazio gestito tramite API.

## Correlati

  * [Plugin di chiamata vocale](</it/plugins/voice-call>)
  * [Modalità conversazione](</it/nodes/talk>)
  * [Creazione di Plugin](</it/plugins/building-plugins>)


Was this useful?YesNo
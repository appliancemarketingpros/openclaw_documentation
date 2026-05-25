---
title: Skills
source_url: https://docs.openclaw.ai/it/tools/skills
scraped_at: 2026-05-25
---

OpenClaw usa cartelle di skill **compatibili con[AgentSkills](<https://agentskills.io>)** per insegnare all'agente come usare gli strumenti. Ogni skill è una directory contenente un `SKILL.md` con frontmatter YAML e istruzioni. OpenClaw carica le skill incluse più eventuali override locali opzionali e le filtra al momento del caricamento in base ad ambiente, configurazione e presenza dei binari.

## Posizioni e precedenza

OpenClaw carica le skill da queste fonti, **prima la precedenza più alta** :

# | Fonte | Percorso  
---|---|---  
1 | Skill del workspace | `<workspace>/skills`  
2 | Skill agente progetto | `<workspace>/.agents/skills`  
3 | Skill agente personali | `~/.agents/skills`  
4 | Skill gestite/locali | `~/.openclaw/skills`  
5 | Skill incluse | fornite con l'installazione  
6 | Cartelle skill extra | `skills.load.extraDirs` (config)  
  
Se il nome di una skill va in conflitto, vince la fonte più alta.

La directory nativa `$CODEX_HOME/skills` della CLI Codex non è una di queste radici di skill OpenClaw. In modalità harness Codex, gli avvii locali dell'app-server usano home Codex isolate per agente, quindi le skill personali della CLI Codex non vengono caricate implicitamente. Usa `openclaw migrate codex --dry-run` per inventariarle e `openclaw migrate codex` per scegliere le directory delle skill con un prompt interattivo a caselle di controllo prima di copiarle nel workspace dell'agente OpenClaw corrente. Per esecuzioni non interattive, ripeti `--skill <name>` per le skill esatte da copiare.

## Skill per agente e condivise

Nelle configurazioni **multi-agente** ogni agente ha il proprio workspace:

Ambito | Percorso | Visibile a  
---|---|---  
Per agente | `<workspace>/skills` | Solo quell'agente  
Agente progetto | `<workspace>/.agents/skills` | Solo l'agente di quel workspace  
Agente personale | `~/.agents/skills` | Tutti gli agenti su quella macchina  
Gestite/locali condivise | `~/.openclaw/skills` | Tutti gli agenti su quella macchina  
Directory extra condivise | `skills.load.extraDirs` (precedenza più bassa) | Tutti gli agenti su quella macchina  
  
Stesso nome in più posizioni → vince la fonte più alta. Il workspace batte agente progetto, batte agente personale, batte gestite/locali, batte incluse, batte directory extra.

## Allowlist delle skill agente

La **posizione** della skill e la **visibilità** della skill sono controlli separati. Posizione/precedenza decide quale copia di una skill con lo stesso nome vince; le allowlist dell'agente decidono quali skill un agente può effettivamente usare.

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // eredita github, weather      { id: "docs", skills: ["docs-search"] }, // sostituisce i valori predefiniti      { id: "locked-down", skills: [] }, // nessuna skill    ],  },}
[/code]

Regole allowlist

  * Ometti `agents.defaults.skills` per skill senza restrizioni per impostazione predefinita.
  * Ometti `agents.list[].skills` per ereditare `agents.defaults.skills`.
  * Imposta `agents.list[].skills: []` per nessuna skill.
  * Un elenco `agents.list[].skills` non vuoto è l'insieme **finale** per quell'agente - non viene unito ai valori predefiniti.
  * L'allowlist effettiva si applica a costruzione dei prompt, scoperta degli slash-command delle skill, sincronizzazione sandbox e snapshot delle skill.


## Plugin e skill

I Plugin possono fornire le proprie skill elencando le directory `skills` in `openclaw.plugin.json` (percorsi relativi alla radice del plugin). Le skill del Plugin vengono caricate quando il Plugin è abilitato. Questo è il posto giusto per guide operative specifiche degli strumenti che sono troppo lunghe per la descrizione dello strumento ma dovrebbero essere disponibili ogni volta che il Plugin è installato - per esempio, il plugin browser fornisce una skill `browser-automation` per il controllo browser in più passaggi.

Le directory delle skill del Plugin vengono unite nello stesso percorso a bassa precedenza di `skills.load.extraDirs`, quindi una skill inclusa, gestita, agente o workspace con lo stesso nome le sovrascrive. Puoi condizionarle tramite `metadata.openclaw.requires.config` sulla voce di configurazione del Plugin.

Vedi [Plugin](</it/tools/plugin>) per scoperta/configurazione e [Strumenti](</it/tools>) per la superficie degli strumenti che quelle skill insegnano.

## Workshop skill

Il Plugin **Workshop skill** opzionale e sperimentale può creare o aggiornare skill del workspace da procedure riutilizzabili osservate durante il lavoro dell'agente. È disabilitato per impostazione predefinita e deve essere abilitato esplicitamente tramite `plugins.entries.skill-workshop`.

Workshop skill scrive solo in `<workspace>/skills`, scansiona il contenuto generato, supporta approvazione in sospeso o scritture sicure automatiche, mette in quarantena proposte non sicure e aggiorna lo snapshot delle skill dopo scritture riuscite, così le nuove skill diventano disponibili senza riavviare il Gateway.

Usalo per correzioni come _"la prossima volta, verifica l'attribuzione GIF"_ o workflow conquistati con fatica come checklist QA media. Inizia con approvazione in sospeso; usa le scritture automatiche solo in workspace attendibili dopo averne esaminato le proposte. Guida completa: [Plugin Workshop skill](</it/plugins/skill-workshop>).

## ClawHub (installazione e sincronizzazione)

[ClawHub](<https://clawhub.ai>) è il registro pubblico delle skill per OpenClaw. Usa i comandi nativi `openclaw skills` per scoprire/installare/aggiornare, oppure la CLI separata `clawhub` per workflow di pubblicazione/sincronizzazione. Guida completa: [ClawHub](</it/clawhub>).

Azione | Comando  
---|---  
Installa una skill nel workspace | `openclaw skills install <skill-slug>`  
Aggiorna tutte le skill installate | `openclaw skills update --all`  
Sincronizza (scansione + pubblicazione aggiornamenti) | `clawhub sync --all`  
  
`openclaw skills install` nativo installa nella directory `skills/` del workspace attivo. Anche la CLI separata `clawhub` installa in `./skills` sotto la directory di lavoro corrente (oppure ripiega sul workspace OpenClaw configurato). OpenClaw la rileva come `<workspace>/skills` nella sessione successiva. Le radici skill configurate supportano anche un livello di raggruppamento, come `skills/<group>/<skill>/SKILL.md`, così skill di terze parti correlate possono essere mantenute sotto una cartella condivisa senza scansione ricorsiva ampia.

I client Gateway che necessitano di distribuzione privata non ClawHub possono preparare un archivio zip di skill con `skills.upload.begin`, `skills.upload.chunk` e `skills.upload.commit`, quindi installare l'upload confermato con `skills.install({ source: "upload", uploadId, slug, force?, sha256? })`. Questo è un percorso esplicito di upload amministrativo per client attendibili, non il normale flusso `openclaw skills install <slug>` o di installazione ClawHub. È disattivato per impostazione predefinita e funziona solo quando `skills.install.allowUploadedArchives: true` è impostato in `openclaw.json`. La modalità upload installa comunque nella directory predefinita del workspace agente `skills/<slug>`; il nome della cartella interna dell'archivio viene ignorato per il target di installazione finale.

Le pagine skill ClawHub espongono lo stato dell'ultima scansione di sicurezza prima dell'installazione, con pagine di dettaglio scanner per VirusTotal, ClawScan e analisi statica. `openclaw skills install <slug>` resta solo il percorso di installazione; i publisher recuperano i falsi positivi tramite la dashboard ClawHub o `clawhub skill rescan <slug>`.

## Sicurezza

  * La scoperta di skill workspace ed extra-dir accetta solo radici skill e file `SKILL.md` il cui realpath risolto rimane dentro la radice configurata.
  * Le installazioni Gateway di archivi privati sono disattivate per impostazione predefinita. Quando abilitate esplicitamente, richiedono un upload zip confermato contenente `SKILL.md` e riutilizzano le stesse protezioni di estrazione archivio, path traversal, symlink, force e rollback delle installazioni skill ClawHub. Sono protette da `skills.install.allowUploadedArchives`; le normali installazioni ClawHub non richiedono quell'impostazione.
  * Le installazioni di dipendenze skill supportate da Gateway (`skills.install`, onboarding e l'interfaccia impostazioni Skills) eseguono lo scanner integrato per codice pericoloso prima di eseguire i metadati dell'installer. I risultati `critical` bloccano per impostazione predefinita a meno che il chiamante non imposti esplicitamente l'override pericoloso; i risultati sospetti continuano solo ad avvisare.
  * `openclaw skills install <slug>` è diverso - scarica una cartella skill ClawHub nel workspace e non usa il percorso dei metadati dell'installer sopra.
  * `skills.entries.*.env` e `skills.entries.*.apiKey` iniettano segreti nel processo **host** per quel turno dell'agente (non nella sandbox). Tieni i segreti fuori da prompt e log.


Per un modello di minaccia più ampio e checklist, vedi [Sicurezza](</it/gateway/security>).

## Formato [SKILL.md](<http://SKILL.md>)

`SKILL.md` deve includere almeno:

markdownCopy code
[code]
    ---name: image-labdescription: Generate or edit images via a provider-backed image workflow---
[/code]

OpenClaw segue la specifica AgentSkills per layout/intento. Il parser usato dall'agente incorporato supporta solo chiavi frontmatter **su riga singola** ; `metadata` dovrebbe essere un **oggetto JSON su riga singola**. Usa `{baseDir}` nelle istruzioni per fare riferimento al percorso della cartella della skill.

### Chiavi frontmatter opzionali

URL mostrato come "Sito web" nell'interfaccia Skills di macOS. Supportato anche tramite `metadata.openclaw.homepage`.

Quando `true`, la skill viene esposta come slash command utente.

Quando `true`, OpenClaw tiene le istruzioni della skill fuori dal normale prompt dell'agente. La skill rimane installata e può comunque essere eseguita esplicitamente come slash command quando anche `user-invocable` è `true`.

Quando impostato a `tool`, lo slash command bypassa il modello e invia direttamente a uno strumento.

Nome dello strumento da invocare quando `command-dispatch: tool` è impostato.

Per il dispatch allo strumento, inoltra la stringa args grezza allo strumento (nessun parsing core). Lo strumento viene invocato con `{ command: "<raw args>", commandName: "<slash command>", skillName: "<skill name>" }`.

## Gating (filtri al caricamento)

OpenClaw filtra le skill al momento del caricamento usando `metadata` (JSON su riga singola):

markdownCopy code
[code]
    ---name: image-labdescription: Generate or edit images via a provider-backed image workflowmetadata:  {    "openclaw":      {        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"], "config": ["browser.enabled"] },        "primaryEnv": "GEMINI_API_KEY",      },  }---
[/code]

Campi sotto `metadata.openclaw`:

Quando `true`, includi sempre la skill (saltando gli altri gate).

Emoji facoltativa usata dall'interfaccia utente Skills di macOS.

URL facoltativo mostrato come "Sito web" nell'interfaccia utente Skills di macOS.

Elenco facoltativo di piattaforme. Se impostato, la skill è idonea solo su quei sistemi operativi.

Ognuno deve esistere in `PATH`.

Almeno uno deve esistere in `PATH`.

La variabile di ambiente deve esistere o essere fornita nella configurazione.

Elenco di percorsi `openclaw.json` che devono essere truthy.

Nome della variabile di ambiente associata a `skills.entries.<name>.apiKey`.

Specifiche di installazione facoltative usate dall'interfaccia utente Skills di macOS (brew/node/go/uv/download).

Se non è presente `metadata.openclaw`, la skill è sempre idonea (a meno che non sia disabilitata nella configurazione o bloccata da `skills.allowBundled` per le skill in bundle).

### Note sul sandboxing

  * `requires.bins` viene controllato sull'**host** al momento del caricamento della skill.
  * Se un agente è in sandbox, il binario deve esistere anche **all'interno del container**. Installalo tramite `agents.defaults.sandbox.docker.setupCommand` (o un'immagine personalizzata). `setupCommand` viene eseguito una volta dopo la creazione del container. Anche le installazioni dei pacchetti richiedono egress di rete, un file system root scrivibile e un utente root nella sandbox.
  * Esempio: la skill `summarize` (`skills/summarize/SKILL.md`) richiede la CLI `summarize` nel container sandbox per essere eseguita lì.


### Specifiche di installazione

markdownCopy code
[code]
    ---name: geminidescription: Use Gemini CLI for coding assistance and Google search lookups.metadata:  {    "openclaw":      {        "emoji": "♊️",        "requires": { "bins": ["gemini"] },        "install":          [            {              "id": "brew",              "kind": "brew",              "formula": "gemini-cli",              "bins": ["gemini"],              "label": "Install Gemini CLI (brew)",            },          ],      },  }---
[/code]

Regole di selezione dell'installer

  * Se sono elencati più installer, il gateway sceglie una singola opzione preferita (brew quando disponibile, altrimenti node).
  * Se tutti gli installer sono `download`, OpenClaw elenca ogni voce così puoi vedere gli artefatti disponibili.
  * Le specifiche di installazione possono includere `os: ["darwin"|"linux"|"win32"]` per filtrare le opzioni per piattaforma.
  * Le installazioni Node rispettano `skills.install.nodeManager` in `openclaw.json` (predefinito: npm; opzioni: npm/pnpm/yarn/bun). Questo influisce solo sulle installazioni delle skill; il runtime Gateway deve comunque essere Node - Bun non è consigliato per WhatsApp/Telegram.
  * La selezione dell'installer supportata dal Gateway è basata sulle preferenze: quando le specifiche di installazione mescolano tipi diversi, OpenClaw preferisce Homebrew quando `skills.install.preferBrew` è abilitato e `brew` esiste, poi `uv`, poi il gestore node configurato, poi altri fallback come `go` o `download`.
  * Se ogni specifica di installazione è `download`, OpenClaw mostra tutte le opzioni di download invece di ridurle a un solo installer preferito.

Dettagli per installer

  * **Installazioni Go:** se `go` manca e `brew` è disponibile, il gateway installa prima Go tramite Homebrew e imposta `GOBIN` sul `bin` di Homebrew quando possibile.
  * **Installazioni tramite download:** `url` (obbligatorio), `archive` (`tar.gz` | `tar.bz2` | `zip`), `extract` (predefinito: auto quando viene rilevato un archivio), `stripComponents`, `targetDir` (predefinito: `~/.openclaw/tools/<skillKey>`).


## Override di configurazione

Le skill in bundle e gestite possono essere attivate/disattivate e ricevere valori di ambiente sotto `skills.entries` in `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  skills: {    entries: {      "image-lab": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" }, // or plaintext string        env: {          GEMINI_API_KEY: "GEMINI_KEY_HERE",        },        config: {          endpoint: "https://example.invalid",          model: "nano-pro",        },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

`false` disabilita la skill anche se è in bundle o installata. La skill in bundle `coding-agent` è opt-in: imposta `skills.entries.coding-agent.enabled: true` prima di esporla agli agenti, poi assicurati che uno tra `claude`, `codex`, `opencode` o `pi` sia installato e autenticato per la propria CLI.

Scorciatoia per le skill che dichiarano `metadata.openclaw.primaryEnv`. Supporta testo in chiaro o SecretRef.

Contenitore facoltativo per campi personalizzati per singola skill. Le chiavi personalizzate devono trovarsi qui.

Allowlist facoltativa solo per le skill **in bundle**. Se impostata, sono idonee solo le skill in bundle presenti nell'elenco (le skill gestite/workspace non sono interessate).

Se il nome della skill contiene trattini, metti la chiave tra virgolette (JSON5 consente chiavi tra virgolette). Le chiavi di configurazione corrispondono al **nome della skill** per impostazione predefinita - se una skill definisce `metadata.openclaw.skillKey`, usa quella chiave sotto `skills.entries`.

## Inserimento dell'ambiente

Quando inizia un'esecuzione dell'agente, OpenClaw:

  1. Legge i metadati della skill.
  2. Applica `skills.entries.<key>.env` e `skills.entries.<key>.apiKey` a `process.env`.
  3. Costruisce il prompt di sistema con le skill **idonee**.
  4. Ripristina l'ambiente originale al termine dell'esecuzione.


L'inserimento dell'ambiente è **limitato all'esecuzione dell'agente** , non è un ambiente shell globale.

Per il backend in bundle `claude-cli`, OpenClaw materializza anche lo stesso snapshot idoneo come Plugin temporaneo di Claude Code e lo passa con `--plugin-dir`. Claude Code può quindi usare il proprio risolutore nativo delle skill mentre OpenClaw continua a gestire precedenza, allowlist per agente, gating e inserimento di variabili di ambiente/chiavi API `skills.entries.*`. Gli altri backend CLI usano solo il catalogo del prompt.

## Snapshot e aggiornamento

OpenClaw crea snapshot delle skill idonee **quando una sessione inizia** e riutilizza tale elenco per i turni successivi nella stessa sessione. Le modifiche a skill o configurazione hanno effetto alla successiva nuova sessione.

Le skill possono aggiornarsi a metà sessione in due casi:

  * Il watcher delle skill è abilitato.
  * Compare un nuovo nodo remoto idoneo.


Pensalo come un **hot reload** : l'elenco aggiornato viene acquisito al turno successivo dell'agente. Se l'allowlist effettiva delle skill dell'agente cambia per quella sessione, OpenClaw aggiorna lo snapshot in modo che le skill visibili restino allineate con l'agente corrente.

### Watcher Skills

Per impostazione predefinita, OpenClaw osserva le cartelle delle skill e aggiorna lo snapshot delle skill quando i file `SKILL.md` cambiano. Configura sotto `skills.load`:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/agent-scripts/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],      watch: true,      watchDebounceMs: 250,    },  },}
[/code]

Usa `allowSymlinkTargets` per layout intenzionali con repository adiacenti in cui una radice di skill integrata contiene un symlink, per esempio `~/.agents/skills/manager -> ~/Projects/manager/skills`. L'elenco dei target viene confrontato dopo la risoluzione realpath e deve restare ristretto.

### Nodi macOS remoti (Gateway Linux)

Se il Gateway viene eseguito su Linux ma è connesso un **nodo macOS** con `system.run` consentito (sicurezza delle approvazioni Exec non impostata su `deny`), OpenClaw può considerare idonee le skill solo macOS quando i binari richiesti sono presenti su quel nodo. L'agente deve eseguire quelle skill tramite lo strumento `exec` con `host=node`.

Questo si basa sul fatto che il nodo segnali il proprio supporto ai comandi e su una verifica dei binari tramite `system.which` o `system.run`. I nodi offline **non** rendono visibili le skill solo remote. Se un nodo connesso smette di rispondere alle verifiche dei binari, OpenClaw cancella le corrispondenze dei binari nella cache, così gli agenti non vedono più skill che al momento non possono essere eseguite lì.

## Impatto sui token

Quando le skill sono idonee, OpenClaw inserisce nel prompt di sistema un elenco XML compatto delle skill disponibili (tramite `formatSkillsForPrompt` in `pi-coding-agent`). Il costo è deterministico:

  * **Overhead di base** (solo quando ≥1 skill): 195 caratteri.
  * **Per skill:** 97 caratteri + la lunghezza dei valori XML-escaped `<name>`, `<description>` e `<location>`.


Formula (caratteri):

textCopy code
[code]
    total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
[/code]

L'escape XML espande `& < > " '` in entità (`&amp;`, `&lt;`, ecc.), aumentando la lunghezza. Il conteggio dei token varia in base al tokenizer del modello. Una stima approssimativa in stile OpenAI è ~4 caratteri/token, quindi **97 caratteri ≈ 24 token** per skill più le lunghezze effettive dei campi.

## Ciclo di vita delle skill gestite

OpenClaw include un set di base di skill come **skill in bundle** con l'installazione (pacchetto npm o OpenClaw.app). `~/.openclaw/skills` esiste per override locali - per esempio, fissare o patchare una skill senza modificare la copia in bundle. Le skill del workspace sono di proprietà dell'utente e hanno la precedenza su entrambe in caso di conflitti di nome.

## Cerchi altre skill?

Sfoglia <https://clawhub.ai>. Schema completo di configurazione: [Configurazione Skills](</it/tools/skills-config>).

## Correlati

  * [ClawHub](</it/clawhub>) \- registro pubblico delle skill
  * [Creazione di skill](</it/tools/creating-skills>) \- creazione di skill personalizzate
  * [Plugin](</it/tools/plugin>) \- panoramica del sistema di Plugin
  * [Plugin Skill Workshop](</it/plugins/skill-workshop>) \- genera skill dal lavoro dell'agente
  * [Configurazione Skills](</it/tools/skills-config>) \- riferimento per la configurazione delle skill
  * [Comandi slash](</it/tools/slash-commands>) \- tutti i comandi slash disponibili


Was this useful?YesNo
---
title: Plugin
source_url: https://docs.openclaw.ai/it/cli/plugins
scraped_at: 2026-05-25
---

Gestisci Plugin del Gateway, pacchetti di hook e bundle compatibili.

[**Sistema di Plugin** Guida per utenti finali per installare, abilitare e risolvere problemi dei plugin. ](</it/tools/plugin>) [**Gestire i plugin** Esempi rapidi per installazione, elenco, aggiornamento, disinstallazione e pubblicazione. ](</it/plugins/manage-plugins>) [**Bundle di Plugin** Modello di compatibilità dei bundle. ](</it/plugins/bundles>) [**Manifest del Plugin** Campi del manifest e schema di configurazione. ](</it/plugins/manifest>) [**Sicurezza** Rafforzamento della sicurezza per le installazioni di plugin. ](</it/gateway/security>)

## Comandi

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

Per analizzare installazioni, ispezioni, disinstallazioni o aggiornamenti del registro lenti, esegui il comando con `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`. La traccia scrive i tempi delle fasi su stderr e mantiene analizzabile l'output JSON. Vedi [Debugging](</it/help/debugging#plugin-lifecycle-trace>).

### Installazione

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

I maintainer che testano installazioni in fase di configurazione possono sovrascrivere le sorgenti di installazione automatica dei plugin con variabili d'ambiente protette. Vedi [Sovrascritture dell'installazione dei Plugin](</it/plugins/install-overrides>).

`plugins search` interroga ClawHub per pacchetti di plugin installabili e stampa nomi di pacchetto pronti per l'installazione. Cerca pacchetti code-plugin e bundle-plugin, non Skills. Usa `openclaw skills search` per le Skills di ClawHub.

Inclusioni di configurazione e riparazione di configurazioni non valide

Se la sezione `plugins` è supportata da un `$include` a file singolo, `plugins install/update/enable/disable/uninstall` scrive in quel file incluso e lascia `openclaw.json` invariato. Inclusioni radice, array di inclusioni e inclusioni con sovrascritture sorelle falliscono in modo chiuso invece di essere appiattiti. Vedi [Inclusioni di configurazione](</it/gateway/configuration>) per le forme supportate.

Se la configurazione non è valida durante l'installazione, `plugins install` normalmente fallisce in modo chiuso e ti dice di eseguire prima `openclaw doctor --fix`. Durante l'avvio del Gateway e il ricaricamento a caldo, una configurazione plugin non valida fallisce in modo chiuso come qualsiasi altra configurazione non valida; `openclaw doctor --fix` può mettere in quarantena la voce del plugin non valida. L'unica eccezione documentata in fase di installazione è un percorso ristretto di recupero dei plugin inclusi per i plugin che scelgono esplicitamente `openclaw.install.allowInvalidConfigRecovery`.

\--force e reinstallazione rispetto ad aggiornamento

`--force` riutilizza la destinazione di installazione esistente e sovrascrive sul posto un plugin o un pacchetto di hook già installato. Usalo quando stai intenzionalmente reinstallando lo stesso id da un nuovo percorso locale, archivio, pacchetto ClawHub o artefatto npm. Per gli aggiornamenti di routine di un plugin npm già tracciato, preferisci `openclaw plugins update <id-or-npm-spec>`.

Se esegui `plugins install` per un id plugin già installato, OpenClaw si ferma e ti indirizza a `plugins update <id-or-npm-spec>` per un normale aggiornamento, oppure a `plugins install <package> --force` quando vuoi davvero sovrascrivere l'installazione corrente da una sorgente diversa.

Ambito di --pin

`--pin` si applica solo alle installazioni npm. Non è supportato con installazioni `git:`; usa un ref git esplicito come `git:github.com/acme/plugin@v1.2.3` quando vuoi una sorgente fissata. Non è supportato con `--marketplace`, perché le installazioni marketplace persistono metadati della sorgente marketplace invece di una specifica npm.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` è un'opzione di emergenza per falsi positivi nello scanner integrato di codice pericoloso. Consente all'installazione di continuare anche quando lo scanner integrato segnala risultati `critical`, ma **non** aggira i blocchi delle policy degli hook `before_install` del plugin e **non** aggira i fallimenti della scansione.

Questo flag CLI si applica ai flussi di installazione/aggiornamento dei plugin. Le installazioni delle dipendenze Skills supportate dal Gateway usano la corrispondente sovrascrittura di richiesta `dangerouslyForceUnsafeInstall`, mentre `openclaw skills install` rimane un flusso separato di download/installazione delle Skills di ClawHub.

Se un plugin che hai pubblicato su ClawHub viene bloccato da una scansione del registro, usa i passaggi per publisher in [ClawHub](</it/clawhub/security>).

Pacchetti di hook e specifiche npm

`plugins install` è anche la superficie di installazione per pacchetti di hook che espongono `openclaw.hooks` in `package.json`. Usa `openclaw hooks` per visibilità filtrata degli hook e abilitazione per singolo hook, non per l'installazione dei pacchetti.

Le specifiche npm sono **solo registro** (nome pacchetto + **versione esatta** o **dist-tag** opzionale). Specifiche Git/URL/file e intervalli semver vengono rifiutati. Le installazioni delle dipendenze vengono eseguite localmente al progetto con `--ignore-scripts` per sicurezza, anche quando la tua shell ha impostazioni globali di installazione npm. Le radici npm dei plugin gestiti ereditano gli `overrides` npm a livello di pacchetto di OpenClaw, quindi i pin di sicurezza dell'host si applicano anche alle dipendenze dei plugin issate.

Usa `npm:<package>` quando vuoi rendere esplicita la risoluzione npm. Anche le specifiche di pacchetto semplici installano direttamente da npm durante la transizione di lancio.

Le specifiche semplici e `@latest` restano sul canale stabile. Le versioni di correzione con data di OpenClaw come `2026.5.3-1` sono release stabili per questo controllo. Se npm risolve una di queste a una prerelease, OpenClaw si ferma e ti chiede di aderire esplicitamente con un tag prerelease come `@beta`/`@rc` o una versione prerelease esatta come `@1.2.3-beta.4`.

Se una specifica di installazione semplice corrisponde a un id plugin ufficiale (ad esempio `diffs`), OpenClaw installa direttamente la voce del catalogo. Per installare un pacchetto npm con lo stesso nome, usa una specifica con ambito esplicita (ad esempio `@scope/diffs`).

Repository Git

Usa `git:<repo>` per installare direttamente da un repository git. Le forme supportate includono URL di clone `git:github.com/owner/repo`, `git:owner/repo`, `https://` completo, `ssh://`, `git://`, `file://` e `git@host:owner/repo.git`. Aggiungi `@<ref>` o `#<ref>` per eseguire il checkout di un branch, tag o commit prima dell'installazione.

Le installazioni Git clonano in una directory temporanea, eseguono il checkout del ref richiesto quando presente, poi usano il normale installatore di directory plugin. Ciò significa che validazione del manifest, scansione del codice pericoloso, lavoro di installazione del package manager e record di installazione si comportano come nelle installazioni npm. Le installazioni git registrate includono l'URL/ref della sorgente più il commit risolto, così `openclaw plugins update` può risolvere di nuovo la sorgente in seguito.

Dopo l'installazione da git, usa `openclaw plugins inspect <id> --runtime --json` per verificare le registrazioni runtime come metodi gateway e comandi CLI. Se il plugin ha registrato una radice CLI con `api.registerCli`, esegui quel comando direttamente tramite la CLI radice di OpenClaw, ad esempio `openclaw demo-plugin ping`.

Archivi

Archivi supportati: `.zip`, `.tgz`, `.tar.gz`, `.tar`. Gli archivi di plugin OpenClaw nativi devono contenere un `openclaw.plugin.json` valido nella radice estratta del plugin; gli archivi che contengono solo `package.json` vengono rifiutati prima che OpenClaw scriva i record di installazione.

Usa `npm-pack:<path.tgz>` quando il file è un tarball npm-pack e vuoi testare lo stesso percorso di installazione npm-root gestito usato dalle installazioni da registro, inclusa la verifica di `package-lock.json`, la scansione delle dipendenze issate e i record di installazione npm. I percorsi di archivio semplici installano ancora come archivi locali sotto la radice delle estensioni del plugin.

Sono supportate anche le installazioni dal marketplace Claude.

Le installazioni ClawHub usano un localizzatore esplicito `clawhub:<package>`:

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

Le specifiche di plugin semplici sicure per npm installano da npm per impostazione predefinita durante la transizione di lancio:

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

Usa `npm:` per rendere esplicita la risoluzione solo npm:

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw verifica la compatibilità pubblicizzata dell'API del plugin / Gateway minimo prima dell'installazione. Quando la versione ClawHub selezionata pubblica un artefatto ClawPack, OpenClaw scarica il `.tgz` versionato npm-pack, verifica l'header digest di ClawHub e il digest dell'artefatto, quindi lo installa tramite il normale percorso di archivio. Le versioni ClawHub più vecchie senza metadati ClawPack vengono comunque installate tramite il percorso legacy di verifica dell'archivio del pacchetto. Le installazioni registrate conservano i metadati della loro origine ClawHub, il tipo di artefatto, l'integrità npm, lo shasum npm, il nome del tarball e i fatti del digest ClawPack per aggiornamenti successivi. Le installazioni ClawHub senza versione mantengono una specifica registrata senza versione, così `openclaw plugins update` può seguire le release ClawHub più recenti; i selettori espliciti di versione o tag come `clawhub:pkg@1.2.3` e `clawhub:pkg@beta` restano fissati a quel selettore.

#### Scorciatoia del marketplace

Usa la scorciatoia `plugin@marketplace` quando il nome del marketplace esiste nella cache del registro locale di Claude in `~/.claude/plugins/known_marketplaces.json`:

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

Usa `--marketplace` quando vuoi passare esplicitamente l'origine del marketplace:

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### Origini del marketplace

  * un nome di marketplace noto a Claude da `~/.claude/plugins/known_marketplaces.json`
  * una radice marketplace locale o un percorso `marketplace.json`
  * una scorciatoia di repository GitHub come `owner/repo`
  * un URL di repository GitHub come `https://github.com/owner/repo`
  * un URL git


### Regole per marketplace remoti

Per i marketplace remoti caricati da GitHub o git, le voci dei plugin devono restare all'interno del repository marketplace clonato. OpenClaw accetta origini con percorso relativo da quel repository e rifiuta origini di plugin HTTP(S), con percorso assoluto, git, GitHub e altre origini non basate su percorso dai manifest remoti.

Per percorsi locali e archivi, OpenClaw rileva automaticamente:

  * plugin OpenClaw nativi (`openclaw.plugin.json`)
  * bundle compatibili con Codex (`.codex-plugin/plugin.json`)
  * bundle compatibili con Claude (`.claude-plugin/plugin.json` o il layout predefinito dei componenti Claude)
  * bundle compatibili con Cursor (`.cursor-plugin/plugin.json`)


### Elenco

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

Mostra solo i plugin abilitati.

Passa dalla vista tabellare a righe di dettaglio per plugin con metadati di origine/provenienza/versione/attivazione.

Inventario leggibile dalla macchina più diagnostica del registro e stato di installazione delle dipendenze dei pacchetti.

`plugins search` è una ricerca remota nel catalogo ClawHub. Non ispeziona lo stato locale, non modifica la configurazione, non installa pacchetti e non carica codice runtime del plugin. I risultati di ricerca includono nome pacchetto ClawHub, famiglia, canale, versione, riepilogo e un suggerimento di installazione come `openclaw plugins install clawhub:<package>`.

Per lavorare su plugin in bundle dentro un'immagine Docker pacchettizzata, esegui il bind-mount della directory sorgente del plugin sopra il percorso sorgente pacchettizzato corrispondente, come `/app/extensions/synology-chat`. OpenClaw scoprirà quell'overlay sorgente montato prima di `/app/dist/extensions/synology-chat`; una semplice directory sorgente copiata resta inerte, così le normali installazioni pacchettizzate continuano a usare la dist compilata.

Per il debug degli hook runtime:

  * `openclaw plugins inspect <id> --runtime --json` mostra hook registrati e diagnostica da un passaggio di ispezione con modulo caricato. L'ispezione runtime non installa mai dipendenze; usa `openclaw doctor --fix` per pulire lo stato legacy delle dipendenze o recuperare plugin scaricabili mancanti che sono referenziati dalla configurazione.
  * `openclaw gateway status --deep --require-rpc` conferma il Gateway raggiungibile, suggerimenti su servizio/processo, percorso di configurazione e salute RPC.
  * Gli hook di conversazione non in bundle (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) richiedono `plugins.entries.<id>.hooks.allowConversationAccess=true`.


Usa `--link` per evitare di copiare una directory locale (aggiunge a `plugins.load.paths`):

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Indice dei plugin

I metadati di installazione dei plugin sono stato gestito dalla macchina, non configurazione utente. Installazioni e aggiornamenti li scrivono in `plugins/installs.json` sotto la directory di stato OpenClaw attiva. La sua mappa di primo livello `installRecords` è l'origine durevole dei metadati di installazione, inclusi i record per manifest di plugin rotti o mancanti. L'array `plugins` è la cache del registro a freddo derivata dal manifest. Il file include un avviso di non modifica ed è usato da `openclaw plugins update`, disinstallazione, diagnostica e registro dei plugin a freddo.

Quando OpenClaw vede record legacy distribuiti `plugins.installs` nella configurazione, le letture runtime li trattano come input di compatibilità senza riscrivere `openclaw.json`. Scritture esplicite dei plugin e `openclaw doctor --fix` spostano quei record nell'indice dei plugin e rimuovono la chiave di configurazione quando le scritture della configurazione sono consentite; se una delle scritture fallisce, i record di configurazione vengono mantenuti così i metadati di installazione non vanno persi.

### Disinstallazione

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` rimuove i record dei plugin da `plugins.entries`, dall'indice persistente dei plugin, dalle voci dell'elenco allow/deny dei plugin e dalle voci collegate di `plugins.load.paths` quando applicabile. A meno che `--keep-files` sia impostato, la disinstallazione rimuove anche la directory di installazione gestita tracciata quando si trova dentro la radice delle estensioni plugin di OpenClaw. Per i plugin Active Memory, lo slot di memoria viene reimpostato su `memory-core`.

### Aggiornamento

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

Gli aggiornamenti si applicano alle installazioni di plugin tracciate nell'indice dei plugin gestiti e alle installazioni di hook-pack tracciate in `hooks.internal.installs`.

Risoluzione tra id del plugin e specifica npm

Quando passi un id di plugin, OpenClaw riutilizza la specifica di installazione registrata per quel plugin. Questo significa che i dist-tag memorizzati in precedenza come `@beta` e le versioni esatte fissate continuano a essere usati nelle successive esecuzioni di `update <id>`.

Per le installazioni npm, puoi anche passare una specifica esplicita di pacchetto npm con un dist-tag o una versione esatta. OpenClaw risolve quel nome di pacchetto tornando al record del plugin tracciato, aggiorna quel plugin installato e registra la nuova specifica npm per aggiornamenti futuri basati sull'id.

Passare il nome del pacchetto npm senza versione o tag risolve comunque al record del plugin tracciato. Usalo quando un plugin era fissato a una versione esatta e vuoi riportarlo alla linea di release predefinita del registro.

Aggiornamenti del canale beta

`openclaw plugins update` riutilizza la specifica del plugin tracciata, a meno che tu non passi una nuova specifica. `openclaw update` conosce inoltre il canale di aggiornamento OpenClaw attivo: sul canale beta, i record di plugin npm e ClawHub della linea predefinita provano prima `@beta`, poi ripiegano sulla specifica predefinita/latest registrata se non esiste alcuna release beta del plugin. Quel fallback viene riportato come avviso e non fa fallire l'aggiornamento core. Versioni esatte e tag espliciti restano fissati a quel selettore.

Controlli di versione e deriva dell'integrità

Prima di un aggiornamento npm live, OpenClaw controlla la versione del pacchetto installato rispetto ai metadati del registro npm. Se la versione installata e l'identità dell'artefatto registrata corrispondono già alla destinazione risolta, l'aggiornamento viene saltato senza scaricare, reinstallare o riscrivere `openclaw.json`.

Quando esiste un hash di integrità memorizzato e l'hash dell'artefatto recuperato cambia, OpenClaw lo tratta come deriva dell'artefatto npm. Il comando interattivo `openclaw plugins update` stampa gli hash atteso e reale e chiede conferma prima di procedere. Gli helper di aggiornamento non interattivi falliscono in modo chiuso a meno che il chiamante fornisca una policy esplicita di continuazione.

\--dangerously-force-unsafe-install in update

`--dangerously-force-unsafe-install` è disponibile anche in `plugins update` come override di emergenza per falsi positivi della scansione del codice pericoloso integrata durante gli aggiornamenti dei plugin. Continua a non bypassare i blocchi di policy `before_install` dei plugin o il blocco per fallimento della scansione, e si applica solo agli aggiornamenti dei plugin, non agli aggiornamenti degli hook-pack.

### Ispezione

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect mostra identità, stato di caricamento, origine, capacità del manifest, flag di policy, diagnostica, metadati di installazione, capacità del bundle ed eventuale supporto rilevato per server MCP o LSP senza importare per impostazione predefinita il runtime del plugin. Aggiungi `--runtime` per caricare il modulo del plugin e includere hook, strumenti, comandi, servizi, metodi Gateway e route HTTP registrati. L'ispezione runtime riporta direttamente le dipendenze mancanti del plugin; installazioni e riparazioni restano in `openclaw plugins install`, `openclaw plugins update` e `openclaw doctor --fix`.

I comandi CLI posseduti dal plugin sono di solito installati come gruppi di comandi radice `openclaw`, ma i plugin possono anche registrare comandi nidificati sotto un genitore core come `openclaw nodes`. Dopo che `inspect --runtime` mostra un comando sotto `cliCommands`, eseguilo al percorso indicato; per esempio un plugin che registra `demo-git` può essere verificato con `openclaw demo-git ping`.

Ogni plugin è classificato in base a ciò che registra effettivamente a runtime:

  * **plain-capability** — un solo tipo di capacità (ad es. un plugin solo provider)
  * **hybrid-capability** — più tipi di capacità (ad es. testo + voce + immagini)
  * **hook-only** — solo hook, nessuna capacità o superficie
  * **non-capability** — strumenti/comandi/servizi ma nessuna capacità


Consulta [Forme dei Plugin](</it/plugins/architecture#plugin-shapes>) per maggiori informazioni sul modello delle capacità.

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` segnala errori di caricamento dei plugin, diagnostica di manifest/discovery e avvisi di compatibilità. Quando è tutto pulito, stampa `No plugin issues detected.`

Se un plugin configurato è presente su disco ma bloccato dai controlli di sicurezza dei percorsi del loader, la validazione della configurazione conserva la voce del plugin e la segnala come `present but blocked`. Correggi la diagnostica precedente del plugin bloccato, ad esempio proprietà del percorso o permessi world-writable, invece di rimuovere la configurazione `plugins.entries.<id>` o `plugins.allow`.

Per errori di forma del modulo, come export `register`/`activate` mancanti, riesegui con `OPENCLAW_PLUGIN_LOAD_DEBUG=1` per includere un riepilogo compatto della forma degli export nell'output diagnostico.

### Registro

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

Il registro locale dei plugin è il modello di lettura persistente a freddo di OpenClaw per identità dei plugin installati, abilitazione, metadati della sorgente e proprietà dei contributi. Avvio normale, ricerca del proprietario del provider, classificazione della configurazione del canale e inventario dei plugin possono leggerlo senza importare moduli runtime dei plugin.

Usa `plugins registry` per verificare se il registro persistente è presente, aggiornato o obsoleto. Usa `--refresh` per ricostruirlo dall'indice persistente dei plugin, dalla policy di configurazione e dai metadati di manifest/package. Questo è un percorso di riparazione, non un percorso di attivazione runtime.

`openclaw doctor --fix` ripara anche il drift npm gestito adiacente al registro: se un pacchetto `@openclaw/*` orfano o recuperato sotto la root npm gestita dei plugin oscura un plugin in bundle, doctor rimuove quel pacchetto obsoleto e ricostruisce il registro, così l'avvio valida rispetto al manifest in bundle. Doctor ricollega anche il pacchetto host `openclaw` nei plugin npm gestiti che dichiarano `peerDependencies.openclaw`, così gli import runtime locali al pacchetto, come `openclaw/plugin-sdk/*`, si risolvono dopo aggiornamenti o riparazioni npm.

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

Marketplace list accetta un percorso marketplace locale, un percorso `marketplace.json`, una scorciatoia GitHub come `owner/repo`, un URL di repository GitHub o un URL git. `--json` stampa l'etichetta della sorgente risolta più il manifest marketplace analizzato e le voci dei plugin.

## Correlati

  * [Creazione di plugin](</it/plugins/building-plugins>)
  * [Riferimento CLI](</it/cli>)
  * [ClawHub](</it/clawhub>)


Was this useful?YesNo
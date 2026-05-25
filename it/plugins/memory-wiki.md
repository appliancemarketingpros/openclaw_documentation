---
title: Wiki della memoria
source_url: https://docs.openclaw.ai/it/plugins/memory-wiki
scraped_at: 2026-05-25
---

`memory-wiki` è un Plugin incluso che trasforma la memoria durevole in un vault di conoscenza compilato.

Non sostituisce **il Plugin Active Memory**. Il Plugin Active Memory continua a gestire richiamo, promozione, indicizzazione e Dreaming. `memory-wiki` gli si affianca e compila la conoscenza durevole in una wiki navigabile con pagine deterministiche, dichiarazioni strutturate, provenienza, dashboard e digest leggibili dalle macchine.

Usalo quando vuoi che la memoria si comporti più come un livello di conoscenza mantenuto e meno come una pila di file Markdown.

## Cosa aggiunge

  * Un vault wiki dedicato con layout di pagina deterministico
  * Metadati strutturati per dichiarazioni ed evidenze, non solo prosa
  * Provenienza, attendibilità, contraddizioni e domande aperte a livello di pagina
  * Digest compilati per agenti e consumatori runtime
  * Strumenti nativi della wiki per ricerca/lettura/applicazione/lint
  * Modalità bridge opzionale che importa artefatti pubblici dal Plugin Active Memory
  * Modalità di rendering opzionale compatibile con Obsidian e integrazione CLI


## Come si integra con la memoria

Pensa alla separazione così:

Livello | Gestisce  
---|---  
Plugin Active Memory (`memory-core`, QMD, Honcho, ecc.) | Richiamo, ricerca semantica, promozione, Dreaming, runtime della memoria  
`memory-wiki` | Pagine wiki compilate, sintesi ricche di provenienza, dashboard, ricerca/lettura/applicazione specifiche della wiki  
  
Se il Plugin Active Memory espone artefatti di richiamo condivisi, OpenClaw può cercare in entrambi i livelli in un solo passaggio con `memory_search corpus=all`.

Quando ti servono ranking specifico della wiki, provenienza o accesso diretto alle pagine, usa invece gli strumenti nativi della wiki.

## Pattern ibrido consigliato

Un buon valore predefinito per configurazioni local-first è:

  * QMD come backend Active Memory per richiamo e ricerca semantica ampia
  * `memory-wiki` in modalità `bridge` per pagine di conoscenza durevole sintetizzata


Questa separazione funziona bene perché ogni livello resta focalizzato:

  * QMD mantiene ricercabili note grezze, esportazioni di sessione e raccolte aggiuntive
  * `memory-wiki` compila entità stabili, dichiarazioni, dashboard e pagine sorgente


Regola pratica:

  * usa `memory_search` quando vuoi un unico passaggio di richiamo ampio sulla memoria
  * usa `wiki_search` e `wiki_get` quando vuoi risultati wiki consapevoli della provenienza
  * usa `memory_search corpus=all` quando vuoi che la ricerca condivisa copra entrambi i livelli


Se la modalità bridge segnala zero artefatti esportati, il Plugin Active Memory non sta ancora esponendo input bridge pubblici. Esegui prima `openclaw wiki doctor`, poi conferma che il Plugin Active Memory supporti artefatti pubblici.

Quando la modalità bridge è attiva e `bridge.readMemoryArtifacts` è abilitato, `openclaw wiki status`, `openclaw wiki doctor` e `openclaw wiki bridge import` leggono attraverso il Gateway in esecuzione. Questo mantiene i controlli bridge della CLI allineati al contesto runtime del Plugin della memoria. Se bridge è disabilitato o le letture degli artefatti sono disattivate, quei comandi mantengono il loro comportamento locale/offline.

## Modalità del vault

`memory-wiki` supporta tre modalità del vault:

### `isolated`

Vault proprio, sorgenti proprie, nessuna dipendenza da `memory-core`.

Usa questa modalità quando vuoi che la wiki sia il suo archivio di conoscenza curato.

### `bridge`

Legge artefatti di memoria pubblici ed eventi di memoria dal Plugin Active Memory attraverso seam pubblici del plugin SDK.

Usa questa modalità quando vuoi che la wiki compili e organizzi gli artefatti esportati dal Plugin della memoria senza accedere agli internals privati del Plugin.

La modalità bridge può indicizzare:

  * artefatti di memoria esportati
  * report di dream
  * note giornaliere
  * file radice della memoria
  * log degli eventi di memoria


### `unsafe-local`

Escape hatch esplicita per percorsi privati locali sulla stessa macchina.

Questa modalità è intenzionalmente sperimentale e non portabile. Usala solo quando comprendi il confine di fiducia e ti serve specificamente accesso al filesystem locale che la modalità bridge non può fornire.

## Layout del vault

Il Plugin inizializza un vault così:

textCopy code
[code]
    <vault>/  AGENTS.md  WIKI.md  index.md  inbox.md  entities/  concepts/  syntheses/  sources/  reports/  _attachments/  _views/  .openclaw-wiki/
[/code]

Il contenuto gestito resta dentro blocchi generati. I blocchi di note umane sono preservati.

I gruppi di pagine principali sono:

  * `sources/` per materiale grezzo importato e pagine supportate da bridge
  * `entities/` per cose durevoli, persone, sistemi, progetti e oggetti
  * `concepts/` per idee, astrazioni, pattern e policy
  * `syntheses/` per riepiloghi compilati e rollup mantenuti
  * `reports/` per dashboard generate


## Dichiarazioni strutturate ed evidenze

Le pagine possono contenere frontmatter `claims` strutturati, non solo testo libero.

Ogni dichiarazione può includere:

  * `id`
  * `text`
  * `status`
  * `confidence`
  * `evidence[]`
  * `updatedAt`


Le voci di evidenza possono includere:

  * `kind`
  * `sourceId`
  * `path`
  * `lines`
  * `weight`
  * `confidence`
  * `privacyTier`
  * `note`
  * `updatedAt`


Questo fa sì che la wiki agisca più come un livello di convinzioni che come un deposito passivo di note. Le dichiarazioni possono essere tracciate, valutate, contestate e ricondotte alle fonti.

## Metadati di entità rivolti agli agenti

Le pagine entità possono anche contenere metadati di routing per l'uso da parte degli agenti. Questo è frontmatter generico, quindi funziona per persone, team, sistemi, progetti o qualsiasi altro tipo di entità.

I campi comuni includono:

  * `entityType`: ad esempio `person`, `team`, `system` o `project`
  * `canonicalId`: chiave di identità stabile usata tra alias e importazioni
  * `aliases`: nomi, handle o etichette che devono risolversi alla stessa pagina
  * `privacyTier`: `public`, `local-private`, `sensitive` o `confirm-before-use`
  * `bestUsedFor` / `notEnoughFor`: indicazioni compatte di routing
  * `lastRefreshedAt`: timestamp di aggiornamento della sorgente separato dall'orario di modifica della pagina
  * `personCard`: scheda di routing opzionale specifica per persona con handle, social, email, fuso orario, corsia, chiedere-per, evitare-di-chiedere-per, attendibilità e privacy
  * `relationships`: archi tipizzati verso pagine correlate con destinazione, tipo, peso, attendibilità, tipo di evidenza, livello di privacy e nota


Per una wiki delle persone, l'agente dovrebbe di solito iniziare da `reports/person-agent-directory.md`, poi aprire la pagina della persona con `wiki_get` prima di usare dettagli di contatto o fatti inferiti.

Esempio:

yamlCopy code
[code]
    pageType: entityentityType: personid: entity.brad-grouxcanonicalId: maintainer.brad-grouxaliases:  - Brad  - bgrouxprivacyTier: local-privatebestUsedFor:  - Microsoft Teams and Azure routingnotEnoughFor:  - legal approvallastRefreshedAt: "2026-04-29T00:00:00.000Z"personCard:  handles:    - "@bgroux"  socials:    - "https://x.example/bgroux"  emails:    - brad@example.com  timezone: America/Chicago  lane: Microsoft ecosystem  askFor:    - Teams rollout questions  avoidAskingFor:    - unrelated billing decisions  confidence: 0.8  privacyTier: confirm-before-userelationships:  - targetId: entity.alice    targetTitle: Alice    kind: collaborates-with    confidence: 0.7    evidenceKind: discrawl-statclaims:  - id: claim.brad.teams    text: Brad is useful for Microsoft Teams routing.    status: supported    confidence: 0.9    evidence:      - kind: maintainer-whois        sourceId: source.maintainers        privacyTier: local-private
[/code]

## Pipeline di compilazione

Il passaggio di compilazione legge le pagine wiki, normalizza i riepiloghi ed emette artefatti stabili rivolti alle macchine sotto:

  * `.openclaw-wiki/cache/agent-digest.json`
  * `.openclaw-wiki/cache/claims.jsonl`


Questi digest esistono perché agenti e codice runtime non debbano estrarre informazioni dalle pagine Markdown.

L'output compilato alimenta anche:

  * indicizzazione wiki di primo passaggio per flussi search/get
  * lookup degli ID delle dichiarazioni verso le pagine proprietarie
  * supplementi compatti per prompt
  * generazione di report/dashboard


## Dashboard e report di salute

Quando `render.createDashboards` è abilitato, la compilazione mantiene dashboard sotto `reports/`.

I report integrati includono:

  * `reports/open-questions.md`
  * `reports/contradictions.md`
  * `reports/low-confidence.md`
  * `reports/claim-health.md`
  * `reports/stale-pages.md`
  * `reports/person-agent-directory.md`
  * `reports/relationship-graph.md`
  * `reports/provenance-coverage.md`
  * `reports/privacy-review.md`


Questi report tracciano aspetti come:

  * cluster di note di contraddizione
  * cluster di dichiarazioni concorrenti
  * dichiarazioni prive di evidenza strutturata
  * pagine e dichiarazioni a bassa attendibilità
  * freschezza obsoleta o sconosciuta
  * pagine con domande irrisolte
  * schede di routing persona/entità
  * archi di relazione strutturati
  * copertura delle classi di evidenza
  * livelli di privacy non pubblici che richiedono revisione prima dell'uso


## Ricerca e recupero

`memory-wiki` supporta due backend di ricerca:

  * `shared`: usa il flusso di ricerca memoria condiviso quando disponibile
  * `local`: cerca localmente nella wiki


Supporta anche tre corpora:

  * `wiki`
  * `memory`
  * `all`


Comportamento importante:

  * `wiki_search` e `wiki_get` usano digest compilati come primo passaggio quando possibile
  * gli ID delle dichiarazioni possono risolversi alla pagina proprietaria
  * dichiarazioni contestate/obsolete/fresche influenzano il ranking
  * le etichette di provenienza possono sopravvivere nei risultati
  * la modalità di ricerca può orientare il ranking per ricerca persona, routing domande, evidenza sorgente o dichiarazioni grezze


Regola pratica:

  * usa `memory_search corpus=all` per un unico passaggio di richiamo ampio
  * usa `wiki_search` \+ `wiki_get` quando ti interessano ranking specifico della wiki, provenienza o struttura delle convinzioni a livello di pagina


Modalità di ricerca:

  * `auto`: valore predefinito bilanciato
  * `find-person`: dà priorità a entità simili a persone, alias, handle, social e ID canonici
  * `route-question`: dà priorità a schede agente, indicazioni ask-for, indicazioni best-used-for e contesto delle relazioni
  * `source-evidence`: dà priorità a pagine sorgente e metadati di evidenza strutturata
  * `raw-claim`: dà priorità alle dichiarazioni strutturate corrispondenti e restituisce metadati di dichiarazione/evidenza nei risultati


Quando un risultato corrisponde a una dichiarazione strutturata, `wiki_search` può restituire `matchedClaimId`, `matchedClaimStatus`, `matchedClaimConfidence`, `evidenceKinds` e `evidenceSourceIds` nel suo payload di dettagli. L'output testuale include anche righe compatte `Claim:` ed `Evidence:` quando disponibili.

## Strumenti per agenti

Il Plugin registra questi strumenti:

  * `wiki_status`
  * `wiki_search`
  * `wiki_get`
  * `wiki_apply`
  * `wiki_lint`


Cosa fanno:

  * `wiki_status`: modalità vault corrente, salute, disponibilità della CLI Obsidian
  * `wiki_search`: cerca pagine wiki e, quando configurato, corpora di memoria condivisi; accetta `mode` per ricerca persona, routing domande, evidenza sorgente o drilldown su dichiarazioni grezze
  * `wiki_get`: legge una pagina wiki per id/percorso o ripiega sul corpus di memoria condiviso
  * `wiki_apply`: mutazioni mirate di sintesi/metadati senza interventi liberi sulla pagina
  * `wiki_lint`: controlli strutturali, lacune di provenienza, contraddizioni, domande aperte


Il Plugin registra anche un supplemento di corpus di memoria non esclusivo, così `memory_search` e `memory_get` condivisi possono raggiungere la wiki quando il Plugin Active Memory supporta la selezione del corpus.

## Comportamento di prompt e contesto

Quando `context.includeCompiledDigestPrompt` è abilitato, le sezioni del prompt di memoria aggiungono uno snapshot compilato compatto da `agent-digest.json`.

Quello snapshot è intenzionalmente piccolo e ad alto segnale:

  * solo pagine principali
  * solo dichiarazioni principali
  * conteggio delle contraddizioni
  * conteggio delle domande
  * qualificatori di attendibilità/freschezza


È opt-in perché cambia la forma del prompt ed è utile principalmente per motori di contesto o assemblaggio legacy di prompt che consumano esplicitamente supplementi di memoria.

## Configurazione

Metti la configurazione sotto `plugins.entries.memory-wiki.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-wiki": {        enabled: true,        config: {          vaultMode: "isolated",          vault: {            path: "~/.openclaw/wiki/main",            renderMode: "obsidian",          },          obsidian: {            enabled: true,            useOfficialCli: true,            vaultName: "OpenClaw Wiki",            openAfterWrites: false,          },          bridge: {            enabled: false,            readMemoryArtifacts: true,            indexDreamReports: true,            indexDailyNotes: true,            indexMemoryRoot: true,            followMemoryEvents: true,          },          ingest: {            autoCompile: true,            maxConcurrentJobs: 1,            allowUrlIngest: true,          },          search: {            backend: "shared",            corpus: "wiki",          },          context: {            includeCompiledDigestPrompt: false,          },          render: {            preserveHumanBlocks: true,            createBacklinks: true,            createDashboards: true,          },        },      },    },  },}
[/code]

Opzioni principali:

  * `vaultMode`: `isolated`, `bridge`, `unsafe-local`
  * `vault.renderMode`: `native` o `obsidian`
  * `bridge.readMemoryArtifacts`: importa gli artefatti pubblici del Plugin Active Memory
  * `bridge.followMemoryEvents`: include i log degli eventi in modalità bridge
  * `search.backend`: `shared` o `local`
  * `search.corpus`: `wiki`, `memory` o `all`
  * `context.includeCompiledDigestPrompt`: aggiungi lo snapshot del digest compatto alle sezioni del prompt di memoria
  * `render.createBacklinks`: genera blocchi correlati deterministici
  * `render.createDashboards`: genera pagine dashboard


### Esempio: QMD + modalità bridge

Usalo quando vuoi QMD per il richiamo e `memory-wiki` per un livello di conoscenza mantenuto:

json5Copy code
[code]
    {  memory: {    backend: "qmd",  },  plugins: {    entries: {      "memory-wiki": {        enabled: true,        config: {          vaultMode: "bridge",          bridge: {            enabled: true,            readMemoryArtifacts: true,            indexDreamReports: true,            indexDailyNotes: true,            indexMemoryRoot: true,            followMemoryEvents: true,          },          search: {            backend: "shared",            corpus: "all",          },          context: {            includeCompiledDigestPrompt: false,          },        },      },    },  },}
[/code]

Questo mantiene:

  * QMD responsabile del richiamo di Active Memory
  * `memory-wiki` focalizzato su pagine compilate e dashboard
  * la forma del prompt invariata finché non abiliti intenzionalmente i prompt con digest compilato


## CLI

`memory-wiki` espone anche una superficie CLI di primo livello:

bashCopy code
[code]
    openclaw wiki statusopenclaw wiki doctoropenclaw wiki initopenclaw wiki ingest ./notes/alpha.mdopenclaw wiki compileopenclaw wiki lintopenclaw wiki search "alpha"openclaw wiki get entity.alphaopenclaw wiki apply synthesis "Alpha Summary" --body "..." --source-id source.alphaopenclaw wiki bridge importopenclaw wiki obsidian status
[/code]

Consulta [CLI: wiki](</it/cli/wiki>) per il riferimento completo dei comandi.

## Supporto Obsidian

Quando `vault.renderMode` è `obsidian`, il Plugin scrive Markdown compatibile con Obsidian e può facoltativamente usare la CLI ufficiale `obsidian`.

I flussi di lavoro supportati includono:

  * verifica dello stato
  * ricerca nel vault
  * apertura di una pagina
  * invocazione di un comando Obsidian
  * passaggio alla nota giornaliera


Questo è facoltativo. La wiki funziona comunque in modalità nativa senza Obsidian.

## Flusso di lavoro consigliato

  1. Mantieni il tuo Plugin Active Memory per richiamo/promozione/dreaming.
  2. Abilita `memory-wiki`.
  3. Inizia con la modalità `isolated` a meno che tu non voglia esplicitamente la modalità bridge.
  4. Usa `wiki_search` / `wiki_get` quando la provenienza è importante.
  5. Usa `wiki_apply` per sintesi mirate o aggiornamenti dei metadati.
  6. Esegui `wiki_lint` dopo modifiche significative.
  7. Attiva le dashboard se vuoi visibilità su contenuti obsoleti o contraddizioni.


## Documentazione correlata

  * [Panoramica della memoria](</it/concepts/memory>)
  * [CLI: memory](</it/cli/memory>)
  * [CLI: wiki](</it/cli/wiki>)
  * [Panoramica del Plugin SDK](</it/plugins/sdk-overview>)


Was this useful?YesNo
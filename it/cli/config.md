---
title: Configurazione
source_url: https://docs.openclaw.ai/it/cli/config
scraped_at: 2026-05-25
---

Helper di configurazione per modifiche non interattive in `openclaw.json`: ottieni/imposta/applica patch/rimuovi/file/schema/convalida valori per percorso e stampa il file di configurazione attivo. Esegui senza un sottocomando per aprire la procedura guidata di configurazione (come `openclaw configure`).

## Opzioni di root

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> Filtro di sezione ripetibile della configurazione guidata quando esegui `openclaw config` senza un sottocomando.

Sezioni guidate supportate: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## Esempi

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

Stampa lo schema JSON generato per `openclaw.json` su stdout come JSON.

Cosa include

  * Lo schema di configurazione root corrente, più un campo stringa root `$schema` per gli strumenti dell'editor.
  * Metadati della documentazione `title` e `description` dei campi usati dalla Control UI.
  * I nodi oggetto annidati, wildcard (`*`) ed elemento di array (`[]`) ereditano gli stessi metadati `title` / `description` quando esiste documentazione dei campi corrispondente.
  * Anche i rami `anyOf` / `oneOf` / `allOf` ereditano gli stessi metadati della documentazione quando esiste documentazione dei campi corrispondente.
  * Metadati di schema di Plugin e canali live nel miglior modo possibile quando i manifest di runtime possono essere caricati.
  * Uno schema di fallback pulito anche quando la configurazione corrente non è valida.

RPC di runtime correlata

`config.schema.lookup` restituisce un percorso di configurazione normalizzato con un nodo schema superficiale (`title`, `description`, `type`, `enum`, `const`, limiti comuni), i metadati dei suggerimenti UI corrispondenti e riepiloghi immediati dei figli. Usalo per il drill-down con ambito percorso nella Control UI o in client personalizzati.

bashCopy code
[code]
    openclaw config schema
[/code]

Reindirizzalo in un file quando vuoi ispezionarlo o convalidarlo con altri strumenti:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### Percorsi

I percorsi usano la notazione con punti o parentesi:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

Usa l'indice dell'elenco degli agenti per puntare a un agente specifico:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## Valori

I valori vengono analizzati come JSON5 quando possibile; altrimenti vengono trattati come stringhe. Usa `--strict-json` per richiedere l'analisi JSON5. `--json` rimane supportato come alias legacy.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` stampa il valore grezzo come JSON invece di testo formattato per terminale.

Usa `--merge` quando aggiungi voci a quelle mappe:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

Usa `--replace` solo quando vuoi intenzionalmente che il valore fornito diventi il valore di destinazione completo.

## Modalità di `config set`

`openclaw config set` supporta quattro stili di assegnazione:

### Modalità valore

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### Modalità builder SecretRef

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Modalità builder provider

La modalità builder provider punta solo a percorsi `secrets.providers.<alias>`:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Modalità batch

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

L'analisi batch usa sempre il payload batch (`--batch-json`/`--batch-file`) come fonte di verità. `--strict-json` / `--json` non modificano il comportamento dell'analisi batch.

## `config patch`

Usa `config patch` quando vuoi incollare o passare tramite pipe una patch con forma di configurazione invece di eseguire molti comandi `config set` basati su percorso. L'input è un oggetto JSON5. Gli oggetti vengono uniti ricorsivamente, gli array e i valori scalari sostituiscono il valore di destinazione e `null` elimina il percorso di destinazione.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

Puoi anche passare una patch su stdin tramite pipe, utile per script di configurazione remota:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

Patch di esempio:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Usa `--replace-path <path>` quando un oggetto o array deve diventare esattamente il valore fornito invece di essere aggiornato ricorsivamente con patch:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` esegue controlli di schema e risolvibilità SecretRef senza scrivere. Le SecretRef basate su exec vengono saltate per impostazione predefinita durante il dry run; aggiungi `--allow-exec` quando vuoi intenzionalmente che il dry run esegua i comandi provider.

La modalità percorso/valore JSON rimane supportata sia per SecretRef sia per provider:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Flag del builder provider

Le destinazioni del builder provider devono usare `secrets.providers.<alias>` come percorso.

Flag comuni

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Provider env (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (ripetibile)

Provider file (--provider-source file)

  * `--provider-path <path>` (obbligatorio)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Provider exec (--provider-source exec)

  * `--provider-command <path>` (obbligatorio)
  * `--provider-arg <arg>` (ripetibile)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (ripetibile)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (ripetibile)
  * `--provider-trusted-dir <path>` (ripetibile)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


Esempio di provider exec rafforzato:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

Usa `--dry-run` per convalidare le modifiche senza scrivere `openclaw.json`.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Comportamento dry-run

  * Modalità builder: esegue controlli di risolvibilità SecretRef per ref/provider modificati.
  * Modalità JSON (`--strict-json`, `--json` o modalità batch): esegue la convalida dello schema più i controlli di risolvibilità SecretRef.
  * La convalida delle policy viene eseguita anche per le superfici di destinazione SecretRef note come non supportate.
  * I controlli di policy valutano l'intera configurazione dopo la modifica, quindi le scritture su oggetti padre (ad esempio impostare `hooks` come oggetto) non possono aggirare la convalida delle superfici non supportate.
  * I controlli SecretRef exec vengono saltati per impostazione predefinita durante il dry run per evitare effetti collaterali dei comandi.
  * Usa `--allow-exec` con `--dry-run` per abilitare i controlli SecretRef exec (questo può eseguire comandi provider).
  * `--allow-exec` è solo per dry-run e genera errore se usato senza `--dry-run`.

Campi --dry-run --json

`--dry-run --json` stampa un report leggibile da macchina:

  * `ok`: indica se il dry-run è riuscito
  * `operations`: numero di assegnazioni valutate
  * `checks`: indica se sono stati eseguiti i controlli di schema/risolvibilità
  * `checks.resolvabilityComplete`: indica se i controlli di risolvibilità sono stati eseguiti fino al completamento (false quando i riferimenti exec vengono saltati)
  * `refsChecked`: numero di riferimenti effettivamente risolti durante il dry-run
  * `skippedExecRefs`: numero di riferimenti exec saltati perché `--allow-exec` non era impostato
  * `errors`: errori strutturati di schema/risolvibilità quando `ok=false`


### Forma dell'output JSON

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Success example

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Failure example

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

If dry-run fails

  * `config schema validation failed`: la forma della configurazione dopo la modifica non è valida; correggi il percorso/valore o la forma dell'oggetto provider/ref.
  * `Config policy validation failed: unsupported SecretRef usage`: riporta quella credenziale a input in testo semplice/stringa e mantieni i SecretRef solo sulle superfici supportate.
  * `SecretRef assignment(s) could not be resolved`: il provider/ref referenziato al momento non può essere risolto (variabile d'ambiente mancante, puntatore file non valido, errore del provider exec o mancata corrispondenza provider/sorgente).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: il dry-run ha saltato i riferimenti exec; esegui di nuovo con `--allow-exec` se ti serve la validazione della risolvibilità exec.
  * Per la modalità batch, correggi le voci non riuscite ed esegui di nuovo `--dry-run` prima di scrivere.


## Sicurezza di scrittura

`openclaw config set` e gli altri writer di configurazione di proprietà di OpenClaw validano l'intera configurazione dopo la modifica prima di salvarla su disco. Se il nuovo payload non supera la validazione dello schema o sembra una sovrascrittura distruttiva, la configurazione attiva resta invariata e il payload rifiutato viene salvato accanto a essa come `openclaw.json.rejected.*`.

Preferisci le scritture tramite CLI per piccole modifiche:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

Se una scrittura viene rifiutata, ispeziona il payload salvato e correggi la forma completa della configurazione:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

Le scritture dirette con editor sono ancora consentite, ma il Gateway in esecuzione le tratta come non attendibili finché non vengono validate. Le modifiche dirette non valide fanno fallire l'avvio o vengono saltate dal ricaricamento a caldo; Gateway non riscrive `openclaw.json`. Esegui `openclaw doctor --fix` per riparare una configurazione con prefissi o sovrascritta, oppure per ripristinare l'ultima copia valida nota. Consulta [risoluzione dei problemi del Gateway](</it/gateway/troubleshooting#gateway-rejected-invalid-config>).

Il ripristino dell'intero file è riservato alla riparazione tramite doctor. Le modifiche allo schema dei Plugin o lo scostamento di `minHostVersion` restano evidenti invece di eseguire il rollback di impostazioni utente non correlate come modelli, provider, profili di autenticazione, canali, esposizione del Gateway, strumenti, memoria, browser o configurazione cron.

## Sottocomandi

  * `config file`: stampa il percorso del file di configurazione attivo (risolto da `OPENCLAW_CONFIG_PATH` o dalla posizione predefinita). Il percorso deve indicare un file normale, non un symlink.


Riavvia il Gateway dopo le modifiche.

## Validare

Valida la configurazione corrente rispetto allo schema attivo senza avviare il Gateway.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

Dopo che `openclaw config validate` riesce, puoi usare la TUI locale per far confrontare a un agente integrato la configurazione attiva con la documentazione mentre validi ogni modifica dallo stesso terminale:

bashCopy code
[code]
    openclaw chat
[/code]

Poi all'interno della TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Ciclo di riparazione tipico:

* ### Compare with docs

Chiedi all'agente di confrontare la configurazione corrente con la pagina della documentazione pertinente e suggerire la correzione più piccola.

* ### Apply targeted edits

Applica modifiche mirate con `openclaw config set` o `openclaw configure`.

* ### Re-validate

Esegui di nuovo `openclaw config validate` dopo ogni modifica.

* ### Doctor for runtime issues

Se la validazione riesce ma il runtime non è ancora integro, esegui `openclaw doctor` o `openclaw doctor --fix` per assistenza su migrazione e riparazione.

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Configurazione](</it/gateway/configuration>)


Was this useful?YesNo
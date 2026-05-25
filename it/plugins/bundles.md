---
title: Bundle di Plugin
source_url: https://docs.openclaw.ai/it/plugins/bundles
scraped_at: 2026-05-25
---

OpenClaw può installare plugin da tre ecosistemi esterni: **Codex** , **Claude** e **Cursor**. Questi sono chiamati **pacchetti** : insiemi di contenuti e metadati che OpenClaw mappa in funzionalità native come Skills, hook e strumenti MCP.

## Perché esistono i pacchetti

Molti plugin utili sono pubblicati in formato Codex, Claude o Cursor. Invece di richiedere agli autori di riscriverli come plugin nativi OpenClaw, OpenClaw rileva questi formati e mappa i loro contenuti supportati nell'insieme di funzionalità native. Questo significa che puoi installare un pacchetto di comandi Claude o un pacchetto di Skills Codex e usarlo immediatamente.

## Installare un pacchetto

* ### Installa da una directory, un archivio o un marketplace

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-bundle # Archiveopenclaw plugins install ./my-bundle.tgz # Claude marketplaceopenclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

* ### Verifica il rilevamento

bashCopy code
[code]
    openclaw plugins listopenclaw plugins inspect <id>
[/code]

I pacchetti vengono mostrati come `Format: bundle` con un sottotipo `codex`, `claude` o `cursor`.

* ### Riavvia e usa

bashCopy code
[code]
    openclaw gateway restart
[/code]

Le funzionalità mappate (Skills, hook, strumenti MCP, valori predefiniti LSP) sono disponibili nella sessione successiva.

## Cosa OpenClaw mappa dai pacchetti

Non tutte le funzionalità dei pacchetti vengono eseguite oggi in OpenClaw. Ecco cosa funziona e cosa viene rilevato ma non è ancora collegato.

### Supportato ora

Funzionalità | Come viene mappata | Si applica a  
---|---|---  
Contenuto Skills | Le radici Skills del pacchetto vengono caricate come normali Skills OpenClaw | Tutti i formati  
Comandi | `commands/` e `.cursor/commands/` trattati come radici Skills | Claude, Cursor  
Pacchetti hook | Layout OpenClaw-style `HOOK.md` \+ `handler.ts` | Codex  
Strumenti MCP | Configurazione MCP del pacchetto unita alle impostazioni Pi incorporate; server stdio e HTTP supportati caricati | Tutti i formati  
Server LSP | `.lsp.json` di Claude e `lspServers` dichiarati nel manifest uniti ai valori predefiniti LSP di Pi incorporato | Claude  
Impostazioni | `settings.json` di Claude importato come valori predefiniti di Pi incorporato | Claude  
  
#### Contenuto Skills

  * le radici Skills del pacchetto vengono caricate come normali radici Skills OpenClaw
  * le radici `commands` di Claude sono trattate come radici Skills aggiuntive
  * le radici `.cursor/commands` di Cursor sono trattate come radici Skills aggiuntive


Questo significa che i file di comando Markdown Claude funzionano tramite il normale loader Skills di OpenClaw. Il Markdown dei comandi Cursor funziona tramite lo stesso percorso.

#### Pacchetti hook

  * le radici hook del pacchetto funzionano **solo** quando usano il normale layout dei pacchetti hook OpenClaw. Oggi questo è principalmente il caso compatibile con Codex: 
    * `HOOK.md`
    * `handler.ts` o `handler.js`


#### MCP per Pi

  * i pacchetti abilitati possono contribuire configurazione server MCP
  * OpenClaw unisce la configurazione MCP del pacchetto nelle impostazioni effettive di Pi incorporato come `mcpServers`
  * OpenClaw espone gli strumenti MCP supportati del pacchetto durante i turni dell'agente Pi incorporato avviando server stdio o connettendosi a server HTTP
  * i profili di strumenti `coding` e `messaging` includono per impostazione predefinita gli strumenti MCP del pacchetto; usa `tools.deny: ["bundle-mcp"]` per disattivarli per un agente o un Gateway
  * le impostazioni Pi locali del progetto si applicano comunque dopo i valori predefiniti del pacchetto, quindi le impostazioni dell'area di lavoro possono sovrascrivere le voci MCP del pacchetto quando necessario
  * i cataloghi degli strumenti MCP del pacchetto vengono ordinati in modo deterministico prima della registrazione, quindi le modifiche all'ordine upstream di `listTools()` non perturbano i blocchi degli strumenti della cache dei prompt


##### Trasporti

I server MCP possono usare il trasporto stdio o HTTP:

**Stdio** avvia un processo figlio:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "my-server": {        "command": "node",        "args": ["server.js"],        "env": { "PORT": "3000" }      }    }  }}
[/code]

**HTTP** si connette a un server MCP in esecuzione su `sse` per impostazione predefinita, oppure su `streamable-http` quando richiesto:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "my-server": {        "url": "http://localhost:3100/mcp",        "transport": "streamable-http",        "headers": {          "Authorization": "Bearer ${MY_SECRET_TOKEN}"        },        "connectionTimeoutMs": 30000      }    }  }}
[/code]

  * `transport` può essere impostato su `"streamable-http"` o `"sse"`; se omesso, OpenClaw usa `sse`
  * `type: "http"` è una forma downstream nativa della CLI; usa `transport: "streamable-http"` nella configurazione OpenClaw. `openclaw mcp set` e `openclaw doctor --fix` normalizzano l'alias comune.
  * sono consentiti solo gli schemi URL `http:` e `https:`
  * i valori `headers` supportano l'interpolazione `${ENV_VAR}`
  * una voce server con sia `command` sia `url` viene rifiutata
  * le credenziali URL (userinfo e parametri query) vengono oscurate dalle descrizioni degli strumenti e dai log
  * `connectionTimeoutMs` sovrascrive il timeout di connessione predefinito di 30 secondi per entrambi i trasporti stdio e HTTP


##### Nomenclatura degli strumenti

OpenClaw registra gli strumenti MCP del pacchetto con nomi sicuri per il provider nella forma `serverName__toolName`. Per esempio, un server con chiave `"vigil-harbor"` che espone uno strumento `memory_search` viene registrato come `vigil-harbor__memory_search`.

  * i caratteri fuori da `A-Za-z0-9_-` vengono sostituiti con `-`
  * i frammenti che inizierebbero con un carattere non alfabetico ricevono un prefisso alfabetico, quindi le chiavi server numeriche come `12306` diventano prefissi strumento sicuri per il provider
  * i prefissi server sono limitati a 30 caratteri
  * i nomi completi degli strumenti sono limitati a 64 caratteri
  * i nomi server vuoti ripiegano su `mcp`
  * i nomi sanificati in collisione vengono disambiguati con suffissi numerici
  * l'ordine finale degli strumenti esposti è deterministico per nome sicuro, per mantenere stabili in cache i turni Pi ripetuti
  * il filtro dei profili tratta tutti gli strumenti di un server MCP del pacchetto come di proprietà del plugin `bundle-mcp`, quindi le allowlist e le deny list dei profili possono includere sia singoli nomi di strumenti esposti sia la chiave plugin `bundle-mcp`


#### Impostazioni Pi incorporate

  * `settings.json` di Claude viene importato come impostazioni Pi incorporate predefinite quando il pacchetto è abilitato
  * OpenClaw sanifica le chiavi di override della shell prima di applicarle


Chiavi sanificate:

  * `shellPath`
  * `shellCommandPrefix`


#### LSP di Pi incorporato

  * i pacchetti Claude abilitati possono contribuire configurazione server LSP
  * OpenClaw carica `.lsp.json` più eventuali percorsi `lspServers` dichiarati nel manifest
  * la configurazione LSP del pacchetto viene unita ai valori predefiniti LSP effettivi di Pi incorporato
  * oggi sono eseguibili solo server LSP supportati basati su stdio; i trasporti non supportati vengono comunque mostrati in `openclaw plugins inspect <id>`


### Rilevato ma non eseguito

Questi elementi sono riconosciuti e mostrati nella diagnostica, ma OpenClaw non li esegue:

  * `agents`, automazione `hooks.json`, `outputStyles` di Claude
  * `.cursor/agents`, `.cursor/hooks.json`, `.cursor/rules` di Cursor
  * metadati inline/app Codex oltre alla segnalazione delle capacità


## Formati dei pacchetti

Pacchetti Codex

Marcatori: `.codex-plugin/plugin.json`

Contenuto opzionale: `skills/`, `hooks/`, `.mcp.json`, `.app.json`

I pacchetti Codex si adattano meglio a OpenClaw quando usano radici Skills e directory di pacchetti hook OpenClaw-style (`HOOK.md` \+ `handler.ts`).

Pacchetti Claude

Due modalità di rilevamento:

  * **Basata su manifest:** `.claude-plugin/plugin.json`
  * **Senza manifest:** layout Claude predefinito (`skills/`, `commands/`, `agents/`, `hooks/`, `.mcp.json`, `.lsp.json`, `settings.json`)


Comportamento specifico di Claude:

  * `commands/` viene trattato come contenuto Skills
  * `settings.json` viene importato nelle impostazioni Pi incorporate (le chiavi di override della shell vengono sanificate)
  * `.mcp.json` espone gli strumenti stdio supportati a Pi incorporato
  * `.lsp.json` più i percorsi `lspServers` dichiarati nel manifest vengono caricati nei valori predefiniti LSP di Pi incorporato
  * `hooks/hooks.json` viene rilevato ma non eseguito
  * i percorsi dei componenti personalizzati nel manifest sono additivi (estendono i valori predefiniti, non li sostituiscono)

Pacchetti Cursor

Marcatori: `.cursor-plugin/plugin.json`

Contenuto opzionale: `skills/`, `.cursor/commands/`, `.cursor/agents/`, `.cursor/rules/`, `.cursor/hooks.json`, `.mcp.json`

  * `.cursor/commands/` viene trattato come contenuto Skills
  * `.cursor/rules/`, `.cursor/agents/` e `.cursor/hooks.json` sono solo rilevati


## Precedenza del rilevamento

OpenClaw controlla prima il formato plugin nativo:

  1. `openclaw.plugin.json` o `package.json` valido con `openclaw.extensions`: trattato come **plugin nativo**
  2. Marcatori di pacchetto (`.codex-plugin/`, `.claude-plugin/` o layout Claude/Cursor predefinito): trattato come **pacchetto**


Se una directory contiene entrambi, OpenClaw usa il percorso nativo. Questo impedisce che pacchetti a doppio formato vengano installati parzialmente come pacchetti.

## Dipendenze di runtime e pulizia

  * I pacchetti compatibili di terze parti non ricevono riparazione `npm install` all'avvio. Devono essere installati tramite `openclaw plugins install` e includere tutto ciò di cui hanno bisogno nella directory del plugin installato.
  * I plugin in pacchetto di proprietà di OpenClaw sono forniti leggeri nel core oppure scaricabili tramite l'installer dei plugin. L'avvio del Gateway non esegue mai un gestore di pacchetti per loro.
  * `openclaw doctor --fix` rimuove le directory legacy delle dipendenze preparate e può recuperare plugin scaricabili che mancano dall'indice plugin locale quando la configurazione li referenzia.


## Sicurezza

I pacchetti hanno un confine di attendibilità più ristretto rispetto ai plugin nativi:

  * OpenClaw **non** carica moduli runtime arbitrari dei pacchetti in-process
  * i percorsi di Skills e pacchetti hook devono restare dentro la radice del plugin (con controllo dei confini)
  * i file di impostazioni vengono letti con gli stessi controlli dei confini
  * i server MCP stdio supportati possono essere avviati come sottoprocessi


Questo rende i pacchetti più sicuri per impostazione predefinita, ma dovresti comunque trattare i pacchetti di terze parti come contenuti attendibili per le funzionalità che espongono.

## Risoluzione dei problemi

Il pacchetto viene rilevato ma le capacità non vengono eseguite

Esegui `openclaw plugins inspect <id>`. Se una capacità è elencata ma contrassegnata come non collegata, si tratta di un limite del prodotto, non di un'installazione rotta.

I file di comando Claude non appaiono

Assicurati che il pacchetto sia abilitato e che i file Markdown si trovino dentro una radice `commands/` o `skills/` rilevata.

Le impostazioni Claude non si applicano

Sono supportate solo le impostazioni Pi incorporate da `settings.json`. OpenClaw non tratta le impostazioni del pacchetto come patch di configurazione grezze.

Gli hook Claude non vengono eseguiti

`hooks/hooks.json` è solo rilevato. Se ti servono hook eseguibili, usa il layout dei pacchetti hook OpenClaw o distribuisci un plugin nativo.

## Correlati

  * [Installa e configura i plugin](</it/tools/plugin>)
  * [Creare plugin](</it/plugins/building-plugins>) — crea un plugin nativo
  * [Manifest del plugin](</it/plugins/manifest>) — schema del manifest nativo


Was this useful?YesNo
---
title: Differenze
source_url: https://docs.openclaw.ai/it/tools/diffs
scraped_at: 2026-05-25
---

`diffs` è uno strumento Plugin opzionale con brevi indicazioni di sistema integrate e una skill complementare che trasforma il contenuto delle modifiche in un artefatto diff di sola lettura per gli agenti.

Accetta alternativamente:

  * testo `before` e `after`
  * una `patch` unificata


Può restituire:

  * un URL del visualizzatore del Gateway per la presentazione su canvas
  * un percorso di file renderizzato (PNG o PDF) per la consegna nei messaggi
  * entrambi gli output in una sola chiamata


Quando è abilitato, il Plugin antepone indicazioni d'uso concise nello spazio del prompt di sistema ed espone anche una skill dettagliata per i casi in cui l'agente ha bisogno di istruzioni più complete.

## Avvio rapido

* ### Installa il Plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Abilita il Plugin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Scegli una modalità

### view

Flussi incentrati sul canvas: gli agenti chiamano `diffs` con `mode: "view"` e aprono `details.viewerUrl` con `canvas present`.

### file

Consegna di file in chat: gli agenti chiamano `diffs` con `mode: "file"` e inviano `details.filePath` con `message` usando `path` o `filePath`.

### both

Combinato: gli agenti chiamano `diffs` con `mode: "both"` per ottenere entrambi gli artefatti in una sola chiamata.

## Disabilitare le indicazioni di sistema integrate

Se vuoi mantenere abilitato lo strumento `diffs` ma disabilitare le sue indicazioni integrate per il prompt di sistema, imposta `plugins.entries.diffs.hooks.allowPromptInjection` su `false`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Questo blocca l'hook `before_prompt_build` del Plugin diffs mantenendo disponibili il Plugin, lo strumento e la skill complementare.

Se vuoi disabilitare sia le indicazioni sia lo strumento, disabilita invece il Plugin.

## Workflow tipico dell'agente

* ### Chiama diffs

L'agente chiama lo strumento `diffs` con l'input.

* ### Leggi i dettagli

L'agente legge i campi `details` dalla risposta.

* ### Presenta

L'agente apre `details.viewerUrl` con `canvas present`, invia `details.filePath` con `message` usando `path` o `filePath`, oppure esegue entrambe le azioni.

## Esempi di input

### Prima e dopo

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Riferimento dell'input dello strumento

Tutti i campi sono opzionali salvo diversa indicazione.

Testo originale. Richiesto con `after` quando `patch` è omesso.

Testo aggiornato. Richiesto con `before` quando `patch` è omesso.

Testo diff unificato. Mutuamente esclusivo con `before` e `after`.

Nome file visualizzato per la modalità prima e dopo.

Suggerimento di override della lingua per la modalità prima e dopo. I valori sconosciuti ripiegano sul testo semplice.

Override del titolo del visualizzatore.

Modalità di output. Il valore predefinito è il default del Plugin `defaults.mode`. Alias deprecato: `"image"` si comporta come `"file"` ed è ancora accettato per compatibilità all'indietro.

Tema del visualizzatore. Il valore predefinito è il default del Plugin `defaults.theme`.

Layout del diff. Il valore predefinito è il default del Plugin `defaults.layout`.

Espande le sezioni invariate quando è disponibile il contesto completo. Opzione solo per singola chiamata (non una chiave predefinita del Plugin).

Formato del file renderizzato. Il valore predefinito è il default del Plugin `defaults.fileFormat`.

Preset di qualità per il rendering PNG o PDF.

Override della scala del dispositivo (`1`-`4`).

Larghezza massima di rendering in pixel CSS (`640`-`2400`).

TTL dell'artefatto in secondi per gli output del visualizzatore e dei file autonomi. Massimo 21600.

Override dell'origine dell'URL del visualizzatore. Sovrascrive `viewerBaseUrl` del Plugin. Deve essere `http` o `https`, senza query/hash.

Alias di input legacy

Ancora accettati per compatibilità all'indietro:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Convalida e limiti

  * `before` e `after` massimo 512 KiB ciascuno.
  * `patch` massimo 2 MiB.
  * `path` massimo 2048 byte.
  * `lang` massimo 128 byte.
  * `title` massimo 1024 byte.
  * Limite di complessità della patch: massimo 128 file e 120000 righe totali.
  * `patch` insieme a `before` o `after` viene rifiutato.
  * Limiti di sicurezza del file renderizzato (applicati a PNG e PDF): 
    * `fileQuality: "standard"`: massimo 8 MP (8.000.000 pixel renderizzati).
    * `fileQuality: "hq"`: massimo 14 MP (14.000.000 pixel renderizzati).
    * `fileQuality: "print"`: massimo 24 MP (24.000.000 pixel renderizzati).
    * Il PDF ha anche un massimo di 50 pagine.


## Contratto dei dettagli di output

Lo strumento restituisce metadati strutturati sotto `details`.

Campi del visualizzatore

Campi condivisi per le modalità che creano un visualizzatore:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId` quando disponibili)

Campi del file

Campi del file quando viene renderizzato PNG o PDF:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (stesso valore di `filePath`, per compatibilità con lo strumento messaggi)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Alias di compatibilità

Restituiti anche per i chiamanti esistenti:

  * `format` (stesso valore di `fileFormat`)
  * `imagePath` (stesso valore di `filePath`)
  * `imageBytes` (stesso valore di `fileBytes`)
  * `imageQuality` (stesso valore di `fileQuality`)
  * `imageScale` (stesso valore di `fileScale`)
  * `imageMaxWidth` (stesso valore di `fileMaxWidth`)


Riepilogo del comportamento delle modalità:

Modalità | Cosa viene restituito  
---|---  
`"view"` | Solo i campi del visualizzatore.  
`"file"` | Solo i campi del file, senza artefatto del visualizzatore.  
`"both"` | Campi del visualizzatore più campi del file. Se il rendering del file fallisce, il visualizzatore viene comunque restituito con `fileError` e l'alias `imageError`.  
  
## Sezioni invariate compresse

  * Il visualizzatore può mostrare righe come `N unmodified lines`.
  * I controlli di espansione su quelle righe sono condizionali e non garantiti per ogni tipo di input.
  * I controlli di espansione compaiono quando il diff renderizzato dispone di dati di contesto espandibili, cosa tipica per l'input prima e dopo.
  * Per molti input patch unificati, i corpi del contesto omessi non sono disponibili negli hunk della patch analizzata, quindi la riga può apparire senza controlli di espansione. Questo è il comportamento previsto.
  * `expandUnchanged` si applica solo quando esiste contesto espandibile.


## Default del Plugin

Imposta i default a livello di Plugin in `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Default supportati:

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


I parametri espliciti dello strumento sovrascrivono questi default.

### Configurazione persistente dell'URL del visualizzatore

Fallback di proprietà del Plugin per i link del visualizzatore restituiti quando una chiamata allo strumento non passa `baseUrl`. Deve essere `http` o `https`, senza query/hash.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Configurazione di sicurezza

`false`: le richieste non loopback alle route del visualizzatore sono negate. `true`: i visualizzatori remoti sono consentiti se il percorso tokenizzato è valido.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Ciclo di vita e archiviazione degli artefatti

  * Gli artefatti sono archiviati nella sottocartella temporanea: `$TMPDIR/openclaw-diffs`.
  * I metadati dell'artefatto del visualizzatore contengono: 
    * ID artefatto casuale (20 caratteri esadecimali)
    * token casuale (48 caratteri esadecimali)
    * `createdAt` e `expiresAt`
    * percorso `viewer.html` archiviato
  * Il TTL predefinito dell'artefatto è 30 minuti quando non specificato.
  * Il TTL massimo accettato del visualizzatore è 6 ore.
  * La pulizia viene eseguita opportunisticamente dopo la creazione dell'artefatto.
  * Gli artefatti scaduti vengono eliminati.
  * La pulizia di fallback rimuove le cartelle obsolete più vecchie di 24 ore quando i metadati mancano.


## URL del visualizzatore e comportamento di rete

Route del visualizzatore:

  * `/plugins/diffs/view/{artifactId}/{token}`


Asset del visualizzatore:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


Il documento del visualizzatore risolve questi asset in modo relativo all'URL del visualizzatore, quindi un prefisso di percorso `baseUrl` opzionale viene preservato anche per entrambe le richieste degli asset.

Comportamento di costruzione dell'URL:

  * Se viene fornito `baseUrl` nella chiamata allo strumento, viene usato dopo una convalida rigorosa.
  * Altrimenti, se `viewerBaseUrl` del Plugin è configurato, viene usato.
  * Senza nessuno dei due override, l'URL del visualizzatore usa per default il loopback `127.0.0.1`.
  * Se la modalità di bind del Gateway è `custom` e `gateway.customBindHost` è impostato, viene usato quell'host.


Regole di `baseUrl`:

  * Deve essere `http://` o `https://`.
  * Query e hash vengono rifiutati.
  * È consentita l'origine più un percorso base opzionale.


## Modello di sicurezza

Rafforzamento del visualizzatore

  * Solo loopback per impostazione predefinita.
  * Percorsi del visualizzatore tokenizzati con convalida rigorosa di ID e token.
  * CSP della risposta del visualizzatore: 
    * `default-src 'none'`
    * script e asset solo da self
    * nessun `connect-src` in uscita
  * Limitazione dei miss remoti quando l'accesso remoto è abilitato: 
    * 40 errori ogni 60 secondi
    * blocco di 60 secondi (`429 Too Many Requests`)

Rafforzamento del rendering dei file

  * Il routing delle richieste del browser per gli screenshot è deny-by-default.
  * Sono consentiti solo gli asset locali del visualizzatore da `http://127.0.0.1/plugins/diffs/assets/*`.
  * Le richieste di rete esterne sono bloccate.


## Requisiti del browser per la modalità file

`mode: "file"` e `mode: "both"` richiedono un browser compatibile con Chromium.

Ordine di risoluzione:

* ### Configurazione

`browser.executablePath` nella configurazione di OpenClaw.

* ### Variabili d'ambiente

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Fallback della piattaforma

Fallback di rilevamento di comandi/percorsi della piattaforma.

Testo di errore comune:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Risolvi installando Chrome, Chromium, Edge o Brave, oppure impostando una delle opzioni di percorso dell'eseguibile indicate sopra.

## Risoluzione dei problemi

Errori di convalida dell'input

  * `Provide patch or both before and after text.` — includi sia `before` sia `after`, oppure fornisci `patch`.
  * `Provide either patch or before/after input, not both.` — non combinare modalità di input.
  * `Invalid baseUrl: ...` — usa un'origine `http(s)` con percorso facoltativo, senza query/hash.
  * `{field} exceeds maximum size (...)` — riduci la dimensione del payload.
  * Rifiuto di patch di grandi dimensioni — riduci il numero di file della patch o le righe totali.

Accessibilità del visualizzatore

  * L'URL del visualizzatore si risolve in `127.0.0.1` per impostazione predefinita.
  * Per scenari di accesso remoto: 
    * imposta `viewerBaseUrl` del plugin, oppure
    * passa `baseUrl` per ogni chiamata allo strumento, oppure
    * usa `gateway.bind=custom` e `gateway.customBindHost`
  * Se `gateway.trustedProxies` include il loopback per un proxy sullo stesso host (per esempio Tailscale Serve), le richieste raw loopback al visualizzatore senza intestazioni client-IP inoltrate falliscono chiuse per progettazione.
  * Per quella topologia di proxy: 
    * preferisci `mode: "file"` o `mode: "both"` quando ti serve solo un allegato, oppure
    * abilita intenzionalmente `security.allowRemoteViewer` e imposta `viewerBaseUrl` del plugin o passa un `baseUrl` proxy/pubblico quando ti serve un URL del visualizzatore condivisibile
  * Abilita `security.allowRemoteViewer` solo quando intendi consentire l'accesso esterno al visualizzatore.

La riga delle righe non modificate non ha pulsante di espansione

Questo può accadere per l'input patch quando la patch non contiene contesto espandibile. È previsto e non indica un errore del visualizzatore.

Artefatto non trovato

  * Artefatto scaduto a causa del TTL.
  * Token o percorso modificati.
  * La pulizia ha rimosso dati obsoleti.


## Indicazioni operative

  * Preferisci `mode: "view"` per revisioni interattive locali in canvas.
  * Preferisci `mode: "file"` per canali chat in uscita che richiedono un allegato.
  * Mantieni `allowRemoteViewer` disabilitato a meno che la tua distribuzione richieda URL remoti del visualizzatore.
  * Imposta `ttlSeconds` brevi ed espliciti per diff sensibili.
  * Evita di inviare segreti nell'input del diff quando non necessario.
  * Se il tuo canale comprime le immagini in modo aggressivo (per esempio Telegram o WhatsApp), preferisci l'output PDF (`fileFormat: "pdf"`).


## Correlati

  * [Browser](</it/tools/browser>)
  * [Plugins](</it/tools/plugin>)
  * [Panoramica degli strumenti](</it/tools>)


Was this useful?YesNo
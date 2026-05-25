---
title: Verschillen
source_url: https://docs.openclaw.ai/nl/tools/diffs
scraped_at: 2026-05-25
---

`diffs` is een optioneel Plugin-hulpmiddel met korte ingebouwde systeemrichtlijnen en een bijbehorende skill die wijzigingsinhoud omzet in een alleen-lezen diff-artefact voor agents.

Het accepteert een van de volgende opties:

  * `before`\- en `after`-tekst
  * een uniforme `patch`


Het kan het volgende teruggeven:

  * een Gateway-viewer-URL voor canvas-presentatie
  * een gerenderd bestandspad (PNG of PDF) voor berichtbezorging
  * beide outputs in een enkele aanroep


Wanneer ingeschakeld, voegt de Plugin beknopte gebruiksrichtlijnen toe aan de systeem-prompt-ruimte en stelt ook een gedetailleerde skill beschikbaar voor gevallen waarin de agent uitgebreidere instructies nodig heeft.

## Snel starten

* ### Installeer de Plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Schakel de Plugin in

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Kies een modus

### view

Canvas-first flows: agents roepen `diffs` aan met `mode: "view"` en openen `details.viewerUrl` met `canvas present`.

### file

Chatbestandsbezorging: agents roepen `diffs` aan met `mode: "file"` en verzenden `details.filePath` met `message` via `path` of `filePath`.

### both

Gecombineerd: agents roepen `diffs` aan met `mode: "both"` om beide artefacten in een enkele aanroep te krijgen.

## Ingebouwde systeemrichtlijnen uitschakelen

Als je het `diffs`-hulpmiddel ingeschakeld wilt houden maar de ingebouwde systeem-prompt-richtlijnen wilt uitschakelen, stel je `plugins.entries.diffs.hooks.allowPromptInjection` in op `false`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Dit blokkeert de `before_prompt_build`-hook van de diffs-Plugin, terwijl de Plugin, het hulpmiddel en de bijbehorende skill beschikbaar blijven.

Als je zowel de richtlijnen als het hulpmiddel wilt uitschakelen, schakel dan in plaats daarvan de Plugin uit.

## Typische agentworkflow

* ### Roep diffs aan

Agent roept het `diffs`-hulpmiddel aan met invoer.

* ### Lees details

Agent leest `details`-velden uit de respons.

* ### Presenteer

Agent opent `details.viewerUrl` met `canvas present`, verzendt `details.filePath` met `message` via `path` of `filePath`, of doet beide.

## Invoervoorbeelden

### Voor en na

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Referentie voor hulpmiddelinvoer

Alle velden zijn optioneel, tenzij anders vermeld.

Oorspronkelijke tekst. Vereist met `after` wanneer `patch` is weggelaten.

Bijgewerkte tekst. Vereist met `before` wanneer `patch` is weggelaten.

Uniforme diff-tekst. Wederzijds uitsluitend met `before` en `after`.

Weergavebestandsnaam voor de voor-en-na-modus.

Hint voor taaloverschrijving voor de voor-en-na-modus. Onbekende waarden vallen terug op platte tekst.

Overschrijving van viewertitel.

Uitvoermodus. Standaard is de Plugin-standaard `defaults.mode`. Verouderde alias: `"image"` gedraagt zich als `"file"` en wordt nog steeds geaccepteerd voor achterwaartse compatibiliteit.

Viewerthema. Standaard is de Plugin-standaard `defaults.theme`.

Diff-indeling. Standaard is de Plugin-standaard `defaults.layout`.

Vouw ongewijzigde secties uit wanneer volledige context beschikbaar is. Alleen optie per aanroep (geen Plugin-standaardsleutel).

Gerenderde bestandsindeling. Standaard is de Plugin-standaard `defaults.fileFormat`.

Kwaliteitspreset voor PNG- of PDF-rendering.

Overschrijving van apparaatschaal (`1`-`4`).

Maximale renderbreedte in CSS-pixels (`640`-`2400`).

Artefact-TTL in seconden voor viewer- en zelfstandige bestandsoutputs. Max 21600.

Overschrijving van viewer-URL-origin. Overschrijft Plugin `viewerBaseUrl`. Moet `http` of `https` zijn, zonder query/hash.

Verouderde invoeraliassen

Nog steeds geaccepteerd voor achterwaartse compatibiliteit:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Validatie en limieten

  * `before` en `after` elk max 512 KiB.
  * `patch` max 2 MiB.
  * `path` max 2048 bytes.
  * `lang` max 128 bytes.
  * `title` max 1024 bytes.
  * Limiet voor patchcomplexiteit: max 128 bestanden en 120000 totale regels.
  * `patch` en `before` of `after` samen worden geweigerd.
  * Veiligheidslimieten voor gerenderde bestanden (van toepassing op PNG en PDF): 
    * `fileQuality: "standard"`: max 8 MP (8.000.000 gerenderde pixels).
    * `fileQuality: "hq"`: max 14 MP (14.000.000 gerenderde pixels).
    * `fileQuality: "print"`: max 24 MP (24.000.000 gerenderde pixels).
    * PDF heeft ook een maximum van 50 pagina's.


## Contract voor outputdetails

Het hulpmiddel retourneert gestructureerde metadata onder `details`.

Viewervelden

Gedeelde velden voor modi die een viewer maken:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId` wanneer beschikbaar)

Bestandsvelden

Bestandsvelden wanneer PNG of PDF wordt gerenderd:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (dezelfde waarde als `filePath`, voor compatibiliteit met bericht-hulpmiddelen)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Compatibiliteitsaliassen

Ook geretourneerd voor bestaande aanroepers:

  * `format` (dezelfde waarde als `fileFormat`)
  * `imagePath` (dezelfde waarde als `filePath`)
  * `imageBytes` (dezelfde waarde als `fileBytes`)
  * `imageQuality` (dezelfde waarde als `fileQuality`)
  * `imageScale` (dezelfde waarde als `fileScale`)
  * `imageMaxWidth` (dezelfde waarde als `fileMaxWidth`)


Samenvatting van modusgedrag:

Modus | Wat wordt geretourneerd  
---|---  
`"view"` | Alleen viewervelden.  
`"file"` | Alleen bestandsvelden, geen viewerartefact.  
`"both"` | Viewervelden plus bestandsvelden. Als bestandsrendering mislukt, wordt de viewer nog steeds geretourneerd met `fileError` en de alias `imageError`.  
  
## Samengevouwen ongewijzigde secties

  * De viewer kan rijen tonen zoals `N unmodified lines`.
  * Uitvouwknoppen op die rijen zijn voorwaardelijk en niet gegarandeerd voor elk invoertype.
  * Uitvouwknoppen verschijnen wanneer de gerenderde diff uitbreidbare contextgegevens heeft, wat typisch is voor voor-en-na-invoer.
  * Voor veel uniforme patch-invoer zijn weggelaten contextinhouden niet beschikbaar in de geparste patch-hunks, zodat de rij zonder uitvouwknoppen kan verschijnen. Dit is verwacht gedrag.
  * `expandUnchanged` is alleen van toepassing wanneer uitbreidbare context bestaat.


## Plugin-standaarden

Stel Plugin-brede standaarden in `~/.openclaw/openclaw.json` in:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Ondersteunde standaarden:

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


Expliciete hulpmiddelparameters overschrijven deze standaarden.

### Configuratie voor persistente viewer-URL

Plugin-eigen fallback voor geretourneerde viewerlinks wanneer een hulpmiddelaanroep geen `baseUrl` doorgeeft. Moet `http` of `https` zijn, zonder query/hash.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Beveiligingsconfiguratie

`false`: niet-loopback-aanvragen naar viewerroutes worden geweigerd. `true`: externe viewers zijn toegestaan als het pad met token geldig is.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Artefactlevenscyclus en opslag

  * Artefacten worden opgeslagen onder de tijdelijke submap: `$TMPDIR/openclaw-diffs`.
  * Viewerartefactmetadata bevat: 
    * willekeurige artefact-ID (20 hex-tekens)
    * willekeurige token (48 hex-tekens)
    * `createdAt` en `expiresAt`
    * opgeslagen `viewer.html`-pad
  * Standaard artefact-TTL is 30 minuten wanneer niet opgegeven.
  * Maximale geaccepteerde viewer-TTL is 6 uur.
  * Opschoning wordt opportunistisch uitgevoerd na het maken van artefacten.
  * Verlopen artefacten worden verwijderd.
  * Fallback-opschoning verwijdert verouderde mappen ouder dan 24 uur wanneer metadata ontbreekt.


## Viewer-URL en netwerkgedrag

Viewerroute:

  * `/plugins/diffs/view/{artifactId}/{token}`


Viewerassets:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


Het viewerdocument lost die assets relatief ten opzichte van de viewer-URL op, zodat een optionele `baseUrl`-padprefix ook voor beide assetaanvragen behouden blijft.

Gedrag voor URL-constructie:

  * Als tool-call `baseUrl` is opgegeven, wordt deze na strikte validatie gebruikt.
  * Anders, als Plugin `viewerBaseUrl` is geconfigureerd, wordt deze gebruikt.
  * Zonder een van beide overschrijvingen valt de viewer-URL terug op loopback `127.0.0.1`.
  * Als Gateway-bindmodus `custom` is en `gateway.customBindHost` is ingesteld, wordt die host gebruikt.


`baseUrl`-regels:

  * Moet `http://` of `https://` zijn.
  * Query en hash worden geweigerd.
  * Origin plus optioneel basispad is toegestaan.


## Beveiligingsmodel

Viewer-verharding

  * Standaard alleen loopback.
  * Getokeniseerde viewer-paden met strikte ID- en tokenvalidatie.
  * CSP voor viewer-respons: 
    * `default-src 'none'`
    * scripts en assets alleen vanaf self
    * geen uitgaande `connect-src`
  * Throttling van externe missers wanneer externe toegang is ingeschakeld: 
    * 40 fouten per 60 seconden
    * 60 seconden lockout (`429 Too Many Requests`)

Verharding van bestandsweergave

  * Routering van screenshot-browserrequests is standaard geweigerd.
  * Alleen lokale viewer-assets vanaf `http://127.0.0.1/plugins/diffs/assets/*` zijn toegestaan.
  * Externe netwerkrequests worden geblokkeerd.


## Browservereisten voor bestandsmodus

`mode: "file"` en `mode: "both"` hebben een Chromium-compatibele browser nodig.

Volgorde van oplossing:

* ### Config

`browser.executablePath` in de OpenClaw-config.

* ### Omgevingsvariabelen

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Platformfallback

Fallback via platformcommando-/paddetectie.

Veelvoorkomende fouttekst:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Los dit op door Chrome, Chromium, Edge of Brave te installeren, of door een van de opties voor het uitvoerbare pad hierboven in te stellen.

## Probleemoplossing

Invoervalidatiefouten

  * `Provide patch or both before and after text.` — neem zowel `before` als `after` op, of geef `patch` op.
  * `Provide either patch or before/after input, not both.` — meng invoermodi niet.
  * `Invalid baseUrl: ...` — gebruik een `http(s)`-origin met optioneel pad, zonder query/hash.
  * `{field} exceeds maximum size (...)` — verklein de payloadgrootte.
  * Afwijzing van grote patch — verminder het aantal patchbestanden of het totale aantal regels.

Toegankelijkheid van viewer

  * De viewer-URL resolveert standaard naar `127.0.0.1`.
  * Voor scenario's met externe toegang: 
    * stel Plugin `viewerBaseUrl` in, of
    * geef `baseUrl` per toolaanroep mee, of
    * gebruik `gateway.bind=custom` en `gateway.customBindHost`
  * Als `gateway.trustedProxies` loopback bevat voor een proxy op dezelfde host (bijvoorbeeld Tailscale Serve), mislukken ruwe loopback-viewerrequests zonder doorgestuurde client-IP-headers bewust fail-closed.
  * Voor die proxytopologie: 
    * geef de voorkeur aan `mode: "file"` of `mode: "both"` wanneer je alleen een bijlage nodig hebt, of
    * schakel bewust `security.allowRemoteViewer` in en stel Plugin `viewerBaseUrl` in of geef een proxy-/publieke `baseUrl` mee wanneer je een deelbare viewer-URL nodig hebt
  * Schakel `security.allowRemoteViewer` alleen in wanneer je externe viewertoegang bedoelt.

Rij met ongewijzigde regels heeft geen uitklapknop

Dit kan gebeuren bij patchinvoer wanneer de patch geen uitbreidbare context bevat. Dit is verwacht en duidt niet op een viewerfout.

Artefact niet gevonden

  * Artefact verlopen door TTL.
  * Token of pad gewijzigd.
  * Opschoning heeft verouderde data verwijderd.


## Operationele richtlijnen

  * Geef de voorkeur aan `mode: "view"` voor lokale interactieve reviews in canvas.
  * Geef de voorkeur aan `mode: "file"` voor uitgaande chatkanalen die een bijlage nodig hebben.
  * Houd `allowRemoteViewer` uitgeschakeld tenzij je deployment externe viewer-URL's vereist.
  * Stel expliciete korte `ttlSeconds` in voor gevoelige diffs.
  * Vermijd het verzenden van geheimen in diff-invoer wanneer dat niet vereist is.
  * Als je kanaal afbeeldingen agressief comprimeert (bijvoorbeeld Telegram of WhatsApp), geef dan de voorkeur aan PDF-uitvoer (`fileFormat: "pdf"`).


## Gerelateerd

  * [Browser](</nl/tools/browser>)
  * [Plugins](</nl/tools/plugin>)
  * [Tools-overzicht](</nl/tools>)


Was this useful?YesNo
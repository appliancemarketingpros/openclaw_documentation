---
title: API voor browserbesturing
source_url: https://docs.openclaw.ai/nl/tools/browser-control
scraped_at: 2026-05-25
---

Zie [Browser](</nl/tools/browser>) voor installatie, configuratie en probleemoplossing. Deze pagina is de referentie voor de lokale control-HTTP-API, de `openclaw browser` CLI en scriptpatronen (snapshots, refs, waits, debugflows).

## Control-API (optioneel)

Alleen voor lokale integraties stelt de Gateway een kleine local loopback HTTP-API beschikbaar:

  * Status/start/stop: `GET /`, `POST /start`, `POST /stop`
  * Tabs: `GET /tabs`, `POST /tabs/open`, `POST /tabs/focus`, `DELETE /tabs/:targetId`
  * Snapshot/screenshot: `GET /snapshot`, `POST /screenshot`
  * Acties: `POST /navigate`, `POST /act`
  * Hooks: `POST /hooks/file-chooser`, `POST /hooks/dialog`
  * Downloads: `POST /download`, `POST /wait/download`
  * Machtigingen: `POST /permissions/grant`
  * Debugging: `GET /console`, `POST /pdf`
  * Debugging: `GET /errors`, `GET /requests`, `POST /trace/start`, `POST /trace/stop`, `POST /highlight`
  * Netwerk: `POST /response/body`
  * Status: `GET /cookies`, `POST /cookies/set`, `POST /cookies/clear`
  * Status: `GET /storage/:kind`, `POST /storage/:kind/set`, `POST /storage/:kind/clear`
  * Instellingen: `POST /set/offline`, `POST /set/headers`, `POST /set/credentials`, `POST /set/geolocation`, `POST /set/media`, `POST /set/timezone`, `POST /set/locale`, `POST /set/device`


Alle endpoints accepteren `?profile=<name>`. `POST /start?headless=true` vraagt een eenmalige headless start aan voor lokaal beheerde profielen zonder de permanente browserconfiguratie te wijzigen; profielen voor attach-only, externe CDP en bestaande sessies wijzen die override af omdat OpenClaw die browserprocessen niet start.

Als shared-secret-authenticatie voor de Gateway is geconfigureerd, vereisen browser-HTTP-routes ook authenticatie:

  * `Authorization: Bearer <gateway token>`
  * `x-openclaw-password: <gateway password>` of HTTP Basic-authenticatie met dat wachtwoord


Opmerkingen:

  * Deze zelfstandige local loopback browser-API gebruikt **geen** vertrouwde-proxy- of Tailscale Serve-identiteitsheaders.
  * Als `gateway.auth.mode` `none` of `trusted-proxy` is, nemen deze local loopback browser- routes die identiteitsdragende modi niet over; houd ze uitsluitend op local loopback.


### `/act`-foutcontract

`POST /act` gebruikt een gestructureerd foutantwoord voor validatie op routeniveau en policyfouten:

jsonCopy code
[code]
    { "error": "<message>", "code": "ACT_*" }
[/code]

Huidige `code`-waarden:

  * `ACT_KIND_REQUIRED` (HTTP 400): `kind` ontbreekt of wordt niet herkend.
  * `ACT_INVALID_REQUEST` (HTTP 400): de actiepayload is niet door normalisatie of validatie gekomen.
  * `ACT_SELECTOR_UNSUPPORTED` (HTTP 400): `selector` is gebruikt met een niet-ondersteund actietype.
  * `ACT_EVALUATE_DISABLED` (HTTP 403): `evaluate` (of `wait --fn`) is uitgeschakeld door de configuratie.
  * `ACT_TARGET_ID_MISMATCH` (HTTP 403): `targetId` op topniveau of in batches conflicteert met het aanvraagtarged.
  * `ACT_EXISTING_SESSION_UNSUPPORTED` (HTTP 501): de actie wordt niet ondersteund voor bestaande-sessieprofielen.


Andere runtimefouten kunnen nog steeds `{ "error": "<message>" }` retourneren zonder een `code`-veld.

### Playwright-vereiste

Sommige functies (navigate/act/AI-snapshot/rolsnapshot, elementscreenshots, PDF) vereisen Playwright. Als Playwright niet is geïnstalleerd, retourneren die endpoints een duidelijke 501-fout.

Wat nog werkt zonder Playwright:

  * ARIA-snapshots
  * Rolachtige toegankelijkheidssnapshots (`--interactive`, `--compact`, `--depth`, `--efficient`) wanneer een CDP-WebSocket per tabblad beschikbaar is. Dit is een fallback voor inspectie en ref-ontdekking; Playwright blijft de primaire actie-engine.
  * Paginascreenshots voor de beheerde `openclaw`-browser wanneer een CDP- WebSocket per tabblad beschikbaar is
  * Paginascreenshots voor `existing-session` / Chrome MCP-profielen
  * Op refs gebaseerde `existing-session`-screenshots (`--ref`) uit snapshotuitvoer


Wat nog steeds Playwright nodig heeft:

  * `navigate`
  * `act`
  * AI-snapshots die afhankelijk zijn van Playwrights native AI-snapshotformaat
  * Elementscreenshots met CSS-selector (`--element`)
  * volledige browser-PDF-export


Elementscreenshots wijzen ook `--full-page` af; de route retourneert `fullPage is not supported for element screenshots`.

Als je `Playwright is not available in this gateway build` ziet, mist de verpakte Gateway de kernruntime-afhankelijkheid voor browsers. Installeer OpenClaw opnieuw of werk het bij, en herstart daarna de Gateway. Installeer voor Docker ook de Chromium- browserbinaries zoals hieronder weergegeven.

#### Docker Playwright-installatie

Als je Gateway in Docker draait, vermijd dan `npx playwright` (npm-overrideconflicten). Bak voor aangepaste images Chromium in de image:

bashCopy code
[code]
    OPENCLAW_INSTALL_BROWSER=1 ./scripts/docker/setup.sh
[/code]

Installeer voor een bestaande image in plaats daarvan via de gebundelde CLI:

bashCopy code
[code]
    docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

Om browserdownloads persistent te maken, stel je `PLAYWRIGHT_BROWSERS_PATH` in (bijvoorbeeld `/home/node/.cache/ms-playwright`) en zorg je dat `/home/node` persistent is via `OPENCLAW_HOME_VOLUME` of een bind mount. OpenClaw detecteert de persistente Chromium automatisch op Linux. Zie [Docker](</nl/install/docker>).

## Hoe het werkt (intern)

Een kleine local loopback control-server accepteert HTTP-verzoeken en maakt verbinding met Chromium-gebaseerde browsers via CDP. Geavanceerde acties (click/type/snapshot/PDF) lopen via Playwright boven op CDP; wanneer Playwright ontbreekt, zijn alleen niet-Playwright-bewerkingen beschikbaar. De agent ziet één stabiele interface terwijl lokale/externe browsers en profielen eronder vrij worden gewisseld.

## CLI-snelreferentie

Alle opdrachten accepteren `--browser-profile <name>` om een specifiek profiel te targeten, en `--json` voor machineleesbare uitvoer.

Basis: status, tabbladen, openen/focussen/sluiten bashCopy code
[code]
    openclaw browser statusopenclaw browser startopenclaw browser start --headless # eenmalige lokaal beheerde headless startopenclaw browser stop            # wist ook emulatie op attach-only/externe CDPopenclaw browser tabsopenclaw browser tab             # snelkoppeling voor huidig tabbladopenclaw browser tab newopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://example.comopenclaw browser focus abcd1234openclaw browser close abcd1234
[/code]

Inspectie: screenshot, snapshot, console, fouten, verzoeken bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref 12        # of --ref e12openclaw browser screenshot --labelsopenclaw browser snapshotopenclaw browser snapshot --format aria --limit 200openclaw browser snapshot --interactive --compact --depth 6openclaw browser snapshot --efficientopenclaw browser snapshot --labelsopenclaw browser snapshot --urlsopenclaw browser snapshot --selector "#main" --interactiveopenclaw browser snapshot --frame "iframe#main" --interactiveopenclaw browser console --level erroropenclaw browser errors --clearopenclaw browser requests --filter api --clearopenclaw browser pdfopenclaw browser responsebody "**/api" --max-chars 5000
[/code]

Acties: navigeren, klikken, typen, slepen, wachten, evalueren bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser resize 1280 720openclaw browser click 12 --double           # of e12 voor rolrefsopenclaw browser click-coords 120 340        # viewportcoördinatenopenclaw browser type 23 "hello" --submitopenclaw browser press Enteropenclaw browser hover 44openclaw browser scrollintoview e12openclaw browser drag 10 11openclaw browser select 9 OptionA OptionBopenclaw browser download e12 report.pdfopenclaw browser waitfordownload report.pdfopenclaw browser upload /tmp/openclaw/uploads/file.pdfopenclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'openclaw browser dialog --acceptopenclaw browser wait --text "Done"openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"openclaw browser evaluate --fn '(el) => el.textContent' --ref 7openclaw browser highlight e12openclaw browser trace startopenclaw browser trace stop
[/code]

Status: cookies, storage, offline, headers, geo, apparaat bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url "https://example.com"openclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set theme darkopenclaw browser storage session clearopenclaw browser set offline onopenclaw browser set headers --headers-json '{"X-Debug":"1"}'openclaw browser set credentials user pass            # --clear om te verwijderenopenclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"openclaw browser set media darkopenclaw browser set timezone America/New_Yorkopenclaw browser set locale en-USopenclaw browser set device "iPhone 14"
[/code]

Opmerkingen:

  * `upload` en `dialog` zijn **voorbereidende** calls; voer ze uit vóór de klik/toetsdruk die de chooser/dialog activeert.
  * `click`/`type`/enzovoort vereisen een `ref` uit `snapshot` (numerieke `12`, rolref `e12`, of uitvoerbare ARIA-ref `ax12`). CSS-selectors worden bewust niet ondersteund voor acties. Gebruik `click-coords` wanneer de zichtbare viewportpositie het enige betrouwbare doel is.
  * Download-, trace- en uploadpaden zijn beperkt tot OpenClaw-temproots: `/tmp/openclaw{,/downloads,/uploads}` (fallback: `${os.tmpdir()}/openclaw/...`).
  * `upload` kan bestandsinputs ook rechtstreeks instellen via `--input-ref` of `--element`.


Stabiele tabblad-id's en labels overleven vervanging van raw Chromium-targets wanneer OpenClaw de vervangende tab kan bewijzen, zoals dezelfde URL of één oud tabblad dat na formulierverzending één nieuw tabblad wordt. Raw target-id's blijven vluchtig; geef in scripts de voorkeur aan `suggestedTargetId` uit `tabs`.

Snapshotflags in één oogopslag:

  * `--format ai` (standaard met Playwright): AI-snapshot met numerieke refs (`aria-ref="<n>"`).
  * `--format aria`: toegankelijkheidsboom met `axN`-refs. Wanneer Playwright beschikbaar is, bindt OpenClaw refs met backend-DOM-id's aan de live pagina zodat vervolgacties ze kunnen gebruiken; behandel de uitvoer anders als uitsluitend voor inspectie.
  * `--efficient` (of `--mode efficient`): compacte voorinstelling voor rolsnapshot. Stel `browser.snapshotDefaults.mode: "efficient"` in om dit de standaard te maken (zie [Gateway-configuratie](</nl/gateway/configuration-reference#browser>)).
  * `--interactive`, `--compact`, `--depth`, `--selector` forceren een rolsnapshot met `ref=e12`-refs. `--frame "<iframe>"` beperkt rolsnapshots tot een iframe.
  * `--labels` voegt een viewport-only screenshot toe met overlay-reflabels (print `MEDIA:<path>`).
  * `--urls` voegt gevonden linkbestemmingen toe aan AI-snapshots.


## Snapshots en refs

OpenClaw ondersteunt twee "snapshot"-stijlen:

  * **AI-snapshot (numerieke refs)** : `openclaw browser snapshot` (standaard; `--format ai`)

    * Uitvoer: een tekstsnapshot met numerieke refs.
    * Acties: `openclaw browser click 12`, `openclaw browser type 23 "hello"`.
    * Intern wordt de ref opgelost via Playwrights `aria-ref`.
  * **Rolsnapshot (rolrefs zoals`e12`)**: `openclaw browser snapshot --interactive` (of `--compact`, `--depth`, `--selector`, `--frame`)

    * Uitvoer: een rolgebaseerde lijst/boom met `[ref=e12]` (en optioneel `[nth=1]`).
    * Acties: `openclaw browser click e12`, `openclaw browser highlight e12`.
    * Intern wordt de ref opgelost via `getByRole(...)` (plus `nth()` voor duplicaten).
    * Voeg `--labels` toe om een viewportscreenshot met overlay-`e12`-labels op te nemen.
    * Voeg `--urls` toe wanneer linktekst ambigu is en de agent concrete navigatiedoelen nodig heeft.
  * **ARIA-snapshot (ARIA-verwijzingen zoals`ax12`)**: `openclaw browser snapshot --format aria`

    * Uitvoer: de toegankelijkheidsboom als gestructureerde knooppunten.
    * Acties: `openclaw browser click ax12` werkt wanneer het snapshotpad de verwijzing via Playwright en DOM-id's van de Chrome-backend kan binden.
  * Als Playwright niet beschikbaar is, kunnen ARIA-snapshots nog steeds nuttig zijn voor inspectie, maar verwijzingen zijn mogelijk niet uitvoerbaar. Maak opnieuw een snapshot met `--format ai` of `--interactive` wanneer je actieverwijzingen nodig hebt.

  * Docker-bewijs voor het raw-CDP-terugvalpad: `pnpm test:docker:browser-cdp-snapshot` start Chromium met CDP, voert `browser doctor --deep` uit en verifieert dat rolsnapshots link-URL's, door de cursor gepromoveerde klikbare elementen en iframe-metadata bevatten.


Gedrag van verwijzingen:

  * Verwijzingen zijn **niet stabiel tussen navigaties** ; als iets mislukt, voer `snapshot` opnieuw uit en gebruik een nieuwe verwijzing.
  * `/act` retourneert de huidige ruwe `targetId` na door een actie veroorzaakte vervanging wanneer het het vervangende tabblad kan bewijzen. Blijf stabiele tabblad-id's/labels gebruiken voor vervolgopdrachten.
  * Als de rolsnapshot met `--frame` is gemaakt, zijn rolverwijzingen beperkt tot dat iframe tot de volgende rolsnapshot.
  * Onbekende of verouderde `axN`-verwijzingen mislukken snel in plaats van door te vallen naar Playwrights `aria-ref`-selector. Voer een nieuwe snapshot uit op hetzelfde tabblad wanneer dat gebeurt.


## Krachtigere wachtopties

Je kunt op meer wachten dan alleen tijd/tekst:

  * Wachten op URL (globs ondersteund door Playwright): 
    * `openclaw browser wait --url "**/dash"`
  * Wachten op laadstatus: 
    * `openclaw browser wait --load networkidle`
  * Wachten op een JS-predicaat: 
    * `openclaw browser wait --fn "window.ready===true"`
  * Wachten tot een selector zichtbaar wordt: 
    * `openclaw browser wait "#main"`


Deze kunnen worden gecombineerd:

bashCopy code
[code]
    openclaw browser wait "#main" \  --url "**/dash" \  --load networkidle \  --fn "window.ready===true" \  --timeout-ms 15000
[/code]

## Debug-workflows

Wanneer een actie mislukt (bijv. "niet zichtbaar", "strict mode violation", "bedekt"):

  1. `openclaw browser snapshot --interactive`
  2. Gebruik `click <ref>` / `type <ref>` (geef in interactieve modus de voorkeur aan rolverwijzingen)
  3. Als het nog steeds mislukt: `openclaw browser highlight <ref>` om te zien waarop Playwright mikt
  4. Als de pagina zich vreemd gedraagt: 
     * `openclaw browser errors --clear`
     * `openclaw browser requests --filter api --clear`
  5. Voor diepgaand debuggen: neem een trace op: 
     * `openclaw browser trace start`
     * reproduceer het probleem
     * `openclaw browser trace stop` (print `TRACE:<path>`)


## JSON-uitvoer

`--json` is bedoeld voor scripting en gestructureerde tooling.

Voorbeelden:

bashCopy code
[code]
    openclaw browser status --jsonopenclaw browser snapshot --interactive --jsonopenclaw browser requests --filter api --jsonopenclaw browser cookies --json
[/code]

Rolsnapshots in JSON bevatten `refs` plus een klein `stats`-blok (lines/chars/refs/interactive), zodat tools kunnen redeneren over payloadgrootte en -dichtheid.

## Status- en omgevingsknoppen

Deze zijn handig voor workflows zoals "laat de site zich gedragen als X":

  * Cookies: `cookies`, `cookies set`, `cookies clear`
  * Opslag: `storage local|session get|set|clear`
  * Offline: `set offline on|off`
  * Headers: `set headers --headers-json '{"X-Debug":"1"}'` (verouderde `set headers --json '{"X-Debug":"1"}'` blijft ondersteund)
  * HTTP-basisverificatie: `set credentials user pass` (of `--clear`)
  * Geolocatie: `set geo <lat> <lon> --origin "https://example.com"` (of `--clear`)
  * Media: `set media dark|light|no-preference|none`
  * Tijdzone / locale: `set timezone ...`, `set locale ...`
  * Apparaat / viewport: 
    * `set device "iPhone 14"` (Playwright-apparaatpresets)
    * `set viewport 1280 720`


## Beveiliging en privacy

  * Het openclaw-browserprofiel kan ingelogde sessies bevatten; behandel het als gevoelig.
  * `browser act kind=evaluate` / `openclaw browser evaluate` en `wait --fn` voeren willekeurige JavaScript uit in de paginacontext. Promptinjectie kan dit sturen. Schakel dit uit met `browser.evaluateEnabled=false` als je het niet nodig hebt.
  * Zie [Browserlogin + X/Twitter plaatsen](</nl/tools/browser-login>) voor aanmeldingen en anti-bot-opmerkingen (X/Twitter, enzovoort).
  * Houd de Gateway/Node-host privé (loopback of alleen tailnet).
  * Externe CDP-eindpunten zijn krachtig; tunnel en bescherm ze.


Voorbeeld van strikte modus (blokkeer standaard privé/interne bestemmingen):

json5Copy code
[code]
    {  browser: {    ssrfPolicy: {      dangerouslyAllowPrivateNetwork: false,      hostnameAllowlist: ["*.example.com", "example.com"],      allowedHostnames: ["localhost"], // optional exact allow    },  },}
[/code]

## Gerelateerd

  * [Browser](</nl/tools/browser>) \- overzicht, configuratie, profielen, beveiliging
  * [Browserlogin](</nl/tools/browser-login>) \- aanmelden bij sites
  * [Browser Linux-probleemoplossing](</nl/tools/browser-linux-troubleshooting>)
  * [Browser WSL2-probleemoplossing](</nl/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo
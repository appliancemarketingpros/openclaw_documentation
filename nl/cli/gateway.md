---
title: Gateway
source_url: https://docs.openclaw.ai/nl/cli/gateway
scraped_at: 2026-05-25
---

De Gateway is de WebSocket-server van OpenClaw (kanalen, nodes, sessies, hooks). Subcommando's op deze pagina vallen onder `openclaw gateway …`.

[**Bonjour discovery** Lokale mDNS + wide-area DNS-SD-installatie. ](</nl/gateway/bonjour>) [**Discovery overview** Hoe OpenClaw gateways adverteert en vindt. ](</nl/gateway/discovery>) [**Configuration** Gateway-configuratiesleutels op hoofdniveau. ](</nl/gateway/configuration>)

## De Gateway uitvoeren

Voer een lokaal Gateway-proces uit:

bashCopy code
[code]
    openclaw gateway
[/code]

Alias voor de voorgrond:

bashCopy code
[code]
    openclaw gateway run
[/code]

Startup behavior

  * Standaard weigert de Gateway te starten tenzij `gateway.mode=local` is ingesteld in `~/.openclaw/openclaw.json`. Gebruik `--allow-unconfigured` voor ad-hoc-/dev-runs.
  * Van `openclaw onboard --mode local` en `openclaw setup` wordt verwacht dat ze `gateway.mode=local` schrijven. Als het bestand bestaat maar `gateway.mode` ontbreekt, behandel dat dan als een defecte of overschreven configuratie en herstel die in plaats van impliciet de lokale modus aan te nemen.
  * Als het bestand bestaat en `gateway.mode` ontbreekt, behandelt de Gateway dat als verdachte configuratieschade en weigert hij voor jou "lokaal te raden".
  * Binden buiten loopback zonder auth wordt geblokkeerd (veiligheidsvangrail).
  * `SIGUSR1` activeert een herstart binnen het proces wanneer dit is geautoriseerd (`commands.restart` is standaard ingeschakeld; stel `commands.restart: false` in om handmatig herstarten te blokkeren, terwijl gateway-tool/config apply/update toegestaan blijven).
  * `SIGINT`/`SIGTERM`-handlers stoppen het gateway-proces, maar ze herstellen geen aangepaste terminalstatus. Als je de CLI omwikkelt met een TUI of raw-mode-invoer, herstel dan de terminal vóór het afsluiten.


### Opties

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> WebSocket-poort (standaard komt uit config/env; meestal `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Tokenoverschrijving (stelt ook `OPENCLAW_GATEWAY_TOKEN` in voor het proces).

Reset de Tailscale serve/funnel-configuratie bij afsluiten.

Sta toe dat de gateway start zonder `gateway.mode=local` in de configuratie. Omzeilt de startup-bescherming alleen voor ad-hoc-/dev-bootstrap; schrijft of herstelt het configuratiebestand niet.

Maak een dev-configuratie + werkruimte aan als die ontbreekt (slaat [BOOTSTRAP.md](<http://BOOTSTRAP.md>) over).

Reset dev-configuratie + referenties + sessies + werkruimte (vereist `--dev`).

Beëindig elke bestaande listener op de geselecteerde poort vóór het starten.

Uitgebreide logs.

Toon alleen CLI-backendlogs in de console (en schakel stdout/stderr in).

Alias voor `--ws-log compact`.

Log onbewerkte modelstream-events naar jsonl.

## De Gateway herstarten

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` vraagt de actieve Gateway om actief OpenClaw-werk vooraf te controleren voordat er wordt herstart. Als bewerkingen in de wachtrij, afleveren van antwoorden, ingebedde runs of taakruns actief zijn, rapporteert de Gateway de blokkades, voegt hij dubbele veilige herstartverzoeken samen en herstart hij zodra het actieve werk is afgehandeld. Gewoon `restart` behoudt het bestaande gedrag van de servicemanager voor compatibiliteit. Gebruik `--force` alleen wanneer je expliciet het directe overschrijvingspad wilt.

`openclaw gateway restart --safe --skip-deferral` voert dezelfde OpenClaw-bewuste gecoördineerde herstart uit als `--safe`, maar omzeilt de uitstelpoort voor actief werk zodat de Gateway de herstart onmiddellijk uitzendt, zelfs wanneer er blokkades worden gerapporteerd. Gebruik dit als de nooduitgang voor operators wanneer uitstel is vastgezet door een vastgelopen taakrun en alleen `--safe` onbeperkt zou wachten. `--skip-deferral` vereist `--safe`.

### Startup-profiling

  * Stel `OPENCLAW_GATEWAY_STARTUP_TRACE=1` in om fasetimings tijdens het starten van de Gateway te loggen, inclusief per-fase `eventLoopMax`-vertraging en timings van Plugin-opzoektabellen voor installed-index, manifestregister, startup-planning en owner-map-werk.
  * Stel `OPENCLAW_DIAGNOSTICS=timeline` in met `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` om een best-effort JSONL-startupdiagnostiektijdlijn te schrijven voor externe QA-harnassen. Je kunt de vlag ook inschakelen met `diagnostics.flags: ["timeline"]` in de configuratie; het pad wordt nog steeds via env geleverd. Voeg `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` toe om event-loop-samples op te nemen.
  * Voer `pnpm test:startup:gateway -- --runs 5 --warmup 1` uit om de startup van de Gateway te benchmarken. De benchmark registreert eerste procesuitvoer, `/healthz`, `/readyz`, startup-tracetimings, event-loop-vertraging en timingdetails van Plugin-opzoektabellen.


## Een actieve Gateway opvragen

Alle querycommando's gebruiken WebSocket-RPC.

### Output modes

  * Standaard: menselijk leesbaar (gekleurd in TTY).
  * `--json`: machineleesbare JSON (geen styling/spinner).
  * `--no-color` (of `NO_COLOR=1`): schakel ANSI uit terwijl de menselijke lay-out behouden blijft.


### Shared options

  * `--url <url>`: Gateway-WebSocket-URL.
  * `--token <token>`: Gateway-token.
  * `--password <password>`: Gateway-wachtwoord.
  * `--timeout <ms>`: time-out/budget (verschilt per commando).
  * `--expect-final`: wacht op een "final"-respons (agent-aanroepen).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

Het HTTP-`/healthz`-endpoint is een liveness-probe: het retourneert zodra de server HTTP kan beantwoorden. Het HTTP-`/readyz`-endpoint is strenger en blijft rood zolang startup-Plugin-sidecars, kanalen of geconfigureerde hooks nog aan het stabiliseren zijn. Lokale of geauthenticeerde gedetailleerde readiness-responsen bevatten een diagnostisch `eventLoop`-blok met event-loop-vertraging, event-loop-gebruik, CPU-coreverhouding en een `degraded`-vlag.

### `gateway usage-cost`

Haal usage-cost-samenvattingen op uit sessielogs.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

Haal de recente diagnostische stabiliteitsrecorder op uit een actieve Gateway.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Maximumaantal recente events om op te nemen (max `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> Filter op diagnostisch eventtype, zoals `payload.large` of `diagnostic.memory.pressure`.

Lees een opgeslagen stabiliteitsbundel in plaats van de actieve Gateway aan te roepen. Gebruik `--bundle latest` (of alleen `--bundle`) voor de nieuwste bundel onder de statusmap, of geef direct een JSON-pad voor een bundel door.

Schrijf een deelbare supportdiagnostiek-zip in plaats van stabiliteitsdetails af te drukken.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> Uitvoerpad voor `--export`.

Privacy and bundle behavior

  * Records bewaren operationele metadata: eventnamen, aantallen, bytegroottes, geheugenuitlezingen, wachtrij-/sessiestatus, kanaal-/Plugin-namen en geredigeerde sessiesamenvattingen. Ze bewaren geen chattekst, webhook-bodies, tooluitvoer, onbewerkte request- of response-bodies, tokens, cookies, geheime waarden, hostnamen of onbewerkte sessie-id's. Stel `diagnostics.enabled: false` in om de recorder volledig uit te schakelen.
  * Bij fatale Gateway-afsluitingen, shutdown-time-outs en startup-fouten bij herstart schrijft OpenClaw dezelfde diagnostische snapshot naar `~/.openclaw/logs/stability/openclaw-stability-*.json` wanneer de recorder events heeft. Inspecteer de nieuwste bundel met `openclaw gateway stability --bundle latest`; `--limit`, `--type` en `--since-seq` zijn ook van toepassing op bundeluitvoer.


### `gateway diagnostics export`

Schrijf een lokale diagnostiek-zip die is bedoeld om aan bugrapporten toe te voegen. Zie [Diagnostiekexport](</nl/gateway/diagnostics>) voor het privacymodel en de bundelinhoud.

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Sla het opzoeken van opgeslagen stabiliteitsbundels over.

Druk het geschreven pad, de grootte en het manifest af als JSON.

De export bevat een manifest, een Markdown-samenvatting, configuratievorm, gesaneerde configuratiedetails, gesaneerde logsamenvattingen, gesaneerde Gateway-status-/health-snapshots en de nieuwste stabiliteitsbundel wanneer die bestaat.

Deze is bedoeld om te delen. De export bewaart operationele details die helpen bij debugging, zoals veilige OpenClaw-logvelden, subsysteemnamen, statuscodes, duur, geconfigureerde modi, poorten, Plugin-id's, provider-id's, niet-geheime functie-instellingen en geredigeerde operationele logberichten. Chattekst, webhook-bodies, tooluitvoer, referenties, cookies, account-/bericht-id's, prompt-/instructietekst, hostnamen en geheime waarden worden weggelaten of geredigeerd. Wanneer een LogTape-achtig bericht op tekst van een gebruiker-/chat-/tool-payload lijkt, bewaart de export alleen dat een bericht is weggelaten plus het aantal bytes ervan.

### `gateway status`

`gateway status` toont de Gateway-service (launchd/systemd/schtasks) plus een optionele probe van connectiviteit/auth-capaciteit.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Sla de connectiviteitsprobe over (alleen serviceweergave).

Scan ook services op systeemniveau.

Upgrade de standaardconnectiviteitsprobe naar een leesprobe en sluit af met een niet-nulcode wanneer die leesprobe mislukt. Kan niet worden gecombineerd met `--no-probe`.

Status semantics

  * `gateway status` blijft beschikbaar voor diagnostiek, zelfs wanneer de lokale CLI-configuratie ontbreekt of ongeldig is.
  * Standaard `gateway status` bewijst servicestatus, WebSocket-verbinding en de auth-capability die zichtbaar is tijdens de handshake. Het bewijst geen lees-/schrijf-/adminbewerkingen.
  * Diagnostische probes muteren niets voor eerste apparaatauthenticatie: ze hergebruiken een bestaande gecachte apparaattoken wanneer die bestaat, maar ze maken geen nieuwe CLI-apparaatidentiteit of alleen-lezen apparaatkoppelingsrecord aan alleen om status te controleren.
  * `gateway status` lost geconfigureerde auth SecretRefs voor probe-authenticatie op wanneer dat mogelijk is.
  * Als een vereiste auth SecretRef in dit commandopad niet is opgelost, rapporteert `gateway status --json` `rpc.authWarning` wanneer probe-connectiviteit/authenticatie mislukt; geef `--token`/`--password` expliciet door of los eerst de secret-bron op.
  * Als de probe slaagt, worden waarschuwingen over niet-opgeloste auth-refs onderdrukt om fout-positieven te vermijden.
  * Gebruik `--require-rpc` in scripts en automatisering wanneer een luisterende service niet genoeg is en ook RPC-aanroepen met leesbereik gezond moeten zijn.
  * `--deep` voegt een best-effort scan toe voor extra launchd/systemd/schtasks-installaties. Wanneer meerdere gateway-achtige services worden gedetecteerd, toont de menselijke uitvoer opruimhints en waarschuwt die dat de meeste opstellingen één Gateway per machine zouden moeten draaien.
  * `--deep` rapporteert ook een recente Gateway supervisor-herstartoverdracht wanneer het serviceproces netjes is afgesloten voor een externe supervisor-herstart.
  * `--deep` voert configuratievalidatie uit in plugin-bewuste modus (`pluginValidation: "full"`) en toont geconfigureerde waarschuwingen uit Plugin-manifests (bijvoorbeeld ontbrekende kanaalconfiguratiemetadata), zodat install- en update-smokechecks ze vinden. Standaard `gateway status` behoudt het snelle alleen-lezen pad dat pluginvalidatie overslaat.
  * Menselijke uitvoer bevat het opgeloste pad naar het bestandslog plus een snapshot van CLI-versus-serviceconfiguratiepaden/geldigheid om profiel- of state-dir-afwijkingen te helpen diagnosticeren.

Linux systemd auth-drift checks

  * Op Linux systemd-installaties lezen service-auth-driftcontroles zowel `Environment=`\- als `EnvironmentFile=`-waarden uit de unit (inclusief `%h`, paden tussen aanhalingstekens, meerdere bestanden en optionele `-`-bestanden).
  * Driftcontroles lossen `gateway.auth.token` SecretRefs op met samengevoegde runtime-env (eerst servicecommando-env, daarna process-env als fallback).
  * Als token-auth niet effectief actief is (expliciete `gateway.auth.mode` van `password`/`none`/`trusted-proxy`, of modus niet ingesteld waarbij wachtwoord kan winnen en geen tokenkandidaat kan winnen), slaan token-driftcontroles configuratietokenresolutie over.


### `gateway probe`

`gateway probe` is het commando voor "alles debuggen". Het proeft altijd:

  * je geconfigureerde externe Gateway (indien ingesteld), en
  * localhost (loopback) **zelfs als remote is geconfigureerd**.


Als je `--url` doorgeeft, wordt dat expliciete doel vóór beide toegevoegd. Menselijke uitvoer labelt de doelen als:

  * `URL (explicit)`
  * `Remote (configured)` of `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Interpretation

  * `Reachable: yes` betekent dat ten minste één doel een WebSocket-verbinding heeft geaccepteerd.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` rapporteert wat de probe over auth kon bewijzen. Dit staat los van bereikbaarheid.
  * `Read probe: ok` betekent dat RPC-aanroepen voor details met leesbereik (`health`/`status`/`system-presence`/`config.get`) ook zijn geslaagd.
  * `Read probe: limited - missing scope: operator.read` betekent dat de verbinding is geslaagd, maar RPC met leesbereik beperkt is. Dit wordt gerapporteerd als **verminderde** bereikbaarheid, niet als volledige fout.
  * `Read probe: failed` na `Connect: ok` betekent dat de Gateway de WebSocket-verbinding heeft geaccepteerd, maar dat vervolgleesdiagnostiek is verlopen of mislukt. Dit is ook **verminderde** bereikbaarheid, geen onbereikbare Gateway.
  * Net als `gateway status` hergebruikt probe bestaande gecachte apparaatauthenticatie, maar maakt het geen eerste apparaatidentiteit of koppelingsstatus aan.
  * De exitcode is alleen niet-nul wanneer geen enkel geprobed doel bereikbaar is.

JSON output

Hoogste niveau:

  * `ok`: ten minste één doel is bereikbaar.
  * `degraded`: ten minste één doel heeft een verbinding geaccepteerd, maar heeft de volledige detail-RPC-diagnostiek niet voltooid.
  * `capability`: beste capability die over bereikbare doelen is gezien (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` of `unknown`).
  * `primaryTargetId`: beste doel om als actieve winnaar te behandelen in deze volgorde: expliciete URL, SSH-tunnel, geconfigureerde remote en daarna local loopback.
  * `warnings[]`: best-effort waarschuwingsrecords met `code`, `message` en optionele `targetIds`.
  * `network`: hints voor local loopback-/tailnet-URL's afgeleid van de huidige configuratie en hostnetwerken.
  * `discovery.timeoutMs` en `discovery.count`: het daadwerkelijke discovery-budget/resultaantal dat voor deze probe-run is gebruikt.


Per doel (`targets[].connect`):

  * `ok`: bereikbaarheid na verbinding + degraded-classificatie.
  * `rpcOk`: volledig detail-RPC-succes.
  * `scopeLimited`: detail-RPC is mislukt door ontbrekend operatorbereik.


Per doel (`targets[].auth`):

  * `role`: auth-rol gerapporteerd in `hello-ok` wanneer beschikbaar.
  * `scopes`: toegekende scopes gerapporteerd in `hello-ok` wanneer beschikbaar.
  * `capability`: de getoonde auth-capabilityclassificatie voor dat doel.

Common warning codes

  * `ssh_tunnel_failed`: SSH-tunnelconfiguratie is mislukt; het commando viel terug op directe probes.
  * `multiple_gateways`: meer dan één doel was bereikbaar; dit is ongebruikelijk tenzij je bewust geïsoleerde profielen draait, zoals een rescue-bot.
  * `auth_secretref_unresolved`: een geconfigureerde auth SecretRef kon niet worden opgelost voor een mislukt doel.
  * `probe_scope_limited`: WebSocket-verbinding is geslaagd, maar de leesprobe werd beperkt door ontbrekende `operator.read`.


#### Remote via SSH (pariteit met Mac-app)

De macOS-appmodus "Remote via SSH" gebruikt een lokale port-forward zodat de externe Gateway (die mogelijk alleen aan loopback gebonden is) bereikbaar wordt op `ws://127.0.0.1:<port>`.

CLI-equivalent:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` of `user@host:port` (poort is standaard `22`).

Kies de eerste ontdekte Gateway-host als SSH-doel uit het opgeloste discovery-eindpunt (`local.` plus het geconfigureerde wide-area-domein, indien aanwezig). TXT-only hints worden genegeerd.

Configuratie (optioneel, gebruikt als standaardwaarden):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Low-level RPC-helper.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

Vooral voor agent-achtige RPC's die tussentijdse events streamen vóór een finale payload.

Machineleesbare JSON-uitvoer.

## De Gateway-service beheren

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Installeren met een wrapper

Gebruik `--wrapper` wanneer de beheerde service via een ander uitvoerbaar bestand moet starten, bijvoorbeeld een secrets manager-shim of een run-as-helper. De wrapper ontvangt de normale Gateway-argumenten en is verantwoordelijk voor het uiteindelijk exec'en van `openclaw` of Node met die argumenten.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Je kunt de wrapper ook via de omgeving instellen. `gateway install` valideert dat het pad een uitvoerbaar bestand is, schrijft de wrapper naar service `ProgramArguments` en bewaart `OPENCLAW_WRAPPER` in de serviceomgeving voor latere geforceerde herinstallaties, updates en doctor- reparaties.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Om een bewaarde wrapper te verwijderen, maak je `OPENCLAW_WRAPPER` leeg tijdens het opnieuw installeren:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Command options

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Levenscyclusgedrag

  * Gebruik `gateway restart` om een beheerde service opnieuw te starten. Koppel `gateway stop` en `gateway start` niet aan elkaar als vervanging voor opnieuw starten.
  * Op macOS gebruikt `gateway stop` standaard `launchctl bootout`, waarmee de LaunchAgent uit de huidige opstartsessie wordt verwijderd zonder een uitschakeling blijvend te maken — automatische KeepAlive-herstel blijft actief voor toekomstige crashes en `gateway start` schakelt opnieuw netjes in zonder handmatige `launchctl enable`. Geef `--disable` door om KeepAlive en RunAtLoad blijvend te onderdrukken, zodat de gateway niet opnieuw start tot de volgende expliciete `gateway start`; gebruik dit wanneer een handmatige stop herstarts of systeemherstarts moet overleven.
  * `gateway restart --safe` vraagt de draaiende Gateway om actief OpenClaw-werk vooraf te controleren en de herstart uit te stellen totdat antwoordlevering, ingesloten runs en taakruns zijn leeggemaakt. `--safe` kan niet worden gecombineerd met `--force` of `--wait`.
  * `gateway restart --wait 30s` overschrijft het geconfigureerde drainbudget voor die herstart. Kale getallen zijn milliseconden; eenheden zoals `s`, `m` en `h` worden geaccepteerd. `--wait 0` wacht onbeperkt.
  * `gateway restart --safe --skip-deferral` voert de OpenClaw-bewuste veilige herstart uit, maar omzeilt de uitstelpoort zodat de Gateway de herstart onmiddellijk uitstoot, zelfs wanneer blokkades worden gemeld. Nooduitgang voor operators bij vastgelopen taakrun-uitstel; vereist `--safe`.
  * `gateway restart --force` slaat het leegmaken van actief werk over en start onmiddellijk opnieuw. Gebruik dit wanneer een operator de vermelde taakblokkades al heeft gecontroleerd en de gateway nu terug wil.
  * Levenscyclusopdrachten accepteren `--json` voor scripting.

Authenticatie en SecretRefs tijdens installatie

  * Wanneer tokenauthenticatie een token vereist en `gateway.auth.token` door SecretRef wordt beheerd, valideert `gateway install` dat de SecretRef oplosbaar is, maar wordt het opgeloste token niet opgeslagen in service-omgevingsmetadata.
  * Als tokenauthenticatie een token vereist en de geconfigureerde token-SecretRef niet oplosbaar is, mislukt de installatie gesloten in plaats van terugval-plattetekst op te slaan.
  * Geef voor wachtwoordauthenticatie bij `gateway run` de voorkeur aan `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` of een door SecretRef ondersteunde `gateway.auth.password` boven inline `--password`.
  * In afgeleide authenticatiemodus versoepelt shell-only `OPENCLAW_GATEWAY_PASSWORD` de tokenvereisten voor installatie niet; gebruik duurzame configuratie (`gateway.auth.password` of config `env`) bij het installeren van een beheerde service.
  * Als zowel `gateway.auth.token` als `gateway.auth.password` zijn geconfigureerd en `gateway.auth.mode` niet is ingesteld, wordt installatie geblokkeerd totdat de modus expliciet is ingesteld.


## Gateways ontdekken (Bonjour)

`gateway discover` scant op Gateway-bakens (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): kies een domein (voorbeeld: `openclaw.internal.`) en stel split DNS + een DNS-server in; zie [Bonjour](</nl/gateway/bonjour>).


Alleen gateways waarvoor Bonjour-detectie is ingeschakeld (standaard) adverteren het baken.

Wide-area-detectierecords kunnen deze TXT-hints bevatten:

  * `role` (hint voor gatewayrol)
  * `transport` (transporthint, bijv. `gateway`)
  * `gatewayPort` (WebSocket-poort, meestal `18789`)
  * `sshPort` (alleen volledige detectiemodus; clients gebruiken standaard SSH-doelen op `22` wanneer dit ontbreekt)
  * `tailnetDns` (MagicDNS-hostnaam, indien beschikbaar)
  * `gatewayTls` / `gatewayTlsSha256` (TLS ingeschakeld + certificaatvingerafdruk)
  * `cliPath` (alleen volledige detectiemodus)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Machineleesbare uitvoer (schakelt ook styling/spinner uit).

Voorbeelden:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Gateway-runbook](</nl/gateway>)


Was this useful?YesNo
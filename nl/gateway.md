---
title: Gateway-draaiboek
source_url: https://docs.openclaw.ai/nl/gateway
scraped_at: 2026-05-25
---

Gebruik deze pagina voor dag-1-opstart en dag-2-operaties van de Gateway-service.

[**Diepe probleemoplossing** Symptoomgerichte diagnostiek met exacte opdrachtladders en logsignaturen. ](</nl/gateway/troubleshooting>) [**Configuratie** Taakgerichte installatiegids + volledige configuratiereferentie. ](</nl/gateway/configuration>) [**Geheimenbeheer** SecretRef-contract, runtime-snapshotgedrag en migratie-/herlaadoperaties. ](</nl/gateway/secrets>) [**Geheimenplancontract** Exacte doel-/padregels voor `secrets apply` en ref-only auth-profielgedrag. ](</nl/gateway/secrets-plan-contract>)

## Lokale opstart in 5 minuten

* ### Start de Gateway

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### Controleer de servicestatus

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Gezonde basislijn: `Runtime: running`, `Connectivity probe: ok` en `Capability: ...` die overeenkomt met wat je verwacht. Gebruik `openclaw gateway status --require-rpc` wanneer je RPC-bewijs met leesbereik nodig hebt, niet alleen bereikbaarheid.

* ### Valideer kanaalgereedheid

bashCopy code
[code]
    openclaw channels status --probe
[/code]

Met een bereikbare Gateway voert dit live kanaalprobes per account en optionele audits uit. Als de Gateway onbereikbaar is, valt de CLI terug op config-only kanaalsamenvattingen in plaats van live probe-uitvoer.

## Runtime-model

  * Eén altijd actief proces voor routering, control plane en kanaalverbindingen.
  * Eén gemultiplexte poort voor: 
    * WebSocket-control/RPC
    * HTTP-API's, OpenAI-compatibel (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * Control-UI en hooks
  * Standaard bind-modus: `loopback`.
  * Auth is standaard vereist. Setups met gedeeld geheim gebruiken `gateway.auth.token` / `gateway.auth.password` (of `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`), en niet-loopback reverse-proxysetups kunnen `gateway.auth.mode: "trusted-proxy"` gebruiken.


## OpenAI-compatibele endpoints

OpenClaw's compatibiliteitsoppervlak met de hoogste impact is nu:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Waarom deze set belangrijk is:

  * De meeste Open WebUI-, LobeChat- en LibreChat-integraties proberen eerst `/v1/models`.
  * Veel RAG- en geheugenpijplijnen verwachten `/v1/embeddings`.
  * Agent-native clients geven steeds vaker de voorkeur aan `/v1/responses`.


Planningsnotitie:

  * `/v1/models` is agent-first: het retourneert `openclaw`, `openclaw/default` en `openclaw/<agentId>`.
  * `openclaw/default` is de stabiele alias die altijd naar de geconfigureerde standaardagent verwijst.
  * Gebruik `x-openclaw-model` wanneer je een backend provider-/modeloverride wilt; anders blijft de normale model- en embeddingsetup van de geselecteerde agent leidend.


Al deze endpoints draaien op de hoofdpoort van de Gateway en gebruiken dezelfde vertrouwde operator-authgrens als de rest van de Gateway-HTTP-API.

### Poort- en bind-voorrang

Instelling | Resolutievolgorde  
---|---  
Gateway-poort | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Bind-modus | CLI/override → `gateway.bind` → `loopback`  
  
Geïnstalleerde Gateway-services registreren de opgeloste `--port` in supervisormetadata. Voer na het wijzigen van `gateway.port` `openclaw doctor --fix` of `openclaw gateway install --force` uit, zodat launchd/systemd/schtasks het proces op de nieuwe poort start.

Gateway-opstart gebruikt dezelfde effectieve poort en bind wanneer het lokale Control-UI-origins zaait voor niet-loopback binds. Bijvoorbeeld, `--bind lan --port 3000` zaait `http://localhost:3000` en `http://127.0.0.1:3000` voordat runtime- validatie wordt uitgevoerd. Voeg alle remote browser-origins, zoals HTTPS-proxy-URL's, expliciet toe aan `gateway.controlUi.allowedOrigins`.

### Modi voor hot reload

`gateway.reload.mode` | Gedrag  
---|---  
`off` | Geen configuratieherlaad  
`hot` | Alleen hot-safe wijzigingen toepassen  
`restart` | Herstarten bij wijzigingen die herstart vereisen  
`hybrid` (standaard) | Hot toepassen wanneer veilig, anders herstarten  
  
## Operator-opdrachtenset

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` is voor extra servicedetectie (LaunchDaemons/systemd-systeem units/schtasks), niet voor een diepere RPC-healthprobe.

## Meerdere gateways (dezelfde host)

De meeste installaties zouden één Gateway per machine moeten draaien. Eén Gateway kan meerdere agents en kanalen hosten.

Je hebt alleen meerdere gateways nodig wanneer je bewust isolatie of een reddingsbot wilt.

Nuttige controles:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

Wat je kunt verwachten:

  * `gateway status --deep` kan `Other gateway-like services detected (best effort)` melden en opschoontips afdrukken wanneer verouderde launchd/systemd/schtasks-installaties nog aanwezig zijn.
  * `gateway probe` kan waarschuwen voor `multiple reachable gateways` wanneer meer dan één doel antwoordt.
  * Als dat bewust is, isoleer dan poorten, config/state en workspace-roots per Gateway.


Checklist per instantie:

  * Unieke `gateway.port`
  * Unieke `OPENCLAW_CONFIG_PATH`
  * Unieke `OPENCLAW_STATE_DIR`
  * Unieke `agents.defaults.workspace`


Voorbeeld:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Gedetailleerde setup: [/gateway/multiple-gateways](</nl/gateway/multiple-gateways>).

## Toegang op afstand

Voorkeur: Tailscale/VPN. Fallback: SSH-tunnel.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Verbind clients daarna lokaal met `ws://127.0.0.1:18789`.

Zie: [Remote Gateway](</nl/gateway/remote>), [Authenticatie](</nl/gateway/authentication>), [Tailscale](</nl/gateway/tailscale>).

## Supervisie en servicelevenscyclus

Gebruik supervised runs voor production-like betrouwbaarheid.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Gebruik `openclaw gateway restart` voor herstarts. Keten `openclaw gateway stop` en `openclaw gateway start` niet als vervanging voor een herstart.

Op macOS gebruikt `gateway stop` standaard `launchctl bootout` — dit verwijdert de LaunchAgent uit de huidige bootsessie zonder een uitschakeling te persisteren, zodat KeepAlive-autoherstel nog steeds werkt na onverwachte crashes en `gateway start` weer netjes inschakelt. Om auto-respawn persistent te onderdrukken over reboots heen, geef `--disable` mee: `openclaw gateway stop --disable`.

LaunchAgent-labels zijn `ai.openclaw.gateway` (standaard) of `ai.openclaw.<profile>` (benoemd profiel). `openclaw doctor` audit en repareert serviceconfiguratiedrift.

### Linux (systemd user)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Schakel lingering in voor persistentie na uitloggen:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Voorbeeld van een handmatige user-unit wanneer je een aangepast installatiepad nodig hebt:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (native)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

Native Windows managed startup gebruikt een Scheduled Task met de naam `OpenClaw Gateway` (of `OpenClaw Gateway (<profile>)` voor benoemde profielen). Als het maken van een Scheduled Task wordt geweigerd, valt OpenClaw terug op een launcher in de Startup-map per gebruiker die verwijst naar `gateway.cmd` in de state-directory.

### Linux (system service)

Gebruik een system unit voor multi-user/altijd actieve hosts.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Gebruik dezelfde servicebody als de user unit, maar installeer deze onder `/etc/systemd/system/openclaw-gateway[-<profile>].service` en pas `ExecStart=` aan als je `openclaw`-binary ergens anders staat.

Laat `openclaw doctor --fix` niet ook een user-level Gateway-service installeren voor hetzelfde profiel/dezelfde poort. Doctor weigert die automatische installatie wanneer het een system-level OpenClaw Gateway-service vindt; gebruik `OPENCLAW_SERVICE_REPAIR_POLICY=external` wanneer de system unit de levenscyclus beheert.

## Snelle route voor dev-profiel

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

Standaarden omvatten geïsoleerde state/config en basis-Gateway-poort `19001`.

## Snelle protocolreferentie (operatorweergave)

  * Het eerste clientframe moet `connect` zijn.
  * Gateway retourneert `hello-ok`-snapshot (`presence`, `health`, `stateVersion`, `uptimeMs`, limieten/beleid).
  * `hello-ok.features.methods` / `events` zijn een conservatieve ontdekkingslijst, geen gegenereerde dump van elke aanroepbare helperroute.
  * Aanvragen: `req(method, params)` → `res(ok/payload|error)`.
  * Veelvoorkomende events zijn onder andere `connect.challenge`, `agent`, `chat`, `session.message`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, events voor de levenscyclus van pairing/approval en `shutdown`.


Agentruns verlopen in twee fasen:

  1. Onmiddellijke accepted-ack (`status:"accepted"`)
  2. Definitieve voltooiingsrespons (`status:"ok"|"error"`), met gestreamde `agent`-events ertussen.


Zie de volledige protocoldocumentatie: [Gateway-protocol](</nl/gateway/protocol>).

## Operationele controles

### Liveness

  * Open WS en verzend `connect`.
  * Verwacht een `hello-ok`-respons met snapshot.


### Readiness

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Herstel van gaten

Events worden niet opnieuw afgespeeld. Vernieuw bij sequentiegaten de state (`health`, `system-presence`) voordat je doorgaat.

## Veelvoorkomende foutsignaturen

Signatuur | Waarschijnlijk probleem  
---|---  
`refusing to bind gateway ... without auth` | Non-loopback-bind zonder een geldig Gateway-auth-pad  
`another gateway instance is already listening` / `EADDRINUSE` | Poortconflict  
`Gateway start blocked: set gateway.mode=local` | Configuratie ingesteld op externe modus, of lokale-modus-stempel ontbreekt in een beschadigde configuratie  
`unauthorized` during connect | Auth komt niet overeen tussen client en Gateway  
  
Gebruik voor volledige diagnosestappen [Gateway-probleemoplossing](</nl/gateway/troubleshooting>).

## Veiligheidsgaranties

  * Gateway-protocolclients falen snel wanneer Gateway niet beschikbaar is (geen impliciete terugval naar direct-channel).
  * Ongeldige/niet-connect-eerste frames worden geweigerd en gesloten.
  * Graceful shutdown verzendt de gebeurtenis `shutdown` voordat de socket sluit.


* * *

Gerelateerd:

  * [Probleemoplossing](</nl/gateway/troubleshooting>)
  * [Achtergrondproces](</nl/gateway/background-process>)
  * [Configuratie](</nl/gateway/configuration>)
  * [Gezondheid](</nl/gateway/health>)
  * [Doctor](</nl/gateway/doctor>)
  * [Authenticatie](</nl/gateway/authentication>)


## Gerelateerd

  * [Configuratie](</nl/gateway/configuration>)
  * [Gateway-probleemoplossing](</nl/gateway/troubleshooting>)
  * [Externe toegang](</nl/gateway/remote>)
  * [Geheimenbeheer](</nl/gateway/secrets>)


Was this useful?YesNo
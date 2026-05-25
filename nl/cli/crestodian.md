---
title: Crestodian
source_url: https://docs.openclaw.ai/nl/cli/crestodian
scraped_at: 2026-05-25
---

# `openclaw crestodian`

Crestodian is OpenClaw's lokale helper voor installatie, herstel en configuratie. Deze is ontworpen om bereikbaar te blijven wanneer het normale agentpad defect is.

Als je `openclaw` zonder opdracht uitvoert, start Crestodian in een interactieve terminal. Als je `openclaw crestodian` uitvoert, start dezelfde helper expliciet.

## Wat Crestodian toont

Bij het opstarten opent interactieve Crestodian dezelfde TUI-shell die wordt gebruikt door `openclaw tui`, met een Crestodian-chatbackend. Het chatlog begint met een korte begroeting:

  * wanneer je Crestodian moet starten
  * het model of het deterministische plannerpad dat Crestodian daadwerkelijk gebruikt
  * configuratiegeldigheid en de standaardagent
  * Gateway-bereikbaarheid vanaf de eerste opstartprobe
  * de volgende debugactie die Crestodian kan uitvoeren


Het dumpt geen geheimen en laadt geen Plugin-CLI-opdrachten alleen om te starten. De TUI biedt nog steeds de normale koptekst, het chatlog, de statusregel, voettekst, autocomplete en editorbediening.

Gebruik `status` voor de gedetailleerde inventaris met configuratiepad, docs-/bronpaden, lokale CLI-probes, aanwezigheid van API-sleutels, agents, model en Gateway-details.

Crestodian gebruikt dezelfde OpenClaw-referentiedetectie als reguliere agents. In een Git-checkout verwijst het zichzelf naar lokale `docs/` en de lokale broncodeboom. In een npm-pakketinstallatie gebruikt het de meegeleverde pakketdocumentatie en linkt het naar <https://github.com/openclaw/openclaw>, met expliciete richtlijnen om de broncode te bekijken wanneer de documentatie niet genoeg is.

## Voorbeelden

bashCopy code
[code]
    openclawopenclaw crestodianopenclaw crestodian --jsonopenclaw crestodian --message "models"openclaw crestodian --message "validate config"openclaw crestodian --message "setup workspace ~/Projects/work model openai/gpt-5.5" --yesopenclaw crestodian --message "set default model openai/gpt-5.5" --yesopenclaw onboard --modern
[/code]

Binnen de Crestodian-TUI:

textCopy code
[code]
    statushealthdoctordoctor fixvalidate configsetupsetup workspace ~/Projects/work model openai/gpt-5.5config set gateway.port 19001config set-ref gateway.auth.token env OPENCLAW_GATEWAY_TOKENgateway statusrestart gatewayagentscreate agent work workspace ~/Projects/workmodelsset default model openai/gpt-5.5plugins listplugins search slackplugin install clawhub:openclaw-codex-app-serverplugin uninstall openclaw-codex-app-servertalk to work agenttalk to agent for ~/Projects/workauditquit
[/code]

## Veilig opstarten

Het opstartpad van Crestodian is bewust klein gehouden. Het kan draaien wanneer:

  * `openclaw.json` ontbreekt
  * `openclaw.json` ongeldig is
  * de Gateway offline is
  * Plugin-opdrachtregistratie niet beschikbaar is
  * er nog geen agent is geconfigureerd


`openclaw --help` en `openclaw --version` gebruiken nog steeds de normale snelle paden. Niet-interactieve `openclaw` sluit af met een kort bericht in plaats van root-help af te drukken, omdat het product zonder opdracht Crestodian is.

## Bewerkingen en goedkeuring

Crestodian gebruikt getypeerde bewerkingen in plaats van configuratie ad hoc te bewerken.

Alleen-lezen bewerkingen kunnen direct worden uitgevoerd:

  * overzicht tonen
  * agents weergeven
  * geïnstalleerde plugins weergeven
  * ClawHub-plugins zoeken
  * model-/backendstatus tonen
  * status- of healthchecks uitvoeren
  * Gateway-bereikbaarheid controleren
  * doctor uitvoeren zonder interactieve fixes
  * configuratie valideren
  * het auditlogpad tonen


Persistente bewerkingen vereisen conversationele goedkeuring in interactieve modus, tenzij je `--yes` meegeeft voor een directe opdracht:

  * configuratie schrijven
  * `config set` uitvoeren
  * ondersteunde SecretRef-waarden instellen via `config set-ref`
  * setup-/onboarding-bootstrap uitvoeren
  * het standaardmodel wijzigen
  * de Gateway starten, stoppen of herstarten
  * agents maken
  * plugins installeren vanuit ClawHub of npm
  * plugins verwijderen
  * doctor-herstellingen uitvoeren die configuratie of status herschrijven


Toegepaste schrijfacties worden vastgelegd in:

textCopy code
[code]
    ~/.openclaw/audit/crestodian.jsonl
[/code]

Detectie wordt niet geaudit. Alleen toegepaste bewerkingen en schrijfacties worden gelogd.

`openclaw onboard --modern` start Crestodian als de moderne onboarding-preview. Gewone `openclaw onboard` voert nog steeds klassieke onboarding uit.

## Setup-bootstrap

`setup` is de chat-first onboarding-bootstrap. Het schrijft alleen via getypeerde configuratiebewerkingen en vraagt eerst om goedkeuring.

textCopy code
[code]
    setupsetup workspace ~/Projects/worksetup workspace ~/Projects/work model openai/gpt-5.5
[/code]

Wanneer er geen model is geconfigureerd, selecteert setup de eerste bruikbare backend in deze volgorde en vertelt het wat is gekozen:

  * bestaand expliciet model, als dit al is geconfigureerd
  * `OPENAI_API_KEY` -> `openai/gpt-5.5`
  * `ANTHROPIC_API_KEY` -> `anthropic/claude-opus-4-7`
  * Claude Code CLI -> `claude-cli/claude-opus-4-7`
  * Codex CLI -> `codex-cli/gpt-5.5`


Als er geen beschikbaar zijn, schrijft setup nog steeds de standaardworkspace en laat het model unset. Installeer of log in bij Codex/Claude Code, of stel `OPENAI_API_KEY`/`ANTHROPIC_API_KEY` beschikbaar, en voer setup daarna opnieuw uit.

## Modelondersteunde planner

Crestodian start altijd in deterministische modus. Voor vage opdrachten die de deterministische parser niet begrijpt, kan lokale Crestodian één begrensde plannerbeurt uitvoeren via de normale runtimepaden van OpenClaw. Het gebruikt eerst het geconfigureerde OpenClaw-model. Als er nog geen geconfigureerd model bruikbaar is, kan het terugvallen op lokale runtimes die al op de machine aanwezig zijn:

  * Claude Code CLI: `claude-cli/claude-opus-4-7`
  * Codex app-server harness: `openai/gpt-5.5`
  * Codex CLI: `codex-cli/gpt-5.5`


De modelondersteunde planner kan configuratie niet direct muteren. Hij moet het verzoek vertalen naar een van de getypeerde opdrachten van Crestodian, waarna de normale goedkeurings- en auditregels gelden. Crestodian drukt het gebruikte model en de geïnterpreteerde opdracht af voordat het iets uitvoert. Plannerbeurten voor fallback zonder configuratie zijn tijdelijk, tool-uitgeschakeld waar de runtime dit ondersteunt, en gebruiken een tijdelijke workspace/sessie.

Rescuemodus via berichtkanalen gebruikt de modelondersteunde planner niet. Remote rescue blijft deterministisch zodat een defect of gecompromitteerd normaal agentpad niet kan worden gebruikt als configuratie-editor.

## Overschakelen naar een agent

Gebruik een selector in natuurlijke taal om Crestodian te verlaten en de normale TUI te openen:

textCopy code
[code]
    talk to agenttalk to work agentswitch to main agent
[/code]

`openclaw tui`, `openclaw chat` en `openclaw terminal` openen nog steeds direct de normale agent-TUI. Ze starten Crestodian niet.

Nadat je bent overgeschakeld naar de normale TUI, gebruik je `/crestodian` om terug te keren naar Crestodian. Je kunt een vervolgaanvraag opnemen:

textCopy code
[code]
    /crestodian/crestodian restart gateway
[/code]

Agentwisselingen binnen de TUI laten een broodkruimel achter dat `/crestodian` beschikbaar is.

## Rescuemodus via berichten

Rescuemodus via berichten is het entrypoint via berichtkanalen voor Crestodian. Het is bedoeld voor het geval waarin je normale agent dood is, maar een vertrouwd kanaal zoals WhatsApp nog steeds opdrachten ontvangt.

Ondersteunde tekstopdracht:

  * `/crestodian <request>`


Operatorflow:

textCopy code
[code]
    You, in a trusted owner DM: /crestodian statusOpenClaw: Crestodian rescue mode. Gateway reachable: no. Config valid: no.You: /crestodian restart gatewayOpenClaw: Plan: restart the Gateway. Reply /crestodian yes to apply.You: /crestodian yesOpenClaw: Applied. Audit entry written.
[/code]

Het maken van agents kan ook vanuit de lokale prompt of rescuemodus in de wachtrij worden gezet:

textCopy code
[code]
    create agent work workspace ~/Projects/work model openai/gpt-5.5/crestodian create agent work workspace ~/Projects/work
[/code]

Remote rescue is een adminoppervlak. Het moet worden behandeld als remote configuratieherstel, niet als normale chat.

Beveiligingscontract voor remote rescue:

  * Uitgeschakeld wanneer sandboxing actief is. Als een agent/sessie in een sandbox draait, moet Crestodian remote rescue weigeren en uitleggen dat lokaal CLI-herstel vereist is.
  * De standaard effectieve status is `auto`: sta remote rescue alleen toe in vertrouwde YOLO- operatie, waarbij de runtime al lokale bevoegdheid zonder sandbox heeft.
  * Vereist een expliciete owner-identiteit. Rescue mag geen wildcard-afzenderregels, open groepsbeleid, niet-geauthenticeerde webhooks of anonieme kanalen accepteren.
  * Standaard alleen owner-DM's. Rescue in groepen/kanalen vereist expliciete opt-in.
  * Plugin zoeken en weergeven zijn alleen-lezen. Plugin-installatie is standaard alleen lokaal omdat het uitvoerbare code downloadt. Plugin-verwijdering kan worden toegestaan als een goedgekeurde herstelbewerking wanneer het rescuebeleid persistente schrijfacties toestaat.
  * Remote rescue kan de lokale TUI niet openen of overschakelen naar een interactieve agentsessie. Gebruik lokale `openclaw` voor agenthandoff.
  * Persistente schrijfacties vereisen nog steeds goedkeuring, zelfs in rescuemodus.
  * Audit elke toegepaste rescuebewerking. Rescue via berichtkanalen registreert kanaal, account, afzender en metadata van het bronadres. Configuratiemuterende bewerkingen leggen ook configuratiehashes vóór en na vast.
  * Echo nooit geheimen. SecretRef-inspectie moet beschikbaarheid rapporteren, niet waarden.
  * Als de Gateway leeft, geef dan de voorkeur aan getypeerde Gateway-bewerkingen. Als de Gateway dood is, gebruik dan alleen het minimale lokale hersteloppervlak dat niet afhankelijk is van de normale agentloop.


Configuratievorm:

jsoncCopy code
[code]
    {  "crestodian": {    "rescue": {      "enabled": "auto",      "ownerDmOnly": true,    },  },}
[/code]

`enabled` moet accepteren:

  * `"auto"`: standaard. Alleen toestaan wanneer de effectieve runtime YOLO is en sandboxing uit staat.
  * `false`: rescuemodus via berichtkanalen nooit toestaan.
  * `true`: rescue expliciet toestaan wanneer de owner-/kanaalcontroles slagen. Dit mag de sandboxingweigering nog steeds niet omzeilen.


De standaard `"auto"` YOLO-houding is:

  * sandboxmodus wordt opgelost naar `off`
  * `tools.exec.security` wordt opgelost naar `full`
  * `tools.exec.ask` wordt opgelost naar `off`


Remote rescue wordt gedekt door de Docker-lane:

bashCopy code
[code]
    pnpm test:docker:crestodian-rescue
[/code]

Lokale plannerfallback zonder configuratie wordt gedekt door:

bashCopy code
[code]
    pnpm test:docker:crestodian-planner
[/code]

Een opt-in live kanaal-commandosurface-smoke controleert `/crestodian status` plus een persistente goedkeuringsroundtrip via de rescuehandler:

bashCopy code
[code]
    pnpm test:live:crestodian-rescue-channel
[/code]

Verse setup zonder configuratie via Crestodian wordt gedekt door:

bashCopy code
[code]
    pnpm test:docker:crestodian-first-run
[/code]

Die lane begint met een lege statusmap, routeert kale `openclaw` naar Crestodian, stelt het standaardmodel in, maakt een extra agent, configureert Discord via een Plugin-activering plus token-SecretRef, valideert configuratie en controleert het auditlog. QA Lab heeft ook een repo-ondersteund scenario voor dezelfde Ring 0-flow:

bashCopy code
[code]
    pnpm openclaw qa suite --scenario crestodian-ring-zero-setup
[/code]

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Doctor](</nl/cli/doctor>)
  * [TUI](</nl/cli/tui>)
  * [Sandbox](</nl/cli/sandbox>)
  * [Beveiliging](</nl/cli/security>)


Was this useful?YesNo
---
title: Slashcommando's
source_url: https://docs.openclaw.ai/nl/tools/slash-commands
scraped_at: 2026-05-25
---

Commando's worden afgehandeld door de Gateway. De meeste commando's moeten worden verzonden als een **zelfstandig** bericht dat begint met `/`. Het host-only bash-chatcommando gebruikt `! <cmd>` (met `/bash <cmd>` als alias).

Wanneer een gesprek of thread is gekoppeld aan een ACP-sessie, wordt normale vervolgtekst naar die ACP-harness gerouteerd. Gateway-beheercommando's blijven nog steeds lokaal: `/acp ...` bereikt altijd de OpenClaw ACP-commandohandler, en `/status` plus `/unfocus` blijven lokaal wanneer commandoafhandeling is ingeschakeld voor het oppervlak.

Er zijn twee gerelateerde systemen:

Commando's

Zelfstandige `/...`-berichten.

Directieven

`/think`, `/fast`, `/verbose`, `/trace`, `/reasoning`, `/elevated`, `/exec`, `/model`, `/queue`.

  * Directieven worden uit het bericht verwijderd voordat het model ze ziet.
  * In normale chatberichten (niet alleen directieven) worden ze behandeld als "inline hints" en blijven sessie-instellingen **niet** behouden.
  * In berichten met alleen directieven (het bericht bevat alleen directieven) blijven ze behouden voor de sessie en antwoorden ze met een bevestiging.
  * Directieven worden alleen toegepast voor **geautoriseerde afzenders**. Als `commands.allowFrom` is ingesteld, is dit de enige gebruikte allowlist; anders komt autorisatie uit kanaal-allowlists/koppeling plus `commands.useAccessGroups`. Ongeautoriseerde afzenders zien directieven behandeld worden als platte tekst.

Inline snelkoppelingen

Alleen afzenders op de allowlist/geautoriseerde afzenders: `/help`, `/commands`, `/status`, `/whoami` (`/id`).

Ze worden direct uitgevoerd, verwijderd voordat het model het bericht ziet, en de resterende tekst gaat verder via de normale stroom.

## Configuratie

json5Copy code
[code]
    {  commands: {    native: "auto",    nativeSkills: "auto",    text: true,    bash: false,    bashForegroundMs: 2000,    config: false,    mcp: false,    plugins: false,    debug: false,    restart: true,    ownerAllowFrom: ["discord:123456789012345678"],    ownerDisplay: "raw",    ownerDisplaySecret: "${OWNER_ID_HASH_SECRET}",    allowFrom: {      "*": ["user1"],      discord: ["user:123"],    },    useAccessGroups: true,  },}
[/code]

Schakelt het parsen van `/...` in chatberichten in. Op oppervlakken zonder native commando's (WhatsApp/WebChat/Signal/iMessage/Google Chat/Microsoft Teams) blijven tekstcommando's werken, zelfs als je dit instelt op `false`.

Registreert native commando's. Auto: aan voor Discord/Telegram; uit voor Slack (totdat je slash-commando's toevoegt); genegeerd voor providers zonder native ondersteuning. Stel `channels.discord.commands.native`, `channels.telegram.commands.native` of `channels.slack.commands.native` in om per provider te overschrijven (bool of `"auto"`). Op Discord slaat `false` de registratie en opschoning van slash-commando's tijdens het opstarten over; eerder geregistreerde commando's kunnen zichtbaar blijven totdat je ze uit de Discord-app verwijdert. Slack-commando's worden beheerd in de Slack-app en worden niet automatisch verwijderd.

Op Discord kunnen native commandospecificaties `descriptionLocalizations` bevatten, die OpenClaw publiceert als Discord `description_localizations` en opneemt in reconcile-vergelijkingen.

Registreert **skill** -commando's native wanneer dit wordt ondersteund. Auto: aan voor Discord/Telegram; uit voor Slack (Slack vereist het maken van een slash-commando per skill). Stel `channels.discord.commands.nativeSkills`, `channels.telegram.commands.nativeSkills` of `channels.slack.commands.nativeSkills` in om per provider te overschrijven (bool of `"auto"`).

Schakelt `! <cmd>` in om host-shellcommando's uit te voeren (`/bash <cmd>` is een alias; vereist `tools.elevated`-allowlists).

Bepaalt hoe lang bash wacht voordat wordt overgeschakeld naar achtergrondmodus (`0` zet direct op de achtergrond).

Schakelt `/config` in (leest/schrijft `openclaw.json`).

Schakelt `/mcp` in (leest/schrijft door OpenClaw beheerde MCP-configuratie onder `mcp.servers`).

Schakelt `/plugins` in (Plugin-detectie/status plus installatie- en inschakel-/uitschakelbediening).

Schakelt `/debug` in (alleen runtime-overschrijvingen).

Schakelt `/restart` plus Gateway-herstarttoolacties in.

Stelt de expliciete eigenaar-allowlist in voor command-/tooloppervlakken die alleen voor de eigenaar zijn. Dit is het account van de menselijke operator dat gevaarlijke acties kan goedkeuren en commando's zoals `/diagnostics`, `/export-trajectory` en `/config` kan uitvoeren. Dit staat los van `commands.allowFrom` en van DM-koppelingstoegang.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImNoYW5uZWxzLjxjaGFubmVs .commands.enforceOwnerForCommands" type="boolean" default="false"> Per kanaal: zorgt dat commando's die alleen voor de eigenaar zijn **eigenaarsidentiteit** vereisen om op dat oppervlak te worden uitgevoerd. Wanneer `true`, moet de afzender overeenkomen met een opgeloste eigenaarskandidaat (bijvoorbeeld een vermelding in `commands.ownerAllowFrom` of provider-native eigenaarsmetadata), of interne `operator.admin`-scope hebben op een intern berichtkanaal. Een wildcardvermelding in kanaal `allowFrom`, of een lege/onopgeloste lijst met eigenaarskandidaten, is **niet** voldoende — commando's die alleen voor de eigenaar zijn falen gesloten op dat kanaal. Laat dit uit als je wilt dat commando's die alleen voor de eigenaar zijn alleen worden afgeschermd door `ownerAllowFrom` en de standaard commando-allowlists.

Bepaalt hoe eigenaars-id's in de systeemprompt verschijnen.

Stelt optioneel het HMAC-geheim in dat wordt gebruikt wanneer `commands.ownerDisplay="hash"`.

Allowlist per provider voor commandoautorisatie. Wanneer geconfigureerd is dit de enige autorisatiebron voor commando's en directieven (kanaal-allowlists/koppeling en `commands.useAccessGroups` worden genegeerd). Gebruik `"*"` voor een globale standaard; providerspecifieke sleutels overschrijven deze.

Dwingt allowlists/beleid af voor commando's wanneer `commands.allowFrom` niet is ingesteld.

## Commandolijst

Huidige bron van waarheid:

  * core built-ins komen uit `src/auto-reply/commands-registry.shared.ts`
  * gegenereerde dock-commando's komen uit `src/auto-reply/commands-registry.data.ts`
  * Plugin-commando's komen uit Plugin-`registerCommand()`-aanroepen
  * daadwerkelijke beschikbaarheid op je Gateway hangt nog steeds af van configuratievlaggen, kanaaloppervlak en geïnstalleerde/ingeschakelde Plugins


### Ingebouwde core-commando's

Sessies en runs

  * `/new [model]` start een nieuwe sessie; `/reset` is de reset-alias.
  * Control UI onderschept getypte `/new` om een nieuwe dashboardsessie te maken en ernaar over te schakelen, behalve wanneer `session.dmScope: "main"` is geconfigureerd en de huidige bovenliggende sessie de hoofdsessie van de agent is; in dat geval reset `/new` de hoofdsessie op zijn plaats. Getypte `/reset` voert nog steeds de in-place reset van de Gateway uit.
  * `/reset soft [message]` behoudt het huidige transcript, verwijdert hergebruikte CLI-backendsessie-id's en voert het laden van opstart-/systeemprompts opnieuw in-place uit.
  * `/compact [instructions]` comprimeert de sessiecontext. Zie [Compaction](</nl/concepts/compaction>).
  * `/stop` breekt de huidige run af.
  * `/session idle <duration|off>` en `/session max-age <duration|off>` beheren de vervaltijd van thread-koppeling.
  * `/export-session [path]` exporteert de huidige sessie naar HTML. Alias: `/export`.
  * `/export-trajectory [path]` vraagt om exec-goedkeuring en exporteert daarna een JSONL-[trajectbundel](</nl/tools/trajectory>) voor de huidige sessie. Gebruik dit wanneer je de prompt-, tool- en transcripttijdlijn voor één OpenClaw-sessie nodig hebt. In groepschats gaan de goedkeuringsprompt en het exportresultaat privé naar de eigenaar. Alias: `/trajectory`.

Model- en runbesturing

  * `/think <level|default>` stelt het denkniveau in of wist de sessie-overschrijving. Opties komen uit het providerprofiel van het actieve model; gangbare niveaus zijn `off`, `minimal`, `low`, `medium` en `high`, met aangepaste niveaus zoals `xhigh`, `adaptive`, `max` of binaire `on` alleen waar ondersteund. Aliassen: `/thinking`, `/t`.
  * `/verbose on|off|full` schakelt uitgebreide uitvoer om. Alias: `/v`.
  * `/trace on|off` schakelt Plugin-trace-uitvoer om voor de huidige sessie.
  * `/fast [status|on|off|default]` toont, stelt in of wist de snelle modus.
  * `/reasoning [on|off|stream]` schakelt de zichtbaarheid van redenering om. Alias: `/reason`.
  * `/elevated [on|off|ask|full]` schakelt verhoogde modus om. Alias: `/elev`.
  * `/exec host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>` toont of stelt exec-standaarden in.
  * `/model [name|#|status]` toont of stelt het model in.
  * `/models [provider] [page] [limit=<n>|size=<n>|all]` vermeldt geconfigureerde/providers met beschikbare authenticatie of modellen voor een provider; voeg `all` toe om de volledige catalogus van die provider te bekijken. `provider/*`-vermeldingen in `agents.defaults.models` zorgen dat `/model` en `/models` alleen ontdekte modellen voor die providers tonen.
  * `/queue <mode>` beheert wachtrijgedrag (`steer`, legacy `queue`, `followup`, `collect`, `steer-backlog`, `interrupt`) plus opties zoals `debounce:0.5s cap:25 drop:summarize`; `/queue default` of `/queue reset` wist de sessie-overschrijving. Zie [Commandowachtrij](</nl/concepts/queue>) en [Stuurwachtrij](</nl/concepts/queue-steering>).
  * `/steer <message>` injecteert begeleiding in de actieve run voor de huidige sessie, onafhankelijk van de `/queue`-modus. Het start geen nieuwe run wanneer de sessie inactief is. Alias: `/tell`. Zie [Sturen](</nl/tools/steer>).

Ontdekking en status

  * `/help` toont de korte helpsamenvatting.
  * `/commands` toont de gegenereerde commandocatalogus.
  * `/tools [compact|verbose]` toont wat de huidige agent op dit moment kan gebruiken.
  * `/status` toont uitvoerings-/runtimestatus, Gateway- en systeem-uptime, plus providergebruik/quota wanneer beschikbaar.
  * `/diagnostics [note]` is de supportrapportstroom voor alleen de eigenaar voor Gateway-bugs en Codex-harness-runs. Het vraagt elke keer om expliciete exec-goedkeuring voordat `openclaw gateway diagnostics export --json` wordt uitgevoerd; keur diagnostiek niet goed met een allow-all-regel. Na goedkeuring verstuurt het een plakbaar rapport met het lokale bundelpad, manifestsamenvatting, privacynotities en relevante sessie-id's. In groepschats gaan de goedkeuringsprompt en het rapport privé naar de eigenaar. Wanneer de actieve sessie de OpenAI Codex-harness gebruikt, verstuurt dezelfde goedkeuring ook relevante Codex-feedback naar OpenAI-servers en vermeldt het voltooide antwoord de OpenClaw-sessie-id's, Codex-thread-id's en `codex resume <thread-id>`-commando's. Zie [Diagnostiekexport](</nl/gateway/diagnostics>).
  * `/crestodian <request>` voert de installatie- en reparatiehulp van Crestodian uit vanuit een eigenaar-DM.
  * `/tasks` vermeldt actieve/recente achtergrondtaken voor de huidige sessie.
  * `/context [list|detail|map|json]` legt uit hoe context wordt samengesteld. `map` verstuurt een treemap-afbeelding van de context van de huidige sessie.
  * `/whoami` toont je afzender-id. Alias: `/id`.
  * `/usage off|tokens|full|cost` beheert de gebruiksvoetnoot per antwoord of drukt een lokale kostensamenvatting af.

Skills, allowlists, goedkeuringen

  * `/skill <name> [input]` voert een skill uit op naam.
  * `/allowlist [list|add|remove] ...` beheert allowlist-vermeldingen. Alleen tekst.
  * `/approve <id> <decision>` handelt uitvoeringsgoedkeuringsprompts af.
  * `/btw <question>` stelt een zijvraag zonder de toekomstige sessiecontext te wijzigen. Alias: `/side`. Zie [BTW](</nl/tools/btw>).

Subagenten en ACP

  * `/subagents list|kill|log|info|send|steer|spawn` beheert subagentuitvoeringen voor de huidige sessie.
  * `/acp spawn|cancel|steer|close|sessions|status|set-mode|set|cwd|permissions|timeout|model|reset-options|doctor|install|help` beheert ACP-sessies en runtime-opties.
  * `/focus <target>` koppelt de huidige Discord-thread of Telegram-topic/conversatie aan een sessiedoel.
  * `/unfocus` verwijdert de huidige koppeling.
  * `/agents` toont agents die aan een thread zijn gekoppeld voor de huidige sessie.
  * `/kill <id|#|all>` breekt een of alle actieve subagenten af.
  * `/subagents steer <id|#> <message>` stuurt bijsturing naar een actieve subagent. Zie [Bijsturen](</nl/tools/steer>).

Alleen-eigenaar schrijfacties en beheer

  * `/config show|get|set|unset` leest of schrijft `openclaw.json`. Alleen eigenaar. Vereist `commands.config: true`.
  * `/mcp show|get|set|unset` leest of schrijft door OpenClaw beheerde MCP-serverconfiguratie onder `mcp.servers`. Alleen eigenaar. Vereist `commands.mcp: true`.
  * `/plugins list|inspect|show|get|install|enable|disable` inspecteert of wijzigt de Plugin-status. `/plugin` is een alias. Alleen eigenaar voor schrijfacties. Vereist `commands.plugins: true`.
  * `/debug show|set|unset|reset` beheert runtime-only configuratie-overschrijvingen. Alleen eigenaar. Vereist `commands.debug: true`.
  * `/restart` herstart OpenClaw wanneer ingeschakeld. Standaard: ingeschakeld; stel `commands.restart: false` in om dit uit te schakelen.
  * `/send on|off|inherit` stelt het verzendbeleid in. Alleen eigenaar.

Spraak, TTS, kanaalbeheer

  * `/tts on|off|status|chat|latest|provider|limit|summary|audio|help` beheert TTS. Zie [TTS](</nl/tools/tts>).
  * `/activation mention|always` stelt de activeringsmodus voor groepen in.
  * `/bash <command>` voert een shellopdracht op de host uit. Alleen tekst. Alias: `! <command>`. Vereist `commands.bash: true` plus `tools.elevated`-allowlists.
  * `!poll [sessionId]` controleert een achtergrond-bash-taak.
  * `!stop [sessionId]` stopt een achtergrond-bash-taak.


### Gegenereerde dock-opdrachten

Dock-opdrachten schakelen de antwoordroute van de huidige sessie over naar een ander gekoppeld kanaal. Zie [Kanaal-docking](</nl/concepts/channel-docking>) voor installatie, voorbeelden en probleemoplossing.

Dock-opdrachten worden gegenereerd uit kanaalplugins met native-command-ondersteuning. Huidige gebundelde set:

  * `/dock-discord` (alias: `/dock_discord`)
  * `/dock-mattermost` (alias: `/dock_mattermost`)
  * `/dock-slack` (alias: `/dock_slack`)
  * `/dock-telegram` (alias: `/dock_telegram`)


Gebruik dock-opdrachten vanuit een directe chat om de antwoordroute van de huidige sessie over te schakelen naar een ander gekoppeld kanaal. De agent behoudt dezelfde sessiecontext, maar toekomstige antwoorden voor die sessie worden geleverd aan de geselecteerde kanaal-peer.

Dock-opdrachten vereisen `session.identityLinks`. De bronafzender en doel-peer moeten in dezelfde identiteitsgroep zitten, bijvoorbeeld `["telegram:123", "discord:456"]`. Als een Telegram-gebruiker met id `123` `/dock_discord` verzendt, slaat OpenClaw `lastChannel: "discord"` en `lastTo: "456"` op in de actieve sessie. Als de afzender niet is gekoppeld aan een Discord-peer, antwoordt de opdracht met een installatietip in plaats van door te vallen naar normale chat.

Docking wijzigt alleen de actieve sessieroute. Het maakt geen kanaalaccounts aan, verleent geen toegang, omzeilt geen kanaal-allowlists en verplaatst geen transcriptgeschiedenis naar een andere sessie. Gebruik `/dock-telegram`, `/dock-slack`, `/dock-mattermost` of een andere gegenereerde dock-opdracht om de route opnieuw te schakelen.

### Gebundelde Plugin-opdrachten

Gebundelde plugins kunnen meer slash-opdrachten toevoegen. Huidige gebundelde opdrachten in deze repo:

  * `/dreaming [on|off|status|help]` schakelt geheugen-Dreaming in of uit. Zie [Dreaming](</nl/concepts/dreaming>).
  * `/pair [qr|status|pending|approve|cleanup|notify]` beheert de apparaatkoppeling-/installatiestroom. Zie [Koppelen](</nl/channels/pairing>).
  * `/phone status|arm <camera|screen|writes|all> [duration]|disarm` wapent tijdelijk risicovolle telefoonnodemands.
  * `/voice status|list [limit]|set <voiceId|name>` beheert Talk-spraakconfiguratie. Op Discord is de native opdrachtnaam `/talkvoice`.
  * `/card ...` verzendt LINE rich-card-presets. Zie [LINE](</nl/channels/line>).
  * `/codex status|models|threads|resume|compact|review|diagnostics|account|mcp|skills` inspecteert en beheert de gebundelde Codex app-server-harness. Zie [Codex-harness](</nl/plugins/codex-harness>).
  * Alleen QQBot-opdrachten: 
    * `/bot-ping`
    * `/bot-version`
    * `/bot-help`
    * `/bot-upgrade`
    * `/bot-logs`


### Dynamische skill-opdrachten

Door gebruikers aanroepbare skills worden ook als slash-opdrachten aangeboden:

  * `/skill <name> [input]` werkt altijd als generiek toegangspunt.
  * skills kunnen ook verschijnen als directe opdrachten zoals `/prose` wanneer de skill/Plugin deze registreert.
  * registratie van native skill-opdrachten wordt beheerd door `commands.nativeSkills` en `channels.<provider>.commands.nativeSkills`.
  * opdrachtspecificaties kunnen `descriptionLocalizations` leveren voor native oppervlakken die gelokaliseerde beschrijvingen ondersteunen, waaronder Discord.


Argument- en parseropmerkingen

  * Opdrachten accepteren optioneel een `:` tussen de opdracht en argumenten (bijv. `/think: high`, `/send: on`, `/help:`).
  * `/new <model>` accepteert een modelalias, `provider/model` of een providernaam (fuzzy match); als er geen match is, wordt de tekst behandeld als de berichtinhoud.
  * Gebruik `openclaw status --usage` voor een volledige uitsplitsing van providergebruik.
  * `/allowlist add|remove` vereist `commands.config=true` en respecteert kanaal-`configWrites`.
  * In multi-accountkanalen respecteren configuratiegerichte `/allowlist --account <id>` en `/config set channels.<provider>.accounts.<id>...` ook de `configWrites` van het doelaccount.
  * `/usage` beheert de gebruiksfooter per antwoord; `/usage cost` print een lokale kostensamenvatting uit OpenClaw-sessielogs.
  * `/restart` is standaard ingeschakeld; stel `commands.restart: false` in om dit uit te schakelen.
  * `/plugins install <spec>` accepteert dezelfde Plugin-specificaties als `openclaw plugins install`: lokaal pad/archief, npm-pakket, `git:<repo>` of `clawhub:<pkg>`, en vraagt daarna om een Gateway-herstart omdat Plugin-bronmodules zijn gewijzigd.
  * `/plugins enable|disable` werkt de Plugin-configuratie bij en activeert Gateway-Plugin-herladen voor nieuwe agentbeurten.

Kanaalspecifiek gedrag

  * Alleen-Discord native opdracht: `/vc join|leave|status` beheert spraakkanalen (niet beschikbaar als tekst). `join` vereist een guild en geselecteerd spraak-/podiumkanaal. Vereist `channels.discord.voice` en native opdrachten.
  * Discord-threadkoppelingsopdrachten (`/focus`, `/unfocus`, `/agents`, `/session idle`, `/session max-age`) vereisen dat effectieve threadkoppelingen zijn ingeschakeld (`session.threadBindings.enabled` en/of `channels.discord.threadBindings.enabled`).
  * ACP-opdrachtreferentie en runtime-gedrag: [ACP-agents](</nl/tools/acp-agents>).

Verbose / trace / fast / reasoning-veiligheid

  * `/verbose` is bedoeld voor debugging en extra zichtbaarheid; houd dit bij normaal gebruik **uit**.
  * `/trace` is nauwer dan `/verbose`: het toont alleen trace-/debugregels die eigendom zijn van plugins en houdt normale verbose tool-ruis uit.
  * `/fast on|off` bewaart een sessie-overschrijving. Gebruik de optie `inherit` in de Sessions UI om deze te wissen en terug te vallen op configuratiestandaarden.
  * `/fast` is providerspecifiek: OpenAI/OpenAI Codex koppelen dit aan `service_tier=priority` op native Responses-eindpunten, terwijl directe publieke Anthropic-verzoeken, inclusief via OAuth geauthenticeerd verkeer dat naar `api.anthropic.com` wordt gestuurd, dit koppelen aan `service_tier=auto` of `standard_only`. Zie [OpenAI](</nl/providers/openai>) en [Anthropic](</nl/providers/anthropic>).
  * Samenvattingen van toolfouten worden nog steeds getoond wanneer relevant, maar gedetailleerde fouttekst wordt alleen opgenomen wanneer `/verbose` `on` of `full` is.
  * `/reasoning`, `/verbose` en `/trace` zijn risicovol in groepsomgevingen: ze kunnen interne redenering, tooluitvoer of Plugin-diagnostiek onthullen die u niet wilde blootstellen. Laat ze bij voorkeur uit, vooral in groepschats.

Model wisselen

  * `/model` bewaart het nieuwe sessiemodel onmiddellijk.
  * Als de agent inactief is, gebruikt de volgende uitvoering dit meteen.
  * Als er al een uitvoering actief is, markeert OpenClaw een live-wissel als in behandeling en herstart het pas in het nieuwe model op een schoon retry-punt.
  * Als toolactiviteit of antwoorduitvoer al is gestart, kan de wachtende wissel in de wachtrij blijven tot een latere retry-mogelijkheid of de volgende gebruikersbeurt.
  * In de lokale TUI keert `/crestodian [request]` terug van de normale agent-TUI naar Crestodian. Dit staat los van rescue-modus voor berichtkanalen en verleent geen externe configuratiebevoegdheid.

Snel pad en inline snelkoppelingen

  * **Snel pad:** berichten met alleen opdrachten van afzenders op de allowlist worden onmiddellijk afgehandeld (omzeilt wachtrij + model).
  * **Groepsvermeldingspoort:** berichten met alleen opdrachten van afzenders op de allowlist omzeilen vermeldingsvereisten.
  * **Inline snelkoppelingen (alleen afzenders op de allowlist):** bepaalde opdrachten werken ook wanneer ze zijn ingebed in een normaal bericht en worden verwijderd voordat het model de resterende tekst ziet. 
    * Voorbeeld: `hey /status` activeert een statusantwoord, en de resterende tekst gaat door de normale stroom.
  * Momenteel: `/help`, `/commands`, `/status`, `/whoami` (`/id`).
  * Niet-geautoriseerde berichten met alleen opdrachten worden stil genegeerd, en inline `/...`-tokens worden behandeld als gewone tekst.

Skill-opdrachten en native argumenten

  * **Skill-opdrachten:** `user-invocable` skills worden als slash-opdrachten aangeboden. Namen worden opgeschoond naar `a-z0-9_` (max. 32 tekens); botsingen krijgen numerieke achtervoegsels (bijv. `_2`). 
    * `/skill <name> [input]` voert een skill uit op naam (nuttig wanneer native opdrachtlimieten afzonderlijke opdrachten per skill verhinderen).
    * Standaard worden skill-opdrachten als een normaal verzoek doorgestuurd naar het model.
    * Skills kunnen optioneel `command-dispatch: tool` declareren om de opdracht direct naar een tool te routeren (deterministisch, geen model).
    * Voorbeeld: `/prose` (OpenProse-Plugin) — zie [OpenProse](</nl/prose>).
  * **Native opdrachtargumenten:** Discord gebruikt autocomplete voor dynamische opties (en knopmenu's wanneer u vereiste argumenten weglaat). Telegram en Slack tonen een knopmenu wanneer een opdracht keuzes ondersteunt en u het argument weglaat. Dynamische keuzes worden opgelost tegen het doel-sessiemodel, zodat modelspecifieke opties zoals `/think`-niveaus de `/model`-overschrijving van die sessie volgen.


## `/tools`

`/tools` beantwoordt een runtime-vraag, geen configuratievraag: **wat deze agent op dit moment in dit gesprek kan gebruiken**.

  * Standaard `/tools` is compact en geoptimaliseerd voor snel scannen.
  * `/tools verbose` voegt korte beschrijvingen toe.
  * Native-command-oppervlakken die argumenten ondersteunen, bieden dezelfde modusschakelaar als `compact|verbose`.
  * Resultaten zijn sessiegebonden, dus het wijzigen van agent, kanaal, thread, afzenderautorisatie of model kan de uitvoer wijzigen.
  * `/tools` bevat tools die daadwerkelijk bereikbaar zijn tijdens runtime, inclusief kerntools, verbonden Plugin-tools en tools die eigendom zijn van kanalen.


Gebruik voor profiel- en overschrijvingsbewerking het Tools-paneel in de Control UI of configuratie-/catalogusoppervlakken in plaats van `/tools` als statische catalogus te behandelen.

## Gebruiksoppervlakken (wat waar wordt getoond)

  * **Providergebruik/quota** (voorbeeld: "Claude 80% over") wordt weergegeven in `/status` voor de huidige modelprovider wanneer gebruikstracking is ingeschakeld. OpenClaw normaliseert providervensters naar `% over`; voor MiniMax worden percentagevelden met alleen resterend gebruik omgekeerd vóór weergave, en `model_remains`-antwoorden geven de voorkeur aan de chatmodelvermelding plus een planningslabel met modeltag.
  * **Token-/cache-regels** in `/status` kunnen terugvallen op de nieuwste gebruiksvermelding in het transcript wanneer de live sessie-snapshot beperkt is. Bestaande niet-nul live waarden blijven voorrang houden, en transcriptfallback kan ook het actieve runtimemodellabel herstellen plus een groter promptgericht totaal wanneer opgeslagen totalen ontbreken of kleiner zijn.
  * **Uitvoering vs runtime:** `/status` rapporteert `Execution` voor het effectieve sandboxpad en `Runtime` voor wie de sessie daadwerkelijk uitvoert: `OpenClaw Pi Default`, `OpenAI Codex`, een CLI-backend of een ACP-backend.
  * **Tokens/kosten per antwoord** wordt beheerd met `/usage off|tokens|full` (toegevoegd aan normale antwoorden).
  * `/model status` gaat over **modellen/authenticatie/eindpunten** , niet over gebruik.


## Modelselectie (`/model`)

`/model` is geïmplementeerd als een richtlijn.

Voorbeelden:

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model opus@anthropic:default/model status
[/code]

Opmerkingen:

  * `/model` en `/model list` tonen een compacte, genummerde kiezer (modelfamilie + beschikbare providers).
  * Op Discord openen `/model` en `/models` een interactieve kiezer met provider- en modelkeuzelijsten plus een verzendstap. De kiezer respecteert `agents.defaults.models`, inclusief `provider/*`-vermeldingen, zodat providergebonden ontdekking de kiezer onder Discords componentlimiet van 25 opties kan houden.
  * `/model <#>` selecteert uit die kiezer (en geeft waar mogelijk de voorkeur aan de huidige provider).
  * `/model status` toont de gedetailleerde weergave, inclusief geconfigureerd providereindpunt (`baseUrl`) en API-modus (`api`) wanneer beschikbaar.


## Debug-overschrijvingen

Met `/debug` kun je **alleen-runtime** configuratieoverschrijvingen instellen (geheugen, niet schijf). Alleen eigenaar. Standaard uitgeschakeld; schakel in met `commands.debug: true`.

Voorbeelden:

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug set channels.whatsapp.allowFrom=["+1555","+4477"]/debug unset messages.responsePrefix/debug reset
[/code]

## Plugin-trace-uitvoer

Met `/trace` kun je **sessiegebonden Plugin-trace-/debugregels** in- en uitschakelen zonder de volledige uitgebreide modus aan te zetten.

Voorbeelden:

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Opmerkingen:

  * `/trace` zonder argument toont de huidige trace-status van de sessie.
  * `/trace on` schakelt Plugin-traceregels in voor de huidige sessie.
  * `/trace off` schakelt ze weer uit.
  * Plugin-traceregels kunnen verschijnen in `/status` en als diagnostisch vervolgbericht na het normale assistentantwoord.
  * `/trace` vervangt `/debug` niet; `/debug` beheert nog steeds alleen-runtime configuratieoverschrijvingen.
  * `/trace` vervangt `/verbose` niet; normale uitgebreide tool-/statusuitvoer hoort nog steeds bij `/verbose`.


## Configuratie-updates

`/config` schrijft naar je configuratie op schijf (`openclaw.json`). Alleen eigenaar. Standaard uitgeschakeld; schakel in met `commands.config: true`.

Voorbeelden:

CodeCopy code
[code]
    /config show/config show messages.responsePrefix/config get messages.responsePrefix/config set messages.responsePrefix="[openclaw]"/config unset messages.responsePrefix
[/code]

## MCP-updates

`/mcp` schrijft door OpenClaw beheerde MCP-serverdefinities onder `mcp.servers`. Alleen eigenaar. Standaard uitgeschakeld; schakel in met `commands.mcp: true`.

Voorbeelden:

textCopy code
[code]
    /mcp show/mcp show context7/mcp set context7={"command":"uvx","args":["context7-mcp"]}/mcp unset context7
[/code]

## Plugin-updates

Met `/plugins` kunnen operators ontdekte plugins inspecteren en inschakeling in configuratie aan- of uitzetten. Alleen-lezen-stromen kunnen `/plugin` als alias gebruiken. Standaard uitgeschakeld; schakel in met `commands.plugins: true`.

Voorbeelden:

textCopy code
[code]
    /plugins/plugins list/plugin show context7/plugins enable context7/plugins disable context7
[/code]

## Surface-opmerkingen

Sessies per surface

  * **Tekstopdrachten** worden uitgevoerd in de normale chatsessie (DM's delen `main`, groepen hebben hun eigen sessie).
  * **Native opdrachten** gebruiken geïsoleerde sessies: 
    * Discord: `agent:<agentId>:discord:slash:<userId>`
    * Slack: `agent:<agentId>:slack:slash:<userId>` (voorvoegsel configureerbaar via `channels.slack.slashCommand.sessionPrefix`)
    * Telegram: `telegram:slash:<userId>` (richt zich op de chatsessie via `CommandTargetSessionKey`)
  * **`/stop`** richt zich op de actieve chatsessie zodat die de huidige run kan afbreken.

Slack-specifiek

`channels.slack.slashCommand` wordt nog steeds ondersteund voor één opdracht in `/openclaw`-stijl. Als je `commands.native` inschakelt, moet je één Slack-slashopdracht maken per ingebouwde opdracht (dezelfde namen als `/help`). Menu's met opdrachtargumenten voor Slack worden geleverd als tijdelijke Block Kit-knoppen.

Native Slack-uitzondering: registreer `/agentstatus` (niet `/status`) omdat Slack `/status` reserveert. Tekstuele `/status` werkt nog steeds in Slack-berichten.

## BTW-zijvragen

`/btw` is een snelle **zijvraag** over de huidige sessie. `/side` is een alias.

Anders dan normale chat:

  * gebruikt het de huidige sessie als achtergrondcontext,
  * wordt het in Codex-harnesssessies uitgevoerd als een tijdelijke Codex-zijdraad met de huidige Codex-machtigingen en native tool-surface,
  * behoudt het in niet-Codex-sessies het oudere directe eenmalige zijaanroepgedrag,
  * verandert het toekomstige sessiecontext niet,
  * wordt het niet naar transcriptgeschiedenis geschreven,
  * wordt het geleverd als live zijresultaat in plaats van als normaal assistentbericht.


Dat maakt `/btw` handig wanneer je een tijdelijke verduidelijking wilt terwijl de hoofdtaak doorgaat.

Voorbeeld:

textCopy code
[code]
    /btw what are we doing right now?/side what changed while the main run continued?
[/code]

Zie [BTW-zijvragen](</nl/tools/btw>) voor het volledige gedrag en de UX-details voor clients.

## Gerelateerd

  * [Skills maken](</nl/tools/creating-skills>)
  * [Skills](</nl/tools/skills>)
  * [Skills-configuratie](</nl/tools/skills-config>)


Was this useful?YesNo
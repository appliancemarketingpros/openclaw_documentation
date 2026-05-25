---
title: Plugins
source_url: https://docs.openclaw.ai/nl/cli/plugins
scraped_at: 2026-05-25
---

Beheer Gateway-plugins, hook-packs en compatibele bundels.

[**Pluginsysteem** Eindgebruikershandleiding voor het installeren, inschakelen en oplossen van problemen met plugins. ](</nl/tools/plugin>) [**Plugins beheren** Snelle voorbeelden voor installeren, weergeven, bijwerken, verwijderen en publiceren. ](</nl/plugins/manage-plugins>) [**Plugin-bundels** Compatibiliteitsmodel voor bundels. ](</nl/plugins/bundles>) [**Plugin-manifest** Manifestvelden en configuratieschema. ](</nl/plugins/manifest>) [**Beveiliging** Beveiligingsverharding voor plugin-installaties. ](</nl/gateway/security>)

## Opdrachten

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

Voor onderzoek naar trage installatie, inspectie, verwijdering of registry-verversing voer je de opdracht uit met `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`. De trace schrijft fasetimings naar stderr en houdt JSON-uitvoer parseerbaar. Zie [Debugging](</nl/help/debugging#plugin-lifecycle-trace>).

### Installeren

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

Maintainers die installaties tijdens setup testen, kunnen automatische plugin-installatiebronnen overschrijven met bewaakte omgevingsvariabelen. Zie [Overschrijvingen voor plugin-installatie](</nl/plugins/install-overrides>).

`plugins search` zoekt in ClawHub naar installeerbare plugin-pakketten en drukt installatieklare pakketnamen af. Het zoekt in code-plugin- en bundle-plugin-pakketten, niet in Skills. Gebruik `openclaw skills search` voor ClawHub-Skills.

Config-includes en reparatie van ongeldige configuratie

Als je `plugins`-sectie wordt ondersteund door een `$include` met één bestand, schrijven `plugins install/update/enable/disable/uninstall` door naar dat opgenomen bestand en laten ze `openclaw.json` ongemoeid. Root-includes, include-arrays en includes met sibling-overschrijvingen falen gesloten in plaats van te worden afgevlakt. Zie [Config-includes](</nl/gateway/configuration>) voor de ondersteunde vormen.

Als de configuratie tijdens installatie ongeldig is, faalt `plugins install` normaal gesproken gesloten en wordt je gevraagd eerst `openclaw doctor --fix` uit te voeren. Tijdens het starten en hot reloaden van de Gateway faalt ongeldige plugin-configuratie gesloten zoals elke andere ongeldige configuratie; `openclaw doctor --fix` kan de ongeldige plugin-vermelding in quarantaine plaatsen. De enige gedocumenteerde uitzondering tijdens installatie is een smal herstelpad voor gebundelde plugins voor plugins die expliciet kiezen voor `openclaw.install.allowInvalidConfigRecovery`.

\--force en opnieuw installeren versus bijwerken

`--force` hergebruikt het bestaande installatiedoel en overschrijft een reeds geïnstalleerde plugin of hook-pack ter plekke. Gebruik dit wanneer je bewust dezelfde id opnieuw installeert vanaf een nieuw lokaal pad, archief, ClawHub-pakket of npm-artefact. Voor routinematige upgrades van een al gevolgde npm-plugin geef je de voorkeur aan `openclaw plugins update <id-or-npm-spec>`.

Als je `plugins install` uitvoert voor een plugin-id die al is geïnstalleerd, stopt OpenClaw en verwijst het je naar `plugins update <id-or-npm-spec>` voor een normale upgrade, of naar `plugins install <package> --force` wanneer je de huidige installatie echt vanuit een andere bron wilt overschrijven.

Bereik van --pin

`--pin` is alleen van toepassing op npm-installaties. Het wordt niet ondersteund met `git:`-installaties; gebruik een expliciete git-ref zoals `git:github.com/acme/plugin@v1.2.3` wanneer je een vastgepinde bron wilt. Het wordt niet ondersteund met `--marketplace`, omdat marketplace-installaties marketplace-bronmetadata bewaren in plaats van een npm-spec.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` is een noodoptie voor fout-positieven in de ingebouwde scanner voor gevaarlijke code. Hiermee kan de installatie doorgaan zelfs wanneer de ingebouwde scanner `critical`-bevindingen rapporteert, maar dit omzeilt **niet** de beleidsblokkeringen van plugin-`before_install`-hooks en omzeilt **niet** scanfouten.

Deze CLI-vlag is van toepassing op plugin-installatie-/updateflows. Gateway-ondersteunde installaties van Skills-afhankelijkheden gebruiken de overeenkomende aanvraagoverride `dangerouslyForceUnsafeInstall`, terwijl `openclaw skills install` een aparte download-/installatieflow voor ClawHub-Skills blijft.

Als een plugin die je op ClawHub hebt gepubliceerd wordt geblokkeerd door een registryscan, gebruik dan de publicatiestappen in [ClawHub](</nl/clawhub/security>).

Hook-packs en npm-specs

`plugins install` is ook het installatieoppervlak voor hook-packs die `openclaw.hooks` in `package.json` blootstellen. Gebruik `openclaw hooks` voor gefilterde hook-zichtbaarheid en inschakeling per hook, niet voor pakketinstallatie.

Npm-specs zijn **alleen registry** (pakketnaam + optioneel **exacte versie** of **dist-tag**). Git-/URL-/bestandsspecs en semver-bereiken worden geweigerd. Afhankelijkheidsinstallaties worden projectlokaal uitgevoerd met `--ignore-scripts` voor veiligheid, zelfs wanneer je shell globale npm-installatie-instellingen heeft. Beheerde npm-roots voor plugins erven de npm-`overrides` op pakketniveau van OpenClaw, zodat beveiligingspins van de host ook van toepassing zijn op gehesen plugin-afhankelijkheden.

Gebruik `npm:<package>` wanneer je npm-resolutie expliciet wilt maken. Kale pakketspecs installeren tijdens de lanceringsomschakeling ook rechtstreeks vanaf npm.

Kale specs en `@latest` blijven op het stabiele spoor. Datumgestempelde correctieversies van OpenClaw zoals `2026.5.3-1` zijn stabiele releases voor deze controle. Als npm een van deze naar een prerelease resolveert, stopt OpenClaw en vraagt het je expliciet in te stemmen met een prerelease-tag zoals `@beta`/`@rc` of een exacte prereleaseversie zoals `@1.2.3-beta.4`.

Als een kale installatiespec overeenkomt met een officiële plugin-id (bijvoorbeeld `diffs`), installeert OpenClaw de catalogusvermelding rechtstreeks. Gebruik een expliciete scoped spec (bijvoorbeeld `@scope/diffs`) om een npm-pakket met dezelfde naam te installeren.

Git-repositories

Gebruik `git:<repo>` om rechtstreeks vanuit een git-repository te installeren. Ondersteunde vormen zijn onder meer `git:github.com/owner/repo`, `git:owner/repo`, volledige `https://`-, `ssh://`-, `git://`-, `file://`\- en `git@host:owner/repo.git`-clone-URL's. Voeg `@<ref>` of `#<ref>` toe om vóór installatie een branch, tag of commit uit te checken.

Git-installaties clonen naar een tijdelijke directory, checken de gevraagde ref uit wanneer die aanwezig is, en gebruiken daarna de normale installer voor plugin-directory's. Dat betekent dat manifestvalidatie, scanning op gevaarlijke code, installatiewerk van de package manager en installatierecords zich gedragen als npm-installaties. Vastgelegde git-installaties bevatten de bron-URL/ref plus de opgeloste commit, zodat `openclaw plugins update` de bron later opnieuw kan resolven.

Gebruik na installatie vanuit git `openclaw plugins inspect <id> --runtime --json` om runtimeregistraties zoals gateway-methoden en CLI-opdrachten te verifiëren. Als de plugin een CLI-root heeft geregistreerd met `api.registerCli`, voer die opdracht dan rechtstreeks uit via de OpenClaw-root-CLI, bijvoorbeeld `openclaw demo-plugin ping`.

Archieven

Ondersteunde archieven: `.zip`, `.tgz`, `.tar.gz`, `.tar`. Native OpenClaw-pluginarchieven moeten een geldige `openclaw.plugin.json` bevatten in de uitgepakte plugin-root; archieven die alleen `package.json` bevatten, worden geweigerd voordat OpenClaw installatierecords schrijft.

Gebruik `npm-pack:<path.tgz>` wanneer het bestand een npm-pack-tarball is en je hetzelfde beheerde npm-root-installatiepad wilt testen dat door registry-installaties wordt gebruikt, inclusief `package-lock.json`-verificatie, scanning van gehesen afhankelijkheden en npm-installatierecords. Gewone archiefpaden installeren nog steeds als lokale archieven onder de plugin-extensiesroot.

Claude marketplace-installaties worden ook ondersteund.

ClawHub-installaties gebruiken een expliciete `clawhub:<package>`-locator:

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

Kale npm-veilige plugin-specs installeren tijdens de lanceringsomschakeling standaard vanaf npm:

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

Gebruik `npm:` om npm-only-resolutie expliciet te maken:

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw controleert de geadverteerde Plugin API / minimale Gateway-compatibiliteit vóór installatie. Wanneer de geselecteerde ClawHub-versie een ClawPack-artefact publiceert, downloadt OpenClaw de versiegebonden npm-pack `.tgz`, verifieert het de ClawHub-digestheader en de artefact-digest, en installeert het dit vervolgens via het normale archiefpad. Oudere ClawHub-versies zonder ClawPack-metadata installeren nog steeds via het legacy-verificatiepad voor pakketarchieven. Vastgelegde installaties bewaren hun ClawHub-bronmetadata, artefactsoort, npm-integriteit, npm-shasum, tarballnaam en ClawPack-digestgegevens voor latere updates. Niet-geversioneerde ClawHub-installaties bewaren een niet-geversioneerde vastgelegde spec zodat `openclaw plugins update` nieuwere ClawHub-releases kan volgen; expliciete versie- of tagselectoren zoals `clawhub:pkg@1.2.3` en `clawhub:pkg@beta` blijven aan die selector vastgepind.

#### Marketplace-shorthand

Gebruik `plugin@marketplace`-shorthand wanneer de marketplace-naam bestaat in Claude's lokale registry-cache op `~/.claude/plugins/known_marketplaces.json`:

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

Gebruik `--marketplace` wanneer je de marketplace-bron expliciet wilt doorgeven:

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### Marketplace-bronnen

  * een Claude bekende-marketplace-naam uit `~/.claude/plugins/known_marketplaces.json`
  * een lokale marketplace-root of `marketplace.json`-pad
  * een GitHub-repo-shorthand zoals `owner/repo`
  * een GitHub-repo-URL zoals `https://github.com/owner/repo`
  * een git-URL


### Regels voor externe marketplace

Voor externe marketplaces die vanaf GitHub of git worden geladen, moeten Plugin-vermeldingen binnen de gekloonde marketplace-repo blijven. OpenClaw accepteert relatieve padbronnen uit die repo en weigert HTTP(S), absolute paden, git, GitHub en andere niet-pad-Plugin-bronnen uit externe manifests.

Voor lokale paden en archieven detecteert OpenClaw automatisch:

  * native OpenClaw-Plugins (`openclaw.plugin.json`)
  * Codex-compatibele bundels (`.codex-plugin/plugin.json`)
  * Claude-compatibele bundels (`.claude-plugin/plugin.json` of de standaard Claude-componentindeling)
  * Cursor-compatibele bundels (`.cursor-plugin/plugin.json`)


### Lijst

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

Toon alleen ingeschakelde Plugins.

Schakel over van de tabelweergave naar detailregels per Plugin met metadata over bron/herkomst/versie/activering.

Machineleesbare inventaris plus registry-diagnostics en installatiestatus van pakketafhankelijkheden.

`plugins search` is een externe ClawHub-cataloguslookup. Het inspecteert geen lokale staat, wijzigt geen configuratie, installeert geen pakketten en laadt geen Plugin-runtimecode. Zoekresultaten bevatten de ClawHub-pakketnaam, familie, kanaal, versie, samenvatting en een installatiehint zoals `openclaw plugins install clawhub:<package>`.

Voor gebundeld Plugin-werk binnen een verpakte Docker-image bind-mount je de Plugin- bronmap over het overeenkomende verpakte bronpad, zoals `/app/extensions/synology-chat`. OpenClaw ontdekt die gemounte bron- overlay vóór `/app/dist/extensions/synology-chat`; een gewone gekopieerde bronmap blijft inert, zodat normale verpakte installaties nog steeds de gecompileerde dist gebruiken.

Voor runtime-hookdebugging:

  * `openclaw plugins inspect <id> --runtime --json` toont geregistreerde hooks en diagnostics uit een module-geladen inspectiepass. Runtime-inspectie installeert nooit afhankelijkheden; gebruik `openclaw doctor --fix` om legacy-afhankelijkheidsstatus op te schonen of ontbrekende downloadbare Plugins te herstellen waarnaar in configuratie wordt verwezen.
  * `openclaw gateway status --deep --require-rpc` bevestigt de bereikbare Gateway, service/proces-hints, configuratiepad en RPC-gezondheid.
  * Niet-gebundelde conversation hooks (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) vereisen `plugins.entries.<id>.hooks.allowConversationAccess=true`.


Gebruik `--link` om het kopiëren van een lokale map te vermijden (voegt toe aan `plugins.load.paths`):

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Plugin-index

Installatiemetadata van Plugins is machinebeheerde staat, geen gebruikersconfiguratie. Installaties en updates schrijven deze naar `plugins/installs.json` onder de actieve OpenClaw-statusmap. De top-level `installRecords`-map is de duurzame bron van installatiemetadata, inclusief records voor kapotte of ontbrekende Plugin-manifests. De `plugins`-array is de van manifest afgeleide koude registry-cache. Het bestand bevat een waarschuwing om het niet te bewerken en wordt gebruikt door `openclaw plugins update`, uninstall, diagnostics en de koude Plugin-registry.

Wanneer OpenClaw meegeleverde legacy `plugins.installs`-records in configuratie ziet, behandelen runtime-lezingen ze als compatibiliteitsinvoer zonder `openclaw.json` te herschrijven. Expliciete Plugin-schrijfacties en `openclaw doctor --fix` verplaatsen die records naar de Plugin-index en verwijderen de configuratiesleutel wanneer configuratieschrijfacties zijn toegestaan; als een van beide schrijfacties mislukt, blijven de configuratierecords behouden zodat de installatiemetadata niet verloren gaat.

### De-installeren

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` verwijdert Plugin-records uit `plugins.entries`, de blijvend opgeslagen Plugin-index, Plugin-allow/deny-listvermeldingen en gelinkte `plugins.load.paths`-vermeldingen waar van toepassing. Tenzij `--keep-files` is ingesteld, verwijdert uninstall ook de bijgehouden beheerde installatiemap wanneer die zich binnen OpenClaw's Plugin-extensions-root bevindt. Voor Active Memory-Plugins wordt het geheugenslot teruggezet naar `memory-core`.

### Bijwerken

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

Updates zijn van toepassing op bijgehouden Plugin-installaties in de beheerde Plugin-index en bijgehouden hook-pack-installaties in `hooks.internal.installs`.

Plugin-id versus npm-spec oplossen

Wanneer je een Plugin-id doorgeeft, hergebruikt OpenClaw de vastgelegde installatiespec voor die Plugin. Dat betekent dat eerder opgeslagen dist-tags zoals `@beta` en exacte vastgepinde versies bij latere `update <id>`-runs gebruikt blijven worden.

Voor npm-installaties kun je ook een expliciete npm-pakketspec met een dist-tag of exacte versie doorgeven. OpenClaw lost die pakketnaam terug op naar het bijgehouden Plugin-record, werkt die geïnstalleerde Plugin bij en legt de nieuwe npm-spec vast voor toekomstige id-gebaseerde updates.

Het doorgeven van de npm-pakketnaam zonder versie of tag lost ook terug op naar het bijgehouden Plugin-record. Gebruik dit wanneer een Plugin was vastgepind op een exacte versie en je deze terug wilt verplaatsen naar de standaard releaselijn van de registry.

Updates voor het bètakanaal

`openclaw plugins update` hergebruikt de bijgehouden Plugin-spec tenzij je een nieuwe spec doorgeeft. `openclaw update` kent daarnaast het actieve OpenClaw-updatekanaal: op het bètakanaal proberen npm- en ClawHub-Plugin-records op de standaardlijn eerst `@beta` en vallen daarna terug op de vastgelegde default/latest-spec als er geen Plugin-bètarelease bestaat. Die fallback wordt als waarschuwing gemeld en laat de core-update niet mislukken. Exacte versies en expliciete tags blijven aan die selector vastgepind.

Versiecontroles en integriteitsdrift

Vóór een live npm-update controleert OpenClaw de geïnstalleerde pakketversie tegen de metadata van de npm-registry. Als de geïnstalleerde versie en vastgelegde artefactidentiteit al overeenkomen met het opgeloste doel, wordt de update overgeslagen zonder te downloaden, opnieuw te installeren of `openclaw.json` te herschrijven.

Wanneer een opgeslagen integrity-hash bestaat en de opgehaalde artefacthash verandert, behandelt OpenClaw dat als npm-artefactdrift. De interactieve opdracht `openclaw plugins update` drukt de verwachte en werkelijke hashes af en vraagt om bevestiging voordat wordt doorgegaan. Niet-interactieve updatehelpers falen gesloten tenzij de aanroeper een expliciet voortzettingsbeleid aanlevert.

\--dangerously-force-unsafe-install bij update

`--dangerously-force-unsafe-install` is ook beschikbaar bij `plugins update` als noodoverride voor foutpositieven in de ingebouwde dangerous-code-scan tijdens Plugin-updates. Het omzeilt nog steeds geen Plugin-`before_install`-beleidsblokkades of blokkering door scanfouten, en het is alleen van toepassing op Plugin-updates, niet op hook-pack-updates.

### Inspecteren

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect toont identiteit, laadstatus, bron, manifestmogelijkheden, beleidsvlaggen, diagnostics, installatiemetadata, bundelmogelijkheden en eventueel gedetecteerde MCP- of LSP-serverondersteuning zonder standaard Plugin-runtime te importeren. Voeg `--runtime` toe om de Plugin-module te laden en geregistreerde hooks, tools, commands, services, gateway methods en HTTP-routes op te nemen. Runtime-inspectie meldt ontbrekende Plugin-afhankelijkheden rechtstreeks; installaties en reparaties blijven in `openclaw plugins install`, `openclaw plugins update` en `openclaw doctor --fix`.

CLI-opdrachten die eigendom zijn van een Plugin worden meestal geïnstalleerd als root-`openclaw`-opdrachtgroepen, maar Plugins kunnen ook geneste opdrachten registreren onder een core-parent zoals `openclaw nodes`. Nadat `inspect --runtime` een opdracht onder `cliCommands` toont, voer je deze uit op het vermelde pad; bijvoorbeeld: een Plugin die `demo-git` registreert, kan worden geverifieerd met `openclaw demo-git ping`.

Elke Plugin wordt geclassificeerd op basis van wat deze daadwerkelijk tijdens runtime registreert:

  * **gewone-capability** — één capabilitytype (bijv. een Plugin die alleen provider is)
  * **hybride-capability** — meerdere capabilitytypen (bijv. tekst + spraak + afbeeldingen)
  * **alleen-hook** — alleen hooks, geen capabilities of oppervlakken
  * **niet-capability** — tools/opdrachten/services maar geen capabilities


Zie [Plugin-vormen](</nl/plugins/architecture#plugin-shapes>) voor meer over het capabilitymodel.

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` rapporteert laadfouten van Plugins, manifest-/discoverydiagnostiek en compatibiliteitsmeldingen. Als alles schoon is, drukt het `No plugin issues detected.` af.

Als een geconfigureerde Plugin op schijf aanwezig is maar wordt geblokkeerd door de padveiligheidscontroles van de loader, behoudt configvalidatie de Plugin-vermelding en rapporteert deze als `present but blocked`. Los de voorafgaande diagnostiek voor de geblokkeerde Plugin op, zoals padeigendom of wereldwijd schrijfbare machtigingen, in plaats van de configuratie `plugins.entries.<id>` of `plugins.allow` te verwijderen.

Voor modulevormfouten zoals ontbrekende `register`-/`activate`-exports, voer opnieuw uit met `OPENCLAW_PLUGIN_LOAD_DEBUG=1` om een compacte samenvatting van de exportvorm in de diagnostische uitvoer op te nemen.

### Registry

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

De lokale Plugin-registry is OpenClaw's blijvend opgeslagen model voor koude reads voor geïnstalleerde Plugin-identiteit, inschakeling, bronmetadata en eigenaarschap van bijdragen. Normaal opstarten, provider-eigenaarsopzoekingen, classificatie van kanaalinstellingen en Plugin-inventaris kunnen dit lezen zonder Plugin-runtime-modules te importeren.

Gebruik `plugins registry` om te controleren of de blijvend opgeslagen registry aanwezig, actueel of verouderd is. Gebruik `--refresh` om deze opnieuw op te bouwen vanuit de blijvend opgeslagen Plugin-index, het configuratiebeleid en manifest-/pakketmetadata. Dit is een herstelpad, geen runtime-activeringspad.

`openclaw doctor --fix` herstelt ook registry-aangrenzende beheerde npm-drift: als een verweesd of hersteld `@openclaw/*`-pakket onder de beheerde Plugin-npm-root een gebundelde Plugin overschaduwt, verwijdert doctor dat verouderde pakket en bouwt de registry opnieuw op zodat opstarten valideert tegen het gebundelde manifest. Doctor koppelt ook het hostpakket `openclaw` opnieuw aan beheerde npm-Plugins die `peerDependencies.openclaw` declareren, zodat pakketlokale runtime-imports zoals `openclaw/plugin-sdk/*` na updates of npm-reparaties worden opgelost.

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

Marketplace list accepteert een lokaal marketplace-pad, een `marketplace.json`-pad, een GitHub-shorthand zoals `owner/repo`, een GitHub-repo-URL of een git-URL. `--json` drukt het opgeloste bronlabel af plus het geparste marketplace-manifest en de Plugin-vermeldingen.

## Gerelateerd

  * [Plugins bouwen](</nl/plugins/building-plugins>)
  * [CLI-referentie](</nl/cli>)
  * [ClawHub](</nl/clawhub>)


Was this useful?YesNo
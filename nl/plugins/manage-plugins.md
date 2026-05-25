---
title: Plugins beheren
source_url: https://docs.openclaw.ai/nl/plugins/manage-plugins
scraped_at: 2026-05-25
---

De meeste plugin-workflows bestaan uit een paar opdrachten: zoeken, installeren, de Gateway herstarten, verifiëren en verwijderen wanneer je de plugin niet meer nodig hebt.

## Plugins weergeven

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Gebruik `--json` voor scripts. Het bevat registerdiagnostiek en de statische `dependencyStatus` van elke plugin wanneer het pluginpakket `dependencies` of `optionalDependencies` declareert.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` is een koude inventariscontrole. Het toont wat OpenClaw kan vinden via configuratie, manifests en het pluginregister; het bewijst niet dat een al draaiend Gateway-proces de plugin-runtime heeft geïmporteerd.

## Plugins installeren

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Herstart na het installeren van plugincode de Gateway die je kanalen bedient:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Gebruik `inspect --runtime` wanneer je bewijs nodig hebt dat de plugin runtime-oppervlakken heeft geregistreerd, zoals tools, hooks, services, Gateway-methoden of CLI-opdrachten die eigendom zijn van de plugin.

## Plugins bijwerken

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Als een plugin is geïnstalleerd vanaf een npm-dist-tag zoals `@beta`, gebruiken latere aanroepen van `update <plugin-id>` die vastgelegde tag opnieuw. Door een expliciete npm-specificatie door te geven, wordt de gevolgde installatie voor toekomstige updates naar die specificatie overgezet.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

De tweede opdracht verplaatst een plugin terug naar de standaardreleasereeks van het register wanneer deze eerder was vastgezet op een exacte versie of tag.

Wanneer `openclaw update` op het bètakanaal draait, proberen npm- en ClawHub-pluginrecords op de standaardreeks eerst de overeenkomende `@beta`-release van de plugin. Als die bètarelease niet bestaat, valt OpenClaw terug op de vastgelegde standaard-/laatste specificatie. Voor npm-plugins valt OpenClaw ook terug wanneer het bètapakket bestaat maar niet door de installatievalidatie komt. Exacte versies en expliciete tags zoals `@rc` of `@beta` blijven behouden.

## Plugins verwijderen

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Verwijderen haalt de configuratievermelding van de plugin, het pluginindexrecord, allow-/denylist- vermeldingen en gekoppelde laadpaden weg wanneer van toepassing. Beheerde installatiemappen worden verwijderd, tenzij je `--keep-files` doorgeeft.

In Nix-modus (`OPENCLAW_NIX_MODE=1`) zijn opdrachten voor het installeren, bijwerken, verwijderen, inschakelen en uitschakelen van plugins uitgeschakeld. Beheer die keuzes in plaats daarvan in de Nix-bron voor de installatie; gebruik voor nix-openclaw de agent-first [Snelstart](<https://github.com/openclaw/nix-openclaw#quick-start>).

## Plugins publiceren

Je kunt externe plugins publiceren naar [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) of beide.

### Publiceren naar ClawHub

ClawHub is het primaire openbare ontdekkingsoppervlak voor OpenClaw-plugins. Het geeft gebruikers doorzoekbare metadata, versiegeschiedenis en resultaten van registerscans vóór installatie.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Gebruikers installeren vanuit ClawHub met:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

De kale vorm controleert nog steeds eerst ClawHub.

### Publiceren naar [npmjs.com](<http://npmjs.com>)

Native npm-plugins moeten een pluginmanifest en OpenClaw-entrypointmetadata in `package.json` bevatten.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Gebruikers installeren npm-only met:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Als hetzelfde pakket ook beschikbaar is op ClawHub, slaat `npm:` de ClawHub-lookup over en forceert het npm-resolutie.

## Bronkeuze

  * **ClawHub** : gebruik dit wanneer je OpenClaw-native ontdekking, scansamenvattingen, versies en installatietips wilt.
  * **[npmjs.com](<http://npmjs.com>)** : gebruik dit wanneer je al JavaScript-pakketten levert of npm- dist-tags/private-registerworkflows nodig hebt.
  * **Git** : gebruik dit wanneer je rechtstreeks vanaf een branch, tag of commit wilt installeren.
  * **Lokaal pad** : gebruik dit wanneer je een plugin op dezelfde machine ontwikkelt of test.


## Gerelateerd

  * [Plugins](</nl/tools/plugin>) \- overzicht en probleemoplossing
  * [`openclaw plugins`](</nl/cli/plugins>) \- volledige CLI-referentie
  * [ClawHub](</nl/clawhub/cli>) \- publicatie- en registerbewerkingen
  * [Plugins bouwen](</nl/plugins/building-plugins>) \- een pluginpakket maken
  * [Pluginmanifest](</nl/plugins/manifest>) \- manifest- en pakketmetadata


Was this useful?YesNo
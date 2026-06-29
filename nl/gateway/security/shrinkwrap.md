---
title: npm shrinkwrap
source_url: https://docs.openclaw.ai/nl/gateway/security/shrinkwrap
scraped_at: 2026-06-29
---

Gateway & OpsGateway

OpenClaw-broncheckouts gebruiken `pnpm-lock.yaml`. Gepubliceerde OpenClaw npm-pakketten gebruiken `npm-shrinkwrap.json`, npm's publiceerbare dependency-lockfile, zodat pakketinstallaties de dependency-grafiek gebruiken die tijdens de release is beoordeeld.

## De eenvoudige versie

Shrinkwrap is een ontvangstbewijs voor de dependency-structuur die met een npm-pakket wordt meegeleverd. Het vertelt npm welke exacte transitieve pakketversies moeten worden geïnstalleerd.

Voor OpenClaw-releases betekent dat:

  * het gepubliceerde pakket vraagt npm niet om tijdens de installatie een nieuwe dependency-grafiek te bedenken;
  * dependency-wijzigingen worden eenvoudiger te beoordelen omdat ze in een lockfile verschijnen;
  * releasevalidatie kan dezelfde grafiek testen die gebruikers zullen installeren;
  * verrassingen rond pakketgrootte of native dependencies zijn gemakkelijker te signaleren vóór publicatie.


Shrinkwrap is geen sandbox. Het maakt een dependency op zichzelf niet veilig, en het vervangt hostisolatie, `openclaw security audit`, pakketherkomst of installatiesmoketests niet.

Het korte mentale model:

Bestand | Waar het ertoe doet | Wat het betekent  
---|---|---  
`pnpm-lock.yaml` | OpenClaw-broncheckout | Maintainer-dependency-grafiek  
`npm-shrinkwrap.json` | Gepubliceerd npm-pakket | npm-installatiegrafiek voor gebruikers  
`package-lock.json` | Lokale npm-apps | Niet het publicatiecontract van OpenClaw  
  
## Waarom OpenClaw dit gebruikt

OpenClaw is een Gateway, Plugin-host, modelrouter en agentruntime. Een standaardinstallatie kan invloed hebben op opstarttijd, schijfgebruik, native pakketdownloads en blootstelling aan supplychain-risico's.

Shrinkwrap geeft releasebeoordeling een stabiele grens:

  * reviewers kunnen transitieve dependency-beweging zien;
  * pakketvalidators kunnen onverwachte lockfile-drift afwijzen;
  * pakketacceptatie kan installaties testen met de grafiek die wordt meegeleverd;
  * Plugin-pakketten kunnen hun eigen vergrendelde dependency-grafiek meenemen in plaats van erop te vertrouwen dat het rootpakket Plugin-specifieke dependencies bezit.


Het doel is niet "meer lockfiles". Het doel is reproduceerbare release-installaties met duidelijk eigenaarschap.

## Technische details

Het root-`openclaw` npm-pakket en npm-Plugin-pakketten die eigendom zijn van OpenClaw bevatten `npm-shrinkwrap.json` wanneer ze publiceren. Geschikte Plugin-pakketten die eigendom zijn van OpenClaw kunnen ook publiceren met expliciete `bundledDependencies`, zodat hun runtime-dependencybestanden in de Plugin-tarball worden meegeleverd in plaats van alleen afhankelijk te zijn van resolutie tijdens installatie.

Onderhoud de grens zo:

bashCopy code
[code]
    pnpm deps:shrinkwrap:generatepnpm deps:shrinkwrap:check
[/code]

De generator lost npm's publiceerbare lockformaat op, maar wijst gegenereerde pakketversies af die nog niet aanwezig zijn in `pnpm-lock.yaml`. Dat houdt de pnpm-grens voor dependency-leeftijd, overrides en patchbeoordeling intact.

Gebruik root-only opdrachten alleen wanneer je bewust het rootpakket vernieuwt zonder Plugin-pakketten aan te raken:

bashCopy code
[code]
    pnpm deps:shrinkwrap:root:generatepnpm deps:shrinkwrap:root:check
[/code]

Beoordeel deze bestanden als security-gevoelig:

  * `pnpm-lock.yaml`
  * `npm-shrinkwrap.json`
  * gebundelde Plugin-dependency-payloads
  * elke `package-lock.json`-diff


OpenClaw-pakketvalidators vereisen shrinkwrap in nieuwe rootpakket-tarballs. Het npm-publicatiepad voor Plugins controleert Plugin-lokale shrinkwrap, installeert pakketlokale gebundelde dependencies en maakt daarna een pakket of publiceert. Pakketvalidators wijzen `package-lock.json` af voor gepubliceerde OpenClaw-pakketten.

Om een gepubliceerd rootpakket te inspecteren:

bashCopy code
[code]
    npm pack openclaw@<version> --json --pack-destination /tmp/openclaw-packtar -tf /tmp/openclaw-pack/openclaw-<version>.tgz | grep '^package/npm-shrinkwrap.json$'
[/code]

Om een Plugin-pakket van OpenClaw te inspecteren:

bashCopy code
[code]
    npm pack @openclaw/discord@<version> --json --pack-destination /tmp/openclaw-plugin-packtar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/npm-shrinkwrap.json$'tar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/node_modules/'
[/code]

Achtergrond: [npm-shrinkwrap.json](<https://docs.npmjs.com/cli/v11/configuring-npm/npm-shrinkwrap-json>).

Was this useful?YesNo

Open issue
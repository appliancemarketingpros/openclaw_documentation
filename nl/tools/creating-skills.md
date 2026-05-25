---
title: Skills aanmaken
source_url: https://docs.openclaw.ai/nl/tools/creating-skills
scraped_at: 2026-05-25
---

Skills leren de agent hoe en wanneer tools te gebruiken. Elke skill is een directory met een `SKILL.md`-bestand met YAML-frontmatter en markdown-instructies.

Zie [Skills](</nl/tools/skills>) voor hoe Skills worden geladen en geprioriteerd.

## Maak je eerste skill

* ### Maak de skill-directory

Skills staan in je werkruimte. Maak een nieuwe map:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Schrijf SKILL.md

Maak `SKILL.md` in die directory. De frontmatter definieert metadata, en de markdown-body bevat instructies voor de agent.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Gebruik hyphen-case met kleine letters, cijfers en koppeltekens voor de skill `name`. Houd de mapnaam en frontmatter-`name` gelijk.

* ### Voeg tools toe (optioneel)

Je kunt aangepaste toolschema's definiëren in de frontmatter of de agent instrueren bestaande systeemtools te gebruiken (zoals `exec` of `browser`). Skills kunnen ook binnen plugins worden meegeleverd naast de tools die ze documenteren.

* ### Laad de skill

Start een nieuwe sessie zodat OpenClaw de skill oppikt:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Controleer of de skill is geladen:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Test het

Stuur een bericht dat de skill zou moeten triggeren:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Of chat gewoon met de agent en vraag om een begroeting.

## Referentie voor skill-metadata

De YAML-frontmatter ondersteunt deze velden:

Veld | Vereist | Beschrijving  
---|---|---  
`name` | Ja | Unieke identifier met kleine letters, cijfers en koppeltekens  
`description` | Ja | Eénregelige beschrijving die aan de agent wordt getoond  
`metadata.openclaw.os` | Nee | OS-filter (`["darwin"]`, `["linux"]`, enz.)  
`metadata.openclaw.requires.bins` | Nee | Vereiste binaries op PATH  
`metadata.openclaw.requires.config` | Nee | Vereiste config-sleutels  
  
## Best practices

  * **Wees beknopt** — instrueer het model over _wat_ het moet doen, niet hoe het een AI moet zijn
  * **Veiligheid eerst** — als je skill `exec` gebruikt, zorg er dan voor dat prompts geen willekeurige command-injectie vanuit onvertrouwde invoer toestaan
  * **Test lokaal** — gebruik `openclaw agent --message "..."` om te testen voordat je deelt
  * **Gebruik ClawHub** — blader door en draag Skills bij op [ClawHub](<https://clawhub.ai>)


## Waar Skills staan

Locatie | Voorrang | Scope  
---|---|---  
`\<workspace\>/skills/` | Hoogst | Per agent  
`\<workspace\>/.agents/skills/` | Hoog | Per werkruimte-agent  
`~/.agents/skills/` | Gemiddeld | Gedeeld agentprofiel  
`~/.openclaw/skills/` | Gemiddeld | Gedeeld (alle agents)  
Gebundeld (meegeleverd met OpenClaw) | Laag | Globaal  
`skills.load.extraDirs` | Laagst | Aangepaste gedeelde mappen  
  
## Gerelateerd

  * [Skills-referentie](</nl/tools/skills>) — laad-, voorrangs- en gatingregels
  * [Skills-config](</nl/tools/skills-config>) — `skills.*`-configschema
  * [ClawHub](</nl/clawhub>) — openbaar skill-register
  * [Plugins bouwen](</nl/plugins/building-plugins>) — plugins kunnen Skills meeleveren


Was this useful?YesNo
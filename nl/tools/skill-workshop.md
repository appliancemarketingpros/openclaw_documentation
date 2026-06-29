---
title: Skill-workshop
source_url: https://docs.openclaw.ai/nl/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skill Workshop is OpenClaw's beheerste pad voor het maken en bijwerken van workspace-skills.

Agents en operators schrijven via dit pad niet rechtstreeks actieve `SKILL.md`-bestanden. Ze maken eerst een **voorstel**. Een voorstel is een concept in behandeling met de voorgestelde skill-inhoud, doelbinding, scannerstatus, hashes, metadata van ondersteuningsbestanden en rollback-metadata. Het wordt pas een live skill wanneer het wordt toegepast.

Skill Workshop schrijft alleen workspace-skills. Het wijzigt geen gebundelde, plugin-, ClawHub-, extra-root-, beheerde, personal-agent- of systeemskills.

## Hoe het werkt

  * **Eerst een voorstel:** gegenereerde skill-inhoud wordt opgeslagen als `PROPOSAL.md`, niet als `SKILL.md`.
  * **Toepassen is de enige live schrijfopdracht:** maken, bijwerken en herzien wijzigen geen actieve skills.
  * **Beperkt tot de workspace:** aanmaken richt zich op de workspace-root `skills/`. Updates zijn alleen toegestaan voor schrijfbare workspace-skills.
  * **Niet overschrijven:** aanmaken mislukt als de doel-skill al bestaat.
  * **Hashgebonden:** updatevoorstellen binden aan de huidige doelhash en worden verouderd als de live skill verandert voordat het voorstel wordt toegepast.
  * **Scanner-gated:** toepassen voert vóór het schrijven opnieuw scans uit.
  * **Herstelbaar:** toepassen schrijft rollback-metadata voordat live bestanden worden gewijzigd.
  * **Consistente oppervlakken:** chat, CLI en Gateway roepen allemaal dezelfde Skill Workshop-service aan.


## Levenscyclus

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Alleen `pending`-voorstellen kunnen worden herzien, toegepast, afgewezen of in quarantaine geplaatst.

## Chat

Vraag de agent om de gewenste skill. De agent roept `skill_workshop` aan en retourneert een voorstel-id.

Aanmaken:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Een bestaande workspace-skill bijwerken:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Itereren op een voorstel in behandeling:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

Standaard tonen door agents geïnitieerde `apply`, `reject` en `quarantine` een goedkeuringsprompt voordat ze worden uitgevoerd. Stel `skills.workshop.approvalPolicy` in op `"auto"` om de prompt over te slaan voor vertrouwde omgevingen.

## CLI

Maak een nieuw skillvoorstel:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Maak een updatevoorstel voor een bestaande workspace-skill:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

Weergeven en inspecteren:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Herzien vóór goedkeuring:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Het voorstel afronden:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Voorstelinhoud

Zolang het voorstel in behandeling is, wordt het opgeslagen als `PROPOSAL.md` met frontmatter die alleen voor voorstellen geldt:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

Bij toepassen schrijft Skill Workshop de actieve `SKILL.md` en verwijdert het velden die alleen voor voorstellen gelden: `status`, voorstel-`version` en voorstel-`date`.

## Ondersteuningsbestanden

Gebruik `--proposal-dir` wanneer de voorgestelde skill bestanden naast `PROPOSAL.md` nodig heeft:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

De map moet `PROPOSAL.md` bevatten. Ondersteuningsbestanden moeten onder staan:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop scant, hasht en bewaart ondersteuningsbestanden met het voorstel. Ze worden pas bij toepassen naast de live `SKILL.md` geschreven.

Afgewezen paden voor ondersteuningsbestanden omvatten absolute paden, verborgen padsegmenten, path traversal, overlappende paden, uitvoerbare bestanden uit voorstelmappen, niet-UTF-8-tekst, null-bytes en bestanden buiten de standaardmappen voor ondersteuning.

## Agent-tool

Het model gebruikt `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Agents moeten `skill_workshop` gebruiken voor gegenereerd skillwerk. Ze mogen geen voorstelbestanden maken of wijzigen via `write`, `edit`, `exec`, shellopdrachten of directe bestandssysteembewerkingen.

## Goedkeuring en autonomie

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: staat OpenClaw toe om voorstellen in behandeling te maken op basis van duurzame gesprekssignalen na succesvolle beurten. Standaard: `false`.
  * `allowSymlinkTargetWrites`: staat toepassen toe om door workspace-skill-symlinks heen te schrijven waarvan het echte doel is opgenomen in `skills.load.allowSymlinkTargets`. Standaard: `false`.
  * `approvalPolicy: "pending"`: vereist een goedkeuringsprompt vóór door agents geïnitieerde `apply`, `reject` of `quarantine`.
  * `approvalPolicy: "auto"`: slaat die goedkeuringsprompt over. De agent moet de actie nog steeds aanroepen.
  * `maxPending`: beperkt voorstellen in behandeling en in quarantaine per workspace.
  * `maxSkillBytes`: beperkt de grootte van de voorstelbody. Standaard: `40000`.


Voorstelbeschrijvingen zijn altijd beperkt tot 160 bytes.

## Gateway-methoden

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Alleen-lezen-methoden vereisen `operator.read`. Muterende methoden vereisen `operator.admin`.

## Opslag

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Standaardstatusmap: `~/.openclaw`.

  * `proposal.json`: canoniek voorstelrecord.
  * `proposals.json`: snelle lijstindex, opnieuw op te bouwen vanuit voorstelmappen.
  * `PROPOSAL.md`: skillvoorstel in behandeling.
  * `rollback.json`: herstelmetadata die wordt geschreven voordat toepassen live bestanden wijzigt.


## Limieten

  * Beschrijving: 160 bytes.
  * Voorstelbody: `skills.workshop.maxSkillBytes` (standaard 40.000).
  * Ondersteuningsbestanden: 64 per voorstel.
  * Grootte van ondersteuningsbestand: elk 256 KB, totaal 2 MB.
  * Voorstellen in behandeling en in quarantaine: `skills.workshop.maxPending` per workspace (standaard 50).


## Probleemoplossing

Probleem | Oplossing  
---|---  
`Skill proposal description is too large` | Verkort `description` tot 160 bytes of minder.  
`Skill proposal content is too large` | Verkort de voorstelbody of verhoog `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Herzie het voorstel tegen het huidige doel, of maak een nieuw voorstel.  
`Proposal scan failed` | Inspecteer scannerbevindingen en herzie het voorstel daarna of plaats het in quarantaine.  
`untrusted symlink target` | Configureer `skills.load.allowSymlinkTargets` en schakel `skills.workshop.allowSymlinkTargetWrites` alleen in voor bewust gedeelde skillroots.  
`Support file paths must be under one of...` | Verplaats ondersteuningsbestanden onder `assets/`, `examples/`, `references/`, `scripts/` of `templates/`.  
Voorstel wordt niet in de lijst weergegeven | Controleer de geselecteerde `--agent`-workspace en `OPENCLAW_STATE_DIR`.  
Agent kan `skill_workshop` niet aanroepen | Controleer het actieve toolbeleid en de runmodus. `coding` bevat de tool; beperkende `tools.allow`-beleidsregels moeten deze expliciet vermelden, en sandbox-runs moeten een normale host-side agentsessie of de CLI gebruiken.  
  
## Gerelateerd

  * [Skills](</nl/tools/skills>) voor laadvolgorde, prioriteit en zichtbaarheid
  * [Skills maken](</nl/tools/creating-skills>) voor de basis van handgeschreven `SKILL.md`
  * [Skills-configuratie](</nl/tools/skills-config>) voor het volledige `skills.workshop`-schema
  * [Skills-CLI](</nl/cli/skills>) voor `openclaw skills`-opdrachten


Was this useful?YesNo

Open issue
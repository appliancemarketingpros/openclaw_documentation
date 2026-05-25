---
title: Parallelle specialistische sporen
source_url: https://docs.openclaw.ai/nl/concepts/parallel-specialist-lanes
scraped_at: 2026-05-25
---

Parallelle specialistische lanes laten één Gateway verschillende chats of ruimtes naar verschillende agents routeren, terwijl de gebruikerservaring snel blijft. De kunst is om parallelisme te behandelen als een ontwerpprobleem rond schaarse resources, niet alleen als "meer agents".

## Basisprincipes

Een specialistische lane verbetert de doorvoer alleen wanneer die de concurrentie om de echte knelpunten vermindert:

  * **Sessievergrendelingen** : slechts één run mag een bepaalde sessie tegelijk wijzigen.
  * **Globale modelcapaciteit** : alle zichtbare chatruns delen nog steeds providerlimieten.
  * **Toolcapaciteit** : shell-, browser-, netwerk- en repositorywerk kan trager zijn dan de modelbeurt zelf.
  * **Contextbudget** : lange transcripties maken elke toekomstige beurt trager en minder gericht.
  * **Onduidelijkheid over eigenaarschap** : dubbele agents die hetzelfde werk doen verspillen capaciteit.


OpenClaw serialiseert runs al per sessie en begrenst globale paralleliteit via de [opdrachtwachtrij](</nl/concepts/queue>). Specialistische lanes voegen daar beleid bovenop toe: welke agent eigenaar is van welk werk, wat in chat blijft, en wat achtergrondwerk wordt.

## Aanbevolen uitrol

### Fase 1: lane-contracten + zwaar achtergrondwerk

Geef elke lane een geschreven contract in de workspace en systeemprompt:

  * **Doel** : het werk waarvan deze lane eigenaar is.
  * **Niet-doelen** : werk dat deze lane moet overdragen in plaats van proberen uit te voeren.
  * **Chatbudget** : snelle antwoorden blijven in chat; lange taken moeten kort worden bevestigd en daarna in een achtergrond-sub-agent of taak worden uitgevoerd.
  * **Overdrachtsregel** : wanneer een andere lane eigenaar is van het werk, zeg waar het heen moet en geef een compacte overdrachtssamenvatting.
  * **Toolrisicoregel** : geef de voorkeur aan het kleinste tool-oppervlak dat de taak kan uitvoeren.


Dit is de goedkoopste fase en lost de meeste verstopping op: één codeertaak verandert de onderzoekslane niet langer in stroop, en elke chat houdt zijn eigen context schoon.

### Fase 2: prioriteits- en gelijktijdigheidsregelingen

Stem wachtrij- en modelcapaciteit af op de bedrijfswaarde van elke lane:

json5Copy code
[code]
    {  agents: {    defaults: {      maxConcurrent: 4,      subagents: { maxConcurrent: 8, delegationMode: "prefer" },    },  },  messages: {    queue: {      mode: "collect",      debounceMs: 1000,      cap: 20,      drop: "summarize",    },  },}
[/code]

Gebruik directe/persoonlijke chats en agents voor productiebeheer voor werk met hoge prioriteit. Laat onderzoek, conceptschrijven en batchgewijs coderen naar achtergrondtaken verplaatsen wanneer het systeem druk is.

### Fase 3: coördinator / verkeersregelaar

Voeg een klein coördinatorpatroon toe zodra meerdere lanes actief zijn:

  * Houd actieve lane-taken en eigenaars bij.
  * Detecteer dubbele verzoeken tussen groepen.
  * Routeer overdrachtssamenvattingen tussen lanes.
  * Toon alleen blokkades, voltooide resultaten en beslissingen die de mens moet nemen.


Begin hier niet. Een coördinator zonder lane-contracten coördineert alleen chaos.

## Minimale template voor lane-contract

mdCopy code
[code]
    # Lane contract ## Owns - <job this lane is responsible for> ## Does not own - <work to hand off> ## Chat budget - Answer quick questions directly.- For multi-step, slow, or tool-heavy work: acknowledge briefly, spawn/background  the work, then return the result when complete. ## Handoff If another lane owns the request, reply with: - target lane- objective- relevant context- exact next action ## Tool posture Use the smallest tool surface that can complete the task. Avoid broad shell ornetwork work unless this lane explicitly owns it.
[/code]

## Gerelateerd

  * [Routering voor meerdere agents](</nl/concepts/multi-agent>)
  * [Opdrachtwachtrij](</nl/concepts/queue>)
  * [Sub-agents](</nl/tools/subagents>)


Was this useful?YesNo
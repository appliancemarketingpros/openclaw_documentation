---
title: Broadcastgroepen
source_url: https://docs.openclaw.ai/nl/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Overzicht

Broadcastgroepen laten meerdere agents hetzelfde bericht gelijktijdig verwerken en beantwoorden. Zo kun je gespecialiseerde agentteams maken die samenwerken in één WhatsApp-groep of DM, allemaal met één telefoonnummer.

Huidige scope: **alleen WhatsApp** (webkanaal).

Broadcastgroepen worden geëvalueerd na kanaal-allowlists en groepsactiveringsregels. In WhatsApp-groepen betekent dit dat broadcasts plaatsvinden wanneer OpenClaw normaal gesproken zou antwoorden (bijvoorbeeld: bij een vermelding, afhankelijk van je groepsinstellingen).

## Gebruiksscenario's

1\. Gespecialiseerde agentteams

Implementeer meerdere agents met afgebakende, gerichte verantwoordelijkheden:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Elke agent verwerkt hetzelfde bericht en geeft zijn gespecialiseerde perspectief.

2\. Meertalige ondersteuning CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Workflows voor kwaliteitsborging CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Taakautomatisering CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Configuratie

### Basisconfiguratie

Voeg een `broadcast`-sectie op het hoogste niveau toe (naast `bindings`). Sleutels zijn WhatsApp-peer-id's:

  * groepschats: groeps-JID (bijv. `120363403215116621@g.us`)
  * DM's: E.164-telefoonnummer (bijv. `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Resultaat:** Wanneer OpenClaw in deze chat zou antwoorden, voert het alle drie de agents uit.

### Verwerkingsstrategie

Bepaal hoe agents berichten verwerken:

### parallel (standaard)

Alle agents verwerken gelijktijdig:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequentieel

Agents verwerken op volgorde (de ene wacht tot de vorige klaar is):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Volledig voorbeeld

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Hoe het werkt

### Berichtstroom

* ### Binnenkomend bericht komt aan

Een WhatsApp-groeps- of DM-bericht komt aan.

* ### Broadcastcontrole

Het systeem controleert of de peer-id in `broadcast` staat.

* ### Als deze in de broadcastlijst staat

  * Alle vermelde agents verwerken het bericht.
  * Elke agent heeft zijn eigen sessiesleutel en geïsoleerde context.
  * Agents verwerken parallel (standaard) of sequentieel.


* ### Als deze niet in de broadcastlijst staat

Normale routing is van toepassing (eerste overeenkomende binding).

### Sessiesisolatie

Elke agent in een broadcastgroep behoudt volledig afzonderlijke:

  * **Sessiesleutels** (`agent:alfred:whatsapp:group:120363...` versus `agent:baerbel:whatsapp:group:120363...`)
  * **Gespreksgeschiedenis** (agent ziet de berichten van andere agents niet)
  * **Workspace** (afzonderlijke sandboxes indien geconfigureerd)
  * **Tooltoegang** (verschillende toestaan/weigeren-lijsten)
  * **Geheugen/context** (afzonderlijke [IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), enz.)
  * **Groepscontextbuffer** (recente groepsberichten die voor context worden gebruikt) wordt per peer gedeeld, zodat alle broadcastagents dezelfde context zien wanneer ze worden geactiveerd


Hierdoor kan elke agent beschikken over:

  * Verschillende persoonlijkheden
  * Verschillende tooltoegang (bijv. alleen-lezen versus lezen-schrijven)
  * Verschillende modellen (bijv. opus versus sonnet)
  * Verschillende geïnstalleerde Skills


### Voorbeeld: geïsoleerde sessies

In groep `120363403215116621@g.us` met agents `["alfred", "baerbel"]`:

### Alfreds context

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Bärbels context

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Best practices

1\. Houd agents gefocust

Ontwerp elke agent met één duidelijke verantwoordelijkheid:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Goed:** Elke agent heeft één taak. ❌ **Slecht:** Eén generieke "dev-helper"-agent.

2\. Gebruik beschrijvende namen

Maak duidelijk wat elke agent doet:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Configureer verschillende tooltoegang

Geef agents alleen de tools die ze nodig hebben:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` is alleen-lezen. `fixer` kan lezen en schrijven.

4\. Bewaak prestaties

Overweeg bij veel agents:

  * `"strategy": "parallel"` (standaard) gebruiken voor snelheid
  * Broadcastgroepen beperken tot 5-10 agents
  * Snellere modellen gebruiken voor eenvoudigere agents

5\. Handel fouten netjes af

Agents falen onafhankelijk. Een fout van één agent blokkeert de andere niet:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Compatibiliteit

### Providers

Broadcastgroepen werken momenteel met:

  * ✅ WhatsApp (geïmplementeerd)
  * 🚧 Telegram (gepland)
  * 🚧 Discord (gepland)
  * 🚧 Slack (gepland)


### Routing

Broadcastgroepen werken naast bestaande routing:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Alleen alfred antwoordt (normale routing).
  * `GROUP_B`: agent1 EN agent2 antwoorden (broadcast).


## Probleemoplossing

Agents reageren niet

**Controleer:**

  1. Agent-id's bestaan in `agents.list`.
  2. Peer-id-indeling is correct (bijv. `120363403215116621@g.us`).
  3. Agents staan niet in weigerlijsten.


**Debuggen:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Slechts één agent reageert

**Oorzaak:** Peer-id staat mogelijk in `bindings` maar niet in `broadcast`.

**Oplossing:** Voeg toe aan de broadcastconfiguratie of verwijder uit bindings.

Prestatieproblemen

Als het traag is met veel agents:

  * Verminder het aantal agents per groep.
  * Gebruik lichtere modellen (sonnet in plaats van opus).
  * Controleer de opstarttijd van de sandbox.


## Voorbeelden

Voorbeeld 1: Codereviewteam jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**Gebruiker stuurt:** Codefragment.

**Reacties:**

  * code-formatter: "Fixed indentation and added type hints"
  * security-scanner: "⚠️ SQL injection vulnerability in line 12"
  * test-coverage: "Coverage is 45%, missing tests for error cases"
  * docs-checker: "Missing docstring for function `process_data`"

Voorbeeld 2: Meertalige ondersteuning jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## API-referentie

### Configuratieschema

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Velden

Hoe agents moeten worden verwerkt. `parallel` voert alle agents gelijktijdig uit; `sequential` voert ze uit in arrayvolgorde.

WhatsApp-groeps-JID, E.164-nummer of andere peer-id. Waarde is de array met agent-id's die berichten moeten verwerken.

## Beperkingen

  1. **Max. agents:** Geen harde limiet, maar 10+ agents kunnen traag zijn.
  2. **Gedeelde context:** Agents zien elkaars reacties niet (volgens ontwerp).
  3. **Berichtvolgorde:** Parallelle reacties kunnen in willekeurige volgorde aankomen.
  4. **Snelheidslimieten:** Alle agents tellen mee voor WhatsApp-snelheidslimieten.


## Toekomstige verbeteringen

Geplande functies:

  * [ ] Modus voor gedeelde context (agents zien elkaars reacties)
  * [ ] Agentcoördinatie (agents kunnen elkaar signaleren)
  * [ ] Dynamische agentselectie (agents kiezen op basis van berichtinhoud)
  * [ ] Agentprioriteiten (sommige agents reageren vóór andere)


## Gerelateerd

  * [Kanaalroutering](</nl/channels/channel-routing>)
  * [Groepen](</nl/channels/groups>)
  * [Multi-agent-sandboxtools](</nl/tools/multi-agent-sandbox-tools>)
  * [Koppelen](</nl/channels/pairing>)
  * [Sessiebeheer](</nl/concepts/session>)


Was this useful?YesNo
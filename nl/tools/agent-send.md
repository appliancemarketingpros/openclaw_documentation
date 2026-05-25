---
title: Agent verzenden
source_url: https://docs.openclaw.ai/nl/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` voert een enkele agentbeurt uit vanaf de opdrachtregel zonder dat er een inkomend chatbericht nodig is. Gebruik dit voor gescripte workflows, testen en programmatische aflevering.

## Snel aan de slag

* ### Voer een eenvoudige agentbeurt uit

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Dit stuurt het bericht via de Gateway en drukt het antwoord af.

* ### Richt je op een specifieke agent of sessie

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Lever het antwoord af bij een kanaal

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Vlaggen

Vlag | Beschrijving  
---|---  
`--message \<text\>` | Te verzenden bericht (vereist)  
`--to \<dest\>` | Leid sessiesleutel af van een doel (telefoon, chat-id)  
`--agent \<id\>` | Richt je op een geconfigureerde agent (gebruikt zijn `main`-sessie)  
`--session-id \<id\>` | Hergebruik een bestaande sessie op id  
`--local` | Forceer lokale embedded runtime (sla Gateway over)  
`--deliver` | Stuur het antwoord naar een chatkanaal  
`--channel \<name\>` | Afleverkanaal (whatsapp, telegram, discord, slack, enz.)  
`--reply-to \<target\>` | Overschrijving van afleverdoel  
`--reply-channel \<name\>` | Overschrijving van afleverkanaal  
`--reply-account \<id\>` | Overschrijving van afleveraccount-id  
`--thinking \<level\>` | Stel denkniveau in voor het geselecteerde modelprofiel  
`--verbose \<on|full|off\>` | Stel verbose-niveau in  
`--timeout \<seconds\>` | Overschrijf agenttime-out  
`--json` | Geef gestructureerde JSON uit  
  
## Gedrag

  * Standaard gaat de CLI **via de Gateway**. Voeg `--local` toe om de embedded runtime op de huidige machine te forceren.
  * Als de Gateway onbereikbaar is, **valt de CLI terug** op de lokale embedded uitvoering.
  * Sessieselectie: `--to` leidt de sessiesleutel af (groep-/kanaaldoelen behouden isolatie; directe chats vallen samen tot `main`).
  * Thinking- en verbose-vlaggen blijven behouden in de sessieopslag.
  * Uitvoer: standaard platte tekst, of `--json` voor gestructureerde payload + metadata.
  * Met `--json --deliver` bevat de JSON afleverstatus voor verzonden, onderdrukte, gedeeltelijke en mislukte verzendingen. Zie [JSON-afleverstatus](</nl/cli/agent#json-delivery-status>).


## Voorbeelden

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Gerelateerd

[**Agent CLI-naslag** Volledige naslag voor vlaggen en opties van `openclaw agent`. ](</nl/cli/agent>) [**Subagents** Subagents op de achtergrond starten. ](</nl/tools/subagents>) [**Sessies** Hoe sessiesleutels werken en hoe `--to`, `--agent` en `--session-id` ze oplossen. ](</nl/concepts/session>) [**Slash-commando's** Native opdrachtencatalogus die binnen agentsessies wordt gebruikt. ](</nl/tools/slash-commands>)

Was this useful?YesNo
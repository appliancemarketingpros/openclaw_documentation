---
title: Gateway-integraties voor externe apps
source_url: https://docs.openclaw.ai/nl/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

Externe apps moeten vandaag via het Gateway-protocol met OpenClaw communiceren. Gebruik Gateway WebSocket- en RPC-methoden wanneer een script, dashboard, CI-taak, IDE- extensie of een ander proces agent-runs wil starten, gebeurtenissen wil streamen, op resultaten wil wachten, werk wil annuleren of Gateway-resources wil inspecteren.

## Wat vandaag beschikbaar is

Oppervlak | Status | Gebruik het voor  
---|---|---  
[Gateway-protocol](</nl/gateway/protocol>) | Gereed | WebSocket-transport, connect-handshake, auth-scopes, protocolversionering en gebeurtenissen.  
[Gateway RPC-referentie](</nl/reference/rpc>) | Gereed | Huidige Gateway-methoden voor agents, sessies, taken, modellen, tools, artefacten en goedkeuringen.  
[`openclaw agent`](</nl/cli/agent>) | Gereed | Eenmalige scriptintegratie wanneer shellen naar de CLI voldoende is.  
[`openclaw message`](</nl/cli/message>) | Gereed | Berichten of kanaalacties verzenden vanuit scripts.  
  
De broncodeboom bevat intern pakketwerk voor een toekomstige clientbibliotheek, maar dat is geen openbaar installatieoppervlak. Behandel het als preview-implementatiedetail totdat de pakketten zijn gepubliceerd en geversioneerd.

## Aanbevolen pad

  1. Start of ontdek een Gateway.
  2. Maak verbinding via het [Gateway-protocol](</nl/gateway/protocol>).
  3. Roep gedocumenteerde RPC-methoden aan uit de [Gateway RPC-referentie](</nl/reference/rpc>).
  4. Pin de OpenClaw-versie waartegen je test.
  5. Controleer de RPC-referentie opnieuw wanneer je OpenClaw upgradet.


Begin voor agent-runs met de `agent`-RPC en combineer die met `agent.wait` wanneer je een terminaal resultaat nodig hebt. Gebruik voor duurzame gespreksstatus de `sessions.*`\- methoden. Abonneer je voor UI-integraties op Gateway-gebeurtenissen en render alleen de gebeurtenisfamilies die je app begrijpt.

## App-code versus Plugin-code

Gebruik Gateway RPC wanneer code buiten OpenClaw leeft:

  * Node-scripts die agent-runs starten of observeren
  * CI-taken die een Gateway aanroepen
  * dashboards en beheerderspanelen
  * IDE-extensies
  * externe bridges die geen kanaalplugins hoeven te worden
  * integratietests met nep- of echte Gateway-transporten


Gebruik de Plugin SDK wanneer code binnen OpenClaw draait:

  * providerplugins
  * kanaalplugins
  * tool- of lifecycle-hooks
  * agent-harnessplugins
  * vertrouwde runtimehelpers


Externe apps moeten `openclaw/plugin-sdk/*` niet importeren; die subpaden zijn voor plugins die door OpenClaw worden geladen.

## Gerelateerd

  * [Gateway-protocol](</nl/gateway/protocol>)
  * [Gateway RPC-referentie](</nl/reference/rpc>)
  * [CLI-agentopdracht](</nl/cli/agent>)
  * [CLI-berichtopdracht](</nl/cli/message>)
  * [Agent-loop](</nl/concepts/agent-loop>)
  * [Agent-runtimes](</nl/concepts/agent-runtimes>)
  * [Sessies](</nl/concepts/session>)
  * [Achtergrondtaken](</nl/automation/tasks>)
  * [ACP-agents](</nl/tools/acp-agents>)
  * [Plugin SDK-overzicht](</nl/plugins/sdk-overview>)


Was this useful?YesNo

Open issue
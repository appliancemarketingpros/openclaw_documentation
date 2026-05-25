---
title: Spraakactivering
source_url: https://docs.openclaw.ai/nl/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw behandelt **wekwoorden als één globale lijst** die eigendom is van de **Gateway**.

  * Er zijn **geen aangepaste wekwoorden per node**.
  * **Elke node-/app-UI kan** de lijst bewerken; wijzigingen worden door de Gateway opgeslagen en naar iedereen uitgezonden.
  * macOS en iOS behouden lokale schakelaars voor **spraakactivering ingeschakeld/uitgeschakeld** (lokale UX en machtigingen verschillen).
  * Android houdt spraakactivering momenteel uitgeschakeld en gebruikt een handmatige microfoonflow in het tabblad Spraak.


## Opslag (Gateway-host)

Wekwoorden worden op de gatewaymachine opgeslagen op:

  * `~/.openclaw/settings/voicewake.json`


Vorm:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## Protocol

### Methoden

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` met params `{ triggers: string[] }` → `{ triggers: string[] }`


Opmerkingen:

  * Triggers worden genormaliseerd (bijgesneden, lege waarden verwijderd). Lege lijsten vallen terug op standaardwaarden.
  * Limieten worden afgedwongen voor veiligheid (limieten voor aantal/lengte).


### Routeringsmethoden (trigger → doel)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` met params `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


Vorm van `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Routedoelen ondersteunen exact één van:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### Gebeurtenissen

  * `voicewake.changed` payload `{ triggers: string[] }`
  * `voicewake.routing.changed` payload `{ config: VoiceWakeRoutingConfig }`


Wie dit ontvangt:

  * Alle WebSocket-clients (macOS-app, WebChat, enz.)
  * Alle verbonden nodes (iOS/Android), en ook bij het verbinden van een node als een initiële push met de "huidige status".


## Clientgedrag

### macOS-app

  * Gebruikt de globale lijst om `VoiceWakeRuntime`-triggers te gate'en.
  * Het bewerken van "Triggerwoorden" in de instellingen voor spraakactivering roept `voicewake.set` aan en vertrouwt vervolgens op de broadcast om andere clients gesynchroniseerd te houden.


### iOS-node

  * Gebruikt de globale lijst voor triggerdetectie door `VoiceWakeManager`.
  * Het bewerken van wekwoorden in Instellingen roept `voicewake.set` aan (via de Gateway-WS) en houdt lokale wekwoorddetectie ook responsief.


### Android-node

  * Spraakactivering is momenteel uitgeschakeld in de Android-runtime/-instellingen.
  * Android-spraak gebruikt handmatige microfoonopname in het tabblad Spraak in plaats van wekwoordtriggers.


## Gerelateerd

  * [Praatmodus](</nl/nodes/talk>)
  * [Audio en spraaknotities](</nl/nodes/audio>)
  * [Mediabegrip](</nl/nodes/media-understanding>)


Was this useful?YesNo
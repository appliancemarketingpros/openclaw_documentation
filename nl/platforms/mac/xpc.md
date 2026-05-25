---
title: macOS IPC
source_url: https://docs.openclaw.ai/nl/platforms/mac/xpc
scraped_at: 2026-05-25
---

# OpenClaw macOS IPC-architectuur

**Huidig model:** een lokale Unix-socket verbindt de **node-hostservice** met de **macOS-app** voor exec-goedkeuringen + `system.run`. Er bestaat een `openclaw-mac` debug-CLI voor ontdekking/verbindingscontroles; agentacties lopen nog steeds via de Gateway WebSocket en `node.invoke`. UI-automatisering gebruikt PeekabooBridge.

## Doelen

  * Eén GUI-appinstantie die eigenaar is van al het TCC-gerichte werk (meldingen, schermopname, microfoon, spraak, AppleScript).
  * Een klein oppervlak voor automatisering: Gateway + node-opdrachten, plus PeekabooBridge voor UI-automatisering.
  * Voorspelbare rechten: altijd dezelfde ondertekende bundel-ID, gestart door launchd, zodat TCC-toekenningen behouden blijven.


## Hoe het werkt

### Gateway + node-transport

  * De app draait de Gateway (lokale modus) en verbindt ermee als een node.
  * Agentacties worden uitgevoerd via `node.invoke` (bijv. `system.run`, `system.notify`, `canvas.*`).


### Node-service + app-IPC

  * Een headless node-hostservice maakt verbinding met de Gateway WebSocket.
  * `system.run`-verzoeken worden via een lokale Unix-socket doorgestuurd naar de macOS-app.
  * De app voert de exec uit in UI-context, vraagt indien nodig om bevestiging en retourneert uitvoer.


Diagram (SCI):

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge (UI-automatisering)

  * UI-automatisering gebruikt een aparte UNIX-socket met de naam `bridge.sock` en het PeekabooBridge JSON-protocol.
  * Voorkeursvolgorde voor hosts (clientzijde): Peekaboo.app → Claude.app → OpenClaw.app → lokale uitvoering.
  * Beveiliging: bridge-hosts vereisen een toegestane TeamID; DEBUG-only same-UID-uitweg wordt bewaakt door `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (Peekaboo-conventie).
  * Zie: [PeekabooBridge-gebruik](</nl/platforms/mac/peekaboo>) voor details.


## Operationele stromen

  * Herstarten/opnieuw bouwen: `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * Beëindigt bestaande instanties
    * Swift-build + pakket
    * Schrijft/bootstrap/kickstart de LaunchAgent
  * Enkele instantie: de app sluit vroegtijdig af als er al een andere instantie met dezelfde bundel-ID draait.


## Hardening-notities

  * Vereis bij voorkeur een TeamID-match voor alle geprivilegieerde oppervlakken.
  * PeekabooBridge: `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (DEBUG-only) kan same-UID-aanroepers toestaan voor lokale ontwikkeling.
  * Alle communicatie blijft alleen lokaal; er worden geen netwerksockets blootgesteld.
  * TCC-prompts zijn alleen afkomstig van de GUI-appbundel; houd de ondertekende bundel-ID stabiel tussen rebuilds.
  * IPC-hardening: socketmodus `0600`, token, peer-UID-controles, HMAC-challenge/response, korte TTL.


## Gerelateerd

  * [macOS-app](</nl/platforms/macos>)
  * [macOS IPC-stroom (exec-goedkeuringen)](</nl/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo
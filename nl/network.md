---
title: Netwerk
source_url: https://docs.openclaw.ai/nl/network
scraped_at: 2026-05-25
---

Deze hub koppelt de kerndocumentatie voor hoe OpenClaw apparaten verbindt, koppelt en beveiligt via localhost, LAN en tailnet.

## Kernmodel

De meeste bewerkingen verlopen via de Gateway (`openclaw gateway`), één langlopend proces dat kanaalverbindingen en de WebSocket-besturingslaag beheert.

  * **Loopback eerst** : de Gateway WS gebruikt standaard `ws://127.0.0.1:18789`. Niet-loopback-binds vereisen een geldig gateway-authenticatiepad: shared-secret token-/wachtwoordauthenticatie, of een correct geconfigureerde niet-loopback `trusted-proxy`-implementatie.
  * **Eén Gateway per host** wordt aanbevolen. Voor isolatie voer je meerdere gateways uit met geïsoleerde profielen en poorten ([Meerdere Gateways](</nl/gateway/multiple-gateways>)).
  * **Canvas-host** wordt aangeboden op dezelfde poort als de Gateway (`/__openclaw__/canvas/`, `/__openclaw__/a2ui/`), beschermd door Gateway-authenticatie wanneer deze buiten loopback wordt gebonden.
  * **Externe toegang** is meestal een SSH-tunnel of Tailscale VPN ([Externe toegang](</nl/gateway/remote>)).


Belangrijke referenties:

  * [Gateway-architectuur](</nl/concepts/architecture>)
  * [Gateway-protocol](</nl/gateway/protocol>)
  * [Gateway-runbook](</nl/gateway>)
  * [Weboppervlakken + bindmodi](</nl/web>)


## Koppeling + identiteit

  * [Overzicht van koppeling (DM + Nodes)](</nl/channels/pairing>)
  * [Door Gateway beheerde Node-koppeling](</nl/gateway/pairing>)
  * [Apparaten-CLI (koppeling + tokenrotatie)](</nl/cli/devices>)
  * [Koppelings-CLI (DM-goedkeuringen)](</nl/cli/pairing>)


Lokaal vertrouwen:

  * Rechtstreekse local loopback-verbindingen kunnen automatisch worden goedgekeurd voor koppeling om de gebruikerservaring op dezelfde host soepel te houden.
  * OpenClaw heeft ook een smal backend-/container-lokaal zelfverbindingspad voor vertrouwde shared-secret-helperflows.
  * Tailnet- en LAN-clients, inclusief tailnet-binds op dezelfde host, vereisen nog steeds expliciete goedkeuring voor koppeling.


## Detectie + transporten

  * [Detectie en transporten](</nl/gateway/discovery>)
  * [Bonjour / mDNS](</nl/gateway/bonjour>)
  * [Externe toegang (SSH)](</nl/gateway/remote>)
  * [Tailscale](</nl/gateway/tailscale>)


## Nodes + transporten

  * [Overzicht van Nodes](</nl/nodes>)
  * [Bridge-protocol (legacy Nodes, historisch)](</nl/gateway/bridge-protocol>)
  * [Node-runbook: iOS](</nl/platforms/ios>)
  * [Node-runbook: Android](</nl/platforms/android>)


## Beveiliging

  * [Beveiligingsoverzicht](</nl/gateway/security>)
  * [Gateway-configuratiereferentie](</nl/gateway/configuration>)
  * [Probleemoplossing](</nl/gateway/troubleshooting>)
  * [Doctor](</nl/gateway/doctor>)


## Gerelateerd

  * [Gateway-runbook](</nl/gateway>)
  * [Externe toegang](</nl/gateway/remote>)


Was this useful?YesNo
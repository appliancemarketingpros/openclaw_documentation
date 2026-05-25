---
title: Brugprotocol
source_url: https://docs.openclaw.ai/nl/gateway/bridge-protocol
scraped_at: 2026-05-25
---

## Waarom het bestond

  * **Beveiligingsgrens** : de bridge stelt een kleine allowlist beschikbaar in plaats van het volledige gateway-API-oppervlak.
  * **Koppeling + node-identiteit** : toelating van nodes is eigendom van de Gateway en gekoppeld aan een token per node.
  * **Discovery-UX** : nodes kunnen gateways ontdekken via Bonjour op LAN, of rechtstreeks verbinden via een tailnet.
  * **Loopback-WS** : het volledige WS-besturingsvlak blijft lokaal tenzij het via SSH wordt getunneld.


## Transport

  * TCP, één JSON-object per regel (JSONL).
  * Optionele TLS (wanneer `bridge.tls.enabled` true is).
  * De historische standaardlistenerpoort was `18790` (huidige builds starten geen TCP-bridge).


Wanneer TLS is ingeschakeld, bevatten discovery-TXT-records `bridgeTls=1` plus `bridgeTlsSha256` als niet-geheim aanknopingspunt. Let erop dat Bonjour/mDNS-TXT-records niet geauthenticeerd zijn; clients mogen de geadverteerde fingerprint niet behandelen als een gezaghebbende pin zonder expliciete gebruikersintentie of andere out-of-band-verificatie.

## Handshake + koppeling

  1. Client verzendt `hello` met nodemetadata + token (als deze al gekoppeld is).
  2. Als deze niet gekoppeld is, antwoordt de Gateway met `error` (`NOT_PAIRED`/`UNAUTHORIZED`).
  3. Client verzendt `pair-request`.
  4. Gateway wacht op goedkeuring en verzendt daarna `pair-ok` en `hello-ok`.


Historisch retourneerde `hello-ok` `serverName`; gehoste Plugin-oppervlakken worden nu geadverteerd via `pluginSurfaceUrls`. Canvas/A2UI gebruikt `pluginSurfaceUrls.canvas`; de verouderde alias `canvasHostUrl` maakt geen deel uit van het gerefactorde protocol.

## Frames

Client → Gateway:

  * `req` / `res`: scoped Gateway-RPC (chat, sessions, config, health, voicewake, skills.bins)
  * `event`: nodesignalen (spraaktranscript, agentaanvraag, chatabonnement, exec-levenscyclus)


Gateway → Client:

  * `invoke` / `invoke-res`: node-opdrachten (`canvas.*`, `camera.*`, `screen.record`, `location.get`, `sms.send`)
  * `event`: chatupdates voor geabonneerde sessies
  * `ping` / `pong`: keepalive


Legacy-allowlistafdwinging stond in `src/gateway/server-bridge.ts` (verwijderd).

## Exec-levenscyclusgebeurtenissen

Nodes kunnen `exec.finished`\- of `exec.denied`-gebeurtenissen uitzenden om system.run-activiteit zichtbaar te maken. Deze worden in de Gateway naar systeemgebeurtenissen gemapt. (Legacy-nodes kunnen nog steeds `exec.started` uitzenden.)

Payloadvelden (allemaal optioneel tenzij vermeld):

  * `sessionKey` (vereist): agentsessie die de systeemgebeurtenis moet ontvangen.
  * `runId`: unieke exec-id voor groepering.
  * `command`: ruwe of geformatteerde opdrachtreeks.
  * `exitCode`, `timedOut`, `success`, `output`: voltooiingsdetails (alleen finished).
  * `reason`: reden voor weigering (alleen denied).


## Historisch tailnet-gebruik

  * Bind de bridge aan een tailnet-IP: `bridge.bind: "tailnet"` in `~/.openclaw/openclaw.json` (alleen historisch; `bridge.*` is niet langer geldig).
  * Clients verbinden via MagicDNS-naam of tailnet-IP.
  * Bonjour werkt **niet** over netwerken heen; gebruik indien nodig handmatige host/poort of wide-area DNS-SD.


## Versiebeheer

De bridge was **impliciet v1** (geen min/max-onderhandeling). Deze sectie is alleen historische referentie; huidige node/operator-clients gebruiken het WebSocket- [Gateway-protocol](</nl/gateway/protocol>).

## Gerelateerd

  * [Gateway-protocol](</nl/gateway/protocol>)
  * [Nodes](</nl/nodes>)


Was this useful?YesNo
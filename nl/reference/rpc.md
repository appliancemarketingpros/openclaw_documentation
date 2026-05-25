---
title: RPC-adapters
source_url: https://docs.openclaw.ai/nl/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw integreert externe CLI's via JSON-RPC. Vandaag worden twee patronen gebruikt.

## Patroon A: HTTP-daemon (signal-cli)

  * `signal-cli` draait als daemon met JSON-RPC via HTTP.
  * De gebeurtenisstroom is SSE (`/api/v1/events`).
  * Gezondheidscontrole: `/api/v1/check`.
  * OpenClaw beheert de levenscyclus wanneer `channels.signal.autoStart=true`.


Zie [Signal](</nl/channels/signal>) voor installatie en eindpunten.

## Patroon B: stdio-kindproces (imsg)

  * OpenClaw start `imsg rpc` als kindproces voor [iMessage](</nl/channels/imessage>).
  * JSON-RPC is regelgescheiden via stdin/stdout (één JSON-object per regel).
  * Geen TCP-poort, geen daemon vereist.


Gebruikte kernmethoden:

  * `watch.subscribe` → meldingen (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (probe/diagnostiek)


Zie [iMessage](</nl/channels/imessage>) voor legacy-installatie en adressering (`chat_id` heeft de voorkeur).

## Adapterrichtlijnen

  * Gateway beheert het proces (start/stop gekoppeld aan de levenscyclus van de provider).
  * Houd RPC-clients robuust: time-outs, herstarten bij afsluiten.
  * Geef de voorkeur aan stabiele ID's (bijv. `chat_id`) boven weergaveteksten.


## Gerelateerd

  * [Gateway-protocol](</nl/gateway/protocol>)


Was this useful?YesNo
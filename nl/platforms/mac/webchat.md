---
title: Webchat (macOS)
source_url: https://docs.openclaw.ai/nl/platforms/mac/webchat
scraped_at: 2026-05-25
---

De macOS-menubalk-app sluit de WebChat-UI in als een native SwiftUI-weergave. Deze maakt verbinding met de Gateway en gebruikt standaard de **hoofdsessie** voor de geselecteerde agent (met een sessiewisselaar voor andere sessies).

  * **Lokale modus** : maakt rechtstreeks verbinding met de lokale Gateway-WebSocket.
  * **Externe modus** : stuurt de Gateway-besturingspoort door via SSH en gebruikt die tunnel als het datavlak.


## Starten en debuggen

  * Handmatig: Lobster-menu → "Chat openen".

  * Automatisch openen voor tests:

bashCopy code
[code]dist/OpenClaw.app/Contents/MacOS/OpenClaw --webchat
[/code]

  * Logboeken: `./scripts/clawlog.sh` (subsysteem `ai.openclaw`, categorie `WebChatSwiftUI`).


## Hoe het is gekoppeld

  * Datavlak: Gateway-WS-methoden `chat.history`, `chat.send`, `chat.abort`, `chat.inject` en events `chat`, `agent`, `presence`, `tick`, `health`.
  * `chat.history` retourneert voor weergave genormaliseerde transcriptieregels: inline directive tags worden uit zichtbare tekst gestript, XML-payloads van toolaanroepen in platte tekst (waaronder `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>`, en afgekorte toolaanroepblokken) en gelekte ASCII-/volledige-breedte-modelbesturingstokens worden gestript, zuivere assistant-regels met stille tokens, zoals exact `NO_REPLY` / `no_reply`, worden weggelaten, en te grote regels kunnen worden vervangen door placeholders.
  * Sessie: gebruikt standaard de primaire sessie (`main`, of `global` wanneer het bereik globaal is). De UI kan wisselen tussen sessies.
  * Onboarding gebruikt een toegewezen sessie om de eerste installatie gescheiden te houden.


## Beveiligingsoppervlak

  * Externe modus stuurt alleen de Gateway-WebSocket-besturingspoort door via SSH.


## Bekende beperkingen

  * De UI is geoptimaliseerd voor chatsessies (geen volledige browsersandbox).


## Gerelateerd

  * [WebChat](</nl/web/webchat>)
  * [macOS-app](</nl/platforms/macos>)


Was this useful?YesNo
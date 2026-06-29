---
title: Raft
source_url: https://docs.openclaw.ai/nl/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Raft-ondersteuning verbindt een OpenClaw-agent met een Raft Externe Agent via de lokale Raft CLI. Raft stuurt geauthenticeerde wake-hints naar de Gateway. De agent gebruikt daarna de Raft CLI om berichten te controleren en te verzenden.

## Installeren

Raft is een officiële externe Plugin. Installeer deze op de Gateway-host:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Details: [Plugins](</nl/tools/plugin>)

## Vereisten

  * Een Raft-werkruimte met een Externe Agent.
  * De Raft CLI geïnstalleerd op dezelfde host als de OpenClaw Gateway.
  * Een Raft CLI-profiel dat al is aangemeld en gekoppeld is aan die Externe Agent.


De Plugin slaat geen Raft-referenties op. De Raft CLI bewaart die authenticatie in zijn eigen profiel.

## Configureren

Stel het profiel in de configuratie in:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Voor het standaardaccount kun je in plaats daarvan `RAFT_PROFILE` instellen in de Gateway- omgeving:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Gebruik een benoemd account wanneer één Gateway verbinding maakt met meer dan één Raft Externe Agent:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

De interactieve setup-flow registreert hetzelfde profiel:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Hoe Het Werkt

Wanneer de Gateway start, doet de Plugin het volgende:

  1. Opent een HTTP-wake-eindpunt dat alleen via loopback bereikbaar is op een efemere poort.
  2. Start `raft --profile <profile> agent bridge` met dat eindpunt en een procesgebonden token.
  3. Accepteert alleen geauthenticeerde, inhoudsloze wake-hints met een replay-identiteit van de lokale bridge.
  4. Vereist één van `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` of `id`.
  5. Dedupliceert recente opnieuw geprobeerde wake-leveringen op bridge-gebeurtenis-id, ook over Gateway-herstarts heen.
  6. Retourneert een stabiele runtimesessie voor de huidige bridge en een lege activity-drain-batch voor het Raft CLI-protocol.
  7. Start één geserialiseerde OpenClaw-agentbeurt voor elke geaccepteerde wake.


De bridge beheert Raft-leveringspogingen en herverbindingen. De OpenClaw-beurt ontvangt alleen een wake-melding, geen gekopieerde Raft-berichtinhoud. Hij gebruikt de CLI om openstaande berichten te lezen en zijn reactie te verzenden:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Verifiëren

Controleer of OpenClaw de CLI kan vinden en een geconfigureerd profiel heeft:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Stuur daarna een bericht naar de Raft Externe Agent. Het Gateway-logboek zou moeten tonen dat de Raft-bridge start, gevolgd door een inkomende wake. De agent zou het geconfigureerde Raft-profiel moeten gebruiken om zijn openstaande berichten te controleren.

## Probleemoplossing

Raft CLI ontbreekt

Installeer de Raft CLI op de Gateway-host en maak `raft` beschikbaar op het `PATH` van de service. Verifieer dit met `raft --help` en herstart daarna de Gateway.

De bridge sluit onmiddellijk af

Controleer of het geconfigureerde profiel is aangemeld en hoort bij de beoogde Raft Externe Agent. Voer `raft --profile <profile> agent bridge` rechtstreeks uit om de CLI-diagnose te zien.

Er komt een wake binnen, maar er wordt geen Raft-reactie verzonden

Dit is verwacht wanneer de agent de Raft CLI niet aanroept. De wake- bridge bevat geen berichtinhoud of automatische definitieve antwoorden. Controleer het toolbeleid van de agent en zorg dat deze `raft --profile <profile> message check` en `message send` kan uitvoeren.

## Referenties

  * [Raft](<https://raft.build/>)
  * [Raft-documentatie](<https://docs.raft.build/welcome/>)
  * [Hermes Raft-integratie](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue
---
title: QA-kanaal
source_url: https://docs.openclaw.ai/nl/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` is een gebundeld synthetisch berichttransport voor geautomatiseerde OpenClaw-QA. Het is geen productiekanaal - het bestaat om dezelfde kanaal-Plugin-grens te testen die echte transporten gebruiken, terwijl de status deterministisch en volledig inspecteerbaar blijft.

## Wat het doet

  * Doelgrammatica van Slack-klasse: 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * Gedeelde `channel:`\- en `group:`-gesprekken worden aan agents aangeboden als groeps-/kanaalkamerbeurten, zodat ze hetzelfde zichtbare-antwoord- en berichttoolrouteringsbeleid testen dat wordt gebruikt door Discord, Slack, Telegram en vergelijkbare transporten.
  * Door HTTP ondersteunde synthetische bus voor injectie van inkomende berichten, vastlegging van uitgaande transcripties, threadaanmaak, reacties, bewerkingen, verwijderingen en zoek-/leesacties.
  * Zelfcontrolerunner aan hostzijde die een Markdown-rapport schrijft naar `.artifacts/qa-e2e/`.


## Configuratie

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

Accountsleutels:

  * `enabled` \- hoofdschakelaar voor dit account.
  * `name` \- optioneel weergavelabel.
  * `baseUrl` \- URL van de synthetische bus.
  * `botUserId` \- botgebruikers-id in Matrix-stijl die wordt gebruikt in de doelgrammatica.
  * `botDisplayName` \- weergavenaam voor uitgaande berichten.
  * `pollTimeoutMs` \- wachttijdvenster voor long-polling. Geheel getal tussen 100 en 30000.
  * `allowFrom` \- afzender-allowlist (gebruikers-id's of `"*"`). Directe berichten en allowlisted groepsbeleid gebruiken beide deze synthetische afzender-id's.
  * `groupPolicy` \- beleid voor gedeelde kamers: `"open"` (standaard), `"allowlist"` of `"disabled"`.
  * `groupAllowFrom` \- optionele afzender-allowlist voor gedeelde kamers. Wanneer dit wordt weggelaten onder `"allowlist"`, valt QA Channel terug op `allowFrom`.
  * `groups.<room>.requireMention` \- vereist een botvermelding voordat er wordt geantwoord in een specifieke groeps-/kanaalkamer. `groups."*"` stelt de standaard in.
  * `defaultTo` \- fallbackdoel wanneer er geen doel is opgegeven.
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads` \- tooltoegang per actie.


Sleutels voor meerdere accounts op het hoogste niveau:

  * `accounts` \- record met benoemde overrides per account, gesleuteld op account-id.
  * `defaultAccount` \- voorkeursaccount-id wanneer er meerdere zijn geconfigureerd.


## Runners

Zelfcontrole aan hostzijde (schrijft een Markdown-rapport onder `.artifacts/qa-e2e/`):

bashCopy code
[code]
    pnpm qa:e2e
[/code]

Dit loopt via `qa-lab`, start de QA-bus in de repo, start de gebundelde `qa-channel`-runtime-slice en voert een deterministische zelfcontrole uit.

Volledige scenarioreeks op basis van de repo:

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

Voert scenario's parallel uit tegen de QA Gateway-lane. Zie [QA-overzicht](</nl/concepts/qa-e2e-automation>) voor scenario's, profielen en providermodi.

Door Docker ondersteunde QA-site (Gateway + QA Lab-debugger-UI in één stack):

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

Bouwt de QA-site, start de door Docker ondersteunde Gateway + QA Lab-stack en drukt de QA Lab-URL af. Van daaruit kun je scenario's kiezen, de modellane selecteren, afzonderlijke runs starten en resultaten live bekijken. De QA Lab-debugger staat los van de meegeleverde Control UI-bundel.

## Gerelateerd

  * [QA-overzicht](</nl/concepts/qa-e2e-automation>) \- volledige stack, transportadapters, scenarioauteurschap
  * [Matrix QA](</nl/concepts/qa-matrix>) \- voorbeeld van een live-transportrunner die een echt kanaal aanstuurt
  * [Koppelen](</nl/channels/pairing>)
  * [Groepen](</nl/channels/groups>)
  * [Kanalenoverzicht](</nl/channels>)


Was this useful?YesNo
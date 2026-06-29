---
title: Conventies voor geheime placeholders
source_url: https://docs.openclaw.ai/nl/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Conventies voor tijdelijke aanduidingen voor geheimen

Gebruik tijdelijke aanduidingen die menselijk leesbaar zijn, maar niet lijken op echte geheimen.

## Aanbevolen stijl

  * Geef de voorkeur aan beschrijvende waarden zoals `example-openai-key-not-real` of `example-discord-bot-token`.
  * Geef voor shellfragmenten de voorkeur aan `${OPENAI_API_KEY}` boven inline tekenreeksen die op tokens lijken.
  * Houd voorbeelden duidelijk nep en beperkt tot hun doel (provider, kanaal, auth-type).


## Vermijd deze patronen in docs

  * Letterlijke header- of footertekst van een PEM-privésleutel.
  * Voorvoegsels die lijken op live-inloggegevens, bijvoorbeeld `sk-...`, `xoxb-...`, `AKIA...`.
  * Bearer-tokens met een realistische uitstraling die uit runtimelogboeken zijn gekopieerd.


## Voorbeeld

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue
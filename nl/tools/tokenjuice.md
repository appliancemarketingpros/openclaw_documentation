---
title: Tokenbudget
source_url: https://docs.openclaw.ai/nl/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` is een optionele gebundelde Plugin die ruisrijke `exec`\- en `bash`-toolresultaten comprimeert nadat de opdracht al is uitgevoerd.

Het wijzigt het geretourneerde `tool_result`, niet de opdracht zelf. Tokenjuice herschrijft geen shellinvoer, voert opdrachten niet opnieuw uit en wijzigt geen exitcodes.

Vandaag geldt dit voor ingebedde PI-uitvoeringen en dynamische OpenClaw-tools in de Codex app-server-harness. Tokenjuice koppelt in op OpenClaw's middleware voor toolresultaten en trimt de uitvoer voordat die teruggaat naar de actieve harness-sessie.

## De Plugin inschakelen

Snelste manier:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Equivalent:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw levert de Plugin al mee. Er is geen aparte stap `plugins install` of `tokenjuice install openclaw`.

Als je de configuratie liever direct bewerkt:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Wat tokenjuice wijzigt

  * Comprimeert ruisrijke `exec`\- en `bash`-resultaten voordat ze terug de sessie in worden gevoerd.
  * Laat de oorspronkelijke opdrachtuitvoering ongemoeid.
  * Behoudt exacte leesacties van bestandsinhoud en andere opdrachten die tokenjuice onbewerkt moet laten.
  * Blijft opt-in: schakel de Plugin uit als je overal letterlijke uitvoer wilt.


## Verifiëren dat het werkt

  1. Schakel de Plugin in.
  2. Start een sessie die `exec` kan aanroepen.
  3. Voer een ruisrijke opdracht uit, zoals `git status`.
  4. Controleer of het geretourneerde toolresultaat korter en beter gestructureerd is dan de ruwe shelluitvoer.


## De Plugin uitschakelen

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Of:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Gerelateerd

  * [Exec-tool](</nl/tools/exec>)
  * [Denkniveaus](</nl/tools/thinking>)
  * [Context-engine](</nl/concepts/context-engine>)


Was this useful?YesNo
---
title: Trajectbundels
source_url: https://docs.openclaw.ai/nl/tools/trajectory
scraped_at: 2026-05-25
---

Trajectorie-opname is OpenClaw's vluchtrecorder per sessie. Deze registreert een gestructureerde tijdlijn voor elke agentrun, waarna `/export-trajectory` de huidige sessie verpakt in een geredigeerde supportbundel.

Gebruik dit wanneer je vragen moet beantwoorden zoals:

  * Welke prompt, systeemprompt en tools zijn naar het model gestuurd?
  * Welke transcriptberichten en toolaanroepen hebben tot dit antwoord geleid?
  * Is de run verlopen, afgebroken, gecompacteerd of op een providerfout gestuit?
  * Welk model, welke plugins, Skills en runtime-instellingen waren actief?
  * Welke gebruiks- en promptcachemetadata heeft de provider teruggegeven?


Als je een breed supportrapport indient voor een live Gateway-probleem, begin dan met [`/diagnostics`](</nl/gateway/diagnostics#chat-command>). Diagnostiek verzamelt de gesaneerde Gateway-bundel en kan voor OpenAI Codex-harnesssessies na goedkeuring ook Codex-feedback naar OpenAI-servers sturen. Gebruik `/export-trajectory` wanneer je specifiek de gedetailleerde prompt-, tool- en transcripttijdlijn per sessie nodig hebt.

## Snel starten

Stuur dit in de actieve sessie:

textCopy code
[code]
    /export-trajectory
[/code]

Alias:

textCopy code
[code]
    /trajectory
[/code]

OpenClaw schrijft de bundel onder de werkruimte:

textCopy code
[code]
    .openclaw/trajectory-exports/openclaw-trajectory-<session>-<timestamp>/
[/code]

Je kunt een relatieve naam voor de uitvoermap kiezen:

textCopy code
[code]
    /export-trajectory bug-1234
[/code]

Het aangepaste pad wordt binnen `.openclaw/trajectory-exports/` opgelost. Absolute paden en `~`-paden worden geweigerd.

Trajectoriebundels kunnen prompts, modelberichten, toolschema's, toolresultaten, runtime-events en lokale paden bevatten. De chat-schuine-streepopdracht loopt daarom elke keer via exec-goedkeuring. Keur de export eenmalig goed wanneer je de bundel wilt maken; gebruik geen allow-all. In groepschats stuurt OpenClaw de goedkeuringsprompt en het exportresultaat privé naar de eigenaar in plaats van de trajectoriedetails terug naar de gedeelde ruimte te plaatsen.

Voor lokale inspectie of supportworkflows kun je het goedgekeurde opdrachtpad ook rechtstreeks uitvoeren:

bashCopy code
[code]
    openclaw sessions export-trajectory --session-key "agent:main:telegram:direct:123" --workspace .
[/code]

## Toegang

Trajectorie-export is een eigenaaropdracht. De afzender moet slagen voor de normale autorisatiecontroles voor opdrachten en de eigenaarcontroles voor het kanaal.

## Wat wordt opgenomen

Trajectorie-opname staat standaard aan voor OpenClaw-agentruns.

Runtime-events omvatten:

  * `session.started`
  * `trace.metadata`
  * `context.compiled`
  * `prompt.submitted`
  * `model.fallback_step`, inclusief het bronmodel, het volgende model, de foutreden/details, de ketenpositie en of fallback is doorgegaan, is geslaagd of de keten heeft uitgeput
  * `model.completed`
  * `trace.artifacts`
  * `session.ended`


Transcript-events worden ook gereconstrueerd vanuit de actieve sessietak:

  * gebruikersberichten
  * assistentberichten
  * toolaanroepen
  * toolresultaten
  * compactions
  * modelwijzigingen
  * labels en aangepaste sessie-items


Events worden geschreven als JSON Lines met deze schemamarkering:

jsonCopy code
[code]
    {  "traceSchema": "openclaw-trajectory",  "schemaVersion": 1}
[/code]

## Bundelbestanden

Een geëxporteerde bundel kan bevatten:

Bestand | Inhoud  
---|---  
`manifest.json` | Bundelschema, bronbestanden, eventaantallen en gegenereerde bestandslijst  
`events.jsonl` | Geordende runtime- en transcripttijdlijn  
`session-branch.json` | Geredigeerde actieve transcripttak en sessiekop  
`metadata.json` | OpenClaw-versie, OS/runtime, model, config-snapshot, plugins, Skills en promptmetadata  
`artifacts.json` | Eindstatus, fouten, gebruik, promptcache, compaction-aantal, assistenttekst en toolmetadata  
`prompts.json` | Ingediende prompts en geselecteerde details voor promptopbouw  
`system-prompt.txt` | Laatst gecompileerde systeemprompt, wanneer vastgelegd  
`tools.json` | Tooldefinities die naar het model zijn gestuurd, wanneer vastgelegd  
  
`manifest.json` vermeldt de bestanden die in die bundel aanwezig zijn. Sommige bestanden worden weggelaten wanneer de sessie de bijbehorende runtimedata niet heeft vastgelegd.

## Opnamelocatie

Standaard worden runtime-trajectorie-events naast het sessiebestand geschreven:

textCopy code
[code]
    <session>.trajectory.jsonl
[/code]

OpenClaw schrijft ook een best-effort pointerbestand naast de sessie:

textCopy code
[code]
    <session>.trajectory-path.json
[/code]

Stel `OPENCLAW_TRAJECTORY_DIR` in om runtime-trajectorie-sidecars in een specifieke map op te slaan:

bashCopy code
[code]
    export OPENCLAW_TRAJECTORY_DIR=/var/lib/openclaw/trajectories
[/code]

Wanneer deze variabele is ingesteld, schrijft OpenClaw één JSONL-bestand per sessie-id in die map.

Sessieonderhoud verwijdert trajectorie-sidecars wanneer hun bijbehorende sessie-item wordt opgeschoond, begrensd of verwijderd door het schijfbudget voor sessies. Runtimebestanden buiten de sessiemap worden alleen verwijderd wanneer het pointerdoel nog steeds bewijst dat het bij die sessie hoort.

## Opname uitschakelen

Stel `OPENCLAW_TRAJECTORY=0` in voordat je OpenClaw start:

bashCopy code
[code]
    export OPENCLAW_TRAJECTORY=0
[/code]

Dit schakelt runtime-trajectorie-opname uit. `/export-trajectory` kan nog steeds de transcripttak exporteren, maar runtime-only bestanden zoals gecompileerde context, providerartefacten en promptmetadata kunnen ontbreken.

## Privacy en limieten

Trajectoriebundels zijn bedoeld voor support en debugging, niet voor openbare publicatie. OpenClaw redigeert gevoelige waarden voordat exportbestanden worden geschreven:

  * inloggegevens en bekende geheim-achtige payloadvelden
  * afbeeldingsdata
  * lokale statuspaden
  * werkruimtepaden, vervangen door `$WORKSPACE_DIR`
  * homemap-paden, waar gedetecteerd


De exporter begrenst ook de invoergrootte:

  * runtime-sidecarbestanden: live opname stopt bij 10 MiB en registreert een truncatie-event wanneer er ruimte overblijft; export accepteert bestaande runtime-sidecars tot 50 MiB
  * sessiebestanden: 50 MiB
  * runtime-events: 200.000
  * totaal geëxporteerde events: 250.000
  * afzonderlijke runtime-eventregels worden boven 256 KiB afgekapt


Controleer bundels voordat je ze buiten je team deelt. Redactie is best-effort en kan niet elk toepassingsspecifiek geheim kennen.

## Problemen oplossen

Als de export geen runtime-events heeft:

  * bevestig dat OpenClaw is gestart zonder `OPENCLAW_TRAJECTORY=0`
  * controleer of `OPENCLAW_TRAJECTORY_DIR` naar een beschrijfbare map verwijst
  * voer nog een bericht uit in de sessie en exporteer daarna opnieuw
  * inspecteer `manifest.json` op `runtimeEventCount`


Als de opdracht het uitvoerpad weigert:

  * gebruik een relatieve naam zoals `bug-1234`
  * geef geen `/tmp/...` of `~/...` door
  * houd de export binnen `.openclaw/trajectory-exports/`


Als de export mislukt met een groottefout, heeft de sessie of sidecar de veiligheidslimieten voor export overschreden. Start een nieuwe sessie of exporteer een kleinere reproductie.

## Gerelateerd

  * [Diffs](</nl/tools/diffs>)
  * [Sessiebeheer](</nl/concepts/session>)
  * [Exec-tool](</nl/tools/exec>)


Was this useful?YesNo
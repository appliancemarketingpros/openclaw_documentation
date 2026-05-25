---
title: Cron
source_url: https://docs.openclaw.ai/nl/cli/cron
scraped_at: 2026-05-25
---

# `openclaw cron`

Beheer cron-taken voor de Gateway-planner.

## Sessies

`--session` accepteert `main`, `isolated`, `current` of `session:<id>`.

Sessiesleutels

  * `main` koppelt aan de hoofdsessie van de agent.
  * `isolated` maakt voor elke uitvoering een nieuw transcript en sessie-id.
  * `current` koppelt aan de actieve sessie op het moment van aanmaken.
  * `session:<id>` zet vast op een expliciete persistente sessiesleutel.

Semantiek van geïsoleerde sessies

Geïsoleerde uitvoeringen resetten de omgevingscontext van het gesprek. Kanaal- en groepsroutering, verzend-/wachtrijbeleid, elevatie, oorsprong en ACP-runtimebinding worden gereset voor de nieuwe uitvoering. Veilige voorkeuren en expliciete, door de gebruiker geselecteerde model- of auth-overschrijvingen kunnen worden meegenomen tussen uitvoeringen.

## Levering

`openclaw cron list` en `openclaw cron show <job-id>` tonen vooraf de opgeloste leveringsroute. Voor `channel: "last"` laat de preview zien of de route is opgelost vanuit de hoofd- of huidige sessie, of gesloten zal mislukken.

Doelen met providerprefix kunnen onopgeloste aankondigingskanalen ondubbelzinnig maken. Bijvoorbeeld: `to: "telegram:123"` selecteert Telegram wanneer `delivery.channel` is weggelaten of `last` is. Alleen prefixes die door de geladen plugin worden geadverteerd, zijn providerselectoren. Als `delivery.channel` expliciet is, moet de prefix overeenkomen met dat kanaal; `channel: "whatsapp"` met `to: "telegram:123"` wordt geweigerd. Serviceprefixes zoals `imessage:` en `sms:` blijven kanaaleigen doelsyntaxis.

### Eigenaarschap van levering

Chatlevering voor geïsoleerde Cron wordt gedeeld tussen de agent en de uitvoerder:

  * De agent kan rechtstreeks verzenden met de `message`-tool wanneer er een chatroute beschikbaar is.
  * `announce` levert de uiteindelijke reactie alleen als fallback wanneer de agent niet rechtstreeks naar het opgeloste doel heeft verzonden.
  * `webhook` plaatst de voltooide payload op een URL.
  * `none` schakelt fallbacklevering door de uitvoerder uit.


`--announce` is fallbacklevering door de uitvoerder voor de uiteindelijke reactie. `--no-deliver` schakelt die fallback uit, maar verwijdert de `message`-tool van de agent niet wanneer er een chatroute beschikbaar is.

Herinneringen die vanuit een actieve chat worden gemaakt, behouden het live chatleveringsdoel voor fallback-aankondigingslevering. Interne sessiesleutels kunnen kleine letters zijn; gebruik ze niet als bron van waarheid voor hoofdlettergevoelige provider-ID's zoals Matrix-ruimte-ID's.

### Levering bij fouten

Foutmeldingen worden in deze volgorde opgelost:

  1. `delivery.failureDestination` op de taak.
  2. Globale `cron.failureDestination`.
  3. Het primaire aankondigingsdoel van de taak (wanneer er geen expliciete foutbestemming is ingesteld).


Opmerking: geïsoleerde Cron-uitvoeringen behandelen uitvoeringsfouten op agentniveau als taakfouten, zelfs wanneer er geen antwoordpayload wordt geproduceerd, zodat model-/providerfouten nog steeds fouttellers verhogen en foutmeldingen activeren.

Als een geïsoleerde uitvoering een time-out krijgt vóór de eerste modelaanvraag, bevatten `openclaw cron show` en `openclaw cron runs` een fasespecifieke fout zoals `setup timed out before runner start` of `stalled before first model call (last phase: context-engine)`. Voor CLI-ondersteunde providers blijft de watchdog vóór het model actief totdat de externe CLI-beurt start, zodat vastlopers bij sessieopzoeking, hook, auth, prompt en CLI-installatie worden gerapporteerd als Cron-fouten vóór het model.

## Planning

### Eenmalige taken

`--at <datetime>` plant een eenmalige uitvoering. Datums en tijden zonder offset worden behandeld als UTC, tenzij je ook `--tz <iana>` meegeeft; dan wordt de wandkloktijd in de opgegeven tijdzone geïnterpreteerd.

### Terugkerende taken

Terugkerende taken gebruiken exponentiële retry-backoff na opeenvolgende fouten: 30s, 1m, 5m, 15m, 60m. De planning keert terug naar normaal na de volgende succesvolle uitvoering.

Overgeslagen uitvoeringen worden apart bijgehouden van uitvoeringsfouten. Ze beïnvloeden de retry-backoff niet, maar `openclaw cron edit <job-id> --failure-alert-include-skipped` kan foutmeldingen laten deelnemen aan herhaalde meldingen voor overgeslagen uitvoeringen.

Voor geïsoleerde taken die gericht zijn op een lokaal geconfigureerde modelprovider, voert Cron een lichte providerpreflight uit voordat de agentbeurt wordt gestart. Loopback-, privénetwerk- en `.local` `api: "ollama"`-providers worden geprobed op `/api/tags`; lokale OpenAI-compatibele providers zoals vLLM, SGLang en LM Studio worden geprobed op `/models`. Als het endpoint onbereikbaar is, wordt de uitvoering geregistreerd als `skipped` en later opnieuw geprobeerd volgens de planning; overeenkomende dode endpoints worden 5 minuten gecachet om te voorkomen dat veel taken dezelfde lokale server bestoken.

Opmerking: Cron-taakdefinities staan in `jobs.json`, terwijl de wachtende runtimestatus in `jobs-state.json` staat. Als `jobs.json` extern wordt bewerkt, laadt de Gateway gewijzigde planningen opnieuw en wist verouderde wachtende slots; herschrijvingen die alleen de opmaak wijzigen, wissen het wachtende slot niet.

### Handmatige uitvoeringen

`openclaw cron run` keert terug zodra de handmatige uitvoering in de wachtrij staat. Succesvolle reacties bevatten `{ ok: true, enqueued: true, runId }`. Gebruik `openclaw cron runs --id <job-id>` om de uiteindelijke uitkomst te volgen.

## Modellen

`cron add|edit --model <ref>` selecteert een toegestaan model voor de taak.

Cron `--model` is een **primaire taakinstelling** , geen `/model`-overschrijving voor een chatsessie. Dat betekent:

  * Geconfigureerde model-fallbacks blijven gelden wanneer het geselecteerde taakmodel mislukt.
  * Per-taak-payload `fallbacks` vervangt de geconfigureerde fallbacklijst wanneer aanwezig.
  * Een lege fallbacklijst per taak (`fallbacks: []` in de taakpayload/API) maakt de Cron-uitvoering strikt.
  * Wanneer een taak `--model` heeft maar er geen fallbacklijst is geconfigureerd, geeft OpenClaw een expliciete lege fallbackoverschrijving door, zodat de primaire agent niet als verborgen retry-doel wordt toegevoegd.


### Modelprioriteit voor geïsoleerde Cron

Geïsoleerde Cron lost het actieve model in deze volgorde op:

  1. Gmail-hookoverschrijving.
  2. Per-taak `--model`.
  3. Opgeslagen modeloverschrijving voor de Cron-sessie (wanneer de gebruiker er een heeft geselecteerd).
  4. Agent- of standaard modelselectie.


### Snelle modus

De snelle modus van geïsoleerde Cron volgt de opgeloste live modelselectie. Modelconfiguratie `params.fastMode` is standaard van toepassing, maar een opgeslagen sessieoverschrijving `fastMode` wint nog steeds van configuratie.

### Retries bij live modelwissels

Als een geïsoleerde uitvoering `LiveSessionModelSwitchError` gooit, bewaart Cron de gewisselde provider en het model (en de gewisselde auth-profieloverschrijving wanneer aanwezig) voor de actieve uitvoering voordat opnieuw wordt geprobeerd. De buitenste retry-lus is begrensd op twee wisselretries na de eerste poging en breekt daarna af in plaats van eindeloos te blijven lopen.

## Uitvoer van uitvoeringen en weigeringen

### Onderdrukking van verouderde bevestigingen

Geïsoleerde Cron-beurten onderdrukken verouderde antwoorden die alleen uit een bevestiging bestaan. Als het eerste resultaat slechts een tussentijdse statusupdate is en er geen afgeleide subagent-uitvoering verantwoordelijk is voor het uiteindelijke antwoord, prompt Cron eenmaal opnieuw om het echte resultaat vóór levering.

### Onderdrukking van stille tokens

Als een geïsoleerde Cron-uitvoering alleen het stille token (`NO_REPLY` of `no_reply`) teruggeeft, onderdrukt Cron zowel directe uitgaande levering als het fallbackpad met samenvatting in de wachtrij, zodat er niets terug naar de chat wordt geplaatst.

### Gestructureerde weigeringen

Geïsoleerde Cron-uitvoeringen geven de voorkeur aan gestructureerde metadata voor uitvoeringsweigering uit de ingebedde uitvoering en vallen daarna terug op bekende weigeringsmarkeringen in de uiteindelijke uitvoer, zoals `SYSTEM_RUN_DENIED`, `INVALID_REQUEST` en zinnen voor weigering van goedkeuringsbinding.

`cron list` en uitvoeringsgeschiedenis tonen de weigeringsreden in plaats van een geblokkeerde opdracht als `ok` te rapporteren.

## Bewaring

Bewaring en opruiming worden in de configuratie geregeld:

  * `cron.sessionRetention` (standaard `24h`) ruimt voltooide geïsoleerde uitvoeringssessies op.
  * `cron.runLog.maxBytes` en `cron.runLog.keepLines` ruimen `~/.openclaw/cron/runs/<jobId>.jsonl` op.


## Oudere taken migreren

## Veelvoorkomende bewerkingen

Werk leveringsinstellingen bij zonder het bericht te wijzigen:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
[/code]

Schakel levering uit voor een geïsoleerde taak:

bashCopy code
[code]
    openclaw cron edit <job-id> --no-deliver
[/code]

Schakel lichte bootstrapcontext in voor een geïsoleerde taak:

bashCopy code
[code]
    openclaw cron edit <job-id> --light-context
[/code]

Kondig aan op een specifiek kanaal:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
[/code]

Kondig aan op een Telegram-forumtopic:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "-1001234567890" --thread-id 42
[/code]

Maak een geïsoleerde taak met lichte bootstrapcontext:

bashCopy code
[code]
    openclaw cron add \  --name "Lightweight morning brief" \  --cron "0 7 * * *" \  --session isolated \  --message "Summarize overnight updates." \  --light-context \  --no-deliver
[/code]

`--light-context` is alleen van toepassing op geïsoleerde agentbeurttaken. Voor Cron-uitvoeringen houdt de lichte modus de bootstrapcontext leeg in plaats van de volledige bootstrapset van de werkruimte te injecteren.

## Veelvoorkomende beheerdersopdrachten

Handmatige uitvoering en inspectie:

bashCopy code
[code]
    openclaw cron listopenclaw cron list --agent opsopenclaw cron get <job-id>openclaw cron show <job-id>openclaw cron run <job-id>openclaw cron run <job-id> --dueopenclaw cron runs --id <job-id> --limit 50
[/code]

`openclaw cron list` toont standaard alle overeenkomende taken. Geef `--agent <id>` mee om alleen taken te tonen waarvan de effectieve genormaliseerde agent-id overeenkomt; taken zonder opgeslagen agent-id tellen als de geconfigureerde standaardagent.

`openclaw cron get <job-id>` geeft de opgeslagen taak-JSON rechtstreeks terug. Gebruik `cron show <job-id>` wanneer je de menselijk leesbare weergave met preview van de leveringsroute wilt.

`cron list --json` en `cron show <job-id> --json` bevatten een top-level `status`-veld op elke taak, berekend uit `enabled`, `state.runningAtMs` en `state.lastRunStatus`. Waarden: `disabled`, `running`, `ok`, `error`, `skipped` of `idle`. Dit weerspiegelt de menselijk leesbare statuskolom, zodat externe tooling de taakstatus kan lezen zonder die opnieuw af te leiden.

Vermeldingen van `cron runs` bevatten leveringsdiagnostiek met het beoogde Cron-doel, het opgeloste doel, verzendingen via message-tool, fallbackgebruik en geleverde status.

Agent- en sessieherroutering:

bashCopy code
[code]
    openclaw cron edit <job-id> --agent opsopenclaw cron edit <job-id> --clear-agentopenclaw cron edit <job-id> --session currentopenclaw cron edit <job-id> --session "session:daily-brief"
[/code]

`openclaw cron add` waarschuwt wanneer `--agent` wordt weggelaten bij agentbeurttaken en valt terug op de standaardagent (`main`). Geef `--agent <id>` mee bij het aanmaken om een specifieke agent vast te zetten.

Leveringsaanpassingen:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"openclaw cron edit <job-id> --best-effort-deliveropenclaw cron edit <job-id> --no-best-effort-deliveropenclaw cron edit <job-id> --no-deliver
[/code]

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Geplande taken](</nl/automation/cron-jobs>)


Was this useful?YesNo
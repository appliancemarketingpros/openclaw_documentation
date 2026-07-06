---
title: ClawRouter
source_url: https://docs.openclaw.ai/nl/providers/clawrouter
scraped_at: 2026-07-06
---

ModelsProviders

ClawRouter geeft OpenClaw één beleidsgebonden sleutel voor meerdere upstream modelproviders. De gebundelde Plugin ontdekt alleen de modellen die voor die sleutel zijn toegestaan, routeert elk model via het gedeclareerde protocol en rapporteert het budget van de sleutel en het geaggregeerde gebruik op de gebruiksoppervlakken van OpenClaw.

Je installeert of authenticeert niet elke upstream provider-Plugin op de OpenClaw-host. Upstream inloggegevens en providerspecifieke forwarding blijven in ClawRouter. OpenClaw heeft alleen de gebundelde `@openclaw/clawrouter`-Plugin nodig en een uitgegeven ClawRouter-inloggegeven.

Eigenschap | Waarde  
---|---  
Provider | `clawrouter`  
Pakket | `@openclaw/clawrouter`  
Authenticatie | `CLAWROUTER_API_KEY`  
Standaard-URL | `https://clawrouter.openclaw.ai`  
Modelcatalogus | Inloggegeven-gebonden via `/v1/catalog`  
Quota's | Maandelijks budget en gebruik via `/v1/usage`  
  
## Aan de slag

* ### Vraag een gebonden inloggegeven aan

Vraag je ClawRouter-beheerder om een inloggegeven waarvan het beleid de providers, modellen en het maandelijkse budget bevat die je moet gebruiken. Inloggegevens worden één keer getoond wanneer ze worden uitgegeven.

* ### Configureer OpenClaw

bashCopy code
[code]
    export CLAWROUTER_API_KEY="..."openclaw onboard --auth-choice clawrouter-api-keyopenclaw plugins enable clawrouter
[/code]

De Plugin is gebundeld met OpenClaw. Als je configuratie `plugins.allow` instelt, voeg dan `clawrouter` aan die lijst toe voordat je de Plugin inschakelt. Stel voor een aangepaste deployment `models.providers.clawrouter.baseUrl` in op de ClawRouter-origin; de standaardwaarde is `https://clawrouter.openclaw.ai`.

* ### Toegestane modellen weergeven

bashCopy code
[code]
    openclaw models list --all --provider clawrouter
[/code]

Gebruik de geretourneerde modelreferenties exact zoals weergegeven. Ze behouden de upstream namespace, zoals `clawrouter/openai/...`, `clawrouter/anthropic/...` of `clawrouter/google/...`. Als `agents.defaults.models` in je configuratie een allowlist is, voeg dan elke geselecteerde ClawRouter-referentie eraan toe.

* ### Selecteer een model

bashCopy code
[code]
    openclaw models set clawrouter/<provider>/<model>
[/code]

Je kunt ook een geretourneerd model voor één run selecteren met `openclaw agent --model clawrouter/<provider>/<model> --message "..."`.

## Modeldetectie

`GET /v1/catalog` is de bron van waarheid. OpenClaw levert geen tweede, vaste lijst met ClawRouter-modellen. Een model dat in ClawRouter is geconfigureerd verschijnt wanneer:

  * het beleid van het inloggegeven de provider toestaat;
  * de providerverbinding is ingeschakeld en gereed is;
  * het catalogusmodel een ondersteunde LLM-capability adverteert; en
  * de catalogus een transportcontract blootlegt dat door de Plugin wordt ondersteund.


Het toevoegen van een ander model aan een ondersteunde ClawRouter-provider vereist daarom geen OpenClaw-release of een andere provider-Plugin. De volgende catalogusverversing ontdekt het. Een model dat een nieuw wire-protocol nodig heeft, vereist ondersteuning in de ClawRouter-Plugin voordat OpenClaw het adverteert.

## Protocol en provider-Plugins

Je hoeft niet de authenticatie-Plugin van elk upstream bedrijf te installeren. ClawRouter beheert upstream inloggegevens; de catalogus vertelt OpenClaw welk transport moet worden gebruikt. De Plugin ondersteunt:

Catalogusroute | OpenClaw-transport  
---|---  
OpenAI-compatibele chat | `openai-completions`  
OpenAI-compatibele Responses | `openai-responses`  
Native Anthropic Messages | `anthropic-messages`  
Native Google Gemini-streaming | `google-generative-ai`  
  
De Plugin past ook het bijpassende replay- en tool-schemabeleid toe voor die families. Catalogusrijen die een ander request-/streamformaat gebruiken, worden opzettelijk niet geadverteerd als OpenClaw-tekstmodellen. Normaliseer die providers naar een van de ondersteunde contracten in ClawRouter in plaats van een incompatibele payload te verzenden.

## Quota's en gebruik

De `/v1/usage`-respons van ClawRouter voedt de normale gebruiksoppervlakken voor OpenClaw-providers. `/status` en gerelateerde dashboardstatus tonen het maandelijkse budgetvenster wanneer de sleutel een limiet heeft, plus totalen voor requests, tokens en uitgaven. Ongemeten sleutels tonen nog steeds geaggregeerd gebruik zonder percentagevenster.

Quota-opzoeking gebruikt dezelfde gebonden sleutel als modeldetectie. Een mislukte quota-opzoeking blokkeert de uitvoering van modellen niet.

Controleer de live momentopname met:

bashCopy code
[code]
    openclaw status --usageopenclaw models status
[/code]

Dezelfde providermomentopname is beschikbaar voor `/status` in chat en de gebruiks-UI van OpenClaw. Het budget geldt voor het hele beleid, dus requests van een andere client die hetzelfde ClawRouter-beleid gebruikt, kunnen het resterende percentage wijzigen.

## Probleemoplossing

Symptoom | Controle  
---|---  
Geen ClawRouter-modellen | Bevestig dat de Plugin is ingeschakeld en toegestaan door `plugins.allow`, en controleer daarna of het inloggegeven actief is en ten minste één gereedstaande provider toestaat.  
Een geconfigureerd ClawRouter-model ontbreekt | Inspecteer de `/v1/catalog`-capability en route-indeling ervan. Niet-ondersteunde transportcontracten worden opzettelijk gefilterd.  
`Unknown model: clawrouter/...` | Voeg de exacte catalogusreferentie toe aan `agents.defaults.models` wanneer die configuratiemap als allowlist wordt gebruikt.  
`401` of `403` van catalogus of gebruik | Geef het ClawRouter-inloggegeven opnieuw uit of pas de scope ervan aan; OpenClaw valt niet terug op upstream providersleutels.  
Modelaanroep mislukt na detectie | Controleer de providerverbinding en upstream gezondheid in ClawRouter, en probeer het opnieuw nadat de gereedheidsstatus is hersteld.  
Gebruik heeft totalen maar geen percentage | Het beleid is ongemeten; voeg een maandelijks budget toe in ClawRouter om een percentagevenster bloot te leggen.  
  
## Beveiligingsgedrag

  * Catalogusdetectie is gebonden aan de geconfigureerde proxysleutel en wordt per sleutel gecachet.
  * De proxysleutel wordt alleen toegevoegd bij request-dispatch; deze wordt niet opgeslagen in modelmetadata.
  * Native Anthropic- en Gemini-model-id's worden alleen bij dispatch herschreven naar hun upstream id's.
  * Niet-ondersteunde of niet-toegestane catalogusrijen falen gesloten en zijn niet selecteerbaar.


## Gerelateerd

[**Modelproviders** Providerconfiguratie en modelselectie. ](</nl/concepts/model-providers>) [**Gebruik bijhouden** OpenClaw-gebruik en statusoppervlakken. ](</nl/concepts/usage-tracking>)

Was this useful?YesNo

Open issue
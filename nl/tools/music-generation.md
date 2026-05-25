---
title: Muziekgeneratie
source_url: https://docs.openclaw.ai/nl/tools/music-generation
scraped_at: 2026-05-25
---

Met het hulpmiddel `music_generate` kan de agent muziek of audio maken via de gedeelde mogelijkheid voor muziekgeneratie met geconfigureerde providers: Google, MiniMax en workflow-geconfigureerde ComfyUI op dit moment.

Voor agentuitvoeringen met sessieondersteuning start OpenClaw muziekgeneratie als achtergrondtaak, houdt deze bij in het taaklogboek en wekt de agent vervolgens opnieuw wanneer de track klaar is, zodat de agent de gebruiker kan informeren en de voltooide audio kan toevoegen. In groeps-/kanaalchats die zichtbare levering alleen via het berichthulpmiddel gebruiken, stuurt de agent het resultaat door via het berichthulpmiddel. Als de voltooiingsagent alleen een privé-eindantwoord schrijft, valt OpenClaw terug op rechtstreeks verzenden via het kanaal met de gegenereerde media. De voltooiingswake waarschuwt de agent expliciet dat normale eindantwoorden privé zijn in die routes.

## Snel aan de slag

### Met gedeelde provider

* ### Authenticatie configureren

Stel een API-sleutel in voor ten minste één provider, bijvoorbeeld `GEMINI_API_KEY` of `MINIMAX_API_KEY`.

* ### Kies een standaardmodel (optioneel)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Vraag het de agent

_"Genereer een opgewekte synthpoptrack over een nachtelijke rit door een neonstad."_

De agent roept `music_generate` automatisch aan. Geen allow-listing voor hulpmiddelen nodig.

Voor directe synchrone contexten zonder agentuitvoering met sessieondersteuning valt het ingebouwde hulpmiddel nog steeds terug op inline generatie en retourneert het uiteindelijke mediapad in het hulpmiddelresultaat.

### ComfyUI-workflow

* ### Configureer de workflow

Configureer `plugins.entries.comfy.config.music` met een workflow-JSON en prompt-/uitvoerknooppunten.

* ### Cloudauthenticatie (optioneel)

Stel voor Comfy Cloud `COMFY_API_KEY` of `COMFY_CLOUD_API_KEY` in.

* ### Roep het hulpmiddel aan

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Voorbeeldprompts:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Ondersteunde providers

Provider | Standaardmodel | Referentie-invoer | Ondersteunde besturingselementen | Authenticatie  
---|---|---|---|---  
ComfyUI | `workflow` | Tot 1 afbeelding | Workflow-gedefinieerde muziek of audio | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Tot 10 afbeeldingen | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Geen | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` of MiniMax OAuth  
  
### Mogelijkhedenmatrix

Het expliciete moduscontract dat wordt gebruikt door `music_generate`, contracttests en de gedeelde live sweep:

Provider | `generate` | `edit` | Bewerkingslimiet | Gedeelde live lanes  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 afbeelding | Niet in de gedeelde sweep; afgedekt door `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 afbeeldingen | `generate`, `edit`  
MiniMax | ✓ | — | Geen | `generate`  
  
Gebruik `action: "list"` om beschikbare gedeelde providers en modellen tijdens runtime te inspecteren:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Gebruik `action: "status"` om de actieve muziekgeneratietaak met sessieondersteuning te inspecteren:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Voorbeeld van directe generatie:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Hulpmiddelparameters

Prompt voor muziekgeneratie. Vereist voor `action: "generate"`.

`"status"` retourneert de huidige sessietaak; `"list"` inspecteert providers.

Provider-/model-override (bijv. `google/lyria-3-pro-preview`, `comfy/workflow`).

Optionele songtekst wanneer de provider expliciete songtekstinvoer ondersteunt.

Vraag om instrumentale uitvoer wanneer de provider dit ondersteunt.

Eén pad of URL naar een referentieafbeelding.

Meerdere referentieafbeeldingen (tot 10 bij ondersteunende providers).

Doelduur in seconden wanneer de provider duurhints ondersteunt.

Hint voor uitvoerformaat wanneer de provider dit ondersteunt.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Optionele time-out voor providerverzoeken in milliseconden. Als deze wordt weggelaten, gebruikt OpenClaw `agents.defaults.musicGenerationModel.timeoutMs` als dit is geconfigureerd. Waarden onder 10000ms worden verhoogd naar 10000ms en gerapporteerd in het hulpmiddelresultaat. OPENCLAW_DOCS_MARKER:paramClose:

## Asynchroon gedrag

Muziekgeneratie met sessieondersteuning draait als achtergrondtaak:

  * **Achtergrondtaak:** `music_generate` maakt een achtergrondtaak aan, retourneert onmiddellijk een gestart-/taakantwoord en plaatst de voltooide track later in een vervolgbericht van de agent.
  * **Voorkoming van duplicaten:** terwijl een taak `queued` of `running` is, retourneren latere `music_generate`-aanroepen in dezelfde sessie taakstatus in plaats van een nieuwe generatie te starten. Gebruik `action: "status"` om dit expliciet te controleren.
  * **Status opzoeken:** `openclaw tasks list` of `openclaw tasks show <taskId>` inspecteert wachtrij-, actieve en terminale status.
  * **Voltooiingswake:** OpenClaw injecteert een interne voltooiingsgebeurtenis terug in dezelfde sessie, zodat het model zelf de gebruikersgerichte opvolging kan schrijven.
  * **Prompthint:** latere gebruikers-/handmatige beurten in dezelfde sessie krijgen een kleine runtimehint wanneer er al een muziektaak loopt, zodat het model niet blind opnieuw `music_generate` aanroept.
  * **Fallback zonder sessie:** directe/lokale contexten zonder echte agentsessie voeren inline uit en retourneren het uiteindelijke audioresultaat in dezelfde beurt.


### Taaklevenscyclus

Status | Betekenis  
---|---  
`queued` | Taak aangemaakt, wacht tot de provider deze accepteert.  
`running` | Provider verwerkt de taak (meestal 30 seconden tot 3 minuten, afhankelijk van provider en duur).  
`succeeded` | Track klaar; de agent wordt gewekt en plaatst deze in het gesprek.  
`failed` | Providerfout of time-out; de agent wordt gewekt met foutdetails.  
  
Controleer status vanuit de CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Configuratie

### Modelselectie

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Selectievolgorde van providers

OpenClaw probeert providers in deze volgorde:

  1. `model`-parameter uit de hulpmiddelaanroep (als de agent er een opgeeft).
  2. `musicGenerationModel.primary` uit de configuratie.
  3. `musicGenerationModel.fallbacks` op volgorde.
  4. Automatische detectie met alleen op authenticatie gebaseerde providerstandaarden: 
     * huidige standaardprovider eerst;
     * resterende geregistreerde muziekgeneratieproviders op volgorde van provider-id.


Als een provider faalt, wordt de volgende kandidaat automatisch geprobeerd. Als alle pogingen falen, bevat de fout details van elke poging.

Stel `agents.defaults.mediaGenerationAutoProviderFallback: false` in om alleen expliciete `model`-, `primary`\- en `fallbacks`-vermeldingen te gebruiken.

## Provideropmerkingen

ComfyUI

Workflowgestuurd en afhankelijk van de geconfigureerde grafiek plus knooppuntmapping voor prompt-/uitvoervelden. De gebundelde `comfy`-Plugin sluit aan op het gedeelde `music_generate`-hulpmiddel via het providerregister voor muziekgeneratie.

Google (Lyria 3)

Gebruikt Lyria 3-batchgeneratie. De huidige gebundelde flow ondersteunt prompt, optionele songtekst en optionele referentieafbeeldingen.

MiniMax

Gebruikt het batch-eindpunt `music_generation`. Ondersteunt prompt, optionele songtekst, instrumentale modus, duursturing en mp3-uitvoer via `minimax`-API-sleutelauthenticatie of `minimax-portal` OAuth.

## Het juiste pad kiezen

  * **Met gedeelde provider** wanneer je modelselectie, providerfailover en de ingebouwde asynchrone taak-/statusflow wilt.
  * **Plugin-pad (ComfyUI)** wanneer je een aangepaste workflowgrafiek nodig hebt of een provider die geen deel uitmaakt van de gedeelde gebundelde muziekmogelijkheid.


Als je ComfyUI-specifiek gedrag debugt, zie [ComfyUI](</nl/providers/comfy>). Als je gedeeld providergedrag debugt, begin dan met [Google (Gemini)](</nl/providers/google>) of [MiniMax](</nl/providers/minimax>).

## Providermogelijkheidsmodi

Het gedeelde muziekgeneratiecontract ondersteunt expliciete modusdeclaraties:

  * `generate` voor generatie met alleen een prompt.
  * `edit` wanneer het verzoek een of meer referentieafbeeldingen bevat.


Nieuwe providerimplementaties moeten bij voorkeur expliciete modusblokken gebruiken:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Verouderde platte velden zoals `maxInputImages`, `supportsLyrics` en `supportsFormat` zijn **niet** genoeg om bewerkingsondersteuning te adverteren. Providers moeten `generate` en `edit` expliciet declareren, zodat live tests, contracttests en het gedeelde `music_generate`-hulpmiddel modusondersteuning deterministisch kunnen valideren.

## Live tests

Opt-in livedekking voor de gedeelde gebundelde providers:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Repo-wrapper:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Dit livebestand laadt ontbrekende provider-env-vars uit `~/.profile`, geeft standaard de voorkeur aan live/env-API-sleutels boven opgeslagen auth-profielen, en voert zowel `generate` als gedeclareerde `edit`-dekking uit wanneer de provider de bewerkmodus inschakelt. Dekking vandaag:

  * `google`: `generate` plus `edit`
  * `minimax`: alleen `generate`
  * `comfy`: afzonderlijke Comfy-live-dekking, niet de gedeelde providersweep


Meld je aan voor live-dekking voor het meegeleverde ComfyUI-muziekpad:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Het Comfy-livebestand dekt ook comfy-image- en videoworkflows wanneer die secties zijn geconfigureerd.

## Gerelateerd

  * [Achtergrondtaken](</nl/automation/tasks>) — taaktracking voor losgekoppelde `music_generate`-runs
  * [ComfyUI](</nl/providers/comfy>)
  * [Configuratiereferentie](</nl/gateway/config-agents#agent-defaults>) — `musicGenerationModel`-configuratie
  * [Google (Gemini)](</nl/providers/google>)
  * [MiniMax](</nl/providers/minimax>)
  * [Modellen](</nl/concepts/models>) — modelconfiguratie en failover
  * [Toolsoverzicht](</nl/tools>)


Was this useful?YesNo
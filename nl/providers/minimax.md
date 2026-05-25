---
title: MiniMax
source_url: https://docs.openclaw.ai/nl/providers/minimax
scraped_at: 2026-05-25
---

OpenClaw's MiniMax-provider gebruikt standaard **MiniMax M2.7**.

MiniMax biedt ook:

  * Gebundelde spraaksynthese via T2A v2
  * Gebundeld beeldbegrip via `MiniMax-VL-01`
  * Gebundelde muziekgeneratie via `music-2.6`
  * Gebundelde `web_search` via de zoek-API van het MiniMax Token Plan


Provider-indeling:

Provider-ID | Auth | Mogelijkheden  
---|---|---  
`minimax` | API-sleutel | Tekst, beeldgeneratie, muziekgeneratie, videogeneratie, beeldbegrip, spraak, webzoekfunctie  
`minimax-portal` | OAuth | Tekst, beeldgeneratie, muziekgeneratie, videogeneratie, beeldbegrip, spraak  
  
## Ingebouwde catalogus

Model | Type | Beschrijving  
---|---|---  
`MiniMax-M2.7` | Chat (redeneren) | Standaard gehost redeneermodel  
`MiniMax-M2.7-highspeed` | Chat (redeneren) | Snellere M2.7-redeneerlaag  
`MiniMax-VL-01` | Vision | Model voor beeldbegrip  
`image-01` | Beeldgeneratie | Tekst-naar-beeld- en beeld-naar-beeldbewerking  
`music-2.6` | Muziekgeneratie | Standaard muziekmodel  
`music-2.5` | Muziekgeneratie | Vorige muziekgeneratielaag  
`music-2.0` | Muziekgeneratie | Verouderde muziekgeneratielaag  
`MiniMax-Hailuo-2.3` | Videogeneratie | Tekst-naar-video- en beeldreferentiestromen  
  
## Aan de slag

Kies je gewenste auth-methode en volg de installatiestappen.

### OAuth (Coding Plan)

**Beste voor:** snelle installatie met MiniMax Coding Plan via OAuth, geen API-sleutel vereist.

### Internationaal

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-oauth
[/code]

Dit authenticeert tegen `api.minimax.io`.

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### China

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-oauth
[/code]

Dit authenticeert tegen `api.minimaxi.com`.

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### API-sleutel

**Beste voor:** gehoste MiniMax met Anthropic-compatibele API.

### Internationaal

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-api
[/code]

Dit configureert `api.minimax.io` als de basis-URL.

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### China

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-api
[/code]

Dit configureert `api.minimaxi.com` als de basis-URL.

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### Configuratievoorbeeld

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "minimax/MiniMax-M2.7" } } },  models: {    mode: "merge",    providers: {      minimax: {        baseUrl: "https://api.minimax.io/anthropic",        apiKey: "${MINIMAX_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "MiniMax-M2.7",            name: "MiniMax M2.7",            reasoning: true,            input: ["text"],            cost: { input: 0.3, output: 1.2, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },          {            id: "MiniMax-M2.7-highspeed",            name: "MiniMax M2.7 Highspeed",            reasoning: true,            input: ["text"],            cost: { input: 0.6, output: 2.4, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },        ],      },    },  },}
[/code]

## Configureren via `openclaw configure`

Gebruik de interactieve configuratiewizard om MiniMax in te stellen zonder JSON te bewerken:

* ### Start de wizard

bashCopy code
[code]
    openclaw configure
[/code]

* ### Selecteer Model/auth

Kies **Model/auth** in het menu.

* ### Kies een MiniMax-authoptie

Kies een van de beschikbare MiniMax-opties:

Auth-keuze | Beschrijving  
---|---  
`minimax-global-oauth` | Internationale OAuth (Coding Plan)  
`minimax-cn-oauth` | China OAuth (Coding Plan)  
`minimax-global-api` | Internationale API-sleutel  
`minimax-cn-api` | China API-sleutel  
* ### Kies je standaardmodel

Selecteer je standaardmodel wanneer daarom wordt gevraagd.

## Mogelijkheden

### Afbeeldingen genereren

De MiniMax-Plugin registreert het model `image-01` voor de tool `image_generate`. Het ondersteunt:

  * **Genereren van tekst naar afbeelding** met controle over beeldverhouding
  * **Bewerking van afbeelding naar afbeelding** (onderwerpreferentie) met controle over beeldverhouding
  * Maximaal **9 uitvoerafbeeldingen** per aanvraag
  * Maximaal **1 referentieafbeelding** per bewerkingsaanvraag
  * Ondersteunde beeldverhoudingen: `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`


Als je MiniMax wilt gebruiken voor het genereren van afbeeldingen, stel je dit in als provider voor afbeeldingsgeneratie:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "minimax/image-01" },    },  },}
[/code]

De Plugin gebruikt dezelfde `MINIMAX_API_KEY` of OAuth-authenticatie als de tekstmodellen. Er is geen aanvullende configuratie nodig als MiniMax al is ingesteld.

Zowel `minimax` als `minimax-portal` registreren `image_generate` met hetzelfde `image-01`-model. Instellingen met API-sleutels gebruiken `MINIMAX_API_KEY`; OAuth-instellingen kunnen in plaats daarvan het gebundelde `minimax-portal`-authenticatiepad gebruiken.

Afbeeldingen genereren gebruikt altijd het speciale afbeeldingseindpunt van MiniMax (`/v1/image_generation`) en negeert `models.providers.minimax.baseUrl`, omdat dat veld de chat/Anthropic-compatibele basis-URL configureert. Stel `MINIMAX_API_HOST=https://api.minimaxi.com` in om afbeeldingsgeneratie via het CN-eindpunt te routeren; het standaard globale eindpunt is `https://api.minimax.io`.

Wanneer onboarding of installatie met API-sleutel expliciete `models.providers.minimax`-vermeldingen schrijft, materialiseert OpenClaw `MiniMax-M2.7` en `MiniMax-M2.7-highspeed` als tekst-only chatmodellen. Afbeeldingsbegrip wordt afzonderlijk beschikbaar gemaakt via de Plugin-eigen mediaprovider `MiniMax-VL-01`.

### Tekst-naar-spraak

De gebundelde `minimax`-Plugin registreert MiniMax T2A v2 als spraakprovider voor `messages.tts`.

  * Standaard TTS-model: `speech-2.8-hd`
  * Standaardstem: `English_expressive_narrator`
  * Ondersteunde gebundelde model-id's zijn onder andere `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd` en `speech-01-turbo`.
  * Auth-resolutie is `messages.tts.providers.minimax.apiKey`, daarna OAuth-/token-authprofielen van `minimax-portal`, daarna omgevingssleutels voor Token Plan (`MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`), daarna `MINIMAX_API_KEY`.
  * Als er geen TTS-host is geconfigureerd, hergebruikt OpenClaw de geconfigureerde OAuth-host van `minimax-portal` en verwijdert het Anthropic-compatibele padsuffixen zoals `/anthropic`.
  * Normale audiobijlagen blijven MP3.
  * Voice-note-doelen zoals Feishu en Telegram worden getranscodeerd van MiniMax MP3 naar 48 kHz Opus met `ffmpeg`, omdat de Feishu/Lark-bestands-API alleen `file_type: "opus"` accepteert voor native audioberichten.
  * MiniMax T2A accepteert fractionele `speed` en `vol`, maar `pitch` wordt verzonden als een geheel getal; OpenClaw kapt fractionele `pitch`-waarden af vóór de API-aanvraag.

Instelling | Env-var | Standaard | Beschrijving  
---|---|---|---  
`messages.tts.providers.minimax.baseUrl` | `MINIMAX_API_HOST` | `https://api.minimax.io` | MiniMax T2A API-host.  
`messages.tts.providers.minimax.model` | `MINIMAX_TTS_MODEL` | `speech-2.8-hd` | TTS-model-id.  
`messages.tts.providers.minimax.voiceId` | `MINIMAX_TTS_VOICE_ID` | `English_expressive_narrator` | Stem-id gebruikt voor spraakuitvoer.  
`messages.tts.providers.minimax.speed` |  | `1.0` | Afspeelsnelheid, `0.5..2.0`.  
`messages.tts.providers.minimax.vol` |  | `1.0` | Volume, `(0, 10]`.  
`messages.tts.providers.minimax.pitch` |  | `0` | Verschuiving van toonhoogte als geheel getal, `-12..12`.  
  
### Muziek genereren

De gebundelde MiniMax-Plugin registreert muziekgeneratie via de gedeelde tool `music_generate` voor zowel `minimax` als `minimax-portal`.

  * Standaard muziekmodel: `minimax/music-2.6`
  * OAuth-muziekmodel: `minimax-portal/music-2.6`
  * Ondersteunt ook `minimax/music-2.5` en `minimax/music-2.0`
  * Promptbesturing: `lyrics`, `instrumental`, `durationSeconds`
  * Uitvoerformaat: `mp3`
  * Runs met sessieondersteuning worden losgekoppeld via de gedeelde taak-/statusflow, inclusief `action: "status"`


MiniMax gebruiken als standaardprovider voor muziek:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "minimax/music-2.6",      },    },  },}
[/code]

### Video genereren

De gebundelde MiniMax-Plugin registreert videogeneratie via de gedeelde tool `video_generate` voor zowel `minimax` als `minimax-portal`.

  * Standaard videomodel: `minimax/MiniMax-Hailuo-2.3`
  * OAuth-videomodel: `minimax-portal/MiniMax-Hailuo-2.3`
  * Modi: tekst-naar-video en flows met enkelbeeldreferentie
  * Ondersteunt `aspectRatio` en `resolution`


MiniMax gebruiken als standaardprovider voor video:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "minimax/MiniMax-Hailuo-2.3",      },    },  },}
[/code]

### Afbeeldingsbegrip

De MiniMax Plugin registreert afbeeldingsbegrip afzonderlijk van de tekstcatalogus:

Provider-ID | Standaard afbeeldingsmodel  
---|---  
`minimax` | `MiniMax-VL-01`  
`minimax-portal` | `MiniMax-VL-01`  
  
Daarom kan automatische mediaroutering MiniMax-afbeeldingsbegrip gebruiken, zelfs wanneer de gebundelde tekstprovidercatalogus nog tekst-only M2.7-chatrefs toont.

### Webzoekopdracht

De MiniMax Plugin registreert ook `web_search` via de MiniMax Token Plan zoek-API.

  * Provider-id: `minimax`
  * Gestructureerde resultaten: titels, URL's, snippets, gerelateerde zoekopdrachten
  * Voorkeurs-env-var: `MINIMAX_CODE_PLAN_KEY`
  * Geaccepteerde env-aliassen: `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN`
  * Compatibiliteitsfallback: `MINIMAX_API_KEY` wanneer deze al naar token-plan-inloggegevens verwijst
  * Hergebruik van regio: `plugins.entries.minimax.config.webSearch.region`, daarna `MINIMAX_API_HOST`, daarna MiniMax-providerbasis-URL's
  * Zoeken blijft op provider-id `minimax`; OAuth CN/global-configuratie kan de regio indirect sturen via `models.providers.minimax-portal.baseUrl` en kan bearer-auth bieden via `MINIMAX_OAUTH_TOKEN`


Configuratie staat onder `plugins.entries.minimax.config.webSearch.*`.

## Geavanceerde configuratie

Configuration options Optie | Beschrijving  
---|---  
`models.providers.minimax.baseUrl` | Geef de voorkeur aan `https://api.minimax.io/anthropic` (Anthropic-compatibel); `https://api.minimax.io/v1` is optioneel voor OpenAI-compatibele payloads  
`models.providers.minimax.api` | Geef de voorkeur aan `anthropic-messages`; `openai-completions` is optioneel voor OpenAI-compatibele payloads  
`models.providers.minimax.apiKey` | MiniMax-API-sleutel (`MINIMAX_API_KEY`)  
`models.providers.minimax.models` | Definieer `id`, `name`, `reasoning`, `contextWindow`, `maxTokens`, `cost`  
`agents.defaults.models` | Aliasmodellen die je in de allowlist wilt opnemen  
`models.mode` | Houd `merge` aan als je MiniMax naast ingebouwde providers wilt toevoegen  
Thinking defaults

Bij `api: "anthropic-messages"` injecteert OpenClaw `thinking: { type: "disabled" }`, tenzij thinking al expliciet is ingesteld in params/config.

Dit voorkomt dat het streamingendpoint van MiniMax `reasoning_content` uitzendt in OpenAI-achtige delta-chunks, waardoor interne redenering naar zichtbare uitvoer zou lekken.

Fast mode

`/fast on` of `params.fastMode: true` herschrijft `MiniMax-M2.7` naar `MiniMax-M2.7-highspeed` op het Anthropic-compatibele streampad.

Fallback example

**Het meest geschikt voor:** behoud je sterkste model van de nieuwste generatie als primaire keuze en val terug op MiniMax M2.7. Het voorbeeld hieronder gebruikt Opus als concrete primaire keuze; vervang dit door je voorkeursmodel van de nieuwste generatie.

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": { alias: "primary" },        "minimax/MiniMax-M2.7": { alias: "minimax" },      },      model: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["minimax/MiniMax-M2.7"],      },    },  },}
[/code]

Coding Plan usage details

  * Coding Plan-gebruiks-API: `https://api.minimaxi.com/v1/token_plan/remains` of `https://api.minimax.io/v1/token_plan/remains` (vereist een codingplansleutel).
  * Gebruikspolling leidt de host af van `models.providers.minimax-portal.baseUrl` of `models.providers.minimax.baseUrl` wanneer geconfigureerd, zodat global-configuraties die `https://api.minimax.io/anthropic` gebruiken `api.minimax.io` pollen. Ontbrekende of onjuist gevormde basis-URL's behouden de CN-fallback voor compatibiliteit.
  * OpenClaw normaliseert MiniMax-codingplangebruik naar dezelfde `% left`-weergave die andere providers gebruiken. De ruwe velden `usage_percent` / `usagePercent` van MiniMax zijn resterend quotum, geen verbruikt quotum, dus OpenClaw keert ze om. Op telling gebaseerde velden hebben voorrang wanneer ze aanwezig zijn.
  * Wanneer de API `model_remains` retourneert, geeft OpenClaw de voorkeur aan de chatmodelvermelding, leidt indien nodig het vensterlabel af van `start_time` / `end_time`, en neemt de geselecteerde modelnaam op in het planlabel zodat codingplanvensters makkelijker te onderscheiden zijn.
  * Gebruikssnapshots behandelen `minimax`, `minimax-cn` en `minimax-portal` als hetzelfde MiniMax-quotumoppervlak, en geven de voorkeur aan opgeslagen MiniMax OAuth voordat wordt teruggevallen op env-vars voor Coding Plan-sleutels.


## Notities

  * Modelrefs volgen het authenticatiepad: 
    * API-sleutelconfiguratie: `minimax/<model>`
    * OAuth-configuratie: `minimax-portal/<model>`
  * Standaard chatmodel: `MiniMax-M2.7`
  * Alternatief chatmodel: `MiniMax-M2.7-highspeed`
  * Onboarding en directe API-sleutelconfiguratie schrijven tekst-only modeldefinities voor beide M2.7-varianten
  * Afbeeldingsbegrip gebruikt de door de Plugin beheerde `MiniMax-VL-01`-mediaprovider
  * Werk prijswaarden bij in `models.json` als je exacte kostenregistratie nodig hebt
  * Gebruik `openclaw models list` om de huidige provider-id te bevestigen en schakel daarna over met `openclaw models set minimax/MiniMax-M2.7` of `openclaw models set minimax-portal/MiniMax-M2.7`


## Probleemoplossing

"Unknown model: minimax/MiniMax-M2.7"

Dit betekent meestal dat de **MiniMax-provider niet is geconfigureerd** (geen overeenkomende providervermelding en geen MiniMax-authprofiel/env-sleutel gevonden). Een oplossing voor deze detectie zit in **2026.1.12**. Los dit op door:

  * Te upgraden naar **2026.1.12** (of te draaien vanaf source `main`) en daarna de Gateway opnieuw te starten.
  * `openclaw configure` uit te voeren en een **MiniMax** -authoptie te selecteren, of
  * Het overeenkomende blok `models.providers.minimax` of `models.providers.minimax-portal` handmatig toe te voegen, of
  * `MINIMAX_API_KEY`, `MINIMAX_OAUTH_TOKEN` of een MiniMax-authprofiel in te stellen zodat de overeenkomende provider kan worden geïnjecteerd.


Zorg dat de model-id **hoofdlettergevoelig** is:

  * API-sleutelpad: `minimax/MiniMax-M2.7` of `minimax/MiniMax-M2.7-highspeed`
  * OAuth-pad: `minimax-portal/MiniMax-M2.7` of `minimax-portal/MiniMax-M2.7-highspeed`


Controleer daarna opnieuw met:

bashCopy code
[code]
    openclaw models list
[/code]

## Gerelateerd

[**Model selection** Providers, modelrefs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Image generation** Gedeelde afbeeldingstoolparameters en providerselectie. ](</nl/tools/image-generation>) [**Music generation** Gedeelde muziektolparameters en providerselectie. ](</nl/tools/music-generation>) [**Video generation** Gedeelde videotoolparameters en providerselectie. ](</nl/tools/video-generation>) [**MiniMax Search** Webzoekconfiguratie via MiniMax Token Plan. ](</nl/tools/minimax-search>) [**Troubleshooting** Algemene probleemoplossing en FAQ. ](</nl/help/troubleshooting>)

Was this useful?YesNo
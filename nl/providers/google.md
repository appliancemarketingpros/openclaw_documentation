---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/nl/providers/google
scraped_at: 2026-05-25
---

De Google-Plugin biedt toegang tot Gemini-modellen via Google AI Studio, plus afbeeldingsgeneratie, mediabegrip (afbeelding/audio/video), tekst-naar-spraak en webzoekopdrachten via Gemini Grounding.

  * Aanbieder: `google`
  * Authenticatie: `GEMINI_API_KEY` of `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Runtimeoptie: provider/model `agentRuntime.id: "google-gemini-cli"` hergebruikt Gemini CLI OAuth terwijl modelverwijzingen canoniek blijven als `google/*`.


## Aan de slag

Kies je gewenste authenticatiemethode en volg de installatiestappen.

### API-sleutel

**Het meest geschikt voor:** standaardtoegang tot de Gemini API via Google AI Studio.

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Of geef de sleutel direct door:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Een standaardmodel instellen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Het meest geschikt voor:** het hergebruiken van een bestaande Gemini CLI-login via PKCE OAuth in plaats van een aparte API-sleutel.

* ### De Gemini CLI installeren

De lokale opdracht `gemini` moet beschikbaar zijn op `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw ondersteunt zowel Homebrew-installaties als globale npm-installaties, inclusief veelvoorkomende Windows/npm-indelingen.

* ### Inloggen via OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Standaardmodel: `google/gemini-3.1-pro-preview`
  * Runtime: `google-gemini-cli`
  * Alias: `gemini-cli`


De Gemini API-model-id van Gemini 3.1 Pro is `gemini-3.1-pro-preview`. OpenClaw accepteert de kortere `google/gemini-3.1-pro` als handige alias en normaliseert die vóór provider-aanroepen.

**Omgevingsvariabelen:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Of de `GEMINI_CLI_*`-varianten.)

`google-gemini-cli/*`-modelverwijzingen zijn verouderde compatibiliteitsaliassen. Nieuwe configuraties moeten `google/*`-modelverwijzingen plus de runtime `google-gemini-cli` gebruiken wanneer ze lokale Gemini CLI-uitvoering willen.

## Mogelijkheden

Mogelijkheid | Ondersteund  
---|---  
Chatvoltooiingen | Ja  
Afbeeldingsgeneratie | Ja  
Muziekgeneratie | Ja  
Tekst-naar-spraak | Ja  
Realtime spraak | Ja (Google Live API)  
Afbeeldingsbegrip | Ja  
Audiotranscriptie | Ja  
Videobegrip | Ja  
Webzoekopdracht (Grounding) | Ja  
Denken/redeneren | Ja (Gemini 2.5+ / Gemini 3+)  
Gemma 4-modellen | Ja  
  
## Webzoekopdracht

De meegeleverde `gemini`-provider voor webzoekopdrachten gebruikt Gemini Google Search-grounding. Configureer een specifieke zoeksleutel onder `plugins.entries.google.config.webSearch`, of laat deze `models.providers.google.apiKey` hergebruiken na `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

De volgorde van credentialvoorrang is de specifieke `webSearch.apiKey`, daarna `GEMINI_API_KEY`, daarna `models.providers.google.apiKey`. `webSearch.baseUrl` is optioneel en bestaat voor operatorproxies of compatibele Gemini API-eindpunten; wanneer dit wordt weggelaten, hergebruikt Gemini-webzoekopdracht `models.providers.google.baseUrl`. Zie [Gemini-zoekopdracht](</nl/tools/gemini-search>) voor het providerspecifieke toolgedrag.

## Afbeeldingsgeneratie

De meegeleverde `google`-provider voor afbeeldingsgeneratie gebruikt standaard `google/gemini-3.1-flash-image-preview`.

  * Ondersteunt ook `google/gemini-3-pro-image-preview`
  * Genereren: maximaal 4 afbeeldingen per aanvraag
  * Bewerkingsmodus: ingeschakeld, maximaal 5 invoerafbeeldingen
  * Geometrie-instellingen: `size`, `aspectRatio` en `resolution`


Google als standaardprovider voor afbeeldingen gebruiken:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Videogeneratie

De meegeleverde `google`-Plugin registreert ook videogeneratie via de gedeelde tool `video_generate`.

  * Standaardvideomodel: `google/veo-3.1-fast-generate-preview`
  * Modi: tekst-naar-video, afbeelding-naar-video en flows met één videoreferentie
  * Ondersteunt `aspectRatio` (`16:9`, `9:16`) en `resolution` (`720P`, `1080P`); audio-uitvoer wordt vandaag niet ondersteund door Veo
  * Ondersteunde duurwaarden: **4, 6 of 8 seconden** (andere waarden worden afgerond naar de dichtstbijzijnde toegestane waarde)


Google als standaardprovider voor video gebruiken:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Muziekgeneratie

De meegeleverde `google`-Plugin registreert ook muziekgeneratie via de gedeelde tool `music_generate`.

  * Standaardmuziekmodel: `google/lyria-3-clip-preview`
  * Ondersteunt ook `google/lyria-3-pro-preview`
  * Promptinstellingen: `lyrics` en `instrumental`
  * Uitvoerformaat: standaard `mp3`, plus `wav` op `google/lyria-3-pro-preview`
  * Referentie-invoer: maximaal 10 afbeeldingen
  * Runs met sessieondersteuning worden losgekoppeld via de gedeelde taak-/statusflow, inclusief `action: "status"`


Google als standaardprovider voor muziek gebruiken:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Tekst-naar-spraak

De meegeleverde `google`-spraakprovider gebruikt het Gemini API TTS-pad met `gemini-3.1-flash-tts-preview`.

  * Standaardstem: `Kore`
  * Authenticatie: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` of `GOOGLE_API_KEY`
  * Uitvoer: WAV voor normale TTS-bijlagen, Opus voor spraaknotitiedoelen, PCM voor Talk/telefonie
  * Spraaknotitie-uitvoer: Google PCM wordt verpakt als WAV en getranscodeerd naar 48 kHz Opus met `ffmpeg`


Het Gemini TTS-batchpad van Google retourneert gegenereerde audio in de voltooide `generateContent`-respons. Gebruik voor gesproken gesprekken met de laagste latentie de Google-provider voor realtime spraak, ondersteund door de Gemini Live API, in plaats van batch- TTS.

Google als standaardprovider voor TTS gebruiken:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS gebruikt prompts in natuurlijke taal voor stijlregeling. Stel `audioProfile` in om een herbruikbare stijlprompt vóór de gesproken tekst te plaatsen. Stel `speakerName` in wanneer je prompttekst naar een benoemde spreker verwijst.

Gemini API TTS accepteert ook expressieve audiotags tussen vierkante haken in de tekst, zoals `[whispers]` of `[laughs]`. Plaats ze in een `[[tts:text]]...[[/tts:text]]`\- blok om tags uit het zichtbare chatantwoord te houden terwijl ze naar TTS worden verzonden:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Realtime spraak

De meegeleverde `google`-Plugin registreert een provider voor realtime spraak, ondersteund door de Gemini Live API voor backend-audiobruggen zoals Voice Call en Google Meet.

Instelling | Configuratiepad | Standaard  
---|---|---  
Model | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Stem | `...google.voice` | `Kore`  
Temperatuur | `...google.temperature` | (niet ingesteld)  
VAD-startgevoeligheid | `...google.startSensitivity` | (niet ingesteld)  
VAD-eindgevoeligheid | `...google.endSensitivity` | (niet ingesteld)  
Stilteduur | `...google.silenceDurationMs` | (niet ingesteld)  
Activiteitsafhandeling | `...google.activityHandling` | Google-standaard, `start-of-activity-interrupts`  
Beurtdekking | `...google.turnCoverage` | Google-standaard, `only-activity`  
Automatische VAD uitschakelen | `...google.automaticActivityDetectionDisabled` | `false`  
Sessiehervatting | `...google.sessionResumption` | `true`  
Contextcompressie | `...google.contextWindowCompression` | `true`  
API-sleutel | `...google.apiKey` | Valt terug op `models.providers.google.apiKey`, `GEMINI_API_KEY` of `GOOGLE_API_KEY`  
  
Voorbeeld van realtimeconfiguratie voor Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Voor live-verificatie door maintainers, voer uit: `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. De smoke dekt ook OpenAI-backend-/WebRTC-paden; de Google-stap maakt dezelfde beperkte Live API-tokenvorm aan die door Control UI Talk wordt gebruikt, opent het browser- WebSocket-eindpunt, verstuurt de initiële setup-payload en wacht op `setupComplete`.

## Geavanceerde configuratie

Direct Gemini-cachehergebruik

Voor directe Gemini API-runs (`api: "google-generative-ai"`) geeft OpenClaw een geconfigureerde `cachedContent`-handle door aan Gemini-verzoeken.

  * Configureer per-model- of globale parameters met `cachedContent` of de oudere `cached_content`
  * Als beide aanwezig zijn, wint `cachedContent`
  * Voorbeeldwaarde: `cachedContents/prebuilt-context`
  * Gemini-cache-hitgebruik wordt genormaliseerd naar OpenClaw `cacheRead` vanuit upstream `cachedContentTokenCount`

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gebruiksnotities voor Gemini CLI JSON

Bij gebruik van de OAuth-provider `google-gemini-cli` normaliseert OpenClaw de CLI JSON-uitvoer als volgt:

  * Antwoordtekst komt uit het CLI JSON-veld `response`.
  * Gebruik valt terug op `stats` wanneer de CLI `usage` leeg laat.
  * `stats.cached` wordt genormaliseerd naar OpenClaw `cacheRead`.
  * Als `stats.input` ontbreekt, leidt OpenClaw invoertokens af uit `stats.input_tokens - stats.cached`.

Omgeving en daemoninstelling

Als de Gateway als daemon draait (launchd/systemd), zorg er dan voor dat `GEMINI_API_KEY` beschikbaar is voor dat proces (bijvoorbeeld in `~/.openclaw/.env` of via `env.shellEnv`).

## Gerelateerd

[**Modelselectie** Providers, modelrefs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Afbeeldingen genereren** Gedeelde parameters voor afbeeldingstools en providerselectie. ](</nl/tools/image-generation>) [**Video genereren** Gedeelde parameters voor videotools en providerselectie. ](</nl/tools/video-generation>) [**Muziek genereren** Gedeelde parameters voor muziektools en providerselectie. ](</nl/tools/music-generation>)

Was this useful?YesNo
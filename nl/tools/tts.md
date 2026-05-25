---
title: Tekst-naar-spraak
source_url: https://docs.openclaw.ai/nl/tools/tts
scraped_at: 2026-05-25
---

OpenClaw kan uitgaande antwoorden omzetten naar audio via **14 spraakproviders** en native spraakberichten leveren op Feishu, Matrix, Telegram en WhatsApp, audio-bijlagen overal elders, en PCM/Ulaw-streams voor telefonie en Talk.

TTS is de spraakuitvoerhelft van de `stt-tts`-modus van Talk. Provider-native `realtime` Talk-sessies synthetiseren spraak binnen de realtime-provider in plaats van dit TTS-pad aan te roepen, terwijl `transcription`-sessies geen spraakantwoord van de assistent synthetiseren.

## Snel aan de slag

* ### Kies een provider

OpenAI en ElevenLabs zijn de betrouwbaarste gehoste opties. Microsoft en Local CLI werken zonder API-sleutel. Zie de providermatrix voor de volledige lijst.

* ### Stel de API-sleutel in

Exporteer de env-var voor je provider (bijvoorbeeld `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft en Local CLI hebben geen sleutel nodig.

* ### Schakel in de configuratie in

Stel `messages.tts.auto: "always"` en `messages.tts.provider` in:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Probeer het in chat

`/tts status` toont de huidige status. `/tts audio Hello from OpenClaw` verzendt een eenmalig audioantwoord.

## Ondersteunde providers

Provider | Auth | Opmerkingen  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (ook `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Native Ogg/Opus-uitvoer voor spraaknotities en telefonie.  
**DeepInfra** | `DEEPINFRA_API_KEY` | OpenAI-compatibele TTS. Standaard `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` of `XI_API_KEY` | Stemklonen, meertalig, deterministisch via `seed`; gestreamd voor Discord-spraakweergave.  
**Google Gemini** | `GEMINI_API_KEY` of `GOOGLE_API_KEY` | Gemini API batch-TTS; personabewust via `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Uitvoer voor spraaknotities en telefonie.  
**Inworld** | `INWORLD_API_KEY` | Streaming TTS-API. Native Opus-spraaknotities en PCM-telefonie.  
**Local CLI** | geen | Voert een geconfigureerde lokale TTS-opdracht uit.  
**Microsoft** | geen | Publieke Edge neural TTS via `node-edge-tts`. Best-effort, geen SLA.  
**MiniMax** | `MINIMAX_API_KEY` (of Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A v2-API. Standaard `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Ook gebruikt voor automatische samenvatting; ondersteunt persona-`instructions`.  
**OpenRouter** | `OPENROUTER_API_KEY` (kan `models.providers.openrouter.apiKey` hergebruiken) | Standaardmodel `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` of `BYTEPLUS_SEED_SPEECH_API_KEY` (legacy AppID/token: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | BytePlus Seed Speech HTTP-API.  
**Vydra** | `VYDRA_API_KEY` | Gedeelde image-, video- en spraakprovider.  
**xAI** | `XAI_API_KEY` | xAI batch-TTS. Native Opus-spraaknotitie wordt **niet** ondersteund.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo TTS via Xiaomi chat completions.  
  
Als meerdere providers zijn geconfigureerd, wordt de geselecteerde provider eerst gebruikt en zijn de andere fallback-opties. Automatische samenvatting gebruikt `summaryModel` (of `agents.defaults.model.primary`), dus die provider moet ook geauthenticeerd zijn als je samenvattingen ingeschakeld houdt.

## Configuratie

TTS-configuratie staat onder `messages.tts` in `~/.openclaw/openclaw.json`. Kies een preset en pas het providerblok aan:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (geen sleutel)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### Stemoverschrijvingen per agent

Gebruik `agents.list[].tts` wanneer één agent met een andere provider, stem, model, persona of Auto-TTS-modus moet spreken. Het agentblok deep-merget over `messages.tts`, zodat providerreferenties in de globale providerconfiguratie kunnen blijven:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Om een persona per agent vast te pinnen, stel je `agents.list[].tts.persona` in naast de providerconfiguratie — deze overschrijft de globale `messages.tts.persona` alleen voor die agent.

Voorrangsvolgorde voor automatische antwoorden, `/tts audio`, `/tts status` en de agenttool `tts`:

  1. `messages.tts`
  2. actieve `agents.list[].tts`
  3. kanaaloverschrijving, wanneer het kanaal `channels.<channel>.tts` ondersteunt
  4. accountoverschrijving, wanneer het kanaal `channels.<channel>.accounts.<id>.tts` doorgeeft
  5. lokale `/tts`-voorkeuren voor deze host
  6. inline `[[tts:...]]`-directieven wanneer modeloverschrijvingen zijn ingeschakeld


Kanaal- en accountoverschrijvingen gebruiken dezelfde vorm als `messages.tts` en worden diep samengevoegd over de eerdere lagen, zodat gedeelde providerreferenties in `messages.tts` kunnen blijven terwijl een kanaal of botaccount alleen stem, model, persona of automatische modus wijzigt:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Persona's

Een **persona** is een stabiele gesproken identiteit die deterministisch over providers heen kan worden toegepast. Deze kan één provider verkiezen, providerneutrale promptintentie definiëren en providerspecifieke koppelingen bevatten voor stemmen, modellen, prompttemplates, seeds en steminstellingen.

### Minimale persona

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Volledige persona (providerneutrale prompt)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Droge, warme Britse butlerverteller.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "Een briljante Britse butler. Droog, gevat, warm, charmant, emotioneel expressief, nooit generiek.",            scene: "Een stille studeerkamer laat op de avond. Close-mic-vertelling voor een vertrouwde operator.",            sampleContext: "De spreker beantwoordt een privé technisch verzoek met beknopt zelfvertrouwen en droge warmte.",            style: "Verfijnd, ingetogen, licht geamuseerd.",            accent: "Brits Engels.",            pacing: "Afgewogen, met korte dramatische pauzes.",            constraints: ["Lees configuratiewaarden niet hardop voor.", "Leg de persona niet uit."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Persona-resolutie

De actieve persona wordt deterministisch geselecteerd:

  1. Lokale voorkeur `/tts persona <id>`, indien ingesteld.
  2. `messages.tts.persona`, indien ingesteld.
  3. Geen persona.


Providerselectie verloopt expliciet eerst:

  1. Directe overschrijvingen (CLI, Gateway, Talk, toegestane TTS-directieven).
  2. Lokale voorkeur `/tts provider <id>`.
  3. `provider` van de actieve persona.
  4. `messages.tts.provider`.
  5. Automatische registerselectie.


Voor elke providerpoging voegt OpenClaw configuraties in deze volgorde samen:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Vertrouwde verzoekoverschrijvingen
  4. Toegestane door het model uitgegeven TTS-directiefoverschrijvingen


### Hoe providers personaprompts gebruiken

Personapromptvelden (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) zijn **providerneutraal**. Elke provider bepaalt hoe deze worden gebruikt:

Google Gemini

Verpakt personapromptvelden in een Gemini TTS-promptstructuur **alleen wanneer** de effectieve Google-providerconfiguratie `promptTemplate: "audio-profile-v1"` of `personaPrompt` instelt. De oudere velden `audioProfile` en `speakerName` worden nog steeds vooraf toegevoegd als Google-specifieke prompttekst. Inline audiotags zoals `[whispers]` of `[laughs]` binnen een `[[tts:text]]`-blok blijven behouden in het Gemini-transcript; OpenClaw genereert deze tags niet.

OpenAI

Koppelt personapromptvelden aan het verzoekveld `instructions` **alleen wanneer** er geen expliciete OpenAI-`instructions` is geconfigureerd. Expliciete `instructions` heeft altijd voorrang.

Andere providers

Gebruiken alleen de providerspecifieke personakoppelingen onder `personas.<id>.providers.<provider>`. Personapromptvelden worden genegeerd tenzij de provider zijn eigen personapromptkoppeling implementeert.

### Fallbackbeleid

`fallbackPolicy` bepaalt het gedrag wanneer een persona **geen koppeling** heeft voor de geprobeerde provider:

Beleid | Gedrag  
---|---  
`preserve-persona` | **Standaard.** Providerneutrale promptvelden blijven beschikbaar; de provider kan ze gebruiken of negeren.  
`provider-defaults` | Persona wordt voor die poging weggelaten uit promptvoorbereiding; de provider gebruikt zijn neutrale standaardwaarden terwijl fallback naar andere providers doorgaat.  
`fail` | Sla die providerpoging over met `reasonCode: "not_configured"` en `personaBinding: "missing"`. Fallbackproviders worden nog steeds geprobeerd.  
  
Het volledige TTS-verzoek mislukt alleen wanneer **elke** geprobeerde provider wordt overgeslagen of mislukt.

Providerselectie voor Talk-sessies is sessiegebonden. Een Talk-client moet provider-id's, model-id's, stem-id's en locales kiezen uit `talk.catalog` en deze doorgeven via de Talk-sessie of het overdrachtsverzoek. Het openen van een stemsessie mag `messages.tts` of globale Talk-providerstandaarden niet wijzigen.

## Modelgestuurde directieven

Standaard **kan** de assistent `[[tts:...]]`-directieven uitsturen om stem, model of snelheid voor één antwoord te overschrijven, plus een optioneel `[[tts:text]]...[[/tts:text]]`-blok voor expressieve aanwijzingen die alleen in audio moeten verschijnen:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Wanneer `messages.tts.auto` `"tagged"` is, zijn **directieven vereist** om audio te activeren. Streaming bloklevering verwijdert directieven uit zichtbare tekst voordat het kanaal ze ziet, zelfs wanneer ze over aangrenzende blokken zijn verdeeld.

`provider=...` wordt genegeerd tenzij `modelOverrides.allowProvider: true`. Wanneer een antwoord `provider=...` declareert, worden de andere sleutels in die directief alleen door die provider geparsed; niet-ondersteunde sleutels worden verwijderd en gerapporteerd als TTS-directiefwaarschuwingen.

**Beschikbare directiefsleutels:**

  * `provider` (geregistreerde provider-id; vereist `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (MiniMax-volume, 0–10)
  * `pitch` (geheel getal voor MiniMax-toonhoogte, −12 tot 12; fractionele waarden worden afgekapt)
  * `emotion` (Volcengine-emotietag)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Modeloverschrijvingen volledig uitschakelen:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Providerwisseling toestaan terwijl andere knoppen configureerbaar blijven:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Slash-commando's

Eén commando `/tts`. Op Discord registreert OpenClaw ook `/voice`, omdat `/tts` een ingebouwd Discord-commando is — tekst `/tts ...` werkt nog steeds.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Gedragsnotities:

  * `/tts on` schrijft de lokale TTS-voorkeur naar `always`; `/tts off` schrijft deze naar `off`.
  * `/tts chat on|off|default` schrijft een sessiegebonden auto-TTS-overschrijving voor de huidige chat.
  * `/tts persona <id>` schrijft de lokale personavoorkeur; `/tts persona off` wist deze.
  * `/tts latest` leest het nieuwste assistentantwoord uit het huidige sessietranscript en verzendt dit eenmaal als audio. Het slaat alleen een hash van dat antwoord op in de sessievermelding om dubbele spraakverzendingen te onderdrukken.
  * `/tts audio` genereert een eenmalig audioantwoord (schakelt TTS **niet** in).
  * `limit` en `summary` worden opgeslagen in **lokale voorkeuren** , niet in de hoofdconfiguratie.
  * `/tts status` bevat fallbackdiagnostiek voor de nieuwste poging — `Fallback: <primary> -> <used>`, `Attempts: ...` en details per poging (`provider:outcome(reasonCode) latency`).
  * `/status` toont de actieve TTS-modus plus geconfigureerde provider, model, stem en opgeschoonde metadata van aangepaste endpoints wanneer TTS is ingeschakeld.


## Voorkeuren per gebruiker

Slash-commando's schrijven lokale overschrijvingen naar `prefsPath`. De standaardwaarde is `~/.openclaw/settings/tts.json`; overschrijf deze met de env-var `OPENCLAW_TTS_PREFS` of `messages.tts.prefsPath`.

Opgeslagen veld | Effect  
---|---  
`auto` | Lokale auto-TTS-overschrijving (`always`, `off`, …)  
`provider` | Lokale primaire provideroverride  
`persona` | Lokale persona-override  
`maxLength` | Samenvattingsdrempel (standaard `1500` tekens)  
`summarize` | Samenvattingsschakelaar (standaard `true`)  
  
Deze overschrijven de effectieve configuratie uit `messages.tts` plus het actieve `agents.list[].tts`-blok voor die host.

## Uitvoerformaten (vast)

TTS-stemlevering wordt gestuurd door kanaalcapaciteiten. Kanaalplugins adverteren of spraakachtige TTS providers moet vragen om een native `voice-note`-doel of normale `audio-file`-synthese moet behouden en alleen compatibele uitvoer voor spraaklevering moet markeren.

  * **Kanalen met spraaknotitie-ondersteuning** : antwoorden als spraaknotitie geven de voorkeur aan Opus (`opus_48000_64` van ElevenLabs, `opus` van OpenAI). 
    * 48 kHz / 64 kbps is een goede afweging voor spraakberichten.
  * **Feishu / WhatsApp** : wanneer een antwoord als spraaknotitie wordt geproduceerd als MP3/WebM/WAV/M4A of een ander waarschijnlijk audiobestand, transcodeert de channel plugin dit naar 48 kHz Ogg/Opus met `ffmpeg` voordat het native spraakbericht wordt verzonden. WhatsApp verzendt het resultaat via de Baileys-`audio`-payload met `ptt: true` en `audio/ogg; codecs=opus`. Als conversie mislukt, ontvangt Feishu het oorspronkelijke bestand als bijlage; verzenden via WhatsApp mislukt in plaats van een incompatibele PTT-payload te plaatsen.
  * **Andere kanalen** : MP3 (`mp3_44100_128` van ElevenLabs, `mp3` van OpenAI). 
    * 44,1 kHz / 128 kbps is de standaardbalans voor spraakhelderheid.
  * **MiniMax** : MP3 (`speech-2.8-hd`-model, samplefrequentie van 32 kHz) voor normale audiobijlagen. Voor door het kanaal aangekondigde spraaknotitie-doelen transcodeert OpenClaw de MiniMax-MP3 naar 48 kHz Opus met `ffmpeg` vóór levering wanneer het kanaal transcoding aankondigt.
  * **Xiaomi MiMo** : standaard MP3, of WAV wanneer geconfigureerd. Voor door het kanaal aangekondigde spraaknotitie-doelen transcodeert OpenClaw Xiaomi-uitvoer naar 48 kHz Opus met `ffmpeg` vóór levering wanneer het kanaal transcoding aankondigt.
  * **Lokale CLI** : gebruikt de geconfigureerde `outputFormat`. Spraaknotitie-doelen worden geconverteerd naar Ogg/Opus en telefonie-uitvoer wordt geconverteerd naar ruwe 16 kHz mono PCM met `ffmpeg`.
  * **Google Gemini** : Gemini API TTS retourneert ruwe 24 kHz PCM. OpenClaw verpakt dit als WAV voor audiobijlagen, transcodeert het naar 48 kHz Opus voor spraaknotitie-doelen en retourneert PCM rechtstreeks voor Talk/telefonie.
  * **Gradium** : WAV voor audiobijlagen, Opus voor spraaknotitie-doelen, en `ulaw_8000` op 8 kHz voor telefonie.
  * **Inworld** : MP3 voor normale audiobijlagen, native `OGG_OPUS` voor spraaknotitie-doelen, en ruwe `PCM` op 22050 Hz voor Talk/telefonie.
  * **xAI** : standaard MP3; `responseFormat` kan `mp3`, `wav`, `pcm`, `mulaw` of `alaw` zijn. OpenClaw gebruikt xAI's batch REST TTS-eindpunt en retourneert een volledige audiobijlage; xAI's streaming TTS WebSocket wordt niet gebruikt door dit providerpad. Native Opus-spraaknotitieformaat wordt niet ondersteund door dit pad.
  * **Microsoft** : gebruikt `microsoft.outputFormat` (standaard `audio-24khz-48kbitrate-mono-mp3`). 
    * Het meegeleverde transport accepteert een `outputFormat`, maar niet alle formaten zijn beschikbaar via de service.
    * Uitvoerformaatwaarden volgen Microsoft Speech-uitvoerformaten (inclusief Ogg/WebM Opus).
    * Telegram `sendVoice` accepteert OGG/MP3/M4A; gebruik OpenAI/ElevenLabs als je gegarandeerde Opus-spraakberichten nodig hebt.
    * Als het geconfigureerde Microsoft-uitvoerformaat mislukt, probeert OpenClaw het opnieuw met MP3.


OpenAI/ElevenLabs-uitvoerformaten zijn per kanaal vastgelegd (zie hierboven).

## Auto-TTS-gedrag

Wanneer `messages.tts.auto` is ingeschakeld, doet OpenClaw het volgende:

  * Slaat TTS over als het antwoord al media of een `MEDIA:`-directive bevat.
  * Slaat zeer korte antwoorden over (minder dan 10 tekens).
  * Vat lange antwoorden samen wanneer samenvattingen zijn ingeschakeld, met `summaryModel` (of `agents.defaults.model.primary`).
  * Voegt de gegenereerde audio toe aan het antwoord.
  * In `mode: "final"` wordt nog steeds audio-only TTS verzonden voor gestreamde eindantwoorden nadat de tekststream is voltooid; de gegenereerde media gaat door dezelfde kanaalmedianormalisatie als normale antwoordbijlagen.


Als het antwoord `maxLength` overschrijdt en samenvatting is uitgeschakeld (of er geen API-sleutel is voor het samenvattingsmodel), wordt audio overgeslagen en wordt het normale tekstantwoord verzonden.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Uitvoerformaten per kanaal

Doel | Formaat  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Antwoorden als spraaknotitie geven de voorkeur aan **Opus** (`opus_48000_64` van ElevenLabs, `opus` van OpenAI). 48 kHz / 64 kbps brengt helderheid en grootte in balans.  
Andere kanalen | **MP3** (`mp3_44100_128` van ElevenLabs, `mp3` van OpenAI). 44,1 kHz / 128 kbps standaard voor spraak.  
Talk / telefonie | Provider-native **PCM** (Inworld 22050 Hz, Google 24 kHz), of `ulaw_8000` van Gradium voor telefonie.  
  
Opmerkingen per provider:

  * **Feishu / WhatsApp-transcoding:** Wanneer een antwoord als spraaknotitie binnenkomt als MP3/WebM/WAV/M4A, transcodeert de channel plugin naar 48 kHz Ogg/Opus met `ffmpeg`. WhatsApp verzendt via Baileys met `ptt: true` en `audio/ogg; codecs=opus`. Als conversie mislukt: Feishu valt terug op het bijvoegen van het oorspronkelijke bestand; verzenden via WhatsApp mislukt in plaats van een incompatibele PTT-payload te plaatsen.
  * **MiniMax / Xiaomi MiMo:** Standaard MP3 (32 kHz voor MiniMax `speech-2.8-hd`); getranscodeerd naar 48 kHz Opus voor spraaknotitie-doelen via `ffmpeg`.
  * **Lokale CLI:** Gebruikt geconfigureerde `outputFormat`. Spraaknotitie-doelen worden geconverteerd naar Ogg/Opus en telefonie-uitvoer naar ruwe 16 kHz mono PCM.
  * **Google Gemini:** Retourneert ruwe 24 kHz PCM. OpenClaw verpakt dit als WAV voor bijlagen, transcodeert naar 48 kHz Opus voor spraaknotitie-doelen, retourneert PCM rechtstreeks voor Talk/telefonie.
  * **Inworld:** MP3-bijlagen, native `OGG_OPUS`-spraaknotitie, ruwe `PCM` 22050 Hz voor Talk/telefonie.
  * **xAI:** Standaard MP3; `responseFormat` kan `mp3|wav|pcm|mulaw|alaw` zijn. Gebruikt xAI's batch REST-eindpunt — streaming WebSocket TTS wordt **niet** gebruikt. Native Opus-spraaknotitieformaat wordt **niet** ondersteund.
  * **Microsoft:** Gebruikt `microsoft.outputFormat` (standaard `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice` accepteert OGG/MP3/M4A; gebruik OpenAI/ElevenLabs als je gegarandeerde Opus-spraakberichten nodig hebt. Als het geconfigureerde Microsoft-formaat mislukt, probeert OpenClaw het opnieuw met MP3.


OpenAI- en ElevenLabs-uitvoerformaten zijn per kanaal vastgelegd zoals hierboven vermeld.

## Veldreferentie

Top-level messages.tts.*

Auto-TTS-modus. `inbound` verzendt alleen audio na een inkomend spraakbericht; `tagged` verzendt alleen audio wanneer het antwoord `[[tts:...]]`-directives of een `[[tts:text]]`-blok bevat.

Verouderde schakelaar. `openclaw doctor --fix` migreert dit naar `auto`.

`"all"` omvat tool-/blokantwoorden naast eindantwoorden.

Spraakprovider-id. Wanneer niet ingesteld, gebruikt OpenClaw de eerste geconfigureerde provider in de registry-autoselectievolgorde. Verouderde `provider: "edge"` wordt door `openclaw doctor --fix` herschreven naar `"microsoft"`.

Actieve persona-id uit `personas`. Genormaliseerd naar kleine letters.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Stabiele gesproken identiteit. Velden: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Zie Persona's.

Goedkoop model voor automatische samenvatting; standaard `agents.defaults.model.primary`. Accepteert `provider/model` of een geconfigureerde modelalias.

Sta toe dat het model TTS-directives uitzendt. `enabled` is standaard `true`; `allowProvider` is standaard `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Provider-eigen instellingen, gesleuteld op spraakprovider-id. Verouderde directe blokken (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) worden door `openclaw doctor --fix` herschreven; commit alleen `messages.tts.providers.<id>`.

Harde limiet voor TTS-invoertekens. `/tts audio` mislukt als deze wordt overschreden.

Aanvraagtime-out in milliseconden.

Overschrijf het lokale prefs-JSON-pad (provider/limiet/samenvatting). Standaard `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, of `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Azure Speech-regio (bijv. `eastus`). Env: `AZURE_SPEECH_REGION` of `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Optionele Azure Speech-eindpunt-override (alias `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Azure-stem ShortName. Standaard `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI SSML-taalcode. Standaard `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` voor standaardaudio. Standaard `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` voor spraaknotitie-uitvoer. Standaard `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Valt terug op `ELEVENLABS_API_KEY` of `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Model-id (bijv. `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (elk `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normaal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2-letterige ISO 639-1 (bijv. `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Integer `0..4294967295` voor best-effort determinisme. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Valt terug op `GEMINI_API_KEY` / `GOOGLE_API_KEY`. Indien weggelaten, kan TTS `models.providers.google.apiKey` hergebruiken vóór env-terugval. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Gemini TTS-model. Standaard `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Gemini vooraf gebouwde stemnaam. Standaard `Kore`. Alias: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Stel in op `audio-profile-v1` om actieve persona-promptvelden in een deterministische Gemini TTS-promptstructuur te verpakken. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Alleen `https://generativelanguage.googleapis.com` wordt geaccepteerd. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standaard `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standaard Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Primaire Inworld

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standaard `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Standaard `inworld-tts-1.5-max`. Ook: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standaard `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Samplingtemperatuur `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Lokale CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Opdrachtargumenten. Ondersteunt tijdelijke aanduidingen `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Verwachte CLI-uitvoerindeling. Standaard `mp3` voor audiobijlagen. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Time-out voor opdracht in milliseconden. Standaard `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (geen API-sleutel)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Naam van Microsoft neural voice (bijv. `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Taalcode (bijv. `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Microsoft-uitvoerindeling. Standaard `audio-24khz-48kbitrate-mono-mp3`. Niet alle indelingen worden ondersteund door het gebundelde Edge-backed transport. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Percentagereeksen (bijv. `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Verouderde alias. Voer `openclaw doctor --fix` uit om opgeslagen configuratie te herschrijven naar `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Valt terug op `MINIMAX_API_KEY`. Token Plan-authenticatie via `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` of `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standaard `https://api.minimax.io`. Env: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Standaard `speech-2.8-hd`. Env: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standaard `English_expressive_narrator`. Env: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Standaard `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Standaard `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Geheel getal `-12..12`. Standaard `0`. Fractionele waarden worden vóór de aanvraag afgekapt. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Valt terug op `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci OpenAI TTS-model-id (bijv. `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Stemnaam (bijv. `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Expliciet OpenAI-veld `instructions`. Wanneer ingesteld, worden personapromptvelden **niet** automatisch toegewezen. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Extra JSON-velden die worden samengevoegd in `/audio/speech`-aanvraagbody's na gegenereerde OpenAI TTS-velden. Gebruik dit voor OpenAI-compatibele endpoints zoals Kokoro die providerspecifieke sleutels zoals `lang` vereisen; onveilige prototypesleutels worden genegeerd. OPENCLAW_DOCS_MARKER:paramClose:

Overschrijf het OpenAI TTS-endpoint. Resolutievolgorde: configuratie → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Niet-standaardwaarden worden behandeld als OpenAI-compatibele TTS-endpoints, dus aangepaste model- en stemnamen worden geaccepteerd.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `OPENROUTER_API_KEY`. Kan `models.providers.openrouter.apiKey` hergebruiken. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standaard `https://openrouter.ai/api/v1`. Verouderde `https://openrouter.ai/v1` wordt genormaliseerd. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Standaard `hexgrad/kokoro-82m`. Alias: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Standaard `af_alloy`. Alias: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Standaard `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `VOLCENGINE_TTS_API_KEY` of `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Standaard `seed-tts-1.0`. Env: `VOLCENGINE_TTS_RESOURCE_ID`. Gebruik `seed-tts-2.0` wanneer je project TTS 2.0-rechten heeft. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg App-key-header. Standaard `aGjiRDfUWi`. Env: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Overschrijf het Seed Speech TTS HTTP-endpoint. Env: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Stemtype. Standaard `en_female_anna_mars_bigtts`. Env: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Verouderde Volcengine Speech Console-velden. Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (standaard `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standaard `https://api.x.ai/v1`. Env: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standaard `eve`. Live stemmen: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci BCP-47-taalcode of `auto`. Standaard `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Standaard `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standaard `https://api.xiaomimimo.com/v1`. Env: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Standaard `mimo-v2.5-tts`. Env: `XIAOMI_TTS_MODEL`. Ondersteunt ook `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Standaard `mimo_default`. Env: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Standaard `mp3`. Env: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Agent-tool

De tool `tts` zet tekst om naar spraak en retourneert een audiobijlage voor antwoordbezorging. Op Feishu, Matrix, Telegram en WhatsApp wordt de audio geleverd als een spraakbericht in plaats van als bestandsbijlage. Feishu en WhatsApp kunnen niet-Opus TTS-uitvoer op dit pad transcoderen wanneer `ffmpeg` beschikbaar is.

WhatsApp verzendt audio via Baileys als een PTT-spraaknotitie (`audio` met `ptt: true`) en verzendt zichtbare tekst **afzonderlijk** van PTT-audio omdat clients bijschriften bij spraaknotities niet consequent weergeven.

De tool accepteert optionele velden `channel` en `timeoutMs`; `timeoutMs` is een provider-aanvraagtime-out per aanroep in milliseconden.

## Gateway RPC

Methode | Doel  
---|---  
`tts.status` | Lees de huidige TTS-status en laatste poging.  
`tts.enable` | Stel lokale automatische voorkeur in op `always`.  
`tts.disable` | Stel lokale automatische voorkeur in op `off`.  
`tts.convert` | Eenmalige tekst → audio.  
`tts.setProvider` | Stel lokale providervoorkeur in.  
`tts.setPersona` | Stel lokale personavoorkeur in.  
`tts.providers` | Toon geconfigureerde providers en status.  
  
## Servicelinks

  * [OpenAI-gids voor tekst-naar-spraak](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [OpenAI Audio API-referentie](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST tekst-naar-spraak](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Azure Speech-provider](</nl/providers/azure-speech>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [ElevenLabs Authentication](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</nl/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</nl/providers/volcengine#text-to-speech>)
  * [Xiaomi MiMo-spraaksynthese](</nl/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Microsoft Speech-uitvoerindelingen](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [xAI tekst-naar-spraak](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Gerelateerd

  * [Media-overzicht](</nl/tools/media-overview>)
  * [Muziekgeneratie](</nl/tools/music-generation>)
  * [Videogeneratie](</nl/tools/video-generation>)
  * [Slash-opdrachten](</nl/tools/slash-commands>)
  * [Plugin voor spraakoproepen](</nl/plugins/voice-call>)


Was this useful?YesNo
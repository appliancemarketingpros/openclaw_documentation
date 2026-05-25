---
title: Inworld
source_url: https://docs.openclaw.ai/nl/providers/inworld
scraped_at: 2026-05-25
---

Inworld is een provider voor streaming tekst-naar-spraak (TTS). In OpenClaw synthetiseert het uitgaande antwoordaudio (standaard MP3, OGG_OPUS voor spraaknotities) en PCM-audio voor telefoniekanalen zoals Voice Call.

OpenClaw post naar het streaming TTS-eindpunt van Inworld, voegt de geretourneerde base64-audiochunks samen tot één buffer, en geeft het resultaat door aan de standaard pijplijn voor antwoordaudio.

Eigenschap | Waarde  
---|---  
Provider-id | `inworld`  
Plugin | meegeleverd, `enabledByDefault: true`  
Contract | `speechProviders` (alleen TTS)  
Auth-env-var | `INWORLD_API_KEY` (HTTP Basic, Base64-dashboardreferentie)  
Basis-URL | `https://api.inworld.ai`  
Standaardstem | `Sarah`  
Standaardmodel | `inworld-tts-1.5-max`  
Uitvoer | MP3 (standaard), OGG_OPUS (spraaknotities), PCM 22050 Hz (telefonie)  
Website | [inworld.ai](<https://inworld.ai>)  
Docs | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Aan de slag

* ### Stel je API-sleutel in

Kopieer de referentie uit je Inworld-dashboard (Workspace > API Keys) en stel deze in als env-var. De waarde wordt letterlijk verzonden als de HTTP Basic- referentie, dus codeer deze niet opnieuw met Base64 en converteer deze niet naar een bearer- token.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### Selecteer Inworld in messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Stuur een bericht

Stuur een antwoord via een verbonden kanaal. OpenClaw synthetiseert de audio met Inworld en levert deze als MP3 (of OGG_OPUS wanneer het kanaal een spraaknotitie verwacht).

## Configuratieopties

Optie | Pad | Beschrijving  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Base64-dashboardreferentie. Valt terug op `INWORLD_API_KEY`.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Overschrijf de basis-URL van de Inworld-API (standaard `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Stem-ID (standaard `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | TTS-model-id (standaard `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Samplingtemperatuur `0..2` (optioneel).  
  
## Opmerkingen

Authenticatie

Inworld gebruikt HTTP Basic-authenticatie met één Base64-gecodeerde referentie- tekenreeks. Kopieer deze letterlijk uit het Inworld-dashboard. De provider verzendt deze als `Authorization: Basic <apiKey>` zonder verdere codering, dus codeer deze niet zelf met Base64 en geef geen bearer-achtig token door. Zie [TTS-authenticatieopmerkingen](</nl/tools/tts#inworld-primary>) voor dezelfde toelichting.

Modellen

Ondersteunde model-id's: `inworld-tts-1.5-max` (standaard), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Audio-uitvoer

Antwoorden gebruiken standaard MP3. Wanneer het kanaaldoel `voice-note` is, vraagt OpenClaw Inworld om `OGG_OPUS` zodat de audio wordt afgespeeld als een native spraakballon. Telefoniesynthese gebruikt ruwe `PCM` op 22050 Hz om de telefoniebrug te voeden.

Aangepaste eindpunten

Overschrijf de API-host met `messages.tts.providers.inworld.baseUrl`. Afsluitende slashes worden verwijderd voordat verzoeken worden verzonden.

## Gerelateerd

[**Tekst-naar-spraak** TTS-overzicht, providers en `messages.tts`-configuratie. ](</nl/tools/tts>) [**Configuratie** Volledige configuratiereferentie inclusief `messages.tts`-instellingen. ](</nl/gateway/configuration>) [**Providers** Alle meegeleverde OpenClaw-providers. ](</nl/providers>) [**Probleemoplossing** Veelvoorkomende problemen en foutopsporingsstappen. ](</nl/help/troubleshooting>)

Was this useful?YesNo
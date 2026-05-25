---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/nl/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo is het API-platform voor **MiMo** -modellen. OpenClaw bevat een gebundelde `xiaomi`-Plugin die zowel een OpenAI-compatibele chatprovider als een spraakprovider (TTS) registreert met dezelfde `XIAOMI_API_KEY`.

Eigenschap | Waarde  
---|---  
Provider-id | `xiaomi`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `XIAOMI_API_KEY`  
Onboarding-vlag | `--auth-choice xiaomi-api-key`  
Directe CLI-vlag | `--xiaomi-api-key <key>`  
Contracten | chataanvullingen + `speechProviders`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.xiaomimimo.com/v1`  
Standaardmodel | `xiaomi/mimo-v2-flash`  
TTS-standaard | `mimo-v2.5-tts`, stem `mimo_default`  
  
## Aan de slag

* ### Een API-sleutel ophalen

Maak een API-sleutel aan in de [Xiaomi MiMo-console](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Of geef de sleutel direct door:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Ingebouwde catalogus

Model-ref | Invoer | Context | Max. uitvoer | Redeneren | Opmerkingen  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | tekst | 262,144 | 8,192 | Nee | Standaardmodel  
`xiaomi/mimo-v2-pro` | tekst | 1,048,576 | 32,000 | Ja | Grote context  
`xiaomi/mimo-v2-omni` | tekst, afbeelding | 262,144 | 32,000 | Ja | Multimodaal  
  
## Tekst-naar-spraak

De gebundelde `xiaomi`-Plugin registreert Xiaomi MiMo ook als spraakprovider voor `messages.tts`. Deze roept Xiaomi's TTS-contract voor chataanvullingen aan met de tekst als een `assistant`-bericht en optionele stijlinstructies als een `user`-bericht.

Eigenschap | Waarde  
---|---  
TTS-id | `xiaomi` (`mimo`-alias)  
Auth | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` met `audio`  
Standaard | `mimo-v2.5-tts`, stem `mimo_default`  
Uitvoer | standaard MP3; WAV wanneer geconfigureerd  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Ondersteunde ingebouwde stemmen zijn onder andere `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` en `Dean`. `mimo-v2-tts` wordt ondersteund voor oudere MiMo TTS-accounts; de standaard gebruikt het huidige MiMo-V2.5 TTS-model. Voor voice-note- doelen zoals Feishu en Telegram transcodeert OpenClaw Xiaomi-uitvoer naar 48kHz Opus met `ffmpeg` vóór levering.

## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Gedrag voor automatische injectie

De `xiaomi`-provider wordt automatisch geïnjecteerd wanneer `XIAOMI_API_KEY` in je omgeving is ingesteld of wanneer er een auth-profiel bestaat. Je hoeft de provider niet handmatig te configureren, tenzij je modelmetadata of de basis-URL wilt overschrijven.

Modeldetails

  * **mimo-v2-flash** — lichtgewicht en snel, ideaal voor algemene teksttaken. Geen ondersteuning voor redeneren.
  * **mimo-v2-pro** — ondersteunt redeneren met een contextvenster van 1M tokens voor workloads met lange documenten.
  * **mimo-v2-omni** — multimodaal model met redeneren dat zowel tekst- als afbeeldingsinvoer accepteert.

Probleemoplossing

  * Als modellen niet verschijnen, controleer dan of `XIAOMI_API_KEY` is ingesteld en geldig is.
  * Wanneer de Gateway als daemon draait, zorg er dan voor dat de sleutel beschikbaar is voor dat proces (bijvoorbeeld in `~/.openclaw/.env` of via `env.shellEnv`).


## Gerelateerd

[**Modelselectie** Providers, model-refs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledige OpenClaw-configuratiereferentie. ](</nl/gateway/configuration-reference>) [**Xiaomi MiMo-console** Xiaomi MiMo-dashboard en API-sleutelbeheer. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo
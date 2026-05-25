---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/it/providers/volcengine
scraped_at: 2026-05-25
---

Il provider Volcengine offre accesso ai modelli Doubao e ai modelli di terze parti ospitati su Volcano Engine, con endpoint separati per i carichi di lavoro generali e di coding. Lo stesso Plugin incluso può anche registrare Volcengine Speech come provider TTS.

Dettaglio | Valore  
---|---  
Provider | `volcengine` (generale + TTS) + `volcengine-plan` (coding)  
Autenticazione modello | `VOLCANO_ENGINE_API_KEY`  
Autenticazione TTS | `VOLCENGINE_TTS_API_KEY` o `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | Modelli compatibili con OpenAI, TTS BytePlus Seed Speech  
  
## Per iniziare

* ### Imposta la chiave API

Esegui l'onboarding interattivo:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Questo registra sia il provider generale (`volcengine`) sia quello di coding (`volcengine-plan`) a partire da una singola chiave API.

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Provider ed endpoint

Provider | Endpoint | Caso d'uso  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Modelli generali  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Modelli di coding  
  
## Catalogo integrato

### Generale (volcengine)

Model ref | Nome | Input | Contesto  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | testo, immagine | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | testo, immagine | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | testo, immagine | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | testo, immagine | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | testo, immagine | 128,000  
  
### Coding (volcengine-plan)

Model ref | Nome | Input | Contesto  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | testo | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | testo | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | testo | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | testo | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | testo | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | testo | 256,000  
  
## Sintesi vocale

Il TTS di Volcengine usa l'API HTTP BytePlus Seed Speech ed è configurato separatamente dalla chiave API dei modelli Doubao compatibili con OpenAI. Nella console BytePlus, apri Seed Speech > Settings > API Keys e copia la chiave API, quindi imposta:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Poi abilitalo in `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Per le destinazioni con note vocali, OpenClaw richiede a Volcengine il formato nativo del provider `ogg_opus`. Per i normali allegati audio, richiede `mp3`. Anche gli alias del provider `bytedance` e `doubao` vengono risolti nello stesso provider vocale.

L'ID risorsa predefinito è `seed-tts-1.0` perché è quello che BytePlus assegna alle chiavi API Seed Speech appena create nel progetto predefinito. Se il tuo progetto ha l'abilitazione TTS 2.0, imposta `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

L'autenticazione legacy AppID/token resta supportata per le applicazioni meno recenti della Speech Console:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Configurazione avanzata

Modello predefinito dopo l'onboarding

`openclaw onboard --auth-choice volcengine-api-key` attualmente imposta `volcengine-plan/ark-code-latest` come modello predefinito registrando anche il catalogo generale `volcengine`.

Comportamento di fallback del selettore del modello

Durante l'onboarding/configurazione della selezione del modello, la scelta di autenticazione Volcengine privilegia sia le righe `volcengine/*` sia `volcengine-plan/*`. Se questi modelli non sono ancora caricati, OpenClaw ripiega sul catalogo non filtrato invece di mostrare un selettore limitato al provider vuoto.

Variabili d'ambiente per i processi daemon

Se il Gateway viene eseguito come daemon (launchd/systemd), assicurati che le variabili d'ambiente del modello e del TTS come `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` e `VOLCENGINE_TTS_TOKEN` siano disponibili per quel processo (per esempio, in `~/.openclaw/.env` o tramite `env.shellEnv`).

## Correlati

[**Selezione del modello** Scelta dei provider, dei model ref e del comportamento di failover. ](</it/concepts/model-providers>) [**Configurazione** Riferimento completo della configurazione per agenti, modelli e provider. ](</it/gateway/configuration>) [**Risoluzione dei problemi** Problemi comuni e passaggi di debug. ](</it/help/troubleshooting>) [**FAQ** Domande frequenti sulla configurazione di OpenClaw. ](</it/help/faq>)

Was this useful?YesNo
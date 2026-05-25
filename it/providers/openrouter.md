---
title: OpenRouter
source_url: https://docs.openclaw.ai/it/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter fornisce un'**API unificata** che instrada le richieste a molti modelli dietro un unico endpoint e una chiave API. È compatibile con OpenAI, quindi la maggior parte degli SDK OpenAI funziona cambiando l'URL di base.

## Primi passi

* ### Ottieni la tua chiave API

Crea una chiave API su [openrouter.ai/keys](<https://openrouter.ai/keys>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Facoltativo) Passa a un modello specifico

L'onboarding usa per impostazione predefinita `openrouter/auto`. Scegli un modello concreto in seguito:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Esempio di configurazione

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Riferimenti dei modelli

Esempi di fallback inclusi:

Riferimento modello | Note  
---|---  
`openrouter/auto` | Instradamento automatico OpenRouter  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 tramite MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 tramite MoonshotAI  
  
## Generazione di immagini

OpenRouter può anche supportare lo strumento `image_generate`. Usa un modello di immagini OpenRouter in `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw invia le richieste di immagini all'API di completamenti chat per immagini di OpenRouter con `modalities: ["image", "text"]`. I modelli di immagini Gemini ricevono suggerimenti supportati per `aspectRatio` e `resolution` tramite `image_config` di OpenRouter. Usa `agents.defaults.imageGenerationModel.timeoutMs` per i modelli di immagini OpenRouter più lenti; il parametro per chiamata `timeoutMs` dello strumento `image_generate` ha comunque la precedenza.

## Generazione video

OpenRouter può anche supportare lo strumento `video_generate` tramite la sua API asincrona `/videos`. Usa un modello video OpenRouter in `agents.defaults.videoGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw invia job text-to-video e image-to-video a OpenRouter, interroga il `polling_url` restituito e scarica il video completato da `unsigned_urls` di OpenRouter o dall'endpoint del contenuto del job documentato. Le immagini di riferimento vengono inviate per impostazione predefinita come immagini del primo/ultimo frame; le immagini contrassegnate con `reference_image` vengono inviate come riferimenti di input OpenRouter. Il valore predefinito incluso `google/veo-3.1-fast` dichiara le durate attualmente supportate di 4/6/8 secondi, le risoluzioni `720P`/`1080P` e i rapporti d'aspetto `16:9`/`9:16`. Video-to-video non è registrato per OpenRouter perché l'API upstream di generazione video attualmente accetta testo e riferimenti di immagini.

## Sintesi vocale

OpenRouter può essere usato anche come provider TTS tramite il suo endpoint compatibile con OpenAI `/audio/speech`.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

Se `messages.tts.providers.openrouter.apiKey` viene omesso, TTS riusa `models.providers.openrouter.apiKey`, quindi `OPENROUTER_API_KEY`.

## Riconoscimento vocale (audio in ingresso)

OpenRouter può trascrivere allegati voce/audio in ingresso tramite il percorso condiviso `tools.media.audio` usando il suo endpoint STT (`/audio/transcriptions`). Questo si applica a qualsiasi Plugin di canale che inoltra voce/audio in ingresso al preflight di comprensione multimediale.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw invia le richieste STT a OpenRouter come JSON con audio base64 in `input_audio` (contratto STT di OpenRouter), non come caricamenti multipart di moduli OpenAI.

## Autenticazione e header

OpenRouter usa internamente un token Bearer con la tua chiave API.

Nelle richieste OpenRouter reali (`https://openrouter.ai/api/v1`), OpenClaw aggiunge anche gli header documentati di attribuzione dell'app di OpenRouter:

Header | Valore  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Configurazione avanzata

Cache delle risposte

La cache delle risposte OpenRouter è opt-in. Abilitala per singolo modello OpenRouter con i parametri del modello:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw invia `X-OpenRouter-Cache: true` e, quando configurato, `X-OpenRouter-Cache-TTL`. `responseCacheClear: true` forza un aggiornamento per la richiesta corrente e archivia la risposta sostitutiva. Sono accettati anche gli alias snake_case (`response_cache`, `response_cache_ttl_seconds` e `response_cache_clear`).

Questo è separato dalla cache dei prompt del provider e dai marker Anthropic `cache_control` di OpenRouter. Viene applicato solo su route `openrouter.ai` verificate, non su URL di base di proxy personalizzati.

Marker della cache Anthropic

Sulle route OpenRouter verificate, i riferimenti ai modelli Anthropic mantengono i marker Anthropic `cache_control` specifici di OpenRouter che OpenClaw usa per migliorare il riutilizzo della cache dei prompt sui blocchi di prompt di sistema/sviluppatore.

Prefill del reasoning Anthropic

Sulle route OpenRouter verificate, i riferimenti ai modelli Anthropic con reasoning abilitato rimuovono i turni finali di prefill dell'assistente prima che la richiesta raggiunga OpenRouter, rispettando il requisito di Anthropic per cui le conversazioni con reasoning terminino con un turno utente.

Iniezione di pensiero / reasoning

Sulle route non `auto` supportate, OpenClaw mappa il livello di pensiero selezionato sui payload di reasoning del proxy OpenRouter. Gli hint di modello non supportati e `openrouter/auto` saltano quell'iniezione di reasoning. Hunter Alpha salta anche il reasoning del proxy per riferimenti di modello configurati obsoleti perché OpenRouter potrebbe restituire testo della risposta finale nei campi di reasoning per quella route ritirata.

Replay del reasoning DeepSeek V4

Sulle route OpenRouter verificate, `openrouter/deepseek/deepseek-v4-flash` e `openrouter/deepseek/deepseek-v4-pro` compilano il `reasoning_content` mancante nei turni assistente riprodotti, così le conversazioni di pensiero/strumenti mantengono la forma di follow-up richiesta da DeepSeek V4. OpenClaw invia valori `reasoning_effort` supportati da OpenRouter per queste route; `xhigh` è il livello pubblicizzato più alto e gli override obsoleti `max` vengono mappati a `xhigh`.

Modellazione delle richieste solo OpenAI

OpenRouter passa comunque attraverso il percorso in stile proxy compatibile con OpenAI, quindi la modellazione delle richieste nativa solo OpenAI come `serviceTier`, Responses `store`, payload di compatibilità del reasoning OpenAI e hint della cache dei prompt non viene inoltrata.

Route basate su Gemini

I riferimenti OpenRouter basati su Gemini restano sul percorso proxy-Gemini: OpenClaw mantiene lì la sanificazione della firma di pensiero Gemini, ma non abilita la validazione nativa del replay Gemini né le riscritture di bootstrap.

Metadati di instradamento del provider

Se passi l'instradamento provider OpenRouter nei parametri del modello, OpenClaw lo inoltra come metadati di instradamento OpenRouter prima che vengano eseguiti i wrapper di stream condivisi.

## Correlati

[**Selezione del modello** Scelta di provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento di configurazione** Riferimento completo alla configurazione per agenti, modelli e provider. ](</it/gateway/configuration-reference>)

Was this useful?YesNo
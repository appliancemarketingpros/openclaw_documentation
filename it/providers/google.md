---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/it/providers/google
scraped_at: 2026-05-25
---

Il plugin Google fornisce accesso ai modelli Gemini tramite Google AI Studio, oltre a generazione di immagini, comprensione dei media (immagini/audio/video), sintesi vocale e ricerca web tramite Gemini Grounding.

  * Provider: `google`
  * Autenticazione: `GEMINI_API_KEY` o `GOOGLE_API_KEY`
  * API: API Google Gemini
  * Opzione di runtime: provider/modello `agentRuntime.id: "google-gemini-cli"` riutilizza l'OAuth della Gemini CLI mantenendo i riferimenti ai modelli canonici come `google/*`.


## Per iniziare

Scegli il metodo di autenticazione preferito e segui i passaggi di configurazione.

### Chiave API

**Ideale per:** accesso standard all'API Gemini tramite Google AI Studio.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Oppure passa direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Ideale per:** riutilizzare un accesso Gemini CLI esistente tramite PKCE OAuth invece di una chiave API separata.

* ### Installa la Gemini CLI

Il comando locale `gemini` deve essere disponibile in `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw supporta sia installazioni Homebrew sia installazioni globali npm, inclusi i layout Windows/npm comuni.

* ### Accedi tramite OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Modello predefinito: `google/gemini-3.1-pro-preview`
  * Runtime: `google-gemini-cli`
  * Alias: `gemini-cli`


L'id del modello Gemini API di Gemini 3.1 Pro è `gemini-3.1-pro-preview`. OpenClaw accetta la forma più breve `google/gemini-3.1-pro` come alias di comodità e la normalizza prima delle chiamate al provider.

**Variabili d'ambiente:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Oppure le varianti `GEMINI_CLI_*`.)

I riferimenti ai modelli `google-gemini-cli/*` sono alias di compatibilità legacy. Le nuove configurazioni dovrebbero usare riferimenti ai modelli `google/*` più il runtime `google-gemini-cli` quando vogliono l'esecuzione locale tramite Gemini CLI.

## Funzionalità

Funzionalità | Supportata  
---|---  
Completamenti chat | Sì  
Generazione di immagini | Sì  
Generazione musicale | Sì  
Sintesi vocale | Sì  
Voce in tempo reale | Sì (Google Live API)  
Comprensione delle immagini | Sì  
Trascrizione audio | Sì  
Comprensione dei video | Sì  
Ricerca web (Grounding) | Sì  
Pensiero/ragionamento | Sì (Gemini 2.5+ / Gemini 3+)  
Modelli Gemma 4 | Sì  
  
## Ricerca web

Il provider di ricerca web `gemini` incluso usa il grounding di Google Search di Gemini. Configura una chiave di ricerca dedicata in `plugins.entries.google.config.webSearch`, oppure lascia che riutilizzi `models.providers.google.apiKey` dopo `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

La precedenza delle credenziali è `webSearch.apiKey` dedicata, poi `GEMINI_API_KEY`, poi `models.providers.google.apiKey`. `webSearch.baseUrl` è facoltativo ed esiste per proxy operatore o endpoint API Gemini compatibili; quando viene omesso, la ricerca web Gemini riutilizza `models.providers.google.baseUrl`. Vedi [Ricerca Gemini](</it/tools/gemini-search>) per il comportamento dello strumento specifico del provider.

## Generazione di immagini

Il provider di generazione di immagini `google` incluso usa come predefinito `google/gemini-3.1-flash-image-preview`.

  * Supporta anche `google/gemini-3-pro-image-preview`
  * Generazione: fino a 4 immagini per richiesta
  * Modalità modifica: abilitata, fino a 5 immagini in input
  * Controlli geometrici: `size`, `aspectRatio` e `resolution`


Per usare Google come provider di immagini predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Generazione video

Il plugin `google` incluso registra anche la generazione video tramite lo strumento condiviso `video_generate`.

  * Modello video predefinito: `google/veo-3.1-fast-generate-preview`
  * Modalità: flussi text-to-video, image-to-video e riferimento a singolo video
  * Supporta `aspectRatio` (`16:9`, `9:16`) e `resolution` (`720P`, `1080P`); l'output audio non è supportato oggi da Veo
  * Durate supportate: **4, 6 o 8 secondi** (gli altri valori vengono arrotondati al valore consentito più vicino)


Per usare Google come provider video predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Generazione musicale

Il plugin `google` incluso registra anche la generazione musicale tramite lo strumento condiviso `music_generate`.

  * Modello musicale predefinito: `google/lyria-3-clip-preview`
  * Supporta anche `google/lyria-3-pro-preview`
  * Controlli del prompt: `lyrics` e `instrumental`
  * Formato di output: `mp3` per impostazione predefinita, più `wav` su `google/lyria-3-pro-preview`
  * Input di riferimento: fino a 10 immagini
  * Le esecuzioni supportate da sessione si distaccano tramite il flusso condiviso attività/stato, incluso `action: "status"`


Per usare Google come provider musicale predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Sintesi vocale

Il provider vocale `google` incluso usa il percorso TTS dell'API Gemini con `gemini-3.1-flash-tts-preview`.

  * Voce predefinita: `Kore`
  * Autenticazione: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` o `GOOGLE_API_KEY`
  * Output: WAV per allegati TTS regolari, Opus per destinazioni di note vocali, PCM per Talk/telefonia
  * Output nota vocale: il PCM Google viene incapsulato come WAV e transcodificato in Opus a 48 kHz con `ffmpeg`


Il percorso batch Gemini TTS di Google restituisce l'audio generato nella risposta `generateContent` completata. Per conversazioni parlate a latenza minima, usa il provider vocale in tempo reale Google basato sulla Gemini Live API invece del TTS batch.

Per usare Google come provider TTS predefinito:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS usa prompt in linguaggio naturale per il controllo dello stile. Imposta `audioProfile` per anteporre un prompt di stile riutilizzabile prima del testo parlato. Imposta `speakerName` quando il testo del prompt fa riferimento a un parlante nominato.

Gemini API TTS accetta anche tag audio espressivi tra parentesi quadre nel testo, come `[whispers]` o `[laughs]`. Per tenere i tag fuori dalla risposta chat visibile mentre li invii al TTS, inseriscili in un blocco `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Voce in tempo reale

Il plugin `google` incluso registra un provider vocale in tempo reale basato sulla Gemini Live API per bridge audio backend come Voice Call e Google Meet.

Impostazione | Percorso configurazione | Predefinito  
---|---|---  
Modello | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Voce | `...google.voice` | `Kore`  
Temperatura | `...google.temperature` | (non impostato)  
Sensibilità di avvio VAD | `...google.startSensitivity` | (non impostato)  
Sensibilità di fine VAD | `...google.endSensitivity` | (non impostato)  
Durata del silenzio | `...google.silenceDurationMs` | (non impostato)  
Gestione dell'attività | `...google.activityHandling` | Predefinito Google, `start-of-activity-interrupts`  
Copertura del turno | `...google.turnCoverage` | Predefinito Google, `only-activity`  
Disabilita VAD automatico | `...google.automaticActivityDetectionDisabled` | `false`  
Ripresa della sessione | `...google.sessionResumption` | `true`  
Compressione del contesto | `...google.contextWindowCompression` | `true`  
Chiave API | `...google.apiKey` | Ripiega su `models.providers.google.apiKey`, `GEMINI_API_KEY` o `GOOGLE_API_KEY`  
  
Esempio di configurazione Voice Call in tempo reale:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Per la verifica live dei maintainer, esegui `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Lo smoke copre anche i percorsi backend/WebRTC di OpenAI; la parte Google emette la stessa forma di token Live API vincolato usata da Control UI Talk, apre l'endpoint WebSocket del browser, invia il payload di configurazione iniziale e attende `setupComplete`.

## Configurazione avanzata

Riutilizzo diretto della cache Gemini

Per le esecuzioni dirette di Gemini API (`api: "google-generative-ai"`), OpenClaw passa un handle `cachedContent` configurato alle richieste Gemini.

  * Configura parametri per modello o globali con `cachedContent` o il legacy `cached_content`
  * Se sono presenti entrambi, `cachedContent` ha la precedenza
  * Valore di esempio: `cachedContents/prebuilt-context`
  * L'utilizzo da cache hit di Gemini viene normalizzato in OpenClaw `cacheRead` da `cachedContentTokenCount` upstream

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Note sull'utilizzo JSON di Gemini CLI

Quando si usa il provider OAuth `google-gemini-cli`, OpenClaw normalizza l'output JSON della CLI come segue:

  * Il testo della risposta proviene dal campo `response` del JSON della CLI.
  * L'utilizzo ripiega su `stats` quando la CLI lascia `usage` vuoto.
  * `stats.cached` viene normalizzato in OpenClaw `cacheRead`.
  * Se `stats.input` manca, OpenClaw deriva i token di input da `stats.input_tokens - stats.cached`.

Ambiente e configurazione del demone

Se il Gateway viene eseguito come demone (launchd/systemd), assicurati che `GEMINI_API_KEY` sia disponibile per quel processo (per esempio in `~/.openclaw/.env` o tramite `env.shellEnv`).

## Correlati

[**Selezione del modello** Scelta dei provider, dei riferimenti ai modelli e del comportamento di failover. ](</it/concepts/model-providers>) [**Generazione di immagini** Parametri dello strumento immagine condiviso e selezione del provider. ](</it/tools/image-generation>) [**Generazione di video** Parametri dello strumento video condiviso e selezione del provider. ](</it/tools/video-generation>) [**Generazione di musica** Parametri dello strumento musica condiviso e selezione del provider. ](</it/tools/music-generation>)

Was this useful?YesNo
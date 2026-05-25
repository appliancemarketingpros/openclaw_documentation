---
title: Panoramica dei media
source_url: https://docs.openclaw.ai/it/tools/media-overview
scraped_at: 2026-05-25
---

OpenClaw genera immagini, video e musica, comprende i media in ingresso (immagini, audio, video) e pronuncia le risposte ad alta voce con la sintesi vocale. Tutte le funzionalità multimediali sono guidate da strumenti: l’agente decide quando usarle in base alla conversazione, e ogni strumento compare solo quando è configurato almeno un provider di supporto.

La voce live usa il contratto di sessione Talk invece del percorso dello strumento multimediale one-shot. Talk ha tre modalità: `realtime` nativa del provider, `stt-tts` locale o in streaming, e `transcription` per l’acquisizione della voce in sola osservazione. Queste modalità condividono cataloghi dei provider, envelope degli eventi e semantiche di annullamento con telefonia, riunioni, browser in tempo reale e client nativi push-to-talk.

## Funzionalità

[**Generazione di immagini** Crea e modifica immagini da prompt testuali o immagini di riferimento tramite `image_generate`. Sincrono: completa inline con la risposta. ](</it/tools/image-generation>) [**Generazione di video** Da testo a video, da immagine a video e da video a video tramite `video_generate`. Asincrono: viene eseguito in background e pubblica il risultato quando è pronto. ](</it/tools/video-generation>) [**Generazione di musica** Genera musica o tracce audio tramite `music_generate`. Asincrono sui provider condivisi; il percorso di workflow ComfyUI viene eseguito in modo sincrono. ](</it/tools/music-generation>) [**Sintesi vocale** Converte le risposte in uscita in audio parlato tramite lo strumento `tts` più la configurazione `messages.tts`. Sincrono. ](</it/tools/tts>) [**Comprensione dei media** Riassume immagini, audio e video in ingresso usando provider di modelli con capacità di visione e plugin dedicati alla comprensione dei media. ](</it/nodes/media-understanding>) [**Trascrizione vocale** Trascrive i messaggi vocali in ingresso tramite STT batch o provider STT in streaming per Voice Call. ](</it/nodes/audio>)

## Matrice delle funzionalità dei provider

Provider | Immagine | Video | Musica | TTS | STT | Voce in tempo reale | Comprensione dei media  
---|---|---|---|---|---|---|---  
Alibaba |  | ✓ |  |  |  |  |   
BytePlus |  | ✓ |  |  |  |  |   
ComfyUI | ✓ | ✓ | ✓ |  |  |  |   
DeepInfra | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Deepgram |  |  |  |  | ✓ | ✓ |   
ElevenLabs |  |  |  | ✓ | ✓ |  |   
fal | ✓ | ✓ |  |  |  |  |   
Google | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓  
Gradium |  |  |  | ✓ |  |  |   
Local CLI |  |  |  | ✓ |  |  |   
Microsoft |  |  |  | ✓ |  |  |   
MiniMax | ✓ | ✓ | ✓ | ✓ |  |  |   
Mistral |  |  |  |  | ✓ |  |   
OpenAI | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓  
OpenRouter | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Qwen |  | ✓ |  |  |  |  |   
Runway |  | ✓ |  |  |  |  |   
SenseAudio |  |  |  |  | ✓ |  |   
Together |  | ✓ |  |  |  |  |   
Vydra | ✓ | ✓ |  | ✓ |  |  |   
xAI | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Xiaomi MiMo | ✓ |  |  | ✓ |  |  | ✓  
  
## Asincrono vs sincrono

Funzionalità | Modalità | Perché  
---|---|---  
Immagine | Sincrona | Le risposte del provider arrivano in pochi secondi; completa inline con la risposta.  
Sintesi vocale | Sincrona | Le risposte del provider arrivano in pochi secondi; vengono allegate all’audio della risposta.  
Video | Asincrona | L’elaborazione del provider richiede da 30 s a diversi minuti; le code lente possono arrivare al timeout configurato.  
Musica (condivisa) | Asincrona | Stessa caratteristica di elaborazione del provider dei video.  
Musica (ComfyUI) | Sincrona | Il workflow locale viene eseguito inline contro il server ComfyUI configurato.  
  
Per gli strumenti asincroni, OpenClaw invia la richiesta al provider, restituisce subito un ID attività e traccia il job nel registro delle attività. L’agente continua a rispondere ad altri messaggi mentre il job è in esecuzione. Quando il provider termina, OpenClaw riattiva l’agente con i percorsi dei media generati, così può informare l’utente e, quando richiesto dalla policy di consegna della sorgente, inoltrare il risultato tramite lo strumento di messaggistica. Per le rotte di gruppo/canale solo con strumento di messaggistica, OpenClaw tratta l’assenza di evidenza di consegna tramite strumento di messaggistica come un tentativo di completamento fallito e invia direttamente il fallback dei media generati al canale originale.

## Trascrizione vocale e Voice Call

Deepgram, DeepInfra, ElevenLabs, Mistral, OpenAI, OpenRouter, SenseAudio e xAI possono tutti trascrivere audio in ingresso tramite il percorso batch `tools.media.audio` quando configurati. I plugin di canale che prevalidano una nota vocale per il gating delle menzioni o il parsing dei comandi marcano l’allegato trascritto sul contesto in ingresso, così il passaggio condiviso di comprensione dei media riusa quella trascrizione invece di fare una seconda chiamata STT per lo stesso audio.

Deepgram, ElevenLabs, Mistral, OpenAI e xAI registrano anche provider STT in streaming per Voice Call, così l’audio telefonico live può essere inoltrato al vendor selezionato senza attendere una registrazione completata.

Per conversazioni utente live, preferisci la [modalità Talk](</it/nodes/talk>). Gli allegati audio batch restano sul percorso multimediale; browser in tempo reale, push-to-talk nativo, telefonia e audio delle riunioni dovrebbero usare eventi Talk e i cataloghi con ambito di sessione restituiti dal Gateway.

## Mappature dei provider (come i vendor si dividono tra le superfici)

Google

Superfici per immagini, video, musica, TTS batch, voce in tempo reale backend e comprensione dei media.

OpenAI

Superfici per immagini, video, TTS batch, STT batch, STT in streaming per Voice Call, voce in tempo reale backend e embedding di memoria.

DeepInfra

Superfici per chat/routing dei modelli, generazione/modifica di immagini, da testo a video, TTS batch, STT batch, comprensione dei media immagine ed embedding di memoria. I modelli di rerank/classificazione/rilevamento oggetti nativi di DeepInfra non vengono registrati finché OpenClaw non dispone di contratti provider dedicati per quelle categorie.

xAI

Immagini, video, ricerca, esecuzione di codice, TTS batch, STT batch e STT in streaming per Voice Call. La voce xAI Realtime è una funzionalità upstream ma non è registrata in OpenClaw finché il contratto condiviso per la voce in tempo reale non può rappresentarla.

## Correlati

  * [Generazione di immagini](</it/tools/image-generation>)
  * [Generazione di video](</it/tools/video-generation>)
  * [Generazione di musica](</it/tools/music-generation>)
  * [Sintesi vocale](</it/tools/tts>)
  * [Comprensione dei media](</it/nodes/media-understanding>)
  * [Nodi audio](</it/nodes/audio>)
  * [Modalità Talk](</it/nodes/talk>)


Was this useful?YesNo
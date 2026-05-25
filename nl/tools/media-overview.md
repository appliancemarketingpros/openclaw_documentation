---
title: Mediaoverzicht
source_url: https://docs.openclaw.ai/nl/tools/media-overview
scraped_at: 2026-05-25
---

OpenClaw genereert afbeeldingen, video's en muziek, begrijpt inkomende media (afbeeldingen, audio, video), en spreekt antwoorden hardop uit met tekst-naar-spraak. Alle mediamogelijkheden zijn toolgestuurd: de agent beslist op basis van het gesprek wanneer ze worden gebruikt, en elke tool verschijnt alleen wanneer er minstens één achterliggende provider is geconfigureerd.

Live spraak gebruikt het Talk-sessiecontract in plaats van het eenmalige mediatoolpad. Talk heeft drie modi: provider-native `realtime`, lokale of streamende `stt-tts`, en `transcription` voor alleen-observerende spraakopname. Die modi delen providercatalogi, event-enveloppen en annuleringssemantiek met telefonie, vergaderingen, browser-realtime en native push-to-talk-clients.

## Mogelijkheden

[**Afbeeldingen genereren** Maak en bewerk afbeeldingen vanuit tekstprompts of referentieafbeeldingen via `image_generate`. Synchroon — wordt inline met het antwoord voltooid. ](</nl/tools/image-generation>) [**Video genereren** Tekst-naar-video, afbeelding-naar-video en video-naar-video via `video_generate`. Asynchroon — draait op de achtergrond en plaatst het resultaat zodra het klaar is. ](</nl/tools/video-generation>) [**Muziek genereren** Genereer muziek of audiotracks via `music_generate`. Asynchroon op gedeelde providers; het ComfyUI-workflowpad draait synchroon. ](</nl/tools/music-generation>) [**Tekst-naar-spraak** Zet uitgaande antwoorden om naar gesproken audio via de `tts`-tool plus `messages.tts`-configuratie. Synchroon. ](</nl/tools/tts>) [**Mediabegrip** Vat inkomende afbeeldingen, audio en video samen met vision-capable modelproviders en speciale plugins voor mediabegrip. ](</nl/nodes/media-understanding>) [**Spraak-naar-tekst** Transcribeer inkomende spraakberichten via batch-STT of Voice Call streaming-STT-providers. ](</nl/nodes/audio>)

## Matrix met providermogelijkheden

Provider | Afbeelding | Video | Muziek | TTS | STT | Realtime spraak | Mediabegrip  
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
  
## Asynchroon versus synchroon

Mogelijkheid | Modus | Waarom  
---|---|---  
Afbeelding | Synchroon | Providerantwoorden keren binnen seconden terug; wordt inline met het antwoord voltooid.  
Tekst-naar-spraak | Synchroon | Providerantwoorden keren binnen seconden terug; gekoppeld aan de antwoordaudio.  
Video | Asynchroon | Providerverwerking duurt 30 s tot enkele minuten; trage wachtrijen kunnen doorlopen tot de geconfigureerde time-out.  
Muziek (gedeeld) | Asynchroon | Dezelfde providerverwerkingskarakteristiek als video.  
Muziek (ComfyUI) | Synchroon | Lokale workflow draait inline tegen de geconfigureerde ComfyUI-server.  
  
Voor asynchrone tools dient OpenClaw de aanvraag in bij de provider, retourneert direct een taak-id en volgt de job in het taaklogboek. De agent blijft reageren op andere berichten terwijl de job draait. Wanneer de provider klaar is, wekt OpenClaw de agent met de gegenereerde mediapaden zodat die de gebruiker kan informeren en, wanneer vereist door het beleid voor bronlevering, het resultaat via de berichttool kan doorgeven. Voor groeps-/kanaalroutes met alleen berichttools behandelt OpenClaw ontbrekend bewijs van berichttoollevering als een mislukte voltooiingspoging en verzendt het de gegenereerde mediafallback rechtstreeks naar het oorspronkelijke kanaal.

## Spraak-naar-tekst en Voice Call

Deepgram, DeepInfra, ElevenLabs, Mistral, OpenAI, OpenRouter, SenseAudio en xAI kunnen allemaal inkomende audio transcriberen via het batchpad `tools.media.audio` wanneer ze zijn geconfigureerd. Kanaalplugins die een spraaknotitie vooraf controleren voor mention-gating of commandoparsing markeren de getranscribeerde bijlage op de inkomende context, zodat de gedeelde mediabegripspas dat transcript hergebruikt in plaats van een tweede STT-aanroep te doen voor dezelfde audio.

Deepgram, ElevenLabs, Mistral, OpenAI en xAI registreren ook Voice Call streaming-STT-providers, zodat live telefoonaudio kan worden doorgestuurd naar de geselecteerde leverancier zonder te wachten op een voltooide opname.

Geef voor live gebruikersgesprekken de voorkeur aan [Talk-modus](</nl/nodes/talk>). Batch-audiobijlagen blijven op het mediapad; browser-realtime, native push-to-talk, telefonie en vergaderaudio moeten Talk-events en de sessiegebonden catalogi gebruiken die door de Gateway worden geretourneerd.

## Providermappings (hoe leveranciers oppervlakken verdelen)

Google

Oppervlakken voor afbeelding, video, muziek, batch-TTS, backend-realtime spraak en mediabegrip.

OpenAI

Oppervlakken voor afbeelding, video, batch-TTS, batch-STT, Voice Call streaming-STT, backend-realtime spraak en geheugenembeddings.

DeepInfra

Chat-/modelroutering, afbeeldingen genereren/bewerken, tekst-naar-video, batch-TTS, batch-STT, mediabegrip voor afbeeldingen en geheugenembeddings. DeepInfra-native modellen voor rerank/classificatie/objectdetectie worden niet geregistreerd totdat OpenClaw speciale providercontracten voor die categorieën heeft.

xAI

Afbeelding, video, zoeken, code-uitvoering, batch-TTS, batch-STT en Voice Call streaming-STT. xAI Realtime-spraak is een upstreammogelijkheid, maar is niet geregistreerd in OpenClaw totdat het gedeelde contract voor realtime-spraak dit kan weergeven.

## Gerelateerd

  * [Afbeeldingen genereren](</nl/tools/image-generation>)
  * [Video genereren](</nl/tools/video-generation>)
  * [Muziek genereren](</nl/tools/music-generation>)
  * [Tekst-naar-spraak](</nl/tools/tts>)
  * [Mediabegrip](</nl/nodes/media-understanding>)
  * [Audionodes](</nl/nodes/audio>)
  * [Talk-modus](</nl/nodes/talk>)


Was this useful?YesNo
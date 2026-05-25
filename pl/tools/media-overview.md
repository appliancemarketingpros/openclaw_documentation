---
title: Omówienie mediów
source_url: https://docs.openclaw.ai/pl/tools/media-overview
scraped_at: 2026-05-25
---

OpenClaw generuje obrazy, filmy i muzykę, rozumie przychodzące multimedia (obrazy, audio, wideo) oraz wypowiada odpowiedzi na głos za pomocą zamiany tekstu na mowę. Wszystkie możliwości multimedialne są sterowane narzędziami: agent decyduje, kiedy ich użyć na podstawie rozmowy, a każde narzędzie pojawia się tylko wtedy, gdy skonfigurowany jest co najmniej jeden obsługujący je dostawca.

Mowa na żywo używa kontraktu sesji Talk zamiast jednorazowej ścieżki narzędzia multimedialnego. Talk ma trzy tryby: natywny dla dostawcy `realtime`, lokalny lub strumieniowy `stt-tts` oraz `transcription` do przechwytywania mowy tylko w trybie obserwacji. Te tryby współdzielą katalogi dostawców, koperty zdarzeń i semantykę anulowania z telefonią, spotkaniami, przeglądarkowym czasem rzeczywistym oraz natywnymi klientami push-to-talk.

## Możliwości

[**Generowanie obrazów** Twórz i edytuj obrazy z promptów tekstowych lub obrazów referencyjnych przez `image_generate`. Synchroniczne — kończy się w treści odpowiedzi. ](</pl/tools/image-generation>) [**Generowanie wideo** Tekst-na-wideo, obraz-na-wideo i wideo-na-wideo przez `video_generate`. Asynchroniczne — działa w tle i publikuje wynik, gdy jest gotowy. ](</pl/tools/video-generation>) [**Generowanie muzyki** Generuj muzykę lub ścieżki audio przez `music_generate`. Asynchroniczne u współdzielonych dostawców; ścieżka przepływu pracy ComfyUI działa synchronicznie. ](</pl/tools/music-generation>) [**Zamiana tekstu na mowę** Konwertuj wychodzące odpowiedzi na mówione audio za pomocą narzędzia `tts` oraz konfiguracji `messages.tts`. Synchroniczne. ](</pl/tools/tts>) [**Rozumienie multimediów** Podsumowuj przychodzące obrazy, audio i wideo przy użyciu dostawców modeli obsługujących wizję oraz dedykowanych pluginów rozumienia multimediów. ](</pl/nodes/media-understanding>) [**Zamiana mowy na tekst** Transkrybuj przychodzące wiadomości głosowe przez wsadowych dostawców STT lub strumieniowych dostawców STT dla Voice Call. ](</pl/nodes/audio>)

## Macierz możliwości dostawców

Dostawca | Obraz | Wideo | Muzyka | TTS | STT | Głos w czasie rzeczywistym | Rozumienie multimediów  
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
  
## Asynchroniczne a synchroniczne

Możliwość | Tryb | Dlaczego  
---|---|---  
Obraz | Synchroniczne | Odpowiedzi dostawcy wracają w kilka sekund; kończy się w treści odpowiedzi.  
Zamiana tekstu na mowę | Synchroniczne | Odpowiedzi dostawcy wracają w kilka sekund; są dołączane do audio odpowiedzi.  
Wideo | Asynchroniczne | Przetwarzanie u dostawcy trwa od 30 s do kilku minut; wolne kolejki mogą działać do skonfigurowanego limitu czasu.  
Muzyka (współdzielona) | Asynchroniczne | Ta sama charakterystyka przetwarzania u dostawcy co w przypadku wideo.  
Muzyka (ComfyUI) | Synchroniczne | Lokalny przepływ pracy działa w treści odpowiedzi względem skonfigurowanego serwera ComfyUI.  
  
W przypadku narzędzi asynchronicznych OpenClaw wysyła żądanie do dostawcy, natychmiast zwraca identyfikator zadania i śledzi je w rejestrze zadań. Agent kontynuuje odpowiadanie na inne wiadomości, gdy zadanie jest wykonywane. Gdy dostawca skończy, OpenClaw wybudza agenta ze ścieżkami wygenerowanych multimediów, aby mógł poinformować użytkownika i, gdy wymaga tego polityka dostarczania źródłowego, przekazać wynik przez narzędzie wiadomości. Dla tras grupowych/kanałowych wyłącznie przez narzędzie wiadomości OpenClaw traktuje brak dowodu dostarczenia przez narzędzie wiadomości jako nieudaną próbę ukończenia i wysyła awaryjnie wygenerowane multimedia bezpośrednio do oryginalnego kanału.

## Zamiana mowy na tekst i Voice Call

Deepgram, DeepInfra, ElevenLabs, Mistral, OpenAI, OpenRouter, SenseAudio i xAI mogą transkrybować przychodzące audio przez wsadową ścieżkę `tools.media.audio`, gdy są skonfigurowane. Pluginy kanałów, które wstępnie sprawdzają notatkę głosową pod kątem bramkowania wzmianek lub parsowania poleceń, oznaczają transkrybowany załącznik w kontekście przychodzącym, więc współdzielony przebieg rozumienia multimediów ponownie wykorzystuje tę transkrypcję zamiast wykonywać drugie wywołanie STT dla tego samego audio.

Deepgram, ElevenLabs, Mistral, OpenAI i xAI rejestrują też strumieniowych dostawców STT dla Voice Call, więc audio telefonu na żywo może być przekazywane do wybranego dostawcy bez czekania na ukończone nagranie.

W przypadku rozmów użytkownika na żywo preferuj [tryb Talk](</pl/nodes/talk>). Wsadowe załączniki audio pozostają na ścieżce multimediów; przeglądarkowy czas rzeczywisty, natywne push-to-talk, telefonia i audio spotkań powinny używać zdarzeń Talk oraz katalogów o zakresie sesji zwracanych przez Gateway.

## Mapowania dostawców (jak dostawcy dzielą się między powierzchniami)

Google

Powierzchnie obrazów, wideo, muzyki, wsadowego TTS, głosu czasu rzeczywistego po stronie backendu oraz rozumienia multimediów.

OpenAI

Powierzchnie obrazów, wideo, wsadowego TTS, wsadowego STT, strumieniowego STT Voice Call, głosu czasu rzeczywistego po stronie backendu oraz osadzania pamięci.

DeepInfra

Powierzchnie routingu czatu/modeli, generowania/edycji obrazów, tekst-na-wideo, wsadowego TTS, wsadowego STT, rozumienia multimediów obrazu oraz osadzania pamięci. Natywne modele DeepInfra do rerankingu/klasyfikacji/wykrywania obiektów nie są rejestrowane, dopóki OpenClaw nie będzie mieć dedykowanych kontraktów dostawców dla tych kategorii.

xAI

Obraz, wideo, wyszukiwanie, wykonywanie kodu, wsadowe TTS, wsadowe STT i strumieniowe STT Voice Call. Głos xAI Realtime jest możliwością upstream, ale nie jest rejestrowany w OpenClaw, dopóki współdzielony kontrakt głosu w czasie rzeczywistym nie będzie mógł go reprezentować.

## Powiązane

  * [Generowanie obrazów](</pl/tools/image-generation>)
  * [Generowanie wideo](</pl/tools/video-generation>)
  * [Generowanie muzyki](</pl/tools/music-generation>)
  * [Zamiana tekstu na mowę](</pl/tools/tts>)
  * [Rozumienie multimediów](</pl/nodes/media-understanding>)
  * [Węzły audio](</pl/nodes/audio>)
  * [Tryb Talk](</pl/nodes/talk>)


Was this useful?YesNo
---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/pl/providers/google
scraped_at: 2026-05-25
---

Plugin Google zapewnia dostęp do modeli Gemini przez Google AI Studio, a także generowanie obrazów, rozumienie multimediów (obraz/audio/wideo), zamianę tekstu na mowę oraz wyszukiwanie w sieci przez Gemini Grounding.

  * Dostawca: `google`
  * Uwierzytelnianie: `GEMINI_API_KEY` lub `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Opcja środowiska uruchomieniowego: provider/model `agentRuntime.id: "google-gemini-cli"` ponownie używa OAuth z Gemini CLI, zachowując kanoniczne odwołania do modeli jako `google/*`.


## Pierwsze kroki

Wybierz preferowaną metodę uwierzytelniania i wykonaj kroki konfiguracji.

### Klucz API

**Najlepsze do:** standardowego dostępu do Gemini API przez Google AI Studio.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Albo przekaż klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Najlepsze do:** ponownego użycia istniejącego logowania Gemini CLI przez PKCE OAuth zamiast osobnego klucza API.

* ### Zainstaluj Gemini CLI

Lokalne polecenie `gemini` musi być dostępne w `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw obsługuje zarówno instalacje Homebrew, jak i globalne instalacje npm, w tym typowe układy Windows/npm.

* ### Zaloguj się przez OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Model domyślny: `google/gemini-3.1-pro-preview`
  * Środowisko uruchomieniowe: `google-gemini-cli`
  * Alias: `gemini-cli`


Identyfikator modelu Gemini 3.1 Pro w Gemini API to `gemini-3.1-pro-preview`. OpenClaw akceptuje krótszy `google/gemini-3.1-pro` jako wygodny alias i normalizuje go przed wywołaniami dostawcy.

**Zmienne środowiskowe:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Albo warianty `GEMINI_CLI_*`.)

Odwołania do modeli `google-gemini-cli/*` są starszymi aliasami zgodności. Nowe konfiguracje powinny używać odwołań do modeli `google/*` oraz środowiska uruchomieniowego `google-gemini-cli`, gdy wymagają lokalnego wykonywania Gemini CLI.

## Możliwości

Możliwość | Obsługiwane  
---|---  
Uzupełnienia czatu | Tak  
Generowanie obrazów | Tak  
Generowanie muzyki | Tak  
Zamiana tekstu na mowę | Tak  
Głos w czasie rzeczywistym | Tak (Google Live API)  
Rozumienie obrazów | Tak  
Transkrypcja audio | Tak  
Rozumienie wideo | Tak  
Wyszukiwanie w sieci (Grounding) | Tak  
Myślenie/rozumowanie | Tak (Gemini 2.5+ / Gemini 3+)  
Modele Gemma 4 | Tak  
  
## Wyszukiwanie w sieci

Dołączony dostawca wyszukiwania w sieci `gemini` używa grounding wyszukiwania Google w Gemini. Skonfiguruj dedykowany klucz wyszukiwania w `plugins.entries.google.config.webSearch`, albo pozwól mu ponownie używać `models.providers.google.apiKey` po `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Pierwszeństwo poświadczeń to dedykowany `webSearch.apiKey`, następnie `GEMINI_API_KEY`, a potem `models.providers.google.apiKey`. `webSearch.baseUrl` jest opcjonalny i istnieje dla proxy operatorów lub zgodnych punktów końcowych Gemini API; gdy zostanie pominięty, wyszukiwanie w sieci Gemini ponownie używa `models.providers.google.baseUrl`. Zobacz [wyszukiwanie Gemini](</pl/tools/gemini-search>), aby poznać zachowanie narzędzia właściwe dla dostawcy.

## Generowanie obrazów

Dołączony dostawca generowania obrazów `google` domyślnie używa `google/gemini-3.1-flash-image-preview`.

  * Obsługuje także `google/gemini-3-pro-image-preview`
  * Generowanie: do 4 obrazów na żądanie
  * Tryb edycji: włączony, do 5 obrazów wejściowych
  * Kontrolki geometrii: `size`, `aspectRatio` i `resolution`


Aby używać Google jako domyślnego dostawcy obrazów:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Generowanie wideo

Dołączony Plugin `google` rejestruje także generowanie wideo przez współdzielone narzędzie `video_generate`.

  * Domyślny model wideo: `google/veo-3.1-fast-generate-preview`
  * Tryby: przepływy tekst-na-wideo, obraz-na-wideo oraz referencja pojedynczego wideo
  * Obsługuje `aspectRatio` (`16:9`, `9:16`) i `resolution` (`720P`, `1080P`); wyjście audio nie jest obecnie obsługiwane przez Veo
  * Obsługiwane czasy trwania: **4, 6 lub 8 sekund** (inne wartości są zaokrąglane do najbliższej dozwolonej wartości)


Aby używać Google jako domyślnego dostawcy wideo:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Generowanie muzyki

Dołączony Plugin `google` rejestruje także generowanie muzyki przez współdzielone narzędzie `music_generate`.

  * Domyślny model muzyki: `google/lyria-3-clip-preview`
  * Obsługuje także `google/lyria-3-pro-preview`
  * Kontrolki promptu: `lyrics` i `instrumental`
  * Format wyjściowy: domyślnie `mp3`, a także `wav` w `google/lyria-3-pro-preview`
  * Wejścia referencyjne: do 10 obrazów
  * Przebiegi oparte na sesji odłączają się przez współdzielony przepływ zadań/statusu, w tym `action: "status"`


Aby używać Google jako domyślnego dostawcy muzyki:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Zamiana tekstu na mowę

Dołączony dostawca mowy `google` używa ścieżki TTS Gemini API z `gemini-3.1-flash-tts-preview`.

  * Domyślny głos: `Kore`
  * Uwierzytelnianie: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` lub `GOOGLE_API_KEY`
  * Wyjście: WAV dla zwykłych załączników TTS, Opus dla celów notatek głosowych, PCM dla Talk/telefonii
  * Wyjście notatek głosowych: Google PCM jest opakowywane jako WAV i transkodowane do 48 kHz Opus za pomocą `ffmpeg`


Wsadowa ścieżka Gemini TTS Google zwraca wygenerowane audio w ukończonej odpowiedzi `generateContent`. Do rozmów mówionych o najniższym opóźnieniu użyj dostawcy głosu Google w czasie rzeczywistym opartego na Gemini Live API zamiast wsadowego TTS.

Aby używać Google jako domyślnego dostawcy TTS:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS używa promptów w języku naturalnym do kontroli stylu. Ustaw `audioProfile`, aby dodać wielokrotnego użytku prompt stylu przed tekstem mówionym. Ustaw `speakerName`, gdy tekst promptu odnosi się do nazwanego mówcy.

Gemini API TTS akceptuje także ekspresyjne tagi audio w nawiasach kwadratowych w tekście, takie jak `[whispers]` lub `[laughs]`. Aby ukryć tagi w widocznej odpowiedzi czatu, a jednocześnie wysłać je do TTS, umieść je w bloku `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Głos w czasie rzeczywistym

Dołączony Plugin `google` rejestruje dostawcę głosu w czasie rzeczywistym opartego na Gemini Live API dla mostków audio backendu, takich jak Voice Call i Google Meet.

Ustawienie | Ścieżka konfiguracji | Wartość domyślna  
---|---|---  
Model | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Głos | `...google.voice` | `Kore`  
Temperatura | `...google.temperature` | (nieustawiona)  
Czułość rozpoczęcia VAD | `...google.startSensitivity` | (nieustawiona)  
Czułość zakończenia VAD | `...google.endSensitivity` | (nieustawiona)  
Czas trwania ciszy | `...google.silenceDurationMs` | (nieustawiony)  
Obsługa aktywności | `...google.activityHandling` | wartość domyślna Google, `start-of-activity-interrupts`  
Zakres tury | `...google.turnCoverage` | wartość domyślna Google, `only-activity`  
Wyłącz automatyczne VAD | `...google.automaticActivityDetectionDisabled` | `false`  
Wznawianie sesji | `...google.sessionResumption` | `true`  
Kompresja kontekstu | `...google.contextWindowCompression` | `true`  
Klucz API | `...google.apiKey` | Używa zapasowo `models.providers.google.apiKey`, `GEMINI_API_KEY` lub `GOOGLE_API_KEY`  
  
Przykładowa konfiguracja połączeń głosowych w czasie rzeczywistym:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Na potrzeby weryfikacji live przez opiekuna uruchom `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Ten smoke test obejmuje też ścieżki backend/WebRTC OpenAI; etap Google tworzy ten sam ograniczony kształt tokena Live API używany przez Control UI Talk, otwiera punkt końcowy WebSocket przeglądarki, wysyła początkowy payload konfiguracji i czeka na `setupComplete`.

## Zaawansowana konfiguracja

Bezpośrednie ponowne użycie pamięci podręcznej Gemini

W przypadku bezpośrednich uruchomień Gemini API (`api: "google-generative-ai"`) OpenClaw przekazuje skonfigurowany uchwyt `cachedContent` do żądań Gemini.

  * Skonfiguruj parametry dla modelu lub globalnie za pomocą `cachedContent` albo starszego `cached_content`
  * Jeśli obecne są oba, pierwszeństwo ma `cachedContent`
  * Przykładowa wartość: `cachedContents/prebuilt-context`
  * Użycie trafień pamięci podręcznej Gemini jest normalizowane do OpenClaw `cacheRead` z nadrzędnego `cachedContentTokenCount`

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Uwagi dotyczące użycia JSON Gemini CLI

Podczas używania dostawcy OAuth `google-gemini-cli` OpenClaw normalizuje wyjście JSON CLI w następujący sposób:

  * Tekst odpowiedzi pochodzi z pola `response` w JSON CLI.
  * Użycie przełącza się zapasowo na `stats`, gdy CLI pozostawia `usage` puste.
  * `stats.cached` jest normalizowane do OpenClaw `cacheRead`.
  * Jeśli brakuje `stats.input`, OpenClaw wylicza tokeny wejściowe z `stats.input_tokens - stats.cached`.

Konfiguracja środowiska i demona

Jeśli Gateway działa jako demon (launchd/systemd), upewnij się, że `GEMINI_API_KEY` jest dostępny dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).

## Powiązane

[**Wybór modelu** Wybór dostawców, odwołań do modeli i zachowania failover. ](</pl/concepts/model-providers>) [**Generowanie obrazów** Współdzielone parametry narzędzia obrazów i wybór dostawcy. ](</pl/tools/image-generation>) [**Generowanie wideo** Współdzielone parametry narzędzia wideo i wybór dostawcy. ](</pl/tools/video-generation>) [**Generowanie muzyki** Współdzielone parametry narzędzia muzyki i wybór dostawcy. ](</pl/tools/music-generation>)

Was this useful?YesNo
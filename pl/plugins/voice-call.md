---
title: Plugin połączeń głosowych
source_url: https://docs.openclaw.ai/pl/plugins/voice-call
scraped_at: 2026-05-25
---

Połączenia głosowe dla OpenClaw przez Plugin. Obsługuje powiadomienia wychodzące, wieloturowe rozmowy, pełnodupleksowy głos w czasie rzeczywistym, strumieniową transkrypcję oraz połączenia przychodzące z zasadami listy dozwolonych.

**Aktualni dostawcy:** `twilio` (Programmable Voice + Media Streams), `telnyx` (Call Control v2), `plivo` (Voice API + XML transfer + GetInput speech), `mock` (tryb deweloperski/bez sieci).

## Szybki start

* ### Zainstaluj Plugin

### Z npm

bashCopy code
[code]
    openclaw plugins install @openclaw/voice-call
[/code]

### Z folderu lokalnego (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/voice-call-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Użyj samej nazwy pakietu, aby śledzić aktualny oficjalny tag wydania. Przypnij dokładną wersję tylko wtedy, gdy potrzebujesz odtwarzalnej instalacji.

Następnie uruchom ponownie Gateway, aby Plugin został załadowany.

* ### Skonfiguruj dostawcę i Webhook

Ustaw konfigurację w `plugins.entries.voice-call.config` (pełny kształt znajdziesz poniżej w sekcji Konfiguracja). Minimalnie: `provider`, dane uwierzytelniające dostawcy, `fromNumber` oraz publicznie osiągalny adres URL Webhook.

* ### Zweryfikuj konfigurację

bashCopy code
[code]
    openclaw voicecall setup
[/code]

Domyślne wyjście jest czytelne w logach czatu i terminalach. Sprawdza, czy Plugin jest włączony, dane uwierzytelniające dostawcy, ekspozycję Webhook oraz czy aktywny jest tylko jeden tryb audio (`streaming` albo `realtime`). Użyj `--json` w skryptach.

* ### Test dymny

bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"
[/code]

Domyślnie oba są przebiegami próbnymi. Dodaj `--yes`, aby faktycznie wykonać krótkie połączenie wychodzące z powiadomieniem:

bashCopy code
[code]
    openclaw voicecall smoke --to "+15555550123" --yes
[/code]

## Konfiguracja

Jeśli `enabled: true`, ale wybranemu dostawcy brakuje danych uwierzytelniających, uruchomienie Gateway zapisuje ostrzeżenie o niekompletnej konfiguracji z brakującymi kluczami i pomija uruchomienie środowiska wykonawczego. Polecenia, wywołania RPC i narzędzia agenta nadal zwracają dokładną brakującą konfigurację dostawcy, gdy są używane.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio", // or "telnyx" | "plivo" | "mock"          fromNumber: "+15550001234", // or TWILIO_FROM_NUMBER for Twilio          toNumber: "+15550005678",          sessionScope: "per-phone", // per-phone | per-call          numbers: {            "+15550009999": {              inboundGreeting: "Silver Fox Cards, how can I help?",              responseSystemPrompt: "You are a concise baseball card specialist.",              tts: {                providers: {                  openai: { voice: "alloy" },                },              },            },          },           twilio: {            accountSid: "ACxxxxxxxx",            authToken: "...",          },          telnyx: {            apiKey: "...",            connectionId: "...",            // Telnyx webhook public key from the Mission Control Portal            // (Base64; can also be set via TELNYX_PUBLIC_KEY).            publicKey: "...",          },          plivo: {            authId: "MAxxxxxxxxxxxxxxxxxxxx",            authToken: "...",          },           // Webhook server          serve: {            port: 3334,            path: "/voice/webhook",          },           // Webhook security (recommended for tunnels/proxies)          webhookSecurity: {            allowedHosts: ["voice.example.com"],            trustedProxyIPs: ["100.64.0.1"],          },           // Public exposure (pick one)          // publicUrl: "https://example.ngrok.app/voice/webhook",          // tunnel: { provider: "ngrok" },          // tailscale: { mode: "funnel", path: "/voice/webhook" },           outbound: {            defaultMode: "notify", // notify | conversation          },           streaming: { enabled: true /* see Streaming transcription */ },          realtime: { enabled: false /* see Realtime voice */ },        },      },    },  },}
[/code]

Ekspozycja dostawcy i uwagi dotyczące bezpieczeństwa

  * Twilio, Telnyx i Plivo wymagają **publicznie osiągalnego** adresu URL Webhook.
  * `mock` to lokalny dostawca deweloperski (bez wywołań sieciowych).
  * Telnyx wymaga `telnyx.publicKey` (albo `TELNYX_PUBLIC_KEY`), chyba że `skipSignatureVerification` ma wartość true.
  * `skipSignatureVerification` służy tylko do testów lokalnych.
  * W bezpłatnej warstwie ngrok ustaw `publicUrl` na dokładny URL ngrok; weryfikacja podpisów jest zawsze wymuszana.
  * `tunnel.allowNgrokFreeTierLoopbackBypass: true` zezwala na Webhook Twilio z nieprawidłowymi podpisami **tylko** wtedy, gdy `tunnel.provider="ngrok"` i `serve.bind` to local loopback (lokalny agent ngrok). Tylko lokalny dev.
  * Adresy URL bezpłatnej warstwy Ngrok mogą się zmieniać lub dodawać zachowanie pośrednie; jeśli `publicUrl` się rozjedzie, podpisy Twilio przestaną działać. Produkcja: preferuj stabilną domenę albo tunel Tailscale.

Limity połączeń strumieniowych

  * `streaming.preStartTimeoutMs` zamyka gniazda, które nigdy nie wysyłają prawidłowej ramki `start`.
  * `streaming.maxPendingConnections` ogranicza łączną liczbę nieuwierzytelnionych gniazd przed startem.
  * `streaming.maxPendingConnectionsPerIp` ogranicza nieuwierzytelnione gniazda przed startem na źródłowy adres IP.
  * `streaming.maxConnections` ogranicza łączną liczbę otwartych gniazd strumienia mediów (oczekujących + aktywnych).

Migracje starszej konfiguracji

Starsze konfiguracje używające `provider: "log"`, `twilio.from` albo starszych kluczy OpenAI `streaming.*` są przepisywane przez `openclaw doctor --fix`. Awaryjna obsługa w czasie wykonywania nadal akceptuje stare klucze voice-call, ale ścieżką przepisywania jest `openclaw doctor --fix`, a warstwa zgodności jest tymczasowa.

Automatycznie migrowane klucze strumieniowania:

  * `streaming.sttProvider` → `streaming.provider`
  * `streaming.openaiApiKey` → `streaming.providers.openai.apiKey`
  * `streaming.sttModel` → `streaming.providers.openai.model`
  * `streaming.silenceDurationMs` → `streaming.providers.openai.silenceDurationMs`
  * `streaming.vadThreshold` → `streaming.providers.openai.vadThreshold`


## Zakres sesji

Domyślnie Voice Call używa `sessionScope: "per-phone"`, więc powtórne połączenia od tego samego dzwoniącego zachowują pamięć rozmowy. Ustaw `sessionScope: "per-call"`, gdy każde połączenie operatora powinno zaczynać ze świeżym kontekstem, na przykład w przepływach recepcji, rezerwacji, IVR albo mostka Google Meet, gdzie ten sam numer telefonu może reprezentować różne spotkania.

## Rozmowy głosowe w czasie rzeczywistym

`realtime` wybiera pełnodupleksowego dostawcę głosu w czasie rzeczywistym dla dźwięku połączeń na żywo. Jest oddzielny od `streaming`, które tylko przekazuje dźwięk do dostawców transkrypcji w czasie rzeczywistym.

Aktualne zachowanie środowiska wykonawczego:

  * `realtime.enabled` jest obsługiwane dla Twilio Media Streams.
  * `realtime.provider` jest opcjonalne. Jeśli nie jest ustawione, Voice Call używa pierwszego zarejestrowanego dostawcy głosu w czasie rzeczywistym.
  * Dołączani dostawcy głosu w czasie rzeczywistym: Google Gemini Live (`google`) i OpenAI (`openai`), rejestrowani przez ich Plugin dostawców.
  * Surowa konfiguracja należąca do dostawcy znajduje się w `realtime.providers.<providerId>`.
  * Voice Call domyślnie udostępnia współdzielone narzędzie czasu rzeczywistego `openclaw_agent_consult`. Model czasu rzeczywistego może je wywołać, gdy dzwoniący prosi o głębsze rozumowanie, aktualne informacje albo normalne narzędzia OpenClaw.
  * `realtime.consultPolicy` opcjonalnie dodaje wskazówki, kiedy model czasu rzeczywistego powinien wywołać `openclaw_agent_consult`.
  * `realtime.agentContext.enabled` jest domyślnie wyłączone. Po włączeniu Voice Call wstrzykuje ograniczoną tożsamość agenta, nadpisanie promptu systemowego i wybraną kapsułę plików obszaru roboczego do instrukcji dostawcy czasu rzeczywistego podczas konfiguracji sesji.
  * `realtime.fastContext.enabled` jest domyślnie wyłączone. Po włączeniu Voice Call najpierw przeszukuje zindeksowaną pamięć/kontekst sesji pod kątem pytania konsultacyjnego i zwraca te fragmenty do modelu czasu rzeczywistego w ramach `realtime.fastContext.timeoutMs`, zanim przejdzie awaryjnie do pełnego agenta konsultacyjnego tylko wtedy, gdy `realtime.fastContext.fallbackToConsult` ma wartość true.
  * Jeśli `realtime.provider` wskazuje niezarejestrowanego dostawcę albo żaden dostawca głosu w czasie rzeczywistym nie jest w ogóle zarejestrowany, Voice Call zapisuje ostrzeżenie i pomija media czasu rzeczywistego zamiast przerywać działanie całego Plugin.
  * Klucze sesji konsultacji ponownie używają zapisanej sesji połączenia, gdy jest dostępna, a następnie przechodzą awaryjnie do skonfigurowanego `sessionScope` (`per-phone` domyślnie albo `per-call` dla izolowanych połączeń).


### Zasady narzędzi

`realtime.toolPolicy` steruje uruchomieniem konsultacji:

Zasada | Zachowanie  
---|---  
`safe-read-only` | Udostępnia narzędzie konsultacji i ogranicza zwykłego agenta do `read`, `web_search`, `web_fetch`, `x_search`, `memory_search` oraz `memory_get`.  
`owner` | Udostępnia narzędzie konsultacji i pozwala zwykłemu agentowi używać normalnych zasad narzędzi agenta.  
`none` | Nie udostępnia narzędzia konsultacji. Niestandardowe `realtime.tools` nadal są przekazywane do dostawcy czasu rzeczywistego.  
  
`realtime.consultPolicy` steruje tylko instrukcjami modelu czasu rzeczywistego:

Zasada | Wskazówki  
---|---  
`auto` | Zachowaj domyślny prompt i pozwól dostawcy zdecydować, kiedy wywołać narzędzie konsultacji.  
`substantive` | Odpowiadaj bezpośrednio na proste elementy rozmowy i konsultuj przed faktami, pamięcią, narzędziami lub kontekstem.  
`always` | Konsultuj przed każdą merytoryczną odpowiedzią.  
  
### Kontekst głosowy agenta

Włącz `realtime.agentContext`, gdy mostek głosowy powinien brzmieć jak skonfigurowany agent OpenClaw bez kosztu pełnej rundy agent-consult przy zwykłych turach. Kapsuła kontekstu jest dodawana raz podczas tworzenia sesji czasu rzeczywistego, więc nie dodaje opóźnienia na turę. Wywołania `openclaw_agent_consult` nadal uruchamiają pełnego agenta OpenClaw i powinny być używane do pracy z narzędziami, aktualnych informacji, wyszukiwania w pamięci albo stanu obszaru roboczego.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          agentId: "main",          realtime: {            enabled: true,            provider: "google",            toolPolicy: "safe-read-only",            consultPolicy: "substantive",            agentContext: {              enabled: true,              maxChars: 6000,              includeIdentity: true,              includeSystemPrompt: true,              includeWorkspaceFiles: true,              files: ["SOUL.md", "IDENTITY.md", "USER.md"],            },          },        },      },    },  },}
[/code]

### Przykłady dostawców realtime

### Google Gemini Live

Domyślne: klucz API z `realtime.providers.google.apiKey`, `GEMINI_API_KEY` albo `GOOGLE_GENERATIVE_AI_API_KEY`; model `gemini-2.5-flash-native-audio-preview-12-2025`; głos `Kore`. `sessionResumption` i `contextWindowCompression` są domyślnie włączone dla dłuższych, możliwych do ponownego połączenia rozmów. Użyj `silenceDurationMs`, `startSensitivity` i `endSensitivity`, aby dostroić szybsze przejmowanie tury w dźwięku telefonicznym.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          provider: "twilio",          inboundPolicy: "allowlist",          allowFrom: ["+15550005678"],          realtime: {            enabled: true,            provider: "google",            instructions: "Speak briefly. Call openclaw_agent_consult before using deeper tools.",            toolPolicy: "safe-read-only",            consultPolicy: "substantive",            consultThinkingLevel: "low",            consultFastMode: true,            agentContext: { enabled: true },            providers: {              google: {                apiKey: "${GEMINI_API_KEY}",                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                silenceDurationMs: 500,                startSensitivity: "high",              },            },          },        },      },    },  },}
[/code]

### OpenAI

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          realtime: {            enabled: true,            provider: "openai",            providers: {              openai: { apiKey: "${OPENAI_API_KEY}" },            },          },        },      },    },  },}
[/code]

Zobacz [dostawcę Google](</pl/providers/google>) i [dostawcę OpenAI](</pl/providers/openai>), aby poznać opcje głosu realtime specyficzne dla dostawcy.

## Transkrypcja strumieniowa

`streaming` wybiera dostawcę transkrypcji realtime dla dźwięku połączeń na żywo.

Bieżące zachowanie runtime:

  * `streaming.provider` jest opcjonalne. Jeśli nie jest ustawione, Voice Call używa pierwszego zarejestrowanego dostawcy transkrypcji realtime.
  * Wbudowani dostawcy transkrypcji realtime: Deepgram (`deepgram`), ElevenLabs (`elevenlabs`), Mistral (`mistral`), OpenAI (`openai`) i xAI (`xai`), rejestrowani przez ich Plugin dostawców.
  * Surowa konfiguracja należąca do dostawcy znajduje się pod `streaming.providers.<providerId>`.
  * Gdy Twilio wyśle zaakceptowaną wiadomość `start` strumienia, Voice Call natychmiast rejestruje strumień, kolejkuje przychodzące media przez dostawcę transkrypcji, gdy dostawca się łączy, i rozpoczyna początkowe powitanie dopiero po gotowości transkrypcji realtime.
  * Jeśli `streaming.provider` wskazuje niezarejestrowanego dostawcę albo żaden nie jest zarejestrowany, Voice Call zapisuje ostrzeżenie w dzienniku i pomija strumieniowanie multimediów zamiast kończyć cały Plugin błędem.


### Przykłady dostawców strumieniowania

### OpenAI

Domyślne: klucz API `streaming.providers.openai.apiKey` albo `OPENAI_API_KEY`; model `gpt-4o-transcribe`; `silenceDurationMs: 800`; `vadThreshold: 0.5`.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "openai",            streamPath: "/voice/stream",            providers: {              openai: {                apiKey: "sk-...", // optional if OPENAI_API_KEY is set                model: "gpt-4o-transcribe",                silenceDurationMs: 800,                vadThreshold: 0.5,              },            },          },        },      },    },  },}
[/code]

### xAI

Domyślne: klucz API `streaming.providers.xai.apiKey` albo `XAI_API_KEY`; punkt końcowy `wss://api.x.ai/v1/stt`; kodowanie `mulaw`; częstotliwość próbkowania `8000`; `endpointingMs: 800`; `interimResults: true`.

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            streamPath: "/voice/stream",            providers: {              xai: {                apiKey: "${XAI_API_KEY}", // optional if XAI_API_KEY is set                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

## TTS dla połączeń

Voice Call używa podstawowej konfiguracji `messages.tts` do strumieniowania mowy podczas połączeń. Możesz ją zastąpić w konfiguracji Plugin z **tym samym kształtem** — zostanie głęboko scalona z `messages.tts`.

json5Copy code
[code]
    {  tts: {    provider: "elevenlabs",    providers: {      elevenlabs: {        voiceId: "pMsXgVXv3BLzUgSXRplE",        modelId: "eleven_multilingual_v2",      },    },  },}
[/code]

Uwagi dotyczące zachowania:

  * Starsze klucze `tts.<provider>` w konfiguracji Plugin (`openai`, `elevenlabs`, `microsoft`, `edge`) są naprawiane przez `openclaw doctor --fix`; zatwierdzona konfiguracja powinna używać `tts.providers.<provider>`.
  * Podstawowe TTS jest używane, gdy strumieniowanie multimediów Twilio jest włączone; w przeciwnym razie połączenia wracają do natywnych głosów dostawcy.
  * Jeśli strumień multimediów Twilio jest już aktywny, Voice Call nie wraca do TwiML `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5`. Jeśli TTS telefoniczny jest niedostępny w tym stanie, żądanie odtwarzania kończy się niepowodzeniem zamiast mieszać dwie ścieżki odtwarzania.
  * Gdy TTS telefoniczny wraca do dostawcy zapasowego, Voice Call zapisuje ostrzeżenie z łańcuchem dostawców (`from`, `to`, `attempts`) na potrzeby debugowania.
  * Gdy Twilio barge-in lub zamknięcie strumienia czyści oczekującą kolejkę TTS, zakolejkowane żądania odtwarzania są rozstrzygane zamiast pozostawiać dzwoniących w oczekiwaniu na ukończenie odtwarzania.


### Przykłady TTS

### Core TTS only

json5Copy code
[code]
    {messages: {tts: {provider: "openai",providers: {  openai: { voice: "alloy" },},},},}
[/code]

### Override to ElevenLabs (calls only)

json5Copy code
[code]
    {plugins: {entries: {"voice-call": {  config: {    tts: {      provider: "elevenlabs",      providers: {        elevenlabs: {          apiKey: "elevenlabs_key",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },},},},}
[/code]

### OpenAI model override (deep-merge)

json5Copy code
[code]
    {plugins: {entries: {"voice-call": {  config: {    tts: {      providers: {        openai: {          model: "gpt-4o-mini-tts",          voice: "marin",        },      },    },  },},},},}
[/code]

## Połączenia przychodzące

Domyślna polityka połączeń przychodzących to `disabled`. Aby włączyć połączenia przychodzące, ustaw:

json5Copy code
[code]
    {inboundPolicy: "allowlist",allowFrom: ["+15550001234"],inboundGreeting: "Hello! How can I help?",}
[/code]

Automatyczne odpowiedzi używają systemu agenta. Dostosuj je za pomocą `responseModel`, `responseSystemPrompt` i `responseTimeoutMs`.

### Routing według numeru

Użyj `numbers`, gdy jeden Plugin Voice Call odbiera połączenia dla wielu numerów telefonu, a każdy numer powinien zachowywać się jak osobna linia. Na przykład jeden numer może używać swobodnego osobistego asystenta, a inny persony biznesowej, innego agenta odpowiedzi i innego głosu TTS.

Trasy są wybierane na podstawie dostarczonego przez dostawcę wybranego numeru `To`. Klucze muszą być numerami E.164. Gdy nadejdzie połączenie, Voice Call raz rozwiązuje pasującą trasę, zapisuje dopasowaną trasę w rekordzie połączenia i ponownie używa tej efektywnej konfiguracji dla powitania, klasycznej ścieżki automatycznej odpowiedzi, ścieżki konsultacji realtime i odtwarzania TTS. Jeśli żadna trasa nie pasuje, używana jest globalna konfiguracja Voice Call. Połączenia wychodzące nie używają `numbers`; podczas inicjowania połączenia przekaż jawnie cel wychodzący, wiadomość i sesję.

Zastąpienia tras obecnie obsługują:

  * `inboundGreeting`
  * `tts`
  * `agentId`
  * `responseModel`
  * `responseSystemPrompt`
  * `responseTimeoutMs`


Wartość trasy `tts` jest głęboko scalana z globalną konfiguracją `tts` Voice Call, więc zwykle możesz zastąpić tylko głos dostawcy:

json5Copy code
[code]
    {inboundGreeting: "Hello from the main line.",responseSystemPrompt: "You are the default voice assistant.",tts: {  provider: "openai",  providers: {    openai: { voice: "coral" },  },},numbers: {  "+15550001111": {    inboundGreeting: "Silver Fox Cards, how can I help?",    responseSystemPrompt: "You are a concise baseball card specialist.",    tts: {      providers: {        openai: { voice: "alloy" },      },    },  },},}
[/code]

### Kontrakt wypowiedzi mówionej

W przypadku automatycznych odpowiedzi Voice Call dołącza ścisły kontrakt wypowiedzi mówionej do promptu systemowego:

textCopy code
[code]
    {"spoken":"..."}
[/code]

Voice Call defensywnie wyodrębnia tekst mowy:

  * Ignoruje ładunki oznaczone jako treść rozumowania/błędu.
  * Parsuje bezpośredni JSON, JSON w bloku kodu albo wbudowane klucze `"spoken"`.
  * Wraca do zwykłego tekstu i usuwa prawdopodobne akapity wprowadzające dotyczące planowania/metadanych.


Dzięki temu odtwarzana mowa pozostaje skupiona na tekście dla dzwoniącego i unika wycieku tekstu planowania do dźwięku.

### Zachowanie uruchamiania rozmowy

W przypadku wychodzących połączeń `conversation` obsługa pierwszej wiadomości jest powiązana ze stanem odtwarzania na żywo:

  * Czyszczenie kolejki barge-in i automatyczna odpowiedź są wstrzymywane tylko wtedy, gdy początkowe powitanie jest aktywnie wypowiadane.
  * Jeśli początkowe odtwarzanie się nie powiedzie, połączenie wraca do `listening`, a początkowa wiadomość pozostaje w kolejce do ponowienia.
  * Początkowe odtwarzanie dla strumieniowania Twilio zaczyna się przy połączeniu strumienia bez dodatkowego opóźnienia.
  * Barge-in przerywa aktywne odtwarzanie i czyści zakolejkowane, ale jeszcze nieodtwarzane wpisy Twilio TTS. Wyczyszczone wpisy rozstrzygają się jako pominięte, więc logika odpowiedzi uzupełniającej może kontynuować bez czekania na dźwięk, który nigdy nie zostanie odtworzony.
  * Rozmowy głosowe realtime używają własnej początkowej tury strumienia realtime. Voice Call **nie** publikuje starszej aktualizacji TwiML `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5` dla tej początkowej wiadomości, więc sesje wychodzące `&lt;Connect&gt;&lt;Stream&gt;` pozostają podłączone.


### Okres karencji rozłączenia strumienia Twilio

Gdy strumień multimediów Twilio zostanie rozłączony, Voice Call czeka **2000 ms** przed automatycznym zakończeniem połączenia:

  * Jeśli strumień połączy się ponownie w tym oknie, automatyczne zakończenie zostaje anulowane.
  * Jeśli po okresie karencji żaden strumień nie zarejestruje się ponownie, połączenie zostaje zakończone, aby zapobiec zablokowanym aktywnym połączeniom.


## Czyszczenie nieaktualnych połączeń

Użyj `staleCallReaperSeconds`, aby zakończyć połączenia, które nigdy nie otrzymują końcowego Webhook (na przykład połączenia w trybie powiadamiania, które nigdy się nie kończą). Wartość domyślna to `0` (wyłączone).

Zalecane zakresy:

  * **Produkcja:** `120`–`300` sekund dla przepływów typu powiadomieniowego.
  * Utrzymuj tę wartość **wyższą niż`maxDurationSeconds`**, aby normalne wywołania mogły się zakończyć. Dobry punkt wyjścia to `maxDurationSeconds + 30–60` sekund.

json5Copy code
[code]
    {plugins: {entries: {  "voice-call": {    config: {      maxDurationSeconds: 300,      staleCallReaperSeconds: 360,    },  },},},}
[/code]

## Zabezpieczenia Webhook

Gdy przed Gateway działa proxy lub tunel, plugin odtwarza publiczny adres URL do weryfikacji podpisu. Te opcje kontrolują, którym nagłówkom przekazywanym można ufać:

Lista dozwolonych hostów z nagłówków przekazywania.

Ufaj nagłówkom przekazywanym bez listy dozwolonych.

Ufaj nagłówkom przekazywanym tylko wtedy, gdy zdalny adres IP żądania pasuje do listy.

Dodatkowe zabezpieczenia:

  * **Ochrona przed ponownym odtworzeniem** Webhook jest włączona dla Twilio i Plivo. Ponownie odtworzone prawidłowe żądania Webhook są potwierdzane, ale pomijane pod kątem skutków ubocznych.
  * Tury konwersacji Twilio zawierają token dla każdej tury w wywołaniach zwrotnych `&lt;Gather&gt;`, więc przestarzałe lub ponownie odtworzone wywołania zwrotne mowy nie mogą zaspokoić nowszej oczekującej tury transkrypcji.
  * Nieuwierzytelnione żądania Webhook są odrzucane przed odczytem treści, gdy brakuje wymaganych nagłówków podpisu dostawcy.
  * Webhook połączeń głosowych używa współdzielonego profilu treści przed uwierzytelnieniem (64 KB / 5 sekund) oraz limitu trwających żądań dla adresu IP przed weryfikacją podpisu.


Przykład ze stabilnym hostem publicznym:

json5Copy code
[code]
    {plugins: {entries: {  "voice-call": {    config: {      publicUrl: "https://voice.example.com/voice/webhook",      webhookSecurity: {        allowedHosts: ["voice.example.com"],      },    },  },},},}
[/code]

## CLI

bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello from OpenClaw"openclaw voicecall start --to "+15555550123"   # alias for callopenclaw voicecall continue --call-id <id> --message "Any questions?"openclaw voicecall speak --call-id <id> --message "One moment"openclaw voicecall dtmf --call-id <id> --digits "ww123456#"openclaw voicecall end --call-id <id>openclaw voicecall status --call-id <id>openclaw voicecall tailopenclaw voicecall latency                      # summarize turn latency from logsopenclaw voicecall expose --mode funnel
[/code]

Gdy Gateway już działa, operacyjne polecenia `voicecall` delegują do środowiska wykonawczego połączeń głosowych zarządzanego przez Gateway, aby CLI nie wiązało drugiego serwera Webhook. Jeśli żaden Gateway nie jest osiągalny, polecenia przechodzą awaryjnie na samodzielne środowisko wykonawcze CLI.

`latency` odczytuje `calls.jsonl` z domyślnej ścieżki przechowywania połączeń głosowych. Użyj `--file <path>`, aby wskazać inny dziennik, oraz `--last <n>`, aby ograniczyć analizę do ostatnich N rekordów (domyślnie 200). Dane wyjściowe zawierają p50/p90/p99 dla opóźnienia tury oraz czasów oczekiwania na słuchanie.

## Narzędzie agenta

Nazwa narzędzia: `voice_call`.

Akcja | Argumenty  
---|---  
`initiate_call` | `message`, `to?`, `mode?`, `dtmfSequence?`  
`continue_call` | `callId`, `message`  
`speak_to_user` | `callId`, `message`  
`send_dtmf` | `callId`, `digits`  
`end_call` | `callId`  
`get_status` | `callId`  
  
To repozytorium zawiera pasujący dokument Skills pod adresem `skills/voice-call/SKILL.md`.

## RPC Gateway

Metoda | Argumenty  
---|---  
`voicecall.initiate` | `to?`, `message`, `mode?`, `dtmfSequence?`  
`voicecall.continue` | `callId`, `message`  
`voicecall.speak` | `callId`, `message`  
`voicecall.dtmf` | `callId`, `digits`  
`voicecall.end` | `callId`  
`voicecall.status` | `callId`  
  
`dtmfSequence` jest prawidłowe tylko z `mode: "conversation"`. Połączenia w trybie powiadamiania powinny używać `voicecall.dtmf` po utworzeniu połączenia, jeśli potrzebują cyfr po nawiązaniu połączenia.

## Rozwiązywanie problemów

### Konfiguracja nie może udostępnić Webhook

Uruchom konfigurację z tego samego środowiska, w którym działa Gateway:

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

Dla `twilio`, `telnyx` i `plivo` element `webhook-exposure` musi być zielony. Skonfigurowany `publicUrl` nadal kończy się niepowodzeniem, gdy wskazuje lokalną lub prywatną przestrzeń sieciową, ponieważ operator nie może oddzwonić na te adresy. Nie używaj `localhost`, `127.0.0.1`, `0.0.0.0`, `10.x`, `172.16.x`-`172.31.x`, `192.168.x`, `169.254.x`, `fc00::/7` ani `fd00::/8` jako `publicUrl`.

Połączenia wychodzące Twilio w trybie powiadamiania wysyłają początkowy TwiML `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5` bezpośrednio w żądaniu utworzenia połączenia, więc pierwsza wypowiedziana wiadomość nie zależy od pobrania TwiML Webhook przez Twilio. Publiczny Webhook nadal jest wymagany do wywołań zwrotnych statusu, połączeń konwersacyjnych, DTMF przed nawiązaniem połączenia, strumieni czasu rzeczywistego oraz sterowania połączeniem po nawiązaniu.

Użyj jednej publicznej ścieżki udostępniania:

json5Copy code
[code]
    {plugins: {entries: {"voice-call": {  config: {    publicUrl: "https://voice.example.com/voice/webhook",    // or    tunnel: { provider: "ngrok" },    // or    tailscale: { mode: "funnel", path: "/voice/webhook" },  },},},},}
[/code]

Po zmianie konfiguracji uruchom ponownie lub przeładuj Gateway, a następnie uruchom:

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall smoke
[/code]

`voicecall smoke` jest przebiegiem próbnym, chyba że przekażesz `--yes`.

### Dane uwierzytelniające dostawcy zawodzą

Sprawdź wybranego dostawcę i wymagane pola danych uwierzytelniających:

  * Twilio: `twilio.accountSid`, `twilio.authToken` i `fromNumber` albo `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN` i `TWILIO_FROM_NUMBER`.
  * Telnyx: `telnyx.apiKey`, `telnyx.connectionId`, `telnyx.publicKey` i `fromNumber`.
  * Plivo: `plivo.authId`, `plivo.authToken` i `fromNumber`.


Dane uwierzytelniające muszą istnieć na hoście Gateway. Edycja lokalnego profilu powłoki nie wpływa na już działający Gateway, dopóki nie zostanie on uruchomiony ponownie lub nie przeładuje swojego środowiska.

### Połączenia się rozpoczynają, ale Webhook dostawcy nie docierają

Potwierdź, że konsola dostawcy wskazuje dokładny publiczny adres URL Webhook:

textCopy code
[code]
    https://voice.example.com/voice/webhook
[/code]

Następnie sprawdź stan środowiska wykonawczego:

bashCopy code
[code]
    openclaw voicecall status --call-id <id>openclaw voicecall tailopenclaw logs --follow
[/code]

Typowe przyczyny:

  * `publicUrl` wskazuje inną ścieżkę niż `serve.path`.
  * Adres URL tunelu zmienił się po uruchomieniu Gateway.
  * Proxy przekazuje żądanie, ale usuwa lub przepisuje nagłówki hosta albo protokołu.
  * Zapora lub DNS kieruje publiczną nazwę hosta gdzie indziej niż do Gateway.
  * Gateway został uruchomiony ponownie bez włączonego Plugin Voice Call.


Gdy przed Gateway działa odwrotne proxy lub tunel, ustaw `webhookSecurity.allowedHosts` na publiczną nazwę hosta albo użyj `webhookSecurity.trustedProxyIPs` dla znanego adresu proxy. Używaj `webhookSecurity.trustForwardingHeaders` tylko wtedy, gdy granica proxy jest pod Twoją kontrolą.

### Weryfikacja podpisu kończy się niepowodzeniem

Podpisy dostawcy są sprawdzane względem publicznego adresu URL, który OpenClaw odtwarza z przychodzącego żądania. Jeśli podpisy zawodzą:

  * Potwierdź, że adres URL Webhook dostawcy dokładnie pasuje do `publicUrl`, w tym schemat, host i ścieżkę.
  * W przypadku adresów URL darmowej warstwy ngrok zaktualizuj `publicUrl`, gdy zmieni się nazwa hosta tunelu.
  * Upewnij się, że proxy zachowuje oryginalne nagłówki hosta i protokołu, albo skonfiguruj `webhookSecurity.allowedHosts`.
  * Nie włączaj `skipSignatureVerification` poza lokalnym testowaniem.


### Dołączenia Google Meet przez Twilio zawodzą

Google Meet używa tego pluginu do dołączeń przez numer telefoniczny Twilio. Najpierw zweryfikuj Voice Call:

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall smoke --to "+15555550123"
[/code]

Następnie jawnie zweryfikuj transport Google Meet:

bashCopy code
[code]
    openclaw googlemeet setup --transport twilio
[/code]

Jeśli Voice Call jest zielony, ale uczestnik Meet nigdy nie dołącza, sprawdź numer telefoniczny Meet, PIN i `--dtmf-sequence`. Połączenie telefoniczne może być sprawne, podczas gdy spotkanie odrzuca lub ignoruje nieprawidłową sekwencję DTMF.

Google Meet uruchamia odcinek telefoniczny Twilio przez `voicecall.start` z sekwencją DTMF przed nawiązaniem połączenia. Sekwencje pochodzące z PIN-u zawierają `voiceCall.dtmfDelayMs` pluginu Google Meet jako początkowe cyfry oczekiwania Twilio. Domyślna wartość to 12 sekund, ponieważ monity dołączenia telefonicznego Meet mogą nadejść późno. Następnie Voice Call przekierowuje z powrotem do obsługi czasu rzeczywistego przed zażądaniem powitania wprowadzającego.

Użyj `openclaw logs --follow` dla śledzenia fazy na żywo. Zdrowe dołączenie Twilio Meet zapisuje w dzienniku tę kolejność:

  * Google Meet deleguje dołączenie Twilio do Voice Call.
  * Voice Call przechowuje TwiML DTMF przed nawiązaniem połączenia.
  * Początkowy TwiML Twilio jest zużywany i serwowany przed obsługą czasu rzeczywistego.
  * Voice Call serwuje TwiML czasu rzeczywistego dla połączenia Twilio.
  * Google Meet żąda mowy wprowadzającej przez `voicecall.speak` po opóźnieniu po DTMF.


`openclaw voicecall tail` nadal pokazuje utrwalone rekordy połączeń; jest przydatne dla stanu połączenia i transkrypcji, ale nie każde przejście Webhook lub czasu rzeczywistego się tam pojawia.

### Połączenie w czasie rzeczywistym nie ma mowy

Potwierdź, że włączony jest tylko jeden tryb audio. `realtime.enabled` i `streaming.enabled` nie mogą jednocześnie mieć wartości true.

Dla połączeń Twilio w czasie rzeczywistym sprawdź także:

  * Plugin dostawcy czasu rzeczywistego jest załadowany i zarejestrowany.
  * `realtime.provider` jest nieustawione albo wskazuje zarejestrowanego dostawcę.
  * Klucz API dostawcy jest dostępny dla procesu Gateway.
  * `openclaw logs --follow` pokazuje zaserwowany TwiML czasu rzeczywistego, uruchomiony most czasu rzeczywistego i początkowe powitanie dodane do kolejki.


## Powiązane

  * [Tryb rozmowy](</pl/nodes/talk>)
  * [Zamiana tekstu na mowę](</pl/tools/tts>)
  * [Wybudzanie głosowe](</pl/nodes/voicewake>)


Was this useful?YesNo
---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/pl/providers/volcengine
scraped_at: 2026-05-25
---

Dostawca Volcengine zapewnia dostęp do modeli Doubao i modeli zewnętrznych hostowanych w Volcano Engine, z oddzielnymi punktami końcowymi dla ogólnych i programistycznych obciążeń. Ten sam dołączony Plugin może również zarejestrować Volcengine Speech jako dostawcę TTS.

Szczegół | Wartość  
---|---  
Dostawcy | `volcengine` (ogólne + TTS) + `volcengine-plan` (kodowanie)  
Uwierzytelnianie modeli | `VOLCANO_ENGINE_API_KEY`  
Uwierzytelnianie TTS | `VOLCENGINE_TTS_API_KEY` lub `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | Modele zgodne z OpenAI, BytePlus Seed Speech TTS  
  
## Pierwsze kroki

* ### Ustaw klucz API

Uruchom interaktywne wdrażanie:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Spowoduje to zarejestrowanie zarówno ogólnego dostawcy (`volcengine`), jak i dostawcy do kodowania (`volcengine-plan`) przy użyciu jednego klucza API.

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Dostawcy i punkty końcowe

Dostawca | Punkt końcowy | Przypadek użycia  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Modele ogólne  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Modele do kodowania  
  
## Wbudowany katalog

### Ogólne (volcengine)

Odwołanie do modelu | Nazwa | Wejście | Kontekst  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | tekst, obraz | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | tekst, obraz | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | tekst, obraz | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | tekst, obraz | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | tekst, obraz | 128,000  
  
### Kodowanie (volcengine-plan)

Odwołanie do modelu | Nazwa | Wejście | Kontekst  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | tekst | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | tekst | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | tekst | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | tekst | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | tekst | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | tekst | 256,000  
  
## Zamiana tekstu na mowę

Volcengine TTS używa interfejsu HTTP API BytePlus Seed Speech i jest konfigurowany oddzielnie od klucza API modeli Doubao zgodnego z OpenAI. W konsoli BytePlus otwórz Seed Speech > Settings > API Keys i skopiuj klucz API, a następnie ustaw:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Następnie włącz to w `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

W przypadku miejsc docelowych dla notatek głosowych OpenClaw prosi Volcengine o natywny dla dostawcy format `ogg_opus`. W przypadku zwykłych załączników audio prosi o `mp3`. Aliasy dostawcy `bytedance` i `doubao` również wskazują tego samego dostawcę mowy.

Domyślny identyfikator zasobu to `seed-tts-1.0`, ponieważ właśnie taki BytePlus przyznaje nowo utworzonym kluczom API Seed Speech w projekcie domyślnym. Jeśli Twój projekt ma uprawnienie TTS 2.0, ustaw `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

Starsze uwierzytelnianie AppID/token nadal jest obsługiwane w przypadku starszych aplikacji Speech Console:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Konfiguracja zaawansowana

Model domyślny po wdrożeniu

`openclaw onboard --auth-choice volcengine-api-key` obecnie ustawia `volcengine-plan/ark-code-latest` jako model domyślny, jednocześnie rejestrując ogólny katalog `volcengine`.

Zachowanie awaryjne selektora modeli

Podczas wdrażania/konfiguracji wyboru modelu opcja uwierzytelniania Volcengine preferuje wiersze `volcengine/*` i `volcengine-plan/*`. Jeśli te modele nie są jeszcze załadowane, OpenClaw wraca do niefiltrowanego katalogu zamiast wyświetlać pusty selektor ograniczony do dostawcy.

Zmienne środowiskowe dla procesów demona

Jeśli Gateway działa jako demon (launchd/systemd), upewnij się, że zmienne środowiskowe modeli i TTS, takie jak `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` oraz `VOLCENGINE_TTS_TOKEN`, są dostępne dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).

## Powiązane

[**Wybór modelu** Wybór dostawców, odwołań do modeli i zachowania awaryjnego. ](</pl/concepts/model-providers>) [**Konfiguracja** Pełna dokumentacja konfiguracji agentów, modeli i dostawców. ](</pl/gateway/configuration>) [**Rozwiązywanie problemów** Typowe problemy i kroki debugowania. ](</pl/help/troubleshooting>) [**FAQ** Często zadawane pytania dotyczące konfiguracji OpenClaw. ](</pl/help/faq>)

Was this useful?YesNo
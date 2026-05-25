---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/pl/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo to platforma API dla modeli **MiMo**. OpenClaw zawiera wbudowany Plugin `xiaomi`, który rejestruje zarówno dostawcę czatu zgodnego z OpenAI, jak i dostawcę mowy (TTS) dla tego samego `XIAOMI_API_KEY`.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `xiaomi`  
Plugin | wbudowany, `enabledByDefault: true`  
Zmienna środowiskowa uwierzytelniania | `XIAOMI_API_KEY`  
Flaga wdrażania | `--auth-choice xiaomi-api-key`  
Bezpośrednia flaga CLI | `--xiaomi-api-key <key>`  
Kontrakty | uzupełnienia czatu + `speechProviders`  
API | zgodne z OpenAI (`openai-completions`)  
Bazowy adres URL | `https://api.xiaomimimo.com/v1`  
Model domyślny | `xiaomi/mimo-v2-flash`  
Domyślne TTS | `mimo-v2.5-tts`, głos `mimo_default`  
  
## Pierwsze kroki

* ### Uzyskaj klucz API

Utwórz klucz API w [konsoli Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Uruchom wdrażanie

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Możesz też przekazać klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Wbudowany katalog

Odniesienie do modelu | Wejście | Kontekst | Maks. wyjście | Rozumowanie | Uwagi  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | text | 262,144 | 8,192 | Nie | Model domyślny  
`xiaomi/mimo-v2-pro` | text | 1,048,576 | 32,000 | Tak | Duży kontekst  
`xiaomi/mimo-v2-omni` | text, image | 262,144 | 32,000 | Tak | Multimodalny  
  
## Zamiana tekstu na mowę

Wbudowany Plugin `xiaomi` rejestruje też Xiaomi MiMo jako dostawcę mowy dla `messages.tts`. Wywołuje kontrakt TTS uzupełnień czatu Xiaomi, przekazując tekst jako wiadomość `assistant` i opcjonalne wskazówki stylistyczne jako wiadomość `user`.

Właściwość | Wartość  
---|---  
Identyfikator TTS | `xiaomi` (alias `mimo`)  
Uwierzytelnianie | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` z `audio`  
Domyślne | `mimo-v2.5-tts`, głos `mimo_default`  
Wyjście | domyślnie MP3; WAV po skonfigurowaniu  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Obsługiwane wbudowane głosy obejmują `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` i `Dean`. `mimo-v2-tts` jest obsługiwany w przypadku starszych kont TTS MiMo; domyślnie używany jest bieżący model TTS MiMo-V2.5. Dla docelowych notatek głosowych, takich jak Feishu i Telegram, OpenClaw transkoduje wyjście Xiaomi do 48 kHz Opus za pomocą `ffmpeg` przed dostarczeniem.

## Przykład konfiguracji

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Zachowanie automatycznego wstrzykiwania

Dostawca `xiaomi` jest wstrzykiwany automatycznie, gdy `XIAOMI_API_KEY` jest ustawiony w środowisku lub istnieje profil uwierzytelniania. Nie musisz ręcznie konfigurować dostawcy, chyba że chcesz zastąpić metadane modelu lub bazowy adres URL.

Szczegóły modeli

  * **mimo-v2-flash** — lekki i szybki, idealny do ogólnych zadań tekstowych. Brak obsługi rozumowania.
  * **mimo-v2-pro** — obsługuje rozumowanie z oknem kontekstu 1 mln tokenów dla obciążeń związanych z długimi dokumentami.
  * **mimo-v2-omni** — model multimodalny z obsługą rozumowania, który przyjmuje zarówno dane tekstowe, jak i obrazy.

Rozwiązywanie problemów

  * Jeśli modele się nie pojawiają, upewnij się, że `XIAOMI_API_KEY` jest ustawiony i prawidłowy.
  * Gdy Gateway działa jako demon, upewnij się, że klucz jest dostępny dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).


## Powiązane

[**Wybór modelu** Wybieranie dostawców, odniesień do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji OpenClaw. ](</pl/gateway/configuration-reference>) [**Konsola Xiaomi MiMo** Panel Xiaomi MiMo i zarządzanie kluczami API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo
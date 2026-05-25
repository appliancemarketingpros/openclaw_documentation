---
title: Chutes
source_url: https://docs.openclaw.ai/pl/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) udostępnia katalogi modeli open-source przez API zgodne z OpenAI. OpenClaw obsługuje zarówno przeglądarkowe OAuth, jak i bezpośrednie uwierzytelnianie kluczem API dla dołączonego dostawcy `chutes`.

Właściwość | Wartość  
---|---  
Dostawca | `chutes`  
API | zgodne z OpenAI  
Bazowy URL | `https://llm.chutes.ai/v1`  
Uwierzytelnianie | OAuth lub klucz API (zobacz niżej)  
  
## Pierwsze kroki

### OAuth

* ### Uruchom przepływ wdrażania OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw uruchamia przepływ w przeglądarce lokalnie albo pokazuje przepływ z adresem URL i wklejeniem przekierowania na zdalnych/bezgłowych hostach. Tokeny OAuth są automatycznie odświeżane przez profile uwierzytelniania OpenClaw.

* ### Zweryfikuj domyślny model

Po wdrożeniu domyślny model jest ustawiony na `chutes/zai-org/GLM-4.7-TEE`, a dołączony katalog Chutes jest zarejestrowany.

### Klucz API

* ### Uzyskaj klucz API

Utwórz klucz na [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Uruchom przepływ wdrażania klucza API

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Zweryfikuj domyślny model

Po wdrożeniu domyślny model jest ustawiony na `chutes/zai-org/GLM-4.7-TEE`, a dołączony katalog Chutes jest zarejestrowany.

## Zachowanie wykrywania

Gdy uwierzytelnianie Chutes jest dostępne, OpenClaw odpytuje katalog Chutes przy użyciu tych poświadczeń i używa wykrytych modeli. Jeśli wykrywanie się nie powiedzie, OpenClaw wraca do dołączonego statycznego katalogu, dzięki czemu wdrażanie i uruchamianie nadal działają.

## Domyślne aliasy

OpenClaw rejestruje trzy wygodne aliasy dla dołączonego katalogu Chutes:

Alias | Model docelowy  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Wbudowany katalog startowy

Dołączony katalog awaryjny zawiera bieżące odwołania Chutes:

Odwołanie modelu  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Przykład konfiguracji

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

Nadpisania OAuth

Możesz dostosować przepływ OAuth za pomocą opcjonalnych zmiennych środowiskowych:

Zmienna | Cel  
---|---  
`CHUTES_CLIENT_ID` | Niestandardowy identyfikator klienta OAuth  
`CHUTES_CLIENT_SECRET` | Niestandardowy sekret klienta OAuth  
`CHUTES_OAUTH_REDIRECT_URI` | Niestandardowy URI przekierowania  
`CHUTES_OAUTH_SCOPES` | Niestandardowe zakresy OAuth  
  
Zobacz [dokumentację OAuth Chutes](<https://chutes.ai/docs/sign-in-with-chutes/overview>), aby poznać wymagania dotyczące aplikacji przekierowującej i uzyskać pomoc.

Uwagi

  * Wykrywanie za pomocą klucza API i OAuth używa tego samego identyfikatora dostawcy `chutes`.
  * Modele Chutes są rejestrowane jako `chutes/<model-id>`.
  * Jeśli wykrywanie nie powiedzie się podczas uruchamiania, dołączony statyczny katalog zostanie użyty automatycznie.


## Powiązane

[**Wybór modelu** Reguły dostawców, odwołania modeli i zachowanie przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełny schemat konfiguracji, w tym ustawienia dostawców. ](</pl/gateway/configuration-reference>) [**Chutes** Panel Chutes i dokumentacja API. ](<https://chutes.ai>) [**Klucze API Chutes** Twórz klucze API Chutes i zarządzaj nimi. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo
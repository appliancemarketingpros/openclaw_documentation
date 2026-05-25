---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/pl/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway udostępnia **ujednolicony interfejs API** , który kieruje żądania do wielu modeli za jednym punktem końcowym i kluczem API. Jest zgodny z OpenAI, więc większość SDK OpenAI działa po zmianie bazowego adresu URL.

Właściwość | Wartość  
---|---  
Dostawca | `kilocode`  
Uwierzytelnianie | `KILOCODE_API_KEY`  
API | Zgodne z OpenAI  
Bazowy adres URL | `https://api.kilo.ai/api/gateway/`  
  
## Pierwsze kroki

* ### Utwórz konto

Przejdź do [app.kilo.ai](<https://app.kilo.ai>), zaloguj się lub utwórz konto, a następnie przejdź do API Keys i wygeneruj nowy klucz.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Albo ustaw zmienną środowiskową bezpośrednio:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Model domyślny

Domyślnym modelem jest `kilocode/kilo/auto`, zarządzany przez dostawcę model inteligentnego routingu obsługiwany przez Kilo Gateway.

## Wbudowany katalog

OpenClaw dynamicznie wykrywa dostępne modele z Kilo Gateway podczas uruchamiania. Użyj `/models kilocode`, aby zobaczyć pełną listę modeli dostępnych na Twoim koncie.

Każdy model dostępny w Gateway może być używany z prefiksem `kilocode/`:

Referencja modelu | Uwagi  
---|---  
`kilocode/kilo/auto` | Domyślny — inteligentny routing  
`kilocode/anthropic/claude-sonnet-4` | Anthropic przez Kilo  
`kilocode/openai/gpt-5.5` | OpenAI przez Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google przez Kilo  
...i wiele innych | Użyj `/models kilocode`, aby wyświetlić wszystkie  
  
## Przykład konfiguracji

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport i zgodność

Kilo Gateway jest udokumentowany w źródle jako zgodny z OpenRouter, więc pozostaje na ścieżce proxy zgodnej z OpenAI zamiast używać natywnego kształtowania żądań OpenAI.

  * Referencje Kilo oparte na Gemini pozostają na ścieżce proxy Gemini, więc OpenClaw zachowuje tam sanityzację sygnatur myśli Gemini bez włączania natywnej walidacji odtwarzania Gemini ani przepisywania bootstrapu.
  * Kilo Gateway używa tokenu Bearer z Twoim kluczem API pod spodem.

Opakowanie strumienia i reasoning

Wspólne opakowanie strumienia Kilo dodaje nagłówek aplikacji dostawcy i normalizuje ładunki reasoning proxy dla obsługiwanych konkretnych referencji modeli.

Rozwiązywanie problemów

  * Jeśli wykrywanie modeli nie powiedzie się podczas uruchamiania, OpenClaw wraca do dołączonego statycznego katalogu zawierającego `kilocode/kilo/auto`.
  * Potwierdź, że Twój klucz API jest prawidłowy i że Twoje konto Kilo ma włączone żądane modele.
  * Gdy Gateway działa jako daemon, upewnij się, że `KILOCODE_API_KEY` jest dostępny dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).


## Powiązane

[**Wybór modelu** Wybór dostawców, referencji modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji OpenClaw. ](</pl/gateway/configuration-reference>) [**Kilo Gateway** Panel Kilo Gateway, klucze API i zarządzanie kontem. ](<https://app.kilo.ai>)

Was this useful?YesNo
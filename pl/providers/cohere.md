---
title: Cohere
source_url: https://docs.openclaw.ai/pl/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) zapewnia wnioskowanie zgodne z OpenAI przez swój Compatibility API. OpenClaw dostarcza dostawcę Cohere podczas przejścia na eksternalizację, a także publikuje go jako oficjalny zewnętrzny plugin z katalogiem modeli Command A.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `cohere`  
Plugin | dołączony w okresie przejściowym; oficjalny pakiet zewnętrzny  
Zmienna środowiskowa uwierzytelniania | `COHERE_API_KEY`  
Flaga wdrożenia | `--auth-choice cohere-api-key`  
Bezpośrednia flaga CLI | `--cohere-api-key <key>`  
API | zgodne z OpenAI (`openai-completions`)  
Bazowy adres URL | `https://api.cohere.ai/compatibility/v1`  
Model domyślny | `cohere/command-a-03-2025`  
  
## Pierwsze kroki

  1. Cohere jest zawarty w bieżących pakietach OpenClaw. Jeśli jest niedostępny, zainstaluj zewnętrzny pakiet i uruchom ponownie Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Utwórz klucz API Cohere.
  3. Uruchom wdrożenie:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Potwierdź, że katalog jest dostępny:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Model domyślny jest ustawiany tylko wtedy, gdy nie skonfigurowano jeszcze modelu podstawowego.

## Konfiguracja tylko przez środowisko

Udostępnij `COHERE_API_KEY` procesowi Gateway, a następnie wybierz model Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Powiązane

  * [Dostawcy modeli](</pl/concepts/model-providers>)
  * [CLI modeli](</pl/cli/models>)
  * [Katalog dostawców](</pl/providers>)


Was this useful?YesNo

Open issue
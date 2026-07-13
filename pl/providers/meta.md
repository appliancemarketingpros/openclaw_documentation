---
title: Meta
source_url: https://docs.openclaw.ai/pl/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** korzysta ze zgodnego z OpenAI interfejsu **Responses API** (`POST /v1/responses`) dla modelu rozumowania `muse-spark-1.1`. Dostawca jest dystrybuowany jako wbudowany plugin OpenClaw.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `meta`  
Plugin | wbudowany dostawca  
Zmienna środowiskowa uwierzytelniania | `MODEL_API_KEY`  
Flaga wdrażania | `--auth-choice meta-api-key`  
Bezpośrednia flaga CLI | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
Bazowy adres URL | `https://api.meta.ai/v1`  
Model domyślny | `meta/muse-spark-1.1`  
Domyślny poziom rozumowania | `high` (`reasoning.effort`)  
  
## Pierwsze kroki

* ### Ustaw klucz API

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Sprawdź dostępność modeli

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Wyświetla statyczny wpis katalogu `muse-spark-1.1`. Jeśli nie można rozpoznać `MODEL_API_KEY`, polecenie `openclaw models status --json` zgłasza brakujące dane uwierzytelniające w `auth.unusableProfiles`.

## Konfiguracja nieinteraktywna

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Wbudowany katalog

Odwołanie do modelu | Nazwa | Rozumowanie | Okno kontekstu | Maks. wynik  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | tak | 1,048,576 | 131,072  
  
Możliwości:

  * Dane wejściowe w postaci tekstu i obrazów
  * Wywoływanie narzędzi i strumieniowanie
  * Poziom rozumowania: `minimal`, `low`, `medium`, `high`, `xhigh` (domyślnie: `high`)
  * Bezstanowe odtwarzanie zaszyfrowanego rozumowania (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Konfiguracja ręczna

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Test dymny

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Testy na żywo używają modelu `muse-spark-1.1` z żądaniami do `POST /v1/responses`.

## Powiązane

[**Dostawcy modeli** Wybieranie dostawców, odwołań do modeli i sposobu przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Tryby myślenia** Poziomy intensywności rozumowania dla modelu muse-spark-1.1. ](</pl/tools/thinking>) [**Dokumentacja konfiguracji** Domyślne ustawienia agentów i konfiguracja modeli. ](</pl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue
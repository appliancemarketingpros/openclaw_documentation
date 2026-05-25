---
title: Zadanie LLM
source_url: https://docs.openclaw.ai/pl/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` to **opcjonalne narzędzie pluginu** , które uruchamia zadanie LLM zwracające wyłącznie JSON i zwraca ustrukturyzowane dane wyjściowe (opcjonalnie walidowane względem JSON Schema).

To idealne rozwiązanie dla silników przepływów pracy, takich jak Lobster: możesz dodać pojedynczy krok LLM bez pisania niestandardowego kodu OpenClaw dla każdego przepływu pracy.

## Włącz plugin

  1. Włącz plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Zezwól na opcjonalne narzędzie:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Używaj `tools.allow` tylko wtedy, gdy chcesz restrykcyjnego trybu listy dozwolonych.

## Konfiguracja (opcjonalna)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` to lista dozwolonych ciągów `provider/model`. Jeśli jest ustawiona, każde żądanie spoza listy zostanie odrzucone.

## Parametry narzędzia

  * `prompt` (ciąg, wymagany)
  * `input` (dowolny, opcjonalny)
  * `schema` (obiekt, opcjonalny JSON Schema)
  * `provider` (ciąg, opcjonalny)
  * `model` (ciąg, opcjonalny)
  * `thinking` (ciąg, opcjonalny)
  * `authProfileId` (ciąg, opcjonalny)
  * `temperature` (liczba, opcjonalna)
  * `maxTokens` (liczba, opcjonalna)
  * `timeoutMs` (liczba, opcjonalna)


`thinking` akceptuje standardowe presety rozumowania OpenClaw, takie jak `low` lub `medium`.

## Dane wyjściowe

Zwraca `details.json` zawierający przeanalizowany JSON (i waliduje względem `schema`, jeśli ją podano).

## Przykład: krok przepływu pracy Lobster

### Ważne ograniczenie

Poniższy przykład zakłada, że **samodzielny Lobster CLI** działa w środowisku, w którym `openclaw.invoke` ma już poprawny adres URL Gateway/kontekst uwierzytelniania.

Dla dołączonego **osadzonego** runnera Lobster wewnątrz OpenClaw ten wzorzec zagnieżdżonego CLI **nie jest obecnie niezawodny** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Dopóki osadzony Lobster nie będzie mieć obsługiwanego mostu dla tego przepływu, preferuj jedno z poniższych rozwiązań:

  * bezpośrednie wywołania narzędzia `llm-task` poza Lobster albo
  * kroki Lobster, które nie polegają na zagnieżdżonych wywołaniach `openclaw.invoke`.


Przykład samodzielnego Lobster CLI:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Uwagi dotyczące bezpieczeństwa

  * Narzędzie zwraca **wyłącznie JSON** i instruuje model, aby zwracał tylko JSON (bez bloków kodu, bez komentarzy).
  * W tym uruchomieniu żadne narzędzia nie są udostępniane modelowi.
  * Traktuj dane wyjściowe jako niezaufane, chyba że walidujesz je za pomocą `schema`.
  * Umieść zatwierdzenia przed każdym krokiem wywołującym skutki uboczne (wysyłanie, publikowanie, wykonywanie).


## Powiązane

  * [Poziomy rozumowania](</pl/tools/thinking>)
  * [Subagenci](</pl/tools/subagents>)
  * [Polecenia z ukośnikiem](</pl/tools/slash-commands>)


Was this useful?YesNo
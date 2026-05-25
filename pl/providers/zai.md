---
title: Z.AI
source_url: https://docs.openclaw.ai/pl/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) to platforma API dla modeli **GLM**. Udostępnia interfejsy REST API dla GLM i używa kluczy API do uwierzytelniania. Utwórz klucz API w konsoli [Z.AI](<http://Z.AI>). OpenClaw używa providera `zai` z kluczem API [Z.AI](<http://Z.AI>).

  * Provider: `zai`
  * Uwierzytelnianie: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (uwierzytelnianie Bearer)


## Pierwsze kroki

### Automatyczne wykrywanie punktu końcowego

**Najlepsze dla:** większości użytkowników. OpenClaw wykrywa pasujący punkt końcowy [Z.AI](<http://Z.AI>) na podstawie klucza i automatycznie stosuje prawidłowy bazowy adres URL.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Sprawdź, czy model jest na liście

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Jawny regionalny punkt końcowy

**Najlepsze dla:** użytkowników, którzy chcą wymusić konkretny Coding Plan albo ogólną powierzchnię API.

* ### Wybierz właściwą opcję onboardingu

bashCopy code
[code]
    # Coding Plan Global (zalecane dla użytkowników Coding Plan)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (region Chin)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (region Chin)openclaw onboard --auth-choice zai-cn
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Sprawdź, czy model jest na liście

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Wbudowany katalog

OpenClaw dostarcza dołączony katalog providera `zai` w manifeście Plugin, więc lista tylko do odczytu może pokazywać znane wiersze GLM bez ładowania środowiska uruchomieniowego providera:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Katalog oparty na manifeście obecnie obejmuje:

Odwołanie do modelu | Uwagi  
---|---  
`zai/glm-5.1` | Model domyślny  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Konfiguracja zaawansowana

Rozwiązywanie w przód nieznanych modeli GLM-5

Nieznane identyfikatory `glm-5*` nadal są rozwiązywane w przód na ścieżce dołączonego providera przez syntetyzowanie metadanych należących do providera z szablonu `glm-4.7`, gdy identyfikator pasuje do bieżącego kształtu rodziny GLM-5.

Strumieniowanie wywołań narzędzi

`tool_stream` jest domyślnie włączone dla strumieniowania wywołań narzędzi [Z.AI](<http://Z.AI>). Aby je wyłączyć:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Myślenie i zachowane myślenie

Myślenie [Z.AI](<http://Z.AI>) podąża za kontrolkami `/think` OpenClaw. Gdy myślenie jest wyłączone, OpenClaw wysyła `thinking: { type: "disabled" }`, aby uniknąć odpowiedzi, które zużywają budżet wyjściowy na `reasoning_content` przed widocznym tekstem.

Zachowane myślenie jest opcjonalne, ponieważ [Z.AI](<http://Z.AI>) wymaga odtworzenia pełnej historycznej zawartości `reasoning_content`, co zwiększa liczbę tokenów promptu. Włącz je dla modelu:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Gdy jest włączone i myślenie jest aktywne, OpenClaw wysyła `thinking: { type: "enabled", clear_thinking: false }` i odtwarza wcześniejsze `reasoning_content` dla tego samego transkryptu zgodnego z OpenAI.

Zaawansowani użytkownicy nadal mogą nadpisać dokładny ładunek providera za pomocą `params.extra_body.thinking`.

Rozumienie obrazów

Dołączony Plugin [Z.AI](<http://Z.AI>) rejestruje rozumienie obrazów.

Właściwość | Wartość  
---|---  
Model | `glm-4.6v`  
  
Rozumienie obrazów jest automatycznie rozwiązywane na podstawie skonfigurowanego uwierzytelniania [Z.AI](<http://Z.AI>) — nie jest potrzebna dodatkowa konfiguracja.

Szczegóły uwierzytelniania

  * [Z.AI](<http://Z.AI>) używa uwierzytelniania Bearer z Twoim kluczem API.
  * Opcja onboardingu `zai-api-key` automatycznie wykrywa pasujący punkt końcowy [Z.AI](<http://Z.AI>) na podstawie prefiksu klucza.
  * Użyj jawnych opcji regionalnych (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`), gdy chcesz wymusić konkretną powierzchnię API.


## Powiązane

[**Rodzina modeli GLM** Przegląd rodziny modeli GLM. ](</pl/providers/glm>) [**Wybór modelu** Wybieranie providerów, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>)

Was this useful?YesNo
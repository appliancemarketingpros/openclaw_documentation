---
title: Arcee AI
source_url: https://docs.openclaw.ai/pl/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) zapewnia dostęp do rodziny modeli Trinity typu mixture-of-experts przez API zgodne z OpenAI. Wszystkie modele Trinity są objęte licencją Apache 2.0.

Do modeli Arcee AI można uzyskać dostęp bezpośrednio przez platformę Arcee lub przez [OpenRouter](</pl/providers/openrouter>).

Właściwość | Wartość  
---|---  
Dostawca | `arcee`  
Uwierzytelnianie | `ARCEEAI_API_KEY` (bezpośrednio) lub `OPENROUTER_API_KEY` (przez OpenRouter)  
API | Zgodne z OpenAI  
Bazowy URL | `https://api.arcee.ai/api/v1` (bezpośrednio) lub `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Pierwsze kroki

### Bezpośrednio (platforma Arcee)

* ### Uzyskaj klucz API

Utwórz klucz API w [Arcee AI](<https://chat.arcee.ai/>).

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Ustaw domyślny model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Przez OpenRouter

* ### Uzyskaj klucz API

Utwórz klucz API w [OpenRouter](<https://openrouter.ai/keys>).

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Ustaw domyślny model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Te same odwołania do modeli działają zarówno w konfiguracji bezpośredniej, jak i przez OpenRouter (na przykład `arcee/trinity-large-thinking`).

## Konfiguracja nieinteraktywna

### Bezpośrednio (platforma Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Przez OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Wbudowany katalog

OpenClaw obecnie dostarcza ten dołączony katalog Arcee:

Odwołanie do modelu | Nazwa | Wejście | Kontekst | Koszt (wej./wyj. za 1 mln) | Uwagi  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | Model domyślny; włączone rozumowanie  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | Ogólnego przeznaczenia; 400 mld parametrów, 13 mld aktywnych  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | Szybki i opłacalny; wywoływanie funkcji  
  
## Obsługiwane funkcje

Funkcja | Obsługiwane  
---|---  
Streaming | Tak  
Użycie narzędzi / wywoływanie funkcji | Tak (Trinity Mini, Trinity Large Preview)  
Dane wyjściowe strukturalne (tryb JSON i schemat JSON) | Tak  
Rozszerzone myślenie | Tak (Trinity Large Thinking; narzędzia wyłączone)  
  
Uwaga dotycząca środowiska

Jeśli Gateway działa jako demon (launchd/systemd), upewnij się, że `ARCEEAI_API_KEY` (lub `OPENROUTER_API_KEY`) jest dostępny dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).

Routing OpenRouter

Gdy używasz modeli Arcee przez OpenRouter, obowiązują te same odwołania do modeli `arcee/*`. OpenClaw obsługuje routing przejrzyście na podstawie wybranego uwierzytelniania. Szczegóły konfiguracji specyficzne dla OpenRouter znajdziesz w [dokumentacji dostawcy OpenRouter](</pl/providers/openrouter>).

## Powiązane

[**OpenRouter** Uzyskaj dostęp do modeli Arcee i wielu innych za pomocą jednego klucza API. ](</pl/providers/openrouter>) [**Wybór modelu** Wybór dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>)

Was this useful?YesNo
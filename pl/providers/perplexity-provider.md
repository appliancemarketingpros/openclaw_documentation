---
title: Perplexity
source_url: https://docs.openclaw.ai/pl/providers/perplexity-provider
scraped_at: 2026-05-25
---

Plugin Perplexity zapewnia funkcje wyszukiwania w sieci za pośrednictwem Perplexity Search API lub Perplexity Sonar przez OpenRouter.

Właściwość | Wartość  
---|---  
Typ | Dostawca wyszukiwania w sieci (nie dostawca modelu)  
Uwierzytelnianie | `PERPLEXITY_API_KEY` (bezpośrednio) lub `OPENROUTER_API_KEY` (przez OpenRouter)  
Ścieżka konfiguracji | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Pierwsze kroki

* ### Ustaw klucz API

Uruchom interaktywny przepływ konfiguracji wyszukiwania w sieci:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Albo ustaw klucz bezpośrednio:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Rozpocznij wyszukiwanie

Agent automatycznie będzie używać Perplexity do wyszukiwań w sieci, gdy klucz zostanie skonfigurowany. Nie są wymagane żadne dodatkowe kroki.

## Tryby wyszukiwania

Plugin automatycznie wybiera transport na podstawie prefiksu klucza API:

### Natywne Perplexity API (pplx-)

Gdy klucz zaczyna się od `pplx-`, OpenClaw używa natywnego Perplexity Search API. Ten transport zwraca uporządkowane wyniki i obsługuje filtry domeny, języka oraz daty (zobacz opcje filtrowania poniżej).

### OpenRouter / Sonar (sk-or-)

Gdy klucz zaczyna się od `sk-or-`, OpenClaw kieruje zapytania przez OpenRouter z użyciem modelu Perplexity Sonar. Ten transport zwraca odpowiedzi zsyntetyzowane przez AI wraz z cytowaniami.

Prefiks klucza | Transport | Funkcje  
---|---|---  
`pplx-` | Natywne Perplexity Search API | Uporządkowane wyniki, filtry domeny/języka/daty  
`sk-or-` | OpenRouter (Sonar) | Odpowiedzi zsyntetyzowane przez AI z cytowaniami  
  
## Filtrowanie w natywnym API

Podczas używania natywnego Perplexity API wyszukiwania obsługują następujące filtry:

Filtr | Opis | Przykład  
---|---|---  
Kraj | 2-literowy kod kraju | `us`, `de`, `jp`  
Język | Kod języka ISO 639-1 | `en`, `fr`, `zh`  
Zakres dat | Okno aktualności | `day`, `week`, `month`, `year`  
Filtry domen | Lista dozwolonych lub blokowanych domen (maks. 20 domen) | `example.com`  
Budżet treści | Limity tokenów na odpowiedź / na stronę | `max_tokens`, `max_tokens_per_page`  
  
## Konfiguracja zaawansowana

Zmienna środowiskowa dla procesów daemon

Jeśli OpenClaw Gateway działa jako daemon (launchd/systemd), upewnij się, że `PERPLEXITY_API_KEY` jest dostępny dla tego procesu.

Konfiguracja proxy OpenRouter

Jeśli wolisz kierować wyszukiwania Perplexity przez OpenRouter, ustaw `OPENROUTER_API_KEY` (prefiks `sk-or-`) zamiast natywnego klucza Perplexity. OpenClaw wykryje prefiks i automatycznie przełączy się na transport Sonar.

## Powiązane

[**Narzędzie wyszukiwania Perplexity** Jak agent wywołuje wyszukiwania Perplexity i interpretuje wyniki. ](</pl/tools/perplexity-search>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji, w tym wpisy Plugin. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo
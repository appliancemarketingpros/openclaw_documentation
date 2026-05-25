---
title: Wyszukiwanie Exa
source_url: https://docs.openclaw.ai/pl/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw obsługuje [Exa AI](<https://exa.ai/>) jako dostawcę `web_search`. Exa oferuje neuronowe, słowokluczowe i hybrydowe tryby wyszukiwania z wbudowaną ekstrakcją treści (wyróżnienia, tekst, podsumowania).

## Uzyskaj klucz API

* ### Utwórz konto

Zarejestruj się na [exa.ai](<https://exa.ai/>) i wygeneruj klucz API w swoim panelu.

* ### Zapisz klucz

Ustaw `EXA_API_KEY` w środowisku Gateway albo skonfiguruj za pomocą:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfiguracja

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Alternatywa środowiskowa:** ustaw `EXA_API_KEY` w środowisku Gateway. W przypadku instalacji gateway umieść go w `~/.openclaw/.env`.

## Nadpisanie bazowego adresu URL

Ustaw `plugins.entries.exa.config.webSearch.baseUrl`, gdy żądania wyszukiwania Exa mają przechodzić przez zgodny serwer proxy lub alternatywny punkt końcowy Exa. OpenClaw normalizuje same hosty, dodając na początku `https://`, i dodaje `/search`, chyba że ścieżka już się tam kończy. Rozwiązany punkt końcowy jest uwzględniany w kluczu pamięci podręcznej wyszukiwania, więc wyniki z różnych punktów końcowych Exa nie są współdzielone.

## Parametry narzędzia

Zapytanie wyszukiwania.

Wyniki do zwrócenia (1–100).

Tryb wyszukiwania.

Filtr czasu.

Wyniki po tej dacie (`YYYY-MM-DD`).

Wyniki przed tą datą (`YYYY-MM-DD`).

Opcje ekstrakcji treści (zobacz niżej).

### Ekstrakcja treści

Exa może zwracać wyodrębnioną treść obok wyników wyszukiwania. Przekaż obiekt `contents`, aby ją włączyć:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Opcja zawartości | Typ | Opis  
---|---|---  
`text` | `boolean | { maxCharacters }` | Wyodrębnij pełny tekst strony  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Wyodrębnij kluczowe zdania  
`summary` | `boolean | { query }` | Podsumowanie wygenerowane przez AI  
  
### Tryby wyszukiwania

Tryb | Opis  
---|---  
`auto` | Exa wybiera najlepszy tryb (domyślnie)  
`neural` | Wyszukiwanie semantyczne/oparte na znaczeniu  
`fast` | Szybkie wyszukiwanie słów kluczowych  
`deep` | Dokładne głębokie wyszukiwanie  
`deep-reasoning` | Głębokie wyszukiwanie z rozumowaniem  
`instant` | Najszybsze wyniki  
  
## Uwagi

  * Jeśli nie podano opcji `contents`, Exa domyślnie używa `{ highlights: true }`, więc wyniki zawierają fragmenty kluczowych zdań
  * Wyniki zachowują pola `highlightScores` i `summary` z odpowiedzi Exa API, gdy są dostępne
  * Opisy wyników są rozwiązywane najpierw z wyróżnień, następnie z podsumowania, a potem z pełnego tekstu — zależnie od tego, co jest dostępne
  * `freshness` oraz `date_after`/`date_before` nie mogą być łączone — użyj jednego trybu filtrowania czasu
  * Na jedno zapytanie można zwrócić do 100 wyników (z zastrzeżeniem limitów typu wyszukiwania Exa)
  * Wyniki są domyślnie buforowane przez 15 minut (konfigurowalne przez `cacheTtlMinutes`)
  * Exa to oficjalna integracja API ze strukturalnymi odpowiedziami JSON


## Powiązane

  * [Omówienie Web Search](</pl/tools/web>) \-- wszyscy dostawcy i automatyczne wykrywanie
  * [Brave Search](</pl/tools/brave-search>) \-- strukturalne wyniki z filtrami kraju/języka
  * [Perplexity Search](</pl/tools/perplexity-search>) \-- strukturalne wyniki z filtrowaniem domen


Was this useful?YesNo
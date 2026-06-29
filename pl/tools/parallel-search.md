---
title: Wyszukiwanie równoległe
source_url: https://docs.openclaw.ai/pl/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

Plugin Parallel udostępnia dwóch dostawców `web_search` [Parallel](<https://parallel.ai/>):

  * **Parallel Search (Free)** (`parallel-free`) -- bezpłatny [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>) od Parallel. Nie wymaga konta ani klucza API. Wybierz go jawnie, gdy chcesz użyć hostowanej przez Parallel ścieżki wyszukiwania bez klucza.
  * **Parallel Search** (`parallel`) -- płatne Search API od Parallel. Wymaga `PARALLEL_API_KEY` i oferuje wyższe limity szybkości oraz dostrajanie celu.


Oba zwracają uszeregowane, zoptymalizowane pod LLM fragmenty z indeksu internetowego zbudowanego dla agentów AI. Ustaw `tools.web.search.provider` na `parallel-free` albo `parallel`, aby wybrać jedno jawnie.

## Instalacja Plugin

Zainstaluj oficjalny plugin, a następnie uruchom ponownie Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## Klucz API (płatny dostawca)

`parallel-free` nie wymaga klucza API, ale nadal musi zostać wybrany jako zarządzany dostawca. Płatny dostawca `parallel` wymaga klucza API:

* ### Utwórz konto

Zarejestruj się na [platform.parallel.ai](<https://platform.parallel.ai>) i wygeneruj klucz API z panelu.

* ### Przechowaj klucz

Ustaw `PARALLEL_API_KEY` w środowisku Gateway albo skonfiguruj przez:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfiguracja

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**Alternatywa środowiskowa:** ustaw `PARALLEL_API_KEY` w środowisku Gateway. W przypadku instalacji gateway umieść go w `~/.openclaw/.env`.

## Nadpisanie bazowego adresu URL

Nadpisanie bazowego adresu URL dotyczy tylko płatnego dostawcy `parallel`. Bezpłatny dostawca `parallel-free` zawsze używa `https://search.parallel.ai/mcp`.

Ustaw `plugins.entries.parallel.config.webSearch.baseUrl`, gdy żądania Parallel mają przechodzić przez zgodny serwer proxy albo alternatywny punkt końcowy Parallel (na przykład Cloudflare AI Gateway). OpenClaw normalizuje same hosty przez dodanie na początku `https://` i dopisuje `/v1/search`, chyba że ścieżka już się tak kończy. Rozwiązany punkt końcowy jest uwzględniany w kluczu pamięci podręcznej wyszukiwania, więc wyniki z różnych punktów końcowych Parallel nie są współdzielone.

## Parametry narzędzia

OpenClaw udostępnia natywny kształt wyszukiwania Parallel, aby model mógł wypełnić zarówno cel w języku naturalnym, jak i kilka krótkich zapytań słów kluczowych — zestawienie, które Parallel [zaleca](<https://docs.parallel.ai/search/best-practices>), aby uzyskać najlepsze wyniki.

Opis bazowego pytania lub celu w języku naturalnym (maks. 5000 znaków). Powinien być samowystarczalny.

Zwięzłe zapytania wyszukiwania słów kluczowych, po 3-6 słów każde (1-5 pozycji, maks. 200 znaków każde). Podaj 2-3 zróżnicowane zapytania, aby uzyskać najlepsze wyniki.

Liczba wyników do zwrócenia (1-40).

Opcjonalny identyfikator sesji Parallel (maks. 1000 znaków dla `parallel`; bezpłatny Search MCP `parallel-free` ogranicza go do 100). Przekaż `sessionId` z poprzedniego wyniku Parallel w kolejnych wyszukiwaniach należących do tego samego zadania, aby Parallel mógł grupować powiązane wywołania i poprawiać kolejne wyniki. Identyfikator przekraczający limit jest odrzucany i generowany jest nowy.

Opcjonalny identyfikator modelu wykonującego wywołanie (np. `claude-opus-4-7`, `gpt-5.5`). Pozwala Parallel dopasować domyślne ustawienia do możliwości Twojego modelu. Przekaż dokładny slug aktywnego modelu; nie skracaj do aliasu rodziny.

## Uwagi

  * Parallel szereguje i kompresuje wyniki na podstawie przydatności dla rozumowania LLM, a nie kliknięć użytkowników; oczekuj gęstych fragmentów w każdym wyniku zamiast pełnej treści strony
  * Fragmenty wyników wracają jako tablica `excerpts` i są też łączone w polu `description` dla zgodności z ogólnym kontraktem `web_search`
  * Parallel zwraca `session_id` w każdej odpowiedzi; OpenClaw udostępnia go jako `sessionId` w ładunku narzędzia, aby wywołujący mogli grupować kolejne wyszukiwania
  * `searchId`, `warnings` i `usage` z Parallel są przekazywane dalej, gdy są obecne
  * OpenClaw zawsze przekazuje do Parallel rozwiązaną liczbę wyników jako `advanced_settings.max_results`. Argument `count` wywołującego ma pierwszeństwo, potem ustawienie najwyższego poziomu `tools.web.search.maxResults`, a w przeciwnym razie ogólna wartość domyślna `web_search` OpenClaw (5). Dzięki temu wolumen wyników pozostaje spójny podczas przełączania między dostawcami; sam Parallel domyślnie używa 10
  * Wyniki są domyślnie buforowane przez 15 minut (konfigurowalne przez `cacheTtlMinutes`)
  * Bezpłatny dostawca `parallel-free` akceptuje te same parametry. Stosuje `count` po stronie klienta i generuje `session_id` dla każdego wywołania, gdy nie zostanie podany.


## Powiązane

  * [Omówienie Web Search](</pl/tools/web>) \-- wszyscy dostawcy i automatyczne wykrywanie
  * [Wyszukiwanie Exa](</pl/tools/exa-search>) \-- wyszukiwanie neuronowe z ekstrakcją treści
  * [Perplexity Search](</pl/tools/perplexity-search>) \-- strukturyzowane wyniki z filtrowaniem domen


Was this useful?YesNo

Open issue
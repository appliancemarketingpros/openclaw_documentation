---
title: Wyszukiwanie MiniMax
source_url: https://docs.openclaw.ai/pl/tools/minimax-search
scraped_at: 2026-05-25
---

OpenClaw obsługuje MiniMax jako dostawcę `web_search` za pośrednictwem interfejsu API wyszukiwania MiniMax Token Plan. Zwraca ustrukturyzowane wyniki wyszukiwania z tytułami, URL-ami, fragmentami i powiązanymi zapytaniami.

## Uzyskaj dane uwierzytelniające Token Plan

* ### Utwórz klucz

Utwórz lub skopiuj klucz MiniMax Token Plan z [MiniMax Platform](<https://platform.minimax.io/user-center/basic-information/interface-key>). Konfiguracje OAuth mogą zamiast tego ponownie użyć `MINIMAX_OAUTH_TOKEN`.

* ### Zapisz klucz

Ustaw `MINIMAX_CODE_PLAN_KEY` w środowisku Gateway albo skonfiguruj za pomocą:

bashCopy code
[code]
    openclaw configure --section web
[/code]

OpenClaw akceptuje również `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` i `MINIMAX_API_KEY` jako aliasy zmiennych środowiskowych. `MINIMAX_API_KEY` powinien wskazywać na dane uwierzytelniające Token Plan z włączonym wyszukiwaniem; zwykłe klucze API modeli MiniMax mogą nie zostać zaakceptowane przez punkt końcowy wyszukiwania Token Plan.

## Konfiguracja

json5Copy code
[code]
    {  plugins: {    entries: {      minimax: {        config: {          webSearch: {            apiKey: "sk-cp-...", // optional if a MiniMax Token Plan env var is set            region: "global", // or "cn"          },        },      },    },  },  tools: {    web: {      search: {        provider: "minimax",      },    },  },}
[/code]

**Alternatywa środowiskowa:** ustaw `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` albo `MINIMAX_API_KEY` w środowisku Gateway. W przypadku instalacji gateway umieść ją w `~/.openclaw/.env`.

## Wybór regionu

MiniMax Search używa następujących punktów końcowych:

  * Globalny: `https://api.minimax.io/v1/coding_plan/search`
  * CN: `https://api.minimaxi.com/v1/coding_plan/search`


Jeśli `plugins.entries.minimax.config.webSearch.region` nie jest ustawione, OpenClaw rozwiązuje region w następującej kolejności:

  1. `tools.web.search.minimax.region` / należące do pluginu `webSearch.region`
  2. `MINIMAX_API_HOST`
  3. `models.providers.minimax.baseUrl`
  4. `models.providers.minimax-portal.baseUrl`


Oznacza to, że wdrażanie CN albo `MINIMAX_API_HOST=https://api.minimaxi.com/...` automatycznie utrzymuje MiniMax Search również na hoście CN.

Nawet jeśli uwierzytelniono MiniMax przez ścieżkę OAuth `minimax-portal`, wyszukiwanie w sieci nadal rejestruje się z identyfikatorem dostawcy `minimax`; bazowy URL dostawcy OAuth jest używany jako wskazówka regionu do wyboru hosta CN/global, a `MINIMAX_OAUTH_TOKEN` może spełniać wymagania danych uwierzytelniających bearer dla MiniMax Search.

## Obsługiwane parametry

Parametr | Typ | Ograniczenia | Opis  
---|---|---|---  
`query` | string | wymagany | Ciąg zapytania wyszukiwania.  
`count` | integer | 1-10 | Liczba wyników do zwrócenia. OpenClaw przycina zwróconą listę do tego rozmiaru.  
  
Filtry specyficzne dla dostawcy nie są obecnie obsługiwane.

## Powiązane

  * [Omówienie Web Search](</pl/tools/web>) \-- wszyscy dostawcy i automatyczne wykrywanie
  * [MiniMax](</pl/providers/minimax>) \-- konfiguracja modeli, obrazów, mowy i uwierzytelniania


Was this useful?YesNo
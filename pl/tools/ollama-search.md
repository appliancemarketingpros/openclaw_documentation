---
title: Wyszukiwanie internetowe Ollama
source_url: https://docs.openclaw.ai/pl/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw obsługuje **Ollama Web Search** jako wbudowanego dostawcę `web_search`. Używa interfejsu API wyszukiwania w sieci Ollama i zwraca uporządkowane wyniki z tytułami, adresami URL oraz fragmentami.

W przypadku lokalnej lub samodzielnie hostowanej Ollama ta konfiguracja domyślnie nie wymaga klucza API. Wymaga natomiast:

  * hosta Ollama osiągalnego z OpenClaw
  * `ollama signin`


W przypadku bezpośredniego wyszukiwania hostowanego ustaw bazowy adres URL dostawcy Ollama na `https://ollama.com` i podaj prawdziwy `OLLAMA_API_KEY`.

## Konfiguracja

* ### Uruchom Ollama

Upewnij się, że Ollama jest zainstalowana i uruchomiona.

* ### Zaloguj się

Uruchom:

bashCopy code
[code]
    ollama signin
[/code]

* ### Wybierz Ollama Web Search

Uruchom:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Następnie wybierz **Ollama Web Search** jako dostawcę.

Jeśli używasz już Ollama do modeli, Ollama Web Search ponownie wykorzystuje ten sam skonfigurowany host.

## Konfiguracja

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Opcjonalne zastąpienie hosta Ollama:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Jeśli Ollama jest już skonfigurowana jako dostawca modeli, dostawca wyszukiwania w sieci może zamiast tego ponownie użyć tego hosta:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Dostawca modeli Ollama używa `baseUrl` jako klucza kanonicznego. Dostawca wyszukiwania w sieci honoruje też `baseURL` w `models.providers.ollama` w celu zgodności z przykładami konfiguracji w stylu OpenAI SDK.

Jeśli nie ustawiono jawnego bazowego adresu URL Ollama, OpenClaw używa `http://127.0.0.1:11434`.

Jeśli host Ollama oczekuje uwierzytelniania bearer, OpenClaw ponownie używa `models.providers.ollama.apiKey` (lub zgodnego uwierzytelniania dostawcy opartego na zmiennych środowiskowych) dla żądań do tego skonfigurowanego hosta.

Bezpośrednie hostowane Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Uwagi

  * Dla tego dostawcy nie jest wymagane pole klucza API specyficzne dla wyszukiwania w sieci.
  * Jeśli host Ollama jest chroniony uwierzytelnianiem, OpenClaw ponownie używa zwykłego klucza API dostawcy Ollama, gdy jest obecny.
  * Jeśli `baseUrl` to `https://ollama.com`, OpenClaw wywołuje bezpośrednio `https://ollama.com/api/web_search` i wysyła skonfigurowany klucz API Ollama jako uwierzytelnianie bearer.
  * Jeśli skonfigurowany host nie udostępnia wyszukiwania w sieci, a `OLLAMA_API_KEY` jest ustawiony, OpenClaw może awaryjnie użyć `https://ollama.com/api/web_search` bez wysyłania tego klucza środowiskowego do lokalnego hosta.
  * OpenClaw ostrzega podczas konfiguracji, jeśli Ollama jest nieosiągalna lub użytkownik nie jest zalogowany, ale nie blokuje wyboru.
  * Automatyczne wykrywanie w czasie działania może awaryjnie wybrać Ollama Web Search, gdy nie skonfigurowano dostawcy z poświadczeniami o wyższym priorytecie.
  * Lokalne hosty demona Ollama używają lokalnego punktu końcowego proxy `/api/experimental/web_search`, który podpisuje żądania i przekazuje je do Ollama Cloud.
  * Hosty `https://ollama.com` używają bezpośrednio publicznego hostowanego punktu końcowego `/api/web_search` z uwierzytelnianiem bearer za pomocą klucza API.


## Powiązane

  * [Omówienie Web Search](</pl/tools/web>) \-- wszyscy dostawcy i automatyczne wykrywanie
  * [Ollama](</pl/providers/ollama>) \-- konfiguracja modeli Ollama oraz tryby chmurowy/lokalny


Was this useful?YesNo
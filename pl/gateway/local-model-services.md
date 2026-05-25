---
title: Lokalne usługi modeli
source_url: https://docs.openclaw.ai/pl/gateway/local-model-services
scraped_at: 2026-05-25
---

`models.providers.<id>.localService` pozwala OpenClaw uruchamiać na żądanie lokalny serwer modelu należący do dostawcy. Jest to konfiguracja na poziomie dostawcy: gdy wybrany model należy do tego dostawcy, OpenClaw sprawdza usługę, uruchamia proces, jeśli punkt końcowy jest niedostępny, czeka na gotowość, a następnie wysyła żądanie do modelu.

Używaj tego dla lokalnych serwerów, których utrzymywanie przez cały dzień jest kosztowne, albo dla ręcznych konfiguracji, w których sam wybór modelu powinien wystarczyć do uruchomienia backendu.

## Jak to działa

  1. Żądanie modelu jest rozwiązywane do skonfigurowanego dostawcy.
  2. Jeśli ten dostawca ma `localService`, OpenClaw sprawdza `healthUrl`.
  3. Jeśli sprawdzenie się powiedzie, OpenClaw używa istniejącego serwera.
  4. Jeśli sprawdzenie się nie powiedzie, OpenClaw uruchamia `command` z `args`.
  5. OpenClaw odpytuje gotowość do momentu wygaśnięcia `readyTimeoutMs`.
  6. Żądanie modelu jest wysyłane przez standardowy transport dostawcy.
  7. Jeśli OpenClaw uruchomił proces, a `idleStopMs` jest dodatnie, proces jest zatrzymywany po tym, jak ostatnie trwające żądanie pozostanie bezczynne przez tak długi czas.


OpenClaw nie instaluje w tym celu launchd, systemd, Docker ani demona. Serwer jest procesem potomnym procesu OpenClaw, który jako pierwszy go potrzebował.

## Struktura konfiguracji

json5Copy code
[code]
    {  models: {    providers: {      local: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "local-model",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/absolute/path/to/server",          args: ["--host", "127.0.0.1", "--port", "8000"],          cwd: "/absolute/path/to/working-dir",          env: { LOCAL_MODEL_CACHE: "/absolute/path/to/cache" },          healthUrl: "http://127.0.0.1:8000/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "my-local-model",            name: "My Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Pola

  * `command`: bezwzględna ścieżka do pliku wykonywalnego. Wyszukiwanie przez powłokę nie jest używane.
  * `args`: argumenty procesu. Nie są stosowane rozwijanie powłoki, potoki, globowanie ani reguły cytowania.
  * `cwd`: opcjonalny katalog roboczy procesu.
  * `env`: opcjonalne zmienne środowiskowe scalane ze środowiskiem procesu OpenClaw.
  * `healthUrl`: URL gotowości. Jeśli zostanie pominięty, OpenClaw dopisuje `/models` do `baseUrl`, więc `http://127.0.0.1:8000/v1` staje się `http://127.0.0.1:8000/v1/models`.
  * `readyTimeoutMs`: limit czasu oczekiwania na gotowość podczas uruchamiania. Domyślnie: `120000`.
  * `idleStopMs`: opóźnienie wyłączenia po bezczynności dla procesów uruchomionych przez OpenClaw. `0` albo pominięcie utrzymuje proces przy życiu do czasu zakończenia OpenClaw.


## Przykład Inferrs

Inferrs jest niestandardowym backendem `/v1` zgodnym z OpenAI, więc to samo API usługi lokalnej działa z wpisem dostawcy `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

Zastąp `command` wynikiem `which inferrs` na maszynie uruchamiającej OpenClaw.

## Przykład ds4

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/Users/you/Projects/oss/ds4/ds4-server",          args: [            "--model",            "/Users/you/Projects/oss/ds4/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "393216",          ],          cwd: "/Users/you/Projects/oss/ds4",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [],      },    },  },}
[/code]

## Uwagi operacyjne

  * Jeden proces OpenClaw zarządza uruchomionym przez siebie procesem potomnym. Inny proces OpenClaw, który zobaczy, że ten sam URL sprawdzania kondycji już działa, użyje go ponownie bez przejmowania nad nim kontroli.
  * Uruchamianie jest serializowane dla każdego zestawu polecenia i argumentów dostawcy, więc równoczesne żądania nie tworzą zduplikowanych serwerów dla tej samej konfiguracji.
  * Aktywne odpowiedzi strumieniowe utrzymują dzierżawę; wyłączenie po bezczynności czeka do zakończenia obsługi treści odpowiedzi.
  * Użyj `timeoutSeconds` dla wolnych dostawców lokalnych, aby zimne starty i długie generowania nie trafiały w domyślny limit czasu żądania modelu.
  * Użyj jawnego `healthUrl`, jeśli Twój serwer udostępnia gotowość w miejscu innym niż `/v1/models`.


## Powiązane

[**Modele lokalne** Konfiguracja modelu lokalnego, wybór dostawcy i wskazówki dotyczące bezpieczeństwa. ](</pl/gateway/local-models>) [**Inferrs** Uruchamiaj OpenClaw przez lokalny serwer inferrs zgodny z OpenAI. ](</pl/providers/inferrs>)

Was this useful?YesNo
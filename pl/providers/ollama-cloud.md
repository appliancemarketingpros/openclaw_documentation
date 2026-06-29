---
title: Ollama Cloud
source_url: https://docs.openclaw.ai/pl/providers/ollama-cloud
scraped_at: 2026-06-29
---

ModelsProviders

Ollama Cloud to hostowane API modeli Ollama. Pozwala OpenClaw wywoływać modele hostowane przez Ollama bezpośrednio, bez instalowania lokalnego serwera Ollama ani logowania lokalnej aplikacji Ollama w trybie chmurowym. Użyj identyfikatora dostawcy `ollama-cloud` i referencji modeli takich jak `ollama-cloud/kimi-k2.6`.

Ta strona dotyczy bezpośredniego routingu wyłącznie przez chmurę. Dostawca używa natywnego stylu Ollama `/api/chat`, a nie trasy zgodnej z OpenAI `/v1`. OpenClaw rejestruje go jako osobny identyfikator dostawcy, aby poświadczenia tylko dla chmury, wykrywanie katalogu na żywo i wybór modelu nie mieszały się z lokalnym hostem `ollama`.

Użyj tej strony, gdy chcesz routingu wyłącznie przez chmurę. Informacje o lokalnym Ollama, hybrydowym routingu chmura plus lokalnie, embeddingach i szczegółach hosta niestandardowego znajdziesz w [Ollama](</pl/providers/ollama>).

## Konfiguracja

Utwórz klucz API Ollama Cloud na [ollama.com/settings/keys](<https://ollama.com/settings/keys>), a następnie uruchom:

bashCopy code
[code]
    openclaw onboard --auth-choice ollama-cloud
[/code]

Albo ustaw:

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret
[/code]

## Wartości domyślne

  * Dostawca: `ollama-cloud`
  * Bazowy URL: `https://ollama.com`
  * Zmienna środowiskowa: `OLLAMA_API_KEY`
  * Styl API: natywne Ollama `/api/chat`
  * Przykładowy model: `ollama-cloud/kimi-k2.6`


## Kiedy wybrać Ollama Cloud

  * Chcesz używać hostowanych modeli Ollama bez lokalnego uruchamiania `ollama serve`.
  * Chcesz tego samego natywnego kształtu API czatu Ollama, którego OpenClaw używa dla lokalnego Ollama, ale skierowanego na `https://ollama.com`.
  * Chcesz prostej ścieżki chmurowej dla modeli, które są już w hostowanym katalogu Ollama.
  * Nie potrzebujesz lokalnego pobierania modeli, lokalnej kontroli GPU ani wnioskowania tylko w sieci LAN.


Zamiast tego użyj [Ollama](</pl/providers/ollama>), gdy chcesz routingu tylko lokalnego lub chmura plus lokalnie przez zalogowanego hosta Ollama. Użyj dostawcy zgodnego z OpenAI, gdy potrzebujesz semantyki `/v1/chat/completions` albo funkcji w stylu OpenAI specyficznych dla dostawcy.

## Modele

OpenClaw wykrywa modele Ollama Cloud z hostowanego katalogu na żywo. Często dostępne hostowane identyfikatory obejmują:

  * `ollama-cloud/gpt-oss:20b`
  * `ollama-cloud/kimi-k2.6`
  * `ollama-cloud/deepseek-v4-flash`
  * `ollama-cloud/minimax-m2.7`
  * `ollama-cloud/glm-5`


Użyj identyfikatora modelu z bieżącego hostowanego katalogu:

bashCopy code
[code]
    openclaw models list --provider ollama-cloudopenclaw models set ollama-cloud/kimi-k2.6
[/code]

Identyfikatory modeli są identyfikatorami katalogu chmurowego, a nie nazwami lokalnego pobierania. Jeśli nazwa modelu działa na lokalnym hoście Ollama, ale nie ma jej w hostowanym katalogu, zamiast tego użyj dostawcy `ollama` z tym lokalnym hostem.

## Test na żywo

W przypadku testów dymnych klucza API Ollama Cloud skieruj test na żywo Ollama na hostowany endpoint i wybierz model z bieżącego katalogu:

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_OLLAMA=1 \OPENCLAW_LIVE_OLLAMA_BASE_URL=https://ollama.com \OPENCLAW_LIVE_OLLAMA_MODEL=kimi-k2.6 \OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=1 \pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

Test dymny w chmurze uruchamia tekst, natywny strumień i wyszukiwanie w sieci. Domyślnie pomija embeddingi dla `https://ollama.com`, ponieważ klucze API Ollama Cloud mogą nie autoryzować `/api/embed`.

## Rozwiązywanie problemów

  * Błędy `Set OLLAMA_API_KEY`: podaj prawdziwy klucz API chmury. Lokalny znacznik `ollama-local` służy tylko do lokalnych lub prywatnych hostów Ollama.
  * Błędy nieznanego modelu: uruchom `openclaw models list --provider ollama-cloud` i dokładnie skopiuj identyfikator hostowanego modelu.
  * Problemy z wywołaniami narzędzi lub surowym JSON na niestandardowych hostach Ollama: sprawdź, czy przypadkiem nie używasz zgodnego z OpenAI URL `/v1`. Trasy Ollama powinny używać natywnego bazowego URL bez sufiksu `/v1`.


## Powiązane

  * [Ollama](</pl/providers/ollama>)
  * [Dostawcy modeli](</pl/concepts/model-providers>)
  * [Wszyscy dostawcy](</pl/providers>)


Was this useful?YesNo

Open issue
---
title: CLI modeli
source_url: https://docs.openclaw.ai/pl/concepts/models
scraped_at: 2026-05-25
---

[**Przełączanie awaryjne modeli** Rotacja profili uwierzytelniania, okresy wyciszenia i ich interakcja z modelami zapasowymi. ](</pl/concepts/model-failover>) [**Dostawcy modeli** Szybki przegląd dostawców i przykłady. ](</pl/concepts/model-providers>) [**Środowiska uruchomieniowe agentów** PI, Codex i inne środowiska uruchomieniowe pętli agenta. ](</pl/concepts/agent-runtimes>) [**Dokumentacja konfiguracji** Klucze konfiguracji modeli. ](</pl/gateway/config-agents#agent-defaults>)

Referencje modeli wybierają dostawcę i model. Zwykle nie wybierają niskopoziomowego środowiska uruchomieniowego agenta. Referencje agentów OpenAI są głównym wyjątkiem: `openai/gpt-5.5` domyślnie działa przez środowisko uruchomieniowe serwera aplikacji Codex u oficjalnego dostawcy OpenAI. Jawne nadpisania środowiska uruchomieniowego należą do zasad dostawcy/modelu, a nie do całego agenta ani sesji. W trybie środowiska uruchomieniowego Codex referencja `openai/gpt-*` nie oznacza rozliczania za pomocą klucza API; uwierzytelnianie może pochodzić z konta Codex albo profilu uwierzytelniania `openai-codex`. Zobacz [Środowiska uruchomieniowe agentów](</pl/concepts/agent-runtimes>).

## Jak działa wybór modelu

OpenClaw wybiera modele w tej kolejności:

* ### Model podstawowy

`agents.defaults.model.primary` (lub `agents.defaults.model`).

* ### Modele zapasowe

`agents.defaults.model.fallbacks` (w kolejności).

* ### Przełączanie awaryjne uwierzytelniania dostawcy

Przełączanie awaryjne uwierzytelniania odbywa się wewnątrz dostawcy przed przejściem do następnego modelu.

Powiązane powierzchnie modeli

  * `agents.defaults.models` to lista dozwolonych/katalog modeli, których OpenClaw może używać (plus aliasy). Użyj wpisów `provider/*`, aby ograniczyć widocznych dostawców, zachowując dynamiczne wykrywanie dostawców.
  * `agents.defaults.imageModel` jest używany **tylko wtedy** , gdy model podstawowy nie może przyjmować obrazów.
  * `agents.defaults.pdfModel` jest używany przez narzędzie `pdf`. Jeśli zostanie pominięty, narzędzie przechodzi awaryjnie do `agents.defaults.imageModel`, a następnie do rozwiązanego modelu sesji/domyślnego.
  * `agents.defaults.imageGenerationModel` jest używany przez współdzieloną funkcję generowania obrazów. Jeśli zostanie pominięty, `image_generate` nadal może wywnioskować domyślnego dostawcę z działającym uwierzytelnianiem. Najpierw próbuje bieżącego domyślnego dostawcy, a potem pozostałych zarejestrowanych dostawców generowania obrazów w kolejności identyfikatorów dostawców. Jeśli ustawisz konkretnego dostawcę/model, skonfiguruj też uwierzytelnianie/klucz API tego dostawcy.
  * `agents.defaults.musicGenerationModel` jest używany przez współdzieloną funkcję generowania muzyki. Jeśli zostanie pominięty, `music_generate` nadal może wywnioskować domyślnego dostawcę z działającym uwierzytelnianiem. Najpierw próbuje bieżącego domyślnego dostawcy, a potem pozostałych zarejestrowanych dostawców generowania muzyki w kolejności identyfikatorów dostawców. Jeśli ustawisz konkretnego dostawcę/model, skonfiguruj też uwierzytelnianie/klucz API tego dostawcy.
  * `agents.defaults.videoGenerationModel` jest używany przez współdzieloną funkcję generowania wideo. Jeśli zostanie pominięty, `video_generate` nadal może wywnioskować domyślnego dostawcę z działającym uwierzytelnianiem. Najpierw próbuje bieżącego domyślnego dostawcy, a potem pozostałych zarejestrowanych dostawców generowania wideo w kolejności identyfikatorów dostawców. Jeśli ustawisz konkretnego dostawcę/model, skonfiguruj też uwierzytelnianie/klucz API tego dostawcy.
  * Domyślne ustawienia poszczególnych agentów mogą nadpisywać `agents.defaults.model` przez `agents.list[].model` oraz powiązania (zobacz [Routing wieloagentowy](</pl/concepts/multi-agent>)).


## Źródło wyboru i zachowanie modeli zapasowych

Ta sama wartość `provider/model` może oznaczać różne rzeczy w zależności od tego, skąd pochodzi:

  * Skonfigurowane wartości domyślne (`agents.defaults.model.primary` i podstawowe modele specyficzne dla agentów) są normalnym punktem startowym i używają `agents.defaults.model.fallbacks`.
  * Automatyczne wybory modelu zapasowego są tymczasowym stanem odzyskiwania. Są przechowywane z `modelOverrideSource: "auto"`, aby kolejne tury mogły nadal używać łańcucha modeli zapasowych bez wcześniejszego sprawdzania znanego niedziałającego modelu podstawowego.
  * Wybory użytkownika w sesji są dokładne. `/model`, selektor modelu, `session_status(model=...)` i `sessions.patch` przechowują `modelOverrideSource: "user"`; jeśli wybrany dostawca/model jest niedostępny, OpenClaw zgłasza widoczny błąd zamiast przechodzić do innego skonfigurowanego modelu.
  * Cron `--model` / ładunek `model` jest modelem podstawowym dla danego zadania. Nadal używa skonfigurowanych modeli zapasowych, chyba że zadanie podaje jawny ładunek `fallbacks` (użyj `fallbacks: []` dla ścisłego uruchomienia cron).
  * Selektory domyślnego modelu CLI i listy dozwolonych respektują `models.mode: "replace"`, wyświetlając jawne `models.providers.*.models` zamiast ładować pełny wbudowany katalog.
  * Selektor modelu w Control UI pyta Gateway o skonfigurowany widok modeli: `agents.defaults.models`, gdy jest obecne, w tym wpisy obejmujące całego dostawcę `provider/*`; w przeciwnym razie jawne `models.providers.*.models` plus dostawcy z użytecznym uwierzytelnianiem. Pełny wbudowany katalog jest zarezerwowany dla jawnych widoków przeglądania, takich jak `models.list` z `view: "all"` albo `openclaw models list --all`.


## Szybkie zasady modeli

  * Ustaw model podstawowy na najsilniejszy dostępny dla Ciebie model najnowszej generacji.
  * Używaj modeli zapasowych do zadań wrażliwych na koszt/opóźnienie oraz czatu o niższej wadze.
  * W przypadku agentów z włączonymi narzędziami lub niezaufanych danych wejściowych unikaj starszych/słabszych poziomów modeli.


## Onboarding (zalecane)

Jeśli nie chcesz ręcznie edytować konfiguracji, uruchom onboarding:

bashCopy code
[code]
    openclaw onboard
[/code]

Może skonfigurować model i uwierzytelnianie dla popularnych dostawców, w tym **subskrypcję OpenAI Code (Codex)** (OAuth) oraz **Anthropic** (klucz API lub Claude CLI).

## Klucze konfiguracji (przegląd)

  * `agents.defaults.model.primary` i `agents.defaults.model.fallbacks`
  * `agents.defaults.imageModel.primary` i `agents.defaults.imageModel.fallbacks`
  * `agents.defaults.pdfModel.primary` i `agents.defaults.pdfModel.fallbacks`
  * `agents.defaults.imageGenerationModel.primary` i `agents.defaults.imageGenerationModel.fallbacks`
  * `agents.defaults.videoGenerationModel.primary` i `agents.defaults.videoGenerationModel.fallbacks`
  * `agents.defaults.models` (lista dozwolonych + aliasy + parametry dostawcy + dynamiczne wpisy dostawców `provider/*`)
  * `models.providers` (niestandardowi dostawcy zapisani w `models.json`)


### Bezpieczne edycje listy dozwolonych

Używaj zapisów addytywnych podczas ręcznej aktualizacji `agents.defaults.models`:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --merge
[/code]

Reguły ochrony przed nadpisaniem

`openclaw config set` chroni mapy modeli/dostawców przed przypadkowym nadpisaniem. Zwykłe przypisanie obiektu do `agents.defaults.models`, `models.providers` lub `models.providers.<id>.models` jest odrzucane, gdy usunęłoby istniejące wpisy. Użyj `--merge` dla zmian addytywnych; użyj `--replace` tylko wtedy, gdy podana wartość ma stać się kompletną wartością docelową.

Interaktywna konfiguracja dostawcy oraz `openclaw configure --section model` także scalają wybory o zakresie dostawcy z istniejącą listą dozwolonych, więc dodanie Codex, Ollama lub innego dostawcy nie usuwa niepowiązanych wpisów modeli. Konfiguracja zachowuje istniejące `agents.defaults.model.primary`, gdy uwierzytelnianie dostawcy jest stosowane ponownie. Jawne polecenia ustawiające wartość domyślną, takie jak `openclaw models auth login --provider <id> --set-default` i `openclaw models set <model>`, nadal zastępują `agents.defaults.model.primary`.

## „Model is not allowed” (i dlaczego odpowiedzi się zatrzymują)

Jeśli `agents.defaults.models` jest ustawione, staje się **listą dozwolonych** dla `/model` i nadpisań sesji. Gdy użytkownik wybierze model, którego nie ma na tej liście dozwolonych, OpenClaw zwraca:

CodeCopy code
[code]
    Model "provider/model" is not allowed. Use /models to list providers, or /models <provider> to list models.Add it with: openclaw config set agents.defaults.models '{"provider/model":{}}' --strict-json --merge
[/code]

Gdy odrzucone polecenie zawierało nadpisanie środowiska uruchomieniowego, takie jak `/model openai/gpt-5.5 --runtime codex`, najpierw napraw listę dozwolonych, a potem ponów to samo polecenie `/model ... --runtime ...`. Dla natywnego wykonania Codex wybrany model nadal jest `openai/gpt-5.5`; środowisko uruchomieniowe `codex` wybiera uprząż i osobno używa uwierzytelniania Codex.

Dla modeli lokalnych/GGUF przechowuj na liście dozwolonych pełną referencję z prefiksem dostawcy, na przykład `ollama/gemma4:26b`, `lmstudio/Gemma4-26b-a4-it-gguf` albo dokładną wartość provider/model pokazaną przez `openclaw models list --provider <provider>`. Same lokalne nazwy plików lub nazwy wyświetlane nie wystarczą, gdy lista dozwolonych jest aktywna.

Jeśli chcesz ograniczyć dostawców bez ręcznego wypisywania każdego modelu, dodaj wpisy `provider/*` do `agents.defaults.models`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai-codex/*": {},        "vllm/*": {},      },    },  },}
[/code]

Przy takiej zasadzie `/model`, `/models` i selektory modeli pokazują wykryty katalog tylko dla tych dostawców. Nowe modele od wybranych dostawców mogą pojawić się bez edytowania listy dozwolonych. Dokładne wpisy `provider/model` można mieszać z wpisami `provider/*`, gdy potrzebujesz jednego konkretnego modelu od innego dostawcy.

Przykładowa konfiguracja listy dozwolonych:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-sonnet-4-6" },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "anthropic/claude-opus-4-6": { alias: "Opus" },      },    },  },}
[/code]

## Przełączanie modeli w czacie (`/model`)

Możesz przełączać modele dla bieżącej sesji bez restartowania:

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model status
[/code]

Zachowanie selektora

  * `/model` (i `/model list`) to kompaktowy, numerowany selektor (rodzina modelu + dostępni dostawcy).
  * W Discord `/model` i `/models` otwierają interaktywny selektor z listami rozwijanymi dostawcy i modelu oraz krokiem Submit.
  * W Telegram wybory selektora `/models` mają zakres sesji; nie zmieniają trwałej wartości domyślnej agenta w `openclaw.json`.
  * `/models add` jest przestarzałe i teraz zwraca komunikat o wycofaniu zamiast rejestrować modele z czatu.
  * `/model <#>` wybiera pozycję z tego selektora.

Trwałość i przełączanie na żywo

  * `/model` natychmiast zapisuje nowy wybór sesji.
  * Jeśli agent jest bezczynny, następne uruchomienie od razu użyje nowego modelu.
  * Jeśli uruchomienie jest już aktywne, OpenClaw oznacza przełączenie na żywo jako oczekujące i restartuje do nowego modelu dopiero w czystym punkcie ponownej próby.
  * Jeśli aktywność narzędzi lub wyjście odpowiedzi już się rozpoczęły, oczekujące przełączenie może pozostać w kolejce do późniejszej okazji ponownej próby albo do następnej tury użytkownika.
  * Referencja `/model` wybrana przez użytkownika jest ścisła dla tej sesji: jeśli wybrany dostawca/model jest niedostępny, odpowiedź kończy się widocznym błędem zamiast po cichu odpowiadać z `agents.defaults.model.fallbacks`. Różni się to od skonfigurowanych wartości domyślnych i podstawowych modeli zadań cron, które nadal mogą używać łańcuchów modeli zapasowych.
  * `/model status` to szczegółowy widok (kandydaci uwierzytelniania oraz, gdy skonfigurowano, punkt końcowy dostawcy `baseUrl` \+ tryb `api`).

Parsowanie referencji

  * Referencje modeli są parsowane przez podział na **pierwszym** `/`. Użyj `provider/model` podczas wpisywania `/model <ref>`.
  * Jeśli sam identyfikator modelu zawiera `/` (w stylu OpenRouter), musisz podać prefiks dostawcy (przykład: `/model openrouter/moonshotai/kimi-k2`).
  * Jeśli pominiesz dostawcę, OpenClaw rozwiązuje dane wejściowe w tej kolejności: 
    1. dopasowanie aliasu
    2. unikalne dopasowanie skonfigurowanego dostawcy dla dokładnie tego identyfikatora modelu bez prefiksu
    3. przestarzałe przejście awaryjne do skonfigurowanego domyślnego dostawcy — jeśli ten dostawca nie udostępnia już skonfigurowanego domyślnego modelu, OpenClaw zamiast tego przechodzi awaryjnie do pierwszego skonfigurowanego dostawcy/modelu, aby uniknąć ujawniania nieaktualnego ustawienia domyślnego usuniętego dostawcy.


Pełne zachowanie poleceń/konfiguracja: [Polecenia ukośnikowe](</pl/tools/slash-commands>).

## Polecenia CLI

bashCopy code
[code]
    openclaw models listopenclaw models statusopenclaw models set <provider/model>openclaw models set-image <provider/model> openclaw models aliases listopenclaw models aliases add <alias> <provider/model>openclaw models aliases remove <alias> openclaw models fallbacks listopenclaw models fallbacks add <provider/model>openclaw models fallbacks remove <provider/model>openclaw models fallbacks clear openclaw models image-fallbacks listopenclaw models image-fallbacks add <provider/model>openclaw models image-fallbacks remove <provider/model>openclaw models image-fallbacks clear
[/code]

`openclaw models` (bez podpolecenia) jest skrótem dla `models status`.

### `models list`

Domyślnie pokazuje skonfigurowane modele/dostępne po uwierzytelnieniu. Przydatne flagi:

Pełny katalog. Obejmuje statyczne wiersze katalogu dołączonych dostawców należące do dostawcy przed skonfigurowaniem uwierzytelniania, więc widoki służące tylko do wykrywania mogą pokazywać modele niedostępne do czasu dodania odpowiednich poświadczeń dostawcy.

Tylko dostawcy lokalni.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcHJvdmlkZXIgPGlk " type="string"> Filtruj według identyfikatora dostawcy, na przykład `moonshot`. Etykiety wyświetlane z interaktywnych selektorów nie są akceptowane.

Jeden model w wierszu.

Dane wyjściowe czytelne maszynowo.

### `models status`

Pokazuje rozwiązany model podstawowy, modele awaryjne, model obrazu oraz przegląd uwierzytelniania skonfigurowanych dostawców. Pokazuje też stan wygaśnięcia OAuth dla profili znalezionych w magazynie uwierzytelniania (domyślnie ostrzega w ciągu 24 godzin). `--plain` wypisuje tylko rozwiązany model podstawowy.

Uwierzytelnianie i zachowanie sondowania

  * Stan OAuth jest zawsze pokazywany (i uwzględniany w danych wyjściowych `--json`). Jeśli skonfigurowany dostawca nie ma poświadczeń, `models status` wypisuje sekcję **Brak uwierzytelniania**.
  * JSON zawiera `auth.oauth` (okno ostrzegania + profile) i `auth.providers` (efektywne uwierzytelnianie dla każdego dostawcy, w tym poświadczenia oparte na env). `auth.oauth` dotyczy tylko kondycji profili w magazynie uwierzytelniania; dostawcy tylko env nie pojawiają się tam.
  * Użyj `--check` do automatyzacji (kod wyjścia `1` przy braku/wygaśnięciu, `2` przy zbliżającym się wygaśnięciu).
  * Użyj `--probe` do sprawdzania uwierzytelniania na żywo; wiersze sondowania mogą pochodzić z profili uwierzytelniania, poświadczeń env lub `models.json`.
  * Jeśli jawne `auth.order.<provider>` pomija zapisany profil, sondowanie zgłasza `excluded_by_auth_order` zamiast próbować go użyć. Jeśli uwierzytelnianie istnieje, ale dla tego dostawcy nie da się rozwiązać modelu możliwego do sondowania, sondowanie zgłasza `status: no_model`.


Przykład (Claude CLI):

bashCopy code
[code]
    claude auth loginopenclaw models status
[/code]

## Skanowanie (darmowe modele OpenRouter)

`openclaw models scan` sprawdza **katalog darmowych modeli** OpenRouter i może opcjonalnie sondować modele pod kątem obsługi narzędzi i obrazów.

Pomiń sondowanie na żywo (tylko metadane).

Ustaw `agents.defaults.model.primary` na pierwszy wybór.

Ustaw `agents.defaults.imageModel.primary` na pierwszy wybór obrazu.

Wyniki skanowania są klasyfikowane według:

  1. Obsługa obrazów
  2. Opóźnienie narzędzi
  3. Rozmiar kontekstu
  4. Liczba parametrów


Dane wejściowe:

  * Lista OpenRouter `/models` (filtr `:free`)
  * Sondowanie na żywo wymaga klucza API OpenRouter z profili uwierzytelniania lub `OPENROUTER_API_KEY` (zobacz [Zmienne środowiskowe](</pl/help/environment>))
  * Filtry opcjonalne: `--max-age-days`, `--min-params`, `--provider`, `--max-candidates`
  * Sterowanie żądaniem/sondowaniem: `--timeout`, `--concurrency`


Gdy sondowanie na żywo działa w TTY, możesz interaktywnie wybierać modele awaryjne. W trybie nieinteraktywnym przekaż `--yes`, aby zaakceptować wartości domyślne. Wyniki tylko z metadanymi mają charakter informacyjny; `--set-default` i `--set-image` wymagają sondowania na żywo, aby OpenClaw nie skonfigurował bezużytecznego modelu OpenRouter bez klucza.

## Rejestr modeli (`models.json`)

Niestandardowi dostawcy w `models.providers` są zapisywani do `models.json` w katalogu agenta (domyślnie `~/.openclaw/agents/<agentId>/agent/models.json`). Ten plik jest domyślnie scalany, chyba że `models.mode` ustawiono na `replace`.

Priorytet trybu scalania

Priorytet trybu scalania dla pasujących identyfikatorów dostawców:

  * Niepuste `baseUrl` obecne już w `models.json` agenta wygrywa.
  * Niepuste `apiKey` w `models.json` agenta wygrywa tylko wtedy, gdy ten dostawca nie jest zarządzany przez SecretRef w bieżącym kontekście konfiguracji/profilu uwierzytelniania.
  * Wartości `apiKey` dostawcy zarządzanego przez SecretRef są odświeżane ze znaczników źródła (`ENV_VAR_NAME` dla referencji env, `secretref-managed` dla referencji file/exec) zamiast utrwalać rozwiązane sekrety.
  * Wartości nagłówków dostawcy zarządzanego przez SecretRef są odświeżane ze znaczników źródła (`secretref-env:ENV_VAR_NAME` dla referencji env, `secretref-managed` dla referencji file/exec).
  * Puste lub brakujące `apiKey`/`baseUrl` agenta przechodzą awaryjnie do konfiguracji `models.providers`.
  * Inne pola dostawcy są odświeżane z konfiguracji i znormalizowanych danych katalogu.


## Powiązane

  * [Środowiska uruchomieniowe agentów](</pl/concepts/agent-runtimes>) — PI, Codex i inne środowiska uruchomieniowe pętli agentów
  * [Informacje o konfiguracji](</pl/gateway/config-agents#agent-defaults>) — klucze konfiguracji modelu
  * [Generowanie obrazów](</pl/tools/image-generation>) — konfiguracja modelu obrazu
  * [Przełączanie awaryjne modeli](</pl/concepts/model-failover>) — łańcuchy awaryjne
  * [Dostawcy modeli](</pl/concepts/model-providers>) — trasowanie dostawców i uwierzytelnianie
  * [Generowanie muzyki](</pl/tools/music-generation>) — konfiguracja modelu muzyki
  * [Generowanie wideo](</pl/tools/video-generation>) — konfiguracja modelu wideo


Was this useful?YesNo
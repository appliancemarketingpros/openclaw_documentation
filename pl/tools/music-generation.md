---
title: Generowanie muzyki
source_url: https://docs.openclaw.ai/pl/tools/music-generation
scraped_at: 2026-05-25
---

Narzędzie `music_generate` pozwala agentowi tworzyć muzykę lub audio przez wspólną funkcję generowania muzyki ze skonfigurowanymi dostawcami — obecnie Google, MiniMax i ComfyUI skonfigurowanym przez workflow.

W przypadku uruchomień agenta opartych na sesji OpenClaw uruchamia generowanie muzyki jako zadanie w tle, śledzi je w rejestrze zadań, a następnie ponownie wybudza agenta, gdy utwór jest gotowy, aby agent mógł poinformować użytkownika i dołączyć gotowe audio. W czatach grupowych/kanałowych, które używają widocznego dostarczania wyłącznie przez narzędzie wiadomości, agent przekazuje wynik przez narzędzie wiadomości. Jeśli agent ukończenia zapisze tylko prywatną odpowiedź końcową, OpenClaw awaryjnie używa bezpośredniej wysyłki do kanału z wygenerowanymi mediami. Wybudzenie po ukończeniu jawnie ostrzega agenta, że zwykłe odpowiedzi końcowe są prywatne w tych trasach.

## Szybki start

### Oparty na współdzielonym dostawcy

* ### Skonfiguruj uwierzytelnianie

Ustaw klucz API dla co najmniej jednego dostawcy — na przykład `GEMINI_API_KEY` lub `MINIMAX_API_KEY`.

* ### Wybierz model domyślny (opcjonalnie)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Poproś agenta

_"Wygeneruj energiczny utwór synthpop o nocnej jeździe przez neonowe miasto."_

Agent automatycznie wywołuje `music_generate`. Nie jest wymagana lista dozwolonych narzędzi.

W bezpośrednich kontekstach synchronicznych bez uruchomienia agenta opartego na sesji wbudowane narzędzie nadal awaryjnie używa generowania inline i zwraca ścieżkę do gotowych mediów w wyniku narzędzia.

### Workflow ComfyUI

* ### Skonfiguruj workflow

Skonfiguruj `plugins.entries.comfy.config.music` z plikiem JSON workflow oraz węzłami promptu/wyjścia.

* ### Uwierzytelnianie w chmurze (opcjonalnie)

Dla Comfy Cloud ustaw `COMFY_API_KEY` lub `COMFY_CLOUD_API_KEY`.

* ### Wywołaj narzędzie

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Przykładowe prompty:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Obsługiwani dostawcy

Dostawca | Model domyślny | Dane referencyjne | Obsługiwane kontrolki | Uwierzytelnianie  
---|---|---|---|---  
ComfyUI | `workflow` | Do 1 obrazu | Muzyka lub audio zdefiniowane przez workflow | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Do 10 obrazów | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Brak | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` lub MiniMax OAuth  
  
### Macierz funkcji

Jawny kontrakt trybu używany przez `music_generate`, testy kontraktu i wspólne przemiatanie live:

Dostawca | `generate` | `edit` | Limit edycji | Wspólne ścieżki live  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 obraz | Nie jest częścią wspólnego przemiatania; pokryte przez `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 obrazów | `generate`, `edit`  
MiniMax | ✓ | — | Brak | `generate`  
  
Użyj `action: "list"`, aby sprawdzić dostępnych współdzielonych dostawców i modele w czasie działania:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Użyj `action: "status"`, aby sprawdzić aktywne zadanie muzyczne oparte na sesji:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Przykład bezpośredniego generowania:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Parametry narzędzia

Prompt generowania muzyki. Wymagany dla `action: "generate"`.

`"status"` zwraca bieżące zadanie sesji; `"list"` sprawdza dostawców.

Nadpisanie dostawcy/modelu (np. `google/lyria-3-pro-preview`, `comfy/workflow`).

Opcjonalny tekst utworu, gdy dostawca obsługuje jawne wejście tekstu utworu.

Zażądaj wyniku wyłącznie instrumentalnego, gdy dostawca to obsługuje.

Pojedyncza ścieżka lub URL obrazu referencyjnego.

Wiele obrazów referencyjnych (do 10 u obsługujących dostawców).

Docelowy czas trwania w sekundach, gdy dostawca obsługuje wskazówki dotyczące czasu trwania.

Wskazówka formatu wyjściowego, gdy dostawca ją obsługuje.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Opcjonalny limit czasu żądania dostawcy w milisekundach. Gdy zostanie pominięty, OpenClaw używa `agents.defaults.musicGenerationModel.timeoutMs`, jeśli jest skonfigurowane. Wartości poniżej 10000ms są podnoszone do 10000ms i raportowane w wyniku narzędzia. OPENCLAW_DOCS_MARKER:paramClose:

## Zachowanie asynchroniczne

Generowanie muzyki oparte na sesji działa jako zadanie w tle:

  * **Zadanie w tle:** `music_generate` tworzy zadanie w tle, od razu zwraca odpowiedź uruchomione/zadanie i później publikuje gotowy utwór w kolejnej wiadomości agenta.
  * **Zapobieganie duplikatom:** gdy zadanie ma stan `queued` lub `running`, późniejsze wywołania `music_generate` w tej samej sesji zwracają status zadania zamiast uruchamiać kolejne generowanie. Użyj `action: "status"`, aby sprawdzić to jawnie.
  * **Wyszukiwanie statusu:** `openclaw tasks list` lub `openclaw tasks show <taskId>` sprawdza statusy w kolejce, uruchomione i końcowe.
  * **Wybudzenie po ukończeniu:** OpenClaw wstrzykuje wewnętrzne zdarzenie ukończenia z powrotem do tej samej sesji, aby model mógł sam napisać dalszą wiadomość widoczną dla użytkownika.
  * **Wskazówka promptu:** późniejsze tury użytkownika/ręczne w tej samej sesji dostają małą wskazówkę runtime, gdy zadanie muzyczne jest już w toku, aby model nie wywoływał bezrefleksyjnie `music_generate` ponownie.
  * **Awaryjnie bez sesji:** bezpośrednie/lokalne konteksty bez rzeczywistej sesji agenta działają inline i zwracają końcowy wynik audio w tej samej turze.


### Cykl życia zadania

Stan | Znaczenie  
---|---  
`queued` | Zadanie utworzone, czeka na przyjęcie przez dostawcę.  
`running` | Dostawca przetwarza (zwykle od 30 sekund do 3 minut, zależnie od dostawcy i czasu trwania).  
`succeeded` | Utwór gotowy; agent wybudza się i publikuje go w rozmowie.  
`failed` | Błąd dostawcy lub limit czasu; agent wybudza się ze szczegółami błędu.  
  
Sprawdź status z CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Konfiguracja

### Wybór modelu

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Kolejność wyboru dostawców

OpenClaw próbuje dostawców w tej kolejności:

  1. Parametr `model` z wywołania narzędzia (jeśli agent go określi).
  2. `musicGenerationModel.primary` z konfiguracji.
  3. `musicGenerationModel.fallbacks` w kolejności.
  4. Automatyczne wykrywanie używające tylko domyślnych dostawców opartych na uwierzytelnianiu: 
     * najpierw bieżący dostawca domyślny;
     * pozostali zarejestrowani dostawcy generowania muzyki w kolejności identyfikatorów dostawców.


Jeśli dostawca zawiedzie, automatycznie próbowany jest następny kandydat. Jeśli wszystkie zawiodą, błąd zawiera szczegóły z każdej próby.

Ustaw `agents.defaults.mediaGenerationAutoProviderFallback: false`, aby używać tylko jawnych wpisów `model`, `primary` i `fallbacks`.

## Uwagi o dostawcach

ComfyUI

Oparte na workflow i zależne od skonfigurowanego grafu oraz mapowania węzłów dla pól promptu/wyjścia. Dołączony plugin `comfy` podłącza się do współdzielonego narzędzia `music_generate` przez rejestr dostawców generowania muzyki.

Google (Lyria 3)

Używa wsadowego generowania Lyria 3. Bieżący dołączony przepływ obsługuje prompt, opcjonalny tekst utworu i opcjonalne obrazy referencyjne.

MiniMax

Używa wsadowego punktu końcowego `music_generation`. Obsługuje prompt, opcjonalny tekst utworu, tryb instrumentalny, sterowanie czasem trwania i wyjście mp3 przez uwierzytelnianie kluczem API `minimax` albo OAuth `minimax-portal`.

## Wybór właściwej ścieżki

  * **Oparta na współdzielonym dostawcy** , gdy chcesz wyboru modelu, przełączania awaryjnego dostawców oraz wbudowanego asynchronicznego przepływu zadań/statusu.
  * **Ścieżka pluginu (ComfyUI)** , gdy potrzebujesz niestandardowego grafu workflow lub dostawcy, który nie jest częścią współdzielonej dołączonej funkcji muzyki.


Jeśli debugujesz zachowanie specyficzne dla ComfyUI, zobacz [ComfyUI](</pl/providers/comfy>). Jeśli debugujesz zachowanie współdzielonego dostawcy, zacznij od [Google (Gemini)](</pl/providers/google>) lub [MiniMax](</pl/providers/minimax>).

## Tryby funkcji dostawcy

Wspólny kontrakt generowania muzyki obsługuje jawne deklaracje trybów:

  * `generate` dla generowania wyłącznie z promptu.
  * `edit`, gdy żądanie zawiera jeden lub więcej obrazów referencyjnych.


Nowe implementacje dostawców powinny preferować jawne bloki trybu:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Starsze płaskie pola, takie jak `maxInputImages`, `supportsLyrics` i `supportsFormat`, **nie** wystarczają do reklamowania obsługi edycji. Dostawcy powinni deklarować `generate` i `edit` jawnie, aby testy live, testy kontraktu i współdzielone narzędzie `music_generate` mogły deterministycznie weryfikować obsługę trybu.

## Testy live

Opcjonalne pokrycie live dla współdzielonych dołączonych dostawców:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper repozytorium:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Ten plik testów na żywo ładuje brakujące zmienne środowiskowe dostawców z `~/.profile`, domyślnie preferuje klucze API z live/env przed zapisanymi profilami uwierzytelniania i uruchamia zarówno pokrycie `generate`, jak i zadeklarowane pokrycie `edit`, gdy dostawca włącza tryb edycji. Dzisiejszy zakres pokrycia:

  * `google`: `generate` oraz `edit`
  * `minimax`: tylko `generate`
  * `comfy`: oddzielne pokrycie Comfy na żywo, nie współdzielony przegląd dostawców


Opcjonalne pokrycie na żywo dla dołączonej ścieżki muzycznej ComfyUI:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Plik testów Comfy na żywo obejmuje również przepływy pracy obrazów i wideo comfy, gdy te sekcje są skonfigurowane.

## Powiązane

  * [Zadania w tle](</pl/automation/tasks>) — śledzenie zadań dla odłączonych uruchomień `music_generate`
  * [ComfyUI](</pl/providers/comfy>)
  * [Dokumentacja konfiguracji](</pl/gateway/config-agents#agent-defaults>) — konfiguracja `musicGenerationModel`
  * [Google (Gemini)](</pl/providers/google>)
  * [MiniMax](</pl/providers/minimax>)
  * [Modele](</pl/concepts/models>) — konfiguracja modeli i przełączanie awaryjne
  * [Przegląd narzędzi](</pl/tools>)


Was this useful?YesNo
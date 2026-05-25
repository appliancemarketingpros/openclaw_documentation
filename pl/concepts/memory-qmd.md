---
title: Silnik pamięci QMD
source_url: https://docs.openclaw.ai/pl/concepts/memory-qmd
scraped_at: 2026-05-25
---

[QMD](<https://github.com/tobi/qmd>) to lokalny proces pomocniczy wyszukiwania local-first, który działa obok OpenClaw. Łączy BM25, wyszukiwanie wektorowe i ponowne rankingowanie w jednym pliku binarnym oraz może indeksować treści poza plikami pamięci Twojego obszaru roboczego.

## Co dodaje względem wbudowanego rozwiązania

  * **Ponowne rankingowanie i rozszerzanie zapytań** dla lepszego przywoływania wyników.
  * **Indeksowanie dodatkowych katalogów** \-- dokumentacji projektu, notatek zespołu, wszystkiego na dysku.
  * **Indeksowanie transkrypcji sesji** \-- przywoływanie wcześniejszych rozmów.
  * **W pełni lokalne** \-- działa z opcjonalnym pakietem runtime `node-llama-cpp` i automatycznie pobiera modele GGUF.
  * **Automatyczne przełączenie awaryjne** \-- jeśli QMD jest niedostępne, OpenClaw płynnie wraca do wbudowanego silnika.


## Pierwsze kroki

### Wymagania wstępne

  * Zainstaluj QMD: `npm install -g @tobilu/qmd` albo `bun install -g @tobilu/qmd`
  * Kompilacja SQLite pozwalająca na rozszerzenia (`brew install sqlite` w macOS).
  * QMD musi znajdować się w `PATH` Gateway.
  * macOS i Linux działają od razu. Windows jest najlepiej obsługiwany przez WSL2.


### Włączanie

json5Copy code
[code]
    {  memory: {    backend: "qmd",  },}
[/code]

OpenClaw tworzy samowystarczalny katalog domowy QMD pod `~/.openclaw/agents/<agentId>/qmd/` i automatycznie zarządza cyklem życia procesu pomocniczego \-- kolekcje, aktualizacje i przebiegi osadzania są obsługiwane za Ciebie. Preferuje bieżącą kolekcję QMD i kształty zapytań MCP, ale w razie potrzeby nadal wraca do alternatywnych flag wzorców kolekcji i starszych nazw narzędzi MCP. Uzgadnianie podczas uruchamiania odtwarza też przestarzałe zarządzane kolekcje do ich kanonicznych wzorców, gdy starsza kolekcja QMD o tej samej nazwie jest nadal obecna.

## Jak działa proces pomocniczy

  * OpenClaw tworzy kolekcje z plików pamięci Twojego obszaru roboczego oraz wszystkich skonfigurowanych `memory.qmd.paths`, a następnie uruchamia `qmd update`, gdy menedżer QMD zostaje otwarty, i okresowo później (domyślnie co 5 minut). Te odświeżenia przebiegają przez podprocesy QMD, a nie przez wewnątrzprocesowe skanowanie systemu plików. Tryby semantyczne uruchamiają też `qmd embed`.
  * Domyślna kolekcja obszaru roboczego śledzi `MEMORY.md` oraz drzewo `memory/`. `memory.md` zapisany małymi literami nie jest indeksowany jako główny plik pamięci.
  * Własny skaner QMD ignoruje ukryte ścieżki i typowe katalogi zależności/kompilacji, takie jak `.git`, `.cache`, `node_modules`, `vendor`, `dist` i `build`. Uruchomienie Gateway domyślnie nie inicjuje QMD, więc zimny start unika importowania runtime pamięci lub tworzenia długotrwałego obserwatora przed pierwszym użyciem pamięci.
  * Jeśli mimo to chcesz odświeżania przy starcie Gateway, ustaw `memory.qmd.update.startup` na `idle` albo `immediate`. Opcjonalne odświeżanie przy starcie używa jednorazowej ścieżki podprocesu QMD zamiast tworzyć pełny długotrwały obserwator wewnątrz procesu.
  * Wyszukiwania używają skonfigurowanego `searchMode` (domyślnie: `search`; obsługuje też `vsearch` i `query`). `search` działa wyłącznie na BM25, więc OpenClaw pomija semantyczne sondy gotowości wektorów i utrzymanie osadzeń w tym trybie. Jeśli tryb zawiedzie, OpenClaw ponawia próbę z `qmd query`.
  * W wydaniach QMD, które deklarują filtry wielu kolekcji, OpenClaw grupuje kolekcje z tego samego źródła w jedno wywołanie wyszukiwania QMD. Starsze wydania QMD zachowują zgodne przełączenie awaryjne na pojedyncze kolekcje.
  * Jeśli QMD całkowicie zawiedzie, OpenClaw wraca do wbudowanego silnika SQLite. Powtarzające się próby w turach czatu wycofują się na krótko po błędzie otwarcia, aby brakujący plik binarny lub uszkodzona zależność procesu pomocniczego nie stworzyły burzy ponowień; `openclaw memory status` i jednorazowe sondy CLI nadal sprawdzają QMD bezpośrednio.


## Wydajność wyszukiwania i zgodność

OpenClaw utrzymuje ścieżkę wyszukiwania QMD zgodną zarówno z bieżącymi, jak i starszymi instalacjami QMD.

Podczas uruchamiania OpenClaw sprawdza tekst pomocy zainstalowanego QMD raz na menedżer. Jeśli plik binarny deklaruje obsługę wielu filtrów kolekcji, OpenClaw przeszukuje wszystkie kolekcje z tego samego źródła jednym poleceniem:

bashCopy code
[code]
    qmd search "router notes" --json -n 10 -c memory-root-main -c memory-dir-main
[/code]

Pozwala to uniknąć uruchamiania osobnego podprocesu QMD dla każdej kolekcji trwałej pamięci. Kolekcje transkrypcji sesji pozostają we własnej grupie źródeł, więc mieszane wyszukiwania `memory` \+ `sessions` nadal dostarczają dywersyfikatorowi wyników dane z obu źródeł.

Starsze kompilacje QMD akceptują tylko jeden filtr kolekcji. Gdy OpenClaw wykryje jedną z takich kompilacji, utrzymuje ścieżkę zgodności i przeszukuje każdą kolekcję osobno przed scaleniem i deduplikacją wyników.

Aby ręcznie sprawdzić zainstalowany kontrakt, uruchom:

bashCopy code
[code]
    qmd --help | grep -i collection
[/code]

Bieżąca pomoc QMD mówi, że filtry kolekcji mogą kierować do jednej lub większej liczby kolekcji. Starsza pomoc zwykle opisuje pojedynczą kolekcję.

## Nadpisania modeli

Zmienne środowiskowe modeli QMD przechodzą niezmienione z procesu Gateway, więc możesz dostrajać QMD globalnie bez dodawania nowej konfiguracji OpenClaw:

bashCopy code
[code]
    export QMD_EMBED_MODEL="hf:Qwen/Qwen3-Embedding-0.6B-GGUF/Qwen3-Embedding-0.6B-Q8_0.gguf"export QMD_RERANK_MODEL="/absolute/path/to/reranker.gguf"export QMD_GENERATE_MODEL="/absolute/path/to/generator.gguf"
[/code]

Po zmianie modelu osadzeń uruchom osadzanie ponownie, aby indeks pasował do nowej przestrzeni wektorowej.

## Indeksowanie dodatkowych ścieżek

Wskaż QMD dodatkowe katalogi, aby można było je przeszukiwać:

json5Copy code
[code]
    {  memory: {    backend: "qmd",    qmd: {      paths: [{ name: "docs", path: "~/notes", pattern: "**/*.md" }],    },  },}
[/code]

Fragmenty z dodatkowych ścieżek pojawiają się w wynikach wyszukiwania jako `qmd/<collection>/<relative-path>`. `memory_get` rozumie ten prefiks i odczytuje z właściwego katalogu głównego kolekcji.

## Indeksowanie transkrypcji sesji

Włącz indeksowanie sesji, aby przywoływać wcześniejsze rozmowy:

json5Copy code
[code]
    {  memory: {    backend: "qmd",    qmd: {      sessions: { enabled: true },    },  },}
[/code]

Transkrypcje są eksportowane jako oczyszczone tury Użytkownik/Asystent do dedykowanej kolekcji QMD pod `~/.openclaw/agents/<id>/qmd/sessions/`.

## Zakres wyszukiwania

Domyślnie wyniki wyszukiwania QMD są udostępniane w sesjach bezpośrednich i kanałowych (nie w grupach). Skonfiguruj `memory.qmd.scope`, aby to zmienić:

json5Copy code
[code]
    {  memory: {    qmd: {      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },    },  },}
[/code]

Gdy zakres odmawia wyszukiwania, OpenClaw zapisuje ostrzeżenie z wyprowadzonym kanałem i typem czatu, aby łatwiej debugować puste wyniki.

## Cytowania

Gdy `memory.citations` ma wartość `auto` albo `on`, fragmenty wyszukiwania zawierają stopkę `Source: <path#line>`. Ustaw `memory.citations = "off"`, aby pominąć stopkę, nadal przekazując ścieżkę agentowi wewnętrznie.

## Kiedy używać

Wybierz QMD, gdy potrzebujesz:

  * Ponownego rankingowania dla wyników wyższej jakości.
  * Wyszukiwania dokumentacji projektu lub notatek poza obszarem roboczym.
  * Przywoływania rozmów z poprzednich sesji.
  * W pełni lokalnego wyszukiwania bez kluczy API.


W prostszych konfiguracjach [wbudowany silnik](</pl/concepts/memory-builtin>) działa dobrze bez dodatkowych zależności.

## Rozwiązywanie problemów

**Nie znaleziono QMD?** Upewnij się, że plik binarny znajduje się w `PATH` Gateway. Jeśli OpenClaw działa jako usługa, utwórz dowiązanie symboliczne: `sudo ln -s ~/.bun/bin/qmd /usr/local/bin/qmd`.

Jeśli `qmd --version` działa w Twojej powłoce, ale OpenClaw nadal zgłasza `spawn qmd ENOENT`, proces Gateway prawdopodobnie ma inny `PATH` niż Twoja powłoka interaktywna. Przypnij plik binarny jawnie:

json5Copy code
[code]
    {  memory: {    backend: "qmd",    qmd: {      command: "/absolute/path/to/qmd",    },  },}
[/code]

Użyj `command -v qmd` w środowisku, w którym QMD jest zainstalowane, a następnie sprawdź ponownie za pomocą `openclaw memory status --deep`.

**Pierwsze wyszukiwanie bardzo wolne?** QMD pobiera modele GGUF przy pierwszym użyciu. Rozgrzej za pomocą `qmd query "test"`, używając tych samych katalogów XDG, których używa OpenClaw.

**Wiele podprocesów QMD podczas wyszukiwania?** Jeśli to możliwe, zaktualizuj QMD. OpenClaw używa jednego procesu dla wyszukiwań wielu kolekcji z tego samego źródła tylko wtedy, gdy zainstalowane QMD deklaruje obsługę wielu filtrów `-c`; w przeciwnym razie zachowuje starsze przełączenie awaryjne na pojedyncze kolekcje dla poprawności.

**QMD tylko z BM25 nadal próbuje budować llama.cpp?** Ustaw `memory.qmd.searchMode = "search"`. OpenClaw traktuje ten tryb jako wyłącznie leksykalny, nie uruchamia sond statusu wektorów QMD ani utrzymania osadzeń i pozostawia semantyczne kontrole gotowości konfiguracjom `vsearch` lub `query`.

**Wyszukiwanie przekracza limit czasu?** Zwiększ `memory.qmd.limits.timeoutMs` (domyślnie: 4000ms). Ustaw na `120000` dla wolniejszego sprzętu.

**Puste wyniki w czatach grupowych?** Sprawdź `memory.qmd.scope` \-- domyślnie zezwala tylko na sesje bezpośrednie i kanałowe.

**Wyszukiwanie pamięci głównej nagle stało się zbyt szerokie?** Uruchom ponownie Gateway albo poczekaj na następne uzgadnianie przy starcie. OpenClaw odtwarza przestarzałe zarządzane kolekcje do kanonicznych wzorców `MEMORY.md` i `memory/`, gdy wykryje konflikt tej samej nazwy.

**Widoczne w obszarze roboczym tymczasowe repozytoria powodują`ENAMETOOLONG` albo uszkodzone indeksowanie?** Przechodzenie QMD obecnie podąża za zachowaniem bazowego skanera QMD, a nie za wbudowanymi regułami dowiązań symbolicznych OpenClaw. Trzymaj tymczasowe checkouty monorepo pod ukrytymi katalogami, takimi jak `.tmp/`, albo poza indeksowanymi katalogami głównymi QMD, dopóki QMD nie udostępni przechodzenia bezpiecznego względem cykli albo jawnych kontrolek wykluczeń.

## Konfiguracja

Pełny zakres konfiguracji (`memory.qmd.*`), tryby wyszukiwania, interwały aktualizacji, reguły zakresu i wszystkie inne pokrętła znajdziesz w [odniesieniu konfiguracji pamięci](</pl/reference/memory-config>).

## Powiązane

  * [Omówienie pamięci](</pl/concepts/memory>)
  * [Wbudowany silnik pamięci](</pl/concepts/memory-builtin>)
  * [Pamięć Honcho](</pl/concepts/memory-honcho>)


Was this useful?YesNo
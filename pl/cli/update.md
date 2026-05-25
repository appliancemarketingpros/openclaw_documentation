---
title: Aktualizacja
source_url: https://docs.openclaw.ai/pl/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Bezpiecznie aktualizuj OpenClaw i przełączaj się między kanałami stable/beta/dev.

Jeśli instalacja została wykonana przez **npm/pnpm/bun** (instalacja globalna, bez metadanych git), aktualizacje odbywają się przez przepływ menedżera pakietów opisany w [Aktualizowanie](</pl/install/updating>).

## Użycie

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Opcje

  * `--no-restart`: pomija ponowne uruchomienie usługi Gateway po udanej aktualizacji. Aktualizacje przez menedżer pakietów, które ponownie uruchamiają Gateway, weryfikują, czy ponownie uruchomiona usługa zgłasza oczekiwaną zaktualizowaną wersję, zanim polecenie zakończy się powodzeniem.
  * `--channel <stable|beta|dev>`: ustawia kanał aktualizacji (git + npm; zapisywany w konfiguracji).
  * `--tag <dist-tag|version|spec>`: nadpisuje docelowy pakiet tylko dla tej aktualizacji. Dla instalacji pakietowych `main` mapuje się na `github:openclaw/openclaw#main`.
  * `--dry-run`: pokazuje planowane działania aktualizacji (kanał/tag/cel/przepływ ponownego uruchomienia) bez zapisywania konfiguracji, instalowania, synchronizowania wtyczek ani ponownego uruchamiania.
  * `--json`: wypisuje czytelny maszynowo JSON `UpdateRunResult`, w tym `postUpdate.plugins.warnings`, gdy uszkodzone lub niemożliwe do załadowania zarządzane wtyczki wymagają naprawy po udanej aktualizacji rdzenia, szczegóły awaryjnego użycia wersji wtyczki dla kanału beta, gdy wtyczka nie ma wydania beta, oraz `postUpdate.plugins.integrityDrifts`, gdy podczas synchronizacji wtyczek po aktualizacji wykryto rozbieżność artefaktu wtyczki npm.
  * `--timeout <seconds>`: limit czasu na krok (domyślnie 1800 s).
  * `--yes`: pomija monity o potwierdzenie (na przykład potwierdzenie obniżenia wersji).


`openclaw update` nie ma flagi `--verbose`. Użyj `--dry-run`, aby podejrzeć planowane działania kanału/tagu/instalacji/ponownego uruchomienia, `--json` dla czytelnych maszynowo wyników oraz `openclaw update status --json`, gdy potrzebujesz tylko szczegółów kanału i dostępności. Jeśli debugujesz logi Gateway podczas aktualizacji, szczegółowość konsoli i poziom logowania do pliku są oddzielne: `--verbose` dla Gateway wpływa na wyjście terminala/WebSocket, natomiast logi plikowe wymagają `logging.level: "debug"` lub `"trace"` w konfiguracji. Zobacz [Logowanie Gateway](</pl/gateway/logging>).

## `update status`

Pokazuje aktywny kanał aktualizacji + tag/gałąź/SHA git (dla checkoutów źródłowych) oraz dostępność aktualizacji.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Opcje:

  * `--json`: wypisuje czytelny maszynowo JSON statusu.
  * `--timeout <seconds>`: limit czasu dla sprawdzeń (domyślnie 3 s).


## `update wizard`

Interaktywny przepływ wyboru kanału aktualizacji i potwierdzenia, czy ponownie uruchomić Gateway po aktualizacji (domyślnie ponowne uruchomienie). Jeśli wybierzesz `dev` bez checkoutu git, zaproponuje jego utworzenie.

Opcje:

  * `--timeout <seconds>`: limit czasu dla każdego kroku aktualizacji (domyślnie `1800`)


## Co robi

Gdy przełączasz kanały jawnie (`--channel ...`), OpenClaw utrzymuje także zgodność metody instalacji:

  * `dev` → zapewnia checkout git (domyślnie: `~/openclaw`, nadpisanie przez `OPENCLAW_GIT_DIR`), aktualizuje go i instaluje globalny CLI z tego checkoutu.
  * `stable` → instaluje z npm przy użyciu `latest`.
  * `beta` → preferuje dist-tag npm `beta`, ale wraca do `latest`, gdy beta jest brakująca lub starsza niż bieżące wydanie stable.


Automatyczny aktualizator rdzenia Gateway (gdy jest włączony przez konfigurację) uruchamia ścieżkę aktualizacji CLI poza aktywną obsługą żądania Gateway. Aktualizacje menedżera pakietów przez płaszczyznę sterowania `update.run` wymuszają nieodroczone ponowne uruchomienie aktualizacyjne bez cooldownu po podmianie pakietu, ponieważ stary proces Gateway nadal może mieć w pamięci fragmenty wskazujące na pliki usunięte przez nowy pakiet.

W przypadku instalacji przez menedżer pakietów `openclaw update` rozwiązuje docelową wersję pakietu przed wywołaniem menedżera pakietów. Globalne instalacje npm używają instalacji etapowej: OpenClaw instaluje nowy pakiet w tymczasowym prefiksie npm, weryfikuje spis zapakowanego `dist`, a następnie podmienia to czyste drzewo pakietu na rzeczywisty prefiks globalny. Jeśli weryfikacja się nie powiedzie, doctor po aktualizacji, synchronizacja wtyczek i ponowne uruchomienie nie są wykonywane z podejrzanego drzewa. Nawet gdy zainstalowana wersja już odpowiada celowi, polecenie odświeża globalną instalację pakietu, a następnie uruchamia synchronizację wtyczek, odświeżenie uzupełnień poleceń rdzenia i ponowne uruchomienie. Dzięki temu spakowane sidecary i rekordy wtyczek należące do kanału pozostają zgodne z zainstalowaną kompilacją OpenClaw, a pełne przebudowy uzupełnień poleceń wtyczek pozostają dla jawnych uruchomień `openclaw completion --write-state`.

Gdy zainstalowana jest lokalna zarządzana usługa Gateway i włączono ponowne uruchomienie, aktualizacje menedżera pakietów zatrzymują działającą usługę przed zastąpieniem drzewa pakietu, następnie odświeżają metadane usługi ze zaktualizowanej instalacji, ponownie uruchamiają usługę i weryfikują, czy ponownie uruchomiony Gateway zgłasza oczekiwaną wersję przed zgłoszeniem powodzenia. W systemie macOS sprawdzenie po aktualizacji weryfikuje także, czy LaunchAgent jest załadowany/uruchomiony dla aktywnego profilu oraz czy skonfigurowany port loopback jest zdrowy. Jeśli plist jest zainstalowany, ale launchd go nie nadzoruje, OpenClaw automatycznie ponownie bootstrapuje LaunchAgent, a następnie ponownie uruchamia sprawdzenia gotowości zdrowia/wersji/kanału. Świeży bootstrap ładuje zadanie RunAtLoad bezpośrednio, więc odzyskiwanie aktualizacji nie wykonuje natychmiast `kickstart -k` na nowo uruchomionym Gateway. Jeśli Gateway nadal nie stanie się zdrowy, polecenie kończy się kodem różnym od zera i wypisuje ścieżkę logu ponownego uruchomienia oraz jawne instrukcje ponownego uruchomienia, ponownej instalacji i wycofania pakietu. Z `--no-restart` zastąpienie pakietu nadal jest wykonywane, ale zarządzana usługa nie jest zatrzymywana ani ponownie uruchamiana, więc działający Gateway może zachować stary kod, dopóki nie uruchomisz go ponownie ręcznie.

## Przepływ checkoutu git

### Wybór kanału

  * `stable`: wykonuje checkout najnowszego tagu nie-beta, a następnie build i doctor.
  * `beta`: preferuje najnowszy tag `-beta`, ale wraca do najnowszego tagu stable, gdy beta jest brakująca lub starsza.
  * `dev`: wykonuje checkout `main`, a następnie fetch i rebase.


### Kroki aktualizacji

* ### Weryfikacja czystego worktree

Wymaga braku niezatwierdzonych zmian.

* ### Przełączenie kanału

Przełącza na wybrany kanał (tag lub gałąź).

* ### Fetch upstream

Tylko dev.

* ### Build preflight (tylko dev)

Uruchamia build TypeScript w tymczasowym worktree. Jeśli tip się nie powiedzie, cofa się maksymalnie o 10 commitów, aby znaleźć najnowszy commit możliwy do zbudowania. Ustaw `OPENCLAW_UPDATE_PREFLIGHT_LINT=1`, aby podczas tego preflight uruchomić także lint; lint działa w ograniczonym trybie szeregowym, ponieważ hosty aktualizacji użytkowników są często mniejsze niż runnerzy CI.

* ### Rebase

Wykonuje rebase na wybrany commit (tylko dev).

* ### Instalacja zależności

Używa menedżera pakietów repozytorium. Dla checkoutów pnpm aktualizator bootstrapuje `pnpm` na żądanie (najpierw przez `corepack`, potem awaryjnie przez tymczasowe `npm install pnpm@11`) zamiast uruchamiać `npm run build` wewnątrz workspace pnpm.

* ### Build Control UI

Buduje gateway i Control UI.

* ### Uruchomienie doctor

`openclaw doctor` działa jako końcowe sprawdzenie bezpiecznej aktualizacji.

* ### Synchronizacja wtyczek

Synchronizuje wtyczki do aktywnego kanału. Dev używa wtyczek wbudowanych; stable i beta używają npm. Aktualizuje śledzone instalacje wtyczek.

Na kanale aktualizacji beta śledzone instalacje wtyczek npm i ClawHub, które podążają za domyślną/najnowszą linią, najpierw próbują wydania wtyczki `@beta`. Jeśli wtyczka nie ma wydania beta, OpenClaw wraca do zapisanej domyślnej/najnowszej specyfikacji i zgłasza to jako ostrzeżenie. Dla wtyczek npm OpenClaw wraca także wtedy, gdy pakiet beta istnieje, ale nie przejdzie walidacji instalacji. Te ostrzeżenia o awaryjnym wyborze wtyczek nie powodują niepowodzenia aktualizacji rdzenia. Dokładne wersje i jawne tagi nie są przepisywane.

## Skrót `--update`

`openclaw --update` przepisuje się na `openclaw update` (przydatne dla powłok i skryptów uruchamiających).

## Powiązane

  * `openclaw doctor` (proponuje najpierw uruchomić aktualizację na checkoutach git)
  * [Kanały deweloperskie](</pl/install/development-channels>)
  * [Aktualizowanie](</pl/install/updating>)
  * [Dokumentacja CLI](</pl/cli>)


Was this useful?YesNo
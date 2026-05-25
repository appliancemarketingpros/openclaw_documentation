---
title: Wewnętrzne mechanizmy instalatora
source_url: https://docs.openclaw.ai/pl/install/installer
scraped_at: 2026-05-25
---

OpenClaw dostarcza trzy skrypty instalacyjne, serwowane z `openclaw.ai`.

Skrypt | Platforma | Co robi  
---|---|---  
`install.sh` | macOS / Linux / WSL | Instaluje Node, jeśli jest potrzebny, instaluje OpenClaw przez npm (domyślnie) albo git i może uruchomić onboarding.  
`install-cli.sh` | macOS / Linux / WSL | Instaluje Node + OpenClaw w lokalnym prefiksie (`~/.openclaw`) w trybach npm albo checkout git. Nie wymaga uprawnień root.  
`install.ps1` | Windows (PowerShell) | Instaluje Node, jeśli jest potrzebny, instaluje OpenClaw przez npm (domyślnie) albo git i może uruchomić onboarding.  
  
## Szybkie polecenia

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Przebieg ([install.sh](<http://install.sh>))

* ### Wykryj system operacyjny

Obsługuje macOS i Linux (w tym WSL). Jeśli wykryje macOS, instaluje Homebrew, jeśli go brakuje.

* ### Domyślnie zapewnij Node.js 24

Sprawdza wersję Node i instaluje Node 24, jeśli jest potrzebny (Homebrew w macOS, skrypty konfiguracyjne NodeSource w Linux apt/dnf/yum). OpenClaw nadal obsługuje Node 22 LTS, obecnie `22.16+`, dla zgodności.

* ### Zapewnij Git

Instaluje Git, jeśli go brakuje.

* ### Zainstaluj OpenClaw

  * metoda `npm` (domyślna): globalna instalacja npm
  * metoda `git`: klonuje/aktualizuje repozytorium, instaluje zależności za pomocą pnpm, buduje, a następnie instaluje wrapper w `~/.local/bin/openclaw`


* ### Zadania po instalacji

  * Odświeża załadowaną usługę Gateway w trybie best-effort (`openclaw gateway install --force`, potem restart)
  * Uruchamia `openclaw doctor --non-interactive` przy aktualizacjach i instalacjach git (best effort)
  * Próbuje uruchomić onboarding, gdy jest to odpowiednie (TTY dostępne, onboarding nie jest wyłączony, a sprawdzenia bootstrap/config przechodzą)
  * Domyślnie ustawia `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Wykrywanie checkoutu źródeł

Jeśli skrypt zostanie uruchomiony wewnątrz checkoutu OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), proponuje:

  * użycie checkoutu (`git`), albo
  * użycie instalacji globalnej (`npm`)


Jeśli TTY nie jest dostępne i nie ustawiono metody instalacji, domyślnie wybiera `npm` i wyświetla ostrzeżenie.

Skrypt kończy działanie kodem `2` przy nieprawidłowym wyborze metody lub nieprawidłowych wartościach `--install-method`.

### Przykłady ([install.sh](<http://install.sh>))

### Domyślne

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Pomiń onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Instalacja git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main przez npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Próba bez zmian

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Opis flag Flaga | Opis  
---|---  
`--install-method npm|git` | Wybierz metodę instalacji (domyślnie: `npm`). Alias: `--method`  
`--npm` | Skrót dla metody npm  
`--git` | Skrót dla metody git. Alias: `--github`  
`--version <version|dist-tag|spec>` | Wersja npm, dist-tag albo specyfikacja pakietu (domyślnie: `latest`)  
`--beta` | Użyj dist-tag beta, jeśli dostępny, w przeciwnym razie wróć do `latest`  
`--git-dir <path>` | Katalog checkoutu (domyślnie: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | Pomiń `git pull` dla istniejącego checkoutu  
`--no-prompt` | Wyłącz monity  
`--no-onboard` | Pomiń onboarding  
`--onboard` | Włącz onboarding  
`--dry-run` | Wypisz działania bez stosowania zmian  
`--verbose` | Włącz wyjście debugowania (`set -x`, logi npm na poziomie notice)  
`--help` | Pokaż użycie (`-h`)  
Opis zmiennych środowiskowych Zmienna | Opis  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metoda instalacji  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Wersja npm, dist-tag albo specyfikacja pakietu  
`OPENCLAW_BETA=0|1` | Użyj beta, jeśli dostępne  
`OPENCLAW_GIT_DIR=<path>` | Katalog checkoutu  
`OPENCLAW_GIT_UPDATE=0|1` | Przełącz aktualizacje git  
`OPENCLAW_NO_PROMPT=1` | Wyłącz monity  
`OPENCLAW_NO_ONBOARD=1` | Pomiń onboarding  
`OPENCLAW_DRY_RUN=1` | Tryb próby bez zmian  
`OPENCLAW_VERBOSE=1` | Tryb debugowania  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Poziom logowania npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Kontroluj zachowanie sharp/libvips (domyślnie: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Przebieg ([install-cli.sh](<http://install-cli.sh>))

* ### Zainstaluj lokalne środowisko uruchomieniowe Node

Pobiera przypięte, obsługiwane archiwum tar Node LTS (wersja jest osadzona w skrypcie i aktualizowana niezależnie) do `<prefix>/tools/node-v<version>` i weryfikuje SHA-256.

* ### Zapewnij Git

Jeśli brakuje Git, próbuje zainstalować go przez apt/dnf/yum w Linux albo Homebrew w macOS.

* ### Zainstaluj OpenClaw pod prefiksem

  * metoda `npm` (domyślna): instaluje pod prefiksem za pomocą npm, a następnie zapisuje wrapper do `<prefix>/bin/openclaw`
  * metoda `git`: klonuje/aktualizuje checkout (domyślnie `~/openclaw`) i nadal zapisuje wrapper do `<prefix>/bin/openclaw`


* ### Odśwież załadowaną usługę Gateway

Jeśli usługa Gateway jest już załadowana z tego samego prefiksu, skrypt uruchamia `openclaw gateway install --force`, następnie `openclaw gateway restart` i sprawdza stan Gateway w trybie best-effort.

### Przykłady ([install-cli.sh](<http://install-cli.sh>))

### Domyślne

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Niestandardowy prefiks + wersja

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Instalacja git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Wyjście JSON automatyzacji

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Uruchom onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Opis flag Flaga | Opis  
---|---  
`--prefix <path>` | Prefiks instalacji (domyślnie: `~/.openclaw`)  
`--install-method npm|git` | Wybierz metodę instalacji (domyślnie: `npm`). Alias: `--method`  
`--npm` | Skrót dla metody npm  
`--git`, `--github` | Skrót dla metody git  
`--git-dir <path>` | Katalog checkoutu git (domyślnie: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | Wersja OpenClaw albo dist-tag (domyślnie: `latest`)  
`--node-version <ver>` | Wersja Node (domyślnie: `22.22.0`)  
`--json` | Emituj zdarzenia NDJSON  
`--onboard` | Uruchom `openclaw onboard` po instalacji  
`--no-onboard` | Pomiń onboarding (domyślnie)  
`--set-npm-prefix` | W Linux wymuś prefiks npm na `~/.npm-global`, jeśli bieżący prefiks nie jest zapisywalny  
`--help` | Pokaż użycie (`-h`)  
Opis zmiennych środowiskowych Zmienna | Opis  
---|---  
`OPENCLAW_PREFIX=<path>` | Prefiks instalacji  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metoda instalacji  
`OPENCLAW_VERSION=<ver>` | Wersja OpenClaw lub dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Wersja Node  
`OPENCLAW_GIT_DIR=<path>` | Katalog checkout Git dla instalacji git  
`OPENCLAW_GIT_UPDATE=0|1` | Przełącznik aktualizacji git dla istniejących checkoutów  
`OPENCLAW_NO_ONBOARD=1` | Pomiń wprowadzanie  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Poziom logowania npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Kontroluj zachowanie sharp/libvips (domyślnie: `1`)  
  
* * *

## install.ps1

### Przebieg (install.ps1)

* ### Zapewnij środowisko PowerShell + Windows

Wymaga PowerShell 5+.

* ### Domyślnie zapewnij Node.js 24

Jeśli go brakuje, próbuje zainstalować przez winget, następnie Chocolatey, a potem Scoop. Node 22 LTS, obecnie `22.16+`, pozostaje obsługiwany dla zgodności.

* ### Zainstaluj OpenClaw

  * Metoda `npm` (domyślna): globalna instalacja npm z użyciem wybranego `-Tag`, uruchamiana z zapisywalnego tymczasowego katalogu instalatora, dzięki czemu powłoki otwarte w chronionych folderach, takich jak `C:\`, nadal działają
  * Metoda `git`: klonowanie/aktualizacja repozytorium, instalacja/budowanie z pnpm oraz instalacja wrappera w `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Zadania po instalacji

  * Dodaje wymagany katalog bin do PATH użytkownika, gdy to możliwe
  * Odświeża załadowaną usługę Gateway w trybie best-effort (`openclaw gateway install --force`, następnie restart)
  * Uruchamia `openclaw doctor --non-interactive` przy aktualizacjach i instalacjach git (best effort)


* ### Obsłuż błędy

Instalacje `iwr ... | iex` i scriptblock zgłaszają błąd kończący bez zamykania bieżącej sesji PowerShell. Bezpośrednie instalacje `powershell -File` / `pwsh -File` nadal kończą się kodem niezerowym na potrzeby automatyzacji.

### Przykłady (install.ps1)

### Domyślne

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Instalacja Git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main przez npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Niestandardowy katalog git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Przebieg próbny

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Śledzenie debugowania

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Opis flag Flaga | Opis  
---|---  
`-InstallMethod npm|git` | Metoda instalacji (domyślnie: `npm`)  
`-Tag <tag|version|spec>` | npm dist-tag, wersja lub specyfikacja pakietu (domyślnie: `latest`)  
`-GitDir <path>` | Katalog checkout (domyślnie: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Pomiń wprowadzanie  
`-NoGitUpdate` | Pomiń `git pull`  
`-DryRun` | Tylko wypisz działania  
Opis zmiennych środowiskowych Zmienna | Opis  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metoda instalacji  
`OPENCLAW_GIT_DIR=<path>` | Katalog checkout  
`OPENCLAW_NO_ONBOARD=1` | Pomiń wprowadzanie  
`OPENCLAW_GIT_UPDATE=0` | Wyłącz git pull  
`OPENCLAW_DRY_RUN=1` | Tryb przebiegu próbnego  
  
* * *

## CI i automatyzacja

Używaj nieinteraktywnych flag/zmiennych środowiskowych, aby uzyskać przewidywalne uruchomienia.

### install.sh (nieinteraktywne npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (nieinteraktywne git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (pomiń wprowadzanie)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Rozwiązywanie problemów

Dlaczego Git jest wymagany?

Git jest wymagany dla metody instalacji `git`. W przypadku instalacji `npm` Git nadal jest sprawdzany/instalowany, aby uniknąć błędów `spawn git ENOENT`, gdy zależności używają adresów URL git.

Dlaczego npm napotyka EACCES w systemie Linux?

Niektóre konfiguracje Linuksa wskazują globalny prefiks npm na ścieżki należące do root. `install.sh` może przełączyć prefiks na `~/.npm-global` i dopisać eksporty PATH do plików rc powłoki (gdy te pliki istnieją).

Problemy z sharp/libvips

Skrypty domyślnie ustawiają `SHARP_IGNORE_GLOBAL_LIBVIPS=1`, aby uniknąć budowania sharp względem systemowego libvips. Aby nadpisać:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Zainstaluj Git for Windows, otwórz ponownie PowerShell, uruchom ponownie instalator.

Windows: "openclaw is not recognized"

Uruchom `npm config get prefix` i dodaj ten katalog do PATH użytkownika (w Windows nie jest wymagany sufiks `\bin`), a następnie otwórz ponownie PowerShell.

Windows: jak uzyskać szczegółowe dane wyjściowe instalatora

`install.ps1` obecnie nie udostępnia przełącznika `-Verbose`. Użyj śledzenia PowerShell do diagnostyki na poziomie skryptu:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Nie znaleziono openclaw po instalacji

Zwykle jest to problem z PATH. Zobacz [rozwiązywanie problemów z Node.js](</pl/install/node#troubleshooting>).

## Powiązane

  * [Omówienie instalacji](</pl/install>)
  * [Aktualizowanie](</pl/install/updating>)
  * [Odinstalowanie](</pl/install/uninstall>)


Was this useful?YesNo
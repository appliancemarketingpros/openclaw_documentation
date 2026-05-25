---
title: Node.js
source_url: https://docs.openclaw.ai/pl/install/node
scraped_at: 2026-05-25
---

OpenClaw wymaga **Node 22.16 lub nowszego**. **Node 24 jest domyślnym i zalecanym środowiskiem uruchomieniowym** dla instalacji, CI i przepływów wydań. Node 22 pozostaje wspierany w ramach aktywnej linii LTS. [Skrypt instalacyjny](</pl/install#alternative-install-methods>) automatycznie wykryje i zainstaluje Node - ta strona jest przeznaczona dla sytuacji, gdy chcesz samodzielnie skonfigurować Node i upewnić się, że wszystko jest poprawnie połączone (wersje, PATH, instalacje globalne).

## Sprawdź swoją wersję

bashCopy code
[code]
    node -v
[/code]

Jeśli polecenie wypisze `v24.x.x` lub nowszą wersję, używasz zalecanej wartości domyślnej. Jeśli wypisze `v22.16.x` lub nowszą wersję, używasz obsługiwanej ścieżki Node 22 LTS, ale nadal zalecamy przejście na Node 24, gdy będzie to wygodne. Jeśli Node nie jest zainstalowany albo wersja jest zbyt stara, wybierz jedną z metod instalacji poniżej.

## Zainstaluj Node

### macOS

**Homebrew** (zalecane):

bashCopy code
[code]
    brew install node
[/code]

Albo pobierz instalator dla macOS z [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Albo użyj menedżera wersji (zobacz poniżej).

### Windows

**winget** (zalecane):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Albo pobierz instalator dla Windows z [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

Menedżery wersji pozwalają łatwo przełączać się między wersjami Node. Popularne opcje:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- szybki, wieloplatformowy
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- powszechnie używany na macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- wielojęzykowy (Node, Python, Ruby itd.)


Przykład z fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Rozwiązywanie problemów

### `openclaw: command not found`

To prawie zawsze oznacza, że globalny katalog bin npm nie znajduje się w PATH.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Poszukaj `<npm-prefix>/bin` (macOS/Linux) lub `<npm-prefix>` (Windows) w wyniku.

* ### Add it to your shell startup file

### macOS / Linux

Dodaj do `~/.zshrc` lub `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Następnie otwórz nowy terminal (albo uruchom `rehash` w zsh / `hash -r` w bash).

### Windows

Dodaj wynik `npm prefix -g` do systemowej zmiennej PATH przez Ustawienia → System → Zmienne środowiskowe.

### Błędy uprawnień przy `npm install -g` (Linux)

Jeśli widzisz błędy `EACCES`, zmień globalny prefiks npm na katalog zapisywalny przez użytkownika:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Dodaj wiersz `export PATH=...` do `~/.bashrc` lub `~/.zshrc`, aby zmiana była trwała.

## Powiązane

  * [Przegląd instalacji](</pl/install>) \- wszystkie metody instalacji
  * [Aktualizowanie](</pl/install/updating>) \- utrzymywanie OpenClaw na bieżąco
  * [Pierwsze kroki](</pl/start/getting-started>) \- pierwsze kroki po instalacji


Was this useful?YesNo
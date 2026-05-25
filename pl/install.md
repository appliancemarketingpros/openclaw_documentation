---
title: Instalacja
source_url: https://docs.openclaw.ai/pl/install
scraped_at: 2026-05-25
---

## Wymagania systemowe

  * **Node 24** (zalecane) lub Node 22.16+ - skrypt instalatora obsługuje to automatycznie
  * **macOS, Linux lub Windows** \- obsługiwane są zarówno natywny Windows, jak i WSL2; WSL2 jest stabilniejszy. Zobacz [Windows](</pl/platforms/windows>).
  * `pnpm` jest potrzebny tylko wtedy, gdy budujesz ze źródeł


## Zalecane: skrypt instalatora

Najszybszy sposób instalacji. Wykrywa system operacyjny, instaluje Node w razie potrzeby, instaluje OpenClaw i uruchamia onboarding.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Aby zainstalować bez uruchamiania onboardingu:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Wszystkie flagi oraz opcje CI/automatyzacji znajdziesz w sekcji [Wewnętrzne działanie instalatora](</pl/install/installer>).

## Alternatywne metody instalacji

### Instalator z lokalnym prefiksem (`install-cli.sh`)

Użyj tego, gdy chcesz, aby OpenClaw i Node były przechowywane pod lokalnym prefiksem, takim jak `~/.openclaw`, bez zależności od systemowej instalacji Node:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Domyślnie obsługuje instalacje npm, a także instalacje z git checkout w ramach tego samego przepływu z prefiksem. Pełna dokumentacja: [Wewnętrzne działanie instalatora](</pl/install/installer#install-clish>).

Masz już instalację? Przełączaj się między instalacjami z pakietu i z git za pomocą `openclaw update --channel dev` oraz `openclaw update --channel stable`. Zobacz [Aktualizacja](</pl/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm lub bun

Jeśli samodzielnie zarządzasz już Node:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Troubleshooting: sharp build errors (npm)

Jeśli `sharp` nie działa z powodu globalnie zainstalowanego libvips:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Ze źródeł

Dla kontrybutorów lub każdego, kto chce uruchamiać z lokalnego checkoutu:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Możesz też pominąć linkowanie i używać `pnpm openclaw ...` z wnętrza repozytorium. Zobacz [Konfiguracja](</pl/start/setup>), aby poznać pełne przepływy pracy deweloperskiej.

### Instalacja z GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Kontenery i menedżery pakietów

[**Docker** Wdrożenia w kontenerach lub bez interfejsu graficznego. ](</pl/install/docker>) [**Podman** Bezrootowa alternatywa kontenerowa dla Docker. ](</pl/install/podman>) [**Nix** Deklaratywna instalacja przez Nix flake. ](</pl/install/nix>) [**Ansible** Automatyczne wdrażanie floty. ](</pl/install/ansible>) [**Bun** Użycie wyłącznie CLI przez środowisko uruchomieniowe Bun. ](</pl/install/bun>)

## Weryfikacja instalacji

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Jeśli po instalacji chcesz mieć zarządzane uruchamianie:

  * macOS: LaunchAgent przez `openclaw onboard --install-daemon` lub `openclaw gateway install`
  * Linux/WSL2: usługa użytkownika systemd przez te same polecenia
  * Natywny Windows: najpierw Zaplanowane zadanie, z awaryjną pozycją logowania w folderze Autostart dla danego użytkownika, jeśli utworzenie zadania zostanie odrzucone


## Hosting i wdrażanie

Wdróż OpenClaw na serwerze w chmurze lub VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9wbC9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Aktualizacja, migracja lub odinstalowanie [**Updating** Utrzymuj OpenClaw na bieżąco. ](</pl/install/updating>) [**Migrating** Przenieś na nową maszynę. ](</pl/install/migrating>) [**Uninstall** Całkowicie usuń OpenClaw. ](</pl/install/uninstall>) Rozwiązywanie problemów: nie znaleziono `openclaw` Jeśli instalacja się powiodła, ale `openclaw` nie jest znajdowany w terminalu: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Jeśli `$(npm prefix -g)/bin` nie znajduje się w Twoim `$PATH`, dodaj go do pliku startowego powłoki (`~/.zshrc` lub `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Następnie otwórz nowy terminal. Więcej szczegółów znajdziesz w sekcji [Konfiguracja Node](</pl/install/node>). ](</pl/install/northflank>) Was this useful?YesNo ](</pl/install/render>)](</pl/install/railway>)](</pl/install/azure>)](</pl/install/gcp>)](</pl/install/hetzner>)](</pl/install/kubernetes>)](</pl/install/docker-vm-runtime>)](</pl/vps>)
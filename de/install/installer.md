---
title: Installer-Interna
source_url: https://docs.openclaw.ai/de/install/installer
scraped_at: 2026-05-25
---

OpenClaw liefert drei Installationsskripte aus, die von `openclaw.ai` bereitgestellt werden.

Skript | Plattform | Funktion  
---|---|---  
`install.sh` | macOS / Linux / WSL | Installiert bei Bedarf Node, installiert OpenClaw über npm (Standard) oder git und kann das Onboarding ausführen.  
`install-cli.sh` | macOS / Linux / WSL | Installiert Node + OpenClaw mit npm- oder git-Checkout-Modus in ein lokales Präfix (`~/.openclaw`). Kein root erforderlich.  
`install.ps1` | Windows (PowerShell) | Installiert bei Bedarf Node, installiert OpenClaw über npm (Standard) oder git und kann das Onboarding ausführen.  
  
## Schnellbefehle

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

### Ablauf ([install.sh](<http://install.sh>))

* ### Detect OS

Unterstützt macOS und Linux (einschließlich WSL). Wenn macOS erkannt wird, wird Homebrew installiert, falls es fehlt.

* ### Ensure Node.js 24 by default

Prüft die Node-Version und installiert bei Bedarf Node 24 (Homebrew unter macOS, NodeSource-Setup-Skripte unter Linux apt/dnf/yum). Aus Kompatibilitätsgründen unterstützt OpenClaw weiterhin Node 22 LTS, derzeit `22.16+`.

* ### Ensure Git

Installiert Git, falls es fehlt.

* ### Install OpenClaw

  * `npm`-Methode (Standard): globale npm-Installation
  * `git`-Methode: Repository klonen/aktualisieren, Abhängigkeiten mit pnpm installieren, bauen, dann Wrapper unter `~/.local/bin/openclaw` installieren


* ### Post-install tasks

  * Aktualisiert nach bestem Aufwand einen geladenen Gateway-Dienst (`openclaw gateway install --force`, dann Neustart)
  * Führt `openclaw doctor --non-interactive` bei Upgrades und git-Installationen aus (nach bestem Aufwand)
  * Versucht bei geeigneten Bedingungen das Onboarding (TTY verfügbar, Onboarding nicht deaktiviert und Bootstrap-/Konfigurationsprüfungen erfolgreich)
  * Setzt standardmäßig `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Erkennung eines Source-Checkouts

Wenn das Skript innerhalb eines OpenClaw-Checkouts ausgeführt wird (`package.json` \+ `pnpm-workspace.yaml`), bietet es Folgendes an:

  * Checkout verwenden (`git`) oder
  * globale Installation verwenden (`npm`)


Wenn kein TTY verfügbar ist und keine Installationsmethode festgelegt wurde, verwendet es standardmäßig `npm` und gibt eine Warnung aus.

Das Skript beendet sich mit Code `2` bei ungültiger Methodenauswahl oder ungültigen `--install-method`-Werten.

### Beispiele ([install.sh](<http://install.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Skip onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Dry run

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Flags reference Flag | Beschreibung  
---|---  
`--install-method npm|git` | Installationsmethode auswählen (Standard: `npm`). Alias: `--method`  
`--npm` | Kurzbefehl für die npm-Methode  
`--git` | Kurzbefehl für die git-Methode. Alias: `--github`  
`--version <version|dist-tag|spec>` | npm-Version, dist-tag oder Paketangabe (Standard: `latest`)  
`--beta` | Beta-dist-tag verwenden, falls verfügbar, sonst Fallback auf `latest`  
`--git-dir <path>` | Checkout-Verzeichnis (Standard: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | `git pull` für vorhandenen Checkout überspringen  
`--no-prompt` | Eingabeaufforderungen deaktivieren  
`--no-onboard` | Onboarding überspringen  
`--onboard` | Onboarding aktivieren  
`--dry-run` | Aktionen ausgeben, ohne Änderungen anzuwenden  
`--verbose` | Debug-Ausgabe aktivieren (`set -x`, npm-Logs auf notice-Level)  
`--help` | Verwendung anzeigen (`-h`)  
Environment variables reference Variable | Beschreibung  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Installationsmethode  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | npm-Version, dist-tag oder Paketangabe  
`OPENCLAW_BETA=0|1` | Beta verwenden, falls verfügbar  
`OPENCLAW_GIT_DIR=<path>` | Checkout-Verzeichnis  
`OPENCLAW_GIT_UPDATE=0|1` | git-Aktualisierungen umschalten  
`OPENCLAW_NO_PROMPT=1` | Eingabeaufforderungen deaktivieren  
`OPENCLAW_NO_ONBOARD=1` | Onboarding überspringen  
`OPENCLAW_DRY_RUN=1` | Probelaufmodus  
`OPENCLAW_VERBOSE=1` | Debug-Modus  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm-Log-Level  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips-Verhalten steuern (Standard: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Ablauf ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

Lädt ein fest gepinntes unterstütztes Node-LTS-Tarball (die Version ist im Skript eingebettet und wird unabhängig aktualisiert) nach `<prefix>/tools/node-v<version>` herunter und verifiziert SHA-256.

* ### Ensure Git

Wenn Git fehlt, wird eine Installation über apt/dnf/yum unter Linux oder Homebrew unter macOS versucht.

* ### Install OpenClaw under prefix

  * `npm`-Methode (Standard): installiert unter dem Präfix mit npm und schreibt dann den Wrapper nach `<prefix>/bin/openclaw`
  * `git`-Methode: klont/aktualisiert einen Checkout (Standard `~/openclaw`) und schreibt den Wrapper dennoch nach `<prefix>/bin/openclaw`


* ### Refresh loaded gateway service

Wenn ein Gateway-Dienst bereits aus demselben Präfix geladen ist, führt das Skript `openclaw gateway install --force`, dann `openclaw gateway restart` aus und prüft die Gateway-Integrität nach bestem Aufwand.

### Beispiele ([install-cli.sh](<http://install-cli.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Custom prefix + version

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Automation JSON output

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Run onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Flags reference Flag | Beschreibung  
---|---  
`--prefix <path>` | Installationspräfix (Standard: `~/.openclaw`)  
`--install-method npm|git` | Installationsmethode auswählen (Standard: `npm`). Alias: `--method`  
`--npm` | Kurzbefehl für die npm-Methode  
`--git`, `--github` | Kurzbefehl für die git-Methode  
`--git-dir <path>` | Git-Checkout-Verzeichnis (Standard: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | OpenClaw-Version oder dist-tag (Standard: `latest`)  
`--node-version <ver>` | Node-Version (Standard: `22.22.0`)  
`--json` | NDJSON-Ereignisse ausgeben  
`--onboard` | Nach der Installation `openclaw onboard` ausführen  
`--no-onboard` | Onboarding überspringen (Standard)  
`--set-npm-prefix` | Unter Linux npm-Präfix auf `~/.npm-global` erzwingen, wenn das aktuelle Präfix nicht beschreibbar ist  
`--help` | Verwendung anzeigen (`-h`)  
Environment variables reference Variable | Beschreibung  
---|---  
`OPENCLAW_PREFIX=<path>` | Installationspräfix  
`OPENCLAW_INSTALL_METHOD=git|npm` | Installationsmethode  
`OPENCLAW_VERSION=<ver>` | OpenClaw-Version oder dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Node-Version  
`OPENCLAW_GIT_DIR=<path>` | Git-Checkout-Verzeichnis für git-Installationen  
`OPENCLAW_GIT_UPDATE=0|1` | git-Updates für vorhandene Checkouts umschalten  
`OPENCLAW_NO_ONBOARD=1` | Onboarding überspringen  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm-Protokollierungsstufe  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips-Verhalten steuern (Standard: `1`)  
  
* * *

## install.ps1

### Ablauf (install.ps1)

* ### PowerShell- und Windows-Umgebung sicherstellen

Erfordert PowerShell 5+.

* ### Standardmäßig Node.js 24 sicherstellen

Falls es fehlt, wird eine Installation über winget versucht, danach über Chocolatey, danach über Scoop. Node 22 LTS, derzeit `22.16+`, bleibt aus Kompatibilitätsgründen unterstützt.

* ### OpenClaw installieren

  * `npm`-Methode (Standard): globale npm-Installation mit dem ausgewählten `-Tag`, gestartet aus einem beschreibbaren temporären Installer-Verzeichnis, damit auch Shells funktionieren, die in geschützten Ordnern wie `C:\` geöffnet wurden
  * `git`-Methode: Repo klonen/aktualisieren, mit pnpm installieren/builden und Wrapper unter `%USERPROFILE%\.local\bin\openclaw.cmd` installieren


* ### Aufgaben nach der Installation

  * Fügt das benötigte bin-Verzeichnis nach Möglichkeit zum Benutzer-PATH hinzu
  * Aktualisiert nach bestem Bemühen einen geladenen Gateway-Dienst (`openclaw gateway install --force`, dann Neustart)
  * Führt `openclaw doctor --non-interactive` bei Upgrades und git-Installationen aus (nach bestem Bemühen)


* ### Fehler behandeln

`iwr ... | iex` und Scriptblock-Installationen melden einen terminierenden Fehler, ohne die aktuelle PowerShell-Sitzung zu schließen. Direkte Installationen mit `powershell -File` / `pwsh -File` beenden sich für Automatisierung weiterhin mit einem Nicht-Null-Status.

### Beispiele (install.ps1)

### Standard

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git-Installation

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main über npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Benutzerdefiniertes git-Verzeichnis

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Testlauf

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Debug-Trace

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Flags-Referenz Flag | Beschreibung  
---|---  
`-InstallMethod npm|git` | Installationsmethode (Standard: `npm`)  
`-Tag <tag|version|spec>` | npm-dist-tag, Version oder Paketspezifikation (Standard: `latest`)  
`-GitDir <path>` | Checkout-Verzeichnis (Standard: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Onboarding überspringen  
`-NoGitUpdate` | `git pull` überspringen  
`-DryRun` | Nur Aktionen ausgeben  
Referenz der Umgebungsvariablen Variable | Beschreibung  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Installationsmethode  
`OPENCLAW_GIT_DIR=<path>` | Checkout-Verzeichnis  
`OPENCLAW_NO_ONBOARD=1` | Onboarding überspringen  
`OPENCLAW_GIT_UPDATE=0` | git pull deaktivieren  
`OPENCLAW_DRY_RUN=1` | Testlaufmodus  
  
* * *

## CI und Automatisierung

Verwenden Sie nicht-interaktive Flags/Umgebungsvariablen für vorhersehbare Ausführungen.

### install.sh (nicht-interaktives npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (nicht-interaktives git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (Onboarding überspringen)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Fehlerbehebung

Warum ist Git erforderlich?

Git ist für die `git`-Installationsmethode erforderlich. Bei `npm`-Installationen wird Git weiterhin geprüft/installiert, um `spawn git ENOENT`-Fehler zu vermeiden, wenn Abhängigkeiten git-URLs verwenden.

Warum trifft npm unter Linux auf EACCES?

Einige Linux-Setups verweisen das globale npm-Präfix auf root-eigene Pfade. `install.sh` kann das Präfix auf `~/.npm-global` umstellen und PATH-Exporte an Shell-rc-Dateien anhängen (wenn diese Dateien vorhanden sind).

sharp/libvips-Probleme

Die Skripte setzen standardmäßig `SHARP_IGNORE_GLOBAL_LIBVIPS=1`, um zu vermeiden, dass sharp gegen das systemweite libvips gebaut wird. Zum Überschreiben:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Installieren Sie Git for Windows, öffnen Sie PowerShell erneut und führen Sie den Installer erneut aus.

Windows: "openclaw is not recognized"

Führen Sie `npm config get prefix` aus und fügen Sie dieses Verzeichnis Ihrem Benutzer-PATH hinzu (unter Windows ist kein `\bin`-Suffix erforderlich), öffnen Sie danach PowerShell erneut.

Windows: ausführliche Installer-Ausgabe erhalten

`install.ps1` stellt derzeit keinen `-Verbose`-Schalter bereit. Verwenden Sie PowerShell-Tracing für Diagnosen auf Skriptebene:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw nach der Installation nicht gefunden

In der Regel ist dies ein PATH-Problem. Siehe [Node.js-Fehlerbehebung](</de/install/node#troubleshooting>).

## Verwandte Themen

  * [Installationsübersicht](</de/install>)
  * [Aktualisierung](</de/install/updating>)
  * [Deinstallation](</de/install/uninstall>)


Was this useful?YesNo
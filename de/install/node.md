---
title: Node.js
source_url: https://docs.openclaw.ai/de/install/node
scraped_at: 2026-05-25
---

OpenClaw benötigt **Node 22.16 oder neuer**. **Node 24 ist die standardmäßige und empfohlene Runtime** für Installationen, CI und Release-Workflows. Node 22 wird weiterhin über den aktiven LTS-Zweig unterstützt. Das [Installationsskript](</de/install#alternative-install-methods>) erkennt und installiert Node automatisch - diese Seite ist für Fälle gedacht, in denen Sie Node selbst einrichten und sicherstellen möchten, dass alles korrekt verbunden ist (Versionen, PATH, globale Installationen).

## Ihre Version prüfen

bashCopy code
[code]
    node -v
[/code]

Wenn dies `v24.x.x` oder höher ausgibt, verwenden Sie den empfohlenen Standard. Wenn es `v22.16.x` oder höher ausgibt, befinden Sie sich auf dem unterstützten Node-22-LTS-Pfad, wir empfehlen dennoch ein Upgrade auf Node 24, sobald es für Sie passt. Wenn Node nicht installiert ist oder die Version zu alt ist, wählen Sie unten eine Installationsmethode.

## Node installieren

### macOS

**Homebrew** (empfohlen):

bashCopy code
[code]
    brew install node
[/code]

Oder laden Sie das macOS-Installationsprogramm von [nodejs.org](<https://nodejs.org/>) herunter.

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

Oder verwenden Sie einen Versionsmanager (siehe unten).

### Windows

**winget** (empfohlen):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Oder laden Sie das Windows-Installationsprogramm von [nodejs.org](<https://nodejs.org/>) herunter.

Einen Versionsmanager verwenden (nvm, fnm, mise, asdf)

Mit Versionsmanagern können Sie einfach zwischen Node-Versionen wechseln. Beliebte Optionen:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- schnell, plattformübergreifend
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- weit verbreitet auf macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- polyglott (Node, Python, Ruby usw.)


Beispiel mit fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Fehlerbehebung

### `openclaw: command not found`

Das bedeutet fast immer, dass sich das globale bin-Verzeichnis von npm nicht in Ihrem PATH befindet.

* ### Ihren globalen npm-Präfix finden

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Prüfen, ob er in Ihrem PATH liegt

bashCopy code
[code]
    echo "$PATH"
[/code]

Suchen Sie in der Ausgabe nach `<npm-prefix>/bin` (macOS/Linux) oder `<npm-prefix>` (Windows).

* ### Ihn zur Startdatei Ihrer Shell hinzufügen

### macOS / Linux

Zu `~/.zshrc` oder `~/.bashrc` hinzufügen:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Öffnen Sie anschließend ein neues Terminal (oder führen Sie `rehash` in zsh / `hash -r` in bash aus).

### Windows

Fügen Sie die Ausgabe von `npm prefix -g` über Einstellungen → System → Umgebungsvariablen zu Ihrem System-PATH hinzu.

### Berechtigungsfehler bei `npm install -g` (Linux)

Wenn Sie `EACCES`-Fehler sehen, ändern Sie den globalen Präfix von npm auf ein Verzeichnis, in das Ihr Benutzer schreiben kann:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Fügen Sie die Zeile `export PATH=...` zu Ihrer `~/.bashrc` oder `~/.zshrc` hinzu, um die Änderung dauerhaft zu machen.

## Verwandte Themen

  * [Installationsübersicht](</de/install>) \- alle Installationsmethoden
  * [Aktualisieren](</de/install/updating>) \- OpenClaw aktuell halten
  * [Erste Schritte](</de/start/getting-started>) \- erste Schritte nach der Installation


Was this useful?YesNo
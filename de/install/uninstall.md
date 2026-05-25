---
title: Deinstallation
source_url: https://docs.openclaw.ai/de/install/uninstall
scraped_at: 2026-05-25
---

Zwei Wege:

  * **Einfacher Weg** , wenn `openclaw` noch installiert ist.
  * **Manuelles Entfernen des Dienstes** , wenn die CLI entfernt wurde, der Dienst aber noch läuft.


## Einfacher Weg (CLI noch installiert)

Empfohlen: Verwenden Sie das integrierte Deinstallationsprogramm:

bashCopy code
[code]
    openclaw uninstall
[/code]

Nicht interaktiv (Automatisierung / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Manuelle Schritte (gleiches Ergebnis):

  1. Gateway-Dienst stoppen:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Gateway-Dienst deinstallieren (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Zustand + Konfiguration löschen:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Wenn Sie `OPENCLAW_CONFIG_PATH` auf einen benutzerdefinierten Ort außerhalb des Zustandsverzeichnisses gesetzt haben, löschen Sie auch diese Datei.

  4. Ihren Workspace löschen (optional, entfernt Agent-Dateien):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Die CLI-Installation entfernen (wählen Sie die Methode, die Sie verwendet haben):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Wenn Sie die macOS-App installiert haben:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Hinweise:

  * Wenn Sie Profile verwendet haben (`--profile` / `OPENCLAW_PROFILE`), wiederholen Sie Schritt 3 für jedes Zustandsverzeichnis (Standards sind `~/.openclaw-<profile>`).
  * Im Remote-Modus befindet sich das Zustandsverzeichnis auf dem **Gateway-Host** , also führen Sie die Schritte 1-4 auch dort aus.


## Manuelles Entfernen des Dienstes (CLI nicht installiert)

Verwenden Sie dies, wenn der Gateway-Dienst weiterläuft, aber `openclaw` fehlt.

### macOS (launchd)

Das Standardlabel ist `ai.openclaw.gateway` (oder `ai.openclaw.<profile>`; veraltete `com.openclaw.*` können noch existieren):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Wenn Sie ein Profil verwendet haben, ersetzen Sie das Label und den Namen der plist durch `ai.openclaw.<profile>`. Entfernen Sie auch eventuell vorhandene veraltete `com.openclaw.*`-plists.

### Linux (systemd-User-Unit)

Der Standardname der Unit ist `openclaw-gateway.service` (oder `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Geplante Aufgabe)

Der Standardname der Aufgabe ist `OpenClaw Gateway` (oder `OpenClaw Gateway (<profile>)`). Das Task-Skript befindet sich unter Ihrem Zustandsverzeichnis.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Wenn Sie ein Profil verwendet haben, löschen Sie den entsprechenden Aufgabennamen und `~\.openclaw-<profile>\gateway.cmd`.

## Normale Installation vs. Source-Checkout

### Normale Installation ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Wenn Sie `https://openclaw.ai/install.sh` oder `install.ps1` verwendet haben, wurde die CLI mit `npm install -g openclaw@latest` installiert. Entfernen Sie sie mit `npm rm -g openclaw` (oder `pnpm remove -g` / `bun remove -g`, wenn Sie auf diese Weise installiert haben).

### Source-Checkout (git clone)

Wenn Sie aus einem Repo-Checkout ausführen (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Deinstallieren Sie den Gateway-Dienst **bevor** Sie das Repo löschen (verwenden Sie den einfachen Weg oben oder das manuelle Entfernen des Dienstes).
  2. Löschen Sie das Repo-Verzeichnis.
  3. Entfernen Sie Zustand + Workspace wie oben gezeigt.


## Verwandt

  * [Install overview](</de/install>)
  * [Migration guide](</de/install/migrating>)


Was this useful?YesNo
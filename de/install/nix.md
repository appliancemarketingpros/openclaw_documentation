---
title: Nix
source_url: https://docs.openclaw.ai/de/install/nix
scraped_at: 2026-05-25
---

Installieren Sie OpenClaw deklarativ mit **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- dem offiziellen, vollständig ausgestatteten Home Manager-Modul.

## Was Sie erhalten

  * Gateway + macOS-App + Tools (whisper, spotify, cameras) -- alles fest gepinnt
  * launchd-Dienst, der Neustarts übersteht
  * Plugin-System mit deklarativer Konfiguration
  * Sofortiges Rollback: `home-manager switch --rollback`


## Schnellstart

* ### Determinate Nix installieren

Wenn Nix noch nicht installiert ist, folgen Sie den Anweisungen des [Determinate Nix-Installers](<https://github.com/DeterminateSystems/nix-installer>).

* ### Lokalen Flake erstellen

Verwenden Sie die agent-first-Vorlage aus dem nix-openclaw-Repo:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### Secrets konfigurieren

Richten Sie Ihr Messaging-Bot-Token und den API-Schlüssel Ihres Modell-Providers ein. Einfache Dateien unter `~/.secrets/` funktionieren gut.

* ### Vorlagen-Platzhalter ausfüllen und wechseln

bashCopy code
[code]
    home-manager switch
[/code]

* ### Überprüfen

Bestätigen Sie, dass der launchd-Dienst läuft und Ihr Bot auf Nachrichten antwortet.

Vollständige Moduloptionen und Beispiele finden Sie in der [nix-openclaw README](<https://github.com/openclaw/nix-openclaw>).

## Laufzeitverhalten im Nix-Modus

Wenn `OPENCLAW_NIX_MODE=1` gesetzt ist (automatisch mit nix-openclaw), wechselt OpenClaw für Nix-verwaltete Installationen in einen deterministischen Modus. Andere Nix-Pakete können denselben Modus setzen; nix-openclaw ist die offizielle Referenz.

Sie können ihn auch manuell setzen:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

Unter macOS erbt die GUI-App Shell-Umgebungsvariablen nicht automatisch. Aktivieren Sie den Nix-Modus stattdessen über defaults:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Was sich im Nix-Modus ändert

  * Abläufe für automatische Installation und Selbständerung sind deaktiviert
  * `openclaw.json` wird als unveränderlich behandelt. Beim Start abgeleitete Standardwerte bleiben nur zur Laufzeit gültig, und Konfigurationsschreiber wie setup, onboarding, verändernde `openclaw update`-Aufrufe, Plugin install/update/uninstall/enable, `doctor --fix`, `doctor --generate-gateway-token` und `openclaw config set` verweigern das Bearbeiten der Datei.
  * Agenten sollten stattdessen die Nix-Quelle bearbeiten. Für nix-openclaw verwenden Sie den agent-first-[Schnellstart](<https://github.com/openclaw/nix-openclaw#quick-start>) und setzen die Konfiguration unter `programs.openclaw.config` oder `instances.<name>.config`.
  * Fehlende Abhängigkeiten zeigen Nix-spezifische Hinweise zur Behebung an
  * Die UI zeigt ein schreibgeschütztes Banner für den Nix-Modus an


### Konfigurations- und Statuspfade

OpenClaw liest die JSON5-Konfiguration aus `OPENCLAW_CONFIG_PATH` und speichert veränderliche Daten in `OPENCLAW_STATE_DIR`. Wenn Sie unter Nix arbeiten, setzen Sie diese Werte explizit auf Nix-verwaltete Speicherorte, damit Laufzeitstatus und Konfiguration außerhalb des unveränderlichen Stores bleiben.

Variable | Standard  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Erkennung des Dienst-PATH

Der launchd/systemd-Gateway-Dienst erkennt Nix-Profil-Binärdateien automatisch, sodass Plugins und Tools, die per Shell auf mit `nix` installierte ausführbare Dateien zugreifen, ohne manuelle PATH-Einrichtung funktionieren:

  * Wenn `NIX_PROFILES` gesetzt ist, wird jeder Eintrag dem Dienst-PATH mit Priorität von rechts nach links hinzugefügt (entspricht der Nix-Shell-Priorität - der rechteste Eintrag gewinnt).
  * Wenn `NIX_PROFILES` nicht gesetzt ist, wird `~/.nix-profile/bin` als Fallback hinzugefügt.


Dies gilt sowohl für macOS-launchd- als auch für Linux-systemd-Dienstumgebungen.

## Verwandt

[**nix-openclaw** Maßgebliches Home Manager-Modul und vollständige Einrichtungsanleitung. ](<https://github.com/openclaw/nix-openclaw>) [**Einrichtungsassistent** Nicht-Nix-CLI-Einrichtungsanleitung. ](</de/start/wizard>) [**Docker** Containerisierte Einrichtung als Nicht-Nix-Alternative. ](</de/install/docker>) [**Aktualisieren** Aktualisieren von Home Manager-verwalteten Installationen zusammen mit dem Paket. ](</de/install/updating>)

Was this useful?YesNo
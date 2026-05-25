---
title: Erste Schritte
source_url: https://docs.openclaw.ai/de/start/getting-started
scraped_at: 2026-05-25
---

OpenClaw installieren, Onboarding ausführen und mit Ihrem KI-Assistenten chatten – alles in etwa 5 Minuten. Am Ende haben Sie einen laufenden Gateway, konfigurierte Authentifizierung und eine funktionierende Chat-Sitzung.

## Was Sie benötigen

  * **Node.js** – Node 24 empfohlen (Node 22.16+ wird ebenfalls unterstützt)
  * **Ein API-Schlüssel** von einem Modell-Provider (Anthropic, OpenAI, Google usw.) – das Onboarding fragt Sie danach


## Schnelle Einrichtung

* ### OpenClaw installieren

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Installationsskript-Prozess](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Der Assistent führt Sie durch die Auswahl eines Modell-Providers, das Festlegen eines API-Schlüssels und die Konfiguration des Gateway. Das dauert etwa 2 Minuten.

Die vollständige Referenz finden Sie unter [Onboarding (CLI)](</de/start/wizard>).

* ### Prüfen, ob der Gateway läuft

bashCopy code
[code]
    openclaw gateway status
[/code]

Sie sollten sehen, dass der Gateway auf Port 18789 lauscht.

* ### Dashboard öffnen

bashCopy code
[code]
    openclaw dashboard
[/code]

Dadurch wird die Control UI in Ihrem Browser geöffnet. Wenn sie geladen wird, funktioniert alles.

* ### Ihre erste Nachricht senden

Geben Sie eine Nachricht im Chat der Control UI ein, und Sie sollten eine KI-Antwort erhalten.

Möchten Sie stattdessen von Ihrem Telefon aus chatten? Der schnellste einzurichtende Kanal ist [Telegram](</de/channels/telegram>) (nur ein Bot-Token). Alle Optionen finden Sie unter [Kanäle](</de/channels>).

Erweitert: benutzerdefinierten Control-UI-Build einbinden

Wenn Sie einen lokalisierten oder angepassten Dashboard-Build pflegen, setzen Sie `gateway.controlUi.root` auf ein Verzeichnis, das Ihre gebauten statischen Assets und `index.html` enthält.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Legen Sie dann fest:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Starten Sie den Gateway neu und öffnen Sie das Dashboard erneut:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Nächste Schritte

[**Kanal verbinden** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo und mehr. ](</de/channels>) [**Kopplung und Sicherheit** Steuern Sie, wer Ihrem Agent Nachrichten senden kann. ](</de/channels/pairing>) [**Gateway konfigurieren** Modelle, Tools, Sandbox und erweiterte Einstellungen. ](</de/gateway/configuration>) [**Tools durchsuchen** Browser, exec, Websuche, Skills und Plugins. ](</de/tools>)

Erweitert: Umgebungsvariablen

Wenn Sie OpenClaw als Dienstkonto ausführen oder benutzerdefinierte Pfade verwenden möchten:

  * `OPENCLAW_HOME` – Home-Verzeichnis für interne Pfadauflösung
  * `OPENCLAW_STATE_DIR` – überschreibt das Zustandsverzeichnis
  * `OPENCLAW_CONFIG_PATH` – überschreibt den Pfad zur Konfigurationsdatei


Vollständige Referenz: [Umgebungsvariablen](</de/help/environment>).

## Verwandt

  * [Installationsübersicht](</de/install>)
  * [Kanalübersicht](</de/channels>)
  * [Einrichtung](</de/start/setup>)


Was this useful?YesNo
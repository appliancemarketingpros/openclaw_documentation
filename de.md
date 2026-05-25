---
title: OpenClaw
source_url: https://docs.openclaw.ai/de
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EXFOLIATE! EXFOLIATE!"_ — vermutlich ein Weltraum-Hummer

**Ein Gateway für jedes Betriebssystem für KI-Agenten über Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo und mehr.**

Senden Sie eine Nachricht und erhalten Sie eine Agentenantwort aus Ihrer Tasche. Betreiben Sie ein Gateway über integrierte Kanäle, gebündelte Kanal-Plugins, WebChat und mobile Nodes hinweg.

[**Erste Schritte** Installieren Sie OpenClaw und starten Sie das Gateway in wenigen Minuten. ](</de/start/getting-started>) [**Onboarding ausführen** Geführte Einrichtung mit `openclaw onboard` und Kopplungsabläufen. ](</de/start/wizard>) [**Steuerungsoberfläche öffnen** Starten Sie das Browser-Dashboard für Chat, Konfiguration und Sitzungen. ](</de/web/control-ui>)

## Was ist OpenClaw?

OpenClaw ist ein **selbst gehostetes Gateway** , das Ihre bevorzugten Chat-Apps und Kanaloberflächen — integrierte Kanäle sowie gebündelte oder externe Kanal-Plugins wie Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo und mehr — mit KI-Coding-Agenten wie Pi verbindet. Sie führen einen einzelnen Gateway-Prozess auf Ihrem eigenen Rechner (oder einem Server) aus, der zur Brücke zwischen Ihren Messaging-Apps und einem stets verfügbaren KI-Assistenten wird.

**Für wen ist es gedacht?** Für Entwickler und erfahrene Nutzer, die einen persönlichen KI-Assistenten möchten, dem sie von überall aus Nachrichten senden können — ohne die Kontrolle über ihre Daten abzugeben oder auf einen gehosteten Dienst angewiesen zu sein.

**Was macht es anders?**

  * **Selbst gehostet** : läuft auf Ihrer Hardware, nach Ihren Regeln
  * **Multi-Channel** : ein Gateway bedient integrierte Kanäle sowie gebündelte oder externe Kanal-Plugins gleichzeitig
  * **Agent-native** : entwickelt für Coding-Agenten mit Tool-Nutzung, Sitzungen, Speicher und Multi-Agent-Routing
  * **Open Source** : MIT-lizenziert, community-getrieben


**Was benötigen Sie?** Node 24 (empfohlen) oder Node 22 LTS (`22.16+`) für Kompatibilität, einen API-Schlüssel von Ihrem gewählten Provider und 5 Minuten. Für beste Qualität und Sicherheit verwenden Sie das stärkste verfügbare Modell der neuesten Generation.

## Funktionsweise
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Das Gateway ist die zentrale Quelle der Wahrheit für Sitzungen, Routing und Kanalverbindungen.

## Wichtige Funktionen

[**Multi-Channel-Gateway** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat und mehr mit einem einzigen Gateway-Prozess. ](</de/channels>) [**Plugin-Kanäle** Gebündelte Plugins fügen Matrix, Nostr, Twitch, Zalo und mehr in normalen aktuellen Releases hinzu. ](</de/tools/plugin>) [**Multi-Agent-Routing** Isolierte Sitzungen pro Agent, Arbeitsbereich oder Absender. ](</de/concepts/multi-agent>) [**Medienunterstützung** Senden und empfangen Sie Bilder, Audio und Dokumente. ](</de/nodes/images>) [**Web-Steuerungsoberfläche** Browser-Dashboard für Chat, Konfiguration, Sitzungen und Nodes. ](</de/web/control-ui>) [**Mobile Nodes** Koppeln Sie iOS- und Android-Nodes für Canvas, Kamera und sprachfähige Workflows. ](</de/nodes>)

## Schnellstart

* ### OpenClaw installieren

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Onboarding durchführen und den Dienst installieren

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chatten

Öffnen Sie die Steuerungsoberfläche in Ihrem Browser und senden Sie eine Nachricht:

bashCopy code
[code]
    openclaw dashboard
[/code]

Oder verbinden Sie einen Kanal ([Telegram](</de/channels/telegram>) ist am schnellsten) und chatten Sie von Ihrem Smartphone aus.

Benötigen Sie die vollständige Installation und Entwicklungsumgebung? Siehe [Erste Schritte](</de/start/getting-started>).

## Dashboard

Öffnen Sie die browserbasierte Steuerungsoberfläche, nachdem das Gateway gestartet wurde.

  * Lokaler Standard: <http://127.0.0.1:18789/>
  * Remote-Zugriff: [Weboberflächen](</de/web>) und [Tailscale](</de/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Konfiguration (optional)

Die Konfiguration befindet sich unter `~/.openclaw/openclaw.json`.

  * Wenn Sie **nichts tun** , verwendet OpenClaw die gebündelte Pi-Binärdatei im RPC-Modus mit Sitzungen pro Absender.
  * Wenn Sie es stärker absichern möchten, beginnen Sie mit `channels.whatsapp.allowFrom` und (für Gruppen) Erwähnungsregeln.


Beispiel:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Hier beginnen

[**Dokumentations-Hubs** Alle Dokumentationen und Anleitungen, nach Anwendungsfall geordnet. ](</de/start/hubs>) [**Konfiguration** Zentrale Gateway-Einstellungen, Tokens und Provider-Konfiguration. ](</de/gateway/configuration>) [**Remote-Zugriff** Zugriffsmuster für SSH und Tailnet. ](</de/gateway/remote>) [**Kanäle** Kanalspezifische Einrichtung für Feishu, Microsoft Teams, WhatsApp, Telegram, Discord und mehr. ](</de/channels/telegram>) [**Nodes** iOS- und Android-Nodes mit Kopplung, Canvas, Kamera und Geräteaktionen. ](</de/nodes>) [**Hilfe** Einstiegspunkt für häufige Korrekturen und Fehlerbehebung. ](</de/help>)

## Mehr erfahren

[**Vollständige Funktionsliste** Vollständige Kanal-, Routing- und Medienfunktionen. ](</de/concepts/features>) [**Multi-Agent-Routing** Arbeitsbereichsisolierung und Sitzungen pro Agent. ](</de/concepts/multi-agent>) [**Sicherheit** Tokens, Allowlists und Sicherheitskontrollen. ](</de/gateway/security>) [**Fehlerbehebung** Gateway-Diagnosen und häufige Fehler. ](</de/gateway/troubleshooting>) [**Über das Projekt und Danksagungen** Projektursprünge, Mitwirkende und Lizenz. ](</de/reference/credits>)

Was this useful?YesNo
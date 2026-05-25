---
title: Hostinger
source_url: https://docs.openclaw.ai/de/install/hostinger
scraped_at: 2026-05-25
---

Ein persistentes OpenClaw Gateway auf [Hostinger](<https://www.hostinger.com/openclaw>) über eine verwaltete **1-Click** -Bereitstellung oder eine **VPS** -Installation ausführen.

## Voraussetzungen

  * Hostinger-Konto ([Registrierung](<https://www.hostinger.com/openclaw>))
  * Etwa 5–10 Minuten


## Option A: 1-Click OpenClaw

Der schnellste Weg für den Einstieg. Hostinger übernimmt Infrastruktur, Docker und automatische Updates.

* ### Kaufen und starten

  1. Wählen Sie auf der [Hostinger-OpenClaw-Seite](<https://www.hostinger.com/openclaw>) einen Managed-OpenClaw-Plan und schließen Sie den Checkout ab.


* ### Einen Messaging-Channel auswählen

Wählen Sie einen oder mehrere Channels, die verbunden werden sollen:

  * **WhatsApp** \-- scannen Sie den im Setup-Assistenten angezeigten QR-Code.
  * **Telegram** \-- fügen Sie den Bot-Token von [BotFather](<https://t.me/BotFather>) ein.


* ### Installation abschließen

Klicken Sie auf **Finish** , um die Instanz bereitzustellen. Sobald sie bereit ist, greifen Sie über **OpenClaw Overview** in hPanel auf das OpenClaw-Dashboard zu.

## Option B: OpenClaw auf VPS

Mehr Kontrolle über Ihren Server. Hostinger stellt OpenClaw über Docker auf Ihrem VPS bereit, und Sie verwalten es über den **Docker Manager** in hPanel.

* ### Einen VPS kaufen

  1. Wählen Sie auf der [Hostinger-OpenClaw-Seite](<https://www.hostinger.com/openclaw>) einen Plan „OpenClaw on VPS“ und schließen Sie den Checkout ab.


* ### OpenClaw konfigurieren

Sobald der VPS bereitgestellt ist, füllen Sie die Konfigurationsfelder aus:

  * **Gateway token** \-- automatisch generiert; speichern Sie es für die spätere Verwendung.
  * **WhatsApp-Nummer** \-- Ihre Nummer mit Landesvorwahl (optional).
  * **Telegram bot token** \-- von [BotFather](<https://t.me/BotFather>) (optional).
  * **API keys** \-- nur erforderlich, wenn Sie beim Checkout keine Credits für Ready-to-Use AI ausgewählt haben.


* ### OpenClaw starten

Klicken Sie auf **Deploy**. Sobald es läuft, öffnen Sie das OpenClaw-Dashboard in hPanel durch Klick auf **Open**.

Logs, Neustarts und Updates werden direkt über die Oberfläche des Docker Manager in hPanel verwaltet. Zum Aktualisieren klicken Sie im Docker Manager auf **Update** ; dadurch wird das neueste Image gezogen.

## Ihr Setup verifizieren

Senden Sie „Hi“ an Ihren Assistant in dem verbundenen Channel. OpenClaw antwortet und führt Sie durch die ersten Einstellungen.

## Fehlerbehebung

**Dashboard lädt nicht** \-- Warten Sie einige Minuten, bis der Container die Bereitstellung abgeschlossen hat. Prüfen Sie die Logs im Docker Manager in hPanel.

**Docker-Container startet ständig neu** \-- Öffnen Sie die Logs im Docker Manager und suchen Sie nach Konfigurationsfehlern (fehlende Tokens, ungültige API keys).

**Telegram-Bot antwortet nicht** \-- Senden Sie Ihre Pairing-Code-Nachricht direkt aus Telegram als Nachricht in Ihren OpenClaw-Chat, um die Verbindung abzuschließen.

## Nächste Schritte

  * [Channels](</de/channels>) \-- Telegram, WhatsApp, Discord und weitere verbinden
  * [Gateway configuration](</de/gateway/configuration>) \-- alle Konfigurationsoptionen


## Verwandt

  * [Install overview](</de/install>)
  * [VPS hosting](</de/vps>)
  * [DigitalOcean](</de/install/digitalocean>)


Was this useful?YesNo
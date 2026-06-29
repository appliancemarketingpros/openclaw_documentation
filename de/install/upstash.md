---
title: Upstash Box
source_url: https://docs.openclaw.ai/de/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Führen Sie einen persistenten OpenClaw Gateway auf Upstash Box aus, einer verwalteten Linux-Umgebung mit Keep-alive-Lifecycle-Unterstützung.

Verwenden Sie einen SSH-Tunnel für den Dashboard-Zugriff. Geben Sie den Gateway-Port nicht direkt für das öffentliche Internet frei.

## Voraussetzungen

  * Upstash-Konto
  * Keep-alive-Upstash-Box
  * SSH-Client auf Ihrem lokalen Computer


## Eine Box erstellen

Erstellen Sie eine Keep-alive-Box in der Upstash Console. Notieren Sie sich die Box-ID, zum Beispiel `right-flamingo-14486`, und Ihren Box-API-Schlüssel.

Upstash pflegt seine aktuelle OpenClaw-Box-Anleitung unter [OpenClaw-Einrichtung](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Mit einem SSH-Tunnel verbinden

Leiten Sie den OpenClaw-Dashboard-Port an Ihren lokalen Computer weiter. Verwenden Sie Ihren Box-API-Schlüssel als SSH-Passwort, wenn Sie dazu aufgefordert werden:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Die Keepalive-Optionen reduzieren Tunnelabbrüche durch Inaktivität während des Onboardings.

## OpenClaw installieren

Innerhalb der Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Folgen Sie den Eingabeaufforderungen. Kopieren Sie die Dashboard-URL und das Token, wenn das Onboarding abgeschlossen ist.

## Gateway starten

Konfigurieren Sie den Gateway für das Box-Netzwerk und starten Sie ihn im Hintergrund:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Öffnen Sie bei aktivem SSH-Tunnel die Dashboard-URL lokal:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Automatischer Neustart

Legen Sie diesen Befehl als Box-Init-Skript fest, damit der Gateway neu startet, wenn die Box startet:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Problembehebung

Wenn SSH während des Onboardings einfriert, verbinden Sie sich erneut mit einer sauberen SSH-Konfiguration und Keepalives:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Dies umgeht veraltete lokale `~/.ssh/config`-Einstellungen und hält den Tunnel während inaktiver Netzwerkphasen aktiv.

## Verwandte Themen

  * [Remote-Zugriff](</de/gateway/remote>)
  * [Gateway-Sicherheit](</de/gateway/security>)
  * [OpenClaw aktualisieren](</de/install/updating>)


Was this useful?YesNo

Open issue
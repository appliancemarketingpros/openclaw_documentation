---
title: Gateway unter macOS
source_url: https://docs.openclaw.ai/de/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app bündelt Node/Bun oder die Gateway-Laufzeit nicht mehr. Die macOS-App erwartet eine **externe** Installation der `openclaw`-CLI, startet das Gateway nicht als Kindprozess und verwaltet einen benutzerspezifischen launchd-Dienst, damit das Gateway läuft (oder verbindet sich mit einem vorhandenen lokalen Gateway, falls bereits eines läuft).

## CLI installieren (für lokalen Modus erforderlich)

Node 24 ist die Standardlaufzeit auf dem Mac. Node 22 LTS, derzeit `22.16+`, funktioniert aus Kompatibilitätsgründen weiterhin. Installieren Sie dann `openclaw` global:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Die Schaltfläche **CLI installieren** der macOS-App führt denselben globalen Installationsablauf aus, den die App intern verwendet: Sie bevorzugt zuerst npm, dann pnpm und dann bun, falls dies der einzige erkannte Paketmanager ist. Node bleibt die empfohlene Gateway-Laufzeit.

## Launchd (Gateway als LaunchAgent)

Label:

  * `ai.openclaw.gateway` (oder `ai.openclaw.<profile>`; veraltetes `com.openclaw.*` kann bestehen bleiben)


Plist-Speicherort (benutzerspezifisch):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (oder `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Manager:

  * Die macOS-App ist im lokalen Modus für Installation/Aktualisierung des LaunchAgent verantwortlich.
  * Die CLI kann ihn ebenfalls installieren: `openclaw gateway install`.


Verhalten:

  * „OpenClaw Active“ aktiviert/deaktiviert den LaunchAgent.
  * Das Beenden der App stoppt das Gateway **nicht** (launchd hält es am Leben).
  * Wenn auf dem konfigurierten Port bereits ein Gateway läuft, verbindet sich die App damit, statt ein neues zu starten.


Protokollierung:

  * launchd stdout/err: `/tmp/openclaw/openclaw-gateway.log`


## Versionskompatibilität

Die macOS-App prüft die Gateway-Version gegen ihre eigene Version. Wenn sie inkompatibel sind, aktualisieren Sie die globale CLI auf die Version der App.

## Smoke-Check

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Dann:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Verwandte Themen

  * [macOS-App](</de/platforms/macos>)
  * [Gateway-Runbook](</de/gateway>)


Was this useful?YesNo
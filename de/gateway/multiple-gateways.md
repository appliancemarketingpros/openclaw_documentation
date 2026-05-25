---
title: Mehrere Gateways
source_url: https://docs.openclaw.ai/de/gateway/multiple-gateways
scraped_at: 2026-05-25
---

Die meisten Setups sollten einen Gateway verwenden, da ein einzelner Gateway mehrere Messaging-Verbindungen und Agents bedienen kann. Wenn Sie stärkere Isolation oder Redundanz benötigen (z. B. einen Rescue-Bot), führen Sie separate Gateways mit isolierten Profilen/Ports aus.

## Am besten empfohlenes Setup

Für die meisten Benutzer ist das einfachste Rescue-Bot-Setup:

  * den Haupt-Bot im Standardprofil belassen
  * den Rescue-Bot mit `--profile rescue` ausführen
  * einen vollständig separaten Telegram-Bot für das Rescue-Konto verwenden
  * den Rescue-Bot auf einem anderen Basis-Port wie `19789` betreiben


Dadurch bleibt der Rescue-Bot vom Haupt-Bot isoliert, sodass er debuggen oder Konfigurationsänderungen anwenden kann, wenn der primäre Bot ausgefallen ist. Lassen Sie mindestens 20 Ports Abstand zwischen Basis-Ports, damit die abgeleiteten Browser-/Canvas-/CDP-Ports niemals kollidieren.

## Rescue-Bot-Schnellstart

Verwenden Sie dies als Standardweg, sofern Sie keinen triftigen Grund haben, etwas anderes zu tun:

bashCopy code
[code]
    # Rescue-Bot (separater Telegram-Bot, separates Profil, Port 19789)openclaw --profile rescue onboardopenclaw --profile rescue gateway install --port 19789
[/code]

Wenn Ihr Haupt-Bot bereits läuft, ist das normalerweise alles, was Sie benötigen.

Während `openclaw --profile rescue onboard`:

  * verwenden Sie das separate Telegram-Bot-Token
  * behalten Sie das Profil `rescue` bei
  * verwenden Sie einen Basis-Port, der mindestens 20 höher ist als der des Haupt-Bots
  * akzeptieren Sie den standardmäßigen Rescue-Arbeitsbereich, sofern Sie nicht bereits selbst einen verwalten


Wenn das Onboarding den Rescue-Dienst bereits für Sie installiert hat, ist das abschließende `gateway install` nicht erforderlich.

## Warum das funktioniert

Der Rescue-Bot bleibt unabhängig, weil er Folgendes jeweils separat hat:

  * Profil/Konfiguration
  * Statusverzeichnis
  * Arbeitsbereich
  * Basis-Port (plus abgeleitete Ports)
  * Telegram-Bot-Token


Für die meisten Setups verwenden Sie einen vollständig separaten Telegram-Bot für das Rescue-Profil:

  * einfach auf Operatoren beschränkbar
  * separates Bot-Token und separate Identität
  * unabhängig von der Channel-/App-Installation des Haupt-Bots
  * einfacher DM-basierter Wiederherstellungsweg, wenn der Haupt-Bot defekt ist


## Was `--profile rescue onboard` ändert

`openclaw --profile rescue onboard` verwendet den normalen Onboarding-Ablauf, schreibt aber alles in ein separates Profil.

In der Praxis bedeutet das, dass der Rescue-Bot Folgendes separat erhält:

  * Konfigurationsdatei
  * Statusverzeichnis
  * Arbeitsbereich (standardmäßig `~/.openclaw/workspace-rescue`)
  * Name des verwalteten Dienstes


Die Eingabeaufforderungen sind ansonsten identisch mit dem normalen Onboarding.

## Allgemeines Multi-Gateway-Setup

Das oben beschriebene Rescue-Bot-Layout ist der einfachste Standard, aber dasselbe Isolationsmuster funktioniert für jedes Paar oder jede Gruppe von Gateways auf einem Host.

Für ein allgemeineres Setup geben Sie jedem zusätzlichen Gateway ein eigenes benanntes Profil und seinen eigenen Basis-Port:

bashCopy code
[code]
    # main (Standardprofil)openclaw setupopenclaw gateway --port 18789 # zusätzlicher Gatewayopenclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Wenn beide Gateways benannte Profile verwenden sollen, funktioniert das ebenfalls:

bashCopy code
[code]
    openclaw --profile main setupopenclaw --profile main gateway --port 18789 openclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Dienste folgen demselben Muster:

bashCopy code
[code]
    openclaw gateway installopenclaw --profile ops gateway install --port 19789
[/code]

Verwenden Sie den Rescue-Bot-Schnellstart, wenn Sie eine Fallback-Operator-Spur benötigen. Verwenden Sie das allgemeine Profilmuster, wenn Sie mehrere langlebige Gateways für verschiedene Channels, Mandanten, Arbeitsbereiche oder Betriebsrollen benötigen.

## Isolations-Checkliste

Halten Sie diese Angaben pro Gateway-Instanz eindeutig:

  * `OPENCLAW_CONFIG_PATH` — Konfigurationsdatei pro Instanz
  * `OPENCLAW_STATE_DIR` — Sitzungen, Zugangsdaten, Caches pro Instanz
  * `agents.defaults.workspace` — Arbeitsbereichsstamm pro Instanz
  * `gateway.port` (oder `--port`) — eindeutig pro Instanz
  * abgeleitete Browser-/Canvas-/CDP-Ports


Wenn diese gemeinsam genutzt werden, treten Konfigurationsrennen und Portkonflikte auf.

## Portzuordnung (abgeleitet)

Basis-Port = `gateway.port` (oder `OPENCLAW_GATEWAY_PORT` / `--port`).

  * Port des Browser-Steuerungsdienstes = Basis + 2 (nur local loopback)
  * Canvas-Host wird auf dem Gateway-HTTP-Server bereitgestellt (derselbe Port wie `gateway.port`)
  * CDP-Ports für Browserprofile werden automatisch aus `browser.controlPort + 9 .. + 108` zugewiesen


Wenn Sie eine dieser Angaben in der Konfiguration oder Umgebung überschreiben, müssen Sie sie pro Instanz eindeutig halten.

## Browser-/CDP-Hinweise (häufige Fehlerquelle)

  * Setzen Sie `browser.cdpUrl` **nicht** auf mehreren Instanzen auf dieselben Werte fest.
  * Jede Instanz benötigt ihren eigenen Browser-Steuerungsport und CDP-Bereich (abgeleitet von ihrem Gateway-Port).
  * Wenn Sie explizite CDP-Ports benötigen, setzen Sie `browser.profiles.<name>.cdpPort` pro Instanz.
  * Remote Chrome: verwenden Sie `browser.profiles.<name>.cdpUrl` (pro Profil, pro Instanz).


## Manuelles Umgebungsbeispiel

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/main.json \OPENCLAW_STATE_DIR=~/.openclaw \openclaw gateway --port 18789 OPENCLAW_CONFIG_PATH=~/.openclaw/rescue.json \OPENCLAW_STATE_DIR=~/.openclaw-rescue \openclaw gateway --port 19789
[/code]

## Schnellprüfungen

bashCopy code
[code]
    openclaw gateway status --deepopenclaw --profile rescue gateway status --deepopenclaw --profile rescue gateway probeopenclaw statusopenclaw --profile rescue statusopenclaw --profile rescue browser status
[/code]

Interpretation:

  * `gateway status --deep` hilft, veraltete launchd-/systemd-/schtasks-Dienste aus älteren Installationen zu erkennen.
  * Warntext von `gateway probe` wie `multiple reachable gateways detected` wird nur erwartet, wenn Sie absichtlich mehr als einen isolierten Gateway ausführen.


## Verwandte Themen

  * [Gateway-Runbook](</de/gateway>)
  * [Gateway-Sperre](</de/gateway/gateway-lock>)
  * [Konfiguration](</de/gateway/configuration>)


Was this useful?YesNo
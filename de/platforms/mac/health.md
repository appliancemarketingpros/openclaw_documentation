---
title: Integritätsprüfungen (macOS)
source_url: https://docs.openclaw.ai/de/platforms/mac/health
scraped_at: 2026-05-25
---

# Integritätsprüfungen unter macOS

So sehen Sie in der Menüleisten-App, ob der verknüpfte Kanal gesund ist.

## Menüleiste

  * Der Statuspunkt spiegelt jetzt die Baileys-Gesundheit wider: 
    * Grün: verknüpft + Socket wurde kürzlich geöffnet.
    * Orange: verbindet sich/versucht erneut.
    * Rot: abgemeldet oder Probe fehlgeschlagen.
  * Die sekundäre Zeile zeigt „linked · auth 12m“ oder den Fehlergrund.
  * Der Menüeintrag „Run Health Check“ löst eine On-Demand-Probe aus.


## Einstellungen

  * Der Reiter Allgemein erhält eine Health-Karte mit: Alter der verknüpften Auth, Pfad/Anzahl des Session-Stores, Zeitpunkt der letzten Prüfung, letzter Fehler/Statuscode sowie Buttons für Run Health Check / Reveal Logs.
  * Verwendet einen gecachten Snapshot, sodass die UI sofort lädt und bei Offline-Betrieb graceful zurückfällt.
  * Der Reiter **Channels** zeigt Kanalstatus + Steuerelemente für WhatsApp/Telegram an (Login-QR, Logout, Probe, letzter Disconnect/Fehler).


## Wie die Probe funktioniert

  * Die App führt etwa alle 60 Sekunden und auf Abruf `openclaw health --json` über `ShellExecutor` aus. Die Probe lädt Zugangsdaten und meldet den Status, ohne Nachrichten zu senden.
  * Cachen Sie den letzten guten Snapshot und den letzten Fehler getrennt, um Flackern zu vermeiden; zeigen Sie den Zeitstempel von beiden an.


## Im Zweifel

  * Sie können weiterhin den CLI-Ablauf unter [Gateway health](</de/gateway/health>) verwenden (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) und `/tmp/openclaw/openclaw-*.log` für `web-heartbeat` / `web-reconnect` tailen.


## Verwandt

  * [Gateway health](</de/gateway/health>)
  * [macOS-App](</de/platforms/macos>)


Was this useful?YesNo
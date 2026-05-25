---
title: Sitzungsverwaltung
source_url: https://docs.openclaw.ai/de/concepts/session
scraped_at: 2026-05-25
---

OpenClaw organisiert Unterhaltungen in **Sessions**. Jede Nachricht wird anhand ihrer Herkunft einer Session zugeordnet -- DMs, Gruppenchats, Cron-Jobs usw.

## Wie Nachrichten geroutet werden

Quelle | Verhalten  
---|---  
Direktnachrichten | Standardmäßig gemeinsame Session  
Gruppenchats | Isoliert pro Gruppe  
Räume/Kanäle | Isoliert pro Raum  
Cron-Jobs | Frische Session pro Lauf  
Webhooks | Isoliert pro Hook  
  
## DM-Isolierung

Standardmäßig teilen sich alle DMs eine Session, um Kontinuität zu gewährleisten. Das ist für Einzelbenutzer-Setups in Ordnung.

**Die Lösung:**

json5Copy code
[code]
    {  session: {    dmScope: "per-channel-peer", // isolate by channel + sender  },}
[/code]

Weitere Optionen:

  * `main` (Standard) -- alle DMs teilen sich eine Session.
  * `per-peer` \-- nach Sender isolieren (über Kanäle hinweg).
  * `per-channel-peer` \-- nach Kanal + Sender isolieren (empfohlen).
  * `per-account-channel-peer` \-- nach Konto + Kanal + Sender isolieren.


### Verknüpfte Kanäle andocken

Dock-Befehle ermöglichen es einem Benutzer, die Antwortroute der aktuellen Direktchat-Session auf einen anderen verknüpften Kanal zu verschieben, ohne eine neue Session zu starten. Siehe [Channel-Docking](</de/concepts/channel-docking>) für Beispiele, Konfiguration und Fehlerbehebung.

Prüfen Sie Ihr Setup mit `openclaw security audit`.

## Session-Lebenszyklus

Sessions werden wiederverwendet, bis sie ablaufen:

  * **Täglicher Reset** (Standard) -- neue Session um 4:00 Uhr Ortszeit auf dem Gateway- Host. Die tägliche Frische basiert darauf, wann die aktuelle `sessionId` gestartet wurde, nicht auf späteren Metadaten-Schreibvorgängen.
  * **Leerlauf-Reset** (optional) -- neue Session nach einer Phase der Inaktivität. Legen Sie `session.reset.idleMinutes` fest. Die Leerlauf-Frische basiert auf der letzten echten Benutzer-/Kanalinteraktion, sodass Heartbeat-, Cron- und Exec-Systemereignisse die Session nicht am Leben halten.
  * **Manueller Reset** \-- geben Sie `/new` oder `/reset` im Chat ein. `/new <model>` wechselt auch das Modell.


Wenn sowohl tägliche als auch Leerlauf-Resets konfiguriert sind, gewinnt derjenige, der zuerst abläuft. Heartbeat-, Cron-, Exec- und andere Systemereignis-Turns können Session-Metadaten schreiben, aber diese Schreibvorgänge verlängern die Frische für tägliche oder Leerlauf-Resets nicht. Wenn ein Reset die Session weiterdreht, werden wartende Systemereignis-Hinweise für die alte Session verworfen, damit veraltete Hintergrundaktualisierungen nicht dem ersten Prompt in der neuen Session vorangestellt werden.

Sessions mit einer aktiven Provider-eigenen CLI-Session werden durch den impliziten täglichen Standard nicht beendet. Verwenden Sie `/reset` oder konfigurieren Sie `session.reset` explizit, wenn diese Sessions nach einem Timer ablaufen sollen.

## Wo der Zustand gespeichert wird

Der gesamte Session-Zustand gehört dem **Gateway**. UI-Clients fragen das Gateway nach Session-Daten ab.

  * **Store:** `~/.openclaw/agents/<agentId>/sessions/sessions.json`
  * **Transkripte:** `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl`


`sessions.json` hält separate Lebenszyklus-Zeitstempel vor:

  * `sessionStartedAt`: wann die aktuelle `sessionId` begonnen hat; der tägliche Reset verwendet diesen Wert.
  * `lastInteractionAt`: letzte Benutzer-/Kanalinteraktion, die die Leerlauf-Lebensdauer verlängert.
  * `updatedAt`: letzte Store-Zeilenmutation; nützlich für Auflistung und Bereinigung, aber nicht maßgeblich für die Frische von täglichen/Leerlauf-Resets.


Ältere Zeilen ohne `sessionStartedAt` werden, sofern verfügbar, aus dem JSONL- Session-Header des Transkripts aufgelöst. Wenn einer älteren Zeile auch `lastInteractionAt` fehlt, fällt die Leerlauf-Frische auf diese Session-Startzeit zurück, nicht auf spätere Buchhaltungs- Schreibvorgänge.

## Session-Wartung

OpenClaw begrenzt den Session-Speicher im Lauf der Zeit automatisch. Standardmäßig läuft es im Modus `warn` (meldet, was bereinigt würde). Setzen Sie `session.maintenance.mode` auf `"enforce"` für automatische Bereinigung:

json5Copy code
[code]
    {  session: {    maintenance: {      mode: "enforce",      pruneAfter: "30d",      maxEntries: 500,    },  },}
[/code]

Für produktionsgroße `maxEntries`-Grenzwerte verwenden Gateway-Laufzeit-Schreibvorgänge einen kleinen High-Water-Puffer und bereinigen in Batches wieder bis zur konfigurierten Obergrenze. Lesevorgänge aus dem Session-Store kürzen oder begrenzen Einträge während des Gateway-Starts nicht. Dadurch wird vermieden, bei jedem Start oder bei jeder isolierten Cron-Session eine vollständige Store-Bereinigung auszuführen. `openclaw sessions cleanup --enforce` wendet die Obergrenze sofort an.

Die Wartung bewahrt dauerhafte externe Unterhaltungszeiger, einschließlich Gruppen- Sessions und thread-bezogener Chat-Sessions, während synthetische Cron-, Hook-, Heartbeat-, ACP- und Sub-Agent-Einträge weiterhin altern und entfernt werden können.

Wenn Sie zuvor Direktnachrichten-Isolierung verwendet und `session.dmScope` später wieder auf `main` gesetzt haben, zeigen Sie veraltete peer-geschlüsselte DM-Zeilen mit `openclaw sessions cleanup --dry-run --fix-dm-scope` in der Vorschau an. Das Anwenden desselben Flags setzt diese alten Direkt-DM-Zeilen außer Betrieb und bewahrt ihre Transkripte als gelöschte Archive auf.

Vorschau mit `openclaw sessions cleanup --dry-run`.

## Sessions prüfen

  * `openclaw status` \-- Pfad zum Session-Store und letzte Aktivität.
  * `openclaw sessions --json` \-- alle Sessions (mit `--active <minutes>` filtern).
  * `/status` im Chat -- Kontextnutzung, Modell und Umschalter.
  * `/context list` \-- was sich im System-Prompt befindet.


## Weiterführende Informationen

  * [Session-Bereinigung](</de/concepts/session-pruning>) \-- Tool-Ergebnisse kürzen
  * [Compaction](</de/concepts/compaction>) \-- lange Unterhaltungen zusammenfassen
  * [Session-Tools](</de/concepts/session-tool>) \-- Agenten-Tools für sitzungsübergreifende Arbeit
  * [Session-Verwaltung im Detail](</de/reference/session-management-compaction>) \-- Store-Schema, Transkripte, Senderichtlinie, Herkunftsmetadaten und erweiterte Konfiguration
  * [Multi-Agent](</de/concepts/multi-agent>) — Routing und Session-Isolierung über Agenten hinweg
  * [Hintergrundaufgaben](</de/automation/tasks>) — wie losgelöste Arbeit Task-Datensätze mit Session-Referenzen erstellt
  * [Channel-Routing](</de/channels/channel-routing>) — wie eingehende Nachrichten zu Sessions geroutet werden


## Verwandt

  * [Session-Bereinigung](</de/concepts/session-pruning>)
  * [Session-Tools](</de/concepts/session-tool>)
  * [Befehlswarteschlange](</de/concepts/queue>)


Was this useful?YesNo
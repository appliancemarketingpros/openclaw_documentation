---
title: Präsenz
source_url: https://docs.openclaw.ai/de/concepts/presence
scraped_at: 2026-05-25
---

OpenClaw „Presence“ ist eine schlanke Best-Effort-Ansicht von:

  * dem **Gateway** selbst und
  * **Clients, die mit dem Gateway verbunden sind** (Mac-App, WebChat, CLI usw.)


Presence wird hauptsächlich verwendet, um den Tab **Instanzen** der macOS-App zu rendern und schnelle operative Sichtbarkeit bereitzustellen.

## Presence-Felder (was angezeigt wird)

Presence-Einträge sind strukturierte Objekte mit Feldern wie:

  * `instanceId` (optional, aber dringend empfohlen): stabile Client-Identität (normalerweise `connect.client.instanceId`)
  * `host`: menschenlesbarer Hostname
  * `ip`: Best-Effort-IP-Adresse
  * `version`: Client-Versionszeichenfolge
  * `deviceFamily` / `modelIdentifier`: Hardware-Hinweise
  * `mode`: `ui`, `webchat`, `cli`, `backend`, `probe`, `test`, `node`, ...
  * `lastInputSeconds`: „Sekunden seit der letzten Benutzereingabe“ (falls bekannt)
  * `reason`: `self`, `connect`, `node-connected`, `periodic`, ...
  * `ts`: Zeitstempel der letzten Aktualisierung (ms seit der Epoche)


## Produzenten (woher Presence stammt)

Presence-Einträge werden von mehreren Quellen erzeugt und **zusammengeführt**.

### 1) Self-Eintrag des Gateway

Das Gateway legt beim Start immer einen „Self“-Eintrag an, damit UIs den Gateway-Host anzeigen, noch bevor sich Clients verbinden.

### 2) WebSocket-Verbindung

Jeder WS-Client beginnt mit einer `connect`-Anfrage. Nach erfolgreichem Handshake legt das Gateway einen Presence-Eintrag für diese Verbindung an oder aktualisiert ihn.

#### Warum einmalige CLI-Befehle nicht angezeigt werden

Die CLI verbindet sich oft für kurze, einmalige Befehle. Um die Instanzenliste nicht zu überfluten, wird `client.mode === "cli"` **nicht** in einen Presence-Eintrag umgewandelt.

### 3) `system-event`-Beacons

Clients können über die Methode `system-event` umfangreichere periodische Beacons senden. Die Mac-App verwendet dies, um Hostname, IP und `lastInputSeconds` zu melden.

### 4) Node-Verbindungen (Rolle: node)

Wenn sich ein Node über das Gateway-WebSocket mit `role: node` verbindet, legt das Gateway einen Presence-Eintrag für diesen Node an oder aktualisiert ihn (derselbe Ablauf wie bei anderen WS-Clients).

## Regeln zum Zusammenführen und Deduplizieren (warum `instanceId` wichtig ist)

Presence-Einträge werden in einer einzelnen In-Memory-Map gespeichert:

  * Einträge werden über einen **Presence-Schlüssel** indiziert.
  * Der beste Schlüssel ist eine stabile `instanceId` (aus `connect.client.instanceId`), die Neustarts überdauert.
  * Schlüssel sind nicht groß-/kleinschreibungssensitiv.


Wenn sich ein Client ohne stabile `instanceId` erneut verbindet, kann er als **doppelte** Zeile erscheinen.

## TTL und begrenzte Größe

Presence ist absichtlich flüchtig:

  * **TTL:** Einträge, die älter als 5 Minuten sind, werden entfernt
  * **Maximale Einträge:** 200 (älteste werden zuerst verworfen)


Dadurch bleibt die Liste aktuell und unbegrenztes Speicherwachstum wird vermieden.

## Hinweis zu Remote/Tunnel (Loopback-IPs)

Wenn sich ein Client über einen SSH-Tunnel / eine lokale Portweiterleitung verbindet, sieht das Gateway die Remote-Adresse möglicherweise als `127.0.0.1`. Um zu vermeiden, dass eine gute vom Client gemeldete IP überschrieben wird, werden Loopback-Remote-Adressen ignoriert.

## Konsumenten

### macOS-Tab „Instanzen“

Die macOS-App rendert die Ausgabe von `system-presence` und wendet eine kleine Statusanzeige (Aktiv/Inaktiv/Veraltet) basierend auf dem Alter der letzten Aktualisierung an.

## Debugging-Tipps

  * Um die Rohdatenliste zu sehen, rufen Sie `system-presence` gegen das Gateway auf.
  * Wenn Sie Duplikate sehen: 
    * bestätigen Sie, dass Clients beim Handshake eine stabile `client.instanceId` senden
    * bestätigen Sie, dass periodische Beacons dieselbe `instanceId` verwenden
    * prüfen Sie, ob dem aus der Verbindung abgeleiteten Eintrag `instanceId` fehlt (Duplikate sind dann erwartet)


## Verwandte Themen

[**Eingabeindikatoren** Wann Eingabeindikatoren gesendet werden und wie Sie sie abstimmen. ](</de/concepts/typing-indicators>) [**Streaming und Chunking** Ausgehendes Streaming, Chunking und kanalspezifische Formatierung. ](</de/concepts/streaming>) [**Gateway-Architektur** Gateway-Komponenten und das WebSocket-Protokoll, das Presence-Aktualisierungen steuert. ](</de/concepts/architecture>) [**Gateway-Protokoll** Das Wire-Protokoll für `connect`, `system-event` und `system-presence`. ](</de/gateway/protocol>)

Was this useful?YesNo
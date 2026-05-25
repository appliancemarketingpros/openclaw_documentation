---
title: Schreibindikatoren
source_url: https://docs.openclaw.ai/de/concepts/typing-indicators
scraped_at: 2026-05-25
---

Tippindikatoren werden an den Chat-Kanal gesendet, während ein Lauf aktiv ist. Verwenden Sie `agents.defaults.typingMode`, um zu steuern, **wann** Tippen beginnt, und `typingIntervalSeconds`, um zu steuern, **wie oft** es aktualisiert wird.

## Standardwerte

Wenn `agents.defaults.typingMode` **nicht gesetzt** ist, behält OpenClaw das bisherige Verhalten bei:

  * **Direktchats** : Tippen beginnt sofort, sobald die Modellschleife startet.
  * **Gruppenchats mit Erwähnung** : Tippen beginnt sofort.
  * **Gruppenchats ohne Erwähnung** : Tippen beginnt erst, wenn Nachrichtentext zu streamen beginnt.
  * **Heartbeat-Läufe** : Tippen beginnt, wenn der Heartbeat-Lauf startet, sofern das aufgelöste Heartbeat-Ziel ein tippfähiger Chat ist und Tippen nicht deaktiviert ist.


## Modi

Setzen Sie `agents.defaults.typingMode` auf einen der folgenden Werte:

  * `never` \- niemals ein Tippindikator.
  * `instant` \- Tippen beginnt **sobald die Modellschleife startet** , auch wenn der Lauf später nur das Token für stille Antworten zurückgibt.
  * `thinking` \- Tippen beginnt beim **ersten Reasoning-Delta** (erfordert `reasoningLevel: "stream"` für den Lauf).
  * `message` \- Tippen beginnt beim **ersten nicht stillen Text-Delta** (ignoriert das stille Token `NO_REPLY`).


Reihenfolge nach „wie früh es ausgelöst wird“: `never` → `message` → `thinking` → `instant`

## Konfiguration

Legen Sie den Standardwert auf Agent-Ebene fest:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Überschreiben Sie Modus oder Takt pro Sitzung:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Hinweise

  * Der Modus `message` zeigt kein Tippen für ausschließlich stille Antworten an, wenn die gesamte Nutzlast exakt dem stillen Token entspricht (zum Beispiel `NO_REPLY` / `no_reply`, ohne Beachtung der Groß-/Kleinschreibung abgeglichen).
  * `thinking` wird nur ausgelöst, wenn der Lauf Reasoning streamt (`reasoningLevel: "stream"`). Wenn das Modell keine Reasoning-Deltas ausgibt, beginnt Tippen nicht.
  * Heartbeat-Tippen ist ein Liveness-Signal für das aufgelöste Zustellziel. Es beginnt beim Start des Heartbeat-Laufs, statt dem Stream-Timing von `message` oder `thinking` zu folgen. Setzen Sie `typingMode: "never"`, um es zu deaktivieren.
  * Heartbeats zeigen kein Tippen an, wenn `target: "none"` gesetzt ist, wenn das Ziel nicht aufgelöst werden kann, wenn die Chat-Zustellung für den Heartbeat deaktiviert ist oder wenn der Kanal Tippen nicht unterstützt.
  * `typingIntervalSeconds` steuert den **Aktualisierungstakt** , nicht die Startzeit. Der Standardwert beträgt 6 Sekunden.


## Verwandte Themen

[**Präsenz** Wie der Gateway verbundene Clients verfolgt und sie im Tab „Instanzen“ von macOS sichtbar macht. ](</de/concepts/presence>) [**Streaming und Chunking** Verhalten beim ausgehenden Streaming, Chunk-Grenzen und kanalspezifische Zustellung. ](</de/concepts/streaming>)

Was this useful?YesNo
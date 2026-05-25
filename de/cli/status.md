---
title: openclaw status
source_url: https://docs.openclaw.ai/de/cli/status
scraped_at: 2026-05-25
---

Diagnose für Kanäle + Sitzungen.

bashCopy code
[code]
    openclaw statusopenclaw status --allopenclaw status --deepopenclaw status --usage
[/code]

Hinweise:

  * `--deep` führt Live-Prüfungen aus (WhatsApp Web + Telegram + Discord + Slack + Signal).
  * Einfaches `openclaw status` bleibt auf dem schnellen schreibgeschützten Pfad und markiert Speicher als `not checked` statt als nicht verfügbar, wenn die Speicherprüfung übersprungen wird. Umfangreiche Sicherheitsprüfung, Plugin-Kompatibilität und Speicher-Vektor-Prüfungen bleiben `openclaw status --all`, `openclaw status --deep`, `openclaw security audit` und `openclaw memory status --deep` vorbehalten.
  * `status --json --all` meldet Speicherdetails aus der aktiven Speicher-Plugin-Laufzeit, die durch `plugins.slots.memory` ausgewählt wurde. Benutzerdefinierte Speicher-Plugins können das integrierte `agents.defaults.memorySearch.enabled` deaktiviert lassen und trotzdem ihren eigenen Datei-, Chunk-, Vektor- und FTS-Status melden.
  * `--usage` gibt normalisierte Provider-Nutzungsfenster als `X% left` aus.
  * Die Sitzungsstatusausgabe trennt `Execution:` von `Runtime:`. `Execution` ist der Sandbox-Pfad (`direct`, `docker/*`), während `Runtime` angibt, ob die Sitzung `OpenClaw Pi Default`, `OpenAI Codex`, ein CLI-Backend oder ein ACP-Backend wie `codex (acp/acpx)` verwendet. Siehe [Agent-Laufzeiten](</de/concepts/agent-runtimes>) für die Unterscheidung zwischen Provider, Modell und Laufzeit.
  * Die rohen Felder `usage_percent` / `usagePercent` von MiniMax geben das verbleibende Kontingent an, daher invertiert OpenClaw sie vor der Anzeige; zählungsbasierte Felder haben Vorrang, wenn sie vorhanden sind. `model_remains`-Antworten bevorzugen den Chat-Modell-Eintrag, leiten die Fensterbezeichnung bei Bedarf aus Zeitstempeln ab und enthalten den Modellnamen in der Planbezeichnung.
  * Wenn der aktuelle Sitzungssnapshot spärlich ist, kann `/status` Token- und Cache-Zähler aus dem neuesten Transkript-Nutzungsprotokoll ergänzen. Vorhandene Live-Werte ungleich null haben weiterhin Vorrang vor Transkript-Fallback-Werten.
  * `/status` enthält eine kompakte Gateway-Prozesslaufzeit und Host-Systemlaufzeit.
  * Der Transkript-Fallback kann auch die aktive Laufzeit-Modellbezeichnung wiederherstellen, wenn sie im Live-Sitzungseintrag fehlt. Wenn dieses Transkriptmodell vom ausgewählten Modell abweicht, löst status das Kontextfenster anhand des wiederhergestellten Laufzeitmodells statt des ausgewählten Modells auf.
  * Für die Prompt-Größenabrechnung bevorzugt der Transkript-Fallback die größere prompt-orientierte Summe, wenn Sitzungsmetadaten fehlen oder kleiner sind, damit Sitzungen mit benutzerdefinierten Providern nicht auf Token-Anzeigen von `0` zurückfallen.
  * Die Ausgabe enthält sitzungsspezifische Speicher pro Agent, wenn mehrere Agenten konfiguriert sind.
  * Die Übersicht enthält den Installations- und Laufzeitstatus des Gateway- und Node-Hostdienstes, sofern verfügbar.
  * Die Übersicht enthält den Update-Kanal + Git-SHA (für Quellcode-Checkouts).
  * Update-Informationen werden in der Übersicht angezeigt; wenn ein Update verfügbar ist, gibt status einen Hinweis aus, `openclaw update` auszuführen (siehe [Aktualisieren](</de/install/updating>)).
  * Fehler beim Aktualisieren der Modellpreise werden als optionale Preiswarnungen angezeigt. Sie bedeuten nicht, dass der Gateway oder die Kanäle fehlerhaft sind.
  * Schreibgeschützte Statusoberflächen (`status`, `status --json`, `status --all`) lösen unterstützte SecretRefs für ihre Zielkonfigurationspfade auf, wenn möglich.
  * Wenn ein unterstützter Kanal-SecretRef konfiguriert, aber im aktuellen Befehlspfad nicht verfügbar ist, bleibt status schreibgeschützt und meldet herabgestufte Ausgabe, statt abzustürzen. Die menschenlesbare Ausgabe zeigt Warnungen wie „konfiguriertes Token in diesem Befehlspfad nicht verfügbar“, und die JSON-Ausgabe enthält `secretDiagnostics`.
  * Wenn die befehlslokale SecretRef-Auflösung erfolgreich ist, bevorzugt status den aufgelösten Snapshot und entfernt vorübergehende Kanalmarker für „Secret nicht verfügbar“ aus der endgültigen Ausgabe.
  * `status --all` enthält eine Secrets-Übersichtszeile und einen Diagnoseabschnitt, der Secret-Diagnosen zusammenfasst (zur besseren Lesbarkeit gekürzt), ohne die Berichtserstellung zu stoppen.


## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Diagnose](</de/gateway/doctor>)


Was this useful?YesNo
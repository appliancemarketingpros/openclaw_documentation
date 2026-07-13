---
title: Aktive Computerpräsenz
source_url: https://docs.openclaw.ai/de/nodes/presence
scraped_at: 2026-07-13
---

Gateway & OpsNodes and media

Die aktive Computerpräsenz teilt dem Gateway mit, welche verbundene macOS-Node zuletzt eine physische Maus- oder Tastatureingabe empfangen hat. OpenClaw verwendet dieses Signal, um einen Mac als `active` zu markieren, dem Agenten einen stabilen Hinweis auf die aktive Node zu geben und Node-Verbindungsbenachrichtigungen an den Computer weiterzuleiten, an dem Sie sich höchstwahrscheinlich befinden.

Dies unterscheidet sich von der [Systempräsenz](</de/concepts/presence>), also der Live-Übersicht der Gateway-Clients, sowie von dauerhaften `node.presence.alive`-Signalen, die erfassen, wann eine mobile Node zuletzt aktiviert wurde, ohne sie als verbunden zu behandeln.

## Voraussetzungen

  * Die OpenClaw-macOS-App ist gekoppelt und im Node-Modus verbunden.
  * Der signierten OpenClaw-App wurde die Berechtigung **Accessibility** erteilt.
  * Für Verbindungsbenachrichtigungen wurde außerdem die Berechtigung **Notifications** erteilt und die Mac-Node stellt `system.notify` bereit.


Die Aktivitätsmeldung ist derzeit durch die native macOS-Node implementiert. iOS-, Android- und watchOS-Nodes sowie headless Node-Hosts können den Verbindungsstatus oder den Zeitpunkt der letzten Hintergrundaktivität melden, werden jedoch bei der Bestimmung des aktiven Computers nicht berücksichtigt.

## Aktiven Computer überprüfen

  1. Öffnen Sie in der macOS-App **Settings - > Permissions** und erteilen Sie **Accessibility** in den macOS-Systemeinstellungen.

  2. Vergewissern Sie sich, dass die Mac-Node verbunden ist:

bashCopy code
[code]openclaw nodes status --connected
[/code]

  3. Bewegen Sie die Maus oder drücken Sie auf diesem Mac eine Taste und führen Sie anschließend Folgendes aus:

bashCopy code
[code]openclaw nodes statusopenclaw nodes describe --node <node-id-or-name>
[/code]


Der zuletzt aktive geeignete Mac wird als `active` markiert. Die Statusausgabe zeigt das Alter seiner letzten Eingabe; `describe` stellt `active`, `lastActiveAtMs` und `presenceUpdatedAtMs` bereit. Aktivitäten werden bewusst zusammengefasst, sodass es nach einer kürzlich erfolgten Meldung bis zu etwa 15 Sekunden dauern kann, bis eine weitere Eingabe angezeigt wird.

## Wie Aktivität zu Präsenz wird

Der macOS-Reporter liest alle zwei Sekunden die Leerlaufzeit der HID-Systemuhr aus. Er meldet einmal, wenn eine Node-Verbindung bereit ist, und danach neuere physische Aktivitäten höchstens einmal alle 15 Sekunden. Im Leerlauf sendet er alle drei Minuten ein Keepalive-Signal. Die Leerlaufdauer ist auf 30 Tage begrenzt, damit eine sehr alte Messung nicht nach vorne verschoben und fälschlicherweise zum neuesten Computer werden kann.

Das Gateway akzeptiert Aktivitäten nur, wenn alle folgenden Bedingungen erfüllt sind:

  * Das Ereignis gehört zur aktuellen authentifizierten Verbindung dieser Node-ID.
  * Die Node verfügt effektiv über die Berechtigung `accessibility: true`.
  * Die Nutzlast enthält einen begrenzten ganzzahligen Wert für `idleSeconds`.


Das Gateway zieht `idleSeconds` von seinem eigenen Beobachtungszeitpunkt ab, um `lastActiveAtMs` zu bestimmen. Es vertraut niemals einem von einer Node bereitgestellten Zeitstempel der Systemuhr. Unter den verbundenen geeigneten Macs gewinnt der neueste Wert für `lastActiveAtMs`; bei Gleichstand wird die aktuellste Präsenzaktualisierung verwendet.

Die Präsenz ist prozesslokal und an die Verbindung gebunden. Wenn die aktuelle Sitzung getrennt, durch eine andere Sitzung mit derselben Node-ID ersetzt oder die Berechtigung Accessibility widerrufen wird, löscht OpenClaw den Aktivitätsstatus dieser Node und bestimmt den aktiven Mac neu.

## Datenschutz und Modellkontext

OpenClaw sendet die Leerlaufdauer, nicht den Inhalt der Eingaben. Es sendet weder Tastenwerte, Mauskoordinaten, Anwendungsnamen, Fenstertitel noch rohe Eingabeereignisse. Der macOS-Reporter liest den HID-Hardwarezustand aus, sodass synthetische Ereignisse zur Computersteuerung einen automatisierten Mac nicht als den Computer erscheinen lassen, den Sie physisch verwendet haben.

Kontinuierliche Aktivität erzeugt keine für das Modell sichtbaren Systemereignisse. Die dynamische Laufzeitzeile enthält ausschließlich die authentifizierte Node-ID:

textCopy code
[code]
    active_node=<node-id>
[/code]

Genaue Zeitstempel und von Nodes kontrollierte Anzeigenamen werden nicht in den Prompt aufgenommen, um Prompt-Injection und Cache-Fluktuationen zu vermeiden. Wenn der Agent aktuelle Details benötigt, kann das Werkzeug `nodes` stattdessen `node.list` oder `node.describe` lesen.

## Weiterleitung von Verbindungsbenachrichtigungen

Nachdem eine Node ihren Gateway-Handshake abgeschlossen hat, wartet OpenClaw 750 Millisekunden, damit der sich verbindende Mac seine erste Aktivitätsmessung übermitteln kann. Anschließend versucht OpenClaw die Zustellung an den verbundenen, benachrichtigungsfähigen Mac mit der aktuellsten Aktivität.

  * Wenn die primäre Zustellung erfolgreich ist, erhält kein anderer Mac die Benachrichtigung.
  * Wenn kein aktiver Mac verfügbar ist oder die primäre Zustellung fehlschlägt, wartet OpenClaw fünf Sekunden und versucht es bei allen übrigen verbundenen Macs, die `system.notify` bereitstellen.
  * Eine Benachrichtigung über die erneute Verbindung derselben Node wird nach einem tatsächlichen Zustellversuch fünf Minuten lang unterdrückt. Dadurch wird verhindert, dass instabile Verbindungen eine Benachrichtigungsflut verursachen.


Benachrichtigungen sind an konkrete Node-Verbindungen gebunden. Eine getrennte oder ersetzte Quellsitzung kann eine alte geplante Benachrichtigung nicht abschließen, während eine als Ziel dienende Ersatzverbindung weiterhin an der Fallback-Zustellung teilnehmen kann.

## Fehlerbehebung

Symptom | Überprüfung  
---|---  
Keine Zeile ist als `active` markiert | Vergewissern Sie sich, dass eine native macOS-Node verbunden ist und `openclaw nodes describe --node <id>` den Wert `permissions.accessibility: true` anzeigt.  
Der falsche Mac bleibt aktiv | Verwenden Sie diesen Mac physisch, warten Sie das Zusammenfassungszeitfenster ab und führen Sie dann `openclaw nodes status` erneut aus. Synthetische Aktionen zur Computersteuerung werden nicht berücksichtigt.  
Daten zur letzten Eingabe verschwinden | Prüfen Sie, ob der Mac getrennt, seine Node-Sitzung ersetzt oder Accessibility widerrufen wurde. Jede dieser Bedingungen löscht die Aktivität absichtlich.  
Die Benachrichtigung erscheint auf mehreren Macs | Die primäre Zustellung war nicht verfügbar oder ist fehlgeschlagen, sodass der verzögerte Fallback ausgeführt wurde. Prüfen Sie, ob der aktive Mac verbunden ist, Benachrichtigungen zulässt und `system.notify` bereitstellt.  
Der Agent erwähnt den aktiven Mac nicht | Beginnen Sie nach Aktivitätsänderungen eine neue Interaktion. Der Laufzeithinweis ist stabil und kompakt; verwenden Sie das Werkzeug `nodes`, um die genauen aktuellen Metadaten abzurufen.  
  
Informationen zur TCC-Wiederherstellung finden Sie unter [macOS-Berechtigungen](</de/platforms/mac/permissions>). Informationen zu Node-Verbindungs- und Befehlsfehlern finden Sie unter [Node-Fehlerbehebung](</de/nodes/troubleshooting>).

## Verwandte Themen

  * [Nodes](</de/nodes>)
  * [Nodes-CLI](</de/cli/nodes>)
  * [Systempräsenz](</de/concepts/presence>)
  * [Gateway-Protokoll](</de/gateway/protocol#presence>)
  * [macOS-App](</de/platforms/macos>)


Was this useful?YesNo

Open issue
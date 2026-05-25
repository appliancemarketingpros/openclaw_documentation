---
title: Steuern
source_url: https://docs.openclaw.ai/de/tools/steer
scraped_at: 2026-05-25
---

`/steer` sendet Hinweise an eine bereits aktive Ausführung. Es ist für Momente gedacht, in denen Sie „diese Ausführung anpassen möchten, während sie noch arbeitet“, nicht zum Starten einer neuen Dialogrunde.

## Aktuelle Sitzung

Verwenden Sie `/steer` auf oberster Ebene, um die aktive Ausführung der aktuellen Sitzung anzusprechen:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Verhalten:

  * Zielt nur auf die aktive Ausführung der aktuellen Sitzung.
  * Funktioniert unabhängig vom `/queue`-Modus der Sitzung.
  * Startet keine neue Ausführung, wenn die Sitzung inaktiv ist.
  * Antwortet mit einer Warnung, wenn es keine aktive Ausführung gibt, die gesteuert werden kann.
  * Verwendet den Steuerungspfad der aktiven Laufzeit, sodass das Modell die Hinweise an der nächsten unterstützten Laufzeitgrenze sieht.


## Steuern im Vergleich zur Queue

`/queue steer` ändert, wie sich normale eingehende Nachrichten verhalten, wenn sie eintreffen, während eine Ausführung aktiv ist. `/steer <message>` ist ein expliziter Befehl, der versucht, die Nachricht dieses Befehls an der nächsten unterstützten Laufzeitgrenze in die aktive Ausführung einzuspeisen, unabhängig von der gespeicherten `/queue`-Einstellung.

Verwenden Sie:

  * `/steer <message>`, wenn Sie die aktive Ausführung jetzt steuern möchten.
  * `/queue steer`, wenn zukünftige normale Nachrichten aktive Ausführungen standardmäßig steuern sollen.
  * `/queue collect` oder `/queue followup`, wenn neue Nachrichten auf eine spätere Dialogrunde warten sollen, statt die aktive Ausführung zu steuern.


Queue-Modi und Fallback-Verhalten finden Sie unter [Befehls-Queue](</de/concepts/queue>) und [Steuerungs-Queue](</de/concepts/queue-steering>).

## Sub-Agenten

Verwenden Sie `/subagents steer`, wenn das Ziel eine untergeordnete Ausführung ist:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` auf oberster Ebene wählt keinen Sub-Agenten nach ID oder Listenindex aus. Es zielt immer auf die aktive Ausführung der aktuellen Sitzung. Unter [Sub-Agenten](</de/tools/subagents>) finden Sie IDs, Labels und Steuerbefehle für Sub-Agenten.

## ACP-Sitzungen

Verwenden Sie `/acp steer`, wenn das Ziel eine ACP-Harness-Sitzung ist:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Unter [ACP-Agenten](</de/tools/acp-agents>) finden Sie Informationen zur Auswahl von ACP-Sitzungen und zum Laufzeitverhalten.

## Verwandt

  * [Slash-Befehle](</de/tools/slash-commands>)
  * [Befehls-Queue](</de/concepts/queue>)
  * [Steuerungs-Queue](</de/concepts/queue-steering>)
  * [Sub-Agenten](</de/tools/subagents>)


Was this useful?YesNo
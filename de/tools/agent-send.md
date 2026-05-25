---
title: Agent senden
source_url: https://docs.openclaw.ai/de/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` führt einen einzelnen Agent-Turn über die Befehlszeile aus, ohne dass eine eingehende Chatnachricht erforderlich ist. Verwenden Sie es für skriptgesteuerte Workflows, Tests und programmatische Auslieferung.

## Schnellstart

* ### Einen einfachen Agent-Turn ausführen

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Dies sendet die Nachricht über den Gateway und gibt die Antwort aus.

* ### Einen bestimmten Agent oder eine bestimmte Sitzung ansteuern

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Die Antwort an einen Kanal zustellen

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Flags

Flag | Beschreibung  
---|---  
`--message \<text\>` | Zu sendende Nachricht (erforderlich)  
`--to \<dest\>` | Sitzungsschlüssel aus einem Ziel ableiten (Telefon, Chat-ID)  
`--agent \<id\>` | Einen konfigurierten Agent ansteuern (verwendet dessen `main`-Sitzung)  
`--session-id \<id\>` | Eine vorhandene Sitzung nach ID wiederverwenden  
`--local` | Lokale eingebettete Runtime erzwingen (Gateway überspringen)  
`--deliver` | Die Antwort an einen Chatkanal senden  
`--channel \<name\>` | Zustellungskanal (whatsapp, telegram, discord, slack usw.)  
`--reply-to \<target\>` | Überschreibung des Zustellungsziels  
`--reply-channel \<name\>` | Überschreibung des Zustellungskanals  
`--reply-account \<id\>` | Überschreibung der Zustellungskonto-ID  
`--thinking \<level\>` | Thinking-Level für das ausgewählte Modellprofil festlegen  
`--verbose \<on|full|off\>` | Verbose-Level festlegen  
`--timeout \<seconds\>` | Agent-Timeout überschreiben  
`--json` | Strukturiertes JSON ausgeben  
  
## Verhalten

  * Standardmäßig läuft die CLI **über den Gateway**. Fügen Sie `--local` hinzu, um die eingebettete Runtime auf dem aktuellen Computer zu erzwingen.
  * Wenn der Gateway nicht erreichbar ist, **fällt die CLI** auf die lokale eingebettete Ausführung zurück.
  * Sitzungsauswahl: `--to` leitet den Sitzungsschlüssel ab (Gruppen-/Kanalziele behalten die Isolation bei; direkte Chats fallen auf `main` zusammen).
  * Thinking- und Verbose-Flags bleiben im Sitzungsspeicher erhalten.
  * Ausgabe: standardmäßig Klartext oder `--json` für strukturierte Nutzdaten + Metadaten.
  * Mit `--json --deliver` enthält das JSON den Zustellungsstatus für gesendete, unterdrückte, teilweise und fehlgeschlagene Sendungen. Siehe [JSON-Zustellungsstatus](</de/cli/agent#json-delivery-status>).


## Beispiele

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Verwandte Themen

[**Agent-CLI-Referenz** Vollständige Referenz zu Flags und Optionen für `openclaw agent`. ](</de/cli/agent>) [**Sub-Agents** Starten von Sub-Agents im Hintergrund. ](</de/tools/subagents>) [**Sitzungen** Wie Sitzungsschlüssel funktionieren und wie `--to`, `--agent` und `--session-id` sie auflösen. ](</de/concepts/session>) [**Slash-Befehle** Nativer Befehlskatalog, der innerhalb von Agent-Sitzungen verwendet wird. ](</de/tools/slash-commands>)

Was this useful?YesNo
---
title: Entfernung von BlueBubbles und der imsg-iMessage-Pfad
source_url: https://docs.openclaw.ai/de/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Entfernen von BlueBubbles und der imsg-iMessage-Pfad

OpenClaw liefert den BlueBubbles-Kanal nicht mehr aus. iMessage-Unterstützung läuft jetzt über das gebündelte `imessage`-Plugin, das [`imsg`](<https://github.com/steipete/imsg>) lokal oder über einen SSH-Wrapper startet und JSON-RPC über stdin/stdout spricht.

Wenn Ihre Konfiguration noch `channels.bluebubbles` enthält, migrieren Sie sie zu `channels.imessage`. Die alte Dokumentations-URL `/channels/bluebubbles` leitet zu [Von BlueBubbles kommend](</de/channels/imessage-from-bluebubbles>) weiter. Dort finden Sie die vollständige Tabelle zur Konfigurationsübersetzung und die Cutover-Checkliste.

## Was sich geändert hat

  * Im unterstützten OpenClaw-iMessage-Pfad gibt es keinen BlueBubbles-HTTP-Server, keine Webhook-Route, kein REST-Passwort und keine BlueBubbles-Plugin-Runtime.
  * OpenClaw liest und überwacht Nachrichten über `imsg` auf dem Mac, auf dem Messages.app angemeldet ist.
  * Grundlegendes Senden, Empfangen, Verlauf und Medien verwenden die normalen `imsg`-Oberflächen und macOS-Berechtigungen.
  * Erweiterte Aktionen wie Thread-Antworten, Tapbacks, Bearbeiten, Zurückziehen von Nachrichten, Effekte, Lesebestätigungen, Tippindikatoren und Gruppenverwaltung erfordern `imsg launch` mit verfügbarer Private-API-Bridge.
  * Linux- und Windows-Gateways können iMessage weiterhin verwenden, indem `channels.imessage.cliPath` auf einen SSH-Wrapper gesetzt wird, der `imsg` auf dem angemeldeten Mac ausführt.


## Was zu tun ist

  1. Installieren und verifizieren Sie `imsg` auf dem Messages-Mac:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Erteilen Sie dem Prozesskontext, der `imsg` und OpenClaw ausführt, Full-Disk-Access- und Automationsberechtigungen.

  3. Übersetzen Sie die alte Konfiguration:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Starten Sie das Gateway neu und verifizieren Sie es:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Testen Sie DMs, Gruppen, Anhänge und alle Private-API-Aktionen, von denen Sie abhängig sind, bevor Sie Ihren alten BlueBubbles-Server löschen.


## Migrationshinweise

  * `channels.bluebubbles.serverUrl` und `channels.bluebubbles.password` haben kein iMessage-Äquivalent.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, Attachment-Roots, Mediengrößenlimits, Chunking und Aktionsumschalter haben iMessage-Äquivalente.
  * `channels.imessage.includeAttachments` ist weiterhin standardmäßig deaktiviert. Setzen Sie es explizit, wenn Sie erwarten, dass eingehende Fotos, Sprachmemos, Videos oder Dateien den Agenten erreichen.
  * Mit `groupPolicy: "allowlist"` kopieren Sie den alten `groups`-Block, einschließlich eines etwaigen `"*"`-Wildcard-Eintrags. Absender-Allowlists für Gruppen und die Gruppenregistrierung sind getrennte Gates.
  * ACP-Bindungen, die `channel: "bluebubbles"` entsprachen, müssen zu `channel: "imessage"` geändert werden.
  * Alte BlueBubbles-Sitzungsschlüssel werden nicht zu iMessage-Sitzungsschlüsseln. Pairing-Freigaben werden nach Handle übernommen, aber der Konversationsverlauf unter BlueBubbles-Sitzungsschlüsseln nicht.


## Siehe auch

  * [Von BlueBubbles kommend](</de/channels/imessage-from-bluebubbles>)
  * [iMessage](</de/channels/imessage>)
  * [Konfigurationsreferenz - iMessage](</de/gateway/config-channels#imessage>)


Was this useful?YesNo
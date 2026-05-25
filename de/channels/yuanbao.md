---
title: Yuanbao
source_url: https://docs.openclaw.ai/de/channels/yuanbao
scraped_at: 2026-05-25
---

Tencent Yuanbao ist Tencents KI-Assistentenplattform. Das OpenClaw-Kanal-Plugin verbindet Yuanbao-Bots über WebSocket mit OpenClaw, damit sie über Direktnachrichten und Gruppenchats mit Benutzern interagieren können.

**Status:** produktionsbereit für Bot-Direktnachrichten + Gruppenchats. WebSocket ist der einzige unterstützte Verbindungsmodus.

* * *

## Schnellstart

> **Erfordert OpenClaw 2026.4.10 oder höher.** Führen Sie `openclaw --version` aus, um dies zu prüfen. Aktualisieren Sie mit `openclaw update`.

* ### Fügen Sie den Yuanbao-Kanal mit Ihren Anmeldedaten hinzu

bashCopy code
[code]
    openclaw channels add --channel yuanbao --token "appKey:appSecret"
[/code]

Der Wert `--token` verwendet das durch Doppelpunkte getrennte Format `appKey:appSecret`. Sie können diese Werte aus der Yuanbao-App abrufen, indem Sie in Ihren Anwendungseinstellungen einen Roboter erstellen.

* ### Starten Sie nach Abschluss der Einrichtung den Gateway neu, um die Änderungen anzuwenden

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Interaktive Einrichtung (Alternative)

Sie können auch den interaktiven Assistenten verwenden:

bashCopy code
[code]
    openclaw channels login --channel yuanbao
[/code]

Folgen Sie den Eingabeaufforderungen, um Ihre App ID und Ihr App Secret einzugeben.

* * *

## Zugriffskontrolle

### Direktnachrichten

Konfigurieren Sie `dmPolicy`, um zu steuern, wer dem Bot Direktnachrichten senden kann:

  * `"pairing"` \- unbekannte Benutzer erhalten einen Kopplungscode; Genehmigung über CLI
  * `"allowlist"` \- nur in `allowFrom` aufgeführte Benutzer können chatten
  * `"open"` \- alle Benutzer zulassen (Standard)
  * `"disabled"` \- alle Direktnachrichten deaktivieren


**Kopplungsanfrage genehmigen:**

bashCopy code
[code]
    openclaw pairing list yuanbaoopenclaw pairing approve yuanbao &lt;CODE&gt;
[/code]

### Gruppenchats

**Erwähnungspflicht** (`channels.yuanbao.requireMention`):

  * `true` \- @mention erforderlich (Standard)
  * `false` \- ohne @mention antworten


Das Antworten auf die Nachricht des Bots in einem Gruppenchat wird als implizite Erwähnung behandelt.

* * *

## Konfigurationsbeispiele

### Grundeinrichtung mit offener Richtlinie für Direktnachrichten

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "open",      },    },  },}
[/code]

### Direktnachrichten auf bestimmte Benutzer beschränken

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "allowlist",        allowFrom: ["user_id_1", "user_id_2"],      },    },  },}
[/code]

### @mention-Pflicht in Gruppen deaktivieren

json5Copy code
[code]
    {  channels: {    yuanbao: {      requireMention: false,    },  },}
[/code]

### Zustellung ausgehender Nachrichten optimieren

json5Copy code
[code]
    {  channels: {    yuanbao: {      // Send each chunk immediately without buffering      outboundQueueStrategy: "immediate",    },  },}
[/code]

### Merge-text-Strategie abstimmen

json5Copy code
[code]
    {  channels: {    yuanbao: {      outboundQueueStrategy: "merge-text",      minChars: 2800, // buffer until this many chars      maxChars: 3000, // force split above this limit      idleMs: 5000, // auto-flush after idle timeout (ms)    },  },}
[/code]

* * *

## Häufige Befehle

Befehl | Beschreibung  
---|---  
`/help` | Verfügbare Befehle anzeigen  
`/status` | Bot-Status anzeigen  
`/new` | Eine neue Sitzung starten  
`/stop` | Den aktuellen Lauf stoppen  
`/restart` | OpenClaw neu starten  
`/compact` | Sitzungskontext komprimieren  
  
> Yuanbao unterstützt native Slash-Command-Menüs. Befehle werden beim Start des Gateway automatisch mit der Plattform synchronisiert.

* * *

## Fehlerbehebung

### Bot antwortet in Gruppenchats nicht

  1. Stellen Sie sicher, dass der Bot zur Gruppe hinzugefügt wurde
  2. Stellen Sie sicher, dass Sie den Bot per @mention erwähnen (standardmäßig erforderlich)
  3. Protokolle prüfen: `openclaw logs --follow`


### Bot empfängt keine Nachrichten

  1. Stellen Sie sicher, dass der Bot in der Yuanbao-App erstellt und genehmigt wurde
  2. Stellen Sie sicher, dass `appKey` und `appSecret` korrekt konfiguriert sind
  3. Stellen Sie sicher, dass der Gateway ausgeführt wird: `openclaw gateway status`
  4. Protokolle prüfen: `openclaw logs --follow`


### Bot sendet leere oder Fallback-Antworten

  1. Prüfen Sie, ob das KI-Modell gültige Inhalte zurückgibt
  2. Die standardmäßige Fallback-Antwort lautet: "暂时无法解答，你可以换个问题问问我哦"
  3. Passen Sie sie über `channels.yuanbao.fallbackReply` an


### App Secret offengelegt

  1. Setzen Sie das App Secret in der YuanBao APP zurück
  2. Aktualisieren Sie den Wert in Ihrer Konfiguration
  3. Starten Sie den Gateway neu: `openclaw gateway restart`


* * *

## Erweiterte Konfiguration

### Mehrere Konten

json5Copy code
[code]
    {  channels: {    yuanbao: {      defaultAccount: "main",      accounts: {        main: {          appKey: "key_xxx",          appSecret: "secret_xxx",          name: "Primary bot",        },        backup: {          appKey: "key_yyy",          appSecret: "secret_yyy",          name: "Backup bot",          enabled: false,        },      },    },  },}
[/code]

`defaultAccount` steuert, welches Konto verwendet wird, wenn ausgehende APIs kein `accountId` angeben.

### Nachrichtenlimits

  * `maxChars` \- maximale Zeichenanzahl für eine einzelne Nachricht (Standard: `3000` Zeichen)
  * `mediaMaxMb` \- Limit für Medien-Upload/-Download (Standard: `20` MB)
  * `overflowPolicy` \- Verhalten, wenn die Nachricht das Limit überschreitet: `"split"` (Standard) oder `"stop"`


### Streaming

Yuanbao unterstützt Streaming-Ausgabe auf Blockebene. Wenn aktiviert, sendet der Bot Text in Blöcken, während er ihn generiert.

json5Copy code
[code]
    {  channels: {    yuanbao: {      disableBlockStreaming: false, // block streaming enabled (default)    },  },}
[/code]

Setzen Sie `disableBlockStreaming: true`, um die vollständige Antwort in einer Nachricht zu senden.

### Gruppenchathistorie-Kontext

Steuern Sie, wie viele frühere Nachrichten für Gruppenchats in den KI-Kontext aufgenommen werden:

json5Copy code
[code]
    {  channels: {    yuanbao: {      historyLimit: 100, // default: 100, set 0 to disable    },  },}
[/code]

### Reply-to-Modus

Steuern Sie, wie der Bot Nachrichten beim Antworten in Gruppenchats zitiert:

json5Copy code
[code]
    {  channels: {    yuanbao: {      replyToMode: "first", // "off" | "first" | "all" (default: "first")    },  },}
[/code]

Wert | Verhalten  
---|---  
`"off"` | Keine Zitatantwort  
`"first"` | Nur die erste Antwort pro eingehender Nachricht zitieren (Standard)  
`"all"` | Jede Antwort zitieren  
  
### Markdown-Hinweis-Injektion

Standardmäßig fügt der Bot Anweisungen in den System-Prompt ein, um zu verhindern, dass das KI-Modell die gesamte Antwort in Markdown-Codeblöcke einschließt.

json5Copy code
[code]
    {  channels: {    yuanbao: {      markdownHintEnabled: true, // default: true    },  },}
[/code]

### Debug-Modus

Aktivieren Sie nicht bereinigte Protokollausgabe für bestimmte Bot-IDs:

json5Copy code
[code]
    {  channels: {    yuanbao: {      debugBotIds: ["bot_user_id_1", "bot_user_id_2"],    },  },}
[/code]

### Multi-Agent-Routing

Verwenden Sie `bindings`, um Yuanbao-Direktnachrichten oder -Gruppen an verschiedene Agenten weiterzuleiten.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main" },      { id: "agent-a", workspace: "/home/user/agent-a" },      { id: "agent-b", workspace: "/home/user/agent-b" },    ],  },  bindings: [    {      agentId: "agent-a",      match: {        channel: "yuanbao",        peer: { kind: "direct", id: "user_xxx" },      },    },    {      agentId: "agent-b",      match: {        channel: "yuanbao",        peer: { kind: "group", id: "group_zzz" },      },    },  ],}
[/code]

Routing-Felder:

  * `match.channel`: `"yuanbao"`
  * `match.peer.kind`: `"direct"` (Direktnachricht) oder `"group"` (Gruppenchat)
  * `match.peer.id`: Benutzer-ID oder Gruppencode


* * *

## Konfigurationsreferenz

Vollständige Konfiguration: [Gateway-Konfiguration](</de/gateway/configuration>)

Einstellung | Beschreibung | Standard  
---|---|---  
`channels.yuanbao.enabled` | Kanal aktivieren/deaktivieren | `true`  
`channels.yuanbao.defaultAccount` | Standardkonto für ausgehendes Routing | `default`  
`channels.yuanbao.accounts.<id>.appKey` | App Key (für Signierung und Ticketerstellung verwendet) | -  
`channels.yuanbao.accounts.<id>.appSecret` | App Secret (für Signierung verwendet) | -  
`channels.yuanbao.accounts.<id>.token` | Vorab signiertes Token (überspringt automatische Ticketsignierung) | -  
`channels.yuanbao.accounts.<id>.name` | Anzeigename des Kontos | -  
`channels.yuanbao.accounts.<id>.enabled` | Bestimmtes Konto aktivieren/deaktivieren | `true`  
`channels.yuanbao.dm.policy` | Richtlinie für Direktnachrichten | `open`  
`channels.yuanbao.dm.allowFrom` | Allowlist für Direktnachrichten (Liste von Benutzer-IDs) | -  
`channels.yuanbao.requireMention` | @mention in Gruppen erforderlich | `true`  
`channels.yuanbao.overflowPolicy` | Verarbeitung langer Nachrichten (`split` oder `stop`) | `split`  
`channels.yuanbao.replyToMode` | Reply-to-Strategie für Gruppen (`off`, `first`, `all`) | `first`  
`channels.yuanbao.outboundQueueStrategy` | Ausgehende Strategie (`merge-text` oder `immediate`) | `merge-text`  
`channels.yuanbao.minChars` | Merge-text: Mindestanzahl Zeichen zum Auslösen des Sendens | `2800`  
`channels.yuanbao.maxChars` | Merge-text: maximale Zeichen pro Nachricht | `3000`  
`channels.yuanbao.idleMs` | Merge-text: Leerlauf-Timeout vor automatischem Flush (ms) | `5000`  
`channels.yuanbao.mediaMaxMb` | Mediengrößenlimit (MB) | `20`  
`channels.yuanbao.historyLimit` | Einträge für Gruppenchathistorie-Kontext | `100`  
`channels.yuanbao.disableBlockStreaming` | Streaming-Ausgabe auf Blockebene deaktivieren | `false`  
`channels.yuanbao.fallbackReply` | Fallback-Antwort, wenn die KI keinen Inhalt zurückgibt | `暂时无法解答，你可以换个问题问问我哦`  
`channels.yuanbao.markdownHintEnabled` | Markdown-Anweisungen gegen Umbruch in Codeblöcke injizieren | `true`  
`channels.yuanbao.debugBotIds` | Debug-Allowlist für Bot-IDs (nicht bereinigte Protokolle) | `[]`  
  
* * *

## Unterstützte Nachrichtentypen

### Empfangen

  * ✅ Text
  * ✅ Bilder
  * ✅ Dateien
  * ✅ Audio / Sprache
  * ✅ Video
  * ✅ Sticker / benutzerdefinierte Emoji
  * ✅ Benutzerdefinierte Elemente (Linkkarten usw.)


### Senden

  * ✅ Text (mit Markdown-Unterstützung)
  * ✅ Bilder
  * ✅ Dateien
  * ✅ Audio
  * ✅ Video
  * ✅ Sticker


### Threads und Antworten

  * ✅ Zitatantworten (konfigurierbar über `replyToMode`)
  * ❌ Thread-Antworten (von der Plattform nicht unterstützt)


* * *

## Verwandte Themen

  * [Kanalübersicht](</de/channels>) \- alle unterstützten Kanäle
  * [Kopplung](</de/channels/pairing>) \- Authentifizierung für Direktnachrichten und Kopplungsablauf
  * [Gruppen](</de/channels/groups>) \- Gruppenchatverhalten und Erwähnungsgating
  * [Kanal-Routing](</de/channels/channel-routing>) \- Sitzungsrouting für Nachrichten
  * [Sicherheit](</de/gateway/security>) \- Zugriffsmodell und Härtung


Was this useful?YesNo
---
title: Nextcloud Talk
source_url: https://docs.openclaw.ai/de/channels/nextcloud-talk
scraped_at: 2026-05-25
---

Status: gebündeltes Plugin (Webhook-Bot). Direktnachrichten, Räume, Reaktionen und Markdown-Nachrichten werden unterstützt.

## Gebündeltes Plugin

Nextcloud Talk wird in aktuellen OpenClaw-Versionen als gebündeltes Plugin ausgeliefert, daher benötigen normale Paket-Builds keine separate Installation.

Wenn Sie eine ältere Version oder eine benutzerdefinierte Installation verwenden, die Nextcloud Talk ausschließt, installieren Sie das npm-Paket direkt:

Installation über CLI (npm-Registry):

bashCopy code
[code]
    openclaw plugins install @openclaw/nextcloud-talk
[/code]

Verwenden Sie das reine Paket, um dem aktuellen offiziellen Release-Tag zu folgen. Pinnen Sie eine exakte Version nur, wenn Sie eine reproduzierbare Installation benötigen.

Lokaler Checkout (wenn Sie aus einem Git-Repo ausführen):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/nextcloud-talk-plugin
[/code]

Details: [Plugins](</de/tools/plugin>)

## Schnelle Einrichtung (Anfänger)

  1. Stellen Sie sicher, dass das Nextcloud Talk-Plugin verfügbar ist.

     * Aktuelle paketierte OpenClaw-Releases bündeln es bereits.
     * Ältere/benutzerdefinierte Installationen können es mit den obigen Befehlen manuell hinzufügen.
  2. Erstellen Sie auf Ihrem Nextcloud-Server einen Bot:

bashCopy code
[code]./occ talk:bot:install "OpenClaw" "<shared-secret>" "<webhook-url>" --feature webhook --feature response --feature reaction
[/code]

  3. Aktivieren Sie den Bot in den Einstellungen des Zielraums.

  4. Konfigurieren Sie OpenClaw:

     * Konfiguration: `channels.nextcloud-talk.baseUrl` \+ `channels.nextcloud-talk.botSecret`
     * Oder Umgebung: `NEXTCLOUD_TALK_BOT_SECRET` (nur Standardkonto)

CLI-Einrichtung:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --url https://cloud.example.com \  --token "<shared-secret>"
[/code]

Entsprechende explizite Felder:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret "<shared-secret>"
[/code]

Dateigestütztes Geheimnis:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret-file /path/to/nextcloud-talk-secret
[/code]

  5. Starten Sie den Gateway neu (oder schließen Sie die Einrichtung ab).


Minimale Konfiguration:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      enabled: true,      baseUrl: "https://cloud.example.com",      botSecret: "shared-secret",      dmPolicy: "pairing",    },  },}
[/code]

## Hinweise

  * Bots können keine Direktnachrichten initiieren. Der Benutzer muss dem Bot zuerst eine Nachricht senden.
  * Die Webhook-URL muss für den Gateway erreichbar sein; setzen Sie `webhookPublicUrl`, wenn sie hinter einem Proxy liegt.
  * Medien-Uploads werden von der Bot-API nicht unterstützt; Medien werden als URLs gesendet.
  * Die Webhook-Nutzlast unterscheidet nicht zwischen Direktnachrichten und Räumen; setzen Sie `apiUser` \+ `apiPassword`, um Raumtyp-Abfragen zu aktivieren (andernfalls werden Direktnachrichten als Räume behandelt).


## Zugriffskontrolle (Direktnachrichten)

  * Standard: `channels.nextcloud-talk.dmPolicy = "pairing"`. Unbekannte Absender erhalten einen Pairing-Code.
  * Genehmigen über: 
    * `openclaw pairing list nextcloud-talk`
    * `openclaw pairing approve nextcloud-talk &lt;CODE&gt;`
  * Öffentliche Direktnachrichten: `channels.nextcloud-talk.dmPolicy="open"` plus `channels.nextcloud-talk.allowFrom=["*"]`.
  * `allowFrom` gleicht nur Nextcloud-Benutzer-IDs ab; Anzeigenamen werden ignoriert.


## Räume (Gruppen)

  * Standard: `channels.nextcloud-talk.groupPolicy = "allowlist"` (durch Erwähnungen gesteuert).
  * Räume mit `channels.nextcloud-talk.rooms` in die Zulassungsliste aufnehmen:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      rooms: {        "room-token": { requireMention: true },      },    },  },}
[/code]

  * Um keine Räume zuzulassen, lassen Sie die Zulassungsliste leer oder setzen Sie `channels.nextcloud-talk.groupPolicy="disabled"`.


## Fähigkeiten

Funktion | Status  
---|---  
Direktnachrichten | Unterstützt  
Räume | Unterstützt  
Threads | Nicht unterstützt  
Medien | Nur URLs  
Reaktionen | Unterstützt  
Native Befehle | Nicht unterstützt  
  
## Konfigurationsreferenz (Nextcloud Talk)

Vollständige Konfiguration: [Konfiguration](</de/gateway/configuration>)

Provider-Optionen:

  * `channels.nextcloud-talk.enabled`: Aktivieren/Deaktivieren des Kanalstarts.
  * `channels.nextcloud-talk.baseUrl`: URL der Nextcloud-Instanz.
  * `channels.nextcloud-talk.botSecret`: gemeinsames Geheimnis des Bots.
  * `channels.nextcloud-talk.botSecretFile`: Pfad zu einer regulären Datei mit dem Geheimnis. Symlinks werden abgelehnt.
  * `channels.nextcloud-talk.apiUser`: API-Benutzer für Raumabfragen (Direktnachrichtenerkennung).
  * `channels.nextcloud-talk.apiPassword`: API-/App-Passwort für Raumabfragen.
  * `channels.nextcloud-talk.apiPasswordFile`: Pfad zur API-Passwortdatei.
  * `channels.nextcloud-talk.webhookPort`: Port des Webhook-Listeners (Standard: 8788).
  * `channels.nextcloud-talk.webhookHost`: Webhook-Host (Standard: 0.0.0.0).
  * `channels.nextcloud-talk.webhookPath`: Webhook-Pfad (Standard: /nextcloud-talk-webhook).
  * `channels.nextcloud-talk.webhookPublicUrl`: extern erreichbare Webhook-URL.
  * `channels.nextcloud-talk.dmPolicy`: `pairing | allowlist | open | disabled`.
  * `channels.nextcloud-talk.allowFrom`: Zulassungsliste für Direktnachrichten (Benutzer-IDs). `open` erfordert `"*"`.
  * `channels.nextcloud-talk.groupPolicy`: `allowlist | open | disabled`.
  * `channels.nextcloud-talk.groupAllowFrom`: Zulassungsliste für Gruppen (Benutzer-IDs).
  * `channels.nextcloud-talk.rooms`: Einstellungen und Zulassungsliste pro Raum.
  * Statische Absender-Zugriffsgruppen können aus `allowFrom` und `groupAllowFrom` mit `accessGroup:<name>` referenziert werden.
  * `channels.nextcloud-talk.historyLimit`: Verlaufsgrenze für Gruppen (0 deaktiviert).
  * `channels.nextcloud-talk.dmHistoryLimit`: Verlaufsgrenze für Direktnachrichten (0 deaktiviert).
  * `channels.nextcloud-talk.dms`: Überschreibungen pro Direktnachricht (historyLimit).
  * `channels.nextcloud-talk.textChunkLimit`: Größe ausgehender Textabschnitte (Zeichen).
  * `channels.nextcloud-talk.chunkMode`: `length` (Standard) oder `newline`, um vor dem Aufteilen nach Länge an Leerzeilen (Absatzgrenzen) zu teilen.
  * `channels.nextcloud-talk.blockStreaming`: Block-Streaming für diesen Kanal deaktivieren.
  * `channels.nextcloud-talk.blockStreamingCoalesce`: Abstimmung der Block-Streaming-Zusammenführung.
  * `channels.nextcloud-talk.mediaMaxMb`: Grenze für eingehende Medien (MB).


## Verwandte Themen

  * [Kanalübersicht](</de/channels>) — alle unterstützten Kanäle
  * [Pairing](</de/channels/pairing>) — Authentifizierung für Direktnachrichten und Pairing-Ablauf
  * [Gruppen](</de/channels/groups>) — Gruppenchat-Verhalten und Erwähnungssteuerung
  * [Kanal-Routing](</de/channels/channel-routing>) — Sitzungs-Routing für Nachrichten
  * [Sicherheit](</de/gateway/security>) — Zugriffsmodell und Härtung


Was this useful?YesNo
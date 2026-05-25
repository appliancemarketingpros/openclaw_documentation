---
title: WeChat
source_url: https://docs.openclaw.ai/de/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw verbindet sich über Tencents externes Channel-Plugin `@tencent-weixin/openclaw-weixin` mit WeChat.

Status: externes Plugin. Direkte Chats und Medien werden unterstützt. Gruppenchats werden von den aktuellen Plugin-Fähigkeitsmetadaten nicht ausgewiesen.

## Benennung

  * **WeChat** ist der benutzerseitige Name in dieser Dokumentation.
  * **Weixin** ist der Name, den Tencents Paket und die Plugin-ID verwenden.
  * `openclaw-weixin` ist die OpenClaw-Channel-ID.
  * `@tencent-weixin/openclaw-weixin` ist das npm-Paket.


Verwenden Sie `openclaw-weixin` in CLI-Befehlen und Konfigurationspfaden.

## So funktioniert es

Der WeChat-Code befindet sich nicht im OpenClaw-Core-Repo. OpenClaw stellt den generischen Channel-Plugin-Vertrag bereit, und das externe Plugin stellt die WeChat-spezifische Runtime bereit:

  1. `openclaw plugins install` installiert `@tencent-weixin/openclaw-weixin`.
  2. Das Gateway erkennt das Plugin-Manifest und lädt den Plugin-Einstiegspunkt.
  3. Das Plugin registriert die Channel-ID `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` startet die QR-Anmeldung.
  5. Das Plugin speichert Kontoanmeldedaten im OpenClaw-State-Verzeichnis.
  6. Wenn das Gateway startet, startet das Plugin seinen Weixin-Monitor für jedes konfigurierte Konto.
  7. Eingehende WeChat-Nachrichten werden über den Channel-Vertrag normalisiert, an den ausgewählten OpenClaw-Agent weitergeleitet und über den ausgehenden Pfad des Plugins zurückgesendet.


Diese Trennung ist wichtig: Der OpenClaw-Core sollte channel-agnostisch bleiben. WeChat-Anmeldung, Tencent-iLink-API-Aufrufe, Medien-Upload/-Download, Kontext-Token und Kontoüberwachung gehören zum externen Plugin.

## Installation

Schnellinstallation:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Manuelle Installation:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Starten Sie das Gateway nach der Installation neu:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Anmeldung

Führen Sie die QR-Anmeldung auf demselben Rechner aus, auf dem das Gateway läuft:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Scannen Sie den QR-Code mit WeChat auf Ihrem Telefon und bestätigen Sie die Anmeldung. Das Plugin speichert das Konto-Token nach einem erfolgreichen Scan lokal.

Um ein weiteres WeChat-Konto hinzuzufügen, führen Sie denselben Anmeldebefehl erneut aus. Isolieren Sie bei mehreren Konten Direktnachrichtensitzungen nach Konto, Channel und Absender:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Zugriffskontrolle

Direktnachrichten verwenden das normale OpenClaw-Pairing- und Allowlist-Modell für Channel- Plugins.

Neue Absender genehmigen:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Das vollständige Zugriffskontrollmodell finden Sie unter [Pairing](</de/channels/pairing>).

## Kompatibilität

Das Plugin prüft beim Start die OpenClaw-Version des Hosts.

Plugin-Linie | OpenClaw-Version | npm-Tag  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Wenn das Plugin meldet, dass Ihre OpenClaw-Version zu alt ist, aktualisieren Sie entweder OpenClaw oder installieren Sie die Legacy-Plugin-Linie:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Sidecar-Prozess

Das WeChat-Plugin kann Hilfsarbeit neben dem Gateway ausführen, während es die Tencent-iLink-API überwacht. In Issue #68451 legte dieser Hilfspfad einen Fehler in OpenClaws generischer Bereinigung veralteter Gateways offen: Ein Kindprozess konnte versuchen, den übergeordneten Gateway-Prozess zu bereinigen, was unter Prozessmanagern wie systemd zu Neustartschleifen führte.

Die aktuelle OpenClaw-Startbereinigung schließt den aktuellen Prozess und seine Vorfahren aus, sodass ein Channel-Helfer das Gateway, das ihn gestartet hat, nicht beenden darf. Diese Korrektur ist generisch; sie ist kein WeChat-spezifischer Pfad im Core.

## Fehlerbehebung

Installation und Status prüfen:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Wenn der Channel als installiert angezeigt wird, aber keine Verbindung herstellt, bestätigen Sie, dass das Plugin aktiviert ist, und starten Sie neu:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Wenn das Gateway nach dem Aktivieren von WeChat wiederholt neu startet, aktualisieren Sie sowohl OpenClaw als auch das Plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Wenn der Start meldet, dass das installierte Plugin-Paket `requires compiled runtime output for TypeScript entry`, wurde das npm-Paket ohne die kompilierten JavaScript-Runtime-Dateien veröffentlicht, die OpenClaw benötigt. Aktualisieren/installieren Sie es erneut, nachdem der Plugin- Publisher ein korrigiertes Paket veröffentlicht hat, oder deaktivieren/deinstallieren Sie das Plugin vorübergehend.

Vorübergehend deaktivieren:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Zugehörige Dokumentation

  * Channel-Übersicht: [Chat Channels](</de/channels>)
  * Pairing: [Pairing](</de/channels/pairing>)
  * Channel-Routing: [Channel Routing](</de/channels/channel-routing>)
  * Plugin-Architektur: [Plugin Architecture](</de/plugins/architecture>)
  * Channel-Plugin-SDK: [Channel Plugin SDK](</de/plugins/sdk-channel-plugins>)
  * Externes Paket: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo
---
title: Twitch
source_url: https://docs.openclaw.ai/de/channels/twitch
scraped_at: 2026-05-25
---

Twitch-Chat-Unterstützung über IRC-Verbindung. OpenClaw verbindet sich als Twitch-Benutzer (Bot-Konto), um Nachrichten in Kanälen zu empfangen und zu senden.

## Gebündeltes Plugin

Wenn Sie einen älteren Build oder eine benutzerdefinierte Installation verwenden, die Twitch ausschließt, installieren Sie das npm-Paket direkt:

### npm-Registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Lokaler Checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Verwenden Sie das reine Paket, um dem aktuellen offiziellen Release-Tag zu folgen. Pinnen Sie eine exakte Version nur, wenn Sie eine reproduzierbare Installation benötigen.

Details: [Plugins](</de/tools/plugin>)

## Schnelle Einrichtung (Einsteiger)

* ### Sicherstellen, dass das Plugin verfügbar ist

Aktuelle paketierte OpenClaw-Releases bündeln es bereits. Ältere/benutzerdefinierte Installationen können es mit den obigen Befehlen manuell hinzufügen.

* ### Twitch-Bot-Konto erstellen

Erstellen Sie ein dediziertes Twitch-Konto für den Bot (oder verwenden Sie ein vorhandenes Konto).

* ### Zugangsdaten erzeugen

Verwenden Sie [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Wählen Sie **Bot Token**
  * Prüfen Sie, dass die Scopes `chat:read` und `chat:write` ausgewählt sind
  * Kopieren Sie die **Client ID** und das **Access Token**


* ### Ihre Twitch-Benutzer-ID finden

Verwenden Sie <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/>, um einen Benutzernamen in eine Twitch-Benutzer-ID umzuwandeln.

* ### Token konfigurieren

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (nur Standardkonto)
  * Oder Konfiguration: `channels.twitch.accessToken`


Wenn beides gesetzt ist, hat die Konfiguration Vorrang (Env-Fallback gilt nur für das Standardkonto).

* ### Gateway starten

Starten Sie das Gateway mit dem konfigurierten Kanal.

Minimale Konfiguration:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Was es ist

  * Ein Twitch-Kanal, der dem Gateway gehört.
  * Deterministisches Routing: Antworten gehen immer zurück an Twitch.
  * Jedes Konto wird einem isolierten Sitzungsschlüssel `agent:<agentId>:twitch:<accountName>` zugeordnet.
  * `username` ist das Konto des Bots (das authentifiziert wird), `channel` ist der Chatraum, dem beigetreten wird.


## Einrichtung (detailliert)

### Zugangsdaten erzeugen

Verwenden Sie [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Wählen Sie **Bot Token**
  * Prüfen Sie, dass die Scopes `chat:read` und `chat:write` ausgewählt sind
  * Kopieren Sie die **Client ID** und das **Access Token**


### Bot konfigurieren

### Env-Variable (nur Standardkonto)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Konfiguration

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Wenn Env und Konfiguration beide gesetzt sind, hat die Konfiguration Vorrang.

### Zugriffskontrolle (empfohlen)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Bevorzugen Sie `allowFrom` für eine harte Positivliste. Verwenden Sie stattdessen `allowedRoles`, wenn Sie rollenbasierten Zugriff möchten.

**Verfügbare Rollen:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Token-Aktualisierung (optional)

Tokens aus [Twitch Token Generator](<https://twitchtokengenerator.com/>) können nicht automatisch aktualisiert werden - erzeugen Sie sie nach Ablauf neu.

Für automatische Token-Aktualisierung erstellen Sie Ihre eigene Twitch-Anwendung in der [Twitch Developer Console](<https://dev.twitch.tv/console>) und fügen Sie der Konfiguration Folgendes hinzu:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Der Bot aktualisiert Tokens automatisch vor dem Ablauf und protokolliert Aktualisierungsereignisse.

## Unterstützung für mehrere Konten

Verwenden Sie `channels.twitch.accounts` mit kontoabhängigen Tokens. Siehe [Konfiguration](</de/gateway/configuration>) für das gemeinsame Muster.

Beispiel (ein Bot-Konto in zwei Kanälen):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Zugriffskontrolle

### Benutzer-ID-Positivliste (am sichersten)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Rollenbasiert

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` ist eine harte Positivliste. Wenn gesetzt, sind nur diese Benutzer-IDs erlaubt. Wenn Sie rollenbasierten Zugriff möchten, lassen Sie `allowFrom` ungesetzt und konfigurieren Sie stattdessen `allowedRoles`.

### @mention-Anforderung deaktivieren

Standardmäßig ist `requireMention` `true`. So deaktivieren Sie dies und antworten auf alle Nachrichten:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Fehlerbehebung

Führen Sie zuerst Diagnosebefehle aus:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot reagiert nicht auf Nachrichten

  * **Zugriffskontrolle prüfen:** Stellen Sie sicher, dass Ihre Benutzer-ID in `allowFrom` enthalten ist, oder entfernen Sie `allowFrom` vorübergehend und setzen Sie zum Testen `allowedRoles: ["all"]`.
  * **Prüfen, ob der Bot im Kanal ist:** Der Bot muss dem in `channel` angegebenen Kanal beitreten.

Token-Probleme

„Failed to connect“ oder Authentifizierungsfehler:

  * Prüfen Sie, dass `accessToken` der OAuth-Zugriffstokenwert ist (beginnt typischerweise mit dem Präfix `oauth:`)
  * Prüfen Sie, dass das Token die Scopes `chat:read` und `chat:write` hat
  * Wenn Sie Token-Aktualisierung verwenden, prüfen Sie, dass `clientSecret` und `refreshToken` gesetzt sind

Token-Aktualisierung funktioniert nicht

Prüfen Sie die Logs auf Aktualisierungsereignisse:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Wenn Sie „token refresh disabled (no refresh token)“ sehen:

  * Stellen Sie sicher, dass `clientSecret` angegeben ist
  * Stellen Sie sicher, dass `refreshToken` angegeben ist


## Konfiguration

### Kontokonfiguration

Bot-Benutzername.

OAuth-Zugriffstoken mit `chat:read` und `chat:write`.

Twitch Client ID (aus Token Generator oder Ihrer App).

Kanal, dem beigetreten werden soll.

Dieses Konto aktivieren.

Optional: für automatische Token-Aktualisierung.

Optional: für automatische Token-Aktualisierung.

Token-Ablauf in Sekunden.

Zeitstempel, zu dem das Token erhalten wurde.

Benutzer-ID-Positivliste.

@mention erforderlich.

### Provider-Optionen

  * `channels.twitch.enabled` \- Kanalstart aktivieren/deaktivieren
  * `channels.twitch.username` \- Bot-Benutzername (vereinfachte Einzelkonto-Konfiguration)
  * `channels.twitch.accessToken` \- OAuth-Zugriffstoken (vereinfachte Einzelkonto-Konfiguration)
  * `channels.twitch.clientId` \- Twitch Client ID (vereinfachte Einzelkonto-Konfiguration)
  * `channels.twitch.channel` \- Kanal, dem beigetreten werden soll (vereinfachte Einzelkonto-Konfiguration)
  * `channels.twitch.accounts.<accountName>` \- Mehrkonten-Konfiguration (alle Kontofelder oben)


Vollständiges Beispiel:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Tool-Aktionen

Der Agent kann `twitch` mit folgender Aktion aufrufen:

  * `send` \- Eine Nachricht an einen Kanal senden


Beispiel:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Sicherheit und Betrieb

  * **Behandeln Sie Tokens wie Passwörter** — Committen Sie Tokens niemals in Git.
  * **Verwenden Sie automatische Token-Aktualisierung** für langlebige Bots.
  * **Verwenden Sie Benutzer-ID-Positivlisten** statt Benutzernamen für die Zugriffskontrolle.
  * **Überwachen Sie Logs** auf Token-Aktualisierungsereignisse und Verbindungsstatus.
  * **Beschränken Sie Tokens minimal** — Fordern Sie nur `chat:read` und `chat:write` an.
  * **Wenn Sie feststecken** : Starten Sie das Gateway neu, nachdem Sie bestätigt haben, dass kein anderer Prozess die Sitzung besitzt.


## Grenzen

  * **500 Zeichen** pro Nachricht (automatisch an Wortgrenzen aufgeteilt).
  * Markdown wird vor dem Aufteilen entfernt.
  * Keine Ratenbegrenzung (verwendet die integrierten Ratenbegrenzungen von Twitch).


## Verwandt

  * [Kanal-Routing](</de/channels/channel-routing>) — Sitzungs-Routing für Nachrichten
  * [Kanalübersicht](</de/channels>) — alle unterstützten Kanäle
  * [Gruppen](</de/channels/groups>) — Gruppenchat-Verhalten und Mention-Gating
  * [Pairing](</de/channels/pairing>) — DM-Authentifizierung und Pairing-Ablauf
  * [Sicherheit](</de/gateway/security>) — Zugriffsmodell und Härtung


Was this useful?YesNo
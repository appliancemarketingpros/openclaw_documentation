---
title: Tlon
source_url: https://docs.openclaw.ai/de/channels/tlon
scraped_at: 2026-05-25
---

Tlon ist ein dezentraler Messenger, der auf Urbit basiert. OpenClaw verbindet sich mit Ihrem Urbit-Ship und kann auf DMs und Gruppenchat-Nachrichten antworten. Gruppenantworten erfordern standardmäßig eine @-Erwähnung und können über Allowlists weiter eingeschränkt werden.

Status: gebündeltes Plugin. DMs, Gruppenerwähnungen, Thread-Antworten, Rich-Text-Formatierung und Bild-Uploads werden unterstützt. Reaktionen und Umfragen werden noch nicht unterstützt.

## Gebündeltes Plugin

Tlon wird in aktuellen OpenClaw-Versionen als gebündeltes Plugin ausgeliefert, daher benötigen normale paketierte Builds keine separate Installation.

Wenn Sie einen älteren Build oder eine benutzerdefinierte Installation verwenden, die Tlon ausschließt, installieren Sie ein aktuelles npm-Paket:

Installation über CLI (npm-Registry):

bashCopy code
[code]
    openclaw plugins install @openclaw/tlon
[/code]

Verwenden Sie das reine Paket, um dem aktuellen offiziellen Release-Tag zu folgen. Pinning auf eine exakte Version sollten Sie nur verwenden, wenn Sie eine reproduzierbare Installation benötigen.

Lokaler Checkout (wenn Sie aus einem Git-Repository ausführen):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/tlon-plugin
[/code]

Details: [Plugins](</de/tools/plugin>)

## Einrichtung

  1. Stellen Sie sicher, dass das Tlon-Plugin verfügbar ist. 
     * Aktuelle paketierte OpenClaw-Releases bündeln es bereits.
     * Ältere/benutzerdefinierte Installationen können es manuell mit den obigen Befehlen hinzufügen.
  2. Ermitteln Sie Ihre Ship-URL und Ihren Login-Code.
  3. Konfigurieren Sie `channels.tlon`.
  4. Starten Sie den Gateway neu.
  5. Senden Sie dem Bot eine DM oder erwähnen Sie ihn in einem Gruppenkanal.


Minimale Konfiguration (ein einzelnes Konto):

json5Copy code
[code]
    {  channels: {    tlon: {      enabled: true,      ship: "~sampel-palnet",      url: "https://your-ship-host",      code: "lidlut-tabwed-pillex-ridrup",      ownerShip: "~your-main-ship", // recommended: your ship, always allowed    },  },}
[/code]

## Private/LAN-Ships

Standardmäßig blockiert OpenClaw private/interne Hostnamen und IP-Bereiche zum Schutz vor SSRF. Wenn Ihr Ship in einem privaten Netzwerk läuft (localhost, LAN-IP oder interner Hostname), müssen Sie dies ausdrücklich aktivieren:

json5Copy code
[code]
    {  channels: {    tlon: {      url: "http://localhost:8080",      allowPrivateNetwork: true,    },  },}
[/code]

Dies gilt für URLs wie:

  * `http://localhost:8080`
  * `http://192.168.x.x:8080`
  * `http://my-ship.local:8080`


⚠️ Aktivieren Sie dies nur, wenn Sie Ihrem lokalen Netzwerk vertrauen. Diese Einstellung deaktiviert SSRF-Schutzmechanismen für Anfragen an Ihre Ship-URL.

## Gruppenkanäle

Die automatische Erkennung ist standardmäßig aktiviert. Sie können Kanäle auch manuell festlegen:

json5Copy code
[code]
    {  channels: {    tlon: {      groupChannels: ["chat/~host-ship/general", "chat/~host-ship/support"],    },  },}
[/code]

Automatische Erkennung deaktivieren:

json5Copy code
[code]
    {  channels: {    tlon: {      autoDiscoverChannels: false,    },  },}
[/code]

## Zugriffskontrolle

DM-Allowlist (leer = keine DMs erlaubt, verwenden Sie `ownerShip` für den Genehmigungsablauf):

json5Copy code
[code]
    {  channels: {    tlon: {      dmAllowlist: ["~zod", "~nec"],    },  },}
[/code]

Gruppenautorisierung (standardmäßig eingeschränkt):

json5Copy code
[code]
    {  channels: {    tlon: {      defaultAuthorizedShips: ["~zod"],      authorization: {        channelRules: {          "chat/~host-ship/general": {            mode: "restricted",            allowedShips: ["~zod", "~nec"],          },          "chat/~host-ship/announcements": {            mode: "open",          },        },      },    },  },}
[/code]

## Owner- und Genehmigungssystem

Legen Sie ein Owner-Ship fest, um Genehmigungsanfragen zu erhalten, wenn nicht autorisierte Benutzer zu interagieren versuchen:

json5Copy code
[code]
    {  channels: {    tlon: {      ownerShip: "~your-main-ship",    },  },}
[/code]

Das Owner-Ship ist **überall automatisch autorisiert** — DM-Einladungen werden automatisch akzeptiert und Kanalnachrichten sind immer erlaubt. Sie müssen den Owner nicht zu `dmAllowlist` oder `defaultAuthorizedShips` hinzufügen.

Wenn festgelegt, erhält der Owner DM-Benachrichtigungen für:

  * DM-Anfragen von Ships, die nicht in der Allowlist stehen
  * Erwähnungen in Kanälen ohne Autorisierung
  * Gruppen-Einladungsanfragen


## Einstellungen für automatische Annahme

DM-Einladungen automatisch akzeptieren (für Ships in dmAllowlist):

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptDmInvites: true,    },  },}
[/code]

Gruppeneinladungen von vertrauenswürdigen Ships automatisch akzeptieren:

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptGroupInvites: true,      groupInviteAllowlist: ["~zod"],    },  },}
[/code]

`autoAcceptGroupInvites` schlägt geschlossen fehl, wenn `groupInviteAllowlist` leer ist. Setzen Sie die Allowlist auf die Ships, deren Gruppeneinladungen automatisch akzeptiert werden sollen.

## Zustellziele (CLI/Cron)

Verwenden Sie diese mit `openclaw message send` oder Cron-Zustellung:

  * DM: `~sampel-palnet` oder `dm/~sampel-palnet`
  * Gruppe: `chat/~host-ship/channel` oder `group:~host-ship/channel`


## Gebündelter Skill

Das Tlon-Plugin enthält einen gebündelten Skill ([`@tloncorp/tlon-skill`](<https://github.com/tloncorp/tlon-skill>)), der CLI-Zugriff auf Tlon-Operationen bereitstellt:

  * **Kontakte** : Profile abrufen/aktualisieren, Kontakte auflisten
  * **Kanäle** : auflisten, erstellen, Nachrichten posten, Verlauf abrufen
  * **Gruppen** : auflisten, erstellen, Mitglieder verwalten
  * **DMs** : Nachrichten senden, auf Nachrichten reagieren
  * **Reaktionen** : Emoji-Reaktionen zu Posts und DMs hinzufügen/entfernen
  * **Einstellungen** : Plugin-Berechtigungen über Slash-Befehle verwalten


Der Skill ist automatisch verfügbar, wenn das Plugin installiert ist.

## Funktionen

Funktion | Status  
---|---  
Direktnachrichten | ✅ Unterstützt  
Gruppen/Kanäle | ✅ Unterstützt (standardmäßig erwähnungsgesteuert)  
Threads | ✅ Unterstützt (automatische Antworten im Thread)  
Rich Text | ✅ Markdown wird in das Tlon-Format konvertiert  
Bilder | ✅ In Tlon-Speicher hochgeladen  
Reaktionen | ✅ Über gebündelten Skill  
Umfragen | ❌ Noch nicht unterstützt  
Native Befehle | ✅ Unterstützt (standardmäßig nur Owner)  
  
## Fehlerbehebung

Führen Sie zuerst diese Abfolge aus:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctor
[/code]

Häufige Fehler:

  * **DMs werden ignoriert** : Absender ist nicht in `dmAllowlist` und kein `ownerShip` für den Genehmigungsablauf konfiguriert.
  * **Gruppennachrichten werden ignoriert** : Kanal wurde nicht erkannt oder Absender ist nicht autorisiert.
  * **Verbindungsfehler** : Prüfen Sie, ob die Ship-URL erreichbar ist; aktivieren Sie `allowPrivateNetwork` für lokale Ships.
  * **Auth-Fehler** : Verifizieren Sie, dass der Login-Code aktuell ist (Codes rotieren).


## Konfigurationsreferenz

Vollständige Konfiguration: [Konfiguration](</de/gateway/configuration>)

Provider-Optionen:

  * `channels.tlon.enabled`: Kanalstart aktivieren/deaktivieren.
  * `channels.tlon.ship`: Urbit-Ship-Name des Bots (z. B. `~sampel-palnet`).
  * `channels.tlon.url`: Ship-URL (z. B. `https://sampel-palnet.tlon.network`).
  * `channels.tlon.code`: Ship-Login-Code.
  * `channels.tlon.allowPrivateNetwork`: localhost-/LAN-URLs erlauben (SSRF-Umgehung).
  * `channels.tlon.ownerShip`: Owner-Ship für Genehmigungssystem (immer autorisiert).
  * `channels.tlon.dmAllowlist`: Ships, die DMs senden dürfen (leer = keine).
  * `channels.tlon.autoAcceptDmInvites`: DMs von Ships in der Allowlist automatisch akzeptieren.
  * `channels.tlon.autoAcceptGroupInvites`: Gruppeneinladungen von Ships in der Allowlist automatisch akzeptieren.
  * `channels.tlon.groupInviteAllowlist`: Ships, deren Gruppeneinladungen automatisch akzeptiert werden dürfen.
  * `channels.tlon.autoDiscoverChannels`: Gruppenkanäle automatisch erkennen (Standard: true).
  * `channels.tlon.groupChannels`: manuell festgelegte Kanal-Nests.
  * `channels.tlon.defaultAuthorizedShips`: Ships, die für alle Kanäle autorisiert sind.
  * `channels.tlon.authorization.channelRules`: Auth-Regeln pro Kanal.
  * `channels.tlon.showModelSignature`: Modellname an Nachrichten anhängen.


## Hinweise

  * Gruppenantworten erfordern eine Erwähnung (z. B. `~your-bot-ship`), um zu antworten.
  * Thread-Antworten: Wenn die eingehende Nachricht in einem Thread ist, antwortet OpenClaw im Thread.
  * Rich Text: Markdown-Formatierung (fett, kursiv, Code, Überschriften, Listen) wird in das native Format von Tlon konvertiert.
  * Bilder: URLs werden in den Tlon-Speicher hochgeladen und als Bildblöcke eingebettet.


## Verwandte Themen

  * [Channels-Übersicht](</de/channels>) — alle unterstützten Kanäle
  * [Pairing](</de/channels/pairing>) — DM-Authentifizierung und Pairing-Ablauf
  * [Gruppen](</de/channels/groups>) — Gruppenchat-Verhalten und Erwähnungssteuerung
  * [Kanal-Routing](</de/channels/channel-routing>) — Sitzungs-Routing für Nachrichten
  * [Sicherheit](</de/gateway/security>) — Zugriffsmodell und Härtung


Was this useful?YesNo
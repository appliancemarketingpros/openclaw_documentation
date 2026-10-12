---
title: 1Password-Secrets-Broker
source_url: https://docs.openclaw.ai/de/plugins/onepassword
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

# 1Password-Secrets-Broker

Das gebündelte Plugin `onepassword` stellt Agenten ein richtliniengesteuertes Tool zum Lesen einer kuratierten Auswahl von 1Password-Feldern bereit. Es ist standardmäßig deaktiviert und führt nichts aus, bis `plugins.entries.onepassword.config` vorhanden ist.

Dies ist ein Agenten-Tool, kein SecretRef-Provider. Es injiziert keine Umgebungsvariablen und löst keine OpenClaw-Konfigurations-Secrets auf.

## Sicherheitsmodell

  * Nur Authentifizierung über ein Dienstkonto. Das Token verbleibt in einer lokalen Anmeldedatendatei und wird in `openclaw.json` niemals akzeptiert.
  * Nur kuratiertes Register. Agenten können konfigurierte Slugs auflisten, aber das Plugin listet niemals einen 1Password-Tresor auf.
  * Richtlinie `auto`, `approve` oder `deny` pro Slug.
  * Genehmigungsfreigaben laufen ab. Ein zwischengespeicherter Wert umgeht niemals die aktuelle Richtlinie.
  * Jeder Zugriffsversuch wird im gemeinsam genutzten SQLite-Status von OpenClaw aufgezeichnet. Audit- Zeilen enthalten den angegebenen Grund; verwenden Sie keine sensiblen Angaben in Gründen. Der Broker kopiert weder einen abgerufenen Wert noch das Dienst-Token in eine Audit-Zeile.
  * Nach der aktuellen Tool-Ausführung ersetzt die OpenClaw-eigene Transkriptpersistenz einen erfolgreichen `get`-Wert durch redigierte Metadaten.
  * Der Wert ist für das Modell während dieser Ausführung sichtbar. Wenn das Modell ihn in einen späteren Tool-Aufruf oder eine Antwort kopiert, liegt dieser separate Datensatz außerhalb des Persistenz-Hooks dieses Plugins. Halten Sie Richtlinien eng gefasst und fordern Sie das Modell nicht auf, einen Wert wiederzugeben.
  * Das Plugin ruft `op` einmal pro Cache-Fehltreffer auf. Bei Ratenbegrenzungen oder anderen Fehlern erfolgt kein erneuter Versuch.
  * Jeder `op`-Aufruf wird mit einer minimalen Umgebung ausgeführt, welche die Integration der 1Password-Desktop-App deaktiviert (`OP_LOAD_DESKTOP_APP_SETTINGS=false`, `OP_BIOMETRIC_UNLOCK_ENABLED=false`), sodass eine auf dem Gateway-Host installierte 1Password-App niemals biometrische oder macOS-Berechtigungsdialoge auslöst.


Gewähren Sie dem Dienstkonto ausschließlich Lesezugriff auf die Tresore und Elemente, die in der Plugin-Konfiguration registriert sind.

## Bevor Sie beginnen

Sie benötigen:

  * die auf dem Gateway-Host installierte 1Password-CLI (`op`)
  * ein 1Password-Dienstkonto mit Zugriff auf die ausgewählten Elemente
  * eine dedizierte Dienstkonto-Token-Datei


Aktivieren Sie das gebündelte Plugin:

bashCopy code
[code]
    openclaw plugins enable onepassword
[/code]

Erstellen Sie das Token-Verzeichnis und die Datei im OpenClaw-Statusverzeichnis:

bashCopy code
[code]
    mkdir -p ~/.openclaw/credentials/onepasswordchmod 700 ~/.openclaw/credentials/onepasswordprintf '%s' "$OP_SERVICE_ACCOUNT_TOKEN" > \  ~/.openclaw/credentials/onepassword/service-account-tokenchmod 600 ~/.openclaw/credentials/onepassword/service-account-tokenunset OP_SERVICE_ACCOUNT_TOKEN
[/code]

Wenn `OPENCLAW_STATE_DIR` festgelegt ist, ersetzen Sie `~/.openclaw` durch dieses Verzeichnis. Das Plugin warnt einmal, wenn die Token-Datei für die Gruppe oder andere Benutzer les- oder beschreibbar ist.

## Registrierte Secrets konfigurieren

Fügen Sie die Plugin-Konfiguration zu `openclaw.json` hinzu:

jsoncCopy code
[code]
    {  "plugins": {    "entries": {      "onepassword": {        "enabled": true,        "config": {          "vault": "Automation",          "defaultPolicy": "approve",          "cacheTtlSeconds": 300,          "grantTtlHours": 720,          "opTimeoutMs": 15000,          "items": {            "repository-token": {              "item": "Repository automation token",              "field": "credential",              "policy": "approve",              "description": "Token for repository automation",            },            "model-key": {              "item": "Model provider key",              "vault": "Agent credentials",              "policy": "auto",            },          },        },      },    },  },}
[/code]

Slugs verwenden Kleinbuchstaben, Zahlen und Bindestriche, beginnen mit einem Buchstaben oder einer Zahl und enthalten höchstens 64 Zeichen. Ein Register kann bis zu 32 Slugs enthalten; Beschreibungen können bis zu 200 Zeichen enthalten. `field` akzeptiert eine Feldbezeichnung oder ID, darf kein Komma enthalten und verwendet standardmäßig `credential`. Ein `vault` auf Elementebene überschreibt den Standardtresor. `opBin` kann einen absoluten Pfad zur ausführbaren Datei `op` festlegen; andernfalls löst das Plugin `op` aus `PATH` auf. Elementtitel dürfen nicht mit einem Bindestrich beginnen.

## Agenten-Tool verwenden

Der Tool-Name lautet `onepassword`.

Registrierte Slugs auflisten:

jsonCopy code
[code]
    { "action": "list" }
[/code]

Das Ergebnis enthält nur den Slug, die Beschreibung, die Richtlinie und die Angabe, ob eine dauerhafte Freigabe aktiv ist. Es enthält niemals einen Secret-Wert und fragt 1Password nicht ab.

Ein Secret anfordern:

jsonCopy code
[code]
    {  "action": "get",  "slug": "repository-token",  "reason": "Authenticate the requested repository operation"}
[/code]

`reason` ist erforderlich, darf nicht leer sein und ist auf 300 Zeichen begrenzt. Ein erfolgreicher `get` gibt den Wert sowie den konfigurierten Slug, den Elementtitel und die Feldbezeichnung zurück.

Das Tool-Schema deklariert außerdem einen internen Parameter `authorizationNonce`. Die Richtlinienebene injiziert ihn nach der Auswertung der Anfrage, um die Autorisierung an den ausgeführten Tool-Aufruf zu übergeben. Legen Sie ihn niemals manuell fest: Der Richtlinien-Hook überschreibt jeden angegebenen Wert, und ein unbekannter Wert führt zum Fehlschlagen der Anfrage.

## Richtlinienstufen und Genehmigungen

  * `auto`: sofort abrufen und die Anfrage auditieren.
  * `deny`: die Anfrage blockieren und auditieren.
  * `approve`: eine nicht abgelaufene dauerhafte Freigabe verwenden oder einen Menschen bitten, einmalig oder immer zu erlauben oder abzulehnen.


„Einmalig erlauben“ autorisiert nur den aktuellen Tool-Aufruf. „Immer erlauben“ schreibt eine dauerhafte Freigabe für diesen Agenten und Slug in SQLite; andere Agenten müssen ihre eigene Genehmigung erhalten. OpenClaw bietet „Immer erlauben“ nur an, wenn der Aufrufer eine konkrete Agentenidentität besitzt. Die Freigabe läuft nach `grantTtlHours` ab, standardmäßig nach 720 Stunden. Eine nicht beantwortete oder zeitüberschrittene Genehmigung lehnt die Anfrage ab; die maximale Wartezeit für eine Genehmigung beträgt 600 Sekunden. Das Plugin behält bis zu 1.024 dauerhafte Freigaben bei; bei Erreichen dieser Grenze wird die älteste Freigabe entfernt, und der zugehörige Agent muss den nächsten Zugriff genehmigen lassen.

Jede ausgewertete Autorisierung ist einmalig verwendbar und wird über den gemeinsam genutzten SQLite-Status an den ausgeführten Tool-Aufruf übergeben, sodass die Übergabe auch funktioniert, wenn mehr als eine Plugin-Instanz im Gateway-Prozess aktiv ist. Nicht verwendete Autorisierungen laufen nach dem 600-sekündigen Genehmigungsfenster ab.

Der In-Memory-Cache verwendet standardmäßig 300 Sekunden und ist durch das konfigurierte Slug-Register begrenzt. Setzen Sie `cacheTtlSeconds` auf `0`, um ihn zu deaktivieren. Die Richtlinie wird vor jedem Cache-Zugriff ausgewertet, und Cache-Treffer werden auditiert. Neuladungen der Laufzeitkonfiguration werden an jeder Richtlinien- und Ausführungsgrenze wirksam; das Deaktivieren des Plugins oder das Entfernen, Ablehnen oder Neuzuweisen eines Slugs macht ausstehende Autorisierungen und zwischengespeicherte Werte ungültig.

## Status und Audit-Verlauf prüfen

Bereitschaft und Registeranzahlen anzeigen:

bashCopy code
[code]
    openclaw onepassword status
[/code]

Dies meldet, ob die Token-Datei vorhanden ist, ob `op` aufgelöst wurde und unter welchem Pfad, die Anzahl der registrierten Elemente sowie die Anzahl pro Richtlinie. Das Token oder Secret-Werte werden niemals gelesen oder ausgegeben.

Die 50 neuesten Audit-Zeilen anzeigen:

bashCopy code
[code]
    openclaw onepassword auditopenclaw onepassword audit --limit 100
[/code]

Die Zeilen sind neueste zuerst sortiert und zeigen Zeitstempel, Agent, Slug, Ergebnis, einen `errorCode`, wenn der Versuch fehlgeschlagen ist, sowie einen gekürzten Grund. Der Grund wird wie angegeben gespeichert; der Broker fügt den abgerufenen Wert niemals zum Audit-Protokoll hinzu.

## Verhalten der 1Password-CLI

Jeder Cache-Fehltreffer führt `op item get` mit dem konfigurierten Element, Tresor und exakten Feldselektor, JSON-Ausgabe, einer begrenzten Zeitüberschreitung und `--cache=false` aus. Der untergeordnete Prozess erhält nur dieses Feld und nicht das vollständige Element. In der Umgebung des untergeordneten Prozesses sind nur `OP_SERVICE_ACCOUNT_TOKEN` und `HOME` vorhanden.

Das Plugin unternimmt einen Versuch. `RATE_LIMITED`-Fehler sollten behandelt werden, indem vor einer späteren Agentenanfrage gewartet wird; das Plugin erstellt keine automatische Wiederholungsschleife.

## Fehlercodes

Fehlgeschlagene Versuche enthalten einen geschlossenen Fehlercode im Tool-Ergebnis und in der Audit- Zeile.

1Password-Zugriffsfehler:

Code | Bedeutung  
---|---  
`TOKEN_MISSING` | Token-Datei fehlt oder ist leer  
`OP_NOT_FOUND` | `op`-Binärdatei konnte nicht aufgelöst werden  
`ITEM_NOT_FOUND` | Konfiguriertes Element befindet sich nicht im Tresor  
`FIELD_NOT_FOUND` | Konfiguriertes Feld befindet sich nicht im Element; verfügbare Bezeichnungen werden aufgelistet  
`RATE_LIMITED` | Ratenbegrenzung des 1Password-Dienstkontos wurde erreicht  
`AUTH_FAILED` | Authentifizierung des Dienstkontos ist fehlgeschlagen  
`TIMEOUT` | `op` hat `opTimeoutMs` überschritten  
`OP_ERROR` | Jeder andere `op`-Fehler oder ungültige Ausgabe  
  
Richtlinien- und Validierungsfehler:

Code | Bedeutung  
---|---  
`INVALID_ACTION`, `INVALID_REASON`, `INVALID_SLUG` | Eingabevalidierung der Anfrage ist fehlgeschlagen  
`UNKNOWN_SLUG` | Slug befindet sich nicht im konfigurierten Register  
`TOOL_CALL_ID_MISSING` | Aufruf ist ohne Tool-Aufruf-ID eingegangen  
`POLICY_NOT_EVALUATED` | Keine passende Autorisierung für diesen Aufruf; die Anfrage wurde nicht durch die Richtlinie genehmigt  
`POLICY_CHANGED` | Konfiguration wurde zwischen Genehmigung und Ausführung geändert  
`GRANT_EXPIRED` | Dauerhafte Freigabe ist vor der Ausführung abgelaufen  
`APPROVAL_CANCELLED` | Die Ausführung wurde abgebrochen, während die Genehmigung ausstand  
  
Was this useful?YesNo

Open issue
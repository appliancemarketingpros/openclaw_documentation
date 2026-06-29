---
title: SMS
source_url: https://docs.openclaw.ai/de/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw kann SMS über eine Twilio-Telefonnummer oder einen Messaging Service empfangen und senden. Der Gateway registriert eine eingehende Webhook-Route, validiert standardmäßig Twilio-Anforderungssignaturen und sendet Antworten über die Messages API von Twilio zurück.

[**Kopplung** Die Standard-DM-Richtlinie für SMS ist Kopplung. ](</de/channels/pairing>) [**Gateway-Sicherheit** Prüfen Sie die Webhook-Exposition und die Zugriffskontrollen für Absender. ](</de/gateway/security>) [**Channel-Fehlerbehebung** Kanalübergreifende Diagnosen und Reparatur-Playbooks. ](</de/channels/troubleshooting>)

## Bevor Sie beginnen

Sie benötigen:

  * Das offizielle SMS-Plugin, installiert mit `openclaw plugins install @openclaw/sms`.
  * Ein Twilio-Konto mit einer SMS-fähigen Telefonnummer oder einem Twilio Messaging Service.
  * Die Twilio Account SID und das Auth Token.
  * Eine öffentliche HTTPS-URL, die Ihren OpenClaw Gateway erreicht.
  * Eine Auswahl für die Absenderrichtlinie: `pairing` für private Nutzung, `allowlist` für vorab genehmigte Telefonnummern oder `open` nur für bewusst öffentlichen SMS-Zugriff.


Verwenden Sie eine Twilio-Nummer sowohl für SMS als auch Voice Call, wenn die Nummer beide Funktionen unterstützt. Konfigurieren Sie den SMS-Webhook und den Voice-Webhook separat in Twilio; diese Seite behandelt nur den SMS-Webhook.

## Schnelleinrichtung

* ### Plugin installieren

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Twilio-Absender erstellen oder auswählen

Öffnen Sie in Twilio **Phone Numbers > Manage > Active numbers** und wählen Sie eine SMS-fähige Nummer aus. Speichern Sie:

  * Account SID, zum Beispiel `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Absender-Telefonnummer, zum Beispiel `+15551234567`


Wenn Sie statt einer festen Absendernummer einen Messaging Service verwenden, speichern Sie die Messaging Service SID, zum Beispiel `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### SMS-Channel konfigurieren

Speichern Sie dies als `sms.patch.json5` und ändern Sie die Platzhalter:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Wenden Sie es an:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Twilio auf den Gateway-Webhook verweisen

Öffnen Sie in den Twilio-Telefonnummerneinstellungen **Messaging** und setzen Sie **A message comes in** auf:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

Verwenden Sie HTTP `POST`. Der standardmäßige lokale Pfad ist `/webhooks/sms`; ändern Sie `channels.sms.webhookPath`, wenn Sie eine andere Route benötigen.

* ### Den genauen SMS-Webhook-Pfad bereitstellen

Ihre öffentliche URL muss den SMS-Pfad an den Gateway-Prozess weiterleiten. Wenn Sie Tailscale Funnel für lokale Tests verwenden, stellen Sie `/webhooks/sms` explizit bereit:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Voice Call und SMS verwenden separate Webhook-Pfade. Wenn dieselbe Twilio-Nummer beides verarbeitet, lassen Sie beide Routen in Twilio und in Ihrem Tunnel konfiguriert.

* ### Gateway starten und ersten Absender genehmigen

bashCopy code
[code]
    openclaw gateway
[/code]

Senden Sie eine Textnachricht an die Twilio-Nummer. Die erste Nachricht erstellt eine Kopplungsanfrage. Genehmigen Sie sie:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

Kopplungscodes laufen nach 1 Stunde ab.

## Konfigurationsbeispiele

### Konfigurationsdatei

Verwenden Sie die Einrichtung per Konfigurationsdatei, wenn die Channel-Definition mit der Gateway-Konfiguration übertragen werden soll:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Umgebungsvariablen

Verwenden Sie die Einrichtung per Umgebungsvariablen für Bereitstellungen mit einem einzelnen Konto, bei denen Geheimnisse aus der Host-Umgebung kommen:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Aktivieren Sie anschließend den Channel in der Konfiguration:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM` wird als Alias für `TWILIO_PHONE_NUMBER` akzeptiert. Verwenden Sie `TWILIO_MESSAGING_SERVICE_SID` statt eines Telefonnummer-Absenders, wenn Twilio den Absender aus einem Messaging Service auswählen soll.

### SecretRef-Auth-Token

`authToken` kann eine SecretRef sein. Verwenden Sie dies, wenn der Gateway das Twilio Auth Token aus der OpenClaw-Secrets-Runtime auflösen soll, statt Klartext-Konfiguration zu speichern:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Die referenzierte Umgebungsvariable oder der Secret-Provider muss für die Gateway-Runtime sichtbar sein. Starten Sie verwaltete Gateway-Prozesse nach Änderungen an Host-Umgebungsvariablen neu.

### Private Nummer nur per Allowlist

Verwenden Sie `allowlist`, wenn nur bekannte Telefonnummern mit dem Agent sprechen dürfen:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Messaging Service-Absender

Verwenden Sie `messagingServiceSid` statt `fromNumber`, wenn Twilio den Absender über einen Messaging Service auswählen soll:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Wenn nach der Auflösung von Konfiguration und Umgebungsvariablen sowohl `fromNumber` als auch `messagingServiceSid` vorhanden sind, wird `fromNumber` verwendet.

### Standardziel für ausgehende Nachrichten

Setzen Sie `defaultTo`, wenn Automatisierung oder vom Agent initiierte Zustellung ein Standardziel haben soll, falls ein Sendeablauf kein explizites Ziel angibt:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Zugriffskontrolle

`channels.sms.dmPolicy` steuert den direkten SMS-Zugriff:

  * `pairing` (Standard)
  * `allowlist` (erfordert mindestens einen Absender in `allowFrom`)
  * `open` (erfordert, dass `allowFrom` `"*"` enthält)
  * `disabled`


`allowFrom`-Einträge sollten E.164-Telefonnummern wie `+15551234567` sein. `sms:`-Präfixe werden akzeptiert und normalisiert. Für einen privaten Assistant bevorzugen Sie `dmPolicy: "allowlist"` mit expliziten Telefonnummern.

## SMS senden

Ausgehende SMS-Ziele verwenden den Service-Präfix `sms:` mit ausgewähltem SMS-Channel:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Wenn die Channel-Auswahl implizit ist, wählt `twilio-sms:+15551234567` diesen Channel aus, ohne den vorhandenen channel-eigenen Service-Präfix `sms:` zu übernehmen, der von iMessage verwendet wird.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

Die CLI erfordert ein explizites `--target`. `defaultTo` ist für Automatisierungs- und vom Agent initiierte Zustellpfade vorgesehen, bei denen das Ziel aus der Channel-Konfiguration aufgelöst werden kann.

Agent-Antworten aus eingehenden SMS-Unterhaltungen gehen automatisch über den konfigurierten Twilio-Absender an den Absender zurück.

SMS-Ausgabe ist Klartext. OpenClaw entfernt Markdown, flacht eingezäunte Codeblöcke ab, erhält lesbare Links und teilt lange Antworten in Abschnitte auf, bevor sie über Twilio gesendet werden.

## Einrichtung überprüfen

Nachdem der Gateway gestartet ist:

  1. Bestätigen Sie, dass das Gateway-Protokoll die SMS-Webhook-Route anzeigt.
  2. Führen Sie eine Twilio-seitige Prüfung aus:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Senden Sie von Ihrem Telefon eine SMS an die Twilio-Nummer.
  4. Führen Sie `openclaw pairing list sms` aus.
  5. Genehmigen Sie den Kopplungscode mit `openclaw pairing approve sms &lt;CODE&gt;`.
  6. Senden Sie eine weitere SMS und bestätigen Sie, dass der Agent antwortet.


Für Tests nur ausgehender Nachrichten verwenden Sie:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### End-to-End-Test aus macOS iMessage/SMS

Auf einem Mac, der über Messages Mobilfunk-SMS senden kann, können Sie `imsg` verwenden, um die Absenderseite zu steuern, ohne Ihr Telefon zu verwenden:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

Die erste Nachricht sollte eine Kopplungsanfrage erstellen. Die zweite Nachricht sollte die Agent-Antwort über Twilio erhalten.

## Webhook-Sicherheit

Standardmäßig validiert OpenClaw `X-Twilio-Signature` mit `publicWebhookUrl` und `authToken`. Halten Sie `publicWebhookUrl` Byte für Byte mit der in Twilio konfigurierten URL abgestimmt, einschließlich Schema, Host, Pfad und Abfragezeichenfolge.

Nur für lokale Tunneltests können Sie setzen:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Verwenden Sie deaktivierte Signaturvalidierung nicht auf einem öffentlichen Gateway.

## Konfiguration für mehrere Konten

Verwenden Sie `accounts`, wenn Sie mehr als eine Twilio-Nummer betreiben:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Jedes Konto sollte einen eindeutigen `webhookPath` verwenden.

## Fehlerbehebung

### Twilio gibt 403 zurück oder OpenClaw weist den Webhook zurück

Prüfen Sie, dass `publicWebhookUrl` genau mit der in Twilio konfigurierten URL übereinstimmt, einschließlich Schema, Host, Pfad und Abfragezeichenfolge. Twilio signiert die öffentliche URL-Zeichenfolge, daher können Proxy-Umschreibungen und alternative Hostnamen die Signaturvalidierung unterbrechen.

### Es erscheint keine Kopplungsanfrage

Prüfen Sie die **Messaging** -Webhook-URL und -Methode der Twilio-Nummer. Sie muss auf die SMS-Webhook-URL zeigen und `POST` verwenden. Bestätigen Sie außerdem, dass der Gateway aus dem öffentlichen Internet oder über Ihren Tunnel erreichbar ist.

Wenn das Twilio-Nachrichtenprotokoll den Fehler `11200` anzeigt, hat Twilio die eingehende SMS akzeptiert, konnte Ihren Webhook aber nicht erreichen. Prüfen Sie:

  * Twilio **Messaging > A message comes in** zeigt auf `publicWebhookUrl`.
  * Die Methode ist `POST`.
  * Der Tunnel oder Reverse Proxy stellt den genauen `webhookPath` bereit; führen Sie für Tailscale Funnel `tailscale funnel status` aus und bestätigen Sie, dass `/webhooks/sms` aufgeführt ist.
  * `publicWebhookUrl` verwendet dasselbe Schema, denselben Host, denselben Pfad und dieselbe Abfragezeichenfolge, die Twilio sendet, damit die Signaturvalidierung die signierte URL reproduzieren kann.


### Ausgehende Sendungen schlagen fehl

Bestätigen Sie, dass `accountSid`, `authToken` und entweder `fromNumber` oder `messagingServiceSid` aufgelöst werden. Wenn Sie ein Twilio-Testkonto verwenden, muss die Zielnummer möglicherweise in Twilio verifiziert werden, bevor ausgehende SMS gesendet werden.

### Nachrichten kommen an, aber der Agent antwortet nicht

Prüfen Sie `dmPolicy` und `allowFrom`. Bei der standardmäßigen Richtlinie `pairing` muss der Absender genehmigt sein, bevor normale Agent-Durchläufe verarbeitet werden.

Was this useful?YesNo

Open issue
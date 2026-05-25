---
title: Andocken von Kanälen
source_url: https://docs.openclaw.ai/de/concepts/channel-docking
scraped_at: 2026-05-25
---

Channel-Docking ist Anrufweiterleitung für eine OpenClaw-Sitzung.

Es behält denselben Unterhaltungskontext bei, ändert aber, wohin zukünftige Antworten für diese Sitzung zugestellt werden.

## Beispiel

Alice kann OpenClaw über Telegram und Discord eine Nachricht senden:

json5Copy code
[code]
    {  session: {    identityLinks: {      alice: ["telegram:123", "discord:456"],    },  },}
[/code]

Wenn Alice dies von Telegram sendet:

textCopy code
[code]
    /dock_discord
[/code]

OpenClaw behält den aktuellen Sitzungskontext bei und ändert die Antwortroute:

Vor dem Docking | Nach `/dock_discord`  
---|---  
Antworten gehen an Telegram `123` | Antworten gehen an Discord `456`  
  
Die Sitzung wird nicht neu erstellt. Der Transkriptverlauf bleibt an dieselbe Sitzung angehängt.

## Warum verwenden

Verwenden Sie Docking, wenn eine Aufgabe in einer Chat-App beginnt, die nächsten Antworten aber an einem anderen Ort ankommen sollen.

Typischer Ablauf:

  1. Starten Sie eine Agent-Aufgabe von Telegram.
  2. Wechseln Sie zu Discord, wo Sie die Arbeit koordinieren.
  3. Senden Sie `/dock_discord` aus der Telegram-Sitzung.
  4. Behalten Sie dieselbe OpenClaw-Sitzung bei, empfangen Sie zukünftige Antworten aber in Discord.


## Erforderliche Konfiguration

Docking erfordert `session.identityLinks`. Der Quellabsender und der Ziel-Peer müssen sich in derselben Identitätsgruppe befinden:

json5Copy code
[code]
    {  session: {    identityLinks: {      alice: ["telegram:123", "discord:456", "slack:U123"],    },  },}
[/code]

Die Werte sind kanalpräfixierte Peer-IDs:

Wert | Bedeutung  
---|---  
`telegram:123` | Telegram-Absender-ID `123`  
`discord:456` | Discord-Direkt-Peer-ID `456`  
`slack:U123` | Slack-Benutzer-ID `U123`  
  
Der kanonische Schlüssel (`alice` oben) ist nur der gemeinsame Name der Identitätsgruppe. Dock-Befehle verwenden die kanalpräfixierten Werte, um nachzuweisen, dass der Quellabsender und der Ziel-Peer dieselbe Person sind.

## Befehle

Dock-Befehle werden aus geladenen Kanal-Plugins generiert, die native Befehle unterstützen. Aktuelle gebündelte Befehle:

Zielkanal | Befehl | Alias  
---|---|---  
Discord | `/dock-discord` | `/dock_discord`  
Mattermost | `/dock-mattermost` | `/dock_mattermost`  
Slack | `/dock-slack` | `/dock_slack`  
Telegram | `/dock-telegram` | `/dock_telegram`  
  
Die Unterstrich-Aliasse sind auf nativen Befehlsoberflächen wie Telegram nützlich.

## Was sich ändert

Docking aktualisiert die Zustellfelder der aktiven Sitzung:

Sitzungsfeld | Beispiel nach `/dock_discord`  
---|---  
`lastChannel` | `discord`  
`lastTo` | `456`  
`lastAccountId` | das Zielkanal-Konto oder `default`  
  
Diese Felder werden im Sitzungsspeicher persistiert und von der späteren Antwortzustellung für diese Sitzung verwendet.

## Was sich nicht ändert

Docking bewirkt nicht Folgendes:

  * Kanalkonten erstellen
  * einen neuen Discord-, Telegram-, Slack- oder Mattermost-Bot verbinden
  * einem Benutzer Zugriff gewähren
  * Kanal-Allowlists oder DM-Richtlinien umgehen
  * Transkriptverlauf in eine andere Sitzung verschieben
  * dafür sorgen, dass nicht zusammengehörige Benutzer eine Sitzung teilen


Es ändert nur die Zustellroute für die aktuelle Sitzung.

## Fehlerbehebung

**Der Befehl meldet, dass der Absender nicht verknüpft ist.**

Fügen Sie sowohl den aktuellen Absender als auch den Ziel-Peer derselben `session.identityLinks`-Gruppe hinzu. Wenn beispielsweise Telegram-Absender `123` zu Discord-Peer `456` docken soll, nehmen Sie sowohl `telegram:123` als auch `discord:456` auf.

**Der Befehl meldet, dass keine aktive Sitzung vorhanden ist.**

Docken Sie aus einer bestehenden Direktchat-Sitzung. Der Befehl benötigt einen aktiven Sitzungseintrag, damit er die neue Route persistieren kann.

**Antworten gehen weiterhin an den alten Kanal.**

Prüfen Sie, ob der Befehl mit einer Erfolgsmeldung geantwortet hat, und bestätigen Sie, dass die Ziel-Peer-ID mit der von diesem Kanal verwendeten ID übereinstimmt. Docking ändert nur die Route der aktiven Sitzung; eine andere Sitzung kann weiterhin anderswohin routen.

**Ich muss zurückwechseln.**

Senden Sie den passenden Befehl für den ursprünglichen Kanal, z. B. `/dock_telegram` oder `/dock-telegram`, von einem verknüpften Absender.

Was this useful?YesNo
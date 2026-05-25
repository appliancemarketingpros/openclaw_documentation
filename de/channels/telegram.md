---
title: Telegram
source_url: https://docs.openclaw.ai/de/channels/telegram
scraped_at: 2026-05-25
---

Einsatzbereit für Bot-DMs und Gruppen über grammY. Long Polling ist der Standardmodus; der Webhook-Modus ist optional.

[**Kopplung** Die Standard-DM-Richtlinie für Telegram ist Kopplung. ](</de/channels/pairing>) [**Kanal-Problembehandlung** Kanalübergreifende Diagnosen und Reparatur-Playbooks. ](</de/channels/troubleshooting>) [**Gateway-Konfiguration** Vollständige Kanalkonfigurationsmuster und Beispiele. ](</de/gateway/configuration>)

## Schnelle Einrichtung

* ### Bot-Token in BotFather erstellen

Öffnen Sie Telegram und chatten Sie mit **@BotFather** (bestätigen Sie, dass der Handle genau `@BotFather` ist).

Führen Sie `/newbot` aus, folgen Sie den Eingabeaufforderungen und speichern Sie das Token.

* ### Token und DM-Richtlinie konfigurieren

json5Copy code
[code]
    {channels: {telegram: {  enabled: true,  botToken: "123:abc",  dmPolicy: "pairing",  groups: { "*": { requireMention: true } },},},}
[/code]

Env-Fallback: `TELEGRAM_BOT_TOKEN=...` (nur Standardkonto). Telegram verwendet **nicht** `openclaw channels login telegram`; konfigurieren Sie das Token in der Konfiguration/Env und starten Sie dann das Gateway.

* ### Gateway starten und erste DM genehmigen

bashCopy code
[code]
    openclaw gatewayopenclaw pairing list telegramopenclaw pairing approve telegram &lt;CODE&gt;
[/code]

Kopplungscodes laufen nach 1 Stunde ab.

* ### Bot zu einer Gruppe hinzufügen

Fügen Sie den Bot Ihrer Gruppe hinzu und ermitteln Sie dann beide IDs, die der Gruppenzugriff benötigt:

  * Ihre Telegram-Benutzer-ID, verwendet in `allowFrom` / `groupAllowFrom`
  * die Telegram-Gruppenchat-ID, verwendet als Schlüssel unter `channels.telegram.groups`


Für die Ersteinrichtung erhalten Sie die Gruppenchat-ID aus `openclaw logs --follow`, einem Bot für weitergeleitete IDs oder über Bot API `getUpdates`. Nachdem die Gruppe zugelassen wurde, kann `/whoami@<bot_username>` die Benutzer- und Gruppen-IDs bestätigen.

Negative Telegram-Supergruppen-IDs, die mit `-100` beginnen, sind Gruppenchat-IDs. Setzen Sie sie unter `channels.telegram.groups`, nicht unter `groupAllowFrom`.

## Telegram-seitige Einstellungen

Datenschutzmodus und Gruppensichtbarkeit

Telegram-Bots verwenden standardmäßig den **Privacy Mode** , der begrenzt, welche Gruppennachrichten sie empfangen.

Wenn der Bot alle Gruppennachrichten sehen muss, entweder:

  * deaktivieren Sie den Datenschutzmodus über `/setprivacy`, oder
  * machen Sie den Bot zum Gruppenadministrator.


Wenn Sie den Datenschutzmodus umschalten, entfernen Sie den Bot in jeder Gruppe und fügen Sie ihn erneut hinzu, damit Telegram die Änderung anwendet.

Gruppenberechtigungen

Der Administratorstatus wird in den Telegram-Gruppeneinstellungen gesteuert.

Administrator-Bots empfangen alle Gruppennachrichten, was für dauerhaft aktives Gruppenverhalten nützlich ist.

Hilfreiche BotFather-Schalter

  * `/setjoingroups`, um das Hinzufügen zu Gruppen zuzulassen/zu verweigern
  * `/setprivacy` für das Verhalten der Gruppensichtbarkeit


## Zugriffskontrolle und Aktivierung

### DM-Richtlinie

`channels.telegram.dmPolicy` steuert den Zugriff auf Direktnachrichten:

  * `pairing` (Standard)
  * `allowlist` (erfordert mindestens eine Sender-ID in `allowFrom`)
  * `open` (erfordert, dass `allowFrom` `"*"` enthält)
  * `disabled`


`dmPolicy: "open"` mit `allowFrom: ["*"]` erlaubt jedem Telegram-Konto, das den Bot-Benutzernamen findet oder errät, den Bot zu steuern. Verwenden Sie dies nur für absichtlich öffentliche Bots mit stark eingeschränkten Tools; Bots mit einem Eigentümer sollten `allowlist` mit numerischen Benutzer-IDs verwenden.

`channels.telegram.allowFrom` akzeptiert numerische Telegram-Benutzer-IDs. Präfixe `telegram:` / `tg:` werden akzeptiert und normalisiert. In Mehrkonten-Konfigurationen wird ein restriktives `channels.telegram.allowFrom` auf oberster Ebene als Sicherheitsgrenze behandelt: `allowFrom: ["*"]`-Einträge auf Kontoebene machen dieses Konto nicht öffentlich, es sei denn, die effektive Konto-Allowlist enthält nach dem Zusammenführen weiterhin einen expliziten Platzhalter. `dmPolicy: "allowlist"` mit leerem `allowFrom` blockiert alle DMs und wird von der Konfigurationsvalidierung abgelehnt. Die Einrichtung fragt nur nach numerischen Benutzer-IDs. Wenn Sie ein Upgrade durchgeführt haben und Ihre Konfiguration `@username`-Allowlist-Einträge enthält, führen Sie `openclaw doctor --fix` aus, um sie aufzulösen (Best-Effort; erfordert ein Telegram-Bot-Token). Wenn Sie zuvor auf Allowlist-Dateien aus dem Kopplungsspeicher vertraut haben, kann `openclaw doctor --fix` Einträge in Allowlist-Flows nach `channels.telegram.allowFrom` wiederherstellen (zum Beispiel, wenn `dmPolicy: "allowlist"` noch keine expliziten IDs hat).

Für Bots mit einem Eigentümer bevorzugen Sie `dmPolicy: "allowlist"` mit expliziten numerischen `allowFrom`-IDs, damit die Zugriffsrichtlinie dauerhaft in der Konfiguration liegt (statt von früheren Kopplungsgenehmigungen abhängig zu sein).

Häufige Verwirrung: Die Genehmigung einer DM-Kopplung bedeutet nicht „dieser Sender ist überall autorisiert“. Die Kopplung gewährt DM-Zugriff. Wenn noch kein Befehlseigentümer existiert, setzt die erste genehmigte Kopplung außerdem `commands.ownerAllowFrom`, sodass nur für Eigentümer verfügbare Befehle und Ausführungsgenehmigungen ein explizites Betreiberkonto haben. Die Autorisierung von Gruppensendern stammt weiterhin aus expliziten Konfigurations-Allowlists. Wenn Sie möchten, dass „ich einmal autorisiert bin und sowohl DMs als auch Gruppenbefehle funktionieren“, setzen Sie Ihre numerische Telegram-Benutzer-ID in `channels.telegram.allowFrom`; stellen Sie für nur Eigentümern vorbehaltene Befehle sicher, dass `commands.ownerAllowFrom` `telegram:<your user id>` enthält.

### Ihre Telegram-Benutzer-ID finden

Sicherer (kein Drittanbieter-Bot):

  1. Senden Sie Ihrem Bot eine DM.
  2. Führen Sie `openclaw logs --follow` aus.
  3. Lesen Sie `from.id`.


Offizielle Bot API-Methode:

bashCopy code
[code]
    curl "https://api.telegram.org/bot<bot_token>/getUpdates"
[/code]

Drittanbieter-Methode (weniger privat): `@userinfobot` oder `@getidsbot`.

### Gruppenrichtlinie und Allowlists

Zwei Steuerungen gelten zusammen:

  1. **Welche Gruppen zugelassen sind** (`channels.telegram.groups`)

     * keine `groups`-Konfiguration: 
       * mit `groupPolicy: "open"`: Jede Gruppe kann Gruppen-ID-Prüfungen bestehen
       * mit `groupPolicy: "allowlist"` (Standard): Gruppen werden blockiert, bis Sie `groups`-Einträge (oder `"*"`) hinzufügen
     * `groups` konfiguriert: fungiert als Allowlist (explizite IDs oder `"*"`)
  2. **Welche Sender in Gruppen zugelassen sind** (`channels.telegram.groupPolicy`)

     * `open`
     * `allowlist` (Standard)
     * `disabled`


`groupAllowFrom` wird für die Filterung von Gruppensendern verwendet. Wenn nicht gesetzt, fällt Telegram auf `allowFrom` zurück. `groupAllowFrom`-Einträge sollten numerische Telegram-Benutzer-IDs sein (`telegram:` / `tg:`-Präfixe werden normalisiert). Setzen Sie keine Telegram-Gruppen- oder Supergruppen-Chat-IDs in `groupAllowFrom`. Negative Chat-IDs gehören unter `channels.telegram.groups`. Nicht numerische Einträge werden für die Senderautorisierung ignoriert. Sicherheitsgrenze (`2026.2.25+`): Die Authentifizierung von Gruppensendern erbt **keine** Genehmigungen aus dem DM-Kopplungsspeicher. Kopplung bleibt nur für DMs. Für Gruppen setzen Sie `groupAllowFrom` oder `allowFrom` pro Gruppe/pro Thema. Wenn `groupAllowFrom` nicht gesetzt ist, fällt Telegram auf die Konfiguration `allowFrom` zurück, nicht auf den Kopplungsspeicher. Praktisches Muster für Bots mit einem Eigentümer: Setzen Sie Ihre Benutzer-ID in `channels.telegram.allowFrom`, lassen Sie `groupAllowFrom` ungesetzt und lassen Sie die Zielgruppen unter `channels.telegram.groups` zu. Laufzeithinweis: Wenn `channels.telegram` vollständig fehlt, verwendet die Laufzeit standardmäßig das fehlersichere `groupPolicy="allowlist"`, sofern `channels.defaults.groupPolicy` nicht explizit gesetzt ist.

Gruppeneinrichtung nur für Eigentümer:

json5Copy code
[code]
    {channels: {telegram: {  enabled: true,  dmPolicy: "pairing",  allowFrom: ["&lt;YOUR_TELEGRAM_USER_ID&gt;"],  groupPolicy: "allowlist",  groups: {    "&lt;GROUP_CHAT_ID&gt;": {      requireMention: true,    },  },},},}
[/code]

Testen Sie es aus der Gruppe mit `@<bot_username> ping`. Einfache Gruppennachrichten lösen den Bot nicht aus, solange `requireMention: true`.

Beispiel: beliebiges Mitglied in einer bestimmten Gruppe zulassen:

json5Copy code
[code]
    {channels: {telegram: {  groups: {    "-1001234567890": {      groupPolicy: "open",      requireMention: false,    },  },},},}
[/code]

Beispiel: nur bestimmte Benutzer innerhalb einer bestimmten Gruppe zulassen:

json5Copy code
[code]
    {channels: {telegram: {  groups: {    "-1001234567890": {      requireMention: true,      allowFrom: ["8734062810", "745123456"],    },  },},},}
[/code]

### Erwähnungsverhalten

Gruppenantworten erfordern standardmäßig eine Erwähnung.

Die Erwähnung kann stammen von:

  * nativer `@botusername`-Erwähnung oder
  * Erwähnungsmustern in: 
    * `agents.list[].groupChat.mentionPatterns`
    * `messages.groupChat.mentionPatterns`


Sitzungsbezogene Befehlsschalter:

  * `/activation always`
  * `/activation mention`


Diese aktualisieren nur den Sitzungsstatus. Verwenden Sie die Konfiguration für Persistenz.

Beispiel für persistente Konfiguration:

json5Copy code
[code]
    {channels: {telegram: {  groups: {    "*": { requireMention: false },  },},},}
[/code]

Gruppenchat-ID abrufen:

  * eine Gruppennachricht an `@userinfobot` / `@getidsbot` weiterleiten
  * oder `chat.id` aus `openclaw logs --follow` lesen
  * oder Bot API `getUpdates` prüfen
  * nachdem die Gruppe zugelassen wurde, `/whoami@<bot_username>` ausführen, wenn native Befehle aktiviert sind


## Laufzeitverhalten

  * Telegram gehört dem Gateway-Prozess.
  * Das Routing ist deterministisch: Telegram-Eingänge antworten zurück an Telegram (das Modell wählt keine Kanäle aus).
  * Eingehende Nachrichten werden in den gemeinsamen Kanal-Umschlag mit Antwortmetadaten, Medienplatzhaltern und persistiertem Antwortkettenkontext für Telegram-Antworten normalisiert, die das Gateway beobachtet hat.
  * Gruppensitzungen sind nach Gruppen-ID isoliert. Forumthemen hängen `:topic:<threadId>` an, um Themen isoliert zu halten.
  * DM-Nachrichten können `message_thread_id` enthalten; OpenClaw bewahrt die Thread-ID für Antworten, hält DMs aber standardmäßig in der flachen Sitzung. Konfigurieren Sie `channels.telegram.dm.threadReplies: "inbound"`, `channels.telegram.direct.<chatId>.threadReplies: "inbound"`, `requireTopic: true` oder eine passende Themenkonfiguration, wenn Sie bewusst eine DM-Themensitzungsisolierung wünschen.
  * Long Polling verwendet den grammY Runner mit Sequenzierung pro Chat/pro Thread. Die gesamte Runner-Sink-Parallelität verwendet `agents.defaults.maxConcurrent`.
  * Long Polling ist innerhalb jedes Gateway-Prozesses abgesichert, sodass jeweils nur ein aktiver Poller ein Bot-Token verwenden kann. Wenn Sie weiterhin `getUpdates`-409-Konflikte sehen, verwendet wahrscheinlich ein anderes OpenClaw-Gateway, Skript oder ein externer Poller dasselbe Token.
  * Neustarts des Long-Polling-Watchdogs werden standardmäßig nach 120 Sekunden ohne abgeschlossene `getUpdates`-Liveness ausgelöst. Erhöhen Sie `channels.telegram.pollingStallThresholdMs` nur, wenn Ihre Bereitstellung während lang laufender Arbeit weiterhin fälschliche Polling-Stall-Neustarts sieht. Der Wert ist in Millisekunden angegeben und von `30000` bis `600000` zulässig; Überschreibungen pro Konto werden unterstützt.
  * Telegram Bot API unterstützt keine Lesebestätigungen (`sendReadReceipts` gilt nicht).


## Funktionsreferenz

Live-Stream-Vorschau (Nachrichtenbearbeitungen)

OpenClaw kann Teilantworten in Echtzeit streamen:

  * Direktchats: Vorschaunachricht + `editMessageText`
  * Gruppen/Themen: Vorschaunachricht + `editMessageText`


Anforderung:

  * `channels.telegram.streaming` ist `off | partial | block | progress` (Standard: `partial`)
  * `progress` behält einen bearbeitbaren Statusentwurf für Tool-Fortschritt bei, löscht ihn nach Abschluss und sendet die finale Antwort als normale Nachricht
  * `streaming.preview.toolProgress` steuert, ob Tool-/Fortschrittsaktualisierungen dieselbe bearbeitete Vorschau-Nachricht wiederverwenden (Standard: `true`, wenn Vorschau-Streaming aktiv ist)
  * `streaming.preview.commandText` steuert Befehls-/Ausführungsdetails in diesen Tool-Fortschrittszeilen: `raw` (Standard, bewahrt das veröffentlichte Verhalten) oder `status` (nur Tool-Bezeichnung)
  * veraltete Werte für `channels.telegram.streamMode` und boolesche `streaming`-Werte werden erkannt; führen Sie `openclaw doctor --fix` aus, um sie nach `channels.telegram.streaming.mode` zu migrieren


Tool-Fortschrittsvorschau-Aktualisierungen sind die kurzen Statuszeilen, die während der Ausführung von Tools angezeigt werden, zum Beispiel Befehlsausführung, Dateilesevorgänge, Planungsaktualisierungen oder Patch-Zusammenfassungen. Telegram lässt diese standardmäßig aktiviert, um dem veröffentlichten OpenClaw-Verhalten ab `v2026.4.22` zu entsprechen. Um die bearbeitete Vorschau für Antworttext beizubehalten, aber Tool-Fortschrittszeilen auszublenden, legen Sie Folgendes fest:

jsonCopy code
[code]
    {  "channels": {    "telegram": {      "streaming": {        "mode": "partial",        "preview": {          "toolProgress": false        }      }    }  }}
[/code]

Um Tool-Fortschritt sichtbar zu lassen, aber Befehls-/Ausführungstext auszublenden, legen Sie Folgendes fest:

jsonCopy code
[code]
    {  "channels": {    "telegram": {      "streaming": {        "mode": "partial",        "preview": {          "commandText": "status"        }      }    }  }}
[/code]

Verwenden Sie den Modus `progress`, wenn Sie sichtbaren Tool-Fortschritt wünschen, ohne die finale Antwort in dieselbe Nachricht hineinzubearbeiten. Legen Sie die Richtlinie für Befehlstext unter `streaming.progress` ab:

jsonCopy code
[code]
    {  "channels": {    "telegram": {      "streaming": {        "mode": "progress",        "progress": {          "toolProgress": true,          "commandText": "status"        }      }    }  }}
[/code]

Verwenden Sie `streaming.mode: "off"` nur, wenn Sie ausschließlich finale Zustellung wünschen: Telegram-Vorschaubearbeitungen werden deaktiviert und generisches Tool-/Fortschrittsgerede wird unterdrückt, statt als eigenständige Statusnachrichten gesendet zu werden. Genehmigungsaufforderungen, Medien-Payloads und Fehler werden weiterhin über die normale finale Zustellung geleitet. Verwenden Sie `streaming.preview.toolProgress: false`, wenn Sie nur Antwortvorschau-Bearbeitungen beibehalten und zugleich die Tool-Fortschrittsstatuszeilen ausblenden möchten.

Für reine Textantworten:

  * kurze DM-/Gruppen-/Themenvorschauen: OpenClaw behält dieselbe Vorschau-Nachricht bei und führt die finale Bearbeitung direkt daran aus
  * lange finale Texte, die in mehrere Telegram-Nachrichten aufgeteilt werden, verwenden die vorhandene Vorschau nach Möglichkeit als ersten finalen Abschnitt wieder und senden danach nur die verbleibenden Abschnitte
  * Finale Antworten im Fortschrittsmodus löschen den Statusentwurf und verwenden normale finale Zustellung, statt den Entwurf zur Antwort umzubearbeiten
  * wenn die finale Bearbeitung fehlschlägt, bevor der vollständige Text bestätigt ist, verwendet OpenClaw normale finale Zustellung und bereinigt die veraltete Vorschau


Bei komplexen Antworten (zum Beispiel Medien-Payloads) fällt OpenClaw auf normale finale Zustellung zurück und bereinigt anschließend die Vorschau-Nachricht.

Vorschau-Streaming ist von Block-Streaming getrennt. Wenn Block-Streaming für Telegram explizit aktiviert ist, überspringt OpenClaw den Vorschau-Stream, um doppeltes Streaming zu vermeiden.

Reiner Telegram-Reasoning-Stream:

  * `/reasoning stream` sendet Reasoning während der Generierung an die Live-Vorschau
  * die Reasoning-Vorschau wird nach der finalen Zustellung gelöscht; verwenden Sie `/reasoning on`, wenn Reasoning sichtbar bleiben soll
  * die finale Antwort wird ohne Reasoning-Text gesendet

Formatting and HTML fallback

Ausgehender Text verwendet Telegram `parse_mode: "HTML"`.

  * Markdown-ähnlicher Text wird in Telegram-sicheres HTML gerendert.
  * Unterstützte Telegram-HTML-Tags bleiben erhalten; nicht unterstütztes HTML wird escaped.
  * Wenn Telegram geparstes HTML ablehnt, versucht OpenClaw es erneut als Klartext.


Linkvorschauen sind standardmäßig aktiviert und können mit `channels.telegram.linkPreview: false` deaktiviert werden.

Native commands and custom commands

Die Registrierung des Telegram-Befehlsmenüs wird beim Start mit `setMyCommands` gehandhabt.

Standardwerte für native Befehle:

  * `commands.native: "auto"` aktiviert native Befehle für Telegram


Benutzerdefinierte Einträge im Befehlsmenü hinzufügen:

json5Copy code
[code]
    {channels: {telegram: {  customCommands: [    { command: "backup", description: "Git backup" },    { command: "generate", description: "Create an image" },  ],},},}
[/code]

Regeln:

  * Namen werden normalisiert (führendes `/` entfernen, Kleinschreibung)
  * gültiges Muster: `a-z`, `0-9`, `_`, Länge `1..32`
  * benutzerdefinierte Befehle können native Befehle nicht überschreiben
  * Konflikte/Duplikate werden übersprungen und protokolliert


Hinweise:

  * benutzerdefinierte Befehle sind nur Menüeinträge; sie implementieren kein Verhalten automatisch
  * Plugin-/Skill-Befehle können weiterhin funktionieren, wenn sie eingegeben werden, auch wenn sie nicht im Telegram-Menü angezeigt werden


Wenn native Befehle deaktiviert sind, werden integrierte Befehle entfernt. Benutzerdefinierte/Plugin-Befehle können weiterhin registriert werden, wenn sie konfiguriert sind.

Häufige Einrichtungsfehler:

  * `setMyCommands failed` mit `BOT_COMMANDS_TOO_MUCH` bedeutet, dass das Telegram-Menü auch nach dem Kürzen noch überlaufen ist; reduzieren Sie Plugin-/Skill-/benutzerdefinierte Befehle oder deaktivieren Sie `channels.telegram.commands.native`.
  * Wenn `deleteWebhook`, `deleteMyCommands` oder `setMyCommands` mit `404: Not Found` fehlschlägt, während direkte Bot-API-`curl`-Befehle funktionieren, kann das bedeuten, dass `channels.telegram.apiRoot` auf den vollständigen `/bot&lt;TOKEN&gt;`-Endpunkt gesetzt wurde. `apiRoot` darf nur die Bot-API-Wurzel sein, und `openclaw doctor --fix` entfernt ein versehentlich angehängtes `/bot&lt;TOKEN&gt;`.
  * `getMe returned 401` bedeutet, dass Telegram das konfigurierte Bot-Token abgelehnt hat. Aktualisieren Sie `botToken`, `tokenFile` oder `TELEGRAM_BOT_TOKEN` mit dem aktuellen BotFather-Token; OpenClaw stoppt vor dem Polling, sodass dies nicht als Fehler bei der Webhook-Bereinigung gemeldet wird.
  * `setMyCommands failed` mit Netzwerk-/Fetch-Fehlern bedeutet üblicherweise, dass ausgehendes DNS/HTTPS zu `api.telegram.org` blockiert ist.


### Befehle zur Gerätekopplung (`device-pair`-Plugin)

Wenn das `device-pair`-Plugin installiert ist:

  1. `/pair` generiert Einrichtungscode
  2. Code in die iOS-App einfügen
  3. `/pair pending` listet ausstehende Anfragen auf (einschließlich Rolle/Scopes)
  4. die Anfrage genehmigen: 
     * `/pair approve <requestId>` für explizite Genehmigung
     * `/pair approve`, wenn es nur eine ausstehende Anfrage gibt
     * `/pair approve latest` für die neueste


Der Einrichtungscode enthält ein kurzlebiges Bootstrap-Token. Die integrierte Bootstrap-Übergabe hält das primäre Node-Token bei `scopes: []`; jedes übergebene Operator-Token bleibt auf `operator.approvals`, `operator.read`, `operator.talk.secrets` und `operator.write` begrenzt. Bootstrap-Scope-Prüfungen sind rollenpräfigiert, sodass diese Operator-Zulassungsliste nur Operator-Anfragen erfüllt; Nicht-Operator-Rollen benötigen weiterhin Scopes unter ihrem eigenen Rollenpräfix.

Wenn ein Gerät es mit geänderten Authentifizierungsdetails erneut versucht (zum Beispiel Rolle/Scopes/öffentlicher Schlüssel), wird die vorherige ausstehende Anfrage ersetzt und die neue Anfrage verwendet eine andere `requestId`. Führen Sie `/pair pending` erneut aus, bevor Sie genehmigen.

Weitere Details: [Kopplung](</de/channels/pairing#pair-via-telegram-recommended-for-ios>).

Inline buttons

Inline-Keyboard-Scope konfigurieren:

json5Copy code
[code]
    {channels: {telegram: {  capabilities: {    inlineButtons: "allowlist",  },},},}
[/code]

Überschreibung pro Konto:

json5Copy code
[code]
    {channels: {telegram: {  accounts: {    main: {      capabilities: {        inlineButtons: "allowlist",      },    },  },},},}
[/code]

Scopes:

  * `off`
  * `dm`
  * `group`
  * `all`
  * `allowlist` (Standard)


Veraltetes `capabilities: ["inlineButtons"]` wird `inlineButtons: "all"` zugeordnet.

Beispiel für eine Nachrichtenaktion:

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",message: "Choose an option:",buttons: [[  { text: "Yes", callback_data: "yes" },  { text: "No", callback_data: "no" },],[{ text: "Cancel", callback_data: "cancel" }],],}
[/code]

Callback-Klicks werden als Text an den Agenten übergeben: `callback_data: <value>`

Telegram message actions for agents and automation

Telegram-Tool-Aktionen umfassen:

  * `sendMessage` (`to`, `content`, optional `mediaUrl`, `replyToMessageId`, `messageThreadId`)
  * `react` (`chatId`, `messageId`, `emoji`)
  * `deleteMessage` (`chatId`, `messageId`)
  * `editMessage` (`chatId`, `messageId`, `content`)
  * `createForumTopic` (`chatId`, `name`, optional `iconColor`, `iconCustomEmojiId`)


Kanal-Nachrichtenaktionen stellen ergonomische Aliasse bereit (`send`, `react`, `delete`, `edit`, `sticker`, `sticker-search`, `topic-create`).

Gating-Steuerungen:

  * `channels.telegram.actions.sendMessage`
  * `channels.telegram.actions.deleteMessage`
  * `channels.telegram.actions.reactions`
  * `channels.telegram.actions.sticker` (Standard: deaktiviert)


Hinweis: `edit` und `topic-create` sind derzeit standardmäßig aktiviert und haben keine separaten `channels.telegram.actions.*`-Schalter. Laufzeit-Sendevorgänge verwenden den aktiven Konfigurations-/Secrets-Snapshot (Start/Reload), daher führen Aktionspfade keine Ad-hoc-Neuauflösung von SecretRef pro Sendevorgang aus.

Semantik zum Entfernen von Reaktionen: [/tools/reactions](</de/tools/reactions>)

Reply threading tags

Telegram unterstützt explizite Antwort-Threading-Tags in generierter Ausgabe:

  * `[[reply_to_current]]` antwortet auf die auslösende Nachricht
  * `[[reply_to:<id>]]` antwortet auf eine bestimmte Telegram-Nachrichten-ID


`channels.telegram.replyToMode` steuert die Behandlung:

  * `off` (Standard)
  * `first`
  * `all`


Wenn Antwort-Threading aktiviert ist und der ursprüngliche Telegram-Text oder die Bildunterschrift verfügbar ist, fügt OpenClaw automatisch einen nativen Telegram-Zitatauszug ein. Telegram begrenzt nativen Zitattext auf 1024 UTF-16-Codeeinheiten; längere Nachrichten werden daher ab dem Anfang zitiert und fallen auf eine einfache Antwort zurück, wenn Telegram das Zitat ablehnt.

Hinweis: `off` deaktiviert implizites Antwort-Threading. Explizite `[[reply_to_*]]`-Tags werden weiterhin berücksichtigt.

Forum topics and thread behavior

Forum-Supergruppen:

  * Themen-Sitzungsschlüssel hängen `:topic:<threadId>` an
  * Antworten und Tippaktionen richten sich an den Themen-Thread
  * Themenkonfigurationspfad: `channels.telegram.groups.<chatId>.topics.<threadId>`


Sonderfall für allgemeines Thema (`threadId=1`):

  * Nachrichtensendungen lassen `message_thread_id` weg (Telegram lehnt `sendMessage(...thread_id=1)` ab)
  * Tippaktionen enthalten weiterhin `message_thread_id`


Themenvererbung: Themeneinträge erben Gruppeneinstellungen, sofern sie nicht überschrieben werden (`requireMention`, `allowFrom`, `skills`, `systemPrompt`, `enabled`, `groupPolicy`). `agentId` ist ausschließlich themenbezogen und erbt nicht von Gruppenstandardwerten.

**Agent-Routing pro Thema** : Jedes Thema kann durch Setzen von `agentId` in der Themenkonfiguration an einen anderen Agenten geleitet werden. Dadurch erhält jedes Thema einen eigenen isolierten Arbeitsbereich, Speicher und eine eigene Sitzung. Beispiel:

json5Copy code
[code]
    {  channels: {    telegram: {      groups: {        "-1001234567890": {          topics: {            "1": { agentId: "main" },      // General topic → main agent            "3": { agentId: "zu" },        // Dev topic → zu agent            "5": { agentId: "coder" }      // Code review → coder agent          }        }      }    }  }}
[/code]

Jedes Topic hat dann einen eigenen Sitzungsschlüssel: `agent:zu:telegram:group:-1001234567890:topic:3`

**Persistente ACP-Topic-Bindung** : Forum-Topics können ACP-Harness-Sitzungen über typisierte ACP-Bindungen auf oberster Ebene anheften (`bindings[]` mit `type: "acp"` und `match.channel: "telegram"`, `peer.kind: "group"` sowie einer Topic-qualifizierten ID wie `-1001234567890:topic:42`). Derzeit auf Forum-Topics in Gruppen/Supergruppen beschränkt. Siehe [ACP-Agenten](</de/tools/acp-agents>).

**Thread-gebundener ACP-Spawn aus dem Chat** : `/acp spawn <agent> --thread here|auto` bindet das aktuelle Topic an eine neue ACP-Sitzung; Folgeantworten werden direkt dorthin geleitet. OpenClaw heftet die Spawn-Bestätigung im Topic an. Erfordert, dass `channels.telegram.threadBindings.spawnSessions` aktiviert bleibt (Standard: `true`).

Der Template-Kontext stellt `MessageThreadId` und `IsForum` bereit. DM-Chats mit `message_thread_id` behalten standardmäßig DM-Routing und Antwortmetadaten in flachen Sitzungen bei; sie verwenden Thread-fähige Sitzungsschlüssel nur, wenn sie mit `threadReplies: "inbound"`, `threadReplies: "always"`, `requireTopic: true` oder einer passenden Topic-Konfiguration konfiguriert sind. Verwenden Sie `channels.telegram.dm.threadReplies` auf oberster Ebene für den Kontostandard oder `direct.<chatId>.threadReplies` für eine einzelne DM.

Audio, Video und Sticker

### Audionachrichten

Telegram unterscheidet Sprachnachrichten von Audiodateien.

  * Standard: Verhalten für Audiodateien
  * Tag `[[audio_as_voice]]` in der Agent-Antwort, um das Senden als Sprachnachricht zu erzwingen
  * Eingehende Transkripte von Sprachnachrichten werden im Agent-Kontext als maschinell erzeugter, nicht vertrauenswürdiger Text gekennzeichnet; die Erwähnungserkennung verwendet weiterhin das rohe Transkript, sodass erwähnungsgesteuerte Sprachnachrichten weiter funktionieren.


Beispiel für eine Nachrichtenaktion:

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",media: "https://example.com/voice.ogg",asVoice: true,}
[/code]

### Videonachrichten

Telegram unterscheidet Videodateien von Videonachrichten.

Beispiel für eine Nachrichtenaktion:

json5Copy code
[code]
    {action: "send",channel: "telegram",to: "123456789",media: "https://example.com/video.mp4",asVideoNote: true,}
[/code]

Videonachrichten unterstützen keine Bildunterschriften; bereitgestellter Nachrichtentext wird separat gesendet.

### Sticker

Verarbeitung eingehender Sticker:

  * statisches WEBP: heruntergeladen und verarbeitet (Platzhalter `<media:sticker>`)
  * animiertes TGS: übersprungen
  * Video-WEBM: übersprungen


Sticker-Kontextfelder:

  * `Sticker.emoji`
  * `Sticker.setName`
  * `Sticker.fileId`
  * `Sticker.fileUniqueId`
  * `Sticker.cachedDescription`


Sticker-Cache-Datei:

  * `~/.openclaw/telegram/sticker-cache.json`


Sticker werden einmal beschrieben (wenn möglich) und zwischengespeichert, um wiederholte Vision-Aufrufe zu reduzieren.

Sticker-Aktionen aktivieren:

json5Copy code
[code]
    {channels: {telegram: {  actions: {    sticker: true,  },},},}
[/code]

Sticker-Aktion senden:

json5Copy code
[code]
    {action: "sticker",channel: "telegram",to: "123456789",fileId: "CAACAgIAAxkBAAI...",}
[/code]

Zwischengespeicherte Sticker suchen:

json5Copy code
[code]
    {action: "sticker-search",channel: "telegram",query: "cat waving",limit: 5,}
[/code]

Reaktionsbenachrichtigungen

Telegram-Reaktionen kommen als `message_reaction`-Updates an (getrennt von Nachrichten-Payloads).

Wenn aktiviert, stellt OpenClaw Systemereignisse wie diese in die Warteschlange:

  * `Telegram reaction added: 👍 by Alice (@alice) on msg 42`


Konfiguration:

  * `channels.telegram.reactionNotifications`: `off | own | all` (Standard: `own`)
  * `channels.telegram.reactionLevel`: `off | ack | minimal | extensive` (Standard: `minimal`)


Hinweise:

  * `own` bedeutet nur Benutzerreaktionen auf vom Bot gesendete Nachrichten (Best Effort über den Cache gesendeter Nachrichten).
  * Reaktionsereignisse respektieren weiterhin Telegram-Zugriffskontrollen (`dmPolicy`, `allowFrom`, `groupPolicy`, `groupAllowFrom`); nicht autorisierte Absender werden verworfen.
  * Telegram stellt in Reaktions-Updates keine Thread-IDs bereit. 
    * Nicht-Forum-Gruppen werden zur Gruppenchat-Sitzung geleitet
    * Forum-Gruppen werden zur allgemeinen Topic-Sitzung der Gruppe (`:topic:1`) geleitet, nicht zum exakten ursprünglichen Topic


`allowed_updates` für Polling/Webhook enthält `message_reaction` automatisch.

Bestätigungsreaktionen

`ackReaction` sendet ein Bestätigungs-Emoji, während OpenClaw eine eingehende Nachricht verarbeitet.

Auflösungsreihenfolge:

  * `channels.telegram.accounts.<accountId>.ackReaction`
  * `channels.telegram.ackReaction`
  * `messages.ackReaction`
  * Fallback auf Emoji der Agent-Identität (`agents.list[].identity.emoji`, sonst "👀")


Hinweise:

  * Telegram erwartet Unicode-Emoji (zum Beispiel "👀").
  * Verwenden Sie `""`, um die Reaktion für einen Kanal oder ein Konto zu deaktivieren.

Konfigurationsschreibvorgänge aus Telegram-Ereignissen und -Befehlen

Schreibvorgänge für die Kanalkonfiguration sind standardmäßig aktiviert (`configWrites !== false`).

Von Telegram ausgelöste Schreibvorgänge umfassen:

  * Gruppenmigrationsereignisse (`migrate_to_chat_id`) zum Aktualisieren von `channels.telegram.groups`
  * `/config set` und `/config unset` (erfordert aktivierte Befehle)


Deaktivieren:

json5Copy code
[code]
    {channels: {telegram: {  configWrites: false,},},}
[/code]

Long Polling vs. Webhook

Standard ist Long Polling. Legen Sie für den Webhook-Modus `channels.telegram.webhookUrl` und `channels.telegram.webhookSecret` fest; optional `webhookPath`, `webhookHost`, `webhookPort` (Standardwerte `/telegram-webhook`, `127.0.0.1`, `8787`).

Im Long-Polling-Modus persistiert OpenClaw seine Neustart-Watermark erst, nachdem ein Update erfolgreich dispatcht wurde. Wenn ein Handler fehlschlägt, bleibt dieses Update im selben Prozess wiederholbar und wird für die Neustart-Deduplizierung nicht als abgeschlossen geschrieben.

Der lokale Listener bindet an `127.0.0.1:8787`. Für öffentlichen Ingress setzen Sie entweder einen Reverse Proxy vor den lokalen Port oder legen `webhookHost: "0.0.0.0"` bewusst fest.

Der Webhook-Modus validiert Request-Guards, das geheime Telegram-Token und den JSON-Body, bevor `200` an Telegram zurückgegeben wird. OpenClaw verarbeitet das Update anschließend asynchron über dieselben Bot-Lanes pro Chat/pro Topic, die auch von Long Polling verwendet werden, sodass langsame Agent-Turns das Delivery-ACK von Telegram nicht blockieren.

Limits, Wiederholung und CLI-Ziele

  * `channels.telegram.textChunkLimit` ist standardmäßig 4000.
  * `channels.telegram.chunkMode="newline"` bevorzugt Absatzgrenzen (Leerzeilen), bevor nach Länge aufgeteilt wird.
  * `channels.telegram.mediaMaxMb` (Standard 100) begrenzt die Größe eingehender und ausgehender Telegram-Medien.
  * `channels.telegram.mediaGroupFlushMs` (Standard 500) steuert, wie lange Telegram-Alben/Mediengruppen gepuffert werden, bevor OpenClaw sie als eine eingehende Nachricht dispatcht. Erhöhen Sie den Wert, wenn Albumteile spät ankommen; verringern Sie ihn, um die Antwortlatenz bei Alben zu reduzieren.
  * `channels.telegram.timeoutSeconds` überschreibt das Timeout des Telegram-API-Clients (wenn nicht gesetzt, gilt der grammY-Standard). Bot-Clients begrenzen konfigurierte Werte unterhalb des 60-sekündigen Request-Guards für ausgehende Text-/Typing-Anfragen, damit grammY die sichtbare Antwortzustellung nicht abbricht, bevor OpenClaws Transport-Guard und Fallback ausgeführt werden können. Long Polling verwendet weiterhin einen 45-sekündigen `getUpdates`-Request-Guard, damit inaktive Polls nicht unbegrenzt offen bleiben.
  * `channels.telegram.pollingStallThresholdMs` ist standardmäßig `120000`; justieren Sie den Wert nur bei falsch positiven Polling-Stall-Neustarts zwischen `30000` und `600000`.
  * Gruppen-Kontexthistorie verwendet `channels.telegram.historyLimit` oder `messages.groupChat.historyLimit` (Standard 50); `0` deaktiviert sie.
  * Ergänzender Kontext für Antworten/Zitate/Weiterleitungen wird in ein ausgewähltes Konversationskontextfenster normalisiert, wenn der Gateway die übergeordneten Nachrichten beobachtet hat; der Cache beobachteter Nachrichten wird neben dem Sitzungsspeicher persistiert. Telegram enthält in Updates nur ein flaches `reply_to_message`, daher sind Ketten, die älter als der Cache sind, auf Telegrams aktuelle Update-Payload begrenzt.
  * Telegram-Allowlists steuern primär, wer den Agent auslösen kann, nicht eine vollständige Redaktionsgrenze für ergänzenden Kontext.
  * DM-Historiensteuerungen: 
    * `channels.telegram.dmHistoryLimit`
    * `channels.telegram.dms["<user_id>"].historyLimit`
  * Die Konfiguration `channels.telegram.retry` gilt für Telegram-Sendehelfer (CLI/Tools/Aktionen) bei behebbaren ausgehenden API-Fehlern. Die Zustellung der endgültigen eingehenden Antwort verwendet ebenfalls eine begrenzte Safe-Send-Wiederholung für Telegram-Pre-Connect-Fehler, wiederholt aber keine mehrdeutigen Post-Send-Netzwerkumschläge, die sichtbare Nachrichten duplizieren könnten.


Sendeziele für CLI und Nachrichten-Tool können eine numerische Chat-ID, ein Benutzername oder ein Forum-Topic-Ziel sein:

bashCopy code
[code]
    openclaw message send --channel telegram --target 123456789 --message "hi"openclaw message send --channel telegram --target @name --message "hi"openclaw message send --channel telegram --target -1001234567890:topic:42 --message "hi topic"
[/code]

Telegram-Polls verwenden `openclaw message poll` und unterstützen Forum-Topics:

bashCopy code
[code]
    openclaw message poll --channel telegram --target 123456789 \--poll-question "Ship it?" --poll-option "Yes" --poll-option "No"openclaw message poll --channel telegram --target -1001234567890:topic:42 \--poll-question "Pick a time" --poll-option "10am" --poll-option "2pm" \--poll-duration-seconds 300 --poll-public
[/code]

Nur-Telegram-Poll-Flags:

  * `--poll-duration-seconds` (5-600)
  * `--poll-anonymous`
  * `--poll-public`
  * `--thread-id` für Forum-Topics (oder verwenden Sie ein `:topic:`-Ziel)


Telegram-Send unterstützt außerdem:

  * `--presentation` mit `buttons`-Blöcken für Inline-Keyboards, wenn `channels.telegram.capabilities.inlineButtons` dies erlaubt
  * `--pin` oder `--delivery '{"pin":true}'`, um angeheftete Zustellung anzufordern, wenn der Bot in diesem Chat anheften kann
  * `--force-document`, um ausgehende Bilder, GIFs und Videos als Dokumente statt als komprimierte Foto-, animierte Medien- oder Video-Uploads zu senden


Aktionssteuerung:

  * `channels.telegram.actions.sendMessage=false` deaktiviert ausgehende Telegram-Nachrichten, einschließlich Polls
  * `channels.telegram.actions.poll=false` deaktiviert das Erstellen von Telegram-Polls, während reguläres Senden aktiviert bleibt

Exec-Freigaben in Telegram

Telegram unterstützt Exec-Freigaben in Genehmiger-DMs und kann Prompts optional im ursprünglichen Chat oder Topic posten. Genehmiger müssen numerische Telegram-Benutzer-IDs sein.

Konfigurationspfad:

  * `channels.telegram.execApprovals.enabled` (aktiviert sich automatisch, wenn mindestens ein Genehmiger auflösbar ist)
  * `channels.telegram.execApprovals.approvers` (fällt auf numerische Owner-IDs aus `commands.ownerAllowFrom` zurück)
  * `channels.telegram.execApprovals.target`: `dm` (Standard) | `channel` | `both`
  * `agentFilter`, `sessionFilter`


`channels.telegram.allowFrom`, `groupAllowFrom` und `defaultTo` steuern, wer mit dem Bot sprechen kann und wohin er normale Antworten sendet. Sie machen niemanden zu einem Exec-Genehmiger. Das erste genehmigte DM-Pairing bootstrapt `commands.ownerAllowFrom`, wenn noch kein Befehls-Owner existiert, sodass die Einrichtung mit einem Owner weiterhin funktioniert, ohne IDs unter `execApprovals.approvers` zu duplizieren.

Kanalzustellung zeigt den Befehlstext im Chat; aktivieren Sie `channel` oder `both` nur in vertrauenswürdigen Gruppen/Topics. Wenn der Prompt in einem Forum-Topic landet, bewahrt OpenClaw das Topic für den Freigabe-Prompt und die Folgeantwort. Exec-Freigaben laufen standardmäßig nach 30 Minuten ab.

Inline-Freigabeschaltflächen erfordern außerdem, dass `channels.telegram.capabilities.inlineButtons` die Zieloberfläche (`dm`, `group` oder `all`) erlaubt. Freigabe-IDs mit Präfix `plugin:` werden über Plugin-Freigaben aufgelöst; andere werden zuerst über Exec-Freigaben aufgelöst.

Siehe [Exec-Freigaben](</de/tools/exec-approvals>).

## Steuerung von Fehlerantworten

Wenn der Agent auf einen Zustell- oder Provider-Fehler stößt, kann Telegram entweder mit dem Fehlertext antworten oder ihn unterdrücken. Zwei Konfigurationsschlüssel steuern dieses Verhalten:

Schlüssel | Werte | Standard | Beschreibung  
---|---|---|---  
`channels.telegram.errorPolicy` | `reply`, `silent` | `reply` | `reply` sendet eine freundliche Fehlermeldung an den Chat. `silent` unterdrückt Fehlerantworten vollständig.  
`channels.telegram.errorCooldownMs` | number (ms) | `60000` | Mindestzeit zwischen Fehlerantworten an denselben Chat. Verhindert Fehler-Spam während Ausfällen.  
  
Überschreibungen pro Konto, Gruppe und Thema werden unterstützt (gleiche Vererbung wie bei anderen Telegram-Konfigurationsschlüsseln).

json5Copy code
[code]
    {  channels: {    telegram: {      errorPolicy: "reply",      errorCooldownMs: 120000,      groups: {        "-1001234567890": {          errorPolicy: "silent", // suppress errors in this group        },      },    },  },}
[/code]

## Fehlerbehebung

Bot antwortet nicht auf Gruppennachrichten ohne Erwähnung

  * Wenn `requireMention=false` ist, muss der Telegram-Datenschutzmodus vollständige Sichtbarkeit erlauben. 
    * BotFather: `/setprivacy` -> Deaktivieren
    * entfernen Sie den Bot anschließend aus der Gruppe und fügen Sie ihn erneut hinzu
  * `openclaw channels status` warnt, wenn die Konfiguration nicht erwähnte Gruppennachrichten erwartet.
  * `openclaw channels status --probe` kann explizite numerische Gruppen-IDs prüfen; wildcard `"*"` kann nicht per Mitgliedschaft geprüft werden.
  * schneller Sitzungstest: `/activation always`.

Bot sieht überhaupt keine Gruppennachrichten

  * wenn `channels.telegram.groups` vorhanden ist, muss die Gruppe aufgeführt sein (oder `"*"` enthalten)
  * prüfen Sie die Bot-Mitgliedschaft in der Gruppe
  * prüfen Sie die Logs: `openclaw logs --follow` für Gründe zum Überspringen

Befehle funktionieren nur teilweise oder gar nicht

  * autorisieren Sie Ihre Absenderidentität (Pairing und/oder numerisches `allowFrom`)
  * die Befehlsautorisierung gilt weiterhin, auch wenn die Gruppenrichtlinie `open` ist
  * `setMyCommands failed` mit `BOT_COMMANDS_TOO_MUCH` bedeutet, dass das native Menü zu viele Einträge hat; reduzieren Sie Plugin-/Skill-/benutzerdefinierte Befehle oder deaktivieren Sie native Menüs
  * `deleteMyCommands`\- / `setMyCommands`-Startaufrufe und `sendChatAction`-Tippindikator-Aufrufe sind begrenzt und werden bei Request-Timeout einmal über Telegrams Transport-Fallback erneut versucht. Dauerhafte Netzwerk-/Fetch-Fehler weisen in der Regel auf DNS-/HTTPS-Erreichbarkeitsprobleme zu `api.telegram.org` hin

Start meldet nicht autorisiertes Token

  * `getMe returned 401` ist ein Telegram-Authentifizierungsfehler für das konfigurierte Bot-Token.
  * Kopieren Sie das Bot-Token in BotFather erneut oder generieren Sie es neu, und aktualisieren Sie dann `channels.telegram.botToken`, `channels.telegram.tokenFile`, `channels.telegram.accounts.<id>.botToken` oder `TELEGRAM_BOT_TOKEN` für das Standardkonto.
  * `deleteWebhook 401 Unauthorized` während des Starts ist ebenfalls ein Authentifizierungsfehler; dies als „kein Webhook vorhanden“ zu behandeln, würde denselben Fehler durch ein ungültiges Token nur auf spätere API-Aufrufe verschieben.

Polling- oder Netzwerkinstabilität

  * Node 22+ + benutzerdefiniertes Fetch/Proxy können sofortiges Abbruchverhalten auslösen, wenn AbortSignal-Typen nicht übereinstimmen.
  * Manche Hosts lösen `api.telegram.org` zuerst zu IPv6 auf; defekter IPv6-Egress kann zeitweise Telegram-API-Fehler verursachen.
  * Wenn Logs `TypeError: fetch failed` oder `Network request for 'getUpdates' failed!` enthalten, versucht OpenClaw diese nun als behebbare Netzwerkfehler erneut.
  * Während des Polling-Starts verwendet OpenClaw den erfolgreichen Start-`getMe`-Probe für grammY wieder, sodass der Runner kein zweites `getMe` vor dem ersten `getUpdates` benötigt.
  * Wenn `deleteWebhook` während des Polling-Starts mit einem transienten Netzwerkfehler fehlschlägt, fährt OpenClaw mit Long Polling fort, statt einen weiteren Control-Plane-Aufruf vor dem Polling auszuführen. Ein noch aktiver Webhook erscheint als `getUpdates`-Konflikt; OpenClaw baut dann den Telegram-Transport neu auf und versucht die Webhook-Bereinigung erneut.
  * Wenn Telegram-Sockets in einem kurzen festen Takt erneuert werden, prüfen Sie auf einen niedrigen Wert für `channels.telegram.timeoutSeconds`; Bot-Clients begrenzen konfigurierte Werte unterhalb der Schutzwerte für ausgehende Requests und `getUpdates`, ältere Releases konnten jedoch jedes Polling oder jede Antwort abbrechen, wenn dies unter diesen Schutzwerten gesetzt war.
  * Wenn Logs `Polling stall detected` enthalten, startet OpenClaw das Polling neu und baut den Telegram-Transport nach standardmäßig 120 Sekunden ohne abgeschlossene Long-Poll-Liveness neu auf.
  * `openclaw channels status --probe` und `openclaw doctor` warnen, wenn ein laufendes Polling-Konto `getUpdates` nach der Startnachfrist nicht abgeschlossen hat, wenn ein laufendes Webhook-Konto `setWebhook` nach der Startnachfrist nicht abgeschlossen hat oder wenn die letzte erfolgreiche Polling-Transportaktivität veraltet ist.
  * Erhöhen Sie `channels.telegram.pollingStallThresholdMs` nur, wenn lang laufende `getUpdates`-Aufrufe fehlerfrei sind, Ihr Host aber weiterhin falsche Polling-Stall-Neustarts meldet. Dauerhafte Stalls deuten in der Regel auf Proxy-, DNS-, IPv6- oder TLS-Egress-Probleme zwischen Host und `api.telegram.org` hin.
  * Telegram berücksichtigt außerdem Prozess-Proxy-Umgebungsvariablen für den Bot-API-Transport, einschließlich `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY` und deren Varianten in Kleinschreibung. `NO_PROXY` / `no_proxy` kann `api.telegram.org` weiterhin umgehen.
  * Wenn der von OpenClaw verwaltete Proxy über `OPENCLAW_PROXY_URL` für eine Dienstumgebung konfiguriert ist und keine standardmäßige Proxy-Umgebungsvariable vorhanden ist, verwendet Telegram diese URL ebenfalls für den Bot-API-Transport.
  * Leiten Sie Telegram-API-Aufrufe auf VPS-Hosts mit instabilem direktem Egress/TLS über `channels.telegram.proxy`:

yamlCopy code
[code]
    channels:telegram:proxy: socks5://<user>:<password>@proxy-host:1080
[/code]

  * Node 22+ verwendet standardmäßig `autoSelectFamily=true` (außer WSL2). Die Reihenfolge der Telegram-DNS-Ergebnisse berücksichtigt `OPENCLAW_TELEGRAM_DNS_RESULT_ORDER`, dann `channels.telegram.network.dnsResultOrder`, dann den Prozessstandard wie `NODE_OPTIONS=--dns-result-order=ipv4first`; wenn nichts davon zutrifft, fällt Node 22+ auf `ipv4first` zurück.
  * Wenn Ihr Host WSL2 ist oder ausdrücklich besser mit reinem IPv4-Verhalten funktioniert, erzwingen Sie die Familienauswahl:

yamlCopy code
[code]
    channels:telegram:network:  autoSelectFamily: false
[/code]

  * Antworten aus dem RFC-2544-Benchmark-Bereich (`198.18.0.0/15`) sind für Telegram-Mediendownloads standardmäßig bereits erlaubt. Wenn ein vertrauenswürdiger Fake-IP- oder transparenter Proxy `api.telegram.org` während Mediendownloads auf eine andere private/interne/Special-Use-Adresse umschreibt, können Sie den nur für Telegram geltenden Bypass aktivieren:

yamlCopy code
[code]
    channels:telegram:network:  dangerouslyAllowPrivateNetwork: true
[/code]

  * Dieselbe Opt-in-Option ist pro Konto unter `channels.telegram.accounts.<accountId>.network.dangerouslyAllowPrivateNetwork` verfügbar.
  * Wenn Ihr Proxy Telegram-Medienhosts in `198.18.x.x` auflöst, lassen Sie das gefährliche Flag zunächst deaktiviert. Telegram-Medien erlauben den RFC-2544-Benchmark-Bereich bereits standardmäßig.


  * Umgebungsüberschreibungen (temporär): 
    * `OPENCLAW_TELEGRAM_DISABLE_AUTO_SELECT_FAMILY=1`
    * `OPENCLAW_TELEGRAM_ENABLE_AUTO_SELECT_FAMILY=1`
    * `OPENCLAW_TELEGRAM_DNS_RESULT_ORDER=ipv4first`
  * DNS-Antworten validieren:

bashCopy code
[code]
    dig +short api.telegram.org Adig +short api.telegram.org AAAA
[/code]

Weitere Hilfe: [Channel-Fehlerbehebung](</de/channels/troubleshooting>).

## Konfigurationsreferenz

Primäre Referenz: [Konfigurationsreferenz - Telegram](</de/gateway/config-channels#telegram>).

Wichtige Telegram-Felder

  * Start/Auth: `enabled`, `botToken`, `tokenFile`, `accounts.*` (`tokenFile` muss auf eine reguläre Datei verweisen; Symlinks werden abgelehnt)
  * Zugriffskontrolle: `dmPolicy`, `allowFrom`, `groupPolicy`, `groupAllowFrom`, `groups`, `groups.*.topics.*`, `bindings[]` auf oberster Ebene (`type: "acp"`)
  * Ausführungsgenehmigungen: `execApprovals`, `accounts.*.execApprovals`
  * Befehl/Menü: `commands.native`, `commands.nativeSkills`, `customCommands`
  * Threads/Antworten: `replyToMode`, `dm.threadReplies`, `direct.*.threadReplies`
  * Streaming: `streaming` (Vorschau), `streaming.preview.toolProgress`, `blockStreaming`
  * Formatierung/Zustellung: `textChunkLimit`, `chunkMode`, `linkPreview`, `responsePrefix`
  * Medien/Netzwerk: `mediaMaxMb`, `mediaGroupFlushMs`, `timeoutSeconds`, `pollingStallThresholdMs`, `retry`, `network.autoSelectFamily`, `network.dangerouslyAllowPrivateNetwork`, `proxy`
  * benutzerdefinierter API-Root: `apiRoot` (nur Bot-API-Root; `/bot&lt;TOKEN&gt;` nicht einschließen)
  * Webhook: `webhookUrl`, `webhookSecret`, `webhookPath`, `webhookHost`
  * Aktionen/Fähigkeiten: `capabilities.inlineButtons`, `actions.sendMessage|editMessage|deleteMessage|reactions|sticker`
  * Reaktionen: `reactionNotifications`, `reactionLevel`
  * Fehler: `errorPolicy`, `errorCooldownMs`
  * Schreibvorgänge/Verlauf: `configWrites`, `historyLimit`, `dmHistoryLimit`, `dms.*.historyLimit`


## Verwandte Themen

[**Pairing** Koppeln Sie einen Telegram-Benutzer mit dem Gateway. ](</de/channels/pairing>) [**Gruppen** Verhalten der Allowlist für Gruppen und Themen. ](</de/channels/groups>) [**Channel-Routing** Leiten Sie eingehende Nachrichten an Agenten weiter. ](</de/channels/channel-routing>) [**Sicherheit** Bedrohungsmodell und Härtung. ](</de/gateway/security>) [**Multi-Agent-Routing** Ordnen Sie Gruppen und Themen Agenten zu. ](</de/concepts/multi-agent>) [**Fehlerbehebung** Kanalübergreifende Diagnose. ](</de/channels/troubleshooting>)

Was this useful?YesNo
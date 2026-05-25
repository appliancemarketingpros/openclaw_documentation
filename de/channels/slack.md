---
title: Slack
source_url: https://docs.openclaw.ai/de/channels/slack
scraped_at: 2026-05-25
---

Bereit für den Produktionseinsatz für DMs und Kanäle über Slack-App-Integrationen. Der Standardmodus ist Socket Mode; HTTP Request URLs werden ebenfalls unterstützt.

[**Kopplung** Slack-DMs verwenden standardmäßig den Kopplungsmodus. ](</de/channels/pairing>) [**Slash-Befehle** Natives Befehlsverhalten und Befehlskatalog. ](</de/tools/slash-commands>) [**Kanal-Fehlerbehebung** Kanalübergreifende Diagnosen und Reparatur-Playbooks. ](</de/channels/troubleshooting>)

## Socket Mode oder HTTP Request URLs auswählen

Beide Transporte sind produktionsreif und erreichen Funktionsgleichheit für Messaging, Slash-Befehle, App Home und Interaktivität. Wählen Sie nach Bereitstellungsform, nicht nach Funktionen.

Aspekt | Socket Mode (Standard) | HTTP Request URLs  
---|---|---  
Öffentliche Gateway-URL | Nicht erforderlich | Erforderlich (DNS, TLS, Reverse Proxy oder Tunnel)  
Ausgehendes Netzwerk | Ausgehendes WSS zu `wss-primary.slack.com` muss erreichbar sein | Kein ausgehendes WS; nur eingehendes HTTPS  
Benötigte Token | Bot-Token (`xoxb-...`) + App-Level Token (`xapp-...`) mit `connections:write` | Bot-Token (`xoxb-...`) + Signing Secret  
Entwicklungs-Laptop / hinter Firewall | Funktioniert unverändert | Benötigt einen öffentlichen Tunnel (ngrok, Cloudflare Tunnel, Tailscale Funnel) oder einen Staging-Gateway  
Horizontale Skalierung | Eine Socket-Mode-Sitzung pro App und Host; mehrere Gateways benötigen separate Slack-Apps | Zustandsloser POST-Handler; mehrere Gateway-Replikate können eine App hinter einem Load Balancer gemeinsam nutzen  
Mehrere Konten auf einem Gateway | Unterstützt; jedes Konto öffnet sein eigenes WS | Unterstützt; jedes Konto benötigt einen eindeutigen `webhookPath` (Standard `/slack/events`), damit Registrierungen nicht kollidieren  
Slash-Befehls-Transport | Wird über die WS-Verbindung zugestellt; `slash_commands[].url` wird ignoriert | Slack sendet POSTs an `slash_commands[].url`; das Feld ist erforderlich, damit der Befehl ausgelöst wird  
Request-Signierung | Nicht verwendet (Authentifizierung erfolgt über das App-Level Token) | Slack signiert jede Anfrage; OpenClaw verifiziert mit `signingSecret`  
Wiederherstellung nach Verbindungsabbruch | Slack SDK verbindet automatisch neu; das Pong-Timeout-Transport-Tuning des Gateway gilt | Keine dauerhafte Verbindung, die abbrechen kann; Wiederholungen erfolgen pro Anfrage durch Slack  
  
## Schnelleinrichtung

### Socket Mode (Standard)

* ### Neue Slack-App erstellen

Öffnen Sie [api.slack.com/apps](<https://api.slack.com/apps/new>) → **Create New App** → **From a manifest** → wählen Sie Ihren Workspace aus → fügen Sie eines der folgenden Manifeste ein → **Next** → **Create**.

EmpfohlenCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]}}}
[/code]

MinimalCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]}}}
[/code]

Nachdem Slack die App erstellt hat:

  * **Basic Information → App-Level Tokens → Generate Token and Scopes** : Fügen Sie `connections:write` hinzu, speichern Sie und kopieren Sie den Wert `xapp-...`.
  * **Install App → Install to Workspace** : Kopieren Sie das Bot User OAuth Token `xoxb-...`.


* ### OpenClaw konfigurieren

Empfohlene SecretRef-Einrichtung:

bashCopy code
[code]
    export SLACK_APP_TOKEN=xapp-...export SLACK_BOT_TOKEN=xoxb-...cat > slack.socket.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "socket",appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },},},}JSON5openclaw config patch --file ./slack.socket.patch.json5 --dry-runopenclaw config patch --file ./slack.socket.patch.json5
[/code]

Env-Fallback (nur Standardkonto):

bashCopy code
[code]
    SLACK_APP_TOKEN=xapp-...SLACK_BOT_TOKEN=xoxb-...
[/code]

* ### Gateway starten

bashCopy code
[code]
    openclaw gateway
[/code]

### HTTP Request URLs

* ### Neue Slack-App erstellen

Öffnen Sie [api.slack.com/apps](<https://api.slack.com/apps/new>) → **Create New App** → **From a manifest** → wählen Sie Ihren Workspace aus → fügen Sie eines der folgenden Manifeste ein → ersetzen Sie `https://gateway-host.example.com/slack/events` durch Ihre öffentliche Gateway-URL → **Next** → **Create**.

EmpfohlenCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

MinimalCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

Nachdem Slack die App erstellt hat:

  * **Basic Information → App Credentials** : Kopieren Sie das **Signing Secret** für die Anfrageverifizierung.
  * **Install App → Install to Workspace** : Kopieren Sie das `xoxb-...` Bot User OAuth Token.


* ### Configure OpenClaw

Empfohlene SecretRef-Einrichtung:

bashCopy code
[code]
    export SLACK_BOT_TOKEN=xoxb-...export SLACK_SIGNING_SECRET=...cat > slack.http.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "http",botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },signingSecret: { source: "env", provider: "default", id: "SLACK_SIGNING_SECRET" },webhookPath: "/slack/events",},},}JSON5openclaw config patch --file ./slack.http.patch.json5 --dry-runopenclaw config patch --file ./slack.http.patch.json5
[/code]

* ### Start gateway

bashCopy code
[code]
    openclaw gateway
[/code]

## Transportabstimmung für Socket Mode

OpenClaw setzt den Pong-Timeout des Slack-SDK-Clients für Socket Mode standardmäßig auf 15 Sekunden. Überschreiben Sie die Transporteinstellungen nur, wenn Sie Workspace- oder Host-spezifische Abstimmung benötigen:

json5Copy code
[code]
    {  channels: {    slack: {      mode: "socket",      socketMode: {        clientPingTimeout: 20000,        serverPingTimeout: 30000,        pingPongLoggingEnabled: false,      },    },  },}
[/code]

Verwenden Sie dies nur für Socket-Mode-Workspaces, die Slack-WebSocket-Pong- oder Server-Ping-Timeouts protokollieren, oder für Hosts mit bekannter Event-Loop-Auslastung. `clientPingTimeout` ist die Wartezeit auf Pong, nachdem das SDK einen Client-Ping gesendet hat; `serverPingTimeout` ist die Wartezeit auf Slack-Server-Pings. App-Nachrichten und Ereignisse bleiben Anwendungszustand, keine Signale für Transport-Liveness.

## Manifest- und Scope-Checkliste

Das Basismanifest der Slack-App ist für Socket Mode und HTTP Request URLs identisch. Nur der Block `settings` (und die Slash-Befehls-`url`) unterscheidet sich.

Basemanifest (Socket Mode als Standard):

jsonCopy code
[code]
    {  "display_information": {    "name": "OpenClaw",    "description": "Slack connector for OpenClaw"  },  "features": {    "bot_user": { "display_name": "OpenClaw", "always_online": true },    "app_home": {      "home_tab_enabled": true,      "messages_tab_enabled": true,      "messages_tab_read_only_enabled": false    },    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false      }    ]  },  "oauth_config": {    "scopes": {      "bot": [        "app_mentions:read",        "assistant:write",        "channels:history",        "channels:read",        "chat:write",        "commands",        "emoji:read",        "files:read",        "files:write",        "groups:history",        "groups:read",        "im:history",        "im:read",        "im:write",        "mpim:history",        "mpim:read",        "mpim:write",        "pins:read",        "pins:write",        "reactions:read",        "reactions:write",        "usergroups:read",        "users:read"      ]    }  },  "settings": {    "socket_mode_enabled": true,    "event_subscriptions": {      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    }  }}
[/code]

Für den **Modus HTTP Request URLs** ersetzen Sie `settings` durch die HTTP-Variante und fügen jedem Slash-Befehl `url` hinzu. Öffentliche URL erforderlich:

jsonCopy code
[code]
    {  "features": {    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false,        "url": "https://gateway-host.example.com/slack/events"      }    ]  },  "settings": {    "event_subscriptions": {      "request_url": "https://gateway-host.example.com/slack/events",      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    },    "interactivity": {      "is_enabled": true,      "request_url": "https://gateway-host.example.com/slack/events",      "message_menu_options_url": "https://gateway-host.example.com/slack/events"    }  }}
[/code]

### Zusätzliche Manifest-Einstellungen

Stellen Sie unterschiedliche Funktionen bereit, die die obigen Standards erweitern.

Das Standardmanifest aktiviert den Slack App Home-Tab **Home** und abonniert `app_home_opened`. Wenn ein Workspace-Mitglied den Home-Tab öffnet, veröffentlicht OpenClaw mit `views.publish` eine sichere Standard-Home-Ansicht; es ist kein Konversations-Payload und keine private Konfiguration enthalten. Der Tab **Messages** bleibt für Slack-DMs aktiviert.

Optional native slash commands

Mehrere native Slash-Befehle können anstelle eines einzelnen konfigurierten Befehls mit Feinabstimmung verwendet werden:

  * Verwenden Sie `/agentstatus` statt `/status`, weil der Befehl `/status` reserviert ist.
  * Es können höchstens 25 Slash-Befehle gleichzeitig verfügbar gemacht werden.


Ersetzen Sie Ihren vorhandenen Abschnitt `features.slash_commands` durch eine Teilmenge der [verfügbaren Befehle](</de/tools/slash-commands#command-list>):

### Socket Mode (default)

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]"},{"command": "/reset","description": "Reset the current session"},{"command": "/compact","description": "Compact the session context","usage_hint": "[instructions]"},{"command": "/stop","description": "Stop the current run"},{"command": "/session","description": "Manage thread-binding expiry","usage_hint": "idle <duration|off> or max-age <duration|off>"},{"command": "/think","description": "Set the thinking level","usage_hint": "<level>"},{"command": "/verbose","description": "Toggle verbose output","usage_hint": "on|off|full"},{"command": "/fast","description": "Show or set fast mode","usage_hint": "[status|on|off]"},{"command": "/reasoning","description": "Toggle reasoning visibility","usage_hint": "[on|off|stream]"},{"command": "/elevated","description": "Toggle elevated mode","usage_hint": "[on|off|ask|full]"},{"command": "/exec","description": "Show or set exec defaults","usage_hint": "host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>"},{"command": "/model","description": "Show or set the model","usage_hint": "[name|#|status]"},{"command": "/models","description": "List providers/models","usage_hint": "[provider] [page] [limit=<n>|size=<n>|all]"},{"command": "/help","description": "Show the short help summary"},{"command": "/commands","description": "Show the generated command catalog"},{"command": "/tools","description": "Show what the current agent can use right now","usage_hint": "[compact|verbose]"},{"command": "/agentstatus","description": "Show runtime status, including provider usage/quota when available"},{"command": "/tasks","description": "List active/recent background tasks for the current session"},{"command": "/context","description": "Explain how context is assembled","usage_hint": "[list|detail|json]"},{"command": "/whoami","description": "Show your sender identity"},{"command": "/skill","description": "Run a skill by name","usage_hint": "<name> [input]"},{"command": "/btw","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/side","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/usage","description": "Control the usage footer or show cost summary","usage_hint": "off|tokens|full|cost"}]}
[/code]

### HTTP Request URLs

Verwenden Sie dieselbe Liste `slash_commands` wie oben für Socket Mode und fügen Sie jedem Eintrag `"url": "https://gateway-host.example.com/slack/events"` hinzu. Beispiel:

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]","url": "https://gateway-host.example.com/slack/events"},{"command": "/help","description": "Show the short help summary","url": "https://gateway-host.example.com/slack/events"}]}
[/code]

Wiederholen Sie diesen `url`-Wert für jeden Befehl in der Liste.

Optionale Autorschafts-Scopes (Schreibvorgänge)

Fügen Sie den Bot-Scope `chat:write.customize` hinzu, wenn ausgehende Nachrichten die aktive Agent-Identität (benutzerdefinierter Benutzername und Symbol) statt der standardmäßigen Slack-App-Identität verwenden sollen.

Wenn Sie ein Emoji-Symbol verwenden, erwartet Slack die Syntax `:emoji_name:`.

Optionale Benutzer-Token-Scopes (Lesevorgänge)

Wenn Sie `channels.slack.userToken` konfigurieren, sind typische Lese-Scopes:

  * `channels:history`, `groups:history`, `im:history`, `mpim:history`
  * `channels:read`, `groups:read`, `im:read`, `mpim:read`
  * `users:read`
  * `reactions:read`
  * `pins:read`
  * `emoji:read`
  * `search:read` (wenn Sie von Slack-Suchlesevorgängen abhängen)


## Token-Modell

  * `botToken` \+ `appToken` sind für Socket Mode erforderlich.
  * HTTP-Modus erfordert `botToken` \+ `signingSecret`.
  * `botToken`, `appToken`, `signingSecret` und `userToken` akzeptieren Klartextzeichenfolgen oder SecretRef-Objekte.
  * Konfigurations-Token überschreiben den Env-Fallback.
  * Der Env-Fallback `SLACK_BOT_TOKEN` / `SLACK_APP_TOKEN` gilt nur für das Standardkonto.
  * `userToken` (`xoxp-...`) ist nur in der Konfiguration verfügbar (kein Env-Fallback) und verwendet standardmäßig schreibgeschütztes Verhalten (`userTokenReadOnly: true`).


Verhalten der Statusmomentaufnahme:

  * Die Slack-Kontoprüfung verfolgt pro Zugangsdaten die Felder `*Source` und `*Status` (`botToken`, `appToken`, `signingSecret`, `userToken`).
  * Der Status ist `available`, `configured_unavailable` oder `missing`.
  * `configured_unavailable` bedeutet, dass das Konto über SecretRef oder eine andere nicht inline angegebene Secret-Quelle konfiguriert ist, der aktuelle Befehls-/Laufzeitpfad den tatsächlichen Wert jedoch nicht auflösen konnte.
  * Im HTTP-Modus ist `signingSecretStatus` enthalten; im Socket Mode ist das erforderliche Paar `botTokenStatus` \+ `appTokenStatus`.


## Aktionen und Gates

Slack-Aktionen werden über `channels.slack.actions.*` gesteuert.

Verfügbare Aktionsgruppen im aktuellen Slack-Tooling:

Gruppe | Standard  
---|---  
messages | aktiviert  
reactions | aktiviert  
pins | aktiviert  
memberInfo | aktiviert  
emojiList | aktiviert  
  
Aktuelle Slack-Nachrichtenaktionen umfassen `send`, `upload-file`, `download-file`, `read`, `edit`, `delete`, `pin`, `unpin`, `list-pins`, `member-info` und `emoji-list`. `download-file` akzeptiert Slack-Datei-IDs, die in Platzhaltern für eingehende Dateien angezeigt werden, und gibt Bildvorschauen für Bilder oder lokale Dateimetadaten für andere Dateitypen zurück.

## Zugriffskontrolle und Routing

### DM-Richtlinie

`channels.slack.dmPolicy` steuert den DM-Zugriff. `channels.slack.allowFrom` ist die kanonische DM-Allowlist.

  * `pairing` (Standard)
  * `allowlist`
  * `open` (erfordert, dass `channels.slack.allowFrom` `"*"` enthält)
  * `disabled`


DM-Flags:

  * `dm.enabled` (standardmäßig true)
  * `channels.slack.allowFrom`
  * `dm.allowFrom` (Legacy)
  * `dm.groupEnabled` (Gruppen-DMs standardmäßig false)
  * `dm.groupChannels` (optionale MPIM-Allowlist)


Vorrang bei mehreren Konten:

  * `channels.slack.accounts.default.allowFrom` gilt nur für das Konto `default`.
  * Benannte Konten erben `channels.slack.allowFrom`, wenn ihr eigenes `allowFrom` nicht gesetzt ist.
  * Benannte Konten erben `channels.slack.accounts.default.allowFrom` nicht.


Legacy-`channels.slack.dm.policy` und `channels.slack.dm.allowFrom` werden aus Kompatibilitätsgründen weiterhin gelesen. `openclaw doctor --fix` migriert sie zu `dmPolicy` und `allowFrom`, wenn dies ohne Änderung des Zugriffs möglich ist.

Pairing in DMs verwendet `openclaw pairing approve slack <code>`.

### Channel-Richtlinie

`channels.slack.groupPolicy` steuert die Channel-Behandlung:

  * `open`
  * `allowlist`
  * `disabled`


Die Channel-Allowlist befindet sich unter `channels.slack.channels` und **muss stabile Slack-Channel-IDs** (zum Beispiel `C12345678`) als Konfigurationsschlüssel verwenden.

Laufzeithinweis: Wenn `channels.slack` vollständig fehlt (reine Env-Einrichtung), fällt die Laufzeit auf `groupPolicy="allowlist"` zurück und protokolliert eine Warnung (auch wenn `channels.defaults.groupPolicy` gesetzt ist).

Namens-/ID-Auflösung:

  * Channel-Allowlist-Einträge und DM-Allowlist-Einträge werden beim Start aufgelöst, wenn der Token-Zugriff dies erlaubt
  * nicht aufgelöste Channel-Namenseinträge werden wie konfiguriert beibehalten, aber standardmäßig für das Routing ignoriert
  * eingehende Autorisierung und Channel-Routing sind standardmäßig ID-first; direkte Benutzername-/Slug-Übereinstimmung erfordert `channels.slack.dangerouslyAllowNameMatching: true`


### Erwähnungen und Channel-Benutzer

Channel-Nachrichten sind standardmäßig durch Erwähnungen gated.

Erwähnungsquellen:

  * explizite App-Erwähnung (`<@botId>`)
  * Slack-Benutzergruppen-Erwähnung (`<!subteam^S...>`), wenn der Bot-Benutzer Mitglied dieser Benutzergruppe ist; erfordert `usergroups:read`
  * Erwähnungs-Regex-Muster (`agents.list[].groupChat.mentionPatterns`, Fallback `messages.groupChat.mentionPatterns`)
  * implizites Antwort-an-Bot-Thread-Verhalten (deaktiviert, wenn `thread.requireExplicitMention` `true` ist)


Steuerungen pro Channel (`channels.slack.channels.<id>`; Namen nur über Startauflösung oder `dangerouslyAllowNameMatching`):

  * `requireMention`
  * `users` (Allowlist)
  * `allowBots`
  * `skills`
  * `systemPrompt`
  * `tools`, `toolsBySender`
  * Schlüsselformat für `toolsBySender`: `channel:`, `id:`, `e164:`, `username:`, `name:` oder `"*"`-Wildcard (Legacy-Schlüssel ohne Präfix werden weiterhin nur `id:` zugeordnet)


`allowBots` ist für Channels und private Channels konservativ: Von Bots verfasste Raumnachrichten werden nur akzeptiert, wenn der sendende Bot explizit in der `users`-Allowlist dieses Raums aufgeführt ist oder wenn mindestens eine explizite Slack-Owner-ID aus `channels.slack.allowFrom` derzeit Mitglied des Raums ist. Wildcards und Owner-Einträge mit Anzeigenamen erfüllen die Owner-Präsenz nicht. Die Owner-Präsenz verwendet Slack `conversations.members`; stellen Sie sicher, dass die App den passenden Lese-Scope für den Raumtyp hat (`channels:read` für öffentliche Channels, `groups:read` für private Channels). Wenn die Mitgliedersuche fehlschlägt, verwirft OpenClaw die von einem Bot verfasste Raumnachricht.

## Threads, Sitzungen und Antwort-Tags

  * DMs routen als `direct`; Channels als `channel`; MPIMs als `group`.
  * Slack-Routenbindungen akzeptieren rohe Peer-IDs sowie Slack-Zielformen wie `channel:C12345678`, `user:U12345678` und `<@U12345678>`.
  * Mit dem Standardwert `session.dmScope=main` werden Slack-DMs auf die Hauptsitzung des Agenten zusammengeführt.
  * Channel-Sitzungen: `agent:<agentId>:slack:channel:<channelId>`.
  * Thread-Antworten können gegebenenfalls Thread-Sitzungssuffixe (`:thread:<threadTs>`) erstellen.
  * In Channels, in denen OpenClaw Top-Level-Nachrichten ohne explizite Erwähnung verarbeitet, routet ein nicht auf `off` gesetzter `replyToMode` jede verarbeitete Root-Nachricht nach `agent:<agentId>:slack:channel:<channelId>:thread:<rootTs>`, sodass der sichtbare Slack-Thread ab dem ersten Turn einer OpenClaw-Sitzung zugeordnet wird.
  * Standard für `channels.slack.thread.historyScope` ist `thread`; Standard für `thread.inheritParent` ist `false`.
  * `channels.slack.thread.initialHistoryLimit` steuert, wie viele vorhandene Thread-Nachrichten abgerufen werden, wenn eine neue Thread-Sitzung startet (Standard `20`; setzen Sie `0`, um dies zu deaktivieren).
  * `channels.slack.thread.requireExplicitMention` (Standard `false`): Wenn `true`, werden implizite Thread-Erwähnungen unterdrückt, sodass der Bot innerhalb von Threads nur auf explizite `@bot`-Erwähnungen antwortet, selbst wenn der Bot bereits am Thread beteiligt war. Ohne dies umgehen Antworten in einem Thread mit Bot-Beteiligung das `requireMention`-Gating.


Steuerungen für Antwort-Threads:

  * `channels.slack.replyToMode`: `off|first|all|batched` (Standard `off`)
  * `channels.slack.replyToModeByChatType`: pro `direct|group|channel`
  * Legacy-Fallback für direkte Chats: `channels.slack.dm.replyToMode`


Manuelle Antwort-Tags werden unterstützt:

  * `[[reply_to_current]]`
  * `[[reply_to:<id>]]`


Für explizite Slack-Thread-Antworten aus dem `message`-Tool setzen Sie `replyBroadcast: true` mit `action: "send"` und `threadId` oder `replyTo`, um Slack anzuweisen, die Thread-Antwort zusätzlich im übergeordneten Channel zu broadcasten. Dies wird dem Slack-Flag `chat.postMessage` `reply_broadcast` zugeordnet und wird nur für Text- oder Block-Kit-Sendungen unterstützt, nicht für Medien-Uploads.

Wenn ein `message`-Tool-Aufruf innerhalb eines Slack-Threads ausgeführt wird und denselben Channel adressiert, erbt OpenClaw normalerweise den aktuellen Slack-Thread gemäß `replyToMode`. Setzen Sie `topLevel: true` bei `action: "send"` oder `action: "upload-file"`, um stattdessen eine neue Nachricht im übergeordneten Channel zu erzwingen. `threadId: null` wird als dieselbe Top-Level-Abwahl akzeptiert.

## Bestätigungsreaktionen

`ackReaction` sendet ein Bestätigungs-Emoji, während OpenClaw eine eingehende Nachricht verarbeitet.

Auflösungsreihenfolge:

  * `channels.slack.accounts.<accountId>.ackReaction`
  * `channels.slack.ackReaction`
  * `messages.ackReaction`
  * Fallback auf Agent-Identitäts-Emoji (`agents.list[].identity.emoji`, sonst "👀")


Hinweise:

  * Slack erwartet Shortcodes (zum Beispiel `"eyes"`).
  * Verwenden Sie `""`, um die Reaktion für das Slack-Konto oder global zu deaktivieren.


## Text-Streaming

`channels.slack.streaming` steuert das Live-Vorschauverhalten:

  * `off`: Live-Vorschau-Streaming deaktivieren.
  * `partial` (Standard): Vorschautext durch die neueste Teilausgabe ersetzen.
  * `block`: fragmentierte Vorschau-Updates anhängen.
  * `progress`: Fortschrittsstatustext während der Generierung anzeigen und anschließend den endgültigen Text senden.
  * `streaming.preview.toolProgress`: Wenn die Entwurfsvorschau aktiv ist, Tool-/Fortschrittsupdates in dieselbe bearbeitete Vorschaunachricht routen (Standard: `true`). Setzen Sie `false`, um separate Tool-/Fortschrittsnachrichten beizubehalten.
  * `streaming.preview.commandText` / `streaming.progress.commandText`: Auf `status` setzen, um kompakte Tool-Fortschrittszeilen beizubehalten und rohen Befehls-/Exec-Text auszublenden (Standard: `raw`).


Rohen Befehls-/Exec-Text ausblenden und kompakte Fortschrittszeilen beibehalten:

jsonCopy code
[code]
    {  "channels": {    "slack": {      "streaming": {        "mode": "progress",        "progress": {          "toolProgress": true,          "commandText": "status"        }      }    }  }}
[/code]

`channels.slack.streaming.nativeTransport` steuert natives Slack-Text-Streaming, wenn `channels.slack.streaming.mode` `partial` ist (Standard: `true`).

  * Ein Antwort-Thread muss verfügbar sein, damit natives Text-Streaming und der Slack-Assistenten-Threadstatus angezeigt werden. Die Thread-Auswahl folgt weiterhin `replyToMode`.
  * Channel-, Gruppenchat- und Top-Level-DM-Wurzeln können weiterhin die normale Entwurfsvorschau verwenden, wenn natives Streaming nicht verfügbar ist oder kein Antwort-Thread vorhanden ist.
  * Top-Level-Slack-DMs bleiben standardmäßig außerhalb von Threads, daher zeigen sie keine native Slack-Stream-/Statusvorschau im Thread-Stil; OpenClaw postet und bearbeitet stattdessen eine Entwurfsvorschau in der DM.
  * Medien und Nicht-Text-Payloads fallen auf die normale Zustellung zurück.
  * Medien-/Fehler-Finals brechen ausstehende Vorschau-Bearbeitungen ab; geeignete Text-/Block-Finals werden nur ausgegeben, wenn sie die Vorschau direkt bearbeiten können.
  * Wenn Streaming mitten in einer Antwort fehlschlägt, fällt OpenClaw für die verbleibenden Payloads auf die normale Zustellung zurück.


Entwurfsvorschau anstelle des nativen Slack-Text-Streamings verwenden:

json5Copy code
[code]
    {  channels: {    slack: {      streaming: {        mode: "partial",        nativeTransport: false,      },    },  },}
[/code]

Legacy-Schlüssel:

  * `channels.slack.streamMode` (`replace | status_final | append`) ist ein Legacy-Laufzeitalias für `channels.slack.streaming.mode`.
  * Der boolesche Wert `channels.slack.streaming` ist ein Legacy-Laufzeitalias für `channels.slack.streaming.mode` und `channels.slack.streaming.nativeTransport`.
  * Das Legacy-`channels.slack.nativeStreaming` ist ein Laufzeitalias für `channels.slack.streaming.nativeTransport`.
  * Führen Sie `openclaw doctor --fix` aus, um persistierte Slack-Streaming-Konfigurationen auf die kanonischen Schlüssel umzuschreiben.


## Fallback für Tipp-Reaktion

`typingReaction` fügt der eingehenden Slack-Nachricht eine temporäre Reaktion hinzu, während OpenClaw eine Antwort verarbeitet, und entfernt sie wieder, wenn der Lauf abgeschlossen ist. Das ist vor allem außerhalb von Thread-Antworten nützlich, die eine standardmäßige Statusanzeige „tippt gerade...“ verwenden.

Auflösungsreihenfolge:

  * `channels.slack.accounts.<accountId>.typingReaction`
  * `channels.slack.typingReaction`


Hinweise:

  * Slack erwartet Shortcodes (zum Beispiel `"hourglass_flowing_sand"`).
  * Die Reaktion erfolgt nach bestem Aufwand, und die Bereinigung wird automatisch versucht, nachdem der Antwort- oder Fehlerpfad abgeschlossen ist.


## Medien, Chunking und Zustellung

Eingehende Anhänge

Slack-Dateianhänge werden von Slack-gehosteten privaten URLs heruntergeladen (token-authentifizierter Anfragefluss) und in den Medienspeicher geschrieben, wenn der Abruf erfolgreich ist und Größenlimits es zulassen. Datei-Platzhalter enthalten die Slack-`fileId`, damit Agenten die Originaldatei mit `download-file` abrufen können.

Downloads verwenden begrenzte Leerlauf- und Gesamt-Timeouts. Wenn das Abrufen von Slack-Dateien stockt oder fehlschlägt, verarbeitet OpenClaw die Nachricht weiter und fällt auf den Datei-Platzhalter zurück.

Die Laufzeit-Größenobergrenze für eingehende Dateien ist standardmäßig `20MB`, sofern sie nicht durch `channels.slack.mediaMaxMb` überschrieben wird.

Ausgehender Text und Dateien

  * Text-Chunks verwenden `channels.slack.textChunkLimit` (Standard 4000)
  * `channels.slack.chunkMode="newline"` aktiviert absatzpriorisierte Aufteilung
  * Dateiübertragungen verwenden Slack-Upload-APIs und können Thread-Antworten (`thread_ts`) enthalten
  * Die Obergrenze für ausgehende Medien folgt `channels.slack.mediaMaxMb`, wenn konfiguriert; andernfalls verwenden Channel-Sendungen MIME-Art-Standardwerte aus der Medienpipeline

Zustellungsziele

Bevorzugte explizite Ziele:

  * `user:<id>` für DMs
  * `channel:<id>` für Channels


Nur-Text-/Nur-Block-Slack-DMs können direkt an Benutzer-IDs posten; Datei-Uploads und Thread-Sendungen öffnen die DM zuerst über Slack-Konversations-APIs, weil diese Pfade eine konkrete Konversations-ID benötigen.

## Befehle und Slash-Verhalten

Slash-Befehle erscheinen in Slack entweder als ein einzelner konfigurierter Befehl oder als mehrere native Befehle. Konfigurieren Sie `channels.slack.slashCommand`, um Befehlsstandardwerte zu ändern:

  * `enabled: false`
  * `name: "openclaw"`
  * `sessionPrefix: "slack:slash"`
  * `ephemeral: true`

txtCopy code
[code]
    /openclaw /help
[/code]

Native Befehle erfordern zusätzliche Manifest-Einstellungen in Ihrer Slack-App und werden stattdessen mit `channels.slack.commands.native: true` oder `commands.native: true` in globalen Konfigurationen aktiviert.

  * Der native Befehls-Automodus ist für Slack **aus** , sodass `commands.native: "auto"` native Slack-Befehle nicht aktiviert.

txtCopy code
[code]
    /help
[/code]

Native Argumentmenüs verwenden eine adaptive Rendering-Strategie, die vor dem Auslösen eines ausgewählten Optionswerts ein Bestätigungsmodal anzeigt:

  * bis zu 5 Optionen: Button-Blöcke
  * 6-100 Optionen: statisches Auswahlmenü
  * mehr als 100 Optionen: externe Auswahl mit asynchroner Optionsfilterung, wenn Interaktivitäts-Options-Handler verfügbar sind
  * überschrittene Slack-Limits: codierte Optionswerte fallen auf Buttons zurück

txtCopy code
[code]
    /think
[/code]

Slash-Sitzungen verwenden isolierte Schlüssel wie `agent:<agentId>:slack:slash:<userId>` und leiten Befehlsausführungen weiterhin mit `CommandTargetSessionKey` an die Ziel-Konversationssitzung weiter.

## Interaktive Antworten

Slack kann von Agenten erstellte interaktive Antwort-Steuerelemente rendern, aber diese Funktion ist standardmäßig deaktiviert.

Global aktivieren:

json5Copy code
[code]
    {  channels: {    slack: {      capabilities: {        interactiveReplies: true,      },    },  },}
[/code]

Oder nur für ein Slack-Konto aktivieren:

json5Copy code
[code]
    {  channels: {    slack: {      accounts: {        ops: {          capabilities: {            interactiveReplies: true,          },        },      },    },  },}
[/code]

Wenn aktiviert, können Agenten Slack-spezifische Antwortdirektiven ausgeben:

  * `[[slack_buttons: Approve:approve, Reject:reject]]`
  * `[[slack_select: Choose a target | Canary:canary, Production:production]]`


Diese Direktiven werden in Slack Block Kit kompiliert und leiten Klicks oder Auswahlen über den bestehenden Slack-Interaktionsereignispfad zurück.

Hinweise:

  * Dies ist eine Slack-spezifische Benutzeroberfläche. Andere Kanäle übersetzen Slack Block Kit-Direktiven nicht in ihre eigenen Schaltflächensysteme.
  * Die interaktiven Callback-Werte sind von OpenClaw generierte opake Tokens, keine direkt vom Agenten verfassten Werte.
  * Wenn generierte interaktive Blöcke die Slack Block Kit-Grenzwerte überschreiten würden, fällt OpenClaw auf die ursprüngliche Textantwort zurück, statt eine ungültige Blocks-Payload zu senden.


## Exec-Genehmigungen in Slack

Slack kann als nativer Genehmigungsclient mit interaktiven Schaltflächen und Interaktionen dienen, statt auf die Weboberfläche oder das Terminal zurückzufallen.

  * Exec-Genehmigungen verwenden `channels.slack.execApprovals.*` für natives DM-/Kanal-Routing.
  * Plugin-Genehmigungen können weiterhin über dieselbe Slack-native Schaltflächenoberfläche aufgelöst werden, wenn die Anfrage bereits in Slack ankommt und die Art der Genehmigungs-ID `plugin:` ist.
  * Die Autorisierung der Genehmigenden wird weiterhin erzwungen: Nur Benutzer, die als Genehmigende identifiziert wurden, können Anfragen über Slack genehmigen oder ablehnen.


Dies verwendet dieselbe gemeinsame Genehmigungsschaltflächen-Oberfläche wie andere Kanäle. Wenn `interactivity` in Ihren Slack-App-Einstellungen aktiviert ist, werden Genehmigungsaufforderungen direkt in der Unterhaltung als Block Kit-Schaltflächen gerendert. Wenn diese Schaltflächen vorhanden sind, sind sie die primäre Genehmigungs-UX; OpenClaw sollte nur dann einen manuellen `/approve`-Befehl einfügen, wenn das Tool-Ergebnis sagt, dass Chat- Genehmigungen nicht verfügbar sind oder die manuelle Genehmigung der einzige Weg ist.

Konfigurationspfad:

  * `channels.slack.execApprovals.enabled`
  * `channels.slack.execApprovals.approvers` (optional; fällt nach Möglichkeit auf `commands.ownerAllowFrom` zurück)
  * `channels.slack.execApprovals.target` (`dm` | `channel` | `both`, Standard: `dm`)
  * `agentFilter`, `sessionFilter`


Slack aktiviert native Exec-Genehmigungen automatisch, wenn `enabled` nicht gesetzt oder `"auto"` ist und mindestens ein Genehmigender aufgelöst wird. Setzen Sie `enabled: false`, um Slack ausdrücklich als nativen Genehmigungsclient zu deaktivieren. Setzen Sie `enabled: true`, um native Genehmigungen zu erzwingen, wenn Genehmigende aufgelöst werden.

Standardverhalten ohne explizite Slack-Exec-Genehmigungskonfiguration:

json5Copy code
[code]
    {  commands: {    ownerAllowFrom: ["slack:U12345678"],  },}
[/code]

Explizite Slack-native Konfiguration ist nur erforderlich, wenn Sie Genehmigende überschreiben, Filter hinzufügen oder die Zustellung an den Ursprungs-Chat aktivieren möchten:

json5Copy code
[code]
    {  channels: {    slack: {      execApprovals: {        enabled: true,        approvers: ["U12345678"],        target: "both",      },    },  },}
[/code]

Gemeinsames `approvals.exec`-Forwarding ist davon getrennt. Verwenden Sie es nur, wenn Exec-Genehmigungsaufforderungen auch an andere Chats oder explizite Out-of-Band-Ziele weitergeleitet werden müssen. Gemeinsames `approvals.plugin`-Forwarding ist ebenfalls getrennt; Slack-native Schaltflächen können Plugin-Genehmigungen weiterhin auflösen, wenn diese Anfragen bereits in Slack ankommen.

Gleich-Chat-`/approve` funktioniert auch in Slack-Kanälen und DMs, die bereits Befehle unterstützen. Siehe [Exec-Genehmigungen](</de/tools/exec-approvals>) für das vollständige Genehmigungs-Forwarding-Modell.

## Ereignisse und Betriebsverhalten

  * Nachrichtenbearbeitungen/-löschungen werden Systemereignissen zugeordnet.
  * Thread-Broadcasts (Thread-Antworten mit „Also send to channel“) werden als normale Benutzernachrichten verarbeitet.
  * Ereignisse zum Hinzufügen/Entfernen von Reaktionen werden Systemereignissen zugeordnet.
  * Ereignisse zu Mitgliederbeitritt/-austritt, Kanalerstellung/-umbenennung und Pin-Hinzufügen/-Entfernen werden Systemereignissen zugeordnet.
  * `channel_id_changed` kann Kanal-Konfigurationsschlüssel migrieren, wenn `configWrites` aktiviert ist.
  * Metadaten zu Kanalthema/-zweck werden als nicht vertrauenswürdiger Kontext behandelt und können in den Routing-Kontext injiziert werden.
  * Thread-Starter und anfängliches Seeding des Thread-Verlaufskontexts werden, sofern zutreffend, nach konfigurierten Sender-Allowlists gefiltert.
  * Blockaktionen und modale Interaktionen geben strukturierte Systemereignisse vom Typ `Slack interaction: ...` mit umfangreichen Payload-Feldern aus: 
    * Blockaktionen: ausgewählte Werte, Labels, Picker-Werte und `workflow_*`-Metadaten
    * modale `view_submission`\- und `view_closed`-Ereignisse mit gerouteten Kanalmetadaten und Formulareingaben


## Konfigurationsreferenz

Primäre Referenz: [Konfigurationsreferenz - Slack](</de/gateway/config-channels#slack>).

Slack-Felder mit hoher Aussagekraft

  * Modus/Auth: `mode`, `botToken`, `appToken`, `signingSecret`, `webhookPath`, `accounts.*`
  * DM-Zugriff: `dm.enabled`, `dmPolicy`, `allowFrom` (veraltet: `dm.policy`, `dm.allowFrom`), `dm.groupEnabled`, `dm.groupChannels`
  * Kompatibilitätsschalter: `dangerouslyAllowNameMatching` (Break-Glass; deaktiviert lassen, sofern nicht erforderlich)
  * Kanalzugriff: `groupPolicy`, `channels.*`, `channels.*.users`, `channels.*.requireMention`
  * Threading/Verlauf: `replyToMode`, `replyToModeByChatType`, `thread.*`, `historyLimit`, `dmHistoryLimit`, `dms.*.historyLimit`
  * Zustellung: `textChunkLimit`, `chunkMode`, `mediaMaxMb`, `streaming`, `streaming.nativeTransport`, `streaming.preview.toolProgress`
  * Unfurls: `unfurlLinks`, `unfurlMedia` zur Steuerung von Link-/Medienvorschauen für `chat.postMessage`
  * Ops/Funktionen: `configWrites`, `commands.native`, `slashCommand.*`, `actions.*`, `userToken`, `userTokenReadOnly`


## Fehlerbehebung

Keine Antworten in Kanälen

Prüfen Sie der Reihe nach:

  * `groupPolicy`
  * Kanal-Allowlist (`channels.slack.channels`) — **Schlüssel müssen Kanal-IDs sein** (`C12345678`), keine Namen (`#channel-name`). Namensbasierte Schlüssel schlagen unter `groupPolicy: "allowlist"` stillschweigend fehl, weil Kanal-Routing standardmäßig zuerst per ID erfolgt. So finden Sie eine ID: Rechtsklicken Sie in Slack auf den Kanal → **Copy link** — der `C...`-Wert am Ende der URL ist die Kanal-ID.
  * `requireMention`
  * kanalbezogene `users`-Allowlist


Nützliche Befehle:

bashCopy code
[code]
    openclaw channels status --probeopenclaw logs --followopenclaw doctor
[/code]

DM-Nachrichten ignoriert

Prüfen Sie:

  * `channels.slack.dm.enabled`
  * `channels.slack.dmPolicy` (oder veraltet `channels.slack.dm.policy`)
  * Pairing-Genehmigungen / Allowlist-Einträge
  * Slack Assistant-DM-Ereignisse: Ausführliche Logs mit `drop message_changed` bedeuten in der Regel, dass Slack ein bearbeitetes Assistant-Thread-Ereignis ohne einen wiederherstellbaren menschlichen Absender in den Nachrichtenmetadaten gesendet hat

bashCopy code
[code]
    openclaw pairing list slack
[/code]

Socket Mode verbindet nicht

Validieren Sie Bot- und App-Tokens sowie die Aktivierung von Socket Mode in den Slack-App-Einstellungen.

Wenn `openclaw channels status --probe --json` `botTokenStatus` oder `appTokenStatus: "configured_unavailable"` anzeigt, ist das Slack-Konto konfiguriert, aber die aktuelle Runtime konnte den SecretRef-gestützten Wert nicht auflösen.

HTTP-Modus empfängt keine Ereignisse

Validieren Sie:

  * Signatur-Secret
  * Webhook-Pfad
  * Slack Request URLs (Events + Interactivity + Slash Commands)
  * eindeutiger `webhookPath` pro HTTP-Konto


Wenn `signingSecretStatus: "configured_unavailable"` in Konto-Snapshots erscheint, ist das HTTP-Konto konfiguriert, aber die aktuelle Runtime konnte das SecretRef-gestützte Signatur-Secret nicht auflösen.

Native-/Slash-Befehle werden nicht ausgelöst

Prüfen Sie, ob Sie Folgendes beabsichtigt haben:

  * nativer Befehlsmodus (`channels.slack.commands.native: true`) mit passenden in Slack registrierten Slash-Befehlen
  * oder einzelner Slash-Befehlsmodus (`channels.slack.slashCommand.enabled: true`)


Prüfen Sie außerdem `commands.useAccessGroups` sowie Kanal-/Benutzer-Allowlists.

## Referenz für Anhang-Vision

Slack kann heruntergeladene Medien an den Agent-Turn anhängen, wenn Slack-Dateidownloads erfolgreich sind und Größenlimits dies zulassen. Bilddateien können über den Pfad für Medienverständnis oder direkt an ein antwortendes vision-fähiges Modell übergeben werden; andere Dateien bleiben als herunterladbarer Dateikontext erhalten, statt als Bildeingabe behandelt zu werden.

### Unterstützte Medientypen

Medientyp | Quelle | Aktuelles Verhalten | Hinweise  
---|---|---|---  
JPEG-/PNG-/GIF-/WebP-Bilder | Slack-Datei-URL | Wird heruntergeladen und für vision-fähige Verarbeitung an den Turn angehängt | Limit pro Datei: `channels.slack.mediaMaxMb` (Standard 20 MB)  
PDF-Dateien | Slack-Datei-URL | Wird heruntergeladen und als Dateikontext für Tools wie `download-file` oder `pdf` bereitgestellt | Slack-Inbound konvertiert PDFs nicht automatisch in Bild-Vision-Eingaben  
Andere Dateien | Slack-Datei-URL | Wird nach Möglichkeit heruntergeladen und als Dateikontext bereitgestellt | Binärdateien werden nicht als Bildeingabe behandelt  
Thread-Antworten | Dateien des Thread-Starters | Dateien der Root-Nachricht können als Kontext hydratisiert werden, wenn die Antwort keine direkten Medien enthält | Starter nur mit Dateien verwenden einen Anhang-Platzhalter  
Nachrichten mit mehreren Bildern | Mehrere Slack-Dateien | Jede Datei wird unabhängig ausgewertet | Slack-Verarbeitung ist auf acht Dateien pro Nachricht begrenzt  
  
### Inbound-Pipeline

Wenn eine Slack-Nachricht mit Dateianhängen eingeht:

  1. OpenClaw lädt die Datei über die private URL von Slack mit dem Bot-Token (`xoxb-...`) herunter.
  2. Die Datei wird bei Erfolg in den Medienspeicher geschrieben.
  3. Heruntergeladene Medienpfade und Inhaltstypen werden dem Inbound-Kontext hinzugefügt.
  4. Bildfähige Modell-/Tool-Pfade können Bildanhänge aus diesem Kontext verwenden.
  5. Nicht-Bilddateien bleiben als Dateimetadaten oder Medienreferenzen für Tools verfügbar, die sie verarbeiten können.


### Vererbung von Thread-Root-Anhängen

Wenn eine Nachricht in einem Thread eingeht (mit einem `thread_ts`-Parent):

  * Wenn die Antwort selbst keine direkten Medien enthält und die enthaltene Root-Nachricht Dateien hat, kann Slack die Root-Dateien als Thread-Starter-Kontext hydratisieren.
  * Direkte Antwortanhänge haben Vorrang vor Anhängen der Root-Nachricht.
  * Eine Root-Nachricht, die nur Dateien und keinen Text enthält, wird mit einem Anhang-Platzhalter dargestellt, damit der Fallback ihre Dateien dennoch einschließen kann.


### Verarbeitung mehrerer Anhänge

Wenn eine einzelne Slack-Nachricht mehrere Dateianhänge enthält:

  * Jeder Anhang wird unabhängig durch die Medien-Pipeline verarbeitet.
  * Heruntergeladene Medienreferenzen werden im Nachrichtenkontext zusammengeführt.
  * Die Verarbeitungsreihenfolge folgt der Dateireihenfolge von Slack in der Event-Payload.
  * Ein Fehler beim Download eines Anhangs blockiert die anderen nicht.


### Größen-, Download- und Modelllimits

  * **Größenlimit** : Standardmäßig 20 MB pro Datei. Konfigurierbar über `channels.slack.mediaMaxMb`.
  * **Downloadfehler** : Dateien, die Slack nicht bereitstellen kann, abgelaufene URLs, nicht zugängliche Dateien, zu große Dateien und Slack-Auth-/Login-HTML-Antworten werden übersprungen, statt als nicht unterstützte Formate gemeldet zu werden.
  * **Vision-Modell** : Die Bildanalyse verwendet das aktive Antwortmodell, wenn es Vision unterstützt, oder das unter `agents.defaults.imageModel` konfigurierte Bildmodell.


### Bekannte Einschränkungen

Szenario | Aktuelles Verhalten | Workaround  
---|---|---  
Abgelaufene Slack-Datei-URL | Datei wird übersprungen; es wird kein Fehler angezeigt | Laden Sie die Datei erneut in Slack hoch  
Vision-Modell nicht konfiguriert | Bildanhänge werden als Medienreferenzen gespeichert, aber nicht als Bilder analysiert | Konfigurieren Sie `agents.defaults.imageModel` oder verwenden Sie ein vision-fähiges Antwortmodell  
Sehr große Bilder (> 20 MB standardmäßig) | Wird gemäß Größenlimit übersprungen | Erhöhen Sie `channels.slack.mediaMaxMb`, wenn Slack dies zulässt  
Weitergeleitete/geteilte Anhänge | Text und von Slack gehostete Bild-/Dateimedien werden nach bestem Aufwand verarbeitet | Teilen Sie sie direkt erneut im OpenClaw-Thread  
PDF-Anhänge | Werden als Datei-/Medienkontext gespeichert, nicht automatisch durch Bild-Vision geleitet | Verwenden Sie `download-file` für Dateimetadaten oder das `pdf`-Tool für die PDF-Analyse  
  
### Zugehörige Dokumentation

  * [Pipeline für Medienverständnis](</de/nodes/media-understanding>)
  * [PDF-Tool](</de/tools/pdf>)
  * Epic: [#51349](<https://github.com/openclaw/openclaw/issues/51349>) — Aktivierung von Slack-Anhang-Vision
  * Regressionstests: [#51353](<https://github.com/openclaw/openclaw/issues/51353>)
  * Live-Verifizierung: [#51354](<https://github.com/openclaw/openclaw/issues/51354>)


## Verwandte Themen

[**Pairing** Koppeln Sie einen Slack-Benutzer mit dem Gateway. ](</de/channels/pairing>) [**Gruppen** Verhalten von Kanälen und Gruppen-DMs. ](</de/channels/groups>) [**Kanal-Routing** Leiten Sie eingehende Nachrichten an Agents weiter. ](</de/channels/channel-routing>) [**Sicherheit** Bedrohungsmodell und Härtung. ](</de/gateway/security>) [**Konfiguration** Konfigurationslayout und Priorität. ](</de/gateway/configuration>) [**Slash-Befehle** Befehlskatalog und Verhalten. ](</de/tools/slash-commands>)

Was this useful?YesNo
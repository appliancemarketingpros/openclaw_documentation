---
title: Klickklack
source_url: https://docs.openclaw.ai/de/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack verbindet OpenClaw über erstklassige ClickClack-Bot-Token mit einem selbst gehosteten ClickClack-Workspace.

Verwenden Sie dies, wenn ein OpenClaw-Agent als ClickClack-Bot-Benutzer erscheinen soll. ClickClack unterstützt unabhängige Service-Bots und benutzereigene Bots; benutzereigene Bots behalten eine `owner_user_id` und erhalten nur die Token-Berechtigungsbereiche, die Sie gewähren.

## Schnelle Einrichtung

Erstellen Sie in ClickClack ein Bot-Token:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

Fügen Sie für einen benutzereigenen Bot `--owner <user_id>` hinzu.

Konfigurieren Sie OpenClaw:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

Führen Sie dann aus:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## Mehrere Bots

Jedes Konto öffnet seine eigene ClickClack-Echtzeitverbindung und verwendet sein eigenes Bot-Token.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` verwendet `api.runtime.llm.complete` direkt für kurze Bot-Antworten. Wenn ein Konto `agentId` festlegt, benötigt OpenClaw das explizite Vertrauensbit `plugins.entries.clickclack.llm.allowAgentIdOverride`, damit das Plugin Completions für diesen Bot-Agenten ausführen kann. Lassen Sie es deaktiviert, wenn Sie nur die Standardroute des Agenten verwenden.

## Ziele

  * `channel:<name-or-id>` sendet an einen Workspace-Kanal. Bloße Ziele verwenden standardmäßig `channel:`.
  * `dm:<user_id>` erstellt eine direkte Unterhaltung mit diesem Benutzer oder verwendet sie erneut.
  * `thread:<message_id>` antwortet in einem vorhandenen Thread.


Beispiele:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## Berechtigungen

ClickClack-Token-Berechtigungsbereiche werden von der ClickClack-API erzwungen.

  * `bot:read`: Workspace-/Kanal-/Nachrichten-/Thread-/DM-/Echtzeit-/Profildaten lesen.
  * `bot:write`: `bot:read` plus Kanalnachrichten, Thread-Antworten, DMs und Uploads.
  * `bot:admin`: `bot:write` plus Kanalerstellung.


OpenClaw benötigt für normalen Agenten-Chat nur `bot:write`.

## Fehlerbehebung

  * `ClickClack is not configured`: Legen Sie `channels.clickclack.token` oder `CLICKCLACK_BOT_TOKEN` fest.
  * `workspace not found`: Legen Sie `workspace` auf die von ClickClack zurückgegebene Workspace-ID oder den Slug fest.
  * Keine eingehenden Antworten: Bestätigen Sie, dass das Token Echtzeit-Lesezugriff hat und der Bot nicht auf seine eigenen Nachrichten antwortet.
  * Kanalversand schlägt fehl: Überprüfen Sie, ob der Bot Mitglied des Workspace ist und `bot:write` hat.


Was this useful?YesNo
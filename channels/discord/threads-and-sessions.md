---
title: Discord threads and sessions
source_url: https://docs.openclaw.ai/channels/discord/threads-and-sessions
scraped_at: 2026-09-14
---

ChannelsMainstream messaging

How Discord threads, forums, and channels map onto OpenClaw sessions.

## Forum channels

Discord forum and media channels only accept thread posts. OpenClaw supports two ways to create them:

  * Send a message to the forum parent (`channel:<forumId>`) to auto-create a thread. The thread title is the first non-empty line of the message (truncated to Discord's 100-character thread-name limit).
  * Use `openclaw message thread create` to create a thread directly. Do not pass `--message-id` for forum channels.


Send to the forum parent to create a thread:

bashCopy code
[code]
    openclaw message send --channel discord --target channel:<forumId> \  --message "Topic title\nBody of the post"
[/code]

Create a forum thread explicitly:

bashCopy code
[code]
    openclaw message thread create --channel discord --target channel:<forumId> \  --thread-name "Topic title" --message "Body of the post"
[/code]

Forum parents do not accept Discord components. If you need components, send to the thread itself (`channel:<threadId>`).

## Session and thread behavior

History, context, and thread behavior

Guild history context:

  * `channels.discord.historyLimit` default `20`
  * fallback: `messages.groupChat.historyLimit`
  * `0` disables


DM history controls:

  * `channels.discord.dmHistoryLimit`
  * `channels.discord.dms["<user_id>"].historyLimit`


Thread behavior:

  * Discord threads route as channel sessions and inherit parent channel config unless overridden.
  * Thread sessions inherit the parent channel's session-level `/model` selection as a model-only fallback; thread-local `/model` selections take precedence, and parent transcript history is not copied unless transcript inheritance is enabled.
  * `channels.discord.thread.inheritParent` (default `false`) opts new auto-threads into seeding from the parent transcript. Per-account override: `channels.discord.accounts.<id>.thread.inheritParent`.
  * Message-tool reactions can resolve `user:<id>` DM targets.
  * `guilds.<guild>.channels.<channel>.requireMention: false` is preserved during reply-stage activation fallback.


Channel topics are injected as **untrusted** context. Allowlists gate who can trigger the agent, not a full supplemental-context redaction boundary.

Thread-bound sessions for subagents

Discord can bind a thread to a session target so follow-up messages in that thread keep routing to the same session (including subagent sessions).

Commands:

  * `/session unbind` remove the current thread binding without closing its agent session
  * `/agents` show active runs and binding state
  * `/session idle <duration|off>` inspect/update inactivity expiry for the current binding
  * `/session max-age <duration|off>` inspect/update hard max age for the current binding


Config:

json5Copy code
[code]
    {session: {threadBindings: {  enabled: true,  idleHours: 24,  maxAgeHours: 0,  spawnSessions: true,  defaultSpawnContext: "fork",},},}
[/code]

Notes:

  * `session.threadBindings.*` is the canonical policy for Discord and Telegram.
  * `spawnSessions` controls auto-create/bind threads for `sessions_spawn({ thread: true })` and ACP thread spawns. Default: `true`.
  * `defaultSpawnContext` controls native subagent context for thread-bound spawns. Default: `"fork"`.
  * Deprecated `spawnSubagentSessions`/`spawnAcpSessions` keys are migrated by `openclaw doctor --fix`.
  * If thread bindings are disabled, thread-bound spawns are unavailable.


See [Sub-agents](</tools/subagents>), [ACP Agents](</tools/acp-agents>), and [Configuration Reference](</gateway/configuration-reference>).

Persistent ACP channel bindings

For stable "always-on" ACP workspaces, configure top-level typed ACP bindings targeting Discord conversations.

Config path: `bindings[]` with `type: "acp"` and `match.channel: "discord"`.

json5Copy code
[code]
    {agents: {entries: {  codex: {    runtime: {      type: "acp",      acp: {        agent: "codex",        backend: "acpx",        mode: "persistent",        cwd: "/workspace/openclaw",      },    },  },},},bindings: [{  type: "acp",  agentId: "codex",  match: {    channel: "discord",    accountId: "default",    peer: { kind: "channel", id: "222222222222222222" },  },  acp: { label: "codex-main" },},],channels: {discord: {  guilds: {    "111111111111111111": {      channels: {        "222222222222222222": {          requireMention: false,        },      },    },  },},},}
[/code]

Notes:

  * `/acp spawn codex --bind here` binds the current channel or thread in place and keeps future messages on the same ACP session. Thread messages inherit the parent channel binding.
  * In a bound channel or thread, `/new` and `/reset` reset the same ACP session in place. Temporary thread bindings can override target resolution while active.
  * `spawnSessions` gates child thread creation/binding via `--thread auto|here`.


See [ACP Agents](</tools/acp-agents>) for binding behavior details.

Was this useful?YesNo

Open issue
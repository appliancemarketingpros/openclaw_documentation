---
title: Advanced overrides and transcripts
source_url: https://docs.openclaw.ai/concepts/active-memory/advanced-options
scraped_at: 2026-09-14
---

AgentsSessions and memory

## Advanced escape hatches

Not part of the recommended setup.

`config.thinking` overrides the sub-agent's thinking level (default `"off"`, since active memory runs in the reply path and extra thinking time directly adds user-visible latency):

json5Copy code
[code]
    thinking: "medium" // default: "off"
[/code]

`config.fastMode` overrides fast mode only for the blocking memory sub-agent. Use `true`, `false`, or `"auto"`; leave it unset to inherit the normal agent, session, and model defaults. `"auto"` uses the recall model's configured `fastAutoOnSeconds` cutoff:

json5Copy code
[code]
    fastMode: true
[/code]

`config.promptAppend` adds operator instructions after the default prompt and before the conversation context — pair it with a custom `toolsAllow` when a non-core memory plugin needs specific tool order or query shaping:

json5Copy code
[code]
    promptAppend: "Prefer stable long-term preferences over one-off events."
[/code]

`config.promptOverride` replaces the default prompt entirely (conversation context is still appended afterward). Not recommended unless deliberately testing a different recall contract — the default prompt is tuned to return either `NONE` or compact user-fact context for the main model:

json5Copy code
[code]
    promptOverride: "You are a memory search agent. Return NONE or one compact user fact."
[/code]

## Transcript persistence

Blocking sub-agent runs keep their runtime transcript in the agent's SQLite store. By default, OpenClaw removes the temporary sub-agent session rows after the run finishes and does not create a JSONL file.

If cleanup crosses the recall deadline, a completed summary grounded in memory results can still be recovered as `timeout_partial` after cleanup settles. This works with temporary transcripts; `persistTranscripts` only controls debugging exports. Failed runs, failed cleanup, and unavailable memory results remain ineligible for timeout recovery. Recovered summaries are not cached or stored in session debug lines.

To export those transcripts as JSONL artifacts for debugging:

json5Copy code
[code]
    {  plugins: {    entries: {      "active-memory": {        enabled: true,        config: {          agents: ["main"],          persistTranscripts: true,          transcriptDir: "active-memory",        },      },    },  },}
[/code]

Exported transcript artifacts go under the OpenClaw state directory, in a plugin-owned, per-agent directory separate from active runtime state:

textCopy code
[code]
    <state-dir>/plugins/active-memory/transcripts/agents/<encoded-agent>/active-memory/<blocking-memory-sub-agent-session-id>.jsonl
[/code]

Agent ids are URI-encoded in this path: for example, `support/agent` becomes `support%2Fagent`. Change the final artifact subdirectory with `config.transcriptDir`. Use this carefully: exports can accumulate quickly on busy sessions, `full` query mode duplicates a lot of conversation context, and these artifacts contain hidden prompt context plus recalled memories.

Was this useful?YesNo

Open issue
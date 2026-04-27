---
title: Trajectory bundles
source_url: https://docs.openclaw.ai/tools/trajectory
scraped_at: 2026-04-27
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools

Trajectory bundles

Trajectory capture is OpenClaw’s per-session flight recorder. It records a structured timeline for each agent run, then `/export-trajectory` packages the current session into a redacted support bundle. Use it when you need to answer questions like:

  * What prompt, system prompt, and tools were sent to the model?
  * Which transcript messages and tool calls led to this answer?
  * Did the run time out, abort, compact, or hit a provider error?
  * Which model, plugins, skills, and runtime settings were active?
  * What usage and prompt-cache metadata did the provider return?


## 

​

Quick start

Send this in the active session:
[code] 
    /export-trajectory
    
[/code]

Alias:
[code] 
    /trajectory
    
[/code]

OpenClaw writes the bundle under the workspace:
[code] 
    .openclaw/trajectory-exports/openclaw-trajectory-<session>-<timestamp>/
    
[/code]

You can choose a relative output directory name:
[code] 
    /export-trajectory bug-1234
    
[/code]

The custom path is resolved inside `.openclaw/trajectory-exports/`. Absolute paths and `~` paths are rejected.

## 

​

Access

Trajectory export is an owner command. The sender must pass the normal command authorization checks and owner checks for the channel.

## 

​

What gets recorded

Trajectory capture is on by default for OpenClaw agent runs. Runtime events include:

  * `session.started`
  * `trace.metadata`
  * `context.compiled`
  * `prompt.submitted`
  * `model.completed`
  * `trace.artifacts`
  * `session.ended`

Transcript events are also reconstructed from the active session branch:

  * user messages
  * assistant messages
  * tool calls
  * tool results
  * compactions
  * model changes
  * labels and custom session entries

Events are written as JSON Lines with this schema marker:
[code] 
    {
      "traceSchema": "openclaw-trajectory",
      "schemaVersion": 1
    }
    
[/code]

## 

​

Bundle files

An exported bundle can contain:

File| Contents  
---|---  
`manifest.json`| Bundle schema, source files, event counts, and generated file list  
`events.jsonl`| Ordered runtime and transcript timeline  
`session-branch.json`| Redacted active transcript branch and session header  
`metadata.json`| OpenClaw version, OS/runtime, model, config snapshot, plugins, skills, and prompt metadata  
`artifacts.json`| Final status, errors, usage, prompt cache, compaction count, assistant text, and tool metadata  
`prompts.json`| Submitted prompts and selected prompt-building details  
`system-prompt.txt`| Latest compiled system prompt, when captured  
`tools.json`| Tool definitions sent to the model, when captured  
  
`manifest.json` lists the files present in that bundle. Some files are omitted when the session did not capture the corresponding runtime data.

## 

​

Capture location

By default, runtime trajectory events are written beside the session file:
[code] 
    <session>.trajectory.jsonl
    
[/code]

OpenClaw also writes a best-effort pointer file beside the session:
[code] 
    <session>.trajectory-path.json
    
[/code]

Set `OPENCLAW_TRAJECTORY_DIR` to store runtime trajectory sidecars in a dedicated directory:
[code] 
    export OPENCLAW_TRAJECTORY_DIR=/var/lib/openclaw/trajectories
    
[/code]

When this variable is set, OpenClaw writes one JSONL file per session id in that directory.

## 

​

Disable capture

Set `OPENCLAW_TRAJECTORY=0` before starting OpenClaw:
[code] 
    export OPENCLAW_TRAJECTORY=0
    
[/code]

This disables runtime trajectory capture. `/export-trajectory` can still export the transcript branch, but runtime-only files such as compiled context, provider artifacts, and prompt metadata may be missing.

## 

​

Privacy and limits

Trajectory bundles are designed for support and debugging, not public posting. OpenClaw redacts sensitive values before writing export files:

  * credentials and known secret-like payload fields
  * image data
  * local state paths
  * workspace paths, replaced with `$WORKSPACE_DIR`
  * home directory paths, where detected

The exporter also bounds input size:

  * runtime sidecar files: 50 MiB
  * session files: 50 MiB
  * runtime events: 200,000
  * total exported events: 250,000
  * individual runtime event lines are truncated above 256 KiB

Review bundles before sharing them outside your team. Redaction is best-effort and cannot know every application-specific secret.

## 

​

Troubleshooting

If the export has no runtime events:

  * confirm OpenClaw was started without `OPENCLAW_TRAJECTORY=0`
  * check whether `OPENCLAW_TRAJECTORY_DIR` points to a writable directory
  * run another message in the session, then export again
  * inspect `manifest.json` for `runtimeEventCount`

If the command rejects the output path:

  * use a relative name like `bug-1234`
  * do not pass `/tmp/...` or `~/...`
  * keep the export inside `.openclaw/trajectory-exports/`

If the export fails with a size error, the session or sidecar exceeded the export safety limits. Start a new session or export a smaller reproduction.

## 

​

Related

  * [Diffs](</tools/diffs>)
  * [Session management](</concepts/session>)
  * [Exec tool](</tools/exec>)


[Tool-loop detection](</tools/loop-detection>)[Text to speech (TTS)](</tools/tts>)

⌘I
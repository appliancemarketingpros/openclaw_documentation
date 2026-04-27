---
title: Tokenjuice
source_url: https://docs.openclaw.ai/tools/tokenjuice
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

Tokenjuice

`tokenjuice` is an optional bundled plugin that compacts noisy `exec` and `bash` tool results after the command has already run. It changes the returned `tool_result`, not the command itself. Tokenjuice does not rewrite shell input, rerun commands, or change exit codes. Today this applies to PI embedded runs and OpenClaw dynamic tools in the Codex app-server harness. Tokenjuice hooks OpenClaw’s tool-result middleware and trims the output before it goes back into the active harness session.

## 

​

Enable the plugin

Fast path:
[code] 
    openclaw config set plugins.entries.tokenjuice.enabled true
    
[/code]

Equivalent:
[code] 
    openclaw plugins enable tokenjuice
    
[/code]

OpenClaw already ships the plugin. There is no separate `plugins install` or `tokenjuice install openclaw` step. If you prefer editing config directly:
[code] 
    {
      plugins: {
        entries: {
          tokenjuice: {
            enabled: true,
          },
        },
      },
    }
    
[/code]

## 

​

What tokenjuice changes

  * Compacts noisy `exec` and `bash` results before they are fed back into the session.
  * Keeps the original command execution untouched.
  * Preserves exact file-content reads and other commands that tokenjuice should leave raw.
  * Stays opt-in: disable the plugin if you want verbatim output everywhere.


## 

​

Verify it is working

  1. Enable the plugin.
  2. Start a session that can call `exec`.
  3. Run a noisy command such as `git status`.
  4. Check that the returned tool result is shorter and more structured than the raw shell output.


## 

​

Disable the plugin
[code] 
    openclaw config set plugins.entries.tokenjuice.enabled false
    
[/code]

Or:
[code] 
    openclaw plugins disable tokenjuice
    
[/code]

## 

​

Related

  * [Exec tool](</tools/exec>)
  * [Thinking levels](</tools/thinking>)
  * [Context engine](</concepts/context-engine>)


[Thinking levels](</tools/thinking>)[Tool-loop detection](</tools/loop-detection>)

⌘I
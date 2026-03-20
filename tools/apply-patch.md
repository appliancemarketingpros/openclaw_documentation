---
title: apply_patch Tool
source_url: https://docs.openclaw.ai/tools/apply-patch
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools

apply_patch Tool

# 

​

apply_patch tool

Apply file changes using a structured patch format. This is ideal for multi-file or multi-hunk edits where a single `edit` call would be brittle. The tool accepts a single `input` string that wraps one or more file operations:

Copy
[code]
    *** Begin Patch
    *** Add File: path/to/file.txt
    +line 1
    +line 2
    *** Update File: src/app.ts
    @@
    -old line
    +new line
    *** Delete File: obsolete.txt
    *** End Patch
    
[/code]

## 

​

Parameters

  * `input` (required): Full patch contents including `*** Begin Patch` and `*** End Patch`.


## 

​

Notes

  * Patch paths support relative paths (from the workspace directory) and absolute paths.
  * `tools.exec.applyPatch.workspaceOnly` defaults to `true` (workspace-contained). Set it to `false` only if you intentionally want `apply_patch` to write/delete outside the workspace directory.
  * Use `*** Move to:` within an `*** Update File:` hunk to rename files.
  * `*** End of File` marks an EOF-only insert when needed.
  * Experimental and disabled by default. Enable with `tools.exec.applyPatch.enabled`.
  * OpenAI-only (including OpenAI Codex). Optionally gate by model via `tools.exec.applyPatch.allowModels`.
  * Config is only under `tools.exec`.


## 

​

Example

Copy
[code]
    {
      "tool": "apply_patch",
      "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"
    }
    
[/code]

[Auth Monitoring](</automation/auth-monitoring>)[Browser (OpenClaw-managed)](</tools/browser>)

⌘I
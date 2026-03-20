---
title: completion
source_url: https://docs.openclaw.ai/cli/completion
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Utility

completion

# 

​

`openclaw completion`

Generate shell completion scripts and optionally install them into your shell profile.

## 

​

Usage

Copy
[code]
    openclaw completion
    openclaw completion --shell zsh
    openclaw completion --install
    openclaw completion --shell fish --install
    openclaw completion --write-state
    openclaw completion --shell bash --write-state
    
[/code]

## 

​

Options

  * `-s, --shell <shell>`: shell target (`zsh`, `bash`, `powershell`, `fish`; default: `zsh`)
  * `-i, --install`: install completion by adding a source line to your shell profile
  * `--write-state`: write completion script(s) to `$OPENCLAW_STATE_DIR/completions` without printing to stdout
  * `-y, --yes`: skip install confirmation prompts


## 

​

Notes

  * `--install` writes a small “OpenClaw Completion” block into your shell profile and points it at the cached script.
  * Without `--install` or `--write-state`, the command prints the script to stdout.
  * Completion generation eagerly loads command trees so nested subcommands are included.


[clawbot](</cli/clawbot>)[dns](</cli/dns>)

⌘I
---
title: Secret Placeholder Conventions
source_url: https://docs.openclaw.ai/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Secret placeholder conventions

Use placeholders that are human-readable but do not resemble real secrets.

## Recommended style

  * Prefer descriptive values like `example-openai-key-not-real` or `example-discord-bot-token`.
  * For shell snippets, prefer `${OPENAI_API_KEY}` over inline token-like strings.
  * Keep examples obviously fake and scoped to purpose (provider, channel, auth type).


## Avoid these patterns in docs

  * Literal PEM private-key header or footer text.
  * Prefixes that resemble live credentials, for example `sk-...`, `xoxb-...`, `AKIA...`.
  * Realistic-looking bearer tokens copied from runtime logs.


## Example

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue
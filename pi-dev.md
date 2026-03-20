---
title: Pi Development Workflow
source_url: https://docs.openclaw.ai/pi-dev
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Developer setup

Pi Development Workflow

# 

​

Pi Development Workflow

This guide summarizes a sane workflow for working on the pi integration in OpenClaw.

## 

​

Type Checking and Linting

  * Type check and build: `pnpm build`
  * Lint: `pnpm lint`
  * Format check: `pnpm format`
  * Full gate before pushing: `pnpm lint && pnpm build && pnpm test`


## 

​

Running Pi Tests

Run the Pi-focused test set directly with Vitest:

Copy
[code]
    pnpm test -- \
      "src/agents/pi-*.test.ts" \
      "src/agents/pi-embedded-*.test.ts" \
      "src/agents/pi-tools*.test.ts" \
      "src/agents/pi-settings.test.ts" \
      "src/agents/pi-tool-definition-adapter*.test.ts" \
      "src/agents/pi-extensions/**/*.test.ts"
    
[/code]

To include the live provider exercise:

Copy
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test -- src/agents/pi-embedded-runner-extraparams.live.test.ts
    
[/code]

This covers the main Pi unit suites:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-extensions/*.test.ts`


## 

​

Manual Testing

Recommended flow:

  * Run the gateway in dev mode:
    * `pnpm gateway:dev`
  * Trigger the agent directly:
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Use the TUI for interactive debugging:
    * `pnpm tui`

For tool call behavior, prompt for a `read` or `exec` action so you can see tool streaming and payload handling.

## 

​

Clean Slate Reset

State lives under the OpenClaw state directory. Default is `~/.openclaw`. If `OPENCLAW_STATE_DIR` is set, use that directory instead. To reset everything:

  * `openclaw.json` for config
  * `credentials/` for auth profiles and tokens
  * `agents/<agentId>/sessions/` for agent session history
  * `agents/<agentId>/sessions.json` for the session index
  * `sessions/` if legacy paths exist
  * `workspace/` if you want a blank workspace

If you only want to reset sessions, delete `agents/<agentId>/sessions/` and `agents/<agentId>/sessions.json` for that agent. Keep `credentials/` if you do not want to reauthenticate.

## 

​

References

  * [Testing](</help/testing>)
  * [Getting Started](</start/getting-started>)


[Setup](</start/setup>)[CI Pipeline](</ci>)

⌘I
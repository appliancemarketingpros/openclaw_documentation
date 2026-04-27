---
title: QA channel
source_url: https://docs.openclaw.ai/channels/qa-channel
scraped_at: 2026-04-27
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Configuration

QA channel

`qa-channel` is a bundled synthetic message transport for automated OpenClaw QA. It is not a production channel. It exists to exercise the same channel plugin boundary used by real transports while keeping state deterministic and fully inspectable.

## 

​

What it does today

  * Slack-class target grammar:
    * `dm:<user>`
    * `channel:<room>`
    * `thread:<room>/<thread>`
  * HTTP-backed synthetic bus for:
    * inbound message injection
    * outbound transcript capture
    * thread creation
    * reactions
    * edits
    * deletes
    * search and read actions
  * Bundled host-side self-check runner that writes a Markdown report


## 

​

Config
[code] 
    {
      "channels": {
        "qa-channel": {
          "baseUrl": "http://127.0.0.1:43123",
          "botUserId": "openclaw",
          "botDisplayName": "OpenClaw QA",
          "allowFrom": ["*"],
          "pollTimeoutMs": 1000
        }
      }
    }
    
[/code]

Supported account keys:

  * `baseUrl`
  * `botUserId`
  * `botDisplayName`
  * `pollTimeoutMs`
  * `allowFrom`
  * `defaultTo`
  * `actions.messages`
  * `actions.reactions`
  * `actions.search`
  * `actions.threads`


## 

​

Runner

Current vertical slice:
[code] 
    pnpm qa:e2e
    
[/code]

This now routes through the bundled `qa-lab` extension. It starts the in-repo QA bus, boots the bundled `qa-channel` runtime slice, runs a deterministic self-check, and writes a Markdown report under `.artifacts/qa-e2e/`. Private debugger UI:
[code] 
    pnpm qa:lab:up
    
[/code]

That one command builds the QA site, starts the Docker-backed gateway + QA Lab stack, and prints the QA Lab URL. From that site you can pick scenarios, choose the model lane, launch individual runs, and watch results live. Full repo-backed QA suite:
[code] 
    pnpm openclaw qa suite
    
[/code]

That launches the private QA debugger at a local URL, separate from the shipped Control UI bundle.

## 

​

Scope

Current scope is intentionally narrow:

  * bus + plugin transport
  * threaded routing grammar
  * channel-owned message actions
  * Markdown reporting
  * Docker-backed QA site with run controls

Follow-up work will add:

  * provider/model matrix execution
  * richer scenario discovery
  * OpenClaw-native orchestration later


## 

​

Related

  * [Pairing](</channels/pairing>)
  * [Groups](</channels/groups>)
  * [Channels overview](</channels>)


[Channel troubleshooting](</channels/troubleshooting>)

⌘I
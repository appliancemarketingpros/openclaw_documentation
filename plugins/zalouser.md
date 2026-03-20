---
title: Zalo Personal Plugin
source_url: https://docs.openclaw.ai/plugins/zalouser
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Zalo Personal Plugin

# 

​

Zalo Personal (plugin)

Zalo Personal support for OpenClaw via a plugin, using native `zca-js` to automate a normal Zalo user account.

> **Warning:** Unofficial automation may lead to account suspension/ban. Use at your own risk.

## 

​

Naming

Channel id is `zalouser` to make it explicit this automates a **personal Zalo user account** (unofficial). We keep `zalo` reserved for a potential future official Zalo API integration.

## 

​

Where it runs

This plugin runs **inside the Gateway process**. If you use a remote Gateway, install/configure it on the **machine running the Gateway** , then restart the Gateway. No external `zca`/`openzca` CLI binary is required.

## 

​

Install

### 

​

Option A: install from npm

Copy
[code]
    openclaw plugins install @openclaw/zalouser
    
[/code]

Restart the Gateway afterwards.

### 

​

Option B: install from a local folder (dev)

Copy
[code]
    openclaw plugins install ./extensions/zalouser
    cd ./extensions/zalouser && pnpm install
    
[/code]

Restart the Gateway afterwards.

## 

​

Config

Channel config lives under `channels.zalouser` (not `plugins.entries.*`):

Copy
[code]
    {
      channels: {
        zalouser: {
          enabled: true,
          dmPolicy: "pairing",
        },
      },
    }
    
[/code]

## 

​

CLI

Copy
[code]
    openclaw channels login --channel zalouser
    openclaw channels logout --channel zalouser
    openclaw channels status --probe
    openclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"
    openclaw directory peers list --channel zalouser --query "name"
    
[/code]

## 

​

Agent tool

Tool name: `zalouser` Actions: `send`, `image`, `link`, `friends`, `groups`, `me`, `status` Channel message actions also support `react` for message reactions.

⌘I
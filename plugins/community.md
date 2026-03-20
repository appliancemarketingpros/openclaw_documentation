---
title: Community Plugins
source_url: https://docs.openclaw.ai/plugins/community
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Plugins

Community Plugins

# 

​

Community Plugins

Community plugins are third-party packages that extend OpenClaw with new channels, tools, providers, or other capabilities. They are built and maintained by the community, published on npm, and installable with a single command.

Copy
[code]
    openclaw plugins install <npm-spec>
    
[/code]

## 

​

Listed plugins

### 

​

Codex App Server Bridge

Independent OpenClaw bridge for Codex App Server conversations. Bind a chat to a Codex thread, talk to it with plain text, and control it with chat-native commands for resume, planning, review, model selection, compaction, and more.

  * **npm:** `openclaw-codex-app-server`
  * **repo:** [github.com/pwrdrvr/openclaw-codex-app-server](<https://github.com/pwrdrvr/openclaw-codex-app-server>)


Copy
[code]
    openclaw plugins install openclaw-codex-app-server
    
[/code]

### 

​

DingTalk

Enterprise robot integration using Stream mode. Supports text, images, and file messages via any DingTalk client.

  * **npm:** `@largezhou/ddingtalk`
  * **repo:** [github.com/largezhou/openclaw-dingtalk](<https://github.com/largezhou/openclaw-dingtalk>)


Copy
[code]
    openclaw plugins install @largezhou/ddingtalk
    
[/code]

### 

​

Lossless Claw (LCM)

Lossless Context Management plugin for OpenClaw. DAG-based conversation summarization with incremental compaction — preserves full context fidelity while reducing token usage.

  * **npm:** `@martian-engineering/lossless-claw`
  * **repo:** [github.com/Martian-Engineering/lossless-claw](<https://github.com/Martian-Engineering/lossless-claw>)


Copy
[code]
    openclaw plugins install @martian-engineering/lossless-claw
    
[/code]

### 

​

Opik

Official plugin that exports agent traces to Opik. Monitor agent behavior, cost, tokens, errors, and more.

  * **npm:** `@opik/opik-openclaw`
  * **repo:** [github.com/comet-ml/opik-openclaw](<https://github.com/comet-ml/opik-openclaw>)


Copy
[code]
    openclaw plugins install @opik/opik-openclaw
    
[/code]

### 

​

QQbot

Connect OpenClaw to QQ via the QQ Bot API. Supports private chats, group mentions, channel messages, and rich media including voice, images, videos, and files.

  * **npm:** `@sliverp/qqbot`
  * **repo:** [github.com/sliverp/qqbot](<https://github.com/sliverp/qqbot>)


Copy
[code]
    openclaw plugins install @sliverp/qqbot
    
[/code]

## 

​

Submit your plugin

We welcome community plugins that are useful, documented, and safe to operate.

1

Publish to npm

Your plugin must be installable via `openclaw plugins install \<npm-spec\>`. See [Building Plugins](</plugins/building-plugins>) for the full guide.

2

Host on GitHub

Source code must be in a public repository with setup docs and an issue tracker.

3

Open a PR

Add your plugin to this page with:

  * Plugin name
  * npm package name
  * GitHub repository URL
  * One-line description
  * Install command


## 

​

Quality bar

Requirement| Why  
---|---  
Published on npm| Users need `openclaw plugins install` to work  
Public GitHub repo| Source review, issue tracking, transparency  
Setup and usage docs| Users need to know how to configure it  
Active maintenance| Recent updates or responsive issue handling  
  
Low-effort wrappers, unclear ownership, or unmaintained packages may be declined.

## 

​

Related

  * [Install and Configure Plugins](</tools/plugin>) — how to install any plugin
  * [Building Plugins](</plugins/building-plugins>) — create your own
  * [Plugin Manifest](</plugins/manifest>) — manifest schema


[Building Plugins](</plugins/building-plugins>)[Plugin Bundles](</plugins/bundles>)

⌘I
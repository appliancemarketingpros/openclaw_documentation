---
title: WeCom
source_url: https://docs.openclaw.ai/channels/wecom
scraped_at: 2026-08-10
---

ChannelsRegional platforms

OpenClaw exposes WeCom through the external `@wecom/wecom-openclaw-plugin` package maintained by the Tencent WeCom team. The plugin is listed in OpenClaw's official channel catalog but is not bundled with the core install.

## Install

bashCopy code
[code]
    openclaw channels add --channel wecomopenclaw gateway restartopenclaw channels status --channel wecom
[/code]

The OpenClaw catalog installs an exact version of `@wecom/wecom-openclaw-plugin`.

## Configure

WeCom credentials, connection modes, callback routes, and access-control behavior belong to the external plugin and can change independently of OpenClaw. Follow the [package documentation](<https://www.npmjs.com/package/@wecom/wecom-openclaw-plugin>) for the installed release before configuring the channel.

When upgrading the plugin independently, keep using the documentation for the installed version.

Was this useful?YesNo

Open issue
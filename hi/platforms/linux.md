---
title: Linux ऐप
source_url: https://docs.openclaw.ai/hi/platforms/linux
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

The Gateway Linux पर पूरी तरह समर्थित है। **Node अनुशंसित runtime है** । Gateway के लिए Bun अनुशंसित नहीं है (WhatsApp/Telegram bugs)।

Native Linux companion apps योजनाबद्ध हैं। यदि आप कोई बनाने में मदद करना चाहते हैं, तो योगदानों का स्वागत है।

## शुरुआती त्वरित मार्ग (VPS)

  1. Node 24 इंस्टॉल करें (अनुशंसित; Node 22 LTS, वर्तमान में `22.19+`, compatibility के लिए अभी भी काम करता है)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. अपने laptop से: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. `http://127.0.0.1:18789/` खोलें और configured shared secret से authenticate करें (default रूप से token; यदि आपने `gateway.auth.mode: "password"` सेट किया है तो password)


पूर्ण Linux server guide: [Linux Server](</hi/vps>). चरण-दर-चरण VPS उदाहरण: [exe.dev](</hi/install/exe-dev>)

## इंस्टॉल करें

  * [शुरू करना](</hi/start/getting-started>)
  * [इंस्टॉल और updates](</hi/install/updating>)
  * वैकल्पिक flows: [Bun (experimental)](</hi/install/bun>), [Nix](</hi/install/nix>), [Docker](</hi/install/docker>)


## Gateway

  * [Gateway runbook](</hi/gateway>)
  * [Configuration](</hi/gateway/configuration>)


## Gateway service install (CLI)

इनमें से एक का उपयोग करें:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

या:

CodeCopy code
[code]
    openclaw gateway install
[/code]

या:

CodeCopy code
[code]
    openclaw configure
[/code]

Prompt आने पर **Gateway service** चुनें।

Repair/migrate:

CodeCopy code
[code]
    openclaw doctor
[/code]

## System control (systemd user unit)

OpenClaw default रूप से systemd **user** service इंस्टॉल करता है। Shared या always-on servers के लिए **system** service का उपयोग करें। `openclaw gateway install` और `openclaw onboard --install-daemon` पहले से ही आपके लिए current canonical unit render करते हैं; custom system/service-manager setup की जरूरत हो तभी इसे हाथ से लिखें। पूरी service guidance [Gateway runbook](</hi/gateway>) में है।

Minimal setup:

`~/.config/systemd/user/openclaw-gateway[-<profile>].service` बनाएं:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143OOMPolicy=continueKillMode=control-group [Install]WantedBy=default.target
[/code]

इसे enable करें:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## Memory pressure और OOM kills

Linux पर, जब किसी host, VM, या container cgroup की memory समाप्त हो जाती है, तो kernel एक OOM victim चुनता है। Gateway खराब victim हो सकता है क्योंकि यह long-lived sessions और channel connections का मालिक होता है। इसलिए OpenClaw, जहां संभव हो, transient child processes को Gateway से पहले kill किए जाने के लिए bias करता है।

Eligible Linux child spawns के लिए, OpenClaw child को एक छोटे `/bin/sh` wrapper के जरिए शुरू करता है, जो child के अपने `oom_score_adj` को `1000` तक बढ़ाता है, फिर real command को `exec` करता है। यह unprivileged operation है क्योंकि child केवल अपनी OOM kill likelihood बढ़ा रहा होता है।

Covered child process surfaces में शामिल हैं:

  * supervisor-managed command children,
  * PTY shell children,
  * MCP stdio server children,
  * OpenClaw-launched browser/Chrome processes.


Wrapper केवल Linux के लिए है और `/bin/sh` उपलब्ध न होने पर skip किया जाता है। इसे तब भी skip किया जाता है यदि child env `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`, `false`, `no`, या `off` सेट करता है।

Child process verify करने के लिए:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

Covered children के लिए expected value `1000` है। Gateway process को अपना normal score रखना चाहिए, आमतौर पर `0`।

Recommended systemd unit `OOMPolicy=continue` भी सेट करता है। इससे OOM killer द्वारा transient child process चुने जाने पर Gateway unit alive रहती है; child command/session fail हो सकता है और systemd द्वारा पूरे gateway service को failed mark करके सभी channels restart किए बिना अपनी error report कर सकता है।

यह normal memory tuning को replace नहीं करता। यदि कोई VPS या container बार-बार children को kill करता है, तो memory limit बढ़ाएं, concurrency घटाएं, या systemd `MemoryMax=` या container-level memory limits जैसे stronger resource controls जोड़ें।

## संबंधित

  * [Install overview](</hi/install>)
  * [Linux server](</hi/vps>)
  * [Raspberry Pi](</hi/install/raspberry-pi>)


Was this useful?YesNo

Open issue
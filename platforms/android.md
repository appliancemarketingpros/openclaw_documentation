---
title: Android App
source_url: https://docs.openclaw.ai/platforms/android
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Platforms overview

Android App

# 

​

Android App (Node)

> **Note:** The Android app has not been publicly released yet. The source code is available in the [OpenClaw repository](<https://github.com/openclaw/openclaw>) under `apps/android`. You can build it yourself using Java 17 and the Android SDK (`./gradlew :app:assemblePlayDebug`). See [apps/android/README.md](<https://github.com/openclaw/openclaw/blob/main/apps/android/README.md>) for build instructions.

## 

​

Support snapshot

  * Role: companion node app (Android does not host the Gateway).
  * Gateway required: yes (run it on macOS, Linux, or Windows via WSL2).
  * Install: [Getting Started](</start/getting-started>) \+ [Pairing](</channels/pairing>).
  * Gateway: [Runbook](</gateway>) \+ [Configuration](</gateway/configuration>).
    * Protocols: [Gateway protocol](</gateway/protocol>) (nodes + control plane).


## 

​

System control

System control (launchd/systemd) lives on the Gateway host. See [Gateway](</gateway>).

## 

​

Connection Runbook

Android node app ⇄ (mDNS/NSD + WebSocket) ⇄ **Gateway** Android connects directly to the Gateway WebSocket (default `ws://<host>:18789`) and uses device pairing (`role: node`).

### 

​

Prerequisites

  * You can run the Gateway on the “master” machine.
  * Android device/emulator can reach the gateway WebSocket:
    * Same LAN with mDNS/NSD, **or**
    * Same Tailscale tailnet using Wide-Area Bonjour / unicast DNS-SD (see below), **or**
    * Manual gateway host/port (fallback)
  * You can run the CLI (`openclaw`) on the gateway machine (or via SSH).


### 

​

1) Start the Gateway

Copy
[code]
    openclaw gateway --port 18789 --verbose
    
[/code]

Confirm in logs you see something like:

  * `listening on ws://0.0.0.0:18789`

For tailnet-only setups (recommended for Vienna ⇄ London), bind the gateway to the tailnet IP:

  * Set `gateway.bind: "tailnet"` in `~/.openclaw/openclaw.json` on the gateway host.
  * Restart the Gateway / macOS menubar app.


### 

​

2) Verify discovery (optional)

From the gateway machine:

Copy
[code]
    dns-sd -B _openclaw-gw._tcp local.
    
[/code]

More debugging notes: [Bonjour](</gateway/bonjour>).

#### 

​

Tailnet (Vienna ⇄ London) discovery via unicast DNS-SD

Android NSD/mDNS discovery won’t cross networks. If your Android node and the gateway are on different networks but connected via Tailscale, use Wide-Area Bonjour / unicast DNS-SD instead:

  1. Set up a DNS-SD zone (example `openclaw.internal.`) on the gateway host and publish `_openclaw-gw._tcp` records.
  2. Configure Tailscale split DNS for your chosen domain pointing at that DNS server.

Details and example CoreDNS config: [Bonjour](</gateway/bonjour>).

### 

​

3) Connect from Android

In the Android app:

  * The app keeps its gateway connection alive via a **foreground service** (persistent notification).
  * Open the **Connect** tab.
  * Use **Setup Code** or **Manual** mode.
  * If discovery is blocked, use manual host/port (and TLS/token/password when required) in **Advanced controls**.

After the first successful pairing, Android auto-reconnects on launch:

  * Manual endpoint (if enabled), otherwise
  * The last discovered gateway (best-effort).


### 

​

4) Approve pairing (CLI)

On the gateway machine:

Copy
[code]
    openclaw devices list
    openclaw devices approve <requestId>
    openclaw devices reject <requestId>
    
[/code]

Pairing details: [Pairing](</channels/pairing>).

### 

​

5) Verify the node is connected

  * Via nodes status:

Copy
[code]openclaw nodes status
        
[/code]

  * Via Gateway:

Copy
[code]openclaw gateway call node.list --params "{}"
        
[/code]


### 

​

6) Chat + history

The Android Chat tab supports session selection (default `main`, plus other existing sessions):

  * History: `chat.history`
  * Send: `chat.send`
  * Push updates (best-effort): `chat.subscribe` → `event:"chat"`


### 

​

7) Canvas + camera

#### 

​

Gateway Canvas Host (recommended for web content)

If you want the node to show real HTML/CSS/JS that the agent can edit on disk, point the node at the Gateway canvas host. Note: nodes load canvas from the Gateway HTTP server (same port as `gateway.port`, default `18789`).

  1. Create `~/.openclaw/workspace/canvas/index.html` on the gateway host.
  2. Navigate the node to it (LAN):


Copy
[code]
    openclaw nodes invoke --node "<Android Node>" --command canvas.navigate --params '{"url":"http://<gateway-hostname>.local:18789/__openclaw__/canvas/"}'
    
[/code]

Tailnet (optional): if both devices are on Tailscale, use a MagicDNS name or tailnet IP instead of `.local`, e.g. `http://<gateway-magicdns>:18789/__openclaw__/canvas/`. This server injects a live-reload client into HTML and reloads on file changes. The A2UI host lives at `http://<gateway-host>:18789/__openclaw__/a2ui/`. Canvas commands (foreground only):

  * `canvas.eval`, `canvas.snapshot`, `canvas.navigate` (use `{"url":""}` or `{"url":"/"}` to return to the default scaffold). `canvas.snapshot` returns `{ format, base64 }` (default `format="jpeg"`).
  * A2UI: `canvas.a2ui.push`, `canvas.a2ui.reset` (`canvas.a2ui.pushJSONL` legacy alias)

Camera commands (foreground only; permission-gated):

  * `camera.snap` (jpg)
  * `camera.clip` (mp4)

See [Camera node](</nodes/camera>) for parameters and CLI helpers.

### 

​

8) Voice + expanded Android command surface

  * Voice: Android uses a single mic on/off flow in the Voice tab with transcript capture and TTS playback (ElevenLabs when configured, system TTS fallback). Voice stops when the app leaves the foreground.
  * Voice wake/talk-mode toggles are currently removed from Android UX/runtime.
  * Additional Android command families (availability depends on device + permissions):
    * `device.status`, `device.info`, `device.permissions`, `device.health`
    * `notifications.list`, `notifications.actions`
    * `photos.latest`
    * `contacts.search`, `contacts.add`
    * `calendar.events`, `calendar.add`
    * `callLog.search`
    * `sms.search`
    * `motion.activity`, `motion.pedometer`


[Windows](</platforms/windows>)[iOS App](</platforms/ios>)

⌘I
---
title: macOS Dev Setup
source_url: https://docs.openclaw.ai/platforms/mac/dev-setup
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

macOS companion app

macOS Dev Setup

# 

​

macOS Developer Setup

This guide covers the necessary steps to build and run the OpenClaw macOS application from source.

## 

​

Prerequisites

Before building the app, ensure you have the following installed:

  1. **Xcode 26.2+** : Required for Swift development.
  2. **Node.js 24 & pnpm**: Recommended for the gateway, CLI, and packaging scripts. Node 22 LTS, currently `22.16+`, remains supported for compatibility.


## 

​

1\. Install Dependencies

Install the project-wide dependencies:

Copy
[code]
    pnpm install
    
[/code]

## 

​

2\. Build and Package the App

To build the macOS app and package it into `dist/OpenClaw.app`, run:

Copy
[code]
    ./scripts/package-mac-app.sh
    
[/code]

If you don’t have an Apple Developer ID certificate, the script will automatically use **ad-hoc signing** (`-`). For dev run modes, signing flags, and Team ID troubleshooting, see the macOS app README: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Note** : Ad-hoc signed apps may trigger security prompts. If the app crashes immediately with “Abort trap 6”, see the Troubleshooting section.

## 

​

3\. Install the CLI

The macOS app expects a global `openclaw` CLI install to manage background tasks. **To install it (recommended):**

  1. Open the OpenClaw app.
  2. Go to the **General** settings tab.
  3. Click **“Install CLI”**.

Alternatively, install it manually:

Copy
[code]
    npm install -g openclaw@<version>
    
[/code]

## 

​

Troubleshooting

### 

​

Build Fails: Toolchain or SDK Mismatch

The macOS app build expects the latest macOS SDK and Swift 6.2 toolchain. **System dependencies (required):**

  * **Latest macOS version available in Software Update** (required by Xcode 26.2 SDKs)
  * **Xcode 26.2** (Swift 6.2 toolchain)

**Checks:**

Copy
[code]
    xcodebuild -version
    xcrun swift --version
    
[/code]

If versions don’t match, update macOS/Xcode and re-run the build.

### 

​

App Crashes on Permission Grant

If the app crashes when you try to allow **Speech Recognition** or **Microphone** access, it may be due to a corrupted TCC cache or signature mismatch. **Fix:**

  1. Reset the TCC permissions:

Copy
[code]tccutil reset All ai.openclaw.mac.debug
         
[/code]

  2. If that fails, change the `BUNDLE_ID` temporarily in [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) to force a “clean slate” from macOS.


### 

​

Gateway “Starting…” indefinitely

If the gateway status stays on “Starting…”, check if a zombie process is holding the port:

Copy
[code]
    openclaw gateway status
    openclaw gateway stop
    
    # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:
    lsof -nP -iTCP:18789 -sTCP:LISTEN
    
[/code]

If a manual run is holding the port, stop that process (Ctrl+C). As a last resort, kill the PID you found above.

[iOS App](</platforms/ios>)[Menu Bar](</platforms/mac/menu-bar>)

⌘I
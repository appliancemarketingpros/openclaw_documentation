---
title: Quick live smokes and the Android node sweep
source_url: https://docs.openclaw.ai/help/testing-live/quick-smokes
scraped_at: 2026-09-28
---

ContributingTesting and CI

## Live: local smoke commands

Export the needed provider key in the process environment before ad hoc live checks.

Safe media smoke:

bashCopy code
[code]
    pnpm openclaw infer tts convert --local --json \  --text "OpenClaw live smoke." \  --output /tmp/openclaw-live-smoke.mp3
[/code]

Safe voice-call readiness smoke:

bashCopy code
[code]
    pnpm openclaw voicecall setup --jsonpnpm openclaw voicecall smoke --to "+15555550123"
[/code]

`voicecall smoke` is a dry run unless `--yes` is also present; use `--yes` only when you intend to place a real call. For Twilio, Telnyx, and Plivo, a successful readiness check requires a public webhook URL - local/private loopback URLs are rejected because those providers cannot reach them.

## Live: Android node capability sweep

  * Test: `src/gateway/android-node.capabilities.live.test.ts`
  * Script: `pnpm android:test:integration`
  * Goal: invoke **every command currently advertised** by a connected Android node and assert command contract behavior.
  * Scope: 
    * Preconditioned/manual setup (the suite does not install/run/pair the app).
    * Command-by-command gateway `node.invoke` validation for the selected Android node.
  * Required pre-setup: 
    * Android app already connected + paired to the gateway.
    * App kept in foreground.
    * Permissions/capture consent granted for capabilities you expect to pass.
  * Optional target overrides: 
    * `OPENCLAW_ANDROID_NODE_ID` or `OPENCLAW_ANDROID_NODE_NAME`.
    * `OPENCLAW_ANDROID_GATEWAY_URL` / `OPENCLAW_ANDROID_GATEWAY_TOKEN` / `OPENCLAW_ANDROID_GATEWAY_PASSWORD`.
  * Full Android setup details: [Android App](</platforms/android>)


Was this useful?YesNo

Open issue
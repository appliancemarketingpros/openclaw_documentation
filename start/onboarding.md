---
title: Onboarding (macOS app)
source_url: https://docs.openclaw.ai/start/onboarding
scraped_at: 2026-06-08
---

Get startedFirst steps

This doc describes the **current** first-run setup flow. The goal is a smooth "day 0" experience: pick where the Gateway runs, connect auth, run the wizard, and let the agent bootstrap itself. For a general overview of onboarding paths, see [Onboarding Overview](</start/onboarding-overview>).

* ### Approve macOS warning

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Approve find local networks

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Welcome and security notice

Read the security notice displayed and decide accordingly ![](/assets/macos-onboarding/03-security-notice.png)

Security trust model:

  * By default, OpenClaw is a personal agent: one trusted operator boundary.
  * Shared/multi-user setups require lock-down (split trust boundaries, keep tool access minimal, and follow [Security](</gateway/security>)).
  * Local onboarding now defaults new configs to `tools.profile: "coding"` so fresh local setups keep filesystem/runtime tools without forcing the unrestricted `full` profile.
  * If hooks/webhooks or other untrusted content feeds are enabled, use a strong modern model tier and keep strict tool policy/sandboxing.


* ### Local vs Remote

![](/assets/macos-onboarding/04-choose-gateway.png)

Where does the **Gateway** run?

  * **This Mac (Local only):** onboarding can configure auth and write credentials locally.
  * **Remote (over SSH/Tailnet):** onboarding does **not** configure local auth; credentials must exist on the gateway host. The remote gateway token field stores the token used by the macOS app to connect to that Gateway; existing non-plaintext `gateway.remote.token` values are preserved until you replace them.
  * **Configure later:** skip setup and leave the app unconfigured.


* ### Permissions

Choose what permissions do you want to give OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

Onboarding requests TCC permissions needed for:

  * Automation (AppleScript)
  * Notifications
  * Accessibility
  * Screen Recording
  * Microphone
  * Speech Recognition
  * Camera
  * Location


* ### CLI

* ### Onboarding Chat (dedicated session)

After setup, the app opens a dedicated onboarding chat session so the agent can introduce itself and guide next steps. This keeps first-run guidance separate from your normal conversation. See [Bootstrapping](</start/bootstrapping>) for what happens on the gateway host during the first agent run.

## Related

  * [Onboarding overview](</start/onboarding-overview>)
  * [Getting started](</start/getting-started>)


Was this useful?YesNo

Open issue
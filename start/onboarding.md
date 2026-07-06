---
title: Onboarding (macOS app)
source_url: https://docs.openclaw.ai/start/onboarding
scraped_at: 2026-07-06
---

Get startedFirst steps

The macOS app's first-run flow: pick where the Gateway runs, connect a verified AI backend, grant permissions, and hand off to the agent's own bootstrap ritual. For CLI onboarding and a comparison of both paths, see [Onboarding Overview](</start/onboarding-overview>).

* ### Approve macOS warning

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Approve find local networks

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Welcome and security notice

Read the security notice displayed and decide accordingly ![](/assets/macos-onboarding/03-security-notice.png)

Security trust model:

  * By default, OpenClaw is a personal agent: one trusted operator boundary.
  * Shared/multi-user setups need lock-down: split trust boundaries, keep tool access minimal, and follow [Security](</gateway/security>).
  * Local onboarding defaults new configs to `tools.profile: "coding"` so fresh setups keep filesystem/runtime tools without the unrestricted `full` profile.
  * If hooks/webhooks or other untrusted content feeds are enabled, use a strong modern model tier and keep strict tool policy/sandboxing.


* ### Local vs Remote

![](/assets/macos-onboarding/04-choose-gateway.png)

Where does the **Gateway** run?

  * **This Mac (Local only):** onboarding configures auth and writes credentials locally.
  * **Remote (over SSH/Tailnet):** onboarding does **not** configure local auth; credentials must already exist on the gateway host. The remote gateway token field stores the token the macOS app uses to connect to that Gateway; existing `gateway.remote.token` SecretRef values are preserved until you replace them.
  * **Configure later:** skip setup and leave the app unconfigured.


* ### CLI

Local setup installs the global `openclaw` CLI via npm, pnpm, or bun, preferring npm first. Node remains the recommended runtime for the Gateway itself. Existing compatible installations are reused.

* ### Connect your AI

Once the Gateway is ready, onboarding looks for AI access you already have: a Claude Code, Codex, or Gemini CLI login, or `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`. The best option is tested with a real completion and only saved after it answers; when a test fails the app automatically tries the next option and shows why the previous one failed. If several options are found you can switch between them before continuing.

If nothing is found (or nothing works), a manual step accepts an API key for Anthropic, OpenAI, or Google, verifies it the same way, and stores it as an auth profile. Next remains locked until one backend has passed its live test, so the first agent chat can never start without working inference. The Crestodian chat stays available from this page (and later under Settings → Crestodian) for help in plain language.

Configure Later skips this step.

* ### Permissions

Choose what permissions do you want to give OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

Onboarding requests TCC permissions for: Automation (AppleScript), Notifications, Accessibility, Screen Recording, Microphone, Speech Recognition, Camera, and Location.

* ### Onboarding Chat (dedicated session)

After setup, the app opens a separate agent onboarding chat so the agent can introduce itself and guide next steps without mixing that exchange into the normal conversation history. This follows the Crestodian setup conversation; it does not replace it. See [Bootstrapping](</start/bootstrapping>) for what happens on the gateway host during the agent's first real turn.

## Related

  * [Onboarding overview](</start/onboarding-overview>)
  * [Getting started](</start/getting-started>)


Was this useful?YesNo

Open issue